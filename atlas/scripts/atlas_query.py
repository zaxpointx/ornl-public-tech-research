#!/usr/bin/env python3
"""Read-only context packets from Atlas's public registry, without network calls."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = ('sources', 'projects', 'facilities', 'software', 'roles')
REFERENCE_FIELDS = ('source_ids', 'facility_ids', 'software_ids', 'role_ids')


def load_registry(root: Path) -> tuple[dict, list]:
    nodes = {}
    for collection in COLLECTIONS:
        for row in json.loads((root / 'registry' / f'{collection}.json').read_text())[collection]:
            if row['id'] in nodes:
                raise ValueError(f"duplicate registry ID: {row['id']}")
            nodes[row['id']] = dict(row, collection=collection)
    edges = json.loads((root / 'registry' / 'edges.json').read_text())['edges']
    for row in nodes.values():
        for field in REFERENCE_FIELDS:
            for target in row.get(field, []):
                if target not in nodes:
                    raise ValueError(f"{row['id']}: missing {field} target {target}")
    for edge in edges:
        for target in [edge['from'], edge['to'], *edge['source_ids']]:
            if target not in nodes:
                raise ValueError(f'missing edge target {target}')
    return nodes, edges


def context_packet(nodes: dict, edges: list, node_id: str) -> dict:
    if node_id not in nodes:
        raise ValueError(f'unknown node: {node_id}')
    node = nodes[node_id]
    related_edges = [e for e in edges if node_id in (e['from'], e['to'])]
    references = {field: node.get(field, []) for field in REFERENCE_FIELDS if node.get(field)}
    selected = {node_id}
    for values in references.values():
        selected.update(values)
    for edge in related_edges:
        selected.update([edge['from'], edge['to'], *edge['source_ids']])
    # Include evidence for each neighboring entity, but do not traverse its other links.
    for target in list(selected):
        selected.update(nodes[target].get('source_ids', []))
    sources = [nodes[key] for key in sorted(selected) if nodes[key]['collection'] == 'sources']
    unresolved = [s['id'] for s in sources if s.get('promotion') != 'verified']
    return {
        'schema_version': 1,
        'boundary': 'Public registry context only. Listed references do not prove integration. '
                    'Verified sources do not automatically verify every claim or relationship. '
                    'Local translations are Atlas designs, not ORNL implementations.',
        'node': node,
        'listed_references': references,
        'typed_relationships': related_edges,
        'neighbors': [nodes[key] for key in sorted(selected)
                      if key != node_id and nodes[key]['collection'] != 'sources'],
        'sources': sources,
        'unresolved_source_ids': unresolved,
    }


def search(nodes: dict, query: str) -> list:
    words = query.casefold().split()
    return [row for _, row in sorted(nodes.items())
            if all(word in json.dumps(row).casefold() for word in words)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--node', help='Export one node and its one-hop evidence neighborhood')
    group.add_argument('--search', help='Find registry records containing every search term')
    parser.add_argument('--root', type=Path, default=ROOT, help='Atlas checkout to read')
    args = parser.parse_args()
    try:
        nodes, edges = load_registry(args.root)
        result = context_packet(nodes, edges, args.node) if args.node else search(nodes, args.search)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'atlas query failed: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
