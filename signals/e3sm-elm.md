<!-- history section (discovery pass) goes above -->

## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. ELM is one component of the multi-lab E3SM model; counts below are for E3SM or ELM papers, not ORNL-only work.

**Outside vs inside:** E3SM is a large DOE multi-lab model with 486 forks and a heavily cited overview paper, and most citers have no ORNL author. ORNL's part is its named ELM work, not E3SM as a whole.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| GitHub | E3SM-Project/E3SM: 448 stars, 486 forks, last push 2026-10-24 UTC; dependents page gave no count | [KNOWN]; dependents [UNKNOWN] | GitHub API |
| Registries | No `e3sm` on PyPI, conda-forge or Spack (404) | [KNOWN] | registries |
| Citations (E3SM) | "The DOE E3SM Coupled Model Version 1" (10.1029/2018MS001603): 826 citing works, 70 with an ORNL author | [KNOWN] | api.openalex.org |
| Citations (ELM) | ELM papers include a 2018 variably saturated flow paper (10.5194/gmd-11-4085-2018, 73 cites) and ELM model-output datasets on ESS-DIVE (10.15485/...) | [KNOWN] | api.openalex.org |

Reasoning: wide outside citation reflects E3SM overall; ORNL's ELM-specific uptake is not separable from this data [INFERRED, medium confidence].
