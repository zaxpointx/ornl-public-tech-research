<!-- history section (discovery pass) goes above -->

## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. EnergyPlus is multi-lab; ORNL is one named copyright holder (LICENSE.txt), and development is led from the National Laboratory of the Rockies GitHub org. Nothing here is credited to ORNL alone.

**Outside vs inside:** EnergyPlus is the best known tool in this batch: 1,607 stars, a Spack package, a 2001 paper with 2,837 citing works (only 30 with an ORNL author), and an outside scripting ecosystem (eppy).

| Signal | Finding | Tag | Source |
|---|---|---|---|
| GitHub | NatLabRockies/EnergyPlus: 1,607 stars, 496 forks, last push 2026-10-24 UTC; dependents page gave no count | [KNOWN]; dependents [UNKNOWN] | GitHub API |
| Spack | `energyplus` package.py exists (homepage energyplus.net) | [KNOWN] | spack-packages builtin |
| PyPI | `energyplus` 0.0.1 "EnergyPlus API Python Bindings" (50 downloads last month), an individual's packaging repo; `eppy` 0.6.7, an outside scripting tool for EnergyPlus files (14,201 downloads last month) | [KNOWN]; not official releases | https://pypi.org/pypi/energyplus/json ; https://pypi.org/pypi/eppy/json |
| Citations | "EnergyPlus: creating a new-generation building energy simulation program" (2001, 10.1016/S0378-7788(00)00114-6): 2,837 citing works, 30 with an ORNL author | [KNOWN] | api.openalex.org |

Reasoning: worldwide building-energy use; ORNL is a small share of citers, consistent with a contributor rather than lead role [INFERRED, medium confidence].
