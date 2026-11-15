#!/usr/bin/env python3
"""Build and query a disposable, offline SQLite index of the public research files."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = 1
BOUNDARY = (
    'Retrieval of recorded research, not fresh source verification. Catalog status, '
    'editorial priority, source confidence and experiment depth are separate. '
    'Text matches are navigation, not evidence of a relationship. Local designs '
    'are not ORNL implementations. Follow the returned paths and primary sources.'
)
COLLECTIONS = ('sources', 'projects', 'facilities', 'software', 'roles', 'edges')
TEXT_ROOTS = ('projects', 'signals', 'deep-dives', 'lessons', 'connections', 'docs', 'verification',
              'atlas/guide', 'atlas/projects', 'atlas/research', 'atlas/sources', 'atlas/labs')
ROOT_DOCS = ('README.md', 'INDEX.md', 'LAB-TREE.md', 'RULES.md', 'GOAL.md', 'atlas/README.md')


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def local_file(root, value):
    if not isinstance(value, str) or not value:
        raise ValueError('expected a repository-relative file path')
    path = root / value
    if Path(value).is_absolute() or not path.resolve().is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError(f'missing or outside-repository file: {value}')
    return path


def source_paths(root):
    paths = {root / p for p in ROOT_DOCS if (root / p).is_file()}
    for folder in TEXT_ROOTS:
        paths.update((root / folder).rglob('*.md'))
    paths.update((root / 'cards').glob('*.json'))
    paths.update(root / f'atlas/registry/{name}.json' for name in COLLECTIONS)
    paths.update(root / p for p in ('discovery/catalog.csv', 'discovery/lanes.csv',
                                  'discovery/registry-links.json'))
    if (root / 'scripts/research_library.py').is_file():
        paths.add(root / 'scripts/research_library.py')
    # Include only referenced machine-readable results, never execute experiments.
    for card in (root / 'cards').glob('*.json'):
        data = read_json(card)
        for path in data.get('supporting_paths', []):
            paths.add(local_file(root, path))
        result = data.get('experiment', {}).get('results_path')
        if result:
            paths.add(local_file(root, result))
    for path in paths:
        local_file(root, path.relative_to(root).as_posix())
    return sorted(paths)


def manifest(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in source_paths(root)}


def csv_by_id(path):
    with path.open(newline='', encoding='utf-8') as stream:
        rows = list(csv.DictReader(stream))
    result = {row['id']: row for row in rows}
    if len(result) != len(rows) or '' in result:
        raise ValueError(f'duplicate or empty ID in {path.name}')
    return result


def validate_card(root, card, catalog, path):
    required = ('id', 'title', 'problem', 'mechanism', 'finding', 'adaptation')
    if card.get('schema_version') != 1 or any(not isinstance(card.get(k), str) or not card[k].strip() for k in required):
        raise ValueError(f'{path}: missing card text or unsupported schema')
    if card['id'] != path.stem or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', card['id']):
        raise ValueError(f'{path}: card ID must match its slug filename')
    for key in ('project_ids', 'source_urls', 'code_refs', 'supporting_paths', 'unknowns'):
        if not isinstance(card.get(key), list) or any(not isinstance(x, str) or not x for x in card[key]):
            raise ValueError(f'{path}: {key} must be a list of strings')
    if not card['project_ids'] or not set(card['project_ids']) <= catalog.keys():
        raise ValueError(f'{path}: unknown or missing catalog project')
    if not card['source_urls'] or not card['supporting_paths'] or not card['unknowns']:
        raise ValueError(f'{path}: sources, local evidence and unknowns required')
    for url in card['source_urls'] + card['code_refs']:
        if not re.match(r'https?://[^/\s]+', url):
            raise ValueError(f'{path}: invalid source URL')
    for url in card['code_refs']:
        if not re.search(r'/(blob|commit)/[0-9a-f]{40}(?:/|#|$)', url):
            raise ValueError(f'{path}: code reference must pin a full commit')
    for value in card['supporting_paths']:
        local_file(root, value)
    level = card.get('evidence_level')
    if level not in {'documented', 'code-inspected', 'experiment-recorded'}:
        raise ValueError(f'{path}: invalid evidence level')
    experiment = card.get('experiment')
    if not isinstance(experiment, dict) or not isinstance(experiment.get('limitations'), str) or not experiment['limitations'].strip():
        raise ValueError(f'{path}: experiment limitations required')
    if experiment.get('status') not in {'not-run', 'recorded'}:
        raise ValueError(f'{path}: invalid experiment status')
    if (level == 'experiment-recorded') != (experiment['status'] == 'recorded'):
        raise ValueError(f'{path}: experiment status and evidence level disagree')
    if level == 'code-inspected' and not card['code_refs']:
        raise ValueError(f'{path}: code-inspected card needs pinned code')
    if experiment['status'] == 'recorded':
        if any(not isinstance(experiment.get(k), str) or not experiment[k].strip()
               for k in ('revision', 'command', 'results_path')):
            raise ValueError(f'{path}: recorded experiment needs revision, command and results')
        local_file(root, experiment['results_path'])


def sections(text):
    """Keep headings, source text and original line numbers; ignore fenced headings."""
    start, title, lines, fence = 1, 'Introduction', [], None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            if fence is None:
                fence = marker[1][0]
            elif marker[1][0] == fence:
                fence = None
        heading = re.match(r'^#{1,6}\s+(.+)', line) if fence is None else None
        if heading and lines:
            yield title, start, '\n'.join(lines)
            lines = []
        if heading:
            title, start = heading[1], number
        lines.append(line)
    if lines:
        yield title, start, '\n'.join(lines)


def collect(root):
    catalog = csv_by_id(root / 'discovery/catalog.csv')
    lanes = csv_by_id(root / 'discovery/lanes.csv')
    if catalog.keys() != lanes.keys():
        raise ValueError('lane IDs must match catalog exactly')
    projects = {key: dict(row, lanes=lanes[key]['lanes'].split(';'), tier=lanes[key]['tier'],
                          priority_reason=lanes[key]['why']) for key, row in catalog.items()}
    for row in projects.values():
        if row['tier'] not in {'deep', 'lead', 'pool'} or not set(row['lanes']) <= {'none', 'cybersecurity', 'software-engineering', 'ai-agents', 'linux-infra'}:
            raise ValueError(f'invalid lane/tier for {row["id"]}')
    registry = {}
    edges = []
    for collection in COLLECTIONS:
        rows = read_json(root / f'atlas/registry/{collection}.json')[collection]
        if collection == 'edges':
            edges = rows
        else:
            for row in rows:
                if row['id'] in registry:
                    raise ValueError(f'duplicate registry ID {row["id"]}')
                registry[row['id']] = dict(row, collection=collection)
    for row in registry.values():
        for field in ('source_ids', 'facility_ids', 'software_ids', 'role_ids'):
            for target in row.get(field, []):
                if target not in registry:
                    raise ValueError(f'missing registry target {target}')
    for edge in edges:
        for target in [edge['from'], edge['to'], *edge['source_ids']]:
            if target not in registry:
                raise ValueError(f'missing edge target {target}')
    links = read_json(root / 'discovery/registry-links.json')['links']
    aliases = {}
    for link in links:
        rid, pid = link['registry_id'], link['project_id']
        if rid not in registry or pid not in projects or rid in aliases or not link.get('basis'):
            raise ValueError(f'invalid or duplicate registry crosswalk: {link}')
        aliases[rid] = pid
    records = []

    def add(key, kind, title, path, body, ids=(), payload=None, line=1):
        records.append(dict(id=key, kind=kind, title=title, path=path, line=line,
                            project_ids=sorted(set(ids)), body=body, payload=payload or {}))

    for key, row in projects.items():
        add(f'catalog:{key}', 'catalog', row['name'], 'discovery/catalog.csv',
            json.dumps(row, ensure_ascii=False), [key], row)
    for key, row in registry.items():
        add(f'registry:{key}', 'registry', row.get('title', row.get('name', key)),
            f'atlas/registry/{row["collection"]}.json', json.dumps(row, ensure_ascii=False),
            [aliases[key]] if key in aliases else [], row)
    for i, edge in enumerate(edges):
        add(f'edge:{i}', 'relationship', edge['relation'], 'atlas/registry/edges.json',
            json.dumps(edge, ensure_ascii=False),
            [aliases[k] for k in (edge['from'], edge['to']) if k in aliases], edge)
    lab_projects = {}
    for path in sorted((root / 'cards').glob('*.json')):
        card = read_json(path)
        validate_card(root, card, catalog, path)
        for supporting in card['supporting_paths']:
            if supporting.startswith('atlas/labs/'):
                lab_projects.setdefault(supporting, set()).update(card['project_ids'])
        add(f'card:{card["id"]}', 'card', card['title'], path.relative_to(root).as_posix(),
            json.dumps(card, ensure_ascii=False), card['project_ids'], card)
    for path in source_paths(root):
        relative = path.relative_to(root).as_posix()
        if path.suffix != '.md':
            continue
        kind = 'lab' if relative.startswith('atlas/labs/') else 'document'
        for title, line, body in sections(path.read_text(encoding='utf-8')):
            # Lexical project associations are only navigation, never graph edges.
            ids = set(lab_projects.get(relative, ()))
            ids.update(key for key, row in projects.items()
                   if relative in {f'projects/{key}.md', f'signals/{key}.md'}
                   or re.search(r'(?<!\w)' + re.escape(row['name']) + r'(?!\w)', body,
                                0 if row['name'].isupper() else re.I)
                   or f'projects/{key}.md' in body)
            add(f'text:{relative}:{line}', kind, title, relative, body, ids, line=line)
    return projects, records, links


def build(root, database):
    fingerprint = manifest(root)
    projects, records, links = collect(root)
    if manifest(root) != fingerprint:
        raise ValueError('research files changed during collection; retry build after edits finish')
    database.parent.mkdir(parents=True, exist_ok=True)
    if database.exists():
        with sqlite3.connect(database.as_uri() + '?mode=ro', uri=True) as old:
            if old.execute('PRAGMA application_id').fetchone()[0] != 1330794060:
                raise ValueError('refusing to overwrite a database not created by research_library.py')
    with tempfile.NamedTemporaryFile(dir=database.parent, suffix='.sqlite3', delete=False) as handle:
        temporary = Path(handle.name)
    try:
        with sqlite3.connect(temporary) as db:
            db.executescript('''
                PRAGMA application_id=1330794060;
                CREATE TABLE meta(key TEXT PRIMARY KEY, value TEXT NOT NULL);
                CREATE TABLE projects(id TEXT PRIMARY KEY, payload TEXT NOT NULL);
                CREATE TABLE records(id TEXT PRIMARY KEY, kind TEXT, title TEXT, path TEXT,
                    line INTEGER, payload TEXT, body TEXT);
                CREATE TABLE associations(record_id TEXT, project_id TEXT,
                    PRIMARY KEY(record_id, project_id));
                CREATE TABLE crosswalk(registry_id TEXT PRIMARY KEY, project_id TEXT, basis TEXT);
                CREATE VIRTUAL TABLE search_index USING fts5(title, body, tokenize='unicode61');
            ''')
            db.executemany('INSERT INTO meta VALUES (?,?)', [('version', str(VERSION)),
                ('manifest', json.dumps(fingerprint, sort_keys=True)), ('boundary', BOUNDARY)])
            db.executemany('INSERT INTO projects VALUES (?,?)',
                           [(key, json.dumps(row)) for key, row in projects.items()])
            for record in records:
                cursor = db.execute('INSERT INTO records VALUES (?,?,?,?,?,?,?)',
                    (record['id'], record['kind'], record['title'], record['path'], record['line'],
                     json.dumps(record['payload']), record['body']))
                db.execute('INSERT INTO search_index(rowid,title,body) VALUES (?,?,?)',
                           (cursor.lastrowid, record['title'], record['body']))
                db.executemany('INSERT INTO associations VALUES (?,?)',
                               [(record['id'], key) for key in record['project_ids']])
            db.executemany('INSERT INTO crosswalk VALUES (?,?,?)',
                [(x['registry_id'], x['project_id'], x['basis']) for x in links])
        temporary.replace(database)
    finally:
        temporary.unlink(missing_ok=True)
    return {'projects': len(projects), 'records': len(records), 'indexed_files': len(fingerprint)}


def open_current(root, database):
    if not database.is_file():
        raise ValueError('database missing; run build first')
    db = sqlite3.connect(database.as_uri() + '?mode=ro', uri=True)
    db.row_factory = sqlite3.Row
    try:
        if db.execute('PRAGMA application_id').fetchone()[0] != 1330794060:
            raise ValueError('not a research library database')
        meta = dict(db.execute('SELECT key,value FROM meta'))
        if meta.get('version') != str(VERSION) or json.loads(meta['manifest']) != manifest(root):
            raise ValueError('database stale; run build again')
        return db
    except (OSError, ValueError, KeyError, TypeError, sqlite3.Error):
        db.close()
        raise


def record_output(db, row):
    result = dict(row)
    if 'payload' in result:
        result['payload'] = json.loads(result['payload'])
    result['project_ids'] = [x[0] for x in db.execute(
        'SELECT project_id FROM associations WHERE record_id=? ORDER BY project_id', (row['id'],))]
    return result


def search(db, query, lane=None, tier=None, kind=None, limit=10):
    terms = list(dict.fromkeys(re.findall(r'[^\W_]+', query, re.UNICODE)))
    if not terms:
        raise ValueError('search needs at least one word')
    expression = ' OR '.join('"' + term + '"' for term in terms)
    sql = '''SELECT r.id,r.kind,r.title,r.path,r.line,
             snippet(search_index,1,'[',']',' ... ',48) AS excerpt
             FROM search_index JOIN records r ON r.rowid=search_index.rowid
             WHERE search_index MATCH ?'''
    params = [expression]
    if kind:
        sql += ' AND r.kind=?'
        params.append(kind)
    if lane or tier:
        sql += ''' AND EXISTS (SELECT 1 FROM associations a JOIN projects p ON p.id=a.project_id
                   WHERE a.record_id=r.id'''
        if tier:
            sql += " AND json_extract(p.payload,'$.tier')=?"
            params.append(tier)
        if lane:
            sql += " AND EXISTS (SELECT 1 FROM json_each(p.payload,'$.lanes') WHERE value=?)"
            params.append(lane)
        sql += ')'
    sql += ' ORDER BY bm25(search_index,3.0,1.0),r.id LIMIT ?'
    params.append(limit)
    return [record_output(db, row) for row in db.execute(sql, params)]


def project_packet(db, project_id):
    row = db.execute('SELECT payload FROM projects WHERE id=?', (project_id,)).fetchone()
    if row is None:
        raise ValueError(f'unknown catalog project: {project_id}')
    project = json.loads(row[0])
    links = [dict(x) for x in db.execute('SELECT * FROM crosswalk WHERE project_id=?', (project_id,))]
    linked = [x['registry_id'] for x in links]
    registry = {json.loads(r[0])['id']: json.loads(r[0]) for r in db.execute(
        "SELECT payload FROM records WHERE kind='registry'")}
    edges = [json.loads(r[0]) for r in db.execute("SELECT payload FROM records WHERE kind='relationship'")]
    edges = [e for e in edges if e['from'] in linked or e['to'] in linked]
    selected = set(linked)
    for edge in edges:
        selected.update([edge['from'], edge['to'], *edge['source_ids']])
    for key in list(selected):
        selected.update(registry[key].get('source_ids', []))
    # Cards also cite local experiment artifacts, which aren't executed or embedded.
    cards = [record_output(db, r)['payload'] for r in db.execute('''SELECT r.* FROM records r
        JOIN associations a ON a.record_id=r.id WHERE a.project_id=? AND r.kind='card' ORDER BY r.id''', (project_id,))]
    documents = [dict(r) for r in db.execute('''SELECT DISTINCT r.path,r.kind FROM records r
        JOIN associations a ON a.record_id=r.id WHERE a.project_id=? AND r.kind IN ('document','lab')
        ORDER BY r.path''', (project_id,))]
    return dict(project=project, crosswalk=links, cards=cards, documents=documents,
                registry_nodes=[registry[k] for k in sorted(selected)], typed_relationships=edges,
                missing_brief=not any(d['path'] == f'projects/{project_id}.md' for d in documents))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--db', type=Path, help='Generated database; defaults to ROOT/.cache/research-library.sqlite3')
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('build', 'check', 'stats'):
        commands.add_parser(name)
    find = commands.add_parser('search', help='Rank literal word matches; no network or semantic model')
    find.add_argument('query')
    find.add_argument('--lane', choices=('cybersecurity', 'software-engineering', 'ai-agents', 'linux-infra', 'none'))
    find.add_argument('--tier', choices=('deep', 'lead', 'pool'))
    find.add_argument('--kind', choices=('catalog', 'registry', 'relationship', 'card', 'document', 'lab'))
    find.add_argument('--limit', type=int, default=10)
    commands.add_parser('project').add_argument('project_id')
    args = parser.parse_args(argv)
    root = args.root.resolve()
    database = (args.db or root / '.cache/research-library.sqlite3').resolve()
    try:
        if args.command == 'build':
            result = build(root, database)
        else:
            db = open_current(root, database)
            try:
                if args.command == 'check':
                    result = {'status': 'current', 'integrity': db.execute('PRAGMA integrity_check').fetchone()[0]}
                    if result['integrity'] != 'ok':
                        raise ValueError('database integrity check failed')
                elif args.command == 'stats':
                    result = dict(projects=db.execute('SELECT count(*) FROM projects').fetchone()[0],
                        records_by_kind={r[0]: r[1] for r in db.execute('SELECT kind,count(*) FROM records GROUP BY kind')})
                elif args.command == 'project':
                    result = project_packet(db, args.project_id)
                else:
                    if not 1 <= args.limit <= 100:
                        raise ValueError('limit must be between 1 and 100')
                    result = search(db, args.query, args.lane, args.tier, args.kind, args.limit)
            finally:
                db.close()
        print(json.dumps({'schema_version': VERSION, 'boundary': BOUNDARY, 'result': result}, indent=2, ensure_ascii=False))
        return 0
    except (OSError, ValueError, KeyError, TypeError, sqlite3.Error) as exc:
        print(f'research library failed: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
