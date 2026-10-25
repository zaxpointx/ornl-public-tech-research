# Signals: datafed

## History, build targets, funding (discovery pass) (accessed 2026-10-24)
Public artifacts only (RULES 15-16). Contributor data is counts only. Source: a fresh clone of https://github.com/ORNL/DataFed plus the OSTI API, unless another source is given.

### What the outside tells us that the inside doesn't
- **A near-stall followed by a big revival.** Commits per year: 2018 528, 2019 496, 2020 704, 2021 472, 2022 58, 2023 504, 2024 1,406, 2025 1,600. 2024 brought 11 new authors (17 active, against 4-6 in 2018-2022). [KNOWN: git log, counts only] That pattern suggests a new round of funding or staffing around 2023-24. [INFERRED, medium] The README doesn't mention it.
- **A four-month pause in 2026.** There were no commits between 2026-04-29 and September 2026. Work resumed with v5.1.3 on 2026-09-22. [KNOWN: git log, tags] The cause is UNKNOWN. A funding-cycle gap is possible but unproven. [INFERRED, low]
- **A non-public pipeline exists and is out of scope.** The public GitHub Actions only cover formatting, linting, docs and unit tests. [KNOWN: .github/workflows/] The repo's `.gitlab-ci.yml` and the `DAPS-####` ticket IDs in commit subjects show a non-public pipeline exists. [KNOWN] Anything beyond that is out of scope (rule 16).
- **The owning org unit is now traceable.** The catalog has the org unit as INFERRED (OLCF/CCS). An ORNL technical memo lists DataFed RSE authors under the Computer Science and Mathematics Division and the National Center for Computational Sciences. [KNOWN: https://info.ornl.gov/sites/publications/Files/Pub166131.pdf, ORNL/TM-166131, Sept 2021] A current ornl.gov staff page places DataFed work in the "Data Lifecycles and Scalable Workflows Group". [KNOWN: https://www.ornl.gov/staff/joshua-s-brown/, used only for the group name] The 2026 EcoKMER report lists ORNL's OLCF as a research org. [KNOWN: osti.gov/biblio/3412938] Suggested catalog update: org unit "NCCS/OLCF with CSMD [KNOWN: TM-166131, OSTI 3412938]".
- **It's data-movement infrastructure, not compute.** No GPU or supercomputer build target appears. "globus" is in 159 files at HEAD, CADES in 16, OLCF in 19. [KNOWN: git grep counts] It targets facility storage and transfer (Globus), not accelerators. [INFERRED, high]

### Signal ledger
| Signal | What it suggests | Tag, source | Confidence |
|---|---|---|---|
| 6,202 commits on all branches (3,713 on default), 236 remote branches, first commit 2017-11-13 | Long-lived, branch-heavy team development | [KNOWN: git] | high |
| 36 distinct authors in total. 9 use ornl.gov addresses, one uses a university address, the rest are personal or noreply | Mostly in-house, with a few outside or student contributors | [KNOWN: git, counts only] | medium |
| Top author 34% of commits, top three 73% | Concentrated core team | [KNOWN] | medium |
| Releases (tag commit dates): v4.0.0 2025-12-07, v5.0.0 2026-02-25 (GitHub release objects published 2025-12-09 and 2026-03-02), v5.1.0-5.1.2 March-April 2026, v5.1.3 2026-09-22 | Two major versions in three months, then a maintenance release | [KNOWN: git tags] | high |
| Sponsors: ASCR (OSTI 1820762 FY2021 RSE report; 1649470 2019 paper); "USDOE" only (code-48776); BER + ASCR on EcoKMER (3412938, PNNL + ORNL OLCF) | Core funding from ASCR. Outside application funding from BER | [KNOWN: OSTI API] | high |
| Job search by project name found no DataFed posting | No public hiring signal | [KNOWN: empty search, logged] | low |
| Wayback: repo page closest captures 2020-12-05, 2022-08-12, 2023-12-03, 2025-02-08. Docs site ornl.github.io/DataFed 2020-12-05, 2024-04-21, 2025-06-18 | Public docs existed by late 2020. Captures are bounds only | [KNOWN: archive.org availability API] | low |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only; institution names from OpenAlex, no individuals profiled. DataFed's servers were not probed (RULES 16).

**Outside vs inside:** The inside says DataFed serves teams doing cross-facility experiments, simulation and analysis. Outside, its Python client is on PyPI with modest downloads and no visible dependents; papers that mention it are mostly ORNL-authored, with a few outside reviews or cross-facility workflow papers (LBNL, Argonne, NERSC) and one 2026 multi-lab application (EcoKMER).

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `datafed` client exists, latest 5.1.0, 24 releases, home page github.com/ORNL/DataFed | [KNOWN] | https://pypi.org/pypi/datafed/json |
| Downloads | pypistats "recent": 3 last day, 25 last week, 43 last month (as of 2026-10-24). Not user counts: mirrors and CI inflate them | [KNOWN] counts; [INFERRED] meaning | https://pypistats.org/api/packages/datafed/recent |
| conda-forge | No `datafed-feedstock` (404) | [KNOWN] | https://github.com/conda-forge/datafed-feedstock |
| Spack | No `datafed` or `py_datafed` package.py (404) | [KNOWN] | github.com/spack/spack-packages builtin |
| GitHub "used by" | Dependents page reads "0 Repositories" | [KNOWN] | https://github.com/ORNL/DataFed/network/dependents |
| GitHub activity | 27 stars, 14 forks, 569 open issues+PRs, pushed 2026-10-23 | [KNOWN] | GitHub API repos/ORNL/DataFed |
| Code search `import datafed` | Not reachable without login | [UNKNOWN] | logged in not-found.md |
| Citations | CSCI 2019 paper "DataFed: Towards Reproducible Research via Federated Data Management" (10.1109/CSCI49370.2019.00245): 22 citing (OpenAlex); 12 of them match "datafed" | [KNOWN] | api.openalex.org cites:W3015715449 |
| Actual use | EcoKMER (OSTI report, DOI 10.2172/3412938, 2026), title "...metagenomic exploration using DataFed", ORNL with PNNL, SUNY, CU Denver | [KNOWN] (title states use) | OpenAlex |
| Mentions only | Superfacility (LBNL, 2020), cross-facility workflows (ANL/LBNL/NERSC/OLCF, 2021), FAIR health-data review (Aalborg, 2023), scattering-ML review (Tübingen, 2023) | [INFERRED] cite/mention, not use (titles/abstract matches only) | OpenAlex |

Reasoning: an actively developed service with a PyPI client but tiny download numbers and no dependents suggests a facility-run service that users reach through the portal/CLI rather than build into code [INFERRED, medium confidence]. Visible users so far: ORNL projects plus one multi-lab bio application; claimed cross-facility audience is only partly visible from outside [INFERRED].


## Sweep notes (fact-check pass, 2026-10-24)
- Re-fetched and verified: ORNL/TM-166131 PDF (title page lists Computer Science and Mathematics Division and National Center for Computational Sciences), the ornl.gov staff page (group name only: "Data Lifecycles and Scalable Workflows Group"), OSTI 3412938 (PNNL + ORNL OLCF; BER + ASCR), 1820762 (ASCR), code-48776 ("USDOE"), tags v5.1.0 to v5.1.3, PyPI 5.1.0 with 24 releases, `.gitlab-ci.yml` present.
- Pipeline bullet: the discovery-pass trimmed version matches the editorial decision. Nothing about hosting is recorded.
- Corrected: release dates are now labeled as tag commit dates, with the release publish dates added.
- The catalog org_unit "NCCS/OLCF with CSMD" is supported by TM-166131 plus OSTI 3412938. Verified.
- Not re-run: git commit and author counts and grep counts (the discovery-pass clone). Taken as reported.
