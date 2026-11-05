# Research manifest

This file records the reproducibility boundary for the living atlas. The table below is a historical published-state snapshot, not a claim that the present checkout is on `main` or that later work has been published. It does not preserve private browsing history, credentials, or model state.

## Historical snapshot: 2026-11-02

| Field | Value |
|---|---|
| Repository | `zaxpointx/ornl-public-tech-research` |
| Branch | `main` |
| Snapshot date | 2026-11-02 |
| Catalog rows | 69 |
| Project briefs | 67 |
| Signals files | 40 |
| Completed deep dives | 6 |
| Verification boundary | Public sources only |
| Structural audit | `python3 scripts/audit_atlas.py` |

## Reproduction procedure

1. Check out the repository at the edition or snapshot commit.
2. Read [the methodology](methodology.md), [the rules](../RULES.md), and [the publication workflow](publication-workflow.md).
3. Recompute coverage from `discovery/catalog.csv`, `projects/`, and `signals/`.
4. Run the structural audit and preserve its output with the review record.
5. Re-fetch load-bearing sources listed in the relevant brief, deep dive, or verification ledger.
6. Record source changes as corrections or new evidence; do not silently rewrite historical findings.

## Known boundaries

- Public pages, repositories, papers, reports, and documentation can change or disappear.
- A public repository is evidence about a published artifact, not proof of a complete internal system.
- Missing public evidence is recorded as unknown or not found; it is not evidence that a project, user, or relationship does not exist.
- Counts are a snapshot and must be regenerated after catalog or corpus changes.

## In-progress public research expansion

Research added after the snapshot is navigable from the [public research guide](public-research-guide.md) and its [evidence ledger](public-research-sources.md). It is an incomplete working edition, not a frozen or independently verified release. Its source retrieval dates and known limitations are recorded in the ledger, while the [coverage matrix](coverage-matrix.md) and [verification log](../verification/log.md) describe open work and checks. The current branch, staged changes and commit status must be determined from Git rather than inferred from this historical table. No exact commit is asserted for the uncommitted expansion.

## Future edition fields

Before cutting a numbered edition, add the exact snapshot commit, catalog checksum, source-freeze date, audit version, release notes link, and archive identifier here.
