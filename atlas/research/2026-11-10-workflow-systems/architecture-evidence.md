# INTERSECT SDK and DataFed: contracts rather than a guessed integrated stack

Research date: 2026-11-10. Evidence packet for Atlas integration. Public read-only research; no software installed, facility APIs used, credentials used, or repositories cloned.

## Research contract and existing context

Target: INTERSECT open architecture, its Python SDK, and DataFed's data-record/provenance model. Purpose: identify technically precise ideas that Hermes and Codex can study locally. Comparison: message contracts versus scientific artifact contracts. Durable output: this file. Unknown without direct evidence: deployed facility topology, production maturity, complete ownership, and a shared INTERSECT/DataFed installation. Existing context read: `guide/project-dossiers/intersect-and-smart-labs.md`, `guide/source-ledger.md` relevant entries, and `registry/software.json`. This extends the existing software-discovery leads rather than replacing prior findings.

## Sweep 1: discovery and reconstruction

### Main discovery

**DIRECT:** INTERSECT has a publicly inspectable Python SDK, not only a conceptual architecture. Its generated schema and runtime code expose concrete boundaries for typed service calls, request correlation, events, and data transport. **DIRECT:** DataFed's published record model separates searchable metadata and typed provenance links from raw scientific files. **INFERRED:** These are complementary ideas for a local research workflow: validate an operation before execution, then preserve the identity and ancestry of its output. They do not establish an actual integrated ORNL stack. [A01–A09]

### System walkthrough

**INTERSECT public SDK:** a client supplies a destination, a capability operation, and input data. A service wraps user-defined capabilities, validates messages, invokes application logic, and returns a response to the source. Capabilities expose decorated, type-annotated functions; declared events provide asynchronous notifications. Message brokers carry control traffic; selected handlers can move response data through another data plane. Domain logic and any instrument-specific messaging remain the application's responsibility. [A02–A05]

```text
client request -> broker -> service message validation -> capability method
                 <- correlated response / error <- output serialization
capability event -> named event -> subscribed client or service
```

The generated hello-world schema provides a concrete example: `HelloExample.say_hello_to_name` accepts a JSON string and returns a JSON string. The request/response header schema includes `message_id`, `campaign_id`, `request_id`, `source`, `destination`, `created_at`, `sdk_version`, and `operation_id`. Operation names combine capability and function. The header has a data-handler field, while events have capability and event names. The schema identifies AsyncAPI 2.6.0. This is the published example at the pinned revision, not a promise that any arbitrary JSON document with those names is wire-compatible. [A03]

**DataFed public model:** a data record holds identifiers, title, descriptive fields, domain metadata, and dependency links. Raw-file contents remain separate from the central metadata graph. The published documentation describes Globus transfers to/from storage repositories, while the README distinguishes central services/database from repository services near raw storage. This supports location-independent data management without turning the metadata database into a raw-file store. [A06–A08]

```text
scientific file -> repository raw storage
              -> record: ID + metadata + typed dependencies
analysis output record --is derived from--> input record
```

The dependent record is the subject: if `result` derives from `measurement`, the edge belongs to `result` and points to `measurement`. The protobuf enum explicitly distinguishes derived-from, component-of, and newer-version-of. A graph request takes a record ID. The record protobuf carries metadata, storage/source information, schema ID/version, and dependency data. [A07–A09]

### Contracts and practical consequences

| Boundary | Publicly documented behavior | Local design implication, labeled INFERRED |
|---|---|---|
| Operation input/output | Generated schema plus request adapters and output serialization in SDK code | Reject malformed input before a task starts; validate generated output too |
| Request correlation | Distinct message, request, and campaign IDs in SDK example | Separate an individual delivery from a logical request and experiment campaign |
| Status versus result | SDK exposes status functions separately from message endpoints | A healthy worker is not evidence that its scientific result is valid |
| Control versus data | Broker configuration and selectable data transfer handlers | Log a small control envelope; store larger artifacts separately |
| Artifact lineage | DataFed typed dependencies point from dependent to upstream record | A changed input can identify downstream results needing review |
| Metadata versus bytes | DataFed central records exclude raw data; metadata is independently searchable | Store an artifact hash and structured metadata without embedding whole files |

The hashing, immutable event log, local JSON representation, and transitive invalidation logic proposed here are **our design choices**, not claims that DataFed uses those mechanisms. [A03, A07–A09]

### Version, license, and maturity boundary

GitHub's public commits API returned these default-branch heads during this pass:

- Python SDK: `d7e9763afac7e058b45212f35b37376bb706fbbb`, committer timestamp 2026-07-29T01:21:34Z. Its pinned `pyproject.toml` declares package version 0.9.3, Python >=3.10,<4.0, and dependency `intersect-sdk-common>=0.9.6,<0.10.0`. The different version number in the schema's `x-intersect-version` must not be mistaken for the Python package version. BSD-3-Clause license. [A01, A03, A10]
- DataFed: `361945a31ffb77c6c9b359f58fd3e364e5527277`, committer timestamp 2026-09-22T04:09:17Z. The license is the repository's custom UT-Battelle open source license; do not relabel it BSD or MIT. The README distinguishes semantic component versions from calendar release versions. [A06, A09, A11]
- INTERSECT architecture documentation displays v1.0 and CC BY 4.0. This is an architecture-document version, not an installed SDK version. [A12]

