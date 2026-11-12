# Cross-layer pilot: research workflow digital twin

**Decision:** Start with a safe, software-only research workflow digital twin. Do not begin with a physical instrument, a live facility, a sensitive dataset, or a large model.

## Why this pilot

This is the smallest experiment that touches the atlas layers without pretending to recreate ORNL:

- **Project:** agentic workflow orchestration and autonomous science.
- **Facility context:** OLCF/Frontier and HPC/manufacturing user facilities, represented only as public context and synthetic nodes.
- **Software:** the local Hermes + Codex study stack, with no ORNL attribution.
- **Role family:** WES/NCCS research-scientist signal from the public job record.
- **Evidence layer:** source IDs, retrieval state, excerpts, and explicit unknowns.

The pilot tests the atlas's operating idea: a research system should preserve the path from question to evidence to decision, not just produce a summary.

## Smallest useful version

Build a deterministic local runner that:

1. Reads `registry/*.json`.
2. Selects one project and its connected source, facility, role, and local-tool records.
3. Creates a synthetic research question and a bounded experiment plan.
4. Requires a human approval flag before execution.
5. Runs a deterministic verifier against synthetic data or fixtures only.
6. Emits an append-only evidence record containing source IDs, inputs, outputs, failures, and the next decision.
7. Fails closed when a required source is `blocked`, `lead`, or missing rather than upgrading the claim.

## First scenario

**Question:** Can the registry identify the minimum control-plane pieces needed to run a trustworthy research loop?

**Synthetic workflow:**

```text
question
  -> select evidence-bearing project
  -> check source states
  -> plan synthetic test
  -> human approval gate
  -> run deterministic test
  -> verify output
  -> write evidence record
  -> choose stop / revise / investigate
```

The first run should use `project-agentic-workflows`, `facility-olcf-frontier`, `role-wes-nccs`, and `software-hermes-codex`. It should not call an ORNL endpoint, submit a job, download restricted data, or claim that the local runner is ORNL's architecture.

## Acceptance criteria

- Every output claim points to a registry source ID or is labeled `local`.
- `blocked` and `lead` sources cannot be silently promoted by the runner.
- A human approval gate is visible in the evidence record.
- The verifier can reproduce the same result from the same fixture.
- No credentials, private data, facility APIs, external system writes, or unattended physical actions are used.
- The pilot produces a useful failure report when a source, edge, or verification step is missing.

## Explicit non-goals

- No claim about classified ORNL work.
- No reverse engineering of internal ORNL systems.
- No remote access to OLCF, HFIR, instruments, or partner networks.
- No handling of PHI, PII, export-controlled, classified, OUO, UCI, UCNI, NDA, or vendor-proprietary material.
- No installation of candidate ORNL software until its own public repository, license, release identifier, citation metadata, and safe input requirements are reviewed.

## Next implementation slice

Add a small Python runner under `labs/cross-layer-pilot/` using the standard library only. Keep the first fixture synthetic and commit the runner separately from later source promotions.


## Implemented local study, 2026-11-10

The [runner and reproduction instructions](cross-layer-pilot/README.md) now implement the synthetic study with registry gates, explicit approval, bounded retry, hash-linked logs, and semantic replay. The [workflow dossier](../guide/project-dossiers/workflow-software-and-local-reconstruction.md) supplies the inspected public software context and keeps the local design distinct from ORNL implementations.
