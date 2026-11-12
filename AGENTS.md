# Public ORNL research: agent guide

This repository is the canonical public research project. The separate ornl-atlas checkout is a local experiment; do not substitute it for this repo.

Before research or edits, read [RULES.md](RULES.md) and [GOAL.md](GOAL.md). They own the sourcing, public-information boundaries and intended outcomes. [INDEX.md](INDEX.md) and [docs/coverage-matrix.md](docs/coverage-matrix.md) describe coverage, not an automatic work queue.

## Continue
Read [docs/portfolio-expansion-2026-11-10/verification.md](docs/portfolio-expansion-2026-11-10/verification.md) for the latest broad-map result and its limits. That work is already written. As of 2026-11-11 it is committed on branch `claude/engineering-patterns-batch-13`, together with batch 13; do not redo it. The 2026-11-11 continuation (batch 13: five new briefs plus [lessons/engineering-patterns.md](lessons/engineering-patterns.md)) is recorded at the end of that same file and in [batches/batch-13.md](batches/batch-13.md). Continue only the requested outcome. When historical reasons are missing, retrieve the owner's original conversation instead of restarting research or copying the separate experiment.

## Verify
- `python3 scripts/audit_atlas.py`: structural consistency and local links.
- `python3 scripts/build_portfolio_map.py --check`: generated map freshness, when map inputs change.
- Review the scoped diff and run `git diff --check`. Keep known/inferred/unknown distinctions and source boundaries.

No push, publication, deployment, private information, credentials, outside-system probing or real-person outreach without explicit authorization. Update the existing verification handoff for a new outcome; no parallel tracker or automatic agent fleet.
