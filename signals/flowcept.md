
## History, build targets, funding (discovery pass) (accessed 2026-10-24)

### What the outside tells us that the inside doesn't
- The team is growing. Active commit authors went from 6 in 2024 to 13 in 2025, with 7 of those new. 2026 has 9 so far. [KNOWN: git log --all, author date] Read: the project is being staffed up, not just maintained. [INFERRED, medium]
- One maintainer still writes most of the code, 66% of commits. [KNOWN: git log] Read: a key-person risk. [INFERRED, medium]
- Frontier is the only named supercomputer with a ready-made setup, in `examples/olcf_frontier/`. CI runs only on ordinary GitHub machines. [KNOWN: repo tree, .github/workflows] Read: Frontier is the main HPC target, but it isn't tested there in public CI. [INFERRED, medium]
- Funding on OSTI is mostly ASCR, with LDRD and one BES materials record. [KNOWN: OSTI API, 12 records matching "flowcept"]
- A workflow named `mirror-to-gitlab.yml` shows there's a non-public mirror. That's out of scope (rule 16).

### Signal ledger
| Signal | Value | Source | Tag |
|---|---|---|---|
| History | First commit 2022-11-07, last 2026-08-12. 2,062 commits across all branches, 2,061 on the default branch | git log, git rev-list | [KNOWN] |
| Commits per year | 2022: 340, 2023: 251, 2024: 564, 2025: 550, 2026: 357 | git log --all, author date | [KNOWN] |
| Active / new authors per year | 2022: 4/4, 2023: 6/3, 2024: 6/2, 2025: 13/7, 2026: 9/5. 21 emails in total. Top three authors 66%, 15% and 12% | git log | [KNOWN] |
| Tags | v1.0.1 2026-07-10, v1.0.2 2026-07-13, v1.0.3 2026-07-20 (three patch releases in 10 days) | git for-each-ref | [KNOWN] |
| CI | 13 jobs on ubuntu-latest or ubuntu-22.04, covering checks, multiple databases, Kafka/RabbitMQ, LLM tests, containers and release-and-publish | .github/workflows | [KNOWN] |
| HPC keywords (files) | frontier 5, summit 2, slurm 5, cuda 6, rocm 7 | grep of working tree | [KNOWN]. The Summit hits are in docs and publications only [KNOWN] |
| Funding | ASCR in 9 of 12 OSTI hits, plus LDRD (2) and BES (1). LDRD project 11521 with Zambeze (OSTI 3025007) | OSTI API | [KNOWN] |
| Wayback | Only one capture found, nearest 2024-04-13 | archive.org availability API | [KNOWN], but only bounds the dates |
| Job postings | Not searched this round | n/a | [UNKNOWN] |

## Who actually uses it
Accessed 2026-10-24 (ET). Artifacts only (RULES 16); institution names from OpenAlex, no individuals profiled. Detail in connections/map.md link 115.

**Outside vs inside:** The inside describes provenance capture for AI and science workflows across facilities. Outside, Flowcept has the most PyPI download activity of the tools checked so far but no visible dependents; nearly all papers mentioning it are ORNL-authored, with one outside-only paper (a Brazilian university, 2026).

| Signal | Finding | Tag | Source |
|---|---|---|---|
| PyPI | `flowcept` 1.0.3, 136 versions | [KNOWN] | https://pypi.org/pypi/flowcept/json |
| Downloads | pypistats recent: 71 last day, 864 last week, 1453 last month (2026-10-24). Not users: CI and mirrors inflate them | [KNOWN] counts; [INFERRED] meaning | https://pypistats.org/api/packages/flowcept/recent |
| conda-forge / Spack | No feedstock; no py_flowcept package.py (404) | [KNOWN] | github.com/conda-forge; spack-packages builtin |
| GitHub "used by" | Lists ORNL/flowcept itself, two PyPI mirror repos and one experiment-utilities repo by a Flowcept contributor | [KNOWN] list; mirrors [UNRELATED] as users | https://github.com/ORNL/flowcept/network/dependents |
| Paired ORNL code | Zambeze repo references Flowcept (deployment/compose-flowcept.yml) | [KNOWN] | https://github.com/ORNL/zambeze |
| Citations | OpenAlex: 18 works match "flowcept", nearly all ORNL-authored (co-authors Argonne, U. Chicago, U. Wisconsin, U. Trento); one outside-only (Universidade Federal Fluminense, SBBD 2026) | [KNOWN] | api.openalex.org search=flowcept |

Reasoning: higher downloads than HydraGNN or DataFed but no dependents and in-house papers suggest use mostly by ORNL workflow teams and close collaborators, with automated installs possibly driving downloads [INFERRED, medium confidence].
