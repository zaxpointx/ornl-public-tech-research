# Research roles

The research is produced with an AI-assisted team workflow. Each role is a separate step, and no draft counts as verified until a different role has checked it against its sources.

| Role | What it does |
|---|---|
| Lead | Picks each batch (five projects or fewer), assigns work, reads every output, and reports only what is verified. |
| Scout | Finds candidate projects and their primary public sources, and adds them to `discovery/catalog.csv`. |
| Reader | Explains one project in plain English: the problem it solves, how its code is organized, and its system flow. |
| Engineering analyst | Records how a public project is built and maintained (layout, languages, dependencies, tests, CI, releases) without guessing at private design reasons. |
| Fact checker | Tries to disprove each claim, checks ownership and dates, fixes errors, and logs every check in `verification/log.md`. |
| Connector | Maps relationships between projects, facilities, papers, and datasets, only from cited evidence. |
| Librarian | Keeps the index, catalog, batch summaries, and file layout consistent. |

## Operating rules

- Public information only. No logins, internal systems, restricted material, or contact with lab staff.
- No full copies of copyrighted papers or code. Short cited quotes only.
- Gaps are labeled `[UNKNOWN]` instead of filled with guesses.
- People are described by role, not by name.

New deep dives follow [templates/project-case-study.md](../templates/project-case-study.md). The full rules are in [RULES.md](../RULES.md).
