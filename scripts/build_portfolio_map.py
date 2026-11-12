#!/usr/bin/env python3
"""Build the public portfolio index without upgrading inherited evidence."""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build(root: Path) -> dict:
    with (root / 'discovery/catalog.csv').open(newline='') as stream:
        catalog = list(csv.DictReader(stream))
    projects = []
    for row in catalog:
        project_id = row['id']
        brief = root / 'projects' / (project_id + '.md')
        signals = root / 'signals' / (project_id + '.md')
        deep_links = []
        for path in sorted((root / 'deep-dives').rglob('*.md')):
            if f'projects/{project_id}.md' in path.read_text():
                deep_links.append(str(path.relative_to(root)))
        projects.append(dict(id=project_id, name=row['name'], domain=row['domain'],
                             recorded_status=row['status'], primary_url=row['url'],
                             repository_url=row['repo_url'] or None,
                             recorded_org_evidence=row['org_unit'],
                             brief=str(brief.relative_to(root)) if brief.exists() else None,
                             signals=str(signals.relative_to(root)) if signals.exists() else None,
                             deep_dive_mentions=deep_links,
                             catalog_notes=row['notes']))
    if len({p['id'] for p in projects}) != len(projects):
        raise ValueError('duplicate catalog identifiers')
    ledger = (root / 'docs/public-research-sources.md').read_text()
    source_records = {}
    section = ''
    context = []
    for line in ledger.splitlines():
        if line.startswith('#'):
            section = line
            context = []
        match = re.match(r'- ([A-Z]+\d+)\s*[—–-]\s*', line)
        if match:
            source_records[match[1]] = dict(ledger_entry=line,
                urls=re.findall(r'https?://[^\s)]+', line),
                ledger_section=section, retrieval_context='\n'.join(context).strip())
        elif line.strip() and not line.startswith('#'):
            context.append(line)
    relationships = []
    for line in (root / 'docs/research-relationships.md').read_text().splitlines():
        if not re.match(r'\| R\d+ \|', line):
            continue
        cells = [cell.strip() for cell in line.strip('|').split('|')]
        if len(cells) != 7:
            raise ValueError(f'malformed relationship: {line}')
        rid, subject, relation, target, evidence, source_text, boundary = cells
        if evidence not in {'DIRECT', 'INFERRED', 'UNKNOWN'}:
            raise ValueError(f'{rid}: unsupported evidence state')
        # Preserve source expressions (including ranges) and complete ledger rows.
        ids = re.findall(r'[A-Z]+\d+', source_text)
        for first, last in re.findall(r'([A-Z]+\d+)–([A-Z]+\d+)', source_text):
            a, b = re.match(r'([A-Z]+)(\d+)', first), re.match(r'([A-Z]+)(\d+)', last)
            if a[1] == b[1]:
                ids.extend(f'{a[1]}{number:02d}' for number in range(int(a[2]), int(b[2]) + 1))
        ids = sorted(set(ids))
        missing = [sid for sid in ids if sid not in source_records]
        if missing:
            raise ValueError(f'{rid}: missing ledger source {missing}')
        relationships.append(dict(id=rid, subject=subject, relation=relation, object=target,
            evidence=evidence, source_expression=source_text,
            sources={sid: source_records[sid] for sid in ids}, limitation=boundary))
    return dict(schema_version=1,
        boundary='Generated navigation over the declared catalog and selected relationship ledger. '
                 'Not a census of ORNL, a live system map, or a fresh source verification. '
                 'Briefs, signals, and deep-dive mentions indicate files, not equal research depth. '
                 'Source retrieval dates remain in their original ledger entries.',
        additional_research_relationships=json.loads((root / 'docs/portfolio-expansion-2026-11-10/connections.json').read_text())['relationships'],
        research_chapters=[dict(path=str(path.relative_to(root)),
            title=path.read_text().splitlines()[0].lstrip('# '),
            source_urls=sorted(set(re.findall(r'https?://[^\s)]+', path.read_text()))))
            for path in sorted((root / 'docs/portfolio-expansion-2026-11-10').glob('*.md'))
            if path.stem in {'materials-biology', 'energy-earth', 'computing-instruments', 'geospatial-uncertainty'}],
        projects=projects, relationships=relationships,
        domains={domain: [p['id'] for p in projects if p['domain'] == domain]
                 for domain in sorted({p['domain'] for p in projects})})


def markdown(data: dict) -> str:
    lines = ['# ORNL public technology portfolio map', '',
        data['boundary'], '',
        f"This navigation covers **{len(data['projects'])} catalog entries**, **{len(data['relationships'])} inherited relationships**, and **{len(data['additional_research_relationships'])} new research propositions**. "
        'The [new technical research](portfolio-expansion-2026-11-10/README.md) adds cross-domain detail outside this inherited catalog. '
        'The [JSON map](portfolio-map.json) preserves every catalog record and original source-ledger text.', '',
        'Rebuild with `python3 scripts/build_portfolio_map.py`; check with `python3 scripts/build_portfolio_map.py --check`.', '',
        '## Read across domains', '',
        '[Lab tree](../LAB-TREE.md) | [Research guide](public-research-guide.md) | '
        '[Relationship propositions](research-relationships.md) | [Coverage and limits](coverage-matrix.md)', '']
    lines += ['## The whole catalog at a glance', '', 'These are research categories, not an ORNL reporting hierarchy.', '', '```mermaid', 'flowchart LR', '  atlas[\"Public technology catalog\"]']
    for index, (domain, ids) in enumerate(data['domains'].items()):
        lines.append(f'  atlas --> d{index}[\"{domain}: {len(ids)} entries\"]')
    lines += ['```', '']
    for domain, ids in data['domains'].items():
        lines += [f'## {domain}', '', '| Project | Recorded status | Reading paths |', '|---|---|---|']
        for row in data['projects']:
            if row['id'] not in ids:
                continue
            readings = []
            if row['brief']:
                readings.append(f"[brief](../{row['brief']})")
            else:
                readings.append('no brief; catalog stub')
            if row['signals']:
                readings.append(f"[public traces](../{row['signals']})")
            if row['deep_dive_mentions']:
                readings.append(f"[case-study mention](../{row['deep_dive_mentions'][0]})")
            name = row['name'].replace('|', '/')
            lines.append(f"| [{name}]({row['primary_url']}) | {row['recorded_status']} | {'; '.join(readings)} |")
        lines.append('')
    lines += ['## Reading the connections', '',
        'The JSON relationship records preserve `DIRECT`, `INFERRED`, and `UNKNOWN` separately, '
        'including source dates and limitations. An unknown link is a question, not a dependency. '
        'A case-study mention does not establish that a project was deeply reconstructed or integrated with its neighbors.', '']
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = build(ROOT)
    outputs = {ROOT / 'docs/portfolio-map.json': json.dumps(data, indent=2, ensure_ascii=False) + '\n',
               ROOT / 'docs/portfolio-map.md': markdown(data)}
    for path, text in outputs.items():
        if args.check:
            if not path.exists() or path.read_text() != text:
                raise SystemExit(f'portfolio map stale: {path.relative_to(ROOT)}')
        else:
            path.write_text(text)
    print(f"portfolio map {'valid' if args.check else 'built'}: {len(data['projects'])} projects, {len(data['relationships'])} relationships, {len(data['domains'])} domains")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
