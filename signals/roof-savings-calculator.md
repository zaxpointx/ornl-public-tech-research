# Signals: roof-savings-calculator


## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- This one looks finished. The software record (OSTI 1238771) is from 2013-11-22. ORNL records mentioning it run from 2010 to 2019 and then stop, with only 12 in all. [KNOWN] Read: a project from the early 2010s that's no longer being written about. Whether the web tool still runs is [UNKNOWN], since I didn't touch the ORNL host.
- It's paid for by buildings money. Every named sponsor is EERE, mostly its Building Technologies Office. [KNOWN: OSTI sponsor fields]
- No Wayback check this round. The archive's API kept failing. [UNKNOWN]
- Source: OSTI API (osti.gov/api/v1), ORNL-filtered by research_org. Word searches can pull namesakes, so counts are rough. No public code exists, so there are no commit or build-target signals. [KNOWN scope limit]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| Software record | OSTI 1238771, 2013-11-22, EERE BTO | OSTI API | [KNOWN] |
| Record span | 12 ORNL records, 2010 to 2019, none since | OSTI API | [KNOWN], rough |
| Sponsors | All EERE (BTO named on 3) | OSTI API | [KNOWN] |
| Still online | Not checked (no host probing) | | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. Roof Savings Calculator is draft-osti-only and a web app with no repo.

**Outside vs inside:** A small but mostly outside citation trail: the 2011 development paper has 9 citing works, 7 without an ORNL author, likely cool-roof researchers.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Registries | No `roof-savings-calculator` on PyPI or conda-forge (404) | [KNOWN] | registries |
| Citations | "Development of a Roof Savings Calculator" (2011, OpenAlex W1521625767): 9 citing, 2 with ORNL author. "Visual Analytics for Roof Savings Calculator Ensembles" (2012): 3 cites | [KNOWN] | api.openalex.org |

Reasoning: a niche public calculator with modest outside academic use; web traffic is not visible [INFERRED, low confidence].
