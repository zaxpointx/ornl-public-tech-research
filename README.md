# ORNL Public Technology Research

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
![Sources: public only](https://img.shields.io/badge/sources-public%20only-blue)
![Status: ongoing](https://img.shields.io/badge/status-ongoing-green)

A plain-English map of the public software, tools, and datasets from Oak Ridge National Laboratory, built only from public sources.

This is an independent, open-source intelligence (OSINT) study of what Oak Ridge National Laboratory (ORNL) has released publicly. It is maintained by Cayden Wilson with an AI-assisted research workflow: Cayden sets the scope, reviews the writing, and makes the editorial decisions. Each project gets a plain-English brief that explains what it does, how its code is organized, and who uses it, with every claim tagged by how well it is supported. A connections map shows how the projects depend on and relate to each other, and signals files read public traces such as commit history and funding records.

> [!IMPORTANT]
> **Independent research. Not affiliated with, sponsored by, or endorsed by ORNL, UT-Battelle, LLC, or the U.S. Department of Energy.** Everything here comes from public sources (ornl.gov, osti.gov, energy.gov, public GitHub/GitLab repositories, public papers and docs). No logins, no restricted material, and no contact with lab staff. Project names belong to their owners. Findings can be wrong or out of date; see [Corrections](CONTRIBUTING.md).

## What this is—and is not

This is an evidence-bounded research atlas and book manuscript about ORNL-related public technology. It is useful for researchers, technical readers, and contributors who want a navigable starting point for public software and research artifacts.

It is not an official ORNL directory, an exhaustive inventory, a claim about private systems or staff, or a substitute for the upstream project's own documentation. Public repositories show published artifacts; they do not by themselves prove production deployment, institutional ownership, or complete internal architecture.

## Read this as a book

The repository is both a living research atlas and the working manuscript for a book-length study. Start with the public research guide, then use the atlas files as the evidence layer behind it.

1. [Public research guide](docs/public-research-guide.md): a growing plain-language, lab-wide orientation (first batch; gaps explicitly marked).
2. [Book Plan](docs/book-plan.md): canonical parts, chapters, reading paths, and completion criteria.
3. [Executive orientation](LAB-TREE.md): the lab map and the research scope.
4. [Project index](INDEX.md): the catalog of briefs and their evidence status.
5. [Deep dives](deep-dives/): selected case studies.
6. [Methods and evidence](docs/methodology.md): how claims are sourced, tagged, and checked.
7. [Research manifest](docs/research-manifest.md): the current snapshot and reproducibility boundary.
8. [Coverage matrix](docs/coverage-matrix.md): catalog-to-book completeness and the active queue.

The [reading order](docs/reading-order.md) links the same corpus for human readers and research assistants; the Book Plan is the canonical editorial structure.

## Choose your path

- **New here:** start with the [public research guide](docs/public-research-guide.md), then explore the [lab map](LAB-TREE.md) and [project index](INDEX.md).
- **Browse projects:** use the [Project Index](INDEX.md) and [coverage matrix](docs/coverage-matrix.md).
- **Read connected stories:** follow [INTERSECT additive manufacturing](docs/intersect-additive-story.md), the [SNS neutron data pipeline](deep-dives/sns-neutron-pipeline.md), [Cyberwheel](deep-dives/cyberwheel/synthesis.md), [autonomous science](docs/autonomous-science.md), or [isotopes and hot cells](docs/isotopes-and-hot-cells.md).
- **Facilities and relationships:** browse the [facilities, instruments and roles guide](docs/facilities-instruments-roles.md) and the selected [relationship index](docs/research-relationships.md).
- **Reuse the engineering:** [engineering patterns in ORNL's public code](lessons/engineering-patterns.md) turns design moves in 15 public repos into reusable patterns, each tied to pinned code lines, with a lookup table by what you are building.
- **Check the evidence:** read the [methodology](docs/methodology.md), [rules](RULES.md), and [verification ledger](verification/log.md).
- **Contribute or correct:** read [CONTRIBUTING.md](CONTRIBUTING.md) and use the appropriate issue template.

GitHub Actions dependencies are checked monthly through Dependabot; proposed updates still pass the repository audit before merging.

The full suggested order is in [docs/reading-order.md](docs/reading-order.md). Publication and reproducibility conventions are documented in [docs/publication-workflow.md](docs/publication-workflow.md).

## Status

Work in progress. Counts below are taken from the files in this snapshot.

| | |
|---|---|
| Projects in the catalog | 74 ([discovery/catalog.csv](discovery/catalog.csv)) |
| Project files | 72 (63 full briefs, 7 short briefs and 2 short OSTI-only drafts) |
| Project files checked in two sweeps | 72 |
| Briefs still to write | 2 OSTI-only stubs (Cincinnatus, CPAD), waiting on a public docs page |
| Deep dives finished | 6 |
| Signals files | 45 ([signals/](signals/)) |
| Research batches | 12 files covering batches 01 to 13; 07 and 08 share a file ([batches/](batches/)) |

The 74 catalog entries are not all complete briefs: 2 are OSTI-only stubs with no public docs page yet. The [coverage matrix](docs/coverage-matrix.md) explains that queue.

## Method

- **Evidence tags.** Every claim is tagged `[KNOWN]` (stated in a cited primary source), `[CORROBORATED]` (confirmed by a second independent source), `[INFERRED]` (reasoned from sources, with the reasoning given), `[UNKNOWN]` (an open question), or `[UNRELATED]` (checked and found not to be part of the project).
- **Two-pass fact check.** A brief is marked verified only after two separate sweeps: one re-checks each claim against its source and a second primary source, the next re-reads the whole brief, re-fetches key sources, and looks for evidence against it.
- **Corrections are logged.** Every check and fix is recorded in [verification/log.md](verification/log.md). Searches that found nothing are kept in [verification/not-found.md](verification/not-found.md).
- **Professional credit, not profiles.** Names may appear for a relevant professional role or authorship directly supported by an official public professional source; no personal details or outreach. Older files may use role labels only. See [RULES.md](RULES.md).
- **AI-assisted workflow.** The research is produced by a team of AI research assistants with separate roles (find, read, fact check, connect, organize), directed and reviewed by the maintainer. No claim is kept unless it traces to a public source. See [docs/roles.md](docs/roles.md).

The batch plan and review gates are in [docs/research-team.md](docs/research-team.md). Every update is checked with `python3 scripts/audit_atlas.py`, which also runs as a GitHub Actions check.

Full detail: [docs/methodology.md](docs/methodology.md) and the working rules in [RULES.md](RULES.md). New deep dives use [templates/project-case-study.md](templates/project-case-study.md).

## Publication status

This is a living edition, not a claim that the book is finished. The catalog is the source of truth for project coverage; the verification ledger is the source of truth for fact-check history; and the Book Plan tracks manuscript completeness. A future numbered edition should be cut only after the release checklist in [docs/publication-workflow.md](docs/publication-workflow.md) passes.

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
lessons/                 how the lab works, and engineering patterns in its code
verification/            fact-check log and searched-but-not-found ledger
batches/                 per-batch summaries
docs/                    methodology, roles, reading order
templates/               templates for briefs and deep dives, engineering checklist
scripts/audit_atlas.py   structure check, run on every push
```

Editorial control files:

```
docs/book-plan.md             canonical book architecture and chapter map
docs/publication-workflow.md  editioning, reproducibility, review, and release rules
docs/research-manifest.md     snapshot inventory and reproduction boundary
docs/coverage-matrix.md       catalog-to-book completeness and priority queue
templates/chapter-checklist.md required evidence and editorial checks for chapters
```

## Corrections

Found something wrong or overstated? Open an issue using the correction template. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation and license

Written research is licensed under [CC BY 4.0](LICENSE). To cite it, use [CITATION.cff](CITATION.cff). Quotes from third-party sources are short, attributed, and remain the property of their owners. Project names belong to their owners.

Maintained by Cayden Wilson ([ZaxPointX](https://github.com/zaxpointx)).


## Whole-portfolio reading map, 2026-11-10

The [portfolio map](docs/portfolio-map.md) links all current catalog entries (74 as of 2026-11-11) across ten research domains, with a [JSON evidence map](docs/portfolio-map.json) retaining the 33 selected relationship propositions and their limits. The [cross-domain research expansion](docs/portfolio-expansion-2026-11-10/README.md) adds technical studies of scientific streaming, quantum simulation, microscopy, biology, materials learning, building models, weather data, grid mathematics, and population uncertainty. Catalog coverage and deep research are reported separately; neither is a claim to cover everything ORNL has done.
