#!/usr/bin/env python3
"""Snapshot public software discovery metadata without credentials or code execution."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
CATALOG = 'ORNL/software-catalog'


def get(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'ORNL-public-research-atlas/1.0', 'Accept': 'application/json'})
    with urllib.request.urlopen(request, timeout=30) as response:
        body = response.read()
    return json.loads(body), hashlib.sha256(body).hexdigest()


def language(value):
    return value.get('name') if isinstance(value, dict) else value


def sanitize(row, source_id, full_name=None, indexed=False):
    """Allowlist project metadata; never retain contributor identities or account data."""
    name = full_name or row.get('full_name') or row.get('nameWithOwner')
    url = row.get('html_url') or row.get('url')
    if not name or not url or not url.startswith(('https://github.com/', 'https://code.ornl.gov/')):
        raise ValueError('not a public project locator')
    lic = row.get('licenseInfo') if indexed else row.get('license')
    license_name = lic.get('spdxId') or lic.get('spdx_id') or lic.get('name') if isinstance(lic, dict) else None
    return dict(full_name=name, name=row.get('name') or name.rsplit('/', 1)[-1], url=url,
        description=row.get('description') or '', language=language(row.get('primaryLanguage') if indexed else row.get('language')),
        license_metadata=license_name, archived=None if indexed else row.get('archived'),
        fork=bool(row.get('parent')) if indexed else row.get('fork'),
        topics=[] if indexed else row.get('topics', []), created_at=row.get('createdAt') if indexed else row.get('created_at'),
        pushed_at=None if indexed else row.get('pushed_at'),
        stars=None if indexed else row.get('stargazers_count'), source_id=source_id,
        evidence='index_lead' if indexed else 'live_repository_metadata',
        limitation='Metadata only. Code behavior, current affiliation, license text and reproducibility require review.')


def collect(orgs_extra=()):
    now = datetime.now(timezone.utc).isoformat()
    revision, _ = get(f'https://api.github.com/repos/{CATALOG}/commits/main')
    sha = revision['sha']
    base = f'https://raw.githubusercontent.com/{CATALOG}/{sha}/'
    sources, observations, searches = [], [], []
    for filename, field in [('explore/github-data/intReposInfo.json', 'github'), ('explore/github-data/intReposInfoGitlab.json', 'gitlab')]:
        url = base + filename
        payload, digest = get(url)
        sid = f'catalog-{field}-{sha}'
        sources.append(dict(id=sid, url=url, sha256=digest, fetched_at=now, kind='official_catalog_snapshot', revision=sha,
            limitation='Public catalog snapshot; listing does not verify every code artifact or current release.'))
        accepted = 0
        for key, row in payload['data'].items():
            try:
                observations.append(sanitize(row, sid, row.get('nameWithOwner') or key, indexed=True))
                accepted += 1
            except ValueError:
                continue
        searches.append(dict(surface=field+' catalog', url=url, records=accepted, complete_for_response=True,
            scope='All entries in this pinned index file, not all ORNL projects.'))
    config_url = base + '_explore/input_lists.json'
    config, digest = get(config_url)
    orgs = sorted(set(config['https://github.com']['orgs']) | set(orgs_extra), key=str.casefold)
    sources.append(dict(id='catalog-inputs-'+sha, url=config_url, sha256=digest, fetched_at=now, kind='discovery_scope', revision=sha))

    def enumerate_org(org):
        found, fetched = [], []
        error = None
        complete = False
        for page in range(1, 21):
            url = f'https://api.github.com/orgs/{urllib.parse.quote(org, safe="")}/repos?type=public&per_page=100&page={page}'
            try:
                rows, digest = get(url)
                if not isinstance(rows, list):
                    raise ValueError('expected public repository list')
                sid = f'github-{org.casefold()}-{page}'
                fetched.append(dict(id=sid, url=url, sha256=digest, fetched_at=now, kind='public_repository_listing', organization=org))
                for row in rows:
                    if row.get('private'):
                        continue
                    found.append(sanitize(row, sid))
                if len(rows) < 100:
                    complete = True
                    break
            except (OSError, ValueError, urllib.error.URLError) as exc:
                error = f'{type(exc).__name__}: {exc}'
                break  # No authentication, access-control bypass, or retry loop.
        return found, fetched, dict(surface='GitHub public organization listing', organization=org,
            records=len(found), pages_fetched=len(fetched), complete_for_response=complete,
            error=error, scope='Repositories visible anonymously in this exact organization, including forks and archives.')
    with ThreadPoolExecutor(max_workers=4) as pool:
        for found, fetched, search in pool.map(enumerate_org, orgs):
            observations.extend(found)
            sources.extend(fetched)
            searches.append(search)
    return dict(schema_version=1, collected_at=now, boundary='Public discovery metadata only. No source code installed or run; no credentials, user profiles or contributor records retained.',
        scope_basis='Official catalog input list plus organizations already represented in the curated project catalog.',
        sources=sources, searches=searches, observations=observations)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--extra-org', action='append', default=[])
    args = parser.parse_args()
    snapshot = collect(args.extra_org)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(snapshot, stream, indent=2, ensure_ascii=False)
        stream.write('\n')
    unique = {r['url'].rstrip('/').removesuffix('.git').casefold() for r in snapshot['observations']}
    print(json.dumps(dict(observations=len(snapshot['observations']), unique_repository_urls=len(unique),
        surfaces=len(snapshot['searches']), incomplete=[s for s in snapshot['searches'] if not s['complete_for_response']]), indent=2))


if __name__ == '__main__':
    main()
