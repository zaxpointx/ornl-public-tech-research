# Signals: hecbench

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- Many people have touched it in a light way. There are 119 author emails in total, 43 of them active in 2020, and the top two authors have 24% and 19% of commits. [KNOWN: git log] Read: a central maintainer accepts many small benchmark contributions. [INFERRED, medium]
- Activity jumped again in 2026, with 1,124 commits so far after 324 in 2024. [KNOWN] Read: renewed investment, which fits its use in recent LLM-for-HPC papers that the fact-check pass found. [INFERRED, low]
- Web archive captures of github.com/ORNL/HeCBench only start in 2026-04, even though the repo dates from 2020-08-06 on GitHub. A fork back from a personal account was made on 2026-02-27. [KNOWN: availability API, GitHub API] Read: the repo was probably transferred into the ORNL org in early 2026. [INFERRED, medium]
- It has no CI, no releases and no tags. [KNOWN] I didn't run a keyword count of supercomputer names this round. The reading-pass folder counts already show the GPU vendor spread.

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2020-08-06, last 2026-10-22. 6,011 commits across all branches, 5,998 on default | git | [KNOWN] |
| Commits per year | 2020: 868, 2021: 1,201, 2022: 930, 2023: 1,012, 2024: 324, 2025: 552, 2026: 1,124 | git log --all, author date | [KNOWN] |
| Active authors per year | 43, 38, 20, 23, 13, 9, 19 (2020 to 2026). 119 emails in total | git log, author date | [KNOWN] |
| CI / tags | None | repo tree, git | [KNOWN] |
| Funding | No OSTI software record. Not checked further this round | OSTI | [UNKNOWN] |
| Wayback | github.com/ORNL/HeCBench nearest captures 2026-04-30 and 2026-10-06 | availability API | [KNOWN], but only bounds the dates |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16; DVC data hosting not examined). Source repo is ORNL/HeCBench only; a separate personal fork is not used as a source. Institution names from OpenAlex/OSTI, no individuals profiled. Detail in connections/map.md links 152-158.

**Outside vs inside:** The inside describes a benchmark suite of the same kernels in CUDA, HIP, SYCL and OpenMP for studying portability. Outside, HeCBench has the broadest visible use of any ORNL tool checked so far: 122 forks and dozens of papers from universities, LLNL, Argonne and vendor co-authors that use it as a test corpus, especially for compilers and LLM code translation, even though GitHub shows 0 dependents (expected for a benchmark suite).

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Packages | None expected or found (benchmark suite) | [KNOWN] | n/a |
| GitHub "used by" | "0 Repositories" | [KNOWN] | https://github.com/ORNL/HeCBench/network/dependents |
| Forks / stars | 122 forks, 310 stars (GitHub API, 2026-10-24); interest, not users | [KNOWN] | GitHub API repos/ORNL/HeCBench |
| Outside papers (OpenAlex, 55 matches) | LRZ and TU Munich (2025 programming-model comparison), Heidelberg University (2022), Universidad Complutense de Madrid (2024), TU Wien (2026), Iowa State, Stony Brook, RIKEN / Institute of Science Tokyo with LLNL, Technion with Argonne/Stanford (LLM parallel-code agents), Intel and Cisco co-authors (OMPar 2024) | [KNOWN] list; use vs cite [INFERRED] from titles | api.openalex.org search=HeCBench |
| ORNL in-house use (OSTI) | ChatPORT (OSTI 3009454, 3009431), ChatHPC (OSTI 3682544), Codex kernel-generation evaluation (OSTI 2000371) | [KNOWN] full-text match; use [INFERRED] | https://www.osti.gov/api/v1/records?q=HeCBench |
| LLNL use (OSTI) | PyOMP (2479416), Proteus JIT (3013408), OpenMP GPU parameter prediction (2998335), HPC benchmark survey (3029610), GPU JIT interfaces (3376636) | [KNOWN] full-text match; use [INFERRED] | same |
| Downloads | Not applicable | [KNOWN] | n/a |

Reasoning: a large fork count plus many outside compiler, programming-model and LLM-for-HPC papers suggests HeCBench has become a shared research test corpus, used well beyond ORNL and Argonne [INFERRED, medium-high confidence]. Claimed audience (portability researchers) matches visible users, with LLM code-translation work as a newer, larger group.
