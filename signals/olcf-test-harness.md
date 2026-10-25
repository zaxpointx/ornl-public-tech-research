# Signals: olcf-test-harness

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- Activity rises and falls with new machines. There were 213 and 146 commits in 2016 and 2017, a quiet stretch from 2018 to 2021, then a pickup from 2022 and a peak of 203 in 2025, with 10 distinct author emails that year, which resolve to two people by commit name. [KNOWN: git log --all; corrected in the fact-check pass 2026-10-24] Read: the harness gets a big push whenever a new system is being accepted, and Frontier fits the 2022 rise. [INFERRED, low]
- The public example config folder has files for Frontier (several variants) and Summit, and the docs cover both Slurm and LSF, the job schedulers on Frontier and on Summit. [KNOWN: configs/olcf_examples file names, docs; corrected 2026-10-24, Summit file was missed] I stopped at the file names and didn't read further into system details (rule 16).
- Releases have sped up. Only v2.1 (2021) existed before 2025, then v3.0, v3.1 and v3.2 came out within 18 months. [KNOWN] DOE CODE code-153320 is dated 2025-07-28, the same day as v3.1. [KNOWN]
- ASCR, the Office of Science's computing program, is the funder on 3 of 4 OSTI hits. [KNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2015-03-10, last 2026-10-16. 1,058 commits on all branches, 1,055 on devel | git | [KNOWN] |
| Commits per year | 21, 213, 146, 6, 17, 37, 29, 121, 105, 81, 203, 79 (2015 to 2026) | git log --all | [KNOWN] |
| Active authors per year | 2, 6, 6, 3, 4, 4, 7, 6, 8, 3, 10, 6. 31 emails. Top three 39%, 16%, 12% | git log | [KNOWN] |
| Tags | v2.1 2021-02-24, v3.0 2025-03-31, v3.1 2025-07-28, v3.2 2026-09-10 | git | [KNOWN] |
| CI | Docs, lint and test workflows on ubuntu runners | .github/workflows | [KNOWN] |
| Funding | code-153320 lists ORNL as research org and Office of Science as sponsor. ASCR on 3 of 4 hits | OSTI API | [KNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users.

**Outside vs inside:** The harness is OLCF's own acceptance-testing tool. Its outside trace is a DOE CODE record and OLCF acceptance-testing papers (Frontier), almost all with ORNL authors, so its users are the facility and its vendors' test teams.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Registries | None on PyPI, conda-forge or Spack (404) | [KNOWN] | registries |
| GitHub | 14 stars, 10 forks, last push 2026-10-16 UTC; dependents page gave no count | [KNOWN]; dependents [UNKNOWN] | GitHub API |
| Citations | DOE CODE "OLCF Test Harness" (10.11578/dc.20250328.1): 2 citing works, 1 with an ORNL author. Related ORNL papers: "A Step Towards the Final Frontier: Lessons Learned from Acceptance Testing..." (10.1002/cpe.7914) | [KNOWN] | api.openalex.org |

Reasoning: a facility tool whose forks likely come from other HPC centers or vendors, but no fork owner was profiled [INFERRED, low confidence].
