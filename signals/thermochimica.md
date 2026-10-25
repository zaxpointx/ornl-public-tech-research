# Signals: thermochimica

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- It peaked in 2021 and 2022, with 837 and 623 commits, then dropped to 16 to 46 a year. But 5 or 6 people have been active every single year since 2018. [KNOWN: git log --all] Read: a finished-feeling library that a small group keeps maintaining. [INFERRED, medium]
- One author has 74% of commits. [KNOWN]
- No tags and no CI workflows at all, even after 2,234 commits. [KNOWN] Read: people use it straight from the main branch, often inside bigger codes. [INFERRED, low]
- Nuclear Energy is the clear funder. 6 of 7 OSTI hits list DOE's Office of Nuclear Energy, with one from the NRC. [KNOWN: OSTI sponsor fields]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2018-01-06, last 2026-07-23. 2,234 commits on all branches, 2,011 on master | git | [KNOWN] |
| Commits per year | 172, 275, 187, 837, 623, 46, 38, 16, 40 (2018 to 2026) | git log --all | [KNOWN] |
| Active authors per year | 5, 8, 4, 5, 5, 5, 6, 5, 6. 25 emails. Top 74% | git log | [KNOWN] |
| Tags | None | git | [KNOWN] |
| CI | None found | repo | [KNOWN] |
| Build targets | No supercomputer named. One HIP mention | grep | [KNOWN] |
| Funding | 7 OSTI hits: Nuclear Energy x6, USDOE x2, LDRD, NRC | OSTI API | [KNOWN] |
| Wayback | Nearest captures 2018-06-17, 2019-09-20, 2023-11-15, 2025-04-04 | availability API | [KNOWN], only bounds dates |

## Connector: who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users.

**Outside vs inside:** Thermochimica is the most outward-facing of this batch: 36 forks and a molten-salt paper cited mostly from outside ORNL, plus its known MOOSE/BISON coupling (OSTI reports), so nuclear-fuel modelers elsewhere use it, but it's not distributed through any package registry.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI / conda-forge / Spack | None (404) | [KNOWN] | registries |
| GitHub "used by" | "0 Repositories"; 69 stars, 36 forks, last push 2026-07-23 UTC | [KNOWN] | https://github.com/ORNL-CEES/thermochimica/network/dependents ; GitHub API |
| Citations | CALPHAD 2021 "Recent developments for molten salt systems in Thermochimica" (10.1016/j.calphad.2021.102341): 21 citing works, 2 with an ORNL author | [KNOWN] | api.openalex.org |
| Coupling reports | OSTI reports "Coupling of Thermochemistry Solver THERMOCHIMICA with MOOSE/BISON" (2015) and "Acceleration of Thermochimica Calculations in Bison" (2020) | [KNOWN] titles | api.openalex.org |

Reasoning: high fork ratio plus outside citers and BISON coupling suggest real use in nuclear-fuel codes [INFERRED, medium confidence].
