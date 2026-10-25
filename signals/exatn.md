# Signals: exatn

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- ExaTN had a big burst and then a slow fade. 501 commits in 2019, then 350, 238, 106 and 25 in 2023, and nothing after 2023-07-19. [KNOWN: git log --all] Read: dormant, not formally archived. [INFERRED, medium]
- It's mostly one person's code. The top author has 73% of commits and the next has 16%, out of 9 emails. No more than 5 people were active in any year. [KNOWN] Read: a high bus-factor risk, which may explain why it stopped. [INFERRED, low]
- It was built for Summit, ORNL's previous supercomputer with NVIDIA V100 GPUs. The README gives a Summit build example with CUDA architecture 70 (V100), and test comments size problems for Summit nodes. Nothing mentions Frontier. [KNOWN: README, NumServerTester.cpp] Read: it never got moved to the AMD machine. [INFERRED, medium]
- There's a `.gitlab-ci.yml` beside the GitHub workflow, so a non-public pipeline exists, out of scope (rule 16). [KNOWN that the file exists]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2018-11-01, last 2023-07-19. 1,235 commits on all branches, 1,202 on devel | git | [KNOWN] |
| Commits per year | 15, 501, 350, 238, 106, 25 (2018 to 2023) | git log --all | [KNOWN] |
| Active authors per year | 2, 5, 3, 2, 3, 3. 9 emails. Top two 73%, 16% | git log | [KNOWN] |
| Tags | None | git | [KNOWN] |
| CI | ci-linux on ubuntu-latest, plus a .gitlab-ci.yml (out of scope) | repo | [KNOWN] |
| Build targets | Summit example with CUDA arch 70. SYCL hits are all inside the bundled Eigen library | README, tpls/eigen | [KNOWN] |
| Funding | code-45739 lists USDOE generically. Other ExaTN papers on OSTI list ASCR and LDRD once each | OSTI API | [KNOWN], mix is [INFERRED, low] |
| Wayback | Nearest captures 2020-12-27, 2023-12-16, 2025-11-21 | availability API | [KNOWN], only bounds dates |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. Map links 10, 42, 162.

**Outside vs inside:** The repo has been quiet since 2023, but its 2022 paper is mostly cited by groups outside ORNL (16 of 19 citing works have no ORNL author, e.g. Technical University of Munich, NVIDIA), so ExaTN lives on more as a reference than as a dependency.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI / conda-forge / Spack | None (404) | [KNOWN] | registries |
| GitHub | 69 stars, 20 forks, last push 2023-07-24 UTC; dependents page gave no count | [KNOWN]; dependents [UNKNOWN] | GitHub API; network/dependents |
| Catalog consumer | TNQVM finds ExaTN optionally (CMakeLists.txt lines 76-79) | [KNOWN] | ORNL-QCI/tnqvm |
| Citations | Frontiers 2022 paper (10.3389/fams.2022.838601): 19 citing works, 3 with an ORNL author | [KNOWN] | api.openalex.org |

Reasoning: outside citations without packaging point to readers comparing or building on the ideas, not running the code [INFERRED, medium confidence].
