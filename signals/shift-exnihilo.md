# Signals: shift-exnihilo


## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- Shift was built for supercomputers from the start. The 2015 benchmarking paper (OSTI 1237627) lists the Oak Ridge Leadership Computing Facility as a research org next to ORNL, with Office of Science money. [KNOWN]
- It's still being pushed onto new machines. A 2025 paper on automated variance reduction "on advanced architectures" (OSTI 3013520) is funded by NNSA and the Office of Science. Variance reduction is a trick for getting accurate Monte Carlo answers faster. [KNOWN] Read: GPU-era supercomputer work is ongoing. [INFERRED, medium]
- One record names Nuclear Energy's NEAMS modeling program and one names NNSA, but most just say "USDOE". [KNOWN, narrow search, rough] Shift also ships inside SCALE as CSAS-Shift (per the brief), so some of SCALE's NRC and DOE money likely helps it too. [INFERRED, low]
- No DOE CODE record turned up for Shift on its own. [KNOWN for this search]
- No Wayback check this round. The archive's API kept failing. [UNKNOWN]
- Source: OSTI API (osti.gov/api/v1), ORNL-filtered by research_org. Word searches can pull namesakes, so counts are rough. No public code exists, so there are no commit or build-target signals. [KNOWN scope limit]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| Benchmark paper | OSTI 1237627, 2015-12-21, DOE SC; OLCF listed | OSTI API | [KNOWN] |
| Recent architecture work | OSTI 3013520, 2025-05-28, NNSA and SC | OSTI API | [KNOWN] |
| Other sponsors | NEAMS x1, NNSA x1, USDOE x13 | OSTI API | [KNOWN], rough |
| Own code record | None found | OSTI API | [KNOWN] |
| Wayback | Not checked | | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. Shift ships inside SCALE and has no public repo.

**Outside vs inside:** Shift is mostly an ORNL research code from the outside: 95 of the 134 papers citing its 2015 benchmark paper include an ORNL author, so outside uptake is real but smaller than SCALE's.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Registries | PyPI `shift` 0.0.4 is a generic Python template library, a namesake; no `exnihilo` package | [UNRELATED]; [KNOWN] | https://pypi.org/pypi/shift/json |
| Public repo / dependents | None | [KNOWN] | projects/shift-exnihilo.md |
| Citations | "Implementation, capabilities, and benchmarking of Shift..." (J. Comput. Phys. 2015, 10.1016/j.jcp.2015.12.037): 134 citing, 95 with ORNL author. "Nuclide depletion capabilities in the Shift Monte Carlo code" (2017, 10.1016/j.anucene.2017.11.042): 42 cites | [KNOWN] | api.openalex.org |

Reasoning: development and use are concentrated at ORNL; outside citers likely reach it through SCALE's CSAS-Shift [INFERRED, low confidence].
