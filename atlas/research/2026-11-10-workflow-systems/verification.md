# Sweep 2: verification, results, and continuation handoff

Date: 2026-11-10. Outcome: **verified complete for this bounded research and local experiment batch**. Branch: `codex/workflow-evidence-lab`. Changes remain local and uncommitted; no push or publication performed.

## What changed

The batch adds a technical comparison dossier, two research evidence packets, an independent referee report, twelve source records, one comparison project, four software records (three inspected upstream projects and one local lab), six graph relationships, and repository reading links. The existing DataFed software record gains repository/revision/license information. Registry totals are now 72 sources, 19 projects, 4 facilities, 12 software records, 6 role records, and 26 edges.

The public reading path is `guide/agent-entrypoint.md` -> `scripts/atlas_query.py` -> project packet -> dossier -> pinned source/evidence packet -> local experiment. The CLI reads registries only; it neither loads personal context nor configures Hermes. Existing research and unrelated untracked files were preserved.

## Actual division of work

Three subagents worked alongside the parent: Flowcept/Zambeze research, INTERSECT SDK/DataFed research, and the isolated local lab implementation. The parent integrated registries, wrote synthesis and the reading CLI, checked primary sources, and ran repository-level verification. The software researcher subsequently refereed the other research packet and integrated prose and reproduced a local replay defect. Discovery and verification were distinct passes. Agent summaries were not accepted as source evidence.

## Research verification

Read both complete evidence packets, the integrated dossier, query code, lab implementation/tests/README, and registry diff. Parent re-fetched the pinned Zambeze integration hook, Flowcept README/architecture/export table, SDK schema/service, DataFed dependency enum, and all four license files. Seven direct raw-source checks confirmed the SDK contract, DataFed enums, and license strings. The independent referee checked 17 literal/version strings across nine pinned sources and separately checked the parent's paper, SDL, and DMS sources. See [referee](referee.md) for its actual scope and transport differences.

The paper's PDF excerpt is normalized across line breaks. Publication dates not independently established remain null in the new source records; snapshot commit timestamps in the packets are not publication dates. The DMS `main` and hosted documentation URLs may drift; pinned software revisions delimit stronger code claims.

Repairs and retained boundaries:

- Zambeze's optional Flowcept hook is a direct historical code connection. Missing corresponding exports in the inspected Flowcept revision prevent a current compatibility claim.
- A sequential campaign builder is not described as an arbitrary workflow planner.
- SDK hosted documentation and pinned source disagree about mandatory MinIO. The record preserves this rather than assuming a single consistent version.
- DataFed typed dependencies/annotations do not establish automatic scientific invalidation.
- INTERSECT's public DMS/SDL designs do not establish that DataFed is its installed implementation.
- Architecture descriptions, source code, package manifests, and CI definitions do not establish production deployment, installed releases, measured performance, or passing upstream tests.

## Local experiment results

The standard-library runner models synthetic measurement -> analysis -> independent numerical check -> threshold decision. It checks direct project source metadata and outgoing relationship evidence, requires explicit synthetic approval, bounds recovery to one requested retry, and appends hash-linked events with the relevant registry snapshot. Semantic replay rechecks recorded evidence metadata and reconstructs completed results without reading the live registry.

| Scenario exercised through CLI | Observed outcome |
|---|---|
| Approved default fixture | Exit 0; 4 samples, mean 5, threshold 4.5, accept; 8-event replay, 1 completed run |
| Injected transient failure, one retry | Exit 0; same scientific result; 10-event replay, 1 completed run |
| No approval | Exit 1; stopped before measurement; replay reports 0 completed runs |
| Injected failure, zero retries | Exit 1; recovery exhausted, no decision; replay reports 0 completed runs |
| New workflow comparison project selected | Exit 0; same synthetic result; context includes the twelve new required sources |
| Unknown Atlas query node | Nonzero exit with an explicit unknown-node message |

The meaningful experiment result is that execution failure, provenance consistency, evidence eligibility, and scientific result checks remain separate. It does not validate an ORNL instrument model or an upstream implementation.

The referee found that a rehashed blocked-source snapshot initially passed semantic replay. The implementation now shares recorded-snapshot validation with replay, includes relationship source/endpoint support, and binds request/project identity. Regression tests and the referee's exact reproduction now reject it. Numeric validation also rejects excessively large integers cleanly; threshold decisions use `statistics.mean` after the separate scaled-sum cross-check to avoid rounding-induced classification differences.

## Checks run and results

- `python3 -m unittest discover -s labs/cross-layer-pilot -v`: **20 passed**.
- `python3 -m unittest discover -s tests -v`: **3 passed**.
- `python3 scripts/validate_registry.py`: **registry valid** with totals above.
- `sh scripts/check-links.sh`: **16 PASS, zero WARN**, exit 0. This existing script covers README/project dossiers, not the entire repository.
- Additional concurrent HTTP checks of all twelve newly registered primary URLs: **12 HTTP 200**, zero warnings.
- `python3 -m py_compile scripts/atlas_query.py labs/cross-layer-pilot/runner.py`: passed.
- Both checked-in success/recovery logs passed semantic replay. Tests also exercise append/repeat behavior, false decisions and changed measurements in recomputed chains, missing or blocked evidence, project mismatch, context/relationship omissions, and threshold edge cases.
- Queried new project and Zambeze nodes: valid JSON, evidence states/limitations retained. New project packet includes 14 sources after neighboring DataFed context is included, not twelve duplicated records.
- Final diff/whitespace and local-link checks: passed. No dependency manifest or lint configuration exists for this standard-library slice; no dependencies were added.

## Limits and next work

No upstream ORNL package, facility API, broker, database, MCP integration, or model was executed. The local hash chain is not a signature or secure audit service. Semantic replay checks consistency, not authorship, authenticity, or scientific truth; a coherently rewritten entire run can still pass. One writer per output file. Completed synthetic results are replayable; restart/resume, distributed delivery guarantees, duplicate-request deduplication, and adaptive scientific optimization are not implemented.

Best next bounded task: run a pinned upstream Flowcept offline example in an isolated local environment and compare captured events/lineage with this explicit baseline, including a failed task. Keep upstream results separate from the local proxy. Other promising follow-ups are the historical Zambeze API compatibility study, SDK broker-backed contract tests, and an offline downstream-impact graph. See the [dossier's ranked opportunities](../../guide/project-dossiers/workflow-software-and-local-reconstruction.md).

Stop this batch here: the research question, code, regression coverage, integrated graph, and reading path are complete. Further broad searching would not change the basic execution/provenance/message/data distinction; targeted upstream execution could change compatibility conclusions. The rest of ORNL remains an ongoing Atlas research backlog, not a completeness claim.
