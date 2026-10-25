# Signals: scale


## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- SCALE's DOE CODE record (code-138261) is only from 2023-02-22 and lists just "USDOE", even though the suite is decades old. [KNOWN: OSTI] Read: like AutoBEM, the registration came long after the code. [INFERRED, high]
- The clearest outside funder is the Nuclear Regulatory Commission. NRC pays for SCALE model and benchmark datasets, like the non-light-water reactor models (OSTI 2572299, 2025) and an HTR-PROTEUS benchmark model (2026). [KNOWN] A new criticality-safety tool, IRMA (code-186978, 2026-08), lists a DOE and NRC collaboration on HALEU fuel transport. HALEU is a more enriched reactor fuel. [KNOWN] Read: the regulator is a paying customer, which ties in with the outside-citation pattern on the usage side. [INFERRED, medium]
- NNSA also shows up on a couple of records. [KNOWN] I didn't go further on anything weapons- or export-related (rule 16).
- Searching OSTI for the word "SCALE" is noisy, so I kept to the cited records and a narrow search. [KNOWN method note]
- No Wayback check this round. The archive's API kept failing. [UNKNOWN]
- Source: OSTI API (osti.gov/api/v1), ORNL-filtered by research_org. Word searches can pull namesakes, so counts are rough. No public code exists, so there are no commit or build-target signals. [KNOWN scope limit]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| Code record | code-138261, 2023-02-22, USDOE | OSTI API | [KNOWN] |
| NRC-funded data | OSTI 2572299 (2025-07-29), 3367418 (2026-06-18) | OSTI API | [KNOWN] |
| Related tool | IRMA code-186978, 2026-08-03, DOE and NRC HALEU collaboration | OSTI API | [KNOWN] |
| Other sponsors | NNSA x2, USNRC x2 in narrow search | OSTI API | [KNOWN], small sample |
| Wayback | Not checked | | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. SCALE is distributed under license with no public repo, so there are no registry packages or GitHub dependents to count, by design. No license or distribution portal was opened.

**Outside vs inside:** SCALE's outside use shows only in citations: the SCALE 6 paper has 171 citing works, about 69% without an ORNL author, which fits a licensed tool used by safety analysts and regulators elsewhere.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Registries | PyPI `scale` 1.1.2 is a single-cell ATAC-seq analysis tool, a namesake; no conda-forge feedstock | [UNRELATED]; [KNOWN] | https://pypi.org/pypi/scale/json ; github.com/conda-forge |
| Public repo / dependents | None; not openly distributed (projects/scale.md) | [KNOWN] | https://www.ornl.gov/scale |
| Citations | "SCALE 6: Comprehensive Nuclear Safety Analysis Code System" (Nuclear Technology 2011, 10.13182/nt10-163): 171 citing, 53 with ORNL author. "SCALE Code System" report (2020, 10.2172/1616812): 88 citing, 24 ORNL | [KNOWN] | api.openalex.org |

Reasoning: widely cited outside ORNL despite licensing, consistent with an established nuclear safety standard tool [INFERRED, medium confidence].
