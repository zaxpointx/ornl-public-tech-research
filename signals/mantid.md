
## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- Mantid is huge and truly shared between labs. There are 153,918 commits on the main branch since 2007 and 386 author emails, and no single author has more than 4%. 70 to 100 people were active every year from 2016 to 2025. [KNOWN: git log] Read: a community codebase, not one lab's project. [INFERRED, high]
- Oak Ridge's share has gone up and down. Commits from ornl.gov addresses were 48 to 63% in 2010 and 2011, when the SNS was ramping up, fell to around 10 to 15% later, and have been 18 to 27% since 2023. [KNOWN: author email domains, counted in aggregate only] This is a lower bound, since many people commit from personal or GitHub addresses. [INFERRED]
- Commits peaked at 16,484 in 2016 and are down to 2,399 in 2025. Release tags, though, now come out every few days (latest v6.16 builds, October 2026). [KNOWN] Read: a mature code that's maintained with automated nightly releases. [INFERRED, medium]
- Funding on OSTI points to the Office of Science's Basic Energy Sciences (BES) program, which runs the neutron user facilities, plus one NSF paper. [KNOWN: OSTI sponsor fields, small sample]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2007-04-04, last 2026-10-23. 153,918 commits on main | git | [KNOWN] |
| Commits per year (peak) | 16,484 in 2016. 2,399 in 2025, 1,707 so far in 2026 | git log | [KNOWN] |
| Active authors per year | 8 (2007), up to 101 (2019), 76 (2025). 386 emails. Top 4% | git log | [KNOWN] |
| ornl.gov commit share | 63% (2011), 9% (2019), 27% (2025) | email domains, aggregate | [KNOWN], lower bound |
| Tags | 195. Latest v6.16.20261021.1513 | git | [KNOWN] |
| Funding | BES on OSTI hits for ORNL Mantid papers, one NSF | OSTI API | [KNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users.

**Outside vs inside:** Mantid is the widest-used project in the batch: its 2014 paper has 1,807 citing works, about 61% (1,111) without an ORNL author, matching its multi-facility origin. It ships through its own conda channel, not PyPI or conda-forge.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `mantid` 0.0.1 is an unrelated issue tracker (nirix/mantid) | [UNRELATED] | https://pypi.org/pypi/mantid/json |
| conda | No conda-forge feedstock or Spack package (404); public anaconda.org/mantid channel pages for mantid and mantidworkbench exist | [KNOWN] | github.com/conda-forge; https://anaconda.org/mantid/mantid |
| GitHub | 249 stars, 141 forks, last push 2026-10-24 UTC; dependents page returned no count | [KNOWN]; dependents [UNKNOWN] | GitHub API; network/dependents |
| Citations | NIM A 2014 Mantid paper (10.1016/j.nima.2014.07.029): 1,807 citing works, 696 with an ORNL author | [KNOWN] | api.openalex.org |

Reasoning: heavy citation from many facilities means Mantid is shared infrastructure for neutron and muon science, not an ORNL-only tool [INFERRED, high confidence].
