<!-- Scout section goes above -->

## Scout: history, build targets, funding (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- This is the oldest codebase in batch 06. The first commit is 2012-08-31, and there's been steady, low activity ever since, peaking at 328 commits in 2020. [KNOWN: git log] Read: long-running funded work, not a one-off. [INFERRED, high]
- No single author dominates. The top three each have about 23 to 25%, and 2 to 8 authors are active in any given year. [KNOWN] Read: it's not one person's project. [INFERRED, medium]
- Where the money comes from changed the scope. Among OSTI records matching "xolotl", Nuclear Energy is the top sponsor (22 hits) ahead of Fusion Energy Sciences (10) and NNSA (9). [KNOWN: OSTI API, 40 records] Read: it started as fusion plasma-surface work and grew into fission fuel, which matches the README's two domains. [INFERRED, medium; the keyword hits may include other uses of the word]
- CI runs on macos-latest and ubuntu-latest only, and no named supercomputer appears in the code (hip in 4 files, cuda in 3). [KNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2012-08-31, last 2026-10-21. 2,292 commits across all branches, 2,097 on default | git | [KNOWN] |
| Commits per year | 9, 210, 270, 36, 35, 72, 216, 205, 328, 260, 173, 162, 153, 77, 86 (2012 to 2026) | git log --all | [KNOWN] |
| Active authors per year | 2, 5, 5, 3, 3, 4, 3, 5, 5, 6, 8, 5, 4, 2, 5. 30 emails in total. Top three 25%, 25%, 23% | git log | [KNOWN] |
| Tags | v3.2.3 2025-12-15, v3.3.0 2026-03-03, v3.4.0 2026-09-03 | git | [KNOWN] |
| Funding | OSTI 1513390 (ASCR). Keyword hits: NE 22, FES 10, NNSA 9, ASCR 6 | OSTI API | [KNOWN] for 1513390. The mix is [INFERRED] |
| Wayback | Nearest captures 2018-06-17, 2022-03-07 and 2026-03-05 | availability API | [KNOWN], but only bounds the dates |
| Note | GitHub history starts in 2012, which fits the 2012 LICENSE date. That eases Reader's open question about earlier history living elsewhere | git | [INFERRED, medium] |

## Connector: who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16). Detail in connections/map.md links 136-140.

**Outside vs inside:** The inside models plasma-facing divertor materials and fission fuel. Outside, the six copyright holders, the Spack package and fission-gas papers with INL, LANL and U. Florida show a multi-lab fusion/fission materials community, broader than ORNL alone; there is no PyPI or conda presence and 0 GitHub dependents.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Spack | `xolotl` package.py exists (3.1.0; depends on "petsc ~fortran +kokkos") | [KNOWN] | spack-packages builtin xolotl |
| conda-forge / PyPI | None (404) | [KNOWN] | github.com/conda-forge; pypi.org |
| GitHub "used by" | "0 Repositories" | [KNOWN] | https://github.com/ORNL-Fusion/xolotl/network/dependents |
| Copyright holders | UT-Battelle, U. Tennessee, UChicago Argonne, U. Florida, Penn State, U. Michigan | [KNOWN] | LICENSE |
| Citations | OpenAlex "xolotl cluster dynamics": 65 hits, incl. a 2022 UO2 fission-gas paper (INL, LANL, ORNL, U. Florida; 33 cites) and a 2023 outside-university paper on accelerating cluster dynamics for fission gas | [KNOWN] list; whether each uses Xolotl [INFERRED] from titles/abstracts | api.openalex.org |
| Downloads | Not applicable (no package registry with stats) | [KNOWN] | n/a |

Reasoning: source-built HPC code with Spack packaging and multi-institution authorship suggests users are DOE fusion/fission materials teams and partner universities [INFERRED, medium confidence].
