
## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. ONCat: public PyPI metadata only; no API calls, no client run, no login pages. Refreshes map links 129-130.

**Outside vs inside:** ONCat is a facility data catalog, so its users are SNS and HFIR experimenters, and the only public outside trace is the pyoncat client, with modest downloads and no source repo.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `pyoncat` 2.7 (releases 2.5, 2.6, 2.7), "A Python Client for ONCat (the ORNL Neutron Catalog)", author "ONCat Support", requires `requests`, Python >=3.9 | [KNOWN] | https://pypi.org/pypi/pyoncat/json |
| Downloads | 470 last month, 72 last week (2026-10-24). Not users | [KNOWN] counts | https://pypistats.org/api/packages/pyoncat/recent |
| conda-forge / Spack | None (404) | [KNOWN] | registries |
| Citations | No ONCat software paper found in OpenAlex | [UNKNOWN] | api.openalex.org |

Reasoning: steady client downloads fit scripted data access by facility users [INFERRED, low confidence].
