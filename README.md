# ORNL Public Technology Research

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
![Sources: public only](https://img.shields.io/badge/sources-public%20only-blue)
![Status: ongoing](https://img.shields.io/badge/status-ongoing-green)

An independent, open-source intelligence (OSINT) study of the public software, tools, and datasets released by Oak Ridge National Laboratory (ORNL). Each project gets a plain-English brief that explains what it does, how its code is organized, and who uses it, with every claim tagged by how well it is supported. A connections map shows how the projects depend on and relate to each other, and signals files read public traces such as commit history and funding records.

> [!IMPORTANT]
> **Independent research. Not affiliated with, sponsored by, or endorsed by ORNL, UT-Battelle, LLC, or the U.S. Department of Energy.** Everything here comes from public sources (ornl.gov, osti.gov, energy.gov, public GitHub/GitLab repositories, public papers and docs). No logins, no restricted material, and no contact with lab staff. Project names belong to their owners. Findings can be wrong or out of date; see [Corrections](CONTRIBUTING.md).

## At a glance

| | |
|---|---|
| Projects in the catalog | 68 ([discovery/catalog.csv](discovery/catalog.csv)) |
| Project briefs | 45 passed both fact-check sweeps, more in progress ([INDEX.md](INDEX.md)) |
| Connections map | How the projects relate, every link tagged and sourced ([connections/map.md](connections/map.md)) |
| Signals files | 33 ([signals/](signals/)) |
| Deep dives | 1, Cyberwheel ([deep-dives/cyberwheel/](deep-dives/cyberwheel/)) |
| Research batches | 8 ([batches/](batches/)) |

Counts reflect the snapshot date in [CITATION.cff](CITATION.cff).

## Evidence tags

Every claim carries one tag.

| Tag | Meaning |
|---|---|
| `[KNOWN]` | Stated directly in a cited primary source |
| `[CORROBORATED]` | KNOWN and confirmed by a second independent source |
| `[INFERRED]` | Reasoned from sources but not stated outright; the reasoning is given |
| `[UNKNOWN]` | An open question we could not answer |
| `[UNRELATED]` | Checked and found not to be part of the project (prevents namesake mix-ups) |

Searches that came up empty are logged in [verification/not-found.md](verification/not-found.md). A failed search is bounded negative evidence, not proof of absence.

## Method in brief

1. **Discover** projects from public sources and keep a project in the catalog only if a primary source names ORNL as research org, copyright holder, repo owner, or contributing lab.
2. **Read** official docs and the public repo, and write a brief from a fixed template.
3. **Check, sweep 1:** re-verify each claim against the cited source and at least one other primary source.
4. **Check, sweep 2:** re-read every brief and map link, re-fetch load-bearing sources, look for disconfirming evidence, and fix overstatements.
5. **Connect** projects through dependency files, shared contributors, shared facilities, and funding.
6. **Summarize** each batch and record what is still unknown.

Full detail: [docs/methodology.md](docs/methodology.md) and the working rules in [RULES.md](RULES.md).

## Research-team operations

The repeatable team workflow is documented in [AGENTS.md](AGENTS.md) and [docs/research-team.md](docs/research-team.md). It defines role boundaries, batch size, evidence gates, deep-dive requirements, and the honest completion boundary. Run `python3 scripts/audit_atlas.py` before committing an atlas update.

## Highlights

- **Grid software is picking up.** ExaGO, a power grid optimization tool, was nearly idle in 2025 and has had a large rise in contributors in 2026. GridKit, another grid solver, shares its lead developer with a related solver library.
- **A broken handoff.** Zambeze was built to pass its records to Flowcept, another ORNL workflow tool. Current Flowcept no longer contains the piece Zambeze calls, so that integration likely no longer works.
- **Widely cited, quietly maintained.** The ExaTN quantum tensor library appears in many papers but has had no code changes since mid-2023.
- **Cyberwheel deep dive.** A full public reconstruction of ORNL's reinforcement-learning cyber defense simulator: timeline, system flow, source ledger, and an explicit list of what the public record cannot answer.

## Repository layout

```
INDEX.md                 start here: every project by domain, with status
GOAL.md                  what the research is for and what "done" looks like
RULES.md                 evidence and scope rules used by the research
discovery/catalog.csv    master list of projects
projects/                one plain-English brief per project
signals/                 public-trace readings (commit history, funding, usage)
connections/map.md       how projects relate, with a mermaid diagram
deep-dives/              full reconstructions of selected projects
verification/            fact-check log and searched-but-not-found ledger
batches/                 per-batch summaries
docs/                    methodology and reading order
```

## How to navigate

New here: read [INDEX.md](INDEX.md), then pick a brief in [projects/](projects/). Checking a claim: follow its tag to the cited URL, then look it up in [verification/log.md](verification/log.md). Looking for patterns: open [connections/map.md](connections/map.md). The suggested reading order is in [docs/reading-order.md](docs/reading-order.md).

## Privacy

This research is about projects, not people. Individual names, emails, and account handles are removed or replaced with role labels (for example "credited developer A"). Contributor statistics are reported only as counts and shares. Published paper citations are kept as references.

## Status

Ongoing. New batches are added as they are researched and verified. Briefs marked unverified or stub in the index have not finished both sweeps.

## Citation and license

Written research is licensed under [CC BY 4.0](LICENSE). To cite it, use [CITATION.cff](CITATION.cff) (GitHub shows a "Cite this repository" button). Quotes from third-party sources are short, attributed, and remain the property of their owners.

Maintained by Cayden Wilson ([ZaxPointX](https://github.com/zaxpointx)).
