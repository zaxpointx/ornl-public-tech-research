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
| Catalog entries | 74 | Public projects currently in scope |
| Project briefs | 72 | Entries with a project-level research file |
| Missing briefs | 2 | Explicitly uncovered or stub/unknown entries; not silently treated as complete |
| Signals files | 45 | Public-trace analyses; coverage is intentionally narrower than briefs |
| Existing deep dives | 6 | Listed in INDEX; their forms vary |

The structural audit prints the current missing IDs and status totals on every run. A missing brief is not automatically an error: some entries are intentionally OSTI-only stubs or unresolved public leads. Active entries without briefs are the highest-priority completion queue.

## Priority completion queue

The previous queue incorrectly listed five entries that already have briefs. The structural audit on 2026-11-04 identifies `cpad` and `cincinnatus` as the two catalog entries without briefs; both remain OSTI-only stubs under RULES.md. Do not turn a stub into a full brief without the required public documentation.

The [public research guide](public-research-guide.md), [facilities and roles guide](facilities-instruments-roles.md), [isotope story](isotopes-and-hot-cells.md), [autonomous science story](autonomous-science.md), [additive story](intersect-additive-story.md) and selected [relationship index](research-relationships.md) are incomplete first batches, not a finished edition. Remaining work: source-backed representative research for every directorate; fuller facilities/instruments and dated professional credits; additional autonomy and isotope/hot-cell topics; broader relationship coverage and a machine-readable schema if needed; broader source rechecks and citation validation; and reconciliation of remaining stale editorial documents.

Workstation blocker recorded 2026-11-04: the requested local commit failed because the configured signing key requires an interactive passphrase. The signing key and configuration were not changed or bypassed. The research batch remains uncommitted on the requested branch. Direct-origin link checks are also partially blocked by HTTP 403; see the source ledger for the affected pages and successful public extraction.

Navigation blocker recorded 2026-11-04: creating a repository-level `AGENTS.md` was explicitly blocked without user consent and the file was not created. The recorded response does not establish why approval was not given. Do not retry or work around the protected-file control. The ordinary README and reading-order documents link the shared corpus for human readers and assistants; a protected agent-instruction entry point remains pending explicit approval.

## Editorial rule

Do not describe the book as complete while any chapter or catalog entry is only a placeholder. If a future edition intentionally excludes an entry, record the reason in `verification/not-found.md` or the relevant batch file and preserve the exclusion in the edition manifest.


## Cross-domain expansion, 2026-11-10

The [whole-portfolio map](portfolio-map.md) now covers all 69 existing catalog entries across ten catalog domains and exports 33 selected relationship propositions with their evidence labels and ledger context. This is navigation over inherited research, not a new verification of every historical claim. The [technical research expansion](portfolio-expansion-2026-11-10/README.md) deepens computing/instruments, materials/biology, energy/Earth and population uncertainty. New research sections are not silently counted as new catalog briefs. Existing totals remain 69 catalog rows, 67 briefs and 40 signals files. The two OSTI-only stubs remain unfilled.


## Batch 13, 2026-11-11

[Batch 13](../batches/batch-13.md) adds five catalog rows: ADIOS2, Celeritas, DEDFoam, ChatHPC and MATEY. All five are verified with two sweeps, which brings totals to 74 rows, 72 briefs and 45 signals files. The two OSTI-only stubs are still unfilled. The counts in the 2026-11-10 section above describe that date. The new [engineering patterns guide](../lessons/engineering-patterns.md) adds a code-level synthesis, which is separate from the catalog count.
