# Signals: landscan


## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- LandScan ships like clockwork. There's a new yearly global release on OSTI: Global 2023 "Silver Edition" (2024-10), Global 2024 (2025-08) and Global 2026 (2026-07). There's also a new Mosaic time series covering 1975 to 2024 (2026-05). [KNOWN: OSTI 2574458, 2587445, 17076155, 3365747] Read: very alive, and it now goes back in time as well as forward. [INFERRED, high]
- Oak Ridge output about it is growing. ORNL OSTI records mentioning LandScan went from 1 to 6 a year (2018 to 2023) to 11 to 14 a year (2024 to 2026). [KNOWN, rough count]
- Who pays is mostly hidden. 46 of 59 records just say "USDOE". The named ones are the Office of Science and BER, LDRD (the lab's own seed money), and CESER, DOE's energy security office. [KNOWN] The brief's licensing page covers who can use it, not who funds it. [KNOWN: projects/landscan.md] Who actually funds it is [UNKNOWN] from public records here.
- LandScan feeds other ORNL datasets. The EAGLE-I power outage county dataset turns up in the same search, under CESER money. [KNOWN: OSTI 3022751; the link is INFERRED from the shared search, low]
- No Wayback check this round. The archive's API kept failing. [UNKNOWN]
- Source: OSTI API (osti.gov/api/v1), ORNL-filtered by research_org. Word searches can pull namesakes, so counts are rough. No public code exists, so there are no commit or build-target signals. [KNOWN scope limit]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| Recent releases | Global 2023 Silver (2024-10-01), 2024 (2025-08-01), 2026 (2026-07-01), Mosaic 1975-2024 (2026-05-01) | OSTI API | [KNOWN] |
| ORNL records per year | 2018:4, 2022:6, 2024:11, 2025:14, 2026:13 | OSTI API | [KNOWN], rough |
| Sponsors | USDOE 46 of 59; SC 5; LDRD 3; BER 3; CESER 2 | OSTI API | [KNOWN] |
| Real funder | Not stated publicly in these records | | [UNKNOWN] |
| Wayback | Not checked | | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. LandScan is a dataset with no public code repo; counts are for LandScan papers and dataset articles indexed by OpenAlex, not downloads.

**Outside vs inside:** LandScan is used far beyond ORNL: the 2003 founding chapter has 876 citing works (96% without an ORNL author), and outside libraries and archives redistribute its rasters.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Registries | No `landscan` on PyPI, conda-forge or Spack (404) | [KNOWN] | registries |
| Citations (global) | "LandScan: a global population database for estimating populations at risk" (2003, 10.1201/9781482264678-24): 876 citing, 34 with ORNL author. "LandScan Global 30 Arcsecond Annual Global Gridded Population Datasets from 2000..." (Scientific Data 2025, 10.1038/s41597-025-04817-z): 114 citing, 7 ORNL | [KNOWN] | api.openalex.org |
| Citations (USA) | "LandScan USA: a high-resolution geospatial and temporal modeling approach..." (GeoJournal 2007, 10.1007/s10708-007-9105-9): 454 citing, 53 ORNL | [KNOWN] | api.openalex.org |
| Outside redistribution | University GIS subject guides and a 2026 Zenodo study archive re-host LandScan USA rasters | [KNOWN] | api.openalex.org search |

Reasoning: one of ORNL's most widely used public data products, cited across disaster, health and GIS research [INFERRED, high confidence].
