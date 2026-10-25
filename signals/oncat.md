
## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- ONCat is a service with no public source repo, so the only code trail is its Python client, pyoncat, on PyPI. [KNOWN: oncat brief] PyPI lists 8 versions. The earliest with files is 1.6.2 (2023-09-05) and the latest is 2.7 (2026-09-24), with 2.6 in June. [KNOWN: pypi.org/pypi/pyoncat/json] Read: the client gets updated a few times a year, so the service is alive. [INFERRED, medium]
- It's funded by Basic Energy Sciences, like the rest of the neutron pipeline. All 3 OSTI hits list BES. [KNOWN: OSTI sponsor fields]
- I didn't look at the service itself, its hosts or its sign-in (rule 16). [KNOWN scope limit]
- No Wayback check this round. The archive API was rate-limiting. [UNKNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| Client releases | 8 PyPI versions. 1.6.2 2023-09-05 to 2.7 2026-09-24 | PyPI JSON API | [KNOWN] |
| Funding | 3 OSTI hits, all BES | OSTI API | [KNOWN] |
| Source repo | None public | oncat brief | [KNOWN] |
| Wayback | Not checked (rate-limited) | | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. ONCat: public PyPI metadata only; no API calls, no client run, no login pages. Refreshes map links 129-130.

**Outside vs inside:** ONCat is a facility data catalog, so its users are SNS and HFIR experimenters, and the only public outside trace is the pyoncat client, with modest downloads and no source repo.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `pyoncat` 2.7 (releases 2.5, 2.6, 2.7), "A Python Client for ONCat (the ORNL Neutron Catalog)", author "ONCat Support", requires `requests`, Python >=3.9 | [KNOWN] | https://pypi.org/pypi/pyoncat/json |
| Downloads | 470 last month, 72 last week (2026-10-24). Not users | [KNOWN] counts | https://pypistats.org/api/packages/pyoncat/recent |
| conda-forge / Spack | None (404) | [KNOWN] | registries |
| Citations | No ONCat software paper found in OpenAlex | [UNKNOWN] | api.openalex.org |

Reasoning: steady client downloads fit scripted data access by facility users [INFERRED, low confidence].
