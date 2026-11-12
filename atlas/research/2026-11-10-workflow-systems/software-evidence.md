# Flowcept and Zambeze: repository evidence

Retrieved 2026-11-10. Public-source software track; no packages installed, no repositories cloned, no upstream actions performed. Existing agentic-workflow and INTERSECT dossiers and their software lead descriptions were read first. Scope: how these two published artifacts work, their actual connection, and useful local experiments. Internal facility deployments, complete software inventories, and current operational ownership remain unknown.

## Sweep 1: discovery and reconstruction

### Revision boundary

GitHub repository and commit APIs were fetched directly, then source files were fetched from raw.githubusercontent.com at the returned commit. These are inspected snapshots, not claims about installed versions or latest package releases.

| Project | Default branch snapshot | Commit timestamp reported by API | Package metadata |
|---|---|---|---|
| Flowcept | `c000b10ea49659af6c5821b61918f3893bd46a92` | 2026-07-20T16:03:48Z | Python >=3.11; dynamic version |
| Zambeze | `13875a1e9186c9398df56faef0be3c84cd8bd1a9` | 2024-09-13T14:26:54Z | Python >=3.10; version 0.2 |

Sources: [Flowcept commit API](https://api.github.com/repos/ORNL/flowcept/commits/c000b10ea49659af6c5821b61918f3893bd46a92), [Zambeze commit API](https://api.github.com/repos/ORNL/Zambeze/commits/13875a1e9186c9398df56faef0be3c84cd8bd1a9), [Flowcept package](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/pyproject.toml), [Zambeze package](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/pyproject.toml). API timestamps do not prove continued maintenance or abandonment.

### Flowcept: what it does

DIRECT: Flowcept captures execution provenance. Its published offline path records instrumented Python functions into JSONL without an external broker/database; its distributed path buffers provenance, publishes common-schema messages, and persists them through keeper/consumer services. It is an observation and lineage layer, not proof of a scientific scheduler. [README](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/README.md), [architecture](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/docs/architecture.rst).

The capture inputs are task arguments, returned values, identifiers, timing, and optional telemetry. Capture can come from direct instrumentation or observability adapters watching other software. Messages can flow through Redis, RabbitMQ, Kafka, or Mofka; documented stores include MongoDB and LMDB. The documentation describes independent deployment and configurable flushing. These are documented capabilities, not measured performance results in Atlas. [Architecture](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/docs/architecture.rst).

```text
instrumented function / observed service
  -> task records + workflow identity
  -> local JSONL OR buffered message stream
  -> optional persistent provenance store
  -> lineage queries / reports / UI / agent tools
```

DIRECT: `TaskObject` has `used`, `generated`, `task_id`, `workflow_id`, `campaign_id`, `activity_id`, `status`, timestamps, dependency/dependent IDs, and agent identifiers. Task records can include environment and telemetry fields. A local experiment can borrow the separation of task identity, input/output lineage, and execution status without claiming to implement the Flowcept schema. [TaskObject](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/src/flowcept/commons/flowcept_dataclasses/task_object.py).

DIRECT: The schema documentation separates workflow, task, and blob/object records and describes PROV-AGENT activity subtypes `ai_model_invocation` and `agent_tool`. This supplies a useful distinction for future Hermes experiments: preserve tool executions and model calls as separate activities rather than saving only the final answer. [Schemas](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/docs/schemas.rst).

DIRECT: The README exposes Python, CLI, REST, UI, and MCP-facing analysis paths. MCP capabilities are a future integration opportunity, not a configured Atlas capability. Neither MCP setup nor LLM credentials were accessed in this research. [README](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/README.md).

### Zambeze: what it does

DIRECT: Zambeze describes distributed scientific task orchestration across large-scale and edge systems. Its simple example constructs a `ShellActivity`, supplies file URIs, wraps it in `Campaign`, and dispatches it. The example requires ImageMagick. [README](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/README.md), [example](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/examples/imagemagick_files.py).

DIRECT: The inspected `Campaign._pack_dag_for_dispatch()` builds a sequence of activity nodes between monitor and terminator nodes and attaches predecessor/successor metadata. `dispatch()` sends the serialized DAG through ZeroMQ request/reply communication. Although the underlying graph type supports directed graphs, this inspected campaign builder constructs a chain; do not describe this constructor as an arbitrary branching workflow planner. [Campaign](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/src/zambeze/campaign/campaign.py), [DAG](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/src/zambeze/campaign/dag.py).

DIRECT: The agent's message handler receives a campaign via ZeroMQ, unpacks nodes, and places activity messages on RabbitMQ. It checks configured plugin availability before acknowledging activities. Published activity types include shell execution and Globus transfer. The executor waits for predecessor status messages and invokes plugins. [Message handler](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/src/zambeze/orchestration/agent/message_handler.py), [executor](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/src/zambeze/orchestration/executor.py).

```text
Campaign(activity list)
  -> serialized chain + dependency metadata
  -> local agent via ZeroMQ
  -> activity messages on RabbitMQ
  -> agent/plugin selection
  -> predecessor status checks
  -> shell execution or data transfer
  -> control/status messages
```

This is a reconstruction of the inspected source path, not a proof of an ORNL production deployment. Zambeze agents here are distributed orchestration processes; the term does not establish LLM-driven behavior. [Message handler](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/src/zambeze/orchestration/agent/message_handler.py).

### A direct connection, with version friction

DIRECT: Zambeze's message handler includes an optional Flowcept activation path controlled by settings. It imports `ZambezeInterceptor` and `FlowceptConsumerAPI` and starts the latter. This is stronger evidence than the previous Atlas description of thematic alignment: published Zambeze code explicitly references Flowcept integration. [Message handler, lines 70–80](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/src/zambeze/orchestration/agent/message_handler.py#L70).

DIRECT: Flowcept's inspected top-level exports do not provide either named API, and its repository tree contains no path named Zambeze. Therefore this historical integration hook is not evidence of drop-in compatibility with the inspected Flowcept snapshot. INFERRED: porting or matching a historical Flowcept revision would probably be necessary. No import/runtime compatibility test was performed, so the exact failure behavior remains unverified. [Flowcept exports](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/src/flowcept/__init__.py), [Flowcept tree API](https://api.github.com/repos/ORNL/flowcept/git/trees/c000b10ea49659af6c5821b61918f3893bd46a92?recursive=1).

UNKNOWN: No reviewed source establishes that Zambeze, current Flowcept, DataFed, and INTERSECT compose one currently deployed stack. Preserve this boundary even though one historical pairwise hook is now documented.

### Reproducibility and maturity

Both inspected LICENSE files state MIT License and attribute copyright to Oak Ridge National Laboratory. Source availability and licensing are established; facility maturity and service availability are not. [Flowcept license](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/LICENSE), [Zambeze license](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/LICENSE).

Flowcept's offline CI workflow installs dependencies, creates a full-offline configuration, checks that brokers/databases are disabled, and invokes its offline tests. Zambeze's unit CI workflow uses Python 3.10 and runs marked unit tests. These files demonstrate intended testing workflows; Atlas did not run their suites or establish that the latest CI runs passed. [Flowcept offline CI](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/.github/workflows/run-tests-offline.yml), [Zambeze unit CI](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/.github/workflows/tests.yml).

Zambeze's published dependencies include pyzmq, dill, networkx, SQLAlchemy, Globus SDK, and pika; its compose file supplies RabbitMQ. Flowcept's minimal dependencies include OmegaConf, NumPy, MessagePack, orjson, and Rich, with additional functionality in extras. This explains why a standard-library study proxy is smaller than installing either upstream system for this first batch. [Zambeze dependencies](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/pyproject.toml), [compose](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/compose.yaml), [Flowcept dependencies](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/pyproject.toml).

## Evidence ledger

All entries below are DIRECT observations of publisher ORNL's public repository snapshots, retrieved 2026-11-10. File publication dates are not independently established; commit timestamps above describe snapshot boundaries. Quotes are deliberately short; the linked complete files support the accompanying paraphrases.

| ID | Primary source | Exact excerpt or observed code datum | Supports / limitation |
|---|---|---|---|
| SW-F01 | [Flowcept README](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/README.md) | “This minimal example needs no database, broker, or external service.” | Offline capture documented; not executed here |
| SW-F02 | [Flowcept architecture](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/docs/architecture.rst) | “all provenance messages follow a **common schema**” | Buffer/broker/keeper architecture; no local overhead measurements |
| SW-F03 | [TaskObject](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/src/flowcept/commons/flowcept_dataclasses/task_object.py) | `used`, `generated`, `dependencies`, `workflow_id` | Explicit lineage fields; not sufficient for semantic correctness |
| SW-F04 | [Schemas](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/docs/schemas.rst) | `ai_model_invocation`, `agent_tool` | Agentic activity classification; not proof of any Atlas integration |
| SW-F05 | [Flowcept package](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/pyproject.toml) | `requires-python = ">=3.11"` | Snapshot install requirement; package release not resolved |
| SW-F06 | [Flowcept license](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/LICENSE) | “MIT License” | License at pinned snapshot |
| SW-Z01 | [Zambeze README](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/README.md) | “Zambeze is a distributed task orchestration system” | Project purpose; no production claim |
| SW-Z02 | [Campaign](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/src/zambeze/campaign/campaign.py) | `_pack_dag_for_dispatch`, `dag.add_edge(last_activity, activity.activity_id)` | Sequential builder path |
| SW-Z03 | [Message handler](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/src/zambeze/orchestration/agent/message_handler.py) | `from flowcept import ZambezeInterceptor, FlowceptConsumerAPI` | Historical integration hook; current compatibility unknown |
| SW-Z04 | [Zambeze package](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/pyproject.toml) | `version = "0.2"`; `requires-python = ">=3.10"` | Repository package metadata; not latest registry release |
| SW-Z05 | [Zambeze license](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/LICENSE) | “MIT License” | License at pinned snapshot |
| SW-F07 | [Flowcept exports](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/src/flowcept/__init__.py) | Neither Zambeze import name is exported | Version mismatch evidence; not executed |

## Sweep 2: verification and repair

The first reconstruction was reread against the fetched files. Load-bearing integration files were fetched again: Zambeze message handler and current Flowcept `__init__.py`; repository trees and dependency metadata were checked. Repairs and boundaries:

- Upgraded only the Flowcept–Zambeze pairwise relationship from thematic similarity to historical code-level integration hook.
- Immediately qualified it with missing current export names. Did not claim a working integration.
- Replaced broad “DAG planner” wording with the actual sequential campaign builder behavior.
- Kept agent terminology separate from LLM agents.
- Did not treat repository CI definitions as passed tests, README performance descriptions as measurements, or public code as production proof.
- Executor inspection found commented-out checks and TODOs concerning shell failure handling. This is a reason to test failure propagation explicitly in a study proxy; it is not a fully reproduced upstream bug report. [Executor](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/src/zambeze/orchestration/executor.py).

## Useful experiments and next evidence

1. **Local, dependency-free provenance runner:** synthetic task chain with explicit dependencies, captured inputs/outputs, failure injection, and downstream blocking. Measure how missing lineage or false success changes conclusions. This is our reconstruction, with no upstream schema-compatibility claim.
2. **Future upstream Flowcept comparison:** after choosing and pinning a package release, run its offline quickstart in an isolated project environment and compare task/input/output counts with the local runner. Requires dependency approval only if project policy adds it; not performed in this track.
3. **Future Zambeze compatibility study:** identify the Flowcept revision that exported the historical interceptor, then assess migration to the current capture API. First target should be a local shell fixture, not Globus credentials or facilities.

Searched/inspected but not established: current package release compatibility; operational deployments; complete distributed reliability semantics; DataFed integration; end-to-end pairing of current Flowcept with Zambeze; source-to-production continuity. Searches used Flowcept/ORNL provenance and Zambeze/ORNL orchestration terms; repository inspection narrowed the result to the two public snapshots. The Flowcept publication index supplies follow-up papers, including PROV-AGENT and the 2025 XLOOP agent experiment, but those papers were not fully reconstructed in this software track. [Publication index](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/docs/publications.rst).

Stopping boundary: sufficient evidence for capture-versus-orchestration architecture, local study design, and a historically explicit connection with current version friction. Further research is likely to change compatibility and deployment conclusions; it is unlikely to remove the basic distinction between orchestration and execution provenance.
