# Coverage matrix

This is the editorial control view of the current manuscript. The catalog remains the authoritative project list; this matrix explains how that list becomes a book.

## Book-part coverage

| Part | Subject | Current evidence | Editorial status | Next work |
|---|---|---|---|---|
| I | Scope, method, and public evidence | `GOAL.md`, `RULES.md`, `docs/methodology.md`, `verification/` | Foundation present | Draft a connected introductory chapter |
| II | Portfolio by technical domain | `INDEX.md`, `LAB-TREE.md`, `projects/`, `signals/` | Broad coverage; 18 catalog entries lack briefs | Normalize brief metadata and complete priority gaps |
| III | Deep case studies | `deep-dives/` | 3 complete; additive manufacturing in progress | Apply chapter checklist to every deep dive |
| IV | Connections, maturity, and unknowns | `connections/`, `lessons/`, `verification/` | Evidence exists; synthesis is incomplete | Write comparative conclusion and glossary |

## Catalog coverage

| Measure | Current value | Meaning |
|---|---:|---|
| Catalog entries | 66 | Public projects currently in scope |
| Project briefs | 48 | Entries with a project-level research file |
| Missing briefs | 18 | Explicitly uncovered or stub/unknown entries; not silently treated as complete |
| Signals files | 40 | Public-trace analyses; coverage is intentionally narrower than briefs |
| Completed deep dives | 3 | Full case-study evidence packages |

The structural audit prints the current missing IDs and status totals on every run. A missing brief is not automatically an error: some entries are intentionally OSTI-only stubs or unresolved public leads. Active entries without briefs are the highest-priority completion queue.

## Priority completion queue

The following active catalog entries currently lack project briefs and should be resolved before a numbered book edition:

- `olcf-user-docs`
- `gedi-tutorials`
- `far3d`
- `olm`
- `stor4build`

The remaining uncovered entries are either unresolved public leads or OSTI-only stubs and should be either researched into briefs, moved to an explicitly labeled appendix, or removed under the scope rules after verification.

## Editorial rule

Do not describe the book as complete while any chapter or catalog entry is only a placeholder. If a future edition intentionally excludes an entry, record the reason in `verification/not-found.md` or the relevant batch file and preserve the exclusion in the edition manifest.
