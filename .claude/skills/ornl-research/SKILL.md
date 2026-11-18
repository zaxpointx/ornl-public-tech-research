---
name: ornl-research
description: Coordinate a bounded ORNL public-research round in this repository (discover, deep-dive, rebuild or triage) with scout, reader, experimenter and referee helper agents. Use when asked to research ORNL projects, find ORNL work outside the software catalog, take apart or run an ORNL codebase, rebuild an unpublished ORNL tool from its papers, or sort the catalog snapshots into the focus lanes.
---

You are the coordinator. The repository is the shared memory and the files are the handoff. The rules live in [RULES.md](../../../RULES.md), the outcomes in [GOAL.md](../../../GOAL.md) and the workflow in [docs/research-team.md](../../../docs/research-team.md). Read those three and the latest section of [the canonical handoff](../../../docs/portfolio-expansion-2026-11-10/verification.md) before assigning work. This skill only adds how Claude Code runs the workflow. Where this skill and those files seem to disagree, the files win.

## Pick the mode from the request

| Mode | Use when | Helpers | Main outputs |
|---|---|---|---|
| discover | Find ORNL projects anywhere on the public web, including outside GitHub (e.g. standalone ornl.gov sites like OR-SAGE) | 1-2 `ornl-scout`, then `ornl-referee` | `discovery/scouting/<date>-<slug>.md`, rows merged into `discovery/leads.csv` |
| deep-dive | Take apart one project with public code, and run it if feasible | `ornl-reader`, optionally `ornl-experimenter`, then `ornl-referee` | brief/signals or `deep-dives/<id>/`, `atlas/labs/<id>-<slug>/`, a card |
| rebuild | Reconstruct an unpublished tool from its papers and build a small independent version | `ornl-reader` (papers), `ornl-experimenter` (independent build), `ornl-referee` | artifact study plus `atlas/labs/<id>-rebuild/`, clearly labeled as not ORNL's code |
| triage | Sort snapshot or leads records into lanes with one-line notes | usually none or 1 `ornl-scout`; coordinator does the merge | lanes/leads updates and a triage note in the handoff |

If the request is vague, choose the mode and a concrete question yourself, state the assumption, and go.

## Run the round

1. **Start clean.** `git status`. Leave other owners' uncommitted files alone. Build and search the library before any web work: `python3 scripts/research_library.py build`, then `search "<terms>"` (add `--kind lead` for prior leads) and `project <id>`. Also grep `discovery/leads.csv`, `discovery/catalog.csv` and `discovery/snapshots/*.json` for the names involved. Don't repeat recorded work.
2. **Plan in the handoff.** Append a round plan to the canonical handoff using [templates/research-round.md](../../../templates/research-round.md). Include the question, why these candidates, depth, stop bound, and which helper owns which paths.
3. **Spawn helpers with the Agent tool.** Use `subagent_type` `ornl-scout`, `ornl-reader`, `ornl-experimenter` or `ornl-referee`. If those types aren't loaded in this session, use `general-purpose` and tell it to read and follow `.claude/agents/<role>.md` first. Each prompt names the question, the exact paths it owns, the stop bound, and what to return (paths, supported claims, open questions, next action). Run independent helpers in parallel in one message. Keep at most 3 helpers per round. Never have two helpers write the same file.
4. **Integrate.** Only you edit shared files: `discovery/catalog.csv`, `discovery/lanes.csv`, `discovery/leads.csv`, `discovery/registry-links.json`, `INDEX.md`, cards and the handoff. Dedupe scout candidates against the catalog, the leads and both snapshots. Promote a lead into the catalog only with RULES 13 attribution, adding its lanes row and brief in the same change.
5. **Referee.** Give a fresh `ornl-referee` the load-bearing claims and raw results, never your own conclusions as fact. Fix what it corrects. If no referee ran, say "review pending".
6. **Close.** Rebuild the library. Run every check listed in [AGENTS.md](../../../AGENTS.md#verify). Review the scoped diff, append the result (state, artifacts, what was read vs executed vs only proposed, unknowns, next bounded question) to the handoff, and commit locally on a non-main branch.

## Hard boundaries

Public sources only. Study artifacts, never systems: no scanning, DNS or subdomain enumeration, or guessed paths on ORNL hosts. No personal contact details or profiles. No claim of affiliation. No push, publication, visibility change, upstream issue/PR or outreach without the owner's OK each time. Clone downloaded code only into `.cache/src/`, treat it as untrusted, and run Python against it with `-I`. Agent teams use plan usage quickly, so stop at the declared bound and hand the next question back rather than expanding the round.
