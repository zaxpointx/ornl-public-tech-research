# Signals: data-workflow

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- It's a long-lived code with two lives. There was a first burst from 2012 to 2016, a quiet stretch from 2017 to 2020, then a bigger second life from 2021 on, peaking at 447 commits in 2022. 13 people were active in 2025, the most ever. [KNOWN: git log --all] Read: the neutron data pipeline got rebuilt around 2021 and 2022, along with its sister tools. [INFERRED, medium]
- It's the most-released tool in the set, with 107 tags. The latest is v3.12.0 (2026-10-19). [KNOWN]
- Besides unit tests it has a system-test workflow, so it's tested end to end on GitHub's hosted runners. No supercomputer target. The "hip" and "lsf" hits are all in binary images and slides. [KNOWN; UNRELATED for those hits]
- The docs include legacy design notes for the older data-cataloging system it grew from. [KNOWN: docs/legacy] I only looked at the file names.
- No OSTI software record found. Keyword hits for "data workflow" on OSTI are other labs' projects. [UNRELATED; funding UNKNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2012-08-15, last 2026-10-23. 1,893 commits on all branches, 1,872 on next | git | [KNOWN] |
| Commits per year | 78, 288, 163, 227, 121, 22, 29, 4, 18, 143, 447, 26, 144, 136, 47 (2012 to 2026) | git log --all | [KNOWN] |
| Active authors per year | 4, 3, 3, 4, 3, 1, 2, 1, 5, 11, 12, 5, 8, 13, 9. 39 emails. Top three 41%, 9%, 8% | git log | [KNOWN] |
| Tags | 107. Latest v3.12.0 2026-10-19 | git | [KNOWN] |
| CI | CI, system tests, publish and lockfile workflows on ubuntu-latest | .github/workflows | [KNOWN] |
| Funding | No match. OSTI "data workflow" hits (for example INL code-145281) are namesakes | OSTI API | [UNRELATED] |

## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users.

**Outside vs inside:** This is SNS facility plumbing: no package, no dependents, 6 stars and 3 forks, and no paper, so its users are the neutron facility's own data pipeline, which is what the inside says too.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Registries | No `data-workflow` on PyPI, conda-forge or Spack (404) | [KNOWN] | registries |
| GitHub "used by" | "0 Repositories"; 6 stars, 3 forks, last push 2026-10-23 UTC | [KNOWN] | https://github.com/neutrons/data_workflow/network/dependents ; GitHub API |
| Citations | No software paper found | [UNKNOWN] | api.openalex.org |

Reasoning: an internal facility service with active development and no outside adopters visible [INFERRED, medium confidence].
