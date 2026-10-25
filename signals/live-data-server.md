# Signals: live-data-server

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- It was dormant for years and then revived. 23 commits in 2016, nothing from 2017 to 2021, then 51 in 2022 and a peak of 118 in 2024 with 8 active authors. [KNOWN: git log --all] Read: the neutron software group took it back over and modernized it. [INFERRED, medium]
- It's a team-maintained code, with nobody above 21% of commits across 15 emails. [KNOWN]
- It was released carefully: 17 tags, including several release candidates before v1.5.0 in 2026-01. [KNOWN]
- It's a small web service, packaged with Docker and conda, tested on GitHub's hosted runners. No supercomputer target. [KNOWN] I only looked at the repo, nothing about where it's deployed (rule 16).
- No OSTI record or sponsor field found. [UNKNOWN; logged in not-found.md]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2016-05-27, last 2026-10-21. 268 commits on all branches, 261 on next | git | [KNOWN] |
| Commits per year | 23 (2016), 0 (2017 to 2021), 51, 1, 118, 34, 41 (2022 to 2026) | git log --all | [KNOWN] |
| Active authors per year | 2 (2016), 4, 1, 8, 6, 6 (2022 to 2026). 15 emails. Top three 21%, 16%, 16% | git log | [KNOWN] |
| Tags | 17. Latest v1.5.0 2026-01-28 | git | [KNOWN] |
| CI | Unit tests, publish and lockfile updates on ubuntu-latest | .github/workflows | [KNOWN] |
| Funding | None found on OSTI | OSTI API | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users.

**Outside vs inside:** An internal SNS/HFIR service with 0 stars, 1 fork, no package and no paper; the only users visible are the facility's own systems.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Registries | No `live-data-server` or `live_data_server` on PyPI; none on conda-forge or Spack (404) | [KNOWN] | registries |
| GitHub "used by" | "0 Repositories"; 0 stars, 1 fork, last push 2026-10-21 UTC | [KNOWN] | https://github.com/neutrons/live_data_server/network/dependents ; GitHub API |
| Citations | No paper found | [UNKNOWN] | api.openalex.org |

Reasoning: facility-internal infrastructure, actively maintained [INFERRED, medium confidence].
