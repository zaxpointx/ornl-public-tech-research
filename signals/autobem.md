# Signals: autobem


## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- AutoBEM is a slow, steady research line, not a one-off. OSTI has 51 Oak Ridge records that mention it, every year from 2017 to 2026, with 5 to 8 a year lately. [KNOWN] Its DOE CODE record (code-115947) only showed up in November 2023, years after the work started. [KNOWN] Read: the code got registered late, after the papers. [INFERRED, medium]
- The money comes from several places. EERE, mostly its Building Technologies Office, is the biggest, and the Office of Electricity shows up too. The 2021 "Model America" dataset of every US building also lists NNSA's nonproliferation R&D office and the Office of Science. [KNOWN: OSTI sponsor fields] Newer 2025 Model America outputs are funded by BER's earth systems program. [KNOWN] Read: it started as a buildings tool and is drifting toward climate and grid uses. [INFERRED, medium]
- The 2026 AutoBEM framework paper (OSTI 3740812) only lists "USDOE". [KNOWN]
- No Wayback check this round. The archive's API kept failing. [UNKNOWN]
- Source: OSTI API (osti.gov/api/v1), ORNL-filtered by research_org. Word searches can pull namesakes, so counts are rough. No public code exists, so there are no commit or build-target signals. [KNOWN scope limit]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| Record span | 51 ORNL OSTI records, 2017 to 2026 | OSTI API | [KNOWN], rough |
| Code record | code-115947, 2023-11-15, sponsor USDOE | OSTI API | [KNOWN] |
| Top sponsors | USDOE 36, EERE 26, Office of Electricity 7+3, BTO 4 | OSTI API | [KNOWN] |
| Model America data | 2021 (EERE, BTO, NNSA NA-22, OE, SC); 2025 outputs (BER EESS) | OSTI 1774134, 3424892/3 | [KNOWN] |
| Wayback | Not checked | | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users.

**Outside vs inside:** AutoBEM has no public code repo or package, so its outside reach is through its 2023 paper and the Model America data extracts on Zenodo and OSTI. About half of the citing papers have no ORNL author.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Registries | No PyPI, conda-forge or Spack package (404); catalog row has no repo | [KNOWN] | registries; discovery/catalog.csv |
| Citations | "Automatic Building Energy Model Creation (AutoBEM) for Urban-Scale Energy Modeling..." (2023, OpenAlex W4297696525): 25 citing works, 13 with an ORNL author | [KNOWN] | api.openalex.org |
| Data products | "Model America" extracts from ORNL's AutoBEM: Chicago archetypes (Zenodo 10.5281/zenodo.5798154), Arizona (10.5281/zenodo.7644411; v1.1 10.15485/2212792), cited 0-1 times each | [KNOWN] | api.openalex.org |

Reasoning: outside use runs through papers and the published building models, not the code [INFERRED, medium confidence].
