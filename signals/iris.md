
## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- Activity peaked in 2023 and has slowed since. Commits per year went 832, then 499, then 158 in 2025. There are no commits on the default branch after 2025-11-19. [KNOWN: git log] The v3.0.1 tag (2026-02-10) points at that 2025-11-19 commit. [KNOWN] Read: a maintenance phase, while the research continues as spin-offs like MatRIS, Q-IRIS and IRIS-MASH. [INFERRED, medium]
- Public CI is one ubuntu-latest job. The repo also has a `.gitlab-ci.yml` and Slurm-driven test scripts. [KNOWN] Read: a non-public pipeline exists, out of scope (rule 16).
- No named supercomputer appears in the code, which is unusual for an ORNL HPC runtime. It targets vendor backends instead: hip in 134 files, cuda in 70, sycl in 16. [KNOWN: grep] Read: it's built to be portable across machines, not tuned for one facility. [INFERRED, medium]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2020-09-14, last 2025-11-19. 1,700 commits across all branches, 1,698 on default | git | [KNOWN] |
| Commits per year | 2020: 1, 2021: 33, 2022: 177, 2023: 832, 2024: 499, 2025: 158 | git log --all | [KNOWN] |
| Active / new authors per year | 2020: 1/1, 2021: 2/1, 2022: 10/9, 2023: 6/1, 2024: 7/0, 2025: 7/2. 14 emails in total. Top three authors 54%, 20% and 14% | git log | [KNOWN] |
| Tags | v2.0.0 2023-06-02, v3.0.0 2025-05-30, v3.0.1 2026-02-10 | git for-each-ref | [KNOWN] |
| CI | GitHub Actions on ubuntu-latest, plus a non-public GitLab pipeline (out of scope) | repo files | [KNOWN] |
| Funding | OSTI 2438809 and 3018176 list USDOE generically. No DOE CODE record was found by title search | OSTI API | [KNOWN]. The program is [UNKNOWN] |
| Wayback | Nearest captures 2022-08-06 and 2025-07-19 | availability API | [KNOWN], but only bounds the dates |

## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only (RULES 16). Detail in connections/map.md links 117-121.

**Outside vs inside:** The inside targets "extremely heterogeneous" systems (CPUs, GPUs, FPGAs, DSPs, quantum via QIR-EE). Outside, IRIS has no Spack or conda-forge package and 0 dependents; its visible users are ORNL's own layers on top of it (MatRIS, LaRIS, FFTX-IRIS, IRIS-GNN) and academic partners in papers (U. Tsukuba, Carnegie Mellon).

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Spack | No `iris` package.py (404) | [KNOWN] | spack-packages builtin |
| conda-forge | `iris-feedstock` is SciTools Iris (weather library) | [UNRELATED] | github.com/conda-forge/iris-feedstock |
| PyPI | `pyiris` 0.0.2 "IRIS Python API", points to a non-ORNL GitHub copy; 11 downloads last month (2026-10-24; not users) | [KNOWN]; tie to ORNL IRIS [INFERRED] | https://pypi.org/pypi/pyiris/json |
| GitHub "used by" | "0 Repositories" | [KNOWN] | https://github.com/ORNL/iris/network/dependents |
| In-house users | MatRIS ("A Math library using IRIS", catalog row) plus LaRIS, FFTX-IRIS, IRIS-GNN papers | [KNOWN] | github.com/ORNL/MatRIS; OpenAlex |
| Partners | CHARM-SYCL & IRIS (eScience 2024) with U. Tsukuba; FFTX-IRIS with Carnegie Mellon | [KNOWN] | DOI 10.1109/e-science62913.2024.10678717; 10.1145/3624062.3624242 |

Reasoning: no packaging and no dependents, but a steady paper line building on it, suggests an ORNL research runtime used mostly by its own group and a few academic partners [INFERRED, medium confidence].
