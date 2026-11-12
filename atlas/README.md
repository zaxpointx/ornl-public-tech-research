# ORNL Atlas (merged lab layer)

> **Merged 2026-11-11.** This folder was a separate repository, `ornl-atlas`. It is copied here unchanged in structure from its commit `f70741a` plus the uncommitted work present at 2026-11-11 21:59 local time (the Flowcept failure study and registry updates). Left out of the copy: a private personal context file, the old agent instruction files (the repository-root [AGENTS.md](../AGENTS.md) now governs), and one archived, mis-scoped planning document. Two private local paths were replaced and three raw web-page scrapes were trimmed to titles.
>
> **How it fits.** The rest of this repository is the project catalog, briefs, deep dives and patterns. This folder holds the **operating-model guide** (how INTERSECT, facilities, job families and teams connect), the **JSON registry** with verified, lead and blocked evidence states, the **agent query tool**, and the **labs**, where ORNL software is actually run. Run the commands below from inside this `atlas/` folder.

A public-source research atlas of Oak Ridge National Laboratory: serious projects, hidden connective tissue, and small experiments we can reproduce with Hermes and Codex.

This is not a dump of ORNL links. Each project records:

- what ORNL publicly says
- what the evidence implies
- why it matters
- what could be recreated locally
- confidence and source boundaries

## Research lanes

- autonomous science and agentic workflows
- computing and Codex/HPC
- robotics and machine vision
- quantum communications
- neutron imaging and scientific instruments
- advanced manufacturing
- biology and synthetic biology
- energy, nuclear batteries, climate, and grid resilience
- technology transfer and commercialization

## Evidence rules

1. Public sources only.
2. Separate direct claims from inference.
3. No claim is accepted from a search snippet alone.
4. Every project needs a source URL and an evidence note.
5. Classified or access-controlled work is out of scope.

## First questions

- What would a new ORNL employee learn in their first six months that the public site never states directly?
- Which capabilities appear repeatedly across projects before ORNL names them as a strategic direction?
- Which projects can be reduced to a local Hermes/Codex experiment?

## Atlas spine

- `guide/` — primary human-facing deep-research guide, source ledger, and research plan.
- `registry/` — source, project, facility, software, role, and relationship registries.
- `labs/cross-layer-pilot.md` — optional safe study track, subordinate to the research guide.
- `scripts/validate_registry.py` — offline registry and graph validation.

## Status

The atlas now has a second research layer. The current guide covers autonomous science, INTERSECT, cross-facility workflows, provenance, neutron workflows, facilities, job families, public software, quantum networking, isotope and nuclear-battery work, polymer-reuse biology, grid resilience, wildfire detection, AI security, technology transfer, and new public-source comparison records.

The registry now contains 76 source records, 19 project/capability records, 4 facility records, 13 software records, 6 role records, and 27 typed relationships. The original guide ledger has 57 entries plus twelve source-ID entries from the workflow software batch. Quantum, nuclear, polymer, grid, AI-security, and INTERSECT portfolio lanes now have direct-source dossiers; they still need deeper technical reports, repository inspection, and complete staff maps before the atlas can be called exhaustive. Run `python3 scripts/validate_registry.py` before promoting new relationships.


## Workflow software research and local experiment

The [workflow software dossier](guide/project-dossiers/workflow-software-and-local-reconstruction.md) examines pinned Flowcept, Zambeze, INTERSECT SDK, and DataFed artifacts, including an actual historical Zambeze–Flowcept hook and its version limitations. The [local workflow lab](labs/cross-layer-pilot/README.md) tests synthetic execution, bounded recovery, evidence gates, and provenance replay. It is Atlas-authored code, not an ORNL implementation.

The [Flowcept failure-provenance study](labs/flowcept-failure-study/README.md) is the first experiment that runs real ORNL software. It found that offline Flowcept 1.0.3 loses every record not yet dumped when a process is killed or gets SIGTERM. That's a documented design limit, with a manual `dump_buffer()` workaround. It also found that a workflow is marked FINISHED even when it raises, which looks like a real bug, and that Zambeze's Flowcept hook only works up to Flowcept v0.3.11. Draft upstream issues are included. One fix (the FINISHED-status bug) was later opened upstream as [ORNL/flowcept#357](https://github.com/ORNL/flowcept/pull/357) on 2026-11-11, per the lab README; the other drafts were not posted.

For Codex or Hermes, start with the [agent reading entry point](guide/agent-entrypoint.md). `python3 scripts/atlas_query.py --node project-workflow-software-reconstruction` exports a bounded public context packet. See the [batch verification and handoff](research/2026-11-10-workflow-systems/verification.md) before continuing.
