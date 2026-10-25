# Signals: tesvis-modis


## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- The money is split between two agencies. ORNL OSTI records mentioning MODIS and the ORNL DAAC are mostly funded by BER (24), then NASA (8) and NSF (6). [KNOWN: 39 records] But the DAAC itself is a NASA data archive (per the Daymet brief), and NASA's money mostly doesn't show up on OSTI. So OSTI makes it look more DOE-funded than it is. [INFERRED, high]
- It's being used more and more. Records went from 1 to 4 a year (2016 to 2023) to 12 in 2024 and 10 in 2025. [KNOWN, rough] Most look like papers that use the data, not new tool releases. [INFERRED, medium]
- The public web service and API are documented on modis.ornl.gov (per the brief). I didn't call the API or look at the host (rule 16). [KNOWN scope limit]
- No Wayback check this round. The archive's API kept failing. [UNKNOWN]
- Source: OSTI API (osti.gov/api/v1), ORNL-filtered by research_org. Word searches can pull namesakes, so counts are rough. No public code exists, so there are no commit or build-target signals. [KNOWN scope limit]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| Records | 39 ORNL OSTI records, 2016 to 2026 | OSTI API | [KNOWN], rough |
| Sponsors | BER 24, USDOE 18, NASA 8, NSF 6 | OSTI API | [KNOWN] |
| Records per year | 2024:12, 2025:10 | OSTI API | [KNOWN] |
| Real host funder | NASA, via the DAAC | daymet brief | [KNOWN] |
| Wayback | Not checked | | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. TESViS is a hosted ORNL DAAC service; no code repo, so usage shows through citations and outside client tools.

**Outside vs inside:** Outside users reach TESViS through third-party clients (an R package, MODISTools, and a Python `modis-tools` package that wraps the MODIS API) more than through citations. Its own citation DOI has only 4 indexed citing works, none with an ORNL author.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Citation DOI | ORNL DAAC 2018 (10.3334/ORNLDAAC/1600): 4 citing works, 0 with ORNL author | [KNOWN] | api.openalex.org |
| Service paper | "A SOAP Web Service for accessing MODIS land product subsets" (2011, 10.1007/s12145-011-0079-2): 12 citing, 0 with ORNL author | [KNOWN] | api.openalex.org |
| Outside clients | CRAN `MODISTools` page exists; PyPI `modis-tools` 2.0.1 "Tools for working with the MODIS API" (fraymio), not confirmed to call TESViS | [KNOWN]; [INFERRED] the TESViS link for modis-tools | https://cran.r-project.org/package=MODISTools ; https://pypi.org/pypi/modis-tools/json |

Reasoning: citations undercount use, since many users cite the underlying MODIS products instead [INFERRED, medium confidence].
