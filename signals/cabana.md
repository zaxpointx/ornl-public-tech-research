# Signals: cabana

## Scout: history, build targets, funding (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- The team is broad and has outlasted ECP, the DOE program that funded CoPA. There are 57 author emails, and no author has more than 25% of commits. 17 authors were active in 2025, after ECP ended. [KNOWN: git log] Read: it survived the end of its founding program. [INFERRED, medium]
- Commits have slowed, from 818 in 2019 to 123 a year in 2024 and 2025 and 15 so far in 2026, while releases continue (0.7.0 2024-09-26, 0.8.0 2026-05-29). [KNOWN] Read: a mature library. [INFERRED, medium]
- Besides GitHub Actions, there's a `.gitlab-ci.yml` and an `.ecp-gitlab-ci.yml`. Read: there's a non-public pipeline, which is out of scope (rule 16). No named supercomputer appears in the code. GPU backends show up through Kokkos (cuda in 19 files, hip in 9, sycl in 8). [KNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2018-01-10, last commit 2026-09-16. 3,117 commits across all branches, 2,843 on the default branch | git | [KNOWN] |
| Commits per year | 418, 818, 553, 449, 324, 294, 123, 123, 15 (2018 to 2026) | git log --all | [KNOWN] |
| Active authors per year | 12, 21, 16, 15, 13, 11, 11, 17, 4. 57 emails. Top three 25%, 14%, 12% | git log | [KNOWN] |
| Tags | 0.6.1 2023-11-20, 0.7.0 2024-09-26, 0.8.0 2026-05-29 | git | [KNOWN] |
| CI | GitHub CI, Nightly, Docker and format checks on ubuntu-latest and arm64 | .github/workflows | [KNOWN] |
| Funding | code-45702 lists USDOE generically. The README credits ECP | OSTI API, README | [KNOWN] |
| Wayback | Nearest captures 2020-10-16, 2023-03-16 and 2026-05-12 | availability API | [KNOWN], but only bounds the dates |

## Connector: who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16); institutions from OpenAlex, no individuals profiled. Detail in connections/map.md links 32, 146, 165-166.

**Outside vs inside:** The inside is a multi-lab ECP particle library built on Kokkos. Outside, it reaches users through Spack, and three quarters of the papers citing its JOSS paper have no ORNL author (European HPC centres such as Forschungszentrum Jülich, plus LANL and LLNL), so ORNL is one contributor among several, not the main user.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Spack | `cabana` package.py exists | [KNOWN] | spack-packages builtin cabana |
| conda-forge | No feedstock (404) | [KNOWN] | github.com/conda-forge |
| PyPI | `cabana` on PyPI is a collagen-fibre image analyser, a namesake | [UNRELATED] | https://pypi.org/pypi/cabana/json |
| GitHub "used by" | "0 Repositories"; 284 stars, 68 forks | [KNOWN] | https://github.com/ECP-copa/Cabana/network/dependents |
| Catalog consumer | Finch: `find_package(Cabana 0.6.1 REQUIRED COMPONENTS Cabana::Grid)` | [KNOWN] | ORNL-MDF/Finch CMakeLists.txt |
| Citations | JOSS 2022 (10.21105/joss.04115): 24 citing works, 19 without an ORNL author | [KNOWN] | api.openalex.org |

Reasoning: Spack packaging, multi-lab authorship and mostly non-ORNL citers suggest a shared DOE/European particle-simulation building block [INFERRED, medium confidence]. Downloads are not applicable (no registry stats).
