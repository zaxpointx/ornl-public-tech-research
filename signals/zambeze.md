# Signals: zambeze

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- The project wound down steadily. Commits went 573 (2022), 305 (2023), 193 (2024), and active authors 13, then 10, then 4, with the last commit on 2024-09-13. [KNOWN: git log --all] Read: the work probably moved on, perhaps into Flowcept, since both share LDRD project 11521 and Zambeze has a Flowcept hook. [INFERRED, low. No source says Zambeze was replaced]
- Work was spread across the team. The top three authors have 25%, 21% and 20%, out of 16 emails. [KNOWN]
- There's no named supercomputer apart from a single file mentioning "frontier", and CI runs only on ubuntu-latest, covering checks, tests and integration tests. [KNOWN] Read: it was tested as a distributed service, not on a specific machine. [INFERRED, medium]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2022-04-14, last commit 2024-09-13. 1,071 commits across all branches, 1,061 on the default branch | git | [KNOWN] |
| Commits per year | 2022: 573, 2023: 305, 2024: 193 | git log --all | [KNOWN] |
| Active authors per year | 2022: 13, 2023: 10, 2024: 4. 16 emails | git log | [KNOWN] |
| Tags | v0.0.1-devel 2023-01-25, list 2023-02-07, v0.1-Yambeshe 2023-03-06 | git | [KNOWN] |
| Funding | OSTI 2483434 lists USDOE generically. LDRD 11521 per OSTI 3025007 (map link 111) | OSTI API | [KNOWN] |
| Wayback | Nearest captures 2023-02-14 and 2024-09-17 | availability API | [KNOWN], but only bounds the dates |

## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only (RULES 16). Detail in connections/map.md links 113-114, 168.

**Outside vs inside:** The inside describes cross-facility workflow orchestration paired with Flowcept. Outside, the PyPI release (0.1) lags the repo (0.2), downloads are minimal, the repo has been quiet since 2024-09, and the only papers are ORNL's own, so it looks like an ORNL research prototype whose Flowcept hook may have drifted.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `zambeze` 0.1 (repo pyproject says 0.2) | [KNOWN] | https://pypi.org/pypi/zambeze/json ; pyproject.toml |
| Downloads | pypistats recent: 0 last day, 6 last week, 12 last month (2026-10-24). Not users | [KNOWN] counts; [INFERRED] meaning | https://pypistats.org/api/packages/zambeze/recent |
| conda-forge / Spack | No conda-forge feedstock (404); Spack not found | [KNOWN] | github.com/conda-forge |
| GitHub | 10 stars, 2 forks, last push 2024-09-13 | [KNOWN] | GitHub API |
| Flowcept tie | message_handler.py lines 69-76 import Flowcept's ZambezeInterceptor; Flowcept keeps a Zambeze settings kind but no longer that class | [CORROBORATED] tie; drift [INFERRED] | both repos |
| Citations | ORNL papers: eScience 2023 "Driving Next-Generation Workflows from the Data Plane", OSTI 2483434 (2024) | [KNOWN] | api.openalex.org; OSTI |

Reasoning: inactive since 2024 and used in ORNL papers only [INFERRED, medium confidence].
