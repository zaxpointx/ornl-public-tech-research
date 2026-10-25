<!-- history section (discovery pass) goes above -->

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- This section counts only the land model's folder (components/elm) inside the much bigger E3SM repo. Most of its history in that folder starts in 2020, which looks like when the folder got its current name. [KNOWN: git log on the path; rename INFERRED, medium]
- It's busy and shared. 212 to 435 commits a year since 2020, 31 to 51 active authors a year, and 116 emails touching the folder. [KNOWN]
- Oak Ridge's share is steady at about a tenth. ornl.gov addresses wrote 9 to 14% of commits every year from 2021 to 2026. [KNOWN: email domains, aggregate; lower bound] Read: ORNL is a consistent partner, not the owner. That matches the catalog's "ORNL's named ELM work" scope note. [INFERRED, medium]
- Funding on OSTI for ORNL land-model papers is the Office of Science's Biological and Environmental Research (BER) program. [KNOWN: OSTI sponsor fields]
- Build targets for the full E3SM model weren't checked here. They belong to the whole model, not the land part. [UNKNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| Path history | components/elm: 1,944 commits on default branch, last 2026-10-22 | git log -- components/elm | [KNOWN] |
| Commits per year | 212, 343, 272, 222, 435, 313, 134 (2020 to 2026) | git log | [KNOWN] |
| Active authors per year | 25, 51, 43, 35, 35, 39, 31 (2020 to 2026). Top 19% | git log | [KNOWN] |
| ornl.gov commit share | 9 to 14% a year, 2021 to 2026 | email domains, aggregate | [KNOWN], lower bound |
| Funding | BER on ORNL ELM papers | OSTI API | [KNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. ELM is one component of the multi-lab E3SM model; counts below are for E3SM or ELM papers, not ORNL-only work.

**Outside vs inside:** E3SM is a large DOE multi-lab model with 486 forks and a heavily cited overview paper, and most citers have no ORNL author. ORNL's part is its named ELM work, not E3SM as a whole.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| GitHub | E3SM-Project/E3SM: 448 stars, 486 forks, last push 2026-10-24 UTC; dependents page gave no count | [KNOWN]; dependents [UNKNOWN] | GitHub API |
| Registries | No `e3sm` on PyPI, conda-forge or Spack (404) | [KNOWN] | registries |
| Citations (E3SM) | "The DOE E3SM Coupled Model Version 1" (10.1029/2018MS001603): 826 citing works, 70 with an ORNL author | [KNOWN] | api.openalex.org |
| Citations (ELM) | ELM papers include a 2018 variably saturated flow paper (10.5194/gmd-11-4085-2018, 73 cites) and ELM model-output datasets on ESS-DIVE (10.15485/...) | [KNOWN] | api.openalex.org |

Reasoning: wide outside citation reflects E3SM overall; ORNL's ELM-specific uptake is not separable from this data [INFERRED, medium confidence].
