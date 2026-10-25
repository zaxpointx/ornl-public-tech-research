# Signals: situ


## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- The only real trace is one software record, OSTI 1232450 from 2014-06-16, and its sponsor field is blank (it just reads "u"). [KNOWN] Read: a 2014 code drop with no visible funder, and no sign of later work. [INFERRED, medium]
- Searching OSTI for "Situ" mostly pulls up "in situ" experiment papers, which are namesakes, so there's no usable count. [KNOWN method note; those hits are UNRELATED]
- Whether it's alive is [UNKNOWN]. There's no repo, no newer record and no Wayback data.
- No Wayback check this round. The archive's API kept failing. [UNKNOWN]
- Source: OSTI API (osti.gov/api/v1), ORNL-filtered by research_org. Word searches can pull namesakes, so counts are rough. No public code exists, so there are no commit or build-target signals. [KNOWN scope limit]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| Software record | OSTI 1232450, 2014-06-16, sponsor blank | OSTI API | [KNOWN] |
| Later records | None identified (search swamped by "in situ") | OSTI API | [UNKNOWN] |
| Wayback | Not checked | | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. Situ is draft-osti-only with no repo.

**Outside vs inside:** Situ left almost no outside trace: its 2012 VAST paper has 12 citing works (1 with an ORNL author), and the only later record is a 2018 ORNL report pairing it with FASGuard.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Registries | PyPI `situ` 0.5.0 is a Python-to-JS component compiler, a namesake | [UNRELATED] | https://pypi.org/pypi/situ/json |
| Citations | "situ: Situational understanding and discovery for cyber attacks" (IEEE VAST 2012, 10.1109/vast.2012.6400503): 12 citing, 1 with ORNL author | [KNOWN] | api.openalex.org |
| Later record | "Situ/FASGuard: Combining Anomaly Detection with Signature Generation" (OSTI 3027397, 2018, ORNL author) | [KNOWN] title | api.openalex.org |
| Namesakes | Other "streaming anomaly detection" datasets are different projects | [UNRELATED] | api.openalex.org |

Reasoning: a research prototype cited by a small visual-analytics and cyber audience, inactive in public since 2018 [INFERRED, medium confidence].
