# Signals: gauntlet

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- It's a one-time code release, not a living project. There are only 6 commits, all between 2025-07-09 and 2025-07-18, from 2 people, with no tags and no CI. [KNOWN: git log --all] Read: code published at the end of a funded effort. [INFERRED, medium]
- The first commit date matches the DOE CODE record date exactly (code-157761, 2025-07-09). [KNOWN]
- Sponsors are unusual for ORNL software: FEMA and DOE's Federal Energy Management Program. [KNOWN: OSTI sponsor field] Read: the work was for federal facilities and emergency planning, not for science users. [INFERRED, low]
- It ships as a Docker Compose app, with no HPC target. [KNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | 6 commits, 2025-07-09 to 2025-07-18 | git | [KNOWN] |
| Authors | 2 emails, 83% and 17% | git log | [KNOWN] |
| Tags and CI | None | repo | [KNOWN] |
| Funding | code-157761 lists ORNL as research org, FEMA and FEMP as sponsors | OSTI API | [KNOWN] |
| Other OSTI "gauntlet" hits | Mixed sponsors (NNSA and others), not checked as the same project | OSTI API | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users.

**Outside vs inside:** Gauntlet's outside trace is the data it produces, not the code. The 2025 USA Structures morphology paper calls its features "a gauntlet feature set", and a 2024 building-height paper from the same area is cited mostly outside ORNL. The repo itself is small and quiet since 2025-07.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `gauntlet` 0.1.0 is an unrelated code-check tool ("Your Name" placeholder author); the repo's own pyproject name is `testpypi` | [UNRELATED] | https://pypi.org/pypi/gauntlet/json ; ORNL/gauntlet pyproject.toml |
| conda-forge / Spack | None (404) | [KNOWN] | registries |
| GitHub "used by" | "0 Repositories"; 12 stars, 2 forks, last push 2025-07-18 UTC | [KNOWN] | https://github.com/ORNL/gauntlet/network/dependents ; GitHub API |
| Citations | "Building morphologies of the USA structures database; a gauntlet feature set" (Scientific Data 2025, 10.1038/s41597-025-05925-6): 1 citing work, with ORNL author | [KNOWN] | api.openalex.org |
| Related paper | "Inferring building height from footprint morphology data" (Scientific Reports 2024, 10.1038/s41598-024-66467-2): 22 citing, 9 with ORNL author | [KNOWN] counts; [INFERRED] that it uses Gauntlet features | api.openalex.org |

Reasoning: outside users consume published building-feature data rather than run the tool [INFERRED, low confidence].
