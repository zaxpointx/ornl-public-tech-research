# Signals: adamantine

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- It's a slow, steady grower. Commits ran 113 to 264 a year from 2020 on, and active authors went from 2 in 2020 to 7 or 8 in 2024 and 2025. [KNOWN: git log --all] Read: small but healthy, still getting new people. [INFERRED, medium]
- One author has 67% of commits and the next has 23%. [KNOWN] Read: led by one main developer. [INFERRED, medium]
- It has been run on Frontier. A code comment notes a memory problem hit on Frontier with one of its solver libraries. GPU support comes through Kokkos (18 files) with CUDA mentions in 5. [KNOWN: source/MechanicalOperator.cc] Read: real runs on ORNL's AMD GPU machine. [INFERRED, medium]
- Funding hits on OSTI lean toward DOE's energy-efficiency office (EERE) and LDRD, which fits additive manufacturing work. [KNOWN: OSTI sponsor fields; mix INFERRED, low, small sample]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2016-06-30, last 2026-10-21. 1,458 commits on all branches, 1,289 on master | git | [KNOWN] |
| Commits per year | 56, 47, 0, 29, 113, 229, 192, 143, 264, 190, 195 (2016 to 2026) | git log --all | [KNOWN] |
| Active authors per year | 1, 1, 0, 2, 2, 3, 3, 4, 7, 8, 6. 14 emails. Top two 67%, 23% | git log | [KNOWN] |
| Tags | v1.0 2024-10-01, v1.1 2026-01-23 | git | [KNOWN] |
| CI | Docker and Nix workflows on GitHub runners | .github/workflows | [KNOWN] |
| Funding | 4 OSTI hits: USDOE x2, LDRD, EERE x2 | OSTI API | [KNOWN] |
| Wayback | Nearest captures 2024-04-19 and 2025-10-05 | availability API | [KNOWN], only bounds dates |

## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. Refreshes map links 123, 126.

**Outside vs inside:** Outside traces are thin: no packages, no dependents, and 4 of the 6 papers citing the JOSS paper include an ORNL author, so use is mostly inside ORNL's additive-manufacturing group.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI / conda-forge / Spack | None (404, refreshed) | [KNOWN] | registries |
| GitHub "used by" | "0 Repositories"; 57 stars, 16 forks, last push 2026-10-21 UTC | [KNOWN] | https://github.com/adamantine-sim/adamantine/network/dependents ; GitHub API |
| Citations | JOSS 2024 "Adamantine 1.0" (10.21105/joss.07017): 6 citing works, 4 with an ORNL author | [KNOWN] | api.openalex.org |

Reasoning: active development with mostly ORNL citers suggests an in-house research code with small outside uptake [INFERRED, medium confidence].
