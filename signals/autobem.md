<!-- history section (discovery pass) goes above -->

## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users.

**Outside vs inside:** AutoBEM has no public code repo or package, so its outside reach is through its 2023 paper and the Model America data extracts on Zenodo and OSTI. About half of the citing papers have no ORNL author.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Registries | No PyPI, conda-forge or Spack package (404); catalog row has no repo | [KNOWN] | registries; discovery/catalog.csv |
| Citations | "Automatic Building Energy Model Creation (AutoBEM) for Urban-Scale Energy Modeling..." (2023, OpenAlex W4297696525): 25 citing works, 13 with an ORNL author | [KNOWN] | api.openalex.org |
| Data products | "Model America" extracts from ORNL's AutoBEM: Chicago archetypes (Zenodo 10.5281/zenodo.5798154), Arizona (10.5281/zenodo.7644411; v1.1 10.15485/2212792), cited 0-1 times each | [KNOWN] | api.openalex.org |

Reasoning: outside use runs through papers and the published building models, not the code [INFERRED, medium confidence].
