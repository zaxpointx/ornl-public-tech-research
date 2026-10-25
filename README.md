# ORNL Public Technology Research

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
![Sources: public only](https://img.shields.io/badge/sources-public%20only-blue)
![Status: ongoing](https://img.shields.io/badge/status-ongoing-green)

A plain-English map of the public software, tools, and datasets from Oak Ridge National Laboratory, built only from public sources.

This is an independent, open-source intelligence (OSINT) study of what Oak Ridge National Laboratory (ORNL) has released publicly. Each project gets a plain-English brief that explains what it does, how its code is organized, and who uses it, with every claim tagged by how well it is supported. A connections map shows how the projects depend on and relate to each other, and signals files read public traces such as commit history and funding records.

> [!IMPORTANT]
> **Independent research. Not affiliated with, sponsored by, or endorsed by ORNL, UT-Battelle, LLC, or the U.S. Department of Energy.** Everything here comes from public sources (ornl.gov, osti.gov, energy.gov, public GitHub/GitLab repositories, public papers and docs). No logins, no restricted material, and no contact with lab staff. Project names belong to their owners. Findings can be wrong or out of date; see [Corrections](CONTRIBUTING.md).

## Start here

1. [LAB-TREE.md](LAB-TREE.md): how the lab is organized, and where each project sits in it.
2. Deep dives, the most complete work in the repo:
   - [Cyberwheel](deep-dives/cyberwheel/synthesis.md), a reinforcement-learning cyber defense simulator
   - [SNS neutron data pipeline](deep-dives/sns-neutron-pipeline.md), how neutron experiment data is reduced and analyzed
   - [OLCF test harness](deep-dives/olcf-test-harness.md), automated acceptance testing for supercomputers
3. [INDEX.md](INDEX.md): every project by domain, with a one-line summary and verification status.
4. [lessons/](lessons/): plain-English takeaways about how the lab works.

The full suggested order is in [docs/reading-order.md](docs/reading-order.md).

## Status

Work in progress. Counts below are taken from the files in this snapshot.

| | |
|---|---|
| Projects in the catalog | 66 ([discovery/catalog.csv](discovery/catalog.csv)) |
| Project briefs written | 48 (46 full briefs plus 2 short drafts from public software records) |
| Briefs that passed both fact-check sweeps | 48 |
| Briefs still to write | 18, in progress in batches of five |
| Deep dives finished | 3 |
| Signals files | 40 ([signals/](signals/)) |
| Research batches | 7 ([batches/](batches/)) |

Earlier versions of this README said 68 projects. The catalog has 66 unique entries, and 66 is the correct number.

## Method

- **Evidence tags.** Every claim is tagged `[KNOWN]` (stated in a cited primary source), `[CORROBORATED]` (confirmed by a second independent source), `[INFERRED]` (reasoned from sources, with the reasoning given), `[UNKNOWN]` (an open question), or `[UNRELATED]` (checked and found not to be part of the project).
- **Two-pass fact check.** A brief is marked verified only after two separate sweeps: one re-checks each claim against its source and a second primary source, the next re-reads the whole brief, re-fetches key sources, and looks for evidence against it.
- **Corrections are logged.** Every check and fix is recorded in [verification/log.md](verification/log.md). Searches that found nothing are kept in [verification/not-found.md](verification/not-found.md).
- **People by role only.** The subject is projects, not people. Individuals appear as role labels such as "credited developer A", and contributor data is shown only as counts.
- **AI-assisted workflow.** The research is produced by a team of AI research assistants with separate roles (find, read, fact check, connect, organize), directed and reviewed by the maintainer. No claim is kept unless it traces to a public source. See [docs/roles.md](docs/roles.md).

The batch plan and review gates are in [docs/research-team.md](docs/research-team.md). Every update is checked with `python3 scripts/audit_atlas.py`, which also runs as a GitHub Actions check.

Full detail: [docs/methodology.md](docs/methodology.md) and the working rules in [RULES.md](RULES.md). New deep dives use [templates/project-case-study.md](templates/project-case-study.md).

## Repository layout

```
README.md                this file
LAB-TREE.md              how ORNL is organized, with each project placed in it
INDEX.md                 every project by domain, with status
GOAL.md                  what the research is for and what "done" looks like
RULES.md                 evidence and scope rules
discovery/catalog.csv    master list of projects
projects/                one plain-English brief per project
deep-dives/              full walkthroughs of selected projects
connections/             how projects relate, with mermaid diagrams
signals/                 public-trace readings (commit history, funding, usage)
lessons/                 takeaways about how the lab works
verification/            fact-check log and searched-but-not-found ledger
batches/                 per-batch summaries
docs/                    methodology, roles, reading order
templates/               templates for briefs and deep dives, engineering checklist
scripts/audit_atlas.py   structure check, run on every push
```

## Corrections

Found something wrong or overstated? Open an issue using the correction template. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation and license

Written research is licensed under [CC BY 4.0](LICENSE). To cite it, use [CITATION.cff](CITATION.cff). Quotes from third-party sources are short, attributed, and remain the property of their owners. Project names belong to their owners.

Maintained by Cayden Wilson ([ZaxPointX](https://github.com/zaxpointx)).
