# Workflow software: execution, provenance, messages, and scientific artifacts

Research date: 2026-11-10. Evidence labels describe public artifacts, not facility deployments. Registry project: `project-workflow-software-reconstruction`. [Discovery and verification artifacts](../../research/2026-11-10-workflow-systems/README.md).

## What these systems do

A scientific workflow has several different coordination problems. Someone must dispatch tasks, services must agree on messages, an observer must record what actually happened, and data records must retain their scientific ancestry. The inspected public artifacts expose concrete solutions to these problems. **INFERRED:** they provide complementary design ideas for our own research tooling. **UNKNOWN:** no reviewed source establishes that all four are one deployed ORNL stack.

| System | Publicly established responsibility | Important boundary |
|---|---|---|
| [Zambeze](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/README.md) | Distributed scientific task orchestration | A distributed agent process is not necessarily an LLM agent |
| [Flowcept](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/docs/architecture.rst) | Capture, buffer, stream, persist, and query runtime provenance | Observing execution does not establish scientific correctness |
| [INTERSECT Python SDK](https://github.com/INTERSECT-SDK/python-sdk/blob/d7e9763afac7e058b45212f35b37376bb706fbbb/src/intersect_sdk/service.py) | Typed capability calls, validated requests, and service dispatch | Application-specific science and instrument logic remain outside the transport contract |
| [DataFed](https://github.com/ORNL/DataFed/blob/361945a31ffb77c6c9b359f58fd3e364e5527277/README.md) | Federated scientific data management, central records, and repository services | Central metadata is distinct from raw scientific files |

## A concrete system reconstruction

The [INTERSECT SDK framework paper](https://www.osti.gov/servlets/purl/2000417), sections 2 and 3.1, describes splitting a microscopy workflow into an instrument adapter, compute adapter, and scientific orchestrator. The adapter handles instrument interaction; analysis computes candidate locations; orchestration decides whether the experiment objective has been met. Synthetic instrument twins let developers test interfaces without occupying a microscope. This is a documented development approach, not evidence that our toy measurement model reproduces microscopy physics.

The inspected SDK's [generated hello-world schema](https://github.com/INTERSECT-SDK/python-sdk/blob/d7e9763afac7e058b45212f35b37376bb706fbbb/examples/1_hello_world/hello_service_schema.json) distinguishes message, request, and campaign IDs and names a capability operation. Its typed request and response payloads make interface assumptions inspectable. These identifiers suggest a useful local distinction between a delivery, a logical request, and a research campaign. **INFERRED:** adopting that distinction would help trace retries; it does not make Atlas messages SDK-compatible.

In a separate implementation, Zambeze's [campaign builder](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/src/zambeze/campaign/campaign.py) constructs a chain of activities with dependency information. Its [agent handler](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/src/zambeze/orchestration/agent/message_handler.py) receives campaigns through ZeroMQ and distributes activity messages through RabbitMQ. The inspected constructor is a sequential chain builder, even though the underlying graph representation is more general.

Flowcept's [task schema](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/src/flowcept/commons/flowcept_dataclasses/task_object.py) gives the observation layer concrete fields: task/workflow/campaign identity, used and generated data, dependencies, status, and timing. Its [README](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/README.md) documents offline JSONL capture as well as richer online options. This makes offline event completeness a feasible future experiment without beginning with a database deployment.

DataFed models a different relationship: an output record can point to its upstream input with a [typed dependency](https://github.com/ORNL/DataFed/blob/361945a31ffb77c6c9b359f58fd3e364e5527277/common/proto3/common/enums/dependency_type.proto). Its [overview](https://ornl.github.io/DataFed/system/overview.html) describes provenance orientation and dependency-aware annotations. A downstream result's ancestry can therefore be inspected separately from a worker's execution status. Do not equate annotations with automatic scientific invalidation; the documentation includes owner assessment.

## The connection that is actually supported

**DIRECT:** Zambeze's [pinned message handler](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/src/zambeze/orchestration/agent/message_handler.py) conditionally starts a Flowcept consumer using `ZambezeInterceptor` and `FlowceptConsumerAPI`. This establishes a historical optional integration hook.

**DIRECT:** neither name appears in the inspected Flowcept [top-level exports](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/src/flowcept/__init__.py). **INFERRED:** revision matching or porting would likely be needed. No runtime compatibility test was performed. The graph records the historical hook with this limitation, rather than calling it a working current integration.

The [INTERSECT DMS specification](https://github.com/ORNL/intersect-architecture/blob/main/sos/logical/systems/dms.rst) describes separate storage, transport, registration, and catalog layers and points to the [Scientific Data Layer](https://intersect-sdl.github.io/). That public SDL describes semantic resources, ontologies, and modular data services. This is additional evidence against assuming every INTERSECT data-management reference means DataFed. It does not establish that DataFed is absent from every deployment.

## What Atlas implements locally

The [local workflow lab](../../labs/cross-layer-pilot/README.md) is an Atlas-authored study of these principles. It uses only Python's standard library and synthetic measurements:

```text
Atlas registry -> evidence gate -> explicit synthetic approval
  -> measurement -> analysis -> independent check -> decision
       | transient failure -> bounded retry          |
       +------------ local provenance log -----------+
                         -> integrity check + semantic replay
```

The fixture `[2, 4, 6, 8]` has mean `5.0`; with threshold `4.5`, the local decision is `accept`. The interesting result is the audit behavior, not the arithmetic. A failed measurement cannot produce a decision, a retry has a finite budget, and an unapproved run cannot measure. Semantic replay recomputes science from recorded inputs and checks stage ordering. A recomputed hash chain containing a false decision must still fail replay.

Every experiment event is labeled `local`. Input, registry-snapshot, and result hashes are our design. The runner does not implement SDK wire messages, a Zambeze broker, Flowcept's schema, DataFed storage, or a physical digital twin. It proves local software behavior only. Existing context leads retain their original evidence labels; the evidence gate checks registry metadata, not live external truth.

## Reproduction and next investigations

Run the commands in the lab README; the checked-in success and recovery logs give inspectable examples. [Verification report](../../research/2026-11-10-workflow-systems/verification.md) records the checks and limitations. The [agent entry point](../agent-entrypoint.md) explains how Hermes or Codex can retrieve a public context packet without loading personal files.

Ranked next opportunities, as Atlas judgments:

1. **Flowcept offline comparison:** capture this same synthetic workflow using a pinned upstream release. Compare captured input/output lineage and failures against the explicit baseline; measure capture overhead separately. High feasibility, no facility required. Not performed here.
2. **Historical Zambeze–Flowcept compatibility:** locate the revision that exported the historical APIs, then compare it with current capture interfaces. High architectural value; more environment work and version uncertainty.
3. **SDK contract conformance:** run the pinned hello-world against a local broker and test invalid payloads and correlation. The hosted core-concepts guide and pinned code disagree about mandatory MinIO; [the evidence packet](../../research/2026-11-10-workflow-systems/architecture-evidence.md) preserves that discrepancy.
4. **Scientific dependency review:** use typed input/output records to identify results affected by an upstream revision. Begin with an offline graph and explicit human review. Automatic invalidation would be our policy, not a DataFed deployment claim.

Licenses were inspected: Flowcept and Zambeze are MIT, the SDK is BSD-3-Clause, and DataFed has a custom UT-Battelle license. Pinned revisions and license URLs are in `registry/software.json` and the two evidence packets. No upstream package or tests were run in this batch.

Update 2026-11-11: the Flowcept and Zambeze opportunities were then executed in the [Flowcept failure-provenance study](../../labs/flowcept-failure-study/README.md). Flowcept 1.0.3 offline records raised task errors well. It writes nothing when the process is killed or gets SIGTERM, which is a documented in-memory design limit with a manual `dump_buffer()` workaround. It also marks the workflow FINISHED even when the workflow raised. Zambeze's hook imports only on Flowcept v0.3.11 or older; Flowcept later retired its Zambeze adapter on purpose.
