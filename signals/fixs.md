<!-- history section (discovery pass) goes above -->

## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- It's small but speeding up a lot. 77 commits in 2023, 35 in 2024, 244 in 2025 and 886 so far in 2026. [KNOWN: git log] Read: the project is in a heavy build phase right now, heading toward a 1.0. [INFERRED, medium]
- The version tags back that up: alpha and beta tags for v0.9.0 both landed on 2026-10-12. [KNOWN]
- The DOE CODE record (code-110562, 2023-07-27) still points to an older GitHub home, Real-Sim-XIL/FIXS. [KNOWN: OSTI API] Read: the repo moved to the ORNL-Real-Sim account later. [INFERRED, high]
- Funding is DOE's Vehicle Technologies Office, under EERE's transportation side. [KNOWN: OSTI sponsor field] That matches its sister project Real-Twin. [KNOWN: signals/real-twin.md]
- One author has 53% of commits, out of 16 emails. [KNOWN]

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2023-07-26, last 2026-09-27. 1,242 commits on default branch | git | [KNOWN] |
| Commits per year | 77, 35, 244, 886 (2023 to 2026) | git log | [KNOWN] |
| Active authors per year | 5, 3, 9, 8. 16 emails. Top three 53%, 14%, 14% | git log | [KNOWN] |
| Tags | 9. Latest v0.9.0-alpha and -beta 2026-10-12 | git | [KNOWN] |
| Funding | code-110562: EERE Vehicle Technologies Office | OSTI API | [KNOWN] |
| Old repo link | github.com/Real-Sim-XIL/FIXS in DOE CODE | OSTI API | [KNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16): public registry, GitHub and OpenAlex reads; institution counts only, no individuals profiled. Downloads are not users.

**Outside vs inside:** FIXS is a young, actively developed ORNL co-simulation interface. Its only indexed citations (2) come from ORNL authors, and there's no package or dependent, so visible use is the ORNL team's own vehicle-in-the-loop work.

| Signal | Finding | Tag | Source |
|---|---|---|---|
| Registries | No `fixs` on PyPI, conda-forge or Spack (404) | [KNOWN] | registries |
| GitHub "used by" | "0 Repositories"; 19 stars, 4 forks, last push 2026-10-23 UTC | [KNOWN] | https://github.com/ORNL-Real-Sim/FIXS/network/dependents ; GitHub API |
| Citations | DOE CODE DOI 10.11578/dc.20230727.1 "Real-Sim Flexible Interface for X-in-the-loop Simulation (FIXS)": 2 citing works, both with an ORNL author | [KNOWN] | api.openalex.org |
| Namesakes | "FIXS X-in-the-loop" search hits on coronal loops and hysteresis loops are unrelated | [UNRELATED] | api.openalex.org |

Reasoning: inside-only use so far [INFERRED, medium confidence].
