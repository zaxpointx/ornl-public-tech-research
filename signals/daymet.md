<!-- history section (discovery pass) goes above -->

## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. Daymet is a dataset: counted dataset DOIs at the ORNL DAAC as indexed by OpenAlex, not data downloads.

**Outside vs inside:** Daymet is the most outward-facing project here. Its dataset versions are cited over a thousand times, about 96% from papers with no ORNL author, and outside groups maintain their own access tools (pydaymet in Python, daymetr in R).

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Dataset citations | Version 2 (10.3334/ornldaac/1219): 374 citing, 10 with ORNL author; Version 3 (10.3334/ornldaac/1328): 404 citing, 16 ORNL; Version 4 (10.3334/ornldaac/1840): 244 citing, 8 ORNL; Version 4 R1 (10.3334/ORNLDAAC/2129): 152 citing, 10 ORNL | [KNOWN] | api.openalex.org |
| Outside clients | PyPI `pydaymet` 0.19.4 (HyRiver project, "Access daily, monthly, and annual climate data via the Daymet web service", 1,138 downloads last month, conda-forge feedstock exists); CRAN `daymetr` page exists | [KNOWN]; third-party, not ORNL code | https://pypi.org/pypi/pydaymet/json ; https://cran.r-project.org/package=daymetr |
| ORNL repo | ornldaac/daymet-single-pixel-batch: 10 stars, 24 forks, last push 2025-03-29 UTC, "0 Repositories" dependents | [KNOWN] | GitHub API |
| Registries | No `daymet` package on PyPI, conda-forge or Spack (404) | [KNOWN] | registries |

Reasoning: heavy outside citation plus independent client libraries show wide research use across ecology and hydrology [INFERRED, high confidence].
