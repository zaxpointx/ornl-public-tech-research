# Signals: exago

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- The move to ORNL brought a large staffing jump. Commits dropped to 33 in 2024 and 9 in 2025, then rose to 255 so far in 2026. Active authors went from 5 in 2025 to 24 in 2026. [KNOWN: git log --all] Read: development restarted as a funded ORNL effort after the handoff from PNNL. [INFERRED, high]
- Frontier is the main HPC target. There are Frontier build scripts under `buildsystem/clang-hip/frontier/`, a `docs/web/README.frontier.md`, and gfx90a, the code name for Frontier's AMD GPU, appears in 4 files. Aurora appears in 4 files and Summit in 3. [KNOWN: repo tree, grep] Read: Frontier is the main target, with other machines as secondary ones. [INFERRED, medium]
- Mirror workflows that are now retired sit in `.github/workflows/deprecated/`. Read: there are non-public pipelines, which are out of scope (rule 16).
- The web archive has no capture of github.com/ORNL/ExaGO yet, while pnnl/ExaGO has captures from 2024-02 to 2026-06. [KNOWN] This fits a repo created on 2026-01-08. [KNOWN: GitHub API]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2019-04-26 (carried over from PNNL), last commit 2026-10-21 on some branch (default 2026-10-19). 1,607 commits across all branches, 1,207 on the default branch | git | [KNOWN] |
| Commits per year | 280, 265, 375, 185, 205, 33, 9, 255 (2019 to 2026) | git log --all | [KNOWN] |
| Active authors per year | 5, 6, 12, 13, 15, 10, 5, 24. 54 emails. Top three 22%, 13%, 12% | git log | [KNOWN] |
| Tags | kpp2 2023-08-17, v2.0.0 2026-05-21, v2.1.0 2026-10-08 | git | [KNOWN] |
| CI | Pre-commit and file-naming checks on ubuntu-22.04, 24.04 and latest | .github/workflows | [KNOWN] |
| Funding | code-176348 lists USDOE generically | OSTI API | [KNOWN]. The program is [UNKNOWN] |
| Wayback | ORNL/ExaGO has none. pnnl/ExaGO has 2024-02-22 and 2026-06-16 | availability API | [KNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16); AgentiGrid not run. Detail in connections/map.md links 148-150, 167.

**Outside vs inside:** The inside is a power-grid optimization toolkit that moved from PNNL to ORNL. Outside, it is packaged in Spack but shows no dependents and almost no citations of its main paper (1 citing work), so visible users are DOE grid-optimization teams; it shares 4 contributor accounts with GridKit but no code.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Spack | `exago` package.py exists, depends on hiop | [KNOWN] | spack-packages builtin exago |
| PyPI / conda-forge | None (404) | [KNOWN] | pypi.org; github.com/conda-forge |
| GitHub "used by" | "0 Repositories"; ORNL/ExaGO 17 stars, 11 forks; last commit 2026-10-20 00:05 UTC (2026-10-19 ET) | [KNOWN] | https://github.com/ORNL/ExaGO/network/dependents ; GitHub API |
| Predecessor | pnnl/ExaGO archived; ORNL LICENSE "uses code from the ExaGO v1.6.0" | [KNOWN]; continuation [INFERRED] | GitHub API; LICENSE |
| Citations | 2022 ExaGO paper (arXiv 2203.10587): 1 citing work; "ExaGO" search mostly namesakes | [KNOWN]; namesakes [UNRELATED] | api.openalex.org |
| GridKit overlap | No build tie; 4 shared contributor accounts (counts only) | [KNOWN] | map.md link 150 |

Reasoning: a DOE-internal grid optimization code with Spack packaging and a lab-to-lab handover, not widely adopted outside [INFERRED, medium confidence]. AgentiGrid is "experimental" per CHANGELOG 2.1 only.

## Sweep notes (fact-check pass, 2026-10-24)
- Spot-checked against a fresh clone using author dates: across all branches, 2025 has 9 commits from 5 authors and 2026 has 255 from 24, matching the discovery pass. On the default branch (`develop`) alone, 2026 has 47 commits from 10 authors, so most 2026 work sits on the other 44 remote branches. The "--all" label is correct; read the jump with that in mind.
