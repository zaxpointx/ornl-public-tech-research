
## History, build targets, funding (discovery pass) (accessed 2026-11-11)

### What the outside tells us that the inside doesn't
- The public repo is a release snapshot, not a development history: two commits on 2026-07-30 by one author, the first titled "Add files from internal repository for OS release." [KNOWN: git log --all] Read: development happened elsewhere; the public signals are too thin to say anything about team activity or cadence. [INFERRED, high]
- A test README inside the snapshot is dated 2025-04-15, over a year before the public release. [KNOWN: `tests/gpuTests/README.md` L2] Read: at least about 15 months of internal work before release. [INFERRED, medium]
- The DOE CODE record lists ten authors, nine ORNL and one Argonne. [KNOWN: OSTI API code-186894] The Argonne author is the only outside-institution signal. Read: a PETSc-side collaboration, given the GPU path runs through PETSc. [INFERRED, low: the record does not say what the Argonne author contributed]
- Machine targets come from docs, not CI: build guides for Frontier (AMD MI250X, gfx90a, ROCm, PETSc with HIP), Perlmutter (NVIDIA A100), Aurora (Intel oneAPI) and ORNL CADES condos; no public CI at all. [KNOWN: `doc/source/build-openfoam-*.md`; no `.github/workflows`] Read: written for the three DOE leadership-class GPU families, tested by hand. [INFERRED, medium]
- Funding: EERE Advanced Materials & Manufacturing Technologies Office (AMMTO) only. [KNOWN: OSTI API code-186894]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2026-07-30 14:42 ET, last 2026-07-30 15:06 ET; 2 commits on all branches (HEAD d298a00) | git log --all, git rev-list | [KNOWN] |
| Commits per year | 2026: 2 | git log --all, author date | [KNOWN] |
| Active / new authors per year | 2026: 1/1 (1 email in total) | git log | [KNOWN] |
| Tags | v1.0 2026-07-30 (GitHub release same day) | git for-each-ref; GitHub releases API | [KNOWN] |
| CI | None in repo | tree | [KNOWN] |
| HPC keywords (files) | frontier 6, perlmutter 2, aurora 2, gfx90a 1, rocm 1, hip 1, cuda 2, a100 1, slurm 0, summit 0 | grep -rliw of working tree | [KNOWN]; hits are build docs and the README, not code paths [KNOWN] |
| GPU mechanism | PETSc Kokkos back end (`mat_type mpiaijkokkos`, `vec_type kokkos`) via petsc4Foam | `tests/gpuTests/.../fvSolution_gpu` L28-L37 | [KNOWN] |
| Funding | EERE AMMTO; contract AC05-00OR22725 | OSTI API code-186894 | [KNOWN] |
| Archive DOI | Zenodo 10.5281/zenodo.21708850, gpl-3.0-or-later, creators affiliated ORNL | Zenodo API record 21708850 | [KNOWN] |
| Repo stats | 5 stars, 2 forks, 0 open issues | GitHub API | [KNOWN] |
| Wayback | Not checked this round | n/a | [UNKNOWN] |
| Job postings | Not searched this round | n/a | [UNKNOWN] |

### Usage signals (discovery pass, for the connections pass to extend)
| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI / conda-forge / Spack | No `dedfoam` package on any (404). Not expected for an OpenFOAM solver | [KNOWN] | pypi.org/pypi/dedfoam/json; github.com/conda-forge/dedfoam-feedstock; spack-packages builtin `dedfoam`, `py_dedfoam` (control: `openfoam` package.py returns 200) |
| GitHub "used by" | 0 repositories | [KNOWN] | https://github.com/ORNL/DEDFOAM/network/dependents |
| Citations | OpenAlex: one work matches "DEDFoam", the Zenodo release itself, 0 citations; institutions ORNL and Argonne | [KNOWN] | api.openalex.org search=DEDFoam; doi:10.5281/zenodo.21708850 |
| Paper | No OSTI paper about DEDFoam found; OSTI "DEDFoam" returns only the code record | [KNOWN] bounded negative | OSTI API q=DEDFoam |

Reasoning: three months after release there is no visible outside use or citation, which is normal for a new solver with no paper yet; the signal says "too early", not "unused" [INFERRED, medium confidence].
