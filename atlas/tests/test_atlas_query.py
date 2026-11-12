"""Context packets must preserve evidence boundaries and reject broken graphs."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('atlas_query', Path(__file__).resolve().parents[1] / 'scripts/atlas_query.py')
atlas = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(atlas)


class ContextTests(unittest.TestCase):
    def test_packet_keeps_inferred_edges_and_unverified_evidence_visible(self):
        nodes = {
            'p': {'id': 'p', 'collection': 'projects', 'source_ids': ['s']},
            's': {'id': 's', 'collection': 'sources', 'promotion': 'lead'},
            'sw': {'id': 'sw', 'collection': 'software', 'source_ids': ['s2']},
            's2': {'id': 's2', 'collection': 'sources', 'promotion': 'verified'},
            'unrelated': {'id': 'unrelated', 'collection': 'projects'},
        }
        edges = [{'from': 'p', 'to': 'sw', 'evidence': 'INFERRED', 'source_ids': ['s']}]
        packet = atlas.context_packet(nodes, edges, 'p')
        self.assertEqual(packet['typed_relationships'][0]['evidence'], 'INFERRED')
        self.assertEqual(packet['unresolved_source_ids'], ['s'])
        self.assertEqual({s['id'] for s in packet['sources']}, {'s', 's2'})
        self.assertEqual([n['id'] for n in packet['neighbors']], ['sw'])

    def test_unknown_node_fails(self):
        with self.assertRaisesRegex(ValueError, 'unknown node'):
            atlas.context_packet({}, [], 'missing')

    def test_missing_reference_fails_instead_of_silently_omitting_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'registry').mkdir()
            for collection in (*atlas.COLLECTIONS, 'edges'):
                rows = [{'id': 'p', 'source_ids': ['missing']}] if collection == 'projects' else []
                (root / 'registry' / f'{collection}.json').write_text(json.dumps({collection: rows}))
            with self.assertRaisesRegex(ValueError, 'missing source_ids target'):
                atlas.load_registry(root)


if __name__ == '__main__':
    unittest.main()
