<!-- history section (discovery pass) goes above -->

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- Oak Ridge's hands-on coding share has faded to zero. Commits from ornl.gov addresses were 4 to 10% from 2014 to 2018, then 1% from 2019 to 2021, and 0% since 2022. [KNOWN: author email domains, aggregate] Read: ORNL is now a co-owner and user rather than a main code contributor. That fits the usage finding that it's mostly another lab's project now. [INFERRED, medium; lower bound since many commit from other addresses]
- The project itself is very healthy. 2,400 to 6,400 commits a year, 30 to 43 active authors a year, 163 emails, and nobody above 15%. [KNOWN: git log]
- Releases come out twice a year with several release candidates each time. The latest is v26.2.0 (2026-09-30), with 306 tags in all. [KNOWN]
- ORNL's own EnergyPlus-related software on DOE CODE is add-ons, not the engine, for example stor4build (code-170060), funded by EERE's Building Technologies Office. [KNOWN: OSTI API] ORNL papers that mention EnergyPlus on OSTI are mostly EERE-funded. [KNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2014-03-12 (GitHub era), last 2026-10-23. 44,878 commits on default branch | git | [KNOWN] |
| Commits per year | 1,369 (2014), peak 6,365 (2020), 2,560 (2025) | git log | [KNOWN] |
| Active authors per year | 23 to 43. 163 emails. Top three 15%, 10%, 7% | git log | [KNOWN] |
| ornl.gov commit share | 10% (2016), 1% (2019), 0% (2022 to 2026) | email domains, aggregate | [KNOWN], lower bound |
| Tags | 306. Latest v26.2.0 2026-09-30 | git | [KNOWN] |
| ORNL add-on record | code-170060 stor4build, EERE Building Technologies Office | OSTI API | [KNOWN] |
| Funding | ORNL OSTI hits mentioning EnergyPlus, EERE on most | OSTI API | [KNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. EnergyPlus is multi-lab; ORNL is one named copyright holder (LICENSE.txt), and development is led from the National Laboratory of the Rockies GitHub org. Nothing here is credited to ORNL alone.

**Outside vs inside:** EnergyPlus is the best known tool in this batch: 1,607 stars, a Spack package, a 2001 paper with 2,837 citing works (only 30 with an ORNL author), and an outside scripting ecosystem (eppy).

| Signal | Finding | Tag | Source |
|---|---|---|---|
| GitHub | NatLabRockies/EnergyPlus: 1,607 stars, 496 forks, last push 2026-10-24 UTC; dependents page gave no count | [KNOWN]; dependents [UNKNOWN] | GitHub API |
| Spack | `energyplus` package.py exists (homepage energyplus.net) | [KNOWN] | spack-packages builtin |
| PyPI | `energyplus` 0.0.1 "EnergyPlus API Python Bindings" (50 downloads last month), an individual's packaging repo; `eppy` 0.6.7, an outside scripting tool for EnergyPlus files (14,201 downloads last month) | [KNOWN]; not official releases | https://pypi.org/pypi/energyplus/json ; https://pypi.org/pypi/eppy/json |
| Citations | "EnergyPlus: creating a new-generation building energy simulation program" (2001, 10.1016/S0378-7788(00)00114-6): 2,837 citing works, 30 with an ORNL author | [KNOWN] | api.openalex.org |

Reasoning: worldwide building-energy use; ORNL is a small share of citers, consistent with a contributor rather than lead role [INFERRED, medium confidence].
