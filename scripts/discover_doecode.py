#!/usr/bin/env python3
"""Read the documented public DOE CODE search API; retain software metadata only."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
from urllib.parse import urlencode
from discover_software import get

DOCS = 'https://www.osti.gov/doecodeapi/markdown/Search.md'


def org_names(value):
    return [row.get('organization_name', '') if isinstance(row, dict) else str(row) for row in (value or [])]


def collect():
    now = datetime.now(timezone.utc).isoformat()
    records, sources = [], []
    offset, total, excluded = 0, None, 0
    error = None
    complete = False
    while total is None or offset < total:
        url = 'https://www.osti.gov/doecodeapi/services/search?' + urlencode({'all_fields': '"Oak Ridge National Laboratory"', 'rows': 100, 'start': offset})
        try:
            payload, digest = get(url)
            total = payload['num_found']
            rows = payload['docs']
            sid = f'doecode-search-{offset}'
            sources.append(dict(id=sid, url=url, sha256=digest, fetched_at=now, kind='public_software_record_search', documentation=DOCS))
            for row in rows:
                # Public bibliographic search can refer to controlled artifacts.
                # Do not retain or follow records carrying a restricted-use flag.
                if row.get('official_use_only') or row.get('is_limited'):
                    excluded += 1
                    continue
                research = org_names(row.get('research_organizations'))
                contributing = org_names(row.get('contributing_organizations'))
                developing = org_names(row.get('developing_organizations'))
                direct = any('oak ridge' in name.casefold() for name in research + contributing + developing)
                records.append(dict(code_id=str(row['code_id']), name=row['software_title'],
                    url=f"https://www.osti.gov/doecode/biblio/{row['code_id']}",
                    repository_url=row.get('repository_link') or None,
                    description=row.get('description') or '', languages=row.get('programming_languages') or [],
                    licenses=row.get('licenses') or [], project_type=row.get('project_type'),
                    release_date=row.get('release_date'), version=row.get('version_number'), doi=row.get('doi'),
                    research_organizations=research, contributing_organizations=contributing,
                    developing_organizations=developing, sponsoring_organizations=org_names(row.get('sponsoring_organizations')),
                    source_id=sid, affiliation='explicit_organization_metadata' if direct else 'unverified_search_hit',
                    limitation='Software record only. A search match is not ORNL attribution; versions are not unique projects; closed-source metadata does not grant source access.'))
            offset += len(rows)
            if not rows:
                complete = offset >= total
                if not complete:
                    error = 'empty page before advertised total'
                break
            if offset >= total:
                complete = True
                break
        except (OSError, ValueError, KeyError) as exc:
            error = f'{type(exc).__name__}: {exc}'
            break
    return dict(schema_version=1, collected_at=now, sources=sources, records=records,
        searches=[dict(surface='DOE CODE documented search', query='"Oak Ridge National Laboratory"',
            documentation=DOCS, advertised_total=total, rows_examined=offset, retained=len(records),
            excluded_restricted_flags=excluded, complete_for_response=complete, error=error,
            scope='All-fields software metadata search. Unverified affiliation matches and software versions remain distinct.')])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    data = collect()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('x') as stream:
        json.dump(data, stream, indent=2, ensure_ascii=False)
        stream.write('\n')
    print(json.dumps(data['searches'], indent=2))


if __name__ == '__main__':
    main()
