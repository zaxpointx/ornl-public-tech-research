# Signals: myna

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- Young and lumpy. It started in 2023-05, peaked at 205 commits in 2024, dipped to 126 in 2025 and is back up to 169 in 2026. Active authors went 2, 9, 2, 6. [KNOWN: git log --all] Read: one core developer, plus helpers who come and go with projects or internships. [INFERRED, low]
- One author has 79% of commits. [KNOWN]
- The DOE CODE record (code-141169) is dated 2024-08-19, the same day as the 1.0.0 tag. [KNOWN] Read: the software release was registered right at the first release. [INFERRED, high]
- No supercomputer or GPU target in the code. It's a Python workflow tool, tested on plain ubuntu runners. [KNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2023-05-11, last 2026-10-13. 538 commits on all branches, 475 on main | git | [KNOWN] |
| Commits per year | 38, 205, 126, 169 (2023 to 2026) | git log --all | [KNOWN] |
| Active authors per year | 2, 9, 2, 6. 13 emails. Top 79% | git log | [KNOWN] |
| Tags | 1.0.0 2024-08-19, 1.1.0 2025-04-09 | git | [KNOWN] |
| CI | CI, docs deployment and pre-commit on ubuntu-latest | .github/workflows | [KNOWN] |
| Funding | code-141169 lists ORNL as research org and Office of Science as sponsor. Other Myna hits add EERE and Nuclear Energy once each | OSTI API | [KNOWN] |
| Wayback | Nearest captures 2025-02-02 and 2025-04-13 | availability API | [KNOWN], only bounds dates |

## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. Map links 55 and the AM cluster.

**Outside vs inside:** Its 2025 paper is new, and both citing works come from outside ORNL, but there's no package and no dependents. The PyPI name "myna" holds a bare 0.1 upload with no metadata, which can't be tied to this repo.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `myna` 0.1, no summary, author or links; repo pyproject is `myna` 1.2.0.dev0; no pypistats data | [UNKNOWN] whether it is this project | https://pypi.org/pypi/myna/json ; pyproject.toml |
| conda-forge / Spack | None (404) | [KNOWN] | registries |
| GitHub "used by" | "0 Repositories"; 14 stars, 6 forks, last push 2026-10-13 UTC | [KNOWN] | network/dependents; GitHub API |
| Citations | Computational Materials Science 2025 Myna paper (10.1016/j.commatsci.2025.114094): 2 citing works, 0 with an ORNL author | [KNOWN] | api.openalex.org |

Reasoning: too early to judge adoption; two outside citations are a weak start [INFERRED, low confidence].
