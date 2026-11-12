# LandScan Mosaic: a population estimate is also a distribution

Research date: 2026-11-10. Independent public-source study. This expands the existing [LandScan brief](../../projects/landscan.md); it does not describe individual people or operational systems. Publication details and access limits belong to the individual sources below.

## How the research works

[KNOWN, G01] The 2025 LandScan Mosaic paper replaces fixed building attributes with probability distributions for building use, floor count, and occupancy rate. Sampling these distributions produces multiple plausible population allocations. The paper compares their effect on flood-exposure decisions in Iloilo City, Philippines. A building's footprint, floors, and occupancy density supply allocation weights; the output is a population estimate with uncertainty, rather than an observed headcount.

[INFERRED, G01] The useful engineering idea is that uncertainty should survive the whole pipeline. A precise-looking final map can hide uncertain input classifications. A local study could hold a synthetic region's population total fixed while sampling building-use and occupancy assumptions, then check whether the ranking of exposed districts changes. That would test a decision method, not recreate the published geographic result.

[UNKNOWN, G01] Exact local reproduction is not established. The paper says code and resulting rasters are available on request and notes both commercial and public building inputs. This study did not contact authors, obtain files, or verify a released implementation. The availability statement is a constraint, not an invitation to assume the complete code is open source.

## Distinguish a paper, a release, and a historical model

[KNOWN, G02] ORNL's September 17, 2026 announcement describes a building-centric global release and identifies its output as ambient population averaged across a 24-hour period. Its discussion of daily activity does not establish an individual-level movement dataset or an hourly observed census. It describes a forthcoming historical series as backcasting.

[KNOWN, G03] A separate ORNL dataset record describes version 1.0 of the annual 1975–2024 series: one Cloud-Optimized GeoTIFF per year on a common 3 arc-second WGS84 grid. The 2024 surface is the benchmark; earlier years are modeled using LandCast, built-environment change, and recovery of population control totals. The record's availability year is 2026; it supplies no exact release date in the fetched description.

[UNKNOWN, G02–G03] The announcement's future tense and the record's dataset description do not establish the exact publication sequence. Download availability, file checksums, reuse terms, completeness of the geographic release, and present service status were not tested. Backcast layers are estimates conditioned on a benchmark and historical evidence, not fifty independently observed censuses.

## Connections worth studying

| Connection | Evidence boundary | Why it matters |
|---|---|---|
| LandScan HD methodology -> probabilistic Mosaic methodology | [KNOWN, G01] explicit research lineage | A mature deterministic workflow can be extended to carry uncertainty |
| Mosaic benchmark -> LandCast historical surfaces | [KNOWN, G03] record names the input and method | Changing a benchmark can affect interpretations of historical change |
| Building morphology tools such as Gauntlet/Vivaldi -> Mosaic | [UNKNOWN] no exact implementation link established by the sources inspected here | Similar inputs do not prove shared code; follow the actual import or paper citation before adding an edge |
| Mosaic flood exposure -> Daymet weather products | [INFERRED] a possible future comparison, not documented integration | Temporal scale, grid alignment, population definition, and hazard assumptions must be reconciled first |

## Evidence ledger

All three primary sources were fetched and read on 2026-11-10. Quotes are short; no snippets were promoted to evidence.

- **G01:** Adams and colleagues, *LandScan mosaic enables high-resolution gridded population estimates with explicit uncertainty*, Scientific Reports, published 2025-12-24. [Paper](https://www.nature.com/articles/s41598-025-28125-z), abstract/methods/data availability. Short evidence: “building use types, floor counts, and occupancy rates”. The complete method and data-availability statement support the limitations above. Paper affiliation identifies ORNL. Result concerns the reported case study, not universal forecast accuracy.
- **G02:** ORNL, *ORNL releases LandScan Mosaic*, 2026-09-17. [Announcement](https://www.ornl.gov/news/ornl-releases-landscan-mosaic/), building-model and historical-series sections. Evidence: “the average number of people present in a location over a 24-hour period”. Institutional release account, not an independent validation or download test.
- **G03:** ORNL, *LandScan Mosaic Annual Global Ambient Population Time Series, Version 1.0: 1975–2024*, availability year 2026; exact date unknown. [Dataset record](https://impact.ornl.gov/en/datasets/landscan-mosaic-annual-global-ambient-population-time-series-vers/), description. Evidence: “the 1975–2023 layers are historical annual estimates”. Metadata only; files were not downloaded.

## Sweep 2 and stopping boundary

Re-read the complete narrative against all three fetched sources. Retained the announcement's planned-series wording separately from the dataset record. Corrected a tempting overstatement: ambient population is not observed hourly movement. Kept source/data access requests outside this work. Used angular resolution rather than repeating an inconsistent meter conversion in the paper's discussion of other products: a grid's physical scale also varies with latitude. Sources do not establish a Gauntlet or Vivaldi dependency. No shared-code relationship was added.

Well understood: the probabilistic allocation idea, its three modeled inputs, and the benchmark/backcast distinction. Unknown: complete reproducible implementation, input licenses and present geographic coverage. Next useful evidence is a public code/data release with explicit terms. Broad searches are less useful than resolving those exact artifacts.
