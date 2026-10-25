# Signals: post-processing-agent

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- This is one of the oldest codes in the neutron set. It started in 2014, nearly stopped from 2017 to 2019, then came back in 2023 with 101 commits and has been steady since. [KNOWN: git log --all] Read: the same revival as the other neutron data-pipeline tools around 2021 to 2024. [INFERRED, medium]
- The release pace is fast now. 26 tags, with five releases from v4.2.0 (2025-10) to v4.6.0 (2026-10). [KNOWN]
- It's team-maintained, with 20 emails and the top author at 25%. [KNOWN]
- It's packaged with conda and Docker and tested on GitHub's hosted runners, with no supercomputer target. [KNOWN] Where it runs is out of scope (rule 16).
- No OSTI record or sponsor field found. [UNKNOWN; logged in not-found.md]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2014-05-16, last 2026-10-21. 456 commits on all branches, 451 on main | git | [KNOWN] |
| Commits per year | 57, 35, 29, 4, 4, 3, 0, 19, 18, 101, 88, 67, 31 (2014 to 2026) | git log --all | [KNOWN] |
| Active authors per year | 2, 4, 3, 1, 3, 1, 0, 5, 3, 7, 6, 8, 6. 20 emails. Top three 25%, 17%, 17% | git log | [KNOWN] |
| Tags | 26. Latest v4.6.0 2026-10-16 | git | [KNOWN] |
| CI | Test-and-deploy and lockfile workflows on ubuntu-latest | .github/workflows | [KNOWN] |
| Funding | None found on OSTI | OSTI API | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users. Map link 104 (writes to ONCat).

**Outside vs inside:** Like live-data-server, this is SNS/HFIR facility plumbing: 0 stars, 4 forks, no package, no paper. Its visible user is the facility's own reduction pipeline.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Registries | No `post-processing-agent` on PyPI, conda-forge or Spack (404); PyPI `postprocessing` is an unrelated ML package | [KNOWN]; namesake [UNRELATED] | registries |
| GitHub "used by" | "0 Repositories"; 0 stars, 4 forks, last push 2026-10-21 UTC | [KNOWN] | https://github.com/neutrons/post_processing_agent/network/dependents ; GitHub API |
| Citations | No paper found | [UNKNOWN] | api.openalex.org |

Reasoning: facility-internal and actively maintained [INFERRED, medium confidence].
