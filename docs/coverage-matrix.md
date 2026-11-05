# Coverage matrix

This is the editorial control view of the current manuscript. The catalog remains the authoritative project list; this matrix explains how that list becomes a book.

## Book-part coverage

| Part | Subject | Current evidence | Editorial status | Next work |
|---|---|---|---|---|
| I | Scope, method, and public evidence | `GOAL.md`, `RULES.md`, `docs/methodology.md`, `verification/` | Foundation present | Draft a connected introductory chapter |
| II | Portfolio by technical domain | `INDEX.md`, `LAB-TREE.md`, `projects/`, `signals/` | Broad coverage; 2 OSTI-only stubs lack briefs | Normalize brief metadata and complete priority gaps |
| III | Deep case studies | `deep-dives/` | 6 existing deep dives listed in INDEX; the broader public research guide is a first batch | Apply chapter checklist; extend into facility science |
| IV | Connections, maturity, and unknowns | `connections/`, `lessons/`, `verification/` | Evidence exists; synthesis is incomplete | Write comparative conclusion and glossary |

## Catalog coverage

| Measure | Current value | Meaning |
|---|---:|---|
| Catalog entries | 69 | Public projects currently in scope |
| Project briefs | 67 | Entries with a project-level research file |
| Missing briefs | 2 | Explicitly uncovered or stub/unknown entries; not silently treated as complete |
| Signals files | 40 | Public-trace analyses; coverage is intentionally narrower than briefs |
| Existing deep dives | 6 | Listed in INDEX; their forms vary |

The structural audit prints the current missing IDs and status totals on every run. A missing brief is not automatically an error: some entries are intentionally OSTI-only stubs or unresolved public leads. Active entries without briefs are the highest-priority completion queue.

## Priority completion queue

The previous queue incorrectly listed five entries that already have briefs. The structural audit on 2026-11-04 identifies `cpad` and `cincinnatus` as the two catalog entries without briefs; both remain OSTI-only stubs under RULES.md. Do not turn a stub into a full brief without the required public documentation.

The [public research guide](public-research-guide.md), [facilities and roles guide](facilities-instruments-roles.md), [isotope story](isotopes-and-hot-cells.md), [autonomous science story](autonomous-science.md), [additive story](intersect-additive-story.md) and selected [relationship index](research-relationships.md) are incomplete first batches, not a finished edition. Remaining work: source-backed representative research for every directorate; fuller facilities/instruments and dated professional credits; additional autonomy and isotope/hot-cell topics; broader relationship coverage and a machine-readable schema if needed; broader source rechecks and citation validation; and reconciliation of remaining stale editorial documents.

Workstation blocker recorded 2026-11-04: the requested local commit failed because the configured signing key requires an interactive passphrase. The signing key and configuration were not changed or bypassed. The research batch remains uncommitted on the requested branch. Direct-origin link checks are also partially blocked by HTTP 403; see the source ledger for the affected pages and successful public extraction.

Navigation blocker recorded 2026-11-04: creating a repository-level `AGENTS.md` was explicitly blocked without user consent and the file was not created. The recorded response does not establish why approval was not given. Do not retry or work around the protected-file control. The ordinary README and reading-order documents link the shared corpus for human readers and assistants; a protected agent-instruction entry point remains pending explicit approval.

## Editorial rule

Do not describe the book as complete while any chapter or catalog entry is only a placeholder. If a future edition intentionally excludes an entry, record the reason in `verification/not-found.md` or the relevant batch file and preserve the exclusion in the edition manifest.