These are inspected public artifacts, not proofs that the same revisions run at ORNL. No upstream tests were executed. Test presence proves publicly specified expected behavior, not passing behavior in this environment.

### Source ledger

All sources below were directly retrieved on 2026-11-10. Publication date is unknown unless explicitly stated. Raw source URLs are pinned to the inspected commit; hosted documentation may drift.

**A01. Python SDK project manifest**, INTERSECT-SDK contributors. URL: https://github.com/INTERSECT-SDK/python-sdk/blob/d7e9763afac7e058b45212f35b37376bb706fbbb/pyproject.toml

- DIRECT excerpt: `version = "0.9.3"`; `"intersect-sdk-common>=0.9.6,<0.10.0"`.
- Supports: package version and dependency boundary. Limit: a package manifest does not establish a deployed environment.

**A02. Core Concepts**, INTERSECT Python SDK documentation. URL: https://intersect-python-sdk.readthedocs.io/en/latest/core_concepts.html

- DIRECT excerpt: “all parameters and return values must contain a valid type annotation.”
- Supports: typed capability boundary; decorators and events described on the same page.
- Contradiction/limitation: this page describes a single capability and always requiring MinIO, whereas pinned service code accepts a capability list and pinned examples/tests show conditional MinIO requirements. Prefer pinned code for that behavior.

**A03. Generated hello-world schema**, INTERSECT-SDK contributors. URL: https://github.com/INTERSECT-SDK/python-sdk/blob/d7e9763afac7e058b45212f35b37376bb706fbbb/examples/1_hello_world/hello_service_schema.json

- DIRECT excerpt: `"asyncapi": "2.6.0"`; `"request_id"`; `"campaign_id"`; `"operation_id"`.
- Supports: concrete header and payload contracts, request correlation, hierarchy-shaped service title. Limit: checked-in generated example, not a compatibility test.

**A04. Service implementation**, INTERSECT-SDK contributors. URL: https://github.com/INTERSECT-SDK/python-sdk/blob/d7e9763afac7e058b45212f35b37376bb706fbbb/src/intersect_sdk/service.py

- DIRECT excerpt: `request_obj = fn_meta.request_adapter.validate_json(`.
- Supports: runtime validation; constructor accepts a list of capabilities; schema generation excludes unavailable data handlers. Limit: this was source inspection, not execution.

**A05. Runtime schema rejection test**, INTERSECT-SDK contributors. URL: https://github.com/INTERSECT-SDK/python-sdk/blob/d7e9763afac7e058b45212f35b37376bb706fbbb/tests/unit/test_invalid_schema_runtime.py

- DIRECT excerpt: `def test_minio_not_allowed_without_config`.
- Supports: a capability selecting MINIO must configure that data plane; constructor rejection is tested before requiring a live broker. Limit: test not executed here. Basic example configures only a broker: https://github.com/INTERSECT-SDK/python-sdk/blob/d7e9763afac7e058b45212f35b37376bb706fbbb/examples/1_hello_world/hello_service.py

**A06. DataFed README**, ORNL/DataFed contributors. URL: https://github.com/ORNL/DataFed/blob/361945a31ffb77c6c9b359f58fd3e364e5527277/README.md

- DIRECT excerpt: “Core Database - Central database containing records, metadata, and relationships - everything but raw data”.
- Supports: service decomposition, central metadata versus federated storage. Limit: README still references a BUILD.md location; deployment instructions require separate verification.

**A07. System Overview**, DataFed 1.4 documentation. URL: https://ornl.github.io/DataFed/system/overview.html

- DIRECT excerpt: “includes a direction and a type.”
- Supports: record fields, direct provenance links, dependent-to-upstream orientation, Globus raw-file movement, and annotations propagating to dependent records.
- Limit: documentation version is 1.4 and contains future-feature wording; it is not a current deployment inventory. It describes owner assessment/activation of propagated annotations, not automatic scientific invalidation.

**A08. CLI reference**, DataFed 1.4 documentation. URL: https://ornl.github.io/DataFed/user/cli/reference.html

- DIRECT excerpt: “Fail on metadata validation errors”.
- Supports: `--schema-enforce`; dependencies use `der`, `comp`, `ver`; metadata must define a JSON object. Limit: opt-in CLI schema enforcement is not proof that every DataFed metadata write is universally enforced.

**A09. Protobuf data contracts**, ORNL/DataFed contributors. URLs:

