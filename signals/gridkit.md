# Signals: gridkit

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- GridKit sat almost still for years, then took off. There were 2 to 20 commits a year from 2017 to 2024, then 426 in 2025 and 947 so far in 2026, with active authors going from 3 to 21 to 25. [KNOWN: git log --all] Read: a project that got a new team and real funding around 2025. [INFERRED, medium]
- Most of the work happens on side branches. 1,435 commits across all branches against 356 on the default branch (develop). [KNOWN] Read: lots of parallel feature work that hasn't merged yet. [INFERRED, medium]
- The earliest Wayback capture of the GitHub page is 2025-07-01, even though the history starts in 2017. Read: the public ORNL/GridKit page is likely recent, and the older history came along with the code. [INFERRED, low; Wayback only gives bounds]
- No supercomputer is named in the code. The words "summit", "aurora" and "frontier" show up only as power-grid bus names in test cases and as a math term in docs. [UNRELATED: checked each hit] GPU support shows up as CUDA in 8 files and HIP in 9. [KNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2017-02-01, last 2026-10-23. 1,435 commits on all branches, 356 on develop | git | [KNOWN] |
| Commits per year | 15, 2, 7, 0, 8, 5, 5, 20, 426, 947 (2017 to 2026) | git log --all | [KNOWN] |
| Active authors per year | 1, 1, 1, 0, 2, 4, 1, 3, 21, 25. 35 emails. Top three 30%, 14%, 8% | git log | [KNOWN] |
| Tags | v0.0.7 2023-07-17, v0.1.0 2025-04-14, v0.2.0 2026-10-01 | git | [KNOWN] |
| CI | pre-commit and a Spack default build on ubuntu runners | .github/workflows | [KNOWN] |
| Funding | DOE CODE code-152622 (2025-03-14) lists ORNL as research org and USDOE generically as sponsor | OSTI API | [KNOWN] |
| Namesake | OSTI 1340202 is LLNL's 2016 GridKit, not this project | OSTI API | [UNRELATED] |
| Wayback | Nearest capture 2025-07-01 for every date checked | availability API | [KNOWN], only bounds dates |

## Sweep 2 spot-check (fact-check pass, 2026-10-24)
- Commits per year on all branches match a fresh clone exactly (15, 2, 7, 0, 8, 5, 5, 20, 426, 947 for 2017 to 2026). Active authors for 2024, 2025 and 2026 come out as 3, 19 and 21 by distinct name; the discovery pass's 21 and 25 for 2025 and 2026 likely count distinct emails, so the same people may appear under more than one email. Minor: 2020 had 0 commits, so "2 to 20 a year" in the summary line skips one empty year.

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. Map links 1, 7, 55, 57, 150.

**Outside vs inside:** The inside describes a flexible grid-simulation framework. Outside, it isn't packaged anywhere, has no GitHub dependents and no paper of its own in OpenAlex, so visible use is the ORNL team and its partners building from source.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `gridkit` 1.0.1 is an unrelated infinite-grid Python library (1,253 downloads last month, not this project) | [UNRELATED] | https://pypi.org/pypi/gridkit/json ; pypistats |
| conda-forge / Spack | No feedstock, no Spack package (404) | [KNOWN] | github.com/conda-forge; spack-packages builtin |
| GitHub "used by" | "0 Repositories"; 27 stars, 11 forks | [KNOWN] | https://github.com/ORNL/GridKit/network/dependents ; GitHub API |
| Papers | No GridKit software paper found in OpenAlex; nearest ORNL hit is an OSTI project plan, "Next Generation Grid Simulations" (10.2172/3385022) | [UNKNOWN] | api.openalex.org |
| Namesakes | 2004 "GRIDKIT" overlay networks paper and 2016 Zenodo "Gridkit" grid extracts are other projects | [UNRELATED] | api.openalex.org |

Reasoning: no registry, dependents or citations suggests an early-stage (pre-1.0) research framework used by its own developers [INFERRED, medium confidence].
