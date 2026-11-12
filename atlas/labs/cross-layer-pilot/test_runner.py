import json
from pathlib import Path
import tempfile
import unittest

import runner


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.log = self.root / 'events.jsonl'
        self.fixture = runner.read_json(runner.DEFAULT_FIXTURE)
        self.registry = runner.ROOT / 'registry'

    def execute(self, **kwargs):
        return runner.run(self.registry, self.fixture, self.log, **kwargs)

    def events(self):
        return [json.loads(line) for line in self.log.read_text().splitlines()]

    def test_result_repeats_and_appends(self):
        first = self.execute(approved=True)
        count = runner.verify_log(self.log)
        self.assertEqual(first, self.execute(approved=True))
        self.assertEqual(runner.verify_log(self.log), 2 * count)
        self.assertEqual(first['mean'], 5)
        self.assertEqual(first['decision'], 'accept')

    def test_denied_approval_never_measures(self):
        with self.assertRaisesRegex(ValueError, 'requires'):
            self.execute()
        self.assertNotIn('measure', [e['stage'] for e in self.events()])
        self.assertEqual(self.events()[-1]['stage'], 'stopped')

    def test_blocked_and_missing_evidence_fail_closed(self):
        for state in ('blocked', 'lead', 'missing'):
            with self.subTest(state=state):
                local = self.root / state
                local.mkdir()
                for name in ('projects', 'sources', 'facilities', 'roles', 'software', 'edges'):
                    data = runner.read_json(self.registry / (name + '.json'))
                    if name == 'sources':
                        for row in data[name]:
                            if row['id'] == 'src-agentic-workflows-job':
                                row['promotion'] = state
                        if state == 'missing':
                            data[name] = [r for r in data[name] if r['id'] != 'src-agentic-workflows-job']
                    (local / (name + '.json')).write_text(json.dumps(data))
                with self.assertRaisesRegex(ValueError, 'unverified'):
                    runner.run(local, self.fixture, self.root / (state + '.jsonl'), True)

    def test_invalid_numbers_and_shape_stop(self):
        for fixture in ({'samples': [], 'threshold': 0}, {'samples': [True], 'threshold': 0}, {'samples': [1], 'threshold': float('inf')}, {'samples': [1], 'threshold': 0, 'command': 'x'}):
            with self.subTest(fixture=fixture), self.assertRaises(ValueError):
                runner.validate_fixture(fixture)

    def test_retry_recovers_once_and_has_same_science(self):
        expected = self.execute(approved=True)
        actual = self.execute(approved=True, inject_failure=True, retries=1)
        self.assertEqual(expected, actual)
        self.assertIn('retry', [e['stage'] for e in self.events()])

    def test_no_budget_stops_before_decision(self):
        with self.assertRaisesRegex(ValueError, 'exhausted'):
            self.execute(approved=True, inject_failure=True)
        self.assertNotIn('decision', [e['stage'] for e in self.events()])

    def test_changed_input_changes_fingerprint_and_result(self):
        first = self.execute(approved=True)
        self.fixture['samples'] = [0, 0]
        second = self.execute(approved=True)
        requests = [e for e in self.events() if e['stage'] == 'request']
        self.assertNotEqual(requests[0]['fixture_hash'], requests[1]['fixture_hash'])
        self.assertNotEqual(first['decision'], second['decision'])

    def test_tampered_log_is_rejected_before_append(self):
        self.execute(approved=True)
        text = self.log.read_text().replace('"approved": true', '"approved": false', 1)
        self.log.write_text(text)
        with self.assertRaisesRegex(ValueError, 'chain invalid'):
            self.execute(approved=True)
        self.assertEqual(self.log.read_text(), text)

    def rewrite_chain(self, events):
        previous = None
        for event in events:
            event.pop('hash', None)
            event['previous'] = previous
            event['hash'] = runner.digest(event)
            previous = event['hash']
        self.log.write_text(''.join(json.dumps(event) + '\n' for event in events))

    def test_semantic_replay_repeated_and_recovery(self):
        self.execute(approved=True)
        self.execute(approved=True, inject_failure=True, retries=1)
        self.assertEqual(runner.replay_log(self.log)['completed'], 2)
        self.assertEqual(runner.replay_log(self.log)['runs'], 2)

    def test_semantic_replay_false_decision_with_recomputed_hashes(self):
        self.execute(approved=True)
        events = self.events()
        events[-1]['result']['decision'] = 'revise'
        events[-1]['result_hash'] = runner.digest(events[-1]['result'])
        self.rewrite_chain(events)
        runner.verify_log(self.log)
        with self.assertRaisesRegex(ValueError, 'decision differs'):
            runner.replay_log(self.log)

    def test_semantic_replay_changed_measurement_with_recomputed_hashes(self):
        self.execute(approved=True)
        events = self.events()
        measurement = next(e for e in events if e['stage'] == 'measure')
        measurement['samples'] = [0, 0]
        measurement['output_hash'] = runner.digest(measurement['samples'])
        self.rewrite_chain(events)
        runner.verify_log(self.log)
        with self.assertRaisesRegex(ValueError, 'measurement differs'):
            runner.replay_log(self.log)

    def test_semantic_replay_rejects_unapproved_measurement(self):
        self.execute(approved=True)
        events = self.events()
        events[0]['approved'] = False
        self.rewrite_chain(events)
        with self.assertRaisesRegex(ValueError, 'without approval'):
            runner.replay_log(self.log)

    def test_semantic_replay_stopped_run_and_terminal_boundary(self):
        with self.assertRaises(ValueError):
            self.execute()
        self.assertEqual(runner.replay_log(self.log)['completed'], 0)
        events = self.events()
        events.append(dict(events[-1], sequence=len(events), stage='decision'))
        self.rewrite_chain(events)
        with self.assertRaisesRegex(ValueError, 'after terminal'):
            runner.replay_log(self.log)

    def test_replay_rejects_blocked_snapshot_and_project_mismatch(self):
        self.execute(approved=True)
        original = self.events()
        for mutation in ('blocked', 'project'):
            with self.subTest(mutation=mutation):
                events = json.loads(json.dumps(original))
                gate = next(e for e in events if e['stage'] == 'evidence_gate')
                if mutation == 'blocked':
                    gate['snapshot']['required_sources'][0]['promotion'] = 'blocked'
                else:
                    events[0]['project_id'] = 'different-project'
                gate['snapshot_hash'] = runner.digest(gate['snapshot'])
                self.rewrite_chain(events)
                with self.assertRaises(ValueError):
                    runner.replay_log(self.log)

    def test_replay_rejects_missing_relationship_support(self):
        self.execute(approved=True)
        events = self.events()
        gate = next(e for e in events if e['stage'] == 'evidence_gate')
        gate['snapshot']['relationships'][0]['source_ids'] = ['not-recorded']
        gate['snapshot_hash'] = runner.digest(gate['snapshot'])
        self.rewrite_chain(events)
        with self.assertRaisesRegex(ValueError, 'source support'):
            runner.replay_log(self.log)

    def test_nonproject_relationship_source_is_preserved_for_replay(self):
        local = self.root / 'extra-source'
        local.mkdir()
        for name in ('projects', 'sources', 'facilities', 'roles', 'software', 'edges'):
            data = runner.read_json(self.registry / (name + '.json'))
            if name == 'edges':
                data[name].append({'from': 'project-agentic-workflows', 'to': 'software-hermes-codex', 'relation': 'synthetic_test_relationship', 'evidence': 'verified', 'source_ids': ['src-doe-sti']})
            (local / (name + '.json')).write_text(json.dumps(data))
        runner.run(local, self.fixture, self.log, True)
        snapshot = next(e['snapshot'] for e in self.events() if e['stage'] == 'evidence_gate')
        self.assertIn('src-doe-sti', [row['id'] for row in snapshot['relationship_sources']])
        self.assertEqual(runner.replay_log(self.log)['completed'], 1)

    def test_huge_integer_is_clean_failure(self):
        self.fixture['samples'] = [10 ** 1000]
        with self.assertRaisesRegex(ValueError, 'finite numbers'):
            self.execute(approved=True)
        self.assertEqual(self.events()[-1]['stage'], 'stopped')

    def test_decision_uses_authoritative_mean_at_threshold(self):
        self.fixture = {'samples': [0.1, 0.1, 0.1], 'threshold': 0.1}
        result = self.execute(approved=True)
        self.assertEqual(result['mean'], 0.1)
        self.assertEqual(result['decision'], 'accept')
        self.assertEqual(runner.replay_log(self.log)['completed'], 1)

    def test_missing_relationship_stops(self):
        local = self.root / 'no-edges'
        local.mkdir()
        for name in ('projects', 'sources', 'facilities', 'roles', 'software', 'edges'):
            data = runner.read_json(self.registry / (name + '.json'))
            if name == 'edges':
                data[name] = []
            (local / (name + '.json')).write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'relationships'):
            runner.run(local, self.fixture, self.log, True)

    def test_missing_context_is_rejected(self):
        local = self.root / 'registry'
        local.mkdir()
        for name in ('projects', 'sources', 'facilities', 'roles', 'software', 'edges'):
            data = runner.read_json(self.registry / (name + '.json'))
            if name == 'roles':
                data[name] = []
            (local / (name + '.json')).write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'context record'):
            runner.run(local, self.fixture, self.log, True)


if __name__ == '__main__':
    unittest.main()
