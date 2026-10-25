# Signals: gitr

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- It's the most shared codebase of this batch. 40 emails and nobody has more than 16% of commits. Up to 12 people were active in a year (2021, 2024). [KNOWN: git log --all] Read: a real team code, not one person's project. [INFERRED, medium]
- Activity has slowed lately. 267 commits in 2024, 116 in 2025, and no commits dated after 2025-06-11, though GitHub shows a push on 2025-11-21. [KNOWN: git log, catalog] Read: quiet for about 16 months. Status stays as the catalog has it until someone confirms otherwise. [INFERRED, low]
- The last tag is v1.3.0 from 2022-12-06, so nearly three years of work has no tagged release. [KNOWN]
- Fusion Energy Sciences is the main funder, on 5 of 9 OSTI hits, with ASCR on 2. [KNOWN: OSTI sponsor fields] GPU support is CUDA (12 files). No supercomputer is named in the code. [KNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2015-07-31, last 2025-06-11. 1,467 commits on all branches, 1,213 on main | git | [KNOWN] |
| Commits per year | 6, 172, 34, 140, 211, 130, 178, 111, 102, 267, 116 (2015 to 2025) | git log --all | [KNOWN] |
| Active authors per year | 4, 6, 2, 10, 9, 4, 12, 5, 9, 12, 4. 40 emails. Top three 16%, 15%, 15% | git log | [KNOWN] |
| Tags | 1.0 2019-02-14, 1.1 2020-04-20, v1.2.0 2021-08-14, v1.3.0 2022-12-06 (plus one example tag) | git | [KNOWN] |
| CI | One CMake workflow on ubuntu-latest | .github/workflows | [KNOWN] |
| Funding | 9 OSTI hits: FES x5, USDOE x4, Office of Science x3, ASCR x2 | OSTI API | [KNOWN] |
| Wayback | Nearest captures 2018-06-13, 2020-09-28, 2024-07-30 | availability API | [KNOWN], only bounds dates |

## Connector: who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users.

**Outside vs inside:** GITR has more forks (18) than stars (13) and a well-cited paper, but two thirds of its citers include ORNL authors, so it's mainly a fusion-group code with some outside plasma-material users.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI / conda-forge / Spack | None (404) | [KNOWN] | registries |
| GitHub "used by" | "0 Repositories"; 13 stars, 18 forks, last push 2025-11-21 UTC | [KNOWN] | https://github.com/ORNL-Fusion/GITR/network/dependents ; GitHub API |
| Citations | Computer Physics Communications 2021 GITR paper (10.1016/j.cpc.2021.107885): 34 citing works, 22 with an ORNL author | [KNOWN] | api.openalex.org |

Reasoning: forks above stars suggest people copy it to run their own cases [INFERRED, low confidence]; citers are mostly ORNL [KNOWN counts].
