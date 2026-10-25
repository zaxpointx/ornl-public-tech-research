# Signals: vera


## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- VERA outlived the program that built it. CASL was the DOE hub that made it. ORNL OSTI records mentioning both VERA and CASL peaked at 19 to 24 a year in 2022 and 2023, and dropped to 9 in 2025 and 5 so far in 2026. [KNOWN, rough] Read: the CASL-branded wave is winding down, but the reactor work keeps going. For example, 2025 and 2026 reports on boiling-water-reactor modeling in MPACT, VERA's core solver (OSTI 3002716, 3027390). [KNOWN for the reports; the trend is INFERRED, medium]
- The funder is Nuclear Energy, through its NEAMS modeling program, plus a few Office of Science and NRC records. Most just say "USDOE". [KNOWN: 85 records]
- The VERA Infrastructure software record (OSTI 1546053) is from 2018-12-18 and lists "USDOE". [KNOWN]
- No Wayback check this round. The archive's API kept failing. [UNKNOWN]
- Source: OSTI API (osti.gov/api/v1), ORNL-filtered by research_org. Word searches can pull namesakes, so counts are rough. No public code exists, so there are no commit or build-target signals. [KNOWN scope limit]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| Infrastructure record | OSTI 1546053, 2018-12-18, USDOE | OSTI API | [KNOWN] |
| VERA plus CASL records per year | 2022:19, 2023:24, 2024:18, 2025:9, 2026:5 | OSTI API | [KNOWN], rough |
| Sponsors | USDOE 59, NE 12, NEAMS 11, SC 6, NRC 3 | OSTI API | [KNOWN] |
| Recent work | BWR decusping reports 2025-02, 2026-03 | OSTI 3002716, 3027390 | [KNOWN] |
| Wayback | Not checked | | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. VERA has no public repo or package.

**Outside vs inside:** About two thirds of the papers citing VERA's core-simulator methodology paper have no ORNL author, which fits its multi-partner origin, but there's no public code trace at all.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Registries | PyPI `vera` 0.3.2 is a CLI for "VERA documents", a namesake | [UNRELATED] | https://pypi.org/pypi/vera/json |
| Public repo / dependents | None | [KNOWN] | https://vera.ornl.gov/ |
| Citations | "VERA Core Simulator Methodology for Pressurized Water Reactor Cycle Depletion" (Nucl. Sci. Eng. 2017, 10.13182/nse16-39): 93 citing, 30 with ORNL author. Recent ORNL VERA-MPACT reports (e.g. OSTI 3002716, 2025) have 0 to 4 cites | [KNOWN] | api.openalex.org |

Reasoning: an industry and lab tool known mainly through papers [INFERRED, low confidence].
