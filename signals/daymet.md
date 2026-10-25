<!-- history section (discovery pass) goes above -->

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- Daymet is a dataset, so its history isn't really in git. Its one public helper repo (daymet-single-pixel-batch) has only 15 commits from 2018 to 2025, mostly from ornl.gov addresses. [KNOWN: git log] Read: the tooling around the data is a side job. The real work happens in a non-public pipeline, which is out of scope (rule 16). [INFERRED, medium]
- NASA pays for it. The brief already cites NASA (ESDIS and the Terrestrial Ecology Program) plus DOE BER. NASA money doesn't show up on OSTI at all, so OSTI alone would make it look DOE-funded. [KNOWN: projects/daymet.md; INFERRED about OSTI's blind spot, high]
- On OSTI, ORNL papers that use Daymet are spread across USDOE, Office of Science and EERE money. Read: other ORNL groups use it as an input, for energy and buildings work too. [INFERRED, medium]
- No Wayback check this round. The archive API was rate-limiting. [UNKNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| Helper repo | 15 commits 2018-04-16 to 2025-03-29, 6 emails, no tags | git | [KNOWN] |
| Funding (from brief) | NASA ESDIS and Terrestrial Ecology, DOE BER | daymet brief | [KNOWN] |
| ORNL papers using it | OSTI hits list USDOE, Office of Science, EERE | OSTI API | [KNOWN] |
| Wayback | Not checked (rate-limited) | | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. Daymet is a dataset: counted dataset DOIs at the ORNL DAAC as indexed by OpenAlex, not data downloads.

**Outside vs inside:** Daymet is the most outward-facing project here. Its dataset versions are cited over a thousand times, about 96% from papers with no ORNL author, and outside groups maintain their own access tools (pydaymet in Python, daymetr in R).

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Dataset citations | Version 2 (10.3334/ornldaac/1219): 374 citing, 10 with ORNL author; Version 3 (10.3334/ornldaac/1328): 404 citing, 16 ORNL; Version 4 (10.3334/ornldaac/1840): 244 citing, 8 ORNL; Version 4 R1 (10.3334/ORNLDAAC/2129): 152 citing, 10 ORNL | [KNOWN] | api.openalex.org |
| Outside clients | PyPI `pydaymet` 0.19.4 (HyRiver project, "Access daily, monthly, and annual climate data via the Daymet web service", 1,138 downloads last month, conda-forge feedstock exists); CRAN `daymetr` page exists | [KNOWN]; third-party, not ORNL code | https://pypi.org/pypi/pydaymet/json ; https://cran.r-project.org/package=daymetr |
| ORNL repo | ornldaac/daymet-single-pixel-batch: 10 stars, 24 forks, last push 2025-03-29 UTC, "0 Repositories" dependents | [KNOWN] | GitHub API |
| Registries | No `daymet` package on PyPI, conda-forge or Spack (404) | [KNOWN] | registries |

Reasoning: heavy outside citation plus independent client libraries show wide research use across ecology and hydrology [INFERRED, high confidence].
