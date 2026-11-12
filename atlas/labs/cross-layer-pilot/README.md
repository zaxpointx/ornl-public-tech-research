# Local provenance workflow experiment

_Run commands from the `atlas/` folder of this repository (merged 2026-11-11)._

A standard-library-only experiment in evidence-gated execution, reproducible synthetic analysis, lineage capture, and bounded retry. This is Atlas code. It does not use or implement INTERSECT, Flowcept, DataFed, facility APIs, or an ORNL protocol. Its research motivation is documented in [the original pilot](../cross-layer-pilot.md) and [the workflow dossier](../../guide/project-dossiers/agentic-workflows-and-provenance.md).

## Run from the repository root

```sh
python3 labs/cross-layer-pilot/runner.py --approve-synthetic --output /tmp/atlas-success.jsonl
python3 labs/cross-layer-pilot/runner.py --approve-synthetic --inject-failure --retries 1 --output /tmp/atlas-recovery.jsonl
python3 labs/cross-layer-pilot/runner.py --verify-log /tmp/atlas-recovery.jsonl
python3 labs/cross-layer-pilot/runner.py --replay-log /tmp/atlas-recovery.jsonl
python3 -m unittest discover -s labs/cross-layer-pilot -v
```

The fixture is four synthetic measurements `[2, 4, 6, 8]` with threshold `4.5`. Analysis produces mean `5.0` and decision `accept`. Changing the threshold or measurements changes the recorded input fingerprint. `statistics.mean` independently cross-checks the scaled-sum analysis, then supplies the authoritative mean used for threshold decisions. These numbers model a generic measurement decision; they have no physical units or ORNL validation.

Omit `--approve-synthetic` to observe a denied run. Use `--inject-failure` without retries to observe exhausted recovery. Both return exit status 1 and append a `stopped` event before any scientific decision. The one retry is covered by the explicit synthetic approval; there is no adaptive fixture change. The flag is an execution gate, not identity authentication or a GUI approval service.

## Evidence and lineage

The runner reads the Atlas project, source, facility, role, and software registries. Every source directly required by the selected project must exist, be marked `verified` in both promotion and retrieval state, and include its URL, excerpt, and retrieval date. This checks Atlas metadata, not live source truth. A blocked, lead, missing, or incomplete required source stops execution.

Connected facilities, roles, and software are retained verbatim as context. Their own evidence states remain unchanged; a facility lead is not promoted or used as a scientific execution dependency. A missing referenced context record stops the run. Registry verification remains the responsibility of research and review.

Outgoing project relationships must exist and name existing records; non-local relationship sources must also be verified. Missing graph links produce a stopped run.

The JSONL file contains the complete relevant registry snapshot and its SHA-256 hash, fixture and fingerprint, approval, measurement, analysis, verification, decision, and any failure/retry. Every event links to the preceding event hash and has a sequence number. Existing output is checked before appending. Multiple invocations append separate `request` sequences to the same chain. `--verify-log` checks sequence and content integrity. `--replay-log` additionally reconstructs completed science from recorded fixture and measurements, checks snapshot/input/result fingerprints, recorded project identity, source gate metadata and relationship support without consulting the live registry, approval ordering, retry budget, verification, decision, and terminal-state boundaries across appended runs. It rejects a false decision or altered measurement even if someone recomputes the chain hashes. A coherently rewritten complete synthetic run remains possible; this is consistency checking, not authentication. Partial interrupted runs fail replay until resolved in a separate record.

This hash chain detects accidental edits to an existing chain. It is not signed, concurrent-writer-safe, or secure against a person rewriting the whole chain. Use a separate output file per concurrent process. A malformed fixture JSON or an unserializable/nonfinite request can fail before an event is written. There is no background execution, networking, external installation, telemetry collector, database, distributed scheduling, restart checkpointing, or hardware control.

## Checked behavior

Tests cover reproducible repeated output, append behavior, denied approval, blocked/lead/missing evidence, malformed measurements, dangling context, missing relationships, injected failure with and without a retry budget, changed input fingerprints, refusal to append to an altered chain, and semantic rejection of fabricated decisions/measurements with recomputed hashes. The checked-in `examples/` records are reproducible observations of the synthetic fixture, not research evidence about ORNL.

The next useful extension is a separately scoped adapter experiment with an actual public provenance library after its release, license, and input boundary are verified. Comparing its captured events with this explicit baseline would test event completeness and overhead rather than merely demonstrate installation.
