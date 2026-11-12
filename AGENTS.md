# Public ORNL research: agent guide

This repository is the single home for the ORNL public research. On 2026-11-11 the former `ornl-atlas` repository was merged into [atlas/](atlas/README.md). Do new work here, not in the old checkout.

Before research or edits, read [RULES.md](RULES.md) and [GOAL.md](GOAL.md). They own the sourcing rules, public-information boundaries and intended outcomes.

## Focus: where deep effort goes
The owner's focus lanes are **cybersecurity, software engineering, AI and agents, and Linux/infrastructure**. [discovery/lanes.csv](discovery/lanes.csv) tags every catalog project with its lanes and one tier:
- **deep**: in lane, with public code that can be read and run. Spend research time here.
- **lead**: in lane, but thin public material or only one component is relevant. Research that component only.
- **pool**: outside the lanes. Keep it as context; don't extend it unless a reusable component turns up.

A deep dive is done when the project is understood, run, pushed to a failure boundary, and written up with sources. `atlas/labs/flowcept-failure-study/` is the model.

## Where to look
| Need | Start with |
|---|---|
| Which projects exist and their status | [discovery/catalog.csv](discovery/catalog.csv), [INDEX.md](INDEX.md) |
| Which ones matter for the focus lanes | [discovery/lanes.csv](discovery/lanes.csv) |
| How one project works | `projects/<id>.md`, then `signals/<id>.md` |
| Reusable engineering, with pinned code lines | [lessons/engineering-patterns.md](lessons/engineering-patterns.md) |
| How the lab operates (INTERSECT, facilities, job families) | [atlas/guide/](atlas/guide/README.md) |
| A JSON context packet for an agent | `python3 atlas/scripts/atlas_query.py --search <terms>` or `--node <id>` |
| Relationships between projects | [connections/map.md](connections/map.md), [docs/portfolio-map.json](docs/portfolio-map.json), `atlas/registry/edges.json` |
| Experiments that ran ORNL code | [atlas/labs/](atlas/labs/) |

Two registries exist for now: the catalog (projects) and `atlas/registry/` (sources, roles, facilities, typed edges). They overlap on a few projects and have not been reconciled. Treat the catalog as authoritative for project status and the atlas registry for the operating-model graph.

## Continue
The latest handoff is the end of [docs/portfolio-expansion-2026-11-10/verification.md](docs/portfolio-expansion-2026-11-10/verification.md). Batch 13 and the patterns guide are in [batches/batch-13.md](batches/batch-13.md); the merge is recorded in [atlas/README.md](atlas/README.md). Continue only the requested outcome. One agent owns a task at a time. If another agent's uncommitted files are present, leave them alone.

## Verify
- `python3 scripts/audit_atlas.py`: structural consistency, lanes coverage and local links.
- `python3 scripts/build_portfolio_map.py --check`: map freshness, when catalog inputs change.
- `python3 atlas/scripts/validate_registry.py` and `python3 -m unittest discover -s atlas/tests -p 'test_*.py'`: atlas registry and query tool.
- Review the scoped diff and run `git diff --check`. Keep the known/inferred/unknown distinctions and source boundaries.

No push, publication, deployment, private information, credentials, outside-system probing or real-person outreach without explicit authorization. Opening an upstream issue or pull request on an ORNL repository counts as outreach and needs the owner's OK each time. Update the existing handoff for a new outcome; no parallel tracker or automatic agent fleet.
