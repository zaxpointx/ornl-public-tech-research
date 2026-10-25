
## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- The project is mature and slowing down. Commits per year went 1,214 (2018), 289 (2021), 83 (2024), 44 (2025), and 12 so far in 2026. Releases still come yearly. [KNOWN: git log, tags] Read: a stable library in maintenance mode, not abandoned. [INFERRED, high]
- One author made 68% of all commits. [KNOWN] That matches the single-person copyright line the reading pass found. [INFERRED, medium]
- CI covers macOS, Ubuntu and Windows builds, but there's no GPU runner. The GPU backends (cuda in 46 files, hip in 29, rocm in 17, sycl in 12) are built but not tested in public CI. [KNOWN: workflows, grep; INFERRED: not tested] No named supercomputer appears. [KNOWN]
- DOE CODE code-6305 dates the software to 2013-09-19, about four years before the first GitHub commit (2017-10-16). [KNOWN] Read: there's earlier history outside this repo. [INFERRED, high]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2017-10-16, last 2026-10-19. 3,355 commits across all branches, 3,351 on default | git | [KNOWN] |
| Commits per year | 2017: 19, 2018: 1,214, 2019: 1,155, 2020: 309, 2021: 289, 2022: 117, 2023: 113, 2024: 83, 2025: 44, 2026: 12 | git log --all | [KNOWN] |
| Active authors per year | 2, 8, 7, 5, 7, 3, 2, 4, 5, 3 (2017 to 2026). 15 emails in total. Top authors 68% and 20% | git log | [KNOWN] |
| Tags | v8.0 2023-10-11, v8.1 2024-10-21, v8.2 2025-12-09 | git | [KNOWN] |
| Funding | code-6305 lists USDOE generically. A keyword search for "TASMANIAN" on OSTI picks up many unrelated Tasmania records, so sponsor counts from it aren't usable | OSTI API | [KNOWN] for code-6305. The program is [UNKNOWN] |
| Wayback | Nearest captures 2018-06-17, 2022-02-17 and 2026-05-12 | availability API | [KNOWN], but only bounds the dates |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16). Detail in connections/map.md links 131-135.

**Outside vs inside:** The inside offers sparse grids and DREAM sampling for uncertainty quantification. Outside, TASMANIAN is the best-packaged ORNL tool checked so far: a Spack package that the xSDK bundle references, plus PyPI. That points to reach through DOE HPC software stacks rather than through GitHub dependents (0).

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Spack | `tasmanian` package.py exists (homepage ornl.github.io/TASMANIAN, versions to 8.1) | [KNOWN] | spack-packages builtin tasmanian |
| Spack dependents | xsdk package.py references tasmanian | [KNOWN] | spack-packages builtin xsdk |
| PyPI | `Tasmanian` 8.2; pypistats recent: 6 last day, 44 last week, 174 last month (2026-10-24; not users, CI and mirrors inflate) | [KNOWN] counts; [INFERRED] meaning | https://pypi.org/pypi/Tasmanian/json ; https://pypistats.org/api/packages/tasmanian/recent |
| conda-forge | No feedstock (404) | [KNOWN] | github.com/conda-forge |
| GitHub "used by" | "0 Repositories", "0 Packages" | [KNOWN] | https://github.com/ORNL/TASMANIAN/network/dependents |
| Citations | OpenAlex keyword search ("TASMANIAN sparse grid") returns 888 noisy hits, not usable as a count | [UNKNOWN] | api.openalex.org |
| Not linked | Xolotl's UQ uses Sandia's UQTk, not TASMANIAN | [UNRELATED] | map.md link 139 |

Reasoning: Spack/xSDK inclusion means it is installed as part of DOE HPC stacks, so real use may be wider than GitHub signals show, but who uses it cannot be counted from public traces [INFERRED, medium confidence].
