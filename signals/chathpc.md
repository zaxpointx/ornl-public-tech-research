
## History, build targets, funding (discovery pass) (accessed 2026-11-11)

Covers two repos: ORNL/ChatHPC-app (library) and ORNL/ChatHPC-ChatHPCforKokkos-SC25 (paper artifact).

### What the outside tells us that the inside doesn't
- ChatHPC-app is essentially a one-maintainer library: 237 commits, 235 from one author email; a second author appears only in 2026. [KNOWN: git log --all] Read: key-person risk; the multi-author SC25 paper team is not visible as code authors. [INFERRED, medium]
- Its history starts 2024-03-13, sixteen months before the GitHub repo was created (2025-07-21), and the README shows badges for an internal GitLab. [KNOWN: git log 668c386; GitHub API; README L10-L14] Read: GitHub is a publication mirror of internal development. The internal system is out of scope (rule 16). [INFERRED, high]
- Activity peaked in 2025 (158 commits, tags v25.1.0 to v25.7.1 between January and July) around the SC25 submission, then a burst of CI and Docker work on 2026-02-06 and nothing since. [KNOWN: git log, tags] Read: paper-driven cadence; maintenance mode after SC25. [INFERRED, medium]
- No GPU or HPC machine appears in public CI; the only GPU statements are "tested on systems with Ampere A100 and Hopper H100 GPUs" and two-H100 nodes at ORNL's ExCL. HIP/ROCm keyword hits are in the Kokkos translation dataset (HIP-to-Kokkos prompts), not build targets. [KNOWN: SC25 README L17; OSTI 3682544 Appendix; grep] Read: NVIDIA workstation-class GPUs, not leadership supercomputers, are the target. [INFERRED, high]
- Funding is opaque on OSTI ("USDOE"); the SC25 slides acknowledge ASCR's AI-for-Science program (projects named Ellora and Durban), the Next Generation of Scientific Software Technologies program (S4PST, PESO) and SciDAC RAPIDS2. [KNOWN: OSTI 3682544 sponsor_orgs; https://ornl.github.io/ChatHPC/assets/pdf/ChatHPC-SC25.pdf slide 15] The OSTI S4PST 2024-2025 report also matches "ChatHPC for Kokkos". [KNOWN: OSTI API q="ChatHPC for Kokkos" returns 3016977; full text not read]

### Signal ledger
| Signal | ChatHPC-app | SC25 artifact | Source | Tag |
|---|---|---|---|---|
| HEAD | 5c70d58 | 1a4e6a2 | git rev-parse | [KNOWN] |
| History | 2024-03-13 to 2026-02-06; 237 commits all branches, 237 on default | 2025-04-15 to 2025-08-05; 15 commits | git log --all, rev-list | [KNOWN] |
| Commits per year | 2024: 36, 2025: 158, 2026: 43 | 2025: 15 | git log --all, author date | [KNOWN] |
| Active / new authors per year | 2024: 1/1, 2025: 1/0, 2026: 2/1; 2 emails total; top author 99% | 2025: 2/2; one outside typo-fix PR merged | git log | [KNOWN] |
| Tags | v25.1.0 2025-01-25, v25.2.0 02-21, v25.2.1 02-26, v25.3.0 03-04, v25.4.0 04-15, v25.4.1 04-15, v25.7.0 07-22, v25.7.1 07-22; all GitHub releases published 2025-08-05 | v0.0.1 2025-04-15, v0.0.2 04-17, v0.0.3 08-05 | git tags; GitHub releases API | [KNOWN] |
| CI | GitHub Actions on ubuntu-latest: Docker build, push to GHCR, import smoke test; plus internal GitLab CI (out of scope) | none | `.github/workflows/ci-github-runners.yml`; `.gitlab-ci.yml` | [KNOWN] |
| HPC keywords (files) | frontier 0, slurm 0, cuda 5, rocm 2, hip 2, h100 0 | hip 13, cuda 13, h100 1, a100 1, frontier 0 | grep -rliw | [KNOWN]; dataset content, not targets [KNOWN] |
| Issues / PRs | 3 issues, 3 PRs, all closed | 0 open issues | GitHub search API, repo API | [KNOWN] |
| Funding (OSTI) | "USDOE" only on 3682544; contract AC05-00OR22725 | same | OSTI API | [KNOWN] |
| Archive DOIs | Zenodo 10.5281/zenodo.16746629 (v25.7.1) | Zenodo 10.5281/zenodo.15226006 (titled v3.0.0, tag v0.0.3) | Zenodo API | [KNOWN] |
| Container | ghcr.io/ornl/chathpc-app (package page exists, redirects) | n/a | README L67-L70; GitHub packages URL | [KNOWN] |
| Wayback | Not checked this round | | n/a | [UNKNOWN] |
| Job postings | Not searched this round | | n/a | [UNKNOWN] |

### Usage signals (discovery pass, for the connections pass to extend)
| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI / conda-forge / Spack | No `chathpc-app` or `chathpc` on PyPI; no feedstock; no Spack package (control `py_numpy` 200) | [KNOWN] | pypi.org JSON API; conda-forge; spack-packages builtin |
| Install path | `pip install git+ssh://...ChatHPC-app.git` or Docker image from GHCR | [KNOWN] | README L55-L70 |
| GitHub "used by" | 0 repositories, both repos | [KNOWN] | /network/dependents pages |
| Citations | OpenAlex: SC25 paper (W4416199146) cited 6 times: Argonne (2 PETSc agent papers), Nagoya U. + U. Tokyo, Sandia + Smith College, ORNL (2) | [KNOWN] | api.openalex.org filter=cites:W4416199146 |
| In-house reuse | ChatMPI paper (SCA/HPCAsia '26) says it used the ChatHPC library | [KNOWN] | OSTI 3014267 abstract |
| Namesake | OpenAlex "chatHPC: Empowering HPC users..." (2024, 24 citations) is a separate NCCS paper; not counted here | [UNKNOWN] relation | OSTI 2538074 |

Reasoning: real outside citations within a year of SC25, including two Argonne PETSc papers, suggest the approach is noticed by peer labs, but no package, no dependents and a single maintainer suggest the library itself is used mainly by its ORNL group [INFERRED, medium confidence].
