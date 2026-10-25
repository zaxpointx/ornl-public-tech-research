
## Who actually uses it (connections pass)
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users.

**Outside vs inside:** Mantid is the widest-used project in the batch: its 2014 paper has 1,807 citing works, about 61% (1,111) without an ORNL author, matching its multi-facility origin. It ships through its own conda channel, not PyPI or conda-forge.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `mantid` 0.0.1 is an unrelated issue tracker (nirix/mantid) | [UNRELATED] | https://pypi.org/pypi/mantid/json |
| conda | No conda-forge feedstock or Spack package (404); public anaconda.org/mantid channel pages for mantid and mantidworkbench exist | [KNOWN] | github.com/conda-forge; https://anaconda.org/mantid/mantid |
| GitHub | 249 stars, 141 forks, last push 2026-10-24 UTC; dependents page returned no count | [KNOWN]; dependents [UNKNOWN] | GitHub API; network/dependents |
| Citations | NIM A 2014 Mantid paper (10.1016/j.nima.2014.07.029): 1,807 citing works, 696 with an ORNL author | [KNOWN] | api.openalex.org |

Reasoning: heavy citation from many facilities means Mantid is shared infrastructure for neutron and muon science, not an ORNL-only tool [INFERRED, high confidence].