- https://github.com/ORNL/DataFed/blob/361945a31ffb77c6c9b359f58fd3e364e5527277/common/proto3/common/enums/dependency_type.proto
- https://github.com/ORNL/DataFed/blob/361945a31ffb77c6c9b359f58fd3e364e5527277/common/proto3/common/messages/dependency_spec_data.proto
- https://github.com/ORNL/DataFed/blob/361945a31ffb77c6c9b359f58fd3e364e5527277/common/proto3/common/auth/record_get_dependency_graph_request.proto
- https://github.com/ORNL/DataFed/blob/361945a31ffb77c6c9b359f58fd3e364e5527277/common/proto3/common/messages/record_data.proto

DIRECT excerpts: `DEP_IS_DERIVED_FROM = 0;`; `DEP_IS_COMPONENT_OF = 1;`; `DEP_IS_NEW_VERSION_OF = 2;`; `repeated DependencyData deps = 20;`.
Supports: explicit typed edges, record graph query, structured record contract. Limit: a protobuf schema is not the database's complete integrity policy.

**A10. SDK license**, INTERSECT-SDK contributors. URL: https://github.com/INTERSECT-SDK/python-sdk/blob/d7e9763afac7e058b45212f35b37376bb706fbbb/LICENSE

DIRECT excerpt: “BSD 3-Clause License”. Supports: license identification only.

**A11. DataFed license**, UT-Battelle. URL: https://github.com/ORNL/DataFed/blob/361945a31ffb77c6c9b359f58fd3e364e5527277/LICENSE.md

DIRECT excerpt: “DataFed, Version 1”; “OPEN SOURCE LICENSE”. Supports: custom license identification; read full conditions before redistributing derivative code.

**A12. Architecture Concept**, INTERSECT architecture documentation. URL: https://intersect-architecture.readthedocs.io/en/latest/concept.html

DIRECT excerpt: “Science Use Case Design Patterns”; “System-of-Systems Architecture”; “Microservices Architecture”. Supports: separation of scientific objective, system composition, and service implementation. Limit: normative architecture does not prove operational deployment.

## Sweep 2: verification and repair

This packet was re-read after discovery. Load-bearing pinned source files were re-fetched to check the excerpts and version boundary. Verification passed: eight pinned raw sources were re-fetched and all 14 literal excerpt/version checks passed. Hosted documentation was separately fetched during this pass. This verifies the cited strings and revisions, not upstream executable behavior. Specific repairs from the first interpretation:

1. Replaced the broad claim “MinIO is always required” with conditional data-plane configuration. Pinned hello-world has only broker configuration; the pinned MINIO test rejects MINIO handlers lacking configuration. Hosted core-concepts documentation is inconsistent here. [A02, A04, A05]
2. Did not turn DataFed's dependency-aware annotations into fully automatic invalidation. The overview includes owner impact assessment and activation. Transitive invalidation in a toy experiment would be our mechanism. [A07]
3. Did not treat SDK package 0.9.3 and schema/common 0.9.6 as contradictory release identities. They belong to different packages. [A01, A03]
4. Did not label the custom DataFed license as BSD. [A11]
5. Did not promote the existing Atlas's candidate cross-stack link into established integration.

Disconfirmation searches: `site:github.com/INTERSECT-SDK "DataFed"`, `site:ornl.gov INTERSECT DataFed integration`, and `site:github.com/ORNL/DataFed INTERSECT`. Results included separate project and architecture surfaces and adjacent presentations. No inspected source bound the reviewed SDK revision to a concrete DataFed adapter or joint deployed workflow. This is bounded searched-but-not-established evidence, not proof that integration does not exist. No production status, named service owner, or present facility endpoint is inferred.

## Most useful local experiment

Build a synthetic three-stage measurement -> reduction -> analysis workflow. A typed local request envelope carries request and campaign IDs. Each stage validates inputs and emits a result record with content hash and explicit parent IDs. Replay should reproduce the same scientific outputs. Inject malformed input, duplicate deliveries, and a changed upstream artifact; test that malformed input produces no successful artifact, duplicates do not silently duplicate scientific effects, and changed ancestry identifies downstream records for review.

This is an **Atlas-authored reconstruction of design principles**. It does not run the SDK, implement its wire protocol, use DataFed servers, simulate scientific facility accuracy, or establish ORNL uses our hashes/replay/deduplication algorithm. A later, separate experiment could exercise a pinned SDK hello-world with a local broker, once dependency and infrastructure choices are reviewed. No new dependencies are needed for the principle-level experiment.

## Stopping boundary

Well established: published SDK contract shape, separation of capability and transport, DataFed record/dependency model, license identities, and pinned source revisions. Inferred: complementary use in a local workflow. Unknown: deployed cross-stack integration, actual facility schemas, current operational topology, and scientific validity of any local surrogate. Further research should inspect SDK-common transport implementation and DataFed graph/update tests before claiming delivery guarantees or dependency mutation rules. Broad searches are unlikely to change the basic distinction between message contracts and artifact lineage; targeted source inspection can improve compatibility detail.
