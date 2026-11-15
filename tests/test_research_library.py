"""Behavioral checks for offline retrieval and evidence-preserving joins."""
import copy
import csv
import importlib.util
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('research_library', ROOT / 'scripts/research_library.py')
library = importlib.util.module_from_spec(spec)
spec.loader.exec_module(library)


class LibraryTests(unittest.TestCase):
    def setUp(self):
        (ROOT / 'tmp').mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=ROOT / 'tmp')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.database = self.root / '.cache/library.sqlite3'
        for folder in ('discovery', 'atlas/registry', 'projects', 'cards', 'atlas/labs/study'):
            (self.root / folder).mkdir(parents=True)
        self.write_csv('discovery/catalog.csv', [
            dict(id='flowcept', name='Flowcept', status='active', notes='offline provenance'),
            dict(id='stub', name='Stub', status='stub-osti-only', notes='no public code')])
        self.write_csv('discovery/lanes.csv', [
            dict(id='flowcept', lanes='software-engineering;ai-agents', tier='deep', why='public code'),
            dict(id='stub', lanes='cybersecurity', tier='lead', why='report only')])
        self.write_json('discovery/registry-links.json', {'links': [dict(
            registry_id='software-flowcept', project_id='flowcept', basis='same repository')]})
        for collection in library.COLLECTIONS:
            rows = []
            if collection == 'software':
                rows = [dict(id='software-flowcept', name='Flowcept', evidence='lead', source_ids=['src-one'])]
            elif collection == 'sources':
                rows = [dict(id='src-one', title='Offline source', promotion='blocked', url='https://example.org/source')]
            self.write_json(f'atlas/registry/{collection}.json', {collection: rows})
        self.write('projects/flowcept.md', '# Flowcept\n## Offline buffering\nSIGTERM can lose unflushed provenance.\n')
        self.write('atlas/labs/study/README.md', '# Study\nSynthetic offline run only.\n')
        self.write_json('atlas/labs/study/results.json', {'records': []})
        self.card = dict(schema_version=1, id='buffer-loss', project_ids=['flowcept'],
            title='Buffered provenance loss', problem='Unflushed records', mechanism='Memory buffer',
            finding='Zero records in stored synthetic case', evidence_level='experiment-recorded',
            source_urls=['https://example.org/source'], code_refs=[],
            supporting_paths=['atlas/labs/study/README.md'], experiment=dict(status='recorded',
                revision='a' * 40, command='python scenarios.py', results_path='atlas/labs/study/results.json',
                limitations='Synthetic offline case, historical result only'),
            adaptation='Measure persistence interval', unknowns=['Online behavior'])
        self.write_json('cards/buffer-loss.json', self.card)

    def write(self, path, value):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(value)

    def write_json(self, path, value):
        self.write(path, json.dumps(value))

    def write_csv(self, path, rows):
        with (self.root / path).open('w', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)

    def open(self):
        library.build(self.root, self.database)
        db = library.open_current(self.root, self.database)
        self.addCleanup(db.close)
        return db

    def test_search_and_filters_preserve_recorded_depth(self):
        db = self.open()
        rows = library.search(db, 'provenance', lane='ai-agents', tier='deep', kind='card')
        self.assertEqual([r['id'] for r in rows], ['card:buffer-loss'])
        packet = library.project_packet(db, 'flowcept')
        self.assertEqual(packet['cards'][0]['evidence_level'], 'experiment-recorded')
        self.assertEqual(packet['cards'][0]['experiment']['limitations'], self.card['experiment']['limitations'])
        self.assertEqual(library.search(db, 'provenance', lane='cybersecurity'), [])

    def test_context_keeps_registry_evidence_and_stub(self):
        db = self.open()
        packet = library.project_packet(db, 'flowcept')
        nodes = {n['id']: n for n in packet['registry_nodes']}
        self.assertEqual(nodes['software-flowcept']['evidence'], 'lead')
        self.assertEqual(nodes['src-one']['promotion'], 'blocked')
        self.assertEqual(packet['project']['status'], 'active')
        self.assertFalse(packet['missing_brief'])
        self.assertTrue(library.project_packet(db, 'stub')['missing_brief'])
        self.assertIn({'path': 'atlas/labs/study/README.md', 'kind': 'lab'}, packet['documents'])
        with self.assertRaisesRegex(ValueError, 'unknown catalog'):
            library.project_packet(db, 'not-a-project')

    def test_stale_edit_add_delete_and_result_change(self):
        self.open()
        for relative, value in [('projects/flowcept.md', '# Changed'),
                                ('projects/added.md', '# Added'),
                                ('atlas/labs/study/results.json', '{"records": [1]}')]:
            library.build(self.root, self.database)
            self.write(relative, value)
            with self.assertRaisesRegex(ValueError, 'stale'):
                library.open_current(self.root, self.database)
        library.build(self.root, self.database)
        (self.root / 'projects/added.md').unlink()
        with self.assertRaisesRegex(ValueError, 'stale'):
            library.open_current(self.root, self.database)

    def test_invalid_card_and_alias_do_not_replace_index(self):
        self.open()
        original = self.database.read_bytes()
        invalid = copy.deepcopy(self.card)
        invalid['experiment']['status'] = 'not-run'
        self.write_json('cards/buffer-loss.json', invalid)
        with self.assertRaisesRegex(ValueError, 'disagree'):
            library.build(self.root, self.database)
        self.assertEqual(original, self.database.read_bytes())
        self.write_json('cards/buffer-loss.json', self.card)
        self.write_json('discovery/registry-links.json', {'links': [dict(
            registry_id='software-fake', project_id='flowcept', basis='bad alias')]})
        with self.assertRaisesRegex(ValueError, 'crosswalk'):
            library.build(self.root, self.database)
        self.assertEqual(original, self.database.read_bytes())

    def lead(self, **changes):
        row = dict(id='or-sage', name='OR-SAGE', url='https://orsage.example.org/', surface='standalone site',
                   found_via='owner URL', lanes='none', tier_guess='pool', mechanism='GIS siting screen',
                   status='out-of-lane', checked='2026-11-15', notes='no public code searched')
        row.update(changes)
        return row

    def test_leads_are_searchable_but_not_catalog_projects(self):
        self.write_csv('discovery/leads.csv', [self.lead()])
        db = self.open()
        rows = library.search(db, 'siting', kind='lead')
        self.assertEqual([r['id'] for r in rows], ['lead:or-sage'])
        with self.assertRaisesRegex(ValueError, 'unknown catalog'):
            library.project_packet(db, 'or-sage')
        self.write_csv('discovery/leads.csv', [self.lead(notes='changed')])
        with self.assertRaisesRegex(ValueError, 'stale'):
            library.open_current(self.root, self.database)

    def test_invalid_or_falsely_promoted_lead_is_rejected(self):
        self.open()
        original = self.database.read_bytes()
        for bad in (self.lead(status='maybe'), self.lead(status='promoted'),
                    self.lead(id='flowcept', status='candidate'), self.lead(lanes='physics')):
            self.write_csv('discovery/leads.csv', [bad])
            with self.assertRaisesRegex(ValueError, 'invalid lead'):
                library.build(self.root, self.database)
        self.assertEqual(original, self.database.read_bytes())

    def test_concurrent_source_edit_cannot_certify_old_text(self):
        self.open()
        original = self.database.read_bytes()
        collect = library.collect

        def collect_with_edit(root):
            records = collect(root)
            self.write('projects/flowcept.md', '# Flowcept\nChanged during collection')
            return records

        with patch.object(library, 'collect', side_effect=collect_with_edit):
            with self.assertRaisesRegex(ValueError, 'changed during collection'):
                library.build(self.root, self.database)
        self.assertEqual(original, self.database.read_bytes())

    def test_path_escape_and_unpinned_code_rejected(self):
        card = copy.deepcopy(self.card)
        card['supporting_paths'] = ['../outside.md']
        with self.assertRaisesRegex(ValueError, 'outside-repository'):
            library.validate_card(self.root, card, {'flowcept': {}}, Path('buffer-loss.json'))
        card = copy.deepcopy(self.card)
        card['code_refs'] = ['https://github.com/ORNL/flowcept/blob/main/file.py']
        with self.assertRaisesRegex(ValueError, 'full commit'):
            library.validate_card(self.root, card, {'flowcept': {}}, Path('buffer-loss.json'))

    def test_search_treats_fts_syntax_as_literal_words(self):
        db = self.open()
        self.assertTrue(library.search(db, '"provenance" OR (SIGTERM*)'))
        with self.assertRaisesRegex(ValueError, 'at least one word'):
            library.search(db, '"*()')

    def test_discovery_snapshots_are_not_promoted(self):
        db = self.open()
        self.write_json('discovery/snapshots/unreviewed.json', {'name': 'Unverified secret miracle'})
        # Unowned metadata neither enters results nor invalidates the maintained corpus.
        current = library.open_current(self.root, self.database)
        self.addCleanup(current.close)
        self.assertEqual(library.search(db, 'miracle'), [])

    def test_refuses_to_overwrite_unrelated_database(self):
        self.database.parent.mkdir()
        with sqlite3.connect(self.database) as db:
            db.execute('CREATE TABLE important(value)')
        original = self.database.read_bytes()
        with self.assertRaisesRegex(ValueError, 'refusing to overwrite'):
            library.build(self.root, self.database)
        self.assertEqual(original, self.database.read_bytes())

    def test_markdown_code_fence_is_not_a_section(self):
        text = '# Guide\n```python\n# code comment\n```\n## Result\nObserved\n'
        rows = list(library.sections(text))
        self.assertEqual([r[0] for r in rows], ['Guide', 'Result'])
        self.assertEqual(rows[1][1], 5)


if __name__ == '__main__':
    unittest.main()
