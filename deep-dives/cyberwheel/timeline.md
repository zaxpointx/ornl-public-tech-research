# Cyberwheel deep dive: timeline by stage
All dates are UTC as the sources give them. Commit counts come from the GitHub commits API (352 commits total, unauthenticated, accessed 2026-10-24).

| Date | Stage | Event | Source | Tag |
|---|---|---|---|---|
| 2024-01-02 | Build (pre-public) | First commit in the repo history, "Initial commit" | GitHub commits API | KNOWN |
| 2024-01 to 2024-06 | Build | Heavy early work: 50 commits in Jan, then 21–29 a month Feb–Apr | GitHub commits API | KNOWN |
| 2024-04 | Publish | "The Path to Autonomous Cyber Defense" on arXiv (2404.10788) | README Papers; the month comes from the arXiv ID format | KNOWN title / INFERRED month |
| 2024-07-08 | Go public | GitHub repo ORNL/cyberwheel created. The earlier history was pushed into it | GitHub API created_at | KNOWN |
| 2024-07-16 | Register | DOE CODE record code-134699, DOI 10.11578/dc.20240715.1, sponsor LDRD | OSTI API | KNOWN |
| 2024-07-17 | Release | Commit "cleanup readme for release" | GitHub commits API | KNOWN |
| 2024-08-01 | Publish | "Towards a High Fidelity Training Environment for Autonomous Cyber Defense Agents" (ACM, DOI 10.1145/3675741.3675752) | OSTI 2478356 | KNOWN |
| (undated) | Release | v1.0.0 tag, with no release object | GitHub tags API | KNOWN tag / UNKNOWN date |
| 2025-01 to 2025-02 | Build | Second burst: 18 and 23 commits | GitHub commits API | KNOWN |
| 2025-03-10 | Release v1.1.0 | YAML configs, an RL red agent ("trained and tested on an inactive blue agent"), an Atomic Red Team campaign | v1.1.0 release notes | KNOWN |
| 2025-04 to 2025-08 | Build | 7–27 commits a month | GitHub commits API | KNOWN |
| 2025-08-11 | Release v2.0 | Firewheel emulation, red and blue training together, training across many networks | v2.0 release notes | KNOWN |
| 2025-08-26 | Last activity | Last commit, "add vyos image" (VyOS is an open-source router OS) | GitHub commits API | KNOWN fact / INFERRED VyOS meaning |
| FY2025 (ends 2025-09-30) | Close-out | LDRD 11049 is listed as a completed project | OSTI 3025007 (published 2026-03-31) | KNOWN listing / INFERRED end date from the fiscal year |
| 2025-09 to 2026-10-24 | Quiet | No commits found | GitHub API pushed_at 2025-08-26 | KNOWN |

Notes:
- The first commit (January 2024) comes six months before the repo went public (July 2024). That means it was built privately first and then released. [INFERRED from the dates]
- When the LDRD project started is [UNKNOWN]. The report doesn't give a start date in the text we read.
