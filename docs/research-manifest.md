# Research manifest

This file records the reproducibility boundary for the current living edition. It describes the published repository state; it does not claim to preserve private browsing history, credentials, or model state.

## Snapshot

| Field | Value |
|---|---|
| Repository | `zaxpointx/ornl-public-tech-research` |
| Branch | `main` |
| Snapshot date | 2026-10-24 |
| Catalog rows | 66 |
| Project briefs | 48 |
| Signals files | 40 |
| Completed deep dives | 3 |
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

## Future edition fields

Before cutting a numbered edition, add the exact snapshot commit, catalog checksum, source-freeze date, audit version, release notes link, and archive identifier here.
