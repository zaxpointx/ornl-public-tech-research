# Signals: xacc

## Scout: history, build targets, funding (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- Development stopped in 2023. Commits fell from 887 in 2020 to 135 in 2022 and 32 in 2023, and the last commit on any branch was 2023-08-01. [KNOWN: git log --all] GitHub's 2024-08-13 push timestamp doesn't match any commit date in the history. [KNOWN: GitHub API vs git log] Read: that push was probably repo housekeeping, such as the org move or branch changes, not new code. [INFERRED, low]
- Two people did most of the work, with 62% and 21% of commits. Active authors peaked at 11 in 2020. [KNOWN]
- Public CI is broad (Linux, macOS, aarch64, MPI, Python and Docker builds) but has no GPU or HPC runners, and no named supercomputer appears outside the bundled third-party libraries. [KNOWN: workflows, grep excluding tpls/] Read: it's a portable framework aimed at outside quantum backends, not at ORNL machines. [INFERRED, medium]
- The web archive has github.com/ORNL-QCI/xacc from 2024-10 and eclipse-xacc/xacc from 2025-01. [KNOWN: availability API] Read: the move to eclipse-xacc took place around late 2024. [INFERRED, low; captures only bound dates]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2016-11-11, last commit 2023-08-01. 2,598 commits across all branches, 2,547 on the default branch | git | [KNOWN] |
| Commits per year | 2016: 1, 2017: 429, 2018: 344, 2019: 398, 2020: 887, 2021: 372, 2022: 135, 2023: 32 | git log --all, author date | [KNOWN] |
| Active authors per year | 1, 6, 5, 9, 11, 10, 7, 4 (2016 to 2023). 31 emails | git log | [KNOWN] |
| Tags / releases | None | git | [KNOWN] |
| CI | 7 GitHub workflows on ubuntu-latest and macos-latest | .github/workflows | [KNOWN] |
| Funding | code-5041 lists USDOE generically | OSTI API | [KNOWN]. The program is [UNKNOWN] |
| Wayback | ORNL-QCI/xacc 2024-10-18 and 2026-06-07. eclipse-xacc/xacc 2025-01-20 and 2025-10-28 | availability API | [KNOWN], but only bounds the dates |

## Connector: who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16); institution names from OpenAlex, no individuals profiled. Detail in connections/map.md links 144, 159-164.

**Outside vs inside:** The inside presents XACC as a hardware-agnostic framework for quantum-classical programming across many vendors' QPUs. Outside, it is heavily cited (143 citing works, two thirds with no ORNL author) but lightly installed: 35 PyPI downloads last month, no conda-forge or Spack package, 0 GitHub dependents, and code quiet since 2023-2024. Hands-on users visible in public traces are ORNL groups, ORNL plugins (TNQVM, QIR-EE's optional backend) and partners.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `xacc` 0.1.16, "Hardware-agnostic quantum programming framework" | [KNOWN] | https://pypi.org/pypi/xacc/json |
| Downloads | pypistats recent: 0 last day, 15 last week, 35 last month (2026-10-24). Not users: mirrors and CI inflate them | [KNOWN] counts; [INFERRED] meaning | https://pypistats.org/api/packages/xacc/recent |
| conda-forge / Spack | None (404) | [KNOWN] | github.com/conda-forge; spack-packages builtin |
| GitHub "used by" | "0 Repositories"; 176 stars, 89 forks | [KNOWN] | https://github.com/eclipse-xacc/xacc/network/dependents ; GitHub API |
| Plugins that build on it | TNQVM ("Tensor Network QPU Simulator for Eclipse XACC", ORNL-QCI org); QIR-EE optional XACC interface | [KNOWN] | github.com/ORNL-QCI/tnqvm; ORNL-QCI/qiree CMakeLists.txt |
| Citations | 2020 XACC paper (10.1088/2058-9565/ab6bf6): 143 citing works in OpenAlex; 96 have no ORNL-affiliated author; frequent institutions LBNL, Quantum Science Center, IBM, Argonne, LMU Munich, TU Munich, NVIDIA | [KNOWN] | api.openalex.org cites:W2988491525 |
| Use vs cite | 87 citing works mention XACC; the top ones are ORNL-led extensions (pulse-level control, optimal control, QIR toolchain, chemistry framework) | [KNOWN] list; use [INFERRED] | same |
| Successor | None stated in README, NOTICE or OSTI record | [UNKNOWN] | map.md link 163 |

Reasoning: high outside citation with low install signals and no recent commits suggests XACC is a well-known reference design in quantum-HPC that outsiders cite more than run, while ORNL and close partners extend it [INFERRED, medium confidence].
