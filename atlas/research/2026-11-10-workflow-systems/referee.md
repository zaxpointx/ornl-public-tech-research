# Independent research referee

Review date: 2026-11-10. Reviewer: software-research subagent acting as a second-sweep referee of the separate architecture packet and parent integration. This is independent of the architecture discovery track; it is not an independent review of the reviewer's own software packet.

## Architecture packet verification

Read `architecture-evidence.md` in full. Independently fetched nine pinned files: SDK package manifest, SDK license, generated hello schema, service implementation, schema rejection test; DataFed README, custom license, dependency enum, record protobuf. All 17 literal/version checks matched the fetched source. Re-read DataFed's hosted overview and CLI reference, stripping HTML to verify provenance orientation and opt-in schema enforcement. Hosted ReadTheDocs pages returned HTTP 403 through Python urllib but were fetched successfully with the web tool; the difference is retrieval-channel behavior, not evidence of missing documentation.

Confirmed load-bearing points:

- SDK package 0.9.3 and common dependency >=0.9.6,<0.10.0 are separate version identities.
- SDK license is BSD 3-Clause; DataFed's inspected license is custom UT-Battelle text.
- Generated example contains request/campaign/operation fields and AsyncAPI 2.6.0.
- Runtime service validates request JSON; a source-level test rejects MINIO selection without its configuration. Test existence is correctly separated from test execution.
- DataFed dependent records point upstream. Its annotation propagation includes impact assessment, so Atlas must not describe automatic scientific invalidation as documented DataFed behavior.
- CLI schema enforcement is an option, not proof every write is enforced.
- INTERSECT hosted core-concepts text requires MinIO more broadly than the pinned examples/test. Packet preserves that discrepancy rather than silently combining versions.
- INTERSECT architecture concept page displays v1.0 and CC BY 4.0 and distinguishes science patterns, system composition, and microservices.

Primary URLs checked: the exact pinned A01, A03–A06, A09–A11 URLs in [architecture evidence](architecture-evidence.md), plus [DataFed overview](https://ornl.github.io/DataFed/system/overview.html), [DataFed CLI](https://ornl.github.io/DataFed/user/cli/reference.html), [SDK core concepts](https://intersect-python-sdk.readthedocs.io/en/latest/core_concepts.html), and [architecture concept](https://intersect-architecture.readthedocs.io/en/latest/concept.html).

No substantive unsupported architecture connection, license label, or maturity assertion found. Remaining uncertainty: upstream tests were not run; delivery guarantees, facility deployment, present service owners, and interoperability between these snapshots remain unestablished. The packet labels local hashing, replay, deduplication, and invalidation as Atlas design choices.

## Integration review

Reviewed the complete diff of `registry/sources.json`, `projects.json`, `software.json`, and `edges.json` after parent integration. Source identifiers agree across the additions. The local experiment remains `local`, and the only new external software-to-software edge is expressly historical/optional, with current compatibility untested. License URLs and labels match inspected primary files. No operational ownership or common deployed stack is asserted by those additions.

Independently retrieved the three parent-added primary sources: OSTI paper 2000417 (PDF fetched through urllib and extracted with pdftotext after the web tool returned 502), the hosted Scientific Data Layer page, and INTERSECT's raw DMS specification. The paper confirms microscopy/compute/scientific-orchestrator decomposition and synthetic digital twins used during software development; SDL's URI-addressable-resource excerpt matches; DMS describes tiers 0–III and the cited repository/catalog sentence. The paper excerpt in the registry normalizes PDF line breaks. These sources support the limited recorded claims, not a common DataFed deployment or scientifically accurate local simulator.

Subsequent final prose pass read `guide/project-dossiers/workflow-software-and-local-reconstruction.md` and `guide/agent-entrypoint.md` in full. The dossier correctly preserves historical-hook/current-compatibility boundaries, calls the local runner Atlas-authored, and separates architecture specifications from facility deployments. The agent entry point states it reads only public registries and does not configure Hermes. No substantive research repair was required.

## Local replay finding

Inspected the runner and independently reproduced a semantic replay gap against the checked-in success log using only a temporary directory. Changed `evidence_gate.snapshot.required_sources[0].promotion` to `blocked`, recomputed the snapshot fingerprint and event hash chain, then called `replay_log`. Actual result: `{"verified_events": 8, "runs": 1, "completed": 1}`. Replay rechecks the fingerprint but does not reapply the source-verification gate to recorded snapshot content or bind the snapshot project identity to the request. This is not a hash authentication finding; the issue is accepting internally consistent metadata that should fail the runner's own evidence gate. Sent the reproduction to the parent for repair. Research claims remain supported; final executable verification must include this case after repair.

## Repair verification

After the parent/local-lab repair, reran the exact blocked-source mutation against the regenerated success log, recomputing both snapshot and chain fingerprints. Chain verification still accepted all eight events, while semantic replay now rejected it with `recorded source support is inconsistent`. Separately changed the recorded snapshot project ID, recomputed both fingerprints, and observed rejection with `recorded project does not match request`. The unchanged success log replayed eight events/one completed run; the unchanged recovery log replayed ten events/one completed run. Thus the reported replay defect is repaired in the observed code. No further findings in the requested scope.
