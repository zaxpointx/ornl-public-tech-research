# Signals: matris

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- It's effectively dormant. There were 4 commits in 2025, and the last was 2025-10-23. In 2022 there were 247. [KNOWN: git log] That supports the reading-pass status of unknown. [INFERRED, medium]
- The history is older than the repo. Commits start on 2022-03-01, but GitHub created the repo on 2023-11-08. [KNOWN: git, GitHub API] Read: it was developed elsewhere and then published with its history. [INFERRED, high]
- Two people wrote almost everything, with 69% and 27% of commits out of 9 emails. [KNOWN] The GitHub API lists 5 user accounts, while the brief says 2. The fact-check pass should settle which is right. [KNOWN: API 2026-10-24]
- It targets GPUs from more than one vendor: hip in 40 files, cuda in 45, rocm in 7, slurm in 5, crusher in 1. There's no CI. [KNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2022-03-01, last commit 2025-10-23. 565 commits | git | [KNOWN] |
| Commits per year | 2022: 247, 2023: 181, 2024: 133, 2025: 4 | git log | [KNOWN] |
| Active authors per year | 2022: 3, 2023: 7, 2024: 5, 2025: 1 | git log | [KNOWN] |
| Tags / CI | None | git, repo tree | [KNOWN] |
| Funding | OSTI 2441045 and 2439841 list DOE Office of Science | OSTI API | [KNOWN] |
| Wayback | One capture, 2025-03-05 | availability API | [KNOWN] |

## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only (RULES 16). Detail in connections/map.md links 120, 169.

**Outside vs inside:** The inside is a heterogeneous BLAS/LAPACK layer that requires ORNL's IRIS runtime. Outside, there is no package, no dependents, 1 star and 0 forks, and status is unknown; the PyPI name "matris" belongs to an unrelated project. Visible use is ORNL's IRIS group and its papers.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Spack / conda-forge | None (404) | [KNOWN] | spack-packages builtin; github.com/conda-forge |
| PyPI | `matris` 1.0.0 "MatRIS model" points to HPC-AI-Team, a different project | [UNRELATED] | https://pypi.org/pypi/matris/json |
| GitHub | "0 Repositories" dependents; 1 star, 0 forks; last push 2025-10-23 | [KNOWN] | https://github.com/ORNL/MatRIS ; GitHub API |
| Build tie | Links `iris` in src/algorithms/{blas,lapack,math}/CMakeLists.txt | [KNOWN] | repo |
| Benchmarked against | StarPU, PaRSEC, MAGMA, Chameleon, OmpSs-2 container recipes (containers/*.def), not dependencies | [KNOWN] | repo |
| Citations | SC-W 2023 MatRIS paper (10.1145/3624062.3624184): 11 citing works | [KNOWN] | api.openalex.org |

Reasoning: an ORNL research library within the IRIS ecosystem with no outside packaging [INFERRED, medium confidence].
