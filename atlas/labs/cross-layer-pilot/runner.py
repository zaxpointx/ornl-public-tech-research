#!/usr/bin/env python3
"""Local synthetic workflow study, not an ORNL implementation or adapter."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
import statistics

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FIXTURE = Path(__file__).with_name('fixture.json')


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def verify_log(path):
    previous = None
    count = 0
    if not Path(path).exists():
        return 0
    for line in Path(path).read_text().splitlines():
        event = json.loads(line)
        recorded = event.pop('hash')
        if event.get('previous') != previous or event.get('sequence') != count or digest(event) != recorded:
            raise ValueError(f'evidence chain invalid at event {count}')
        previous = recorded
        count += 1
    return count


def validate_snapshot(snapshot, project_id):
    project = snapshot['project']
    if project.get('id') != project_id:
        raise ValueError('recorded project does not match request')
    direct = {row['id']: row for row in snapshot['required_sources']}
    if not project.get('source_ids') or set(direct) != set(project['source_ids']):
        raise ValueError('required source support is incomplete')
    sources = dict(direct)
    for row in snapshot['relationship_sources']:
        if row['id'] in sources and sources[row['id']] != row:
            raise ValueError('recorded source support is inconsistent')
        sources[row['id']] = row
    for sid, source in sources.items():
        if source.get('promotion') != 'verified' or source.get('retrieval_status') != 'verified' or not all(source.get(k) for k in ('url', 'evidence_excerpt', 'retrieved_on')):
            raise ValueError(f'recorded source is missing or unverified: {sid}')
    node_ids = {project_id, *sources}
    for collection, key in (('facilities', 'facility_ids'), ('roles', 'role_ids'), ('software', 'software_ids')):
        records = snapshot['context'][collection]
        if {row['id'] for row in records} != set(project.get(key, [])):
            raise ValueError('recorded context support is incomplete')
        node_ids.update(row['id'] for row in records)
    node_ids.update(row['id'] for row in snapshot['relationship_targets'])
    if not snapshot['relationships']:
        raise ValueError('project has no outgoing evidence relationships')
    for edge in snapshot['relationships']:
        if edge.get('from') != project_id or edge.get('to') not in node_ids:
            raise ValueError('recorded relationship has missing endpoint support')
        source_ids = edge.get('source_ids')
        if not isinstance(source_ids, list) or (edge.get('evidence') != 'local' and not source_ids):
            raise ValueError('recorded relationship has incomplete source support')
        if any(sid not in sources for sid in source_ids):
            raise ValueError('recorded relationship source support is incomplete')


def replay_log(path):
    """Check the hash chain, then replay every completed synthetic result."""
    count = verify_log(path)
    events = [json.loads(line) for line in Path(path).read_text().splitlines()]
    runs = []
    for event in events:
        if event['stage'] == 'request':
            runs.append([])
        if not runs:
            raise ValueError('replay: event before request')
        runs[-1].append(event)
    completed = 0
    for run_events in runs:
        stages = [event['stage'] for event in run_events]
        request = run_events[0]
        by_stage = {event['stage']: event for event in run_events}
        # Each run has exactly one terminal event. Interrupted partial runs fail
        # replay even though their chain may be intact.
        if stages[-1] not in ('decision', 'stopped'):
            raise ValueError('replay: incomplete run')
        if any(stage in ('decision', 'stopped') for stage in stages[:-1]):
            raise ValueError('replay: event after terminal state')
        if 'evidence_gate' in by_stage:
            gate = by_stage['evidence_gate']
            validate_snapshot(gate['snapshot'], request['project_id'])
            if digest(gate['snapshot']) != gate['snapshot_hash']:
                raise ValueError('replay: snapshot fingerprint differs')
        if 'plan' in by_stage:
            fixture = by_stage['plan']['fixture']
            validate_fixture(fixture)
            if digest(fixture) != request['fixture_hash']:
                raise ValueError('replay: fixture fingerprint differs')
        if 'measure' in by_stage:
            if not request['approved'] or not by_stage.get('approval', {}).get('approved'):
                raise ValueError('replay: measurement without approval')
            prefix = ['request', 'evidence_gate', 'plan', 'approval']
            if stages[:4] != prefix:
                raise ValueError('replay: invalid execution ordering')
            measurement_index = stages.index('measure')
            recovery = stages[4:measurement_index]
            if recovery not in ([], ['measure_failed', 'retry']):
                raise ValueError('replay: invalid recovery ordering')
            if recovery and (request['retries'] != 1 or not request['inject_failure']):
                raise ValueError('replay: unauthorized retry')
            if not recovery and request['inject_failure']:
                raise ValueError('replay: missing injected failure')
            if recovery and (by_stage['measure_failed']['attempt'] != 0 or by_stage['retry']['next_attempt'] != 1):
                raise ValueError('replay: invalid retry attempts')
            measure = by_stage['measure']
            if measure['attempt'] != int(bool(recovery)) or measure['samples'] != fixture['samples'] or measure['output_hash'] != digest(fixture['samples']):
                raise ValueError('replay: measurement differs from fixture')
        if stages[-1] == 'stopped':
            continue
        if 'measure' not in by_stage:
            raise ValueError('replay: decision without measurement')
        if stages[measurement_index:] != ['measure', 'analyze', 'verify', 'decision']:
            raise ValueError('replay: invalid result ordering')
        expected_mean = statistics.mean(fixture['samples'])
        analysis = by_stage['analyze']
        if analysis['input_hash'] != digest(fixture['samples']) or analysis['mean'] != expected_mean:
            raise ValueError('replay: analysis differs from measurements')
        check = by_stage['verify']
        if check['passed'] is not True or check['expected_mean'] != expected_mean:
            raise ValueError('replay: invalid verification result')
        result = by_stage['decision']['result']
        expected = dict(count=len(fixture['samples']), mean=analysis['mean'], threshold=fixture['threshold'], decision='accept' if analysis['mean'] >= fixture['threshold'] else 'revise')
        if result != expected or by_stage['decision']['result_hash'] != digest(result):
            raise ValueError('replay: decision differs from reconstructed result')
        completed += 1
    return dict(verified_events=count, runs=len(runs), completed=completed)


class Evidence:
    def __init__(self, path):
        self.path = Path(path)
        self.sequence = verify_log(path)
        lines = self.path.read_text().splitlines() if self.path.exists() else []
        self.previous = json.loads(lines[-1])['hash'] if lines else None

    def emit(self, stage, **data):
        event = dict(sequence=self.sequence, previous=self.previous, stage=stage, evidence='local', **data)
        event['hash'] = digest(event)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open('a') as stream:
            stream.write(json.dumps(event, sort_keys=True, allow_nan=False) + '\n')
        self.sequence += 1
        self.previous = event['hash']


def context(registry, project_id):
    tables = {name: {r['id']: r for r in read_json(registry / (name + '.json'))[name]}
              for name in ('projects', 'sources', 'facilities', 'roles', 'software')}
    project = tables['projects'].get(project_id)
    if not project:
        raise ValueError(f'missing project: {project_id}')
    sources = []
    for sid in project.get('source_ids', []):
        source = tables['sources'].get(sid)
        if not source or source.get('promotion') != 'verified' or source.get('retrieval_status') != 'verified' or not all(source.get(k) for k in ('url', 'evidence_excerpt', 'retrieved_on')):
            raise ValueError(f'required source is missing or unverified: {sid}')
        sources.append(source)
    if not sources:
        raise ValueError('project has no verified source basis')
    linked = {}
    for name in ('facilities', 'roles', 'software'):
        key = {'facilities': 'facility_ids', 'roles': 'role_ids', 'software': 'software_ids'}[name]
        linked[name] = []
        for rid in project.get(key, []):
            if rid not in tables[name]:
                raise ValueError(f'missing context record: {rid}')
            linked[name].append(tables[name][rid])
    # Connected context is preserved verbatim, including lead/blocked labels. It
    # does not become an execution dependency or a newly verified ORNL claim.
    edges = [edge for edge in read_json(registry / 'edges.json')['edges'] if edge.get('from') == project_id]
    if not edges:
        raise ValueError('project has no outgoing evidence relationships')
    all_ids = set().union(*(set(table) for table in tables.values()))
    for edge in edges:
        if edge.get('to') not in all_ids:
            raise ValueError('relationship points to a missing record')
        if edge.get('evidence') != 'local' and not edge.get('source_ids'):
            raise ValueError('non-local relationship has no source')
        for sid in edge.get('source_ids', []):
            source = tables['sources'].get(sid)
            if not source or source.get('promotion') != 'verified' or source.get('retrieval_status') != 'verified':
                raise ValueError(f'relationship source is missing or unverified: {sid}')
    relationship_ids = {sid for edge in edges for sid in edge.get('source_ids', [])}
    targets = {edge['to'] for edge in edges}
    snapshot = dict(project=project, required_sources=sources, context=linked, relationships=edges,
                    relationship_sources=[tables['sources'][sid] for sid in sorted(relationship_ids)],
                    relationship_targets=[row for table in tables.values() for rid, row in table.items() if rid in targets])
    validate_snapshot(snapshot, project_id)
    return snapshot


def validate_fixture(fixture):
    if set(fixture) != {'samples', 'threshold'}:
        raise ValueError('fixture requires samples and threshold only')
    samples = fixture['samples']
    threshold = fixture['threshold']
    def numeric(value):
        try:
            return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
        except OverflowError:
            return False
    if not isinstance(samples, list) or not samples or len(samples) > 10000 or not all(numeric(n) for n in samples):
        raise ValueError('samples must be 1..10000 finite numbers')
    if not numeric(threshold):
        raise ValueError('threshold must be a finite number')


def run(registry, fixture, output, approved=False, project_id='project-agentic-workflows', inject_failure=False, retries=0):
    if retries not in (0, 1):
        raise ValueError('retries must be 0 or 1')
    log = Evidence(output)
    log.emit('request', approved=approved, project_id=project_id, fixture_hash=digest(fixture), retries=retries, inject_failure=inject_failure)
    try:
        snapshot = context(Path(registry), project_id)
        log.emit('evidence_gate', snapshot=snapshot, snapshot_hash=digest(snapshot))
        validate_fixture(fixture)
        log.emit('plan', question='Does the synthetic mean meet the supplied threshold?', stages=['measure', 'analyze', 'decide'], fixture=fixture)
        if not approved:
            raise ValueError('execution requires --approve-synthetic')
        log.emit('approval', approved=True, scope='this synthetic fixture and at most the requested retry')
        for attempt in range(retries + 1):
            if inject_failure and attempt == 0:
                log.emit('measure_failed', attempt=attempt, reason='injected transient failure')
                if attempt == retries:
                    raise ValueError('measurement failed; retry budget exhausted')
                log.emit('retry', next_attempt=attempt + 1)
                continue
            samples = fixture['samples']
            log.emit('measure', attempt=attempt, samples=samples, output_hash=digest(samples))
            break
        mean = math.fsum(value / len(samples) for value in samples)
        expected_mean = statistics.mean(samples)
        if not math.isclose(mean, expected_mean, rel_tol=1e-12, abs_tol=1e-12):
            raise ValueError('independent mean verification failed')
        mean = expected_mean
        result = dict(count=len(samples), mean=mean, threshold=fixture['threshold'], decision='accept' if mean >= fixture['threshold'] else 'revise')
        log.emit('analyze', input_hash=digest(samples), mean=mean)
        log.emit('verify', method='statistics.mean cross-check', passed=True, expected_mean=expected_mean)
        log.emit('decision', result=result, result_hash=digest(result), next_action='stop; human review before changing fixture')
        return result
    except (ValueError, KeyError, OSError, TypeError, OverflowError) as exc:
        log.emit('stopped', reason=str(exc), next_action='repair input or evidence; start a new approved run')
        raise ValueError(str(exc)) from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--registry', type=Path, default=ROOT / 'registry')
    parser.add_argument('--fixture', type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument('--output', type=Path, default=Path('workflow-evidence.jsonl'))
    parser.add_argument('--project', default='project-agentic-workflows')
    parser.add_argument('--approve-synthetic', action='store_true')
    parser.add_argument('--inject-failure', action='store_true')
    parser.add_argument('--retries', type=int, choices=(0, 1), default=0)
    parser.add_argument('--verify-log', type=Path)
    parser.add_argument('--replay-log', type=Path)
    args = parser.parse_args()
    try:
        if args.replay_log:
            print(json.dumps(replay_log(args.replay_log), sort_keys=True))
        elif args.verify_log:
            if not args.verify_log.is_file():
                raise ValueError('evidence log does not exist')
            print(json.dumps({'verified_events': verify_log(args.verify_log)}))
        else:
            print(json.dumps(run(args.registry, read_json(args.fixture), args.output, args.approve_synthetic, args.project, args.inject_failure, args.retries), sort_keys=True))
    except (ValueError, OSError, KeyError, TypeError, OverflowError) as exc:
        print(f'workflow stopped: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
