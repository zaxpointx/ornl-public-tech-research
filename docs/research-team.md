# ORNL exploration workflow

Owner decision, 2026-11-11: prioritize discoveries that change what Cayden could build or learn. Fifty exceptional projects would be more useful than hundreds of summaries. This is a quality preference, not a quota. Exploration does not require a predefined personal project. Focus on cybersecurity, software engineering, AI/agents and Linux/infrastructure; investigate another field when it exposes a transferable component.

The maintained research files are shared memory. The [searchable library](research-library.md) is generated from them for human browsing and agent retrieval. A catalog entry, an inspected implementation and a reproduced result remain different kinds of evidence.

## Start a bounded round

1. Read [AGENTS.md](../AGENTS.md), [RULES.md](../RULES.md), [GOAL.md](../GOAL.md) and the latest section of the [canonical handoff](portfolio-expansion-2026-11-10/verification.md). Inspect the working tree and preserve other owners' changes.
2. Search existing guides, cards and labs before discovery. Use `python3 scripts/research_library.py search "buffer provenance"` or `python3 scripts/research_library.py project flowcept` from the repository root. Build the index first if needed. Read the returned artifacts and their evidence boundaries, rather than treating a search hit as a verified claim.
3. Choose one investigation question and a small set of candidates that can answer it. Append a round plan to the existing handoff using the [round template](../templates/research-round.md): question, selection rationale, file ownership, depth, cost/stop bound and completion checks. Do not create a parallel tracker.
4. Harvest applicable in-repo work before repeating installations or experiments. Earlier Claude history reports Cyberwheel experiments outside this repo; that report is an unverified lead until the artifacts are inspected with permission for work outside the named repo.

## Discover and select

Search public ORNL repositories and its software catalog, DOE CODE/OSTI records, official project pages, papers and documentation. Follow evidence of dependencies and downstream use. Record unsuccessful searches in the existing [not-found ledger](../verification/not-found.md). A metadata snapshot or search result supplies candidates; it does not establish ownership, implementation, license terms or runtime behavior.

For each serious candidate, explain:

- **Mechanism:** what unusual capability or design warrants attention?
- **Depth:** what public artifacts let us inspect the mechanism rather than repeat the description?
- **Transfer:** what could a builder learn, adapt or combine, even without an immediate use case?
- **Feasibility:** what would another hour of research or a small experiment resolve, and at what cost?

Select on these reasons, not popularity or a target number of new projects. Preserve a promising report-only security project as an artifact study when code is unavailable. Promote a candidate into the catalog only under RULES.md's ORNL attribution requirements; add its lane row and navigation together. Existing discovery scripts and snapshots owned by another task remain untouched until ownership is resolved.

## Choose the depth the artifacts support

| Depth | Deliverable | Boundary |
|---|---|---|
| Artifact study | Plain-language capability, primary-source ledger, missing artifacts and open questions | Describes what public material supports; implementation and execution stay unknown |
| Code reconstruction | Pinned repository/version, architecture and data flow, contracts, tests/CI/history, limitations and reusable mechanism | Distinguishes code observation from runtime behavior and inferred design intent |
| Experiment | Reconstruction plus reproducible environment, inputs, prediction, command, raw results and measured boundary | States exactly which version/configuration was run; synthetic tests do not establish operational deployment |

The investigator chooses depth and explains why. Start with the smallest experiment that resolves the question. Write the prediction before executing; afterward compare it with observations and record uncertainty. A confirmed design or an unsuccessful reproduction can teach something valuable. A bug is not a required outcome. Keep independently built adaptations separate from claims about ORNL's implementation.

## Team and ownership

Use one coordinator with up to two independent workers. Once their artifacts are ready, use a fresh referee for the load-bearing claims. Keep at most four agents active including the coordinator. A single agent may combine discovery, reading and connection work when that is simpler.

| Role | Owned output | Handoff |
|---|---|---|
| Coordinator | Round scope, assignments, shared index/catalog integration and final handoff | Assigns disjoint files, resolves conflicts and checks the finished result |
| Scout/reader | Candidate evidence, selection rationale, project reconstruction | Returns artifact paths, supported claims, unresolved questions and next action |
| Experimenter | Isolated local experiment, prediction and raw results | Returns exact commands, environment/version, outputs and limits |
| Referee | Independent source checks and corrections in the verification ledger | Re-fetches load-bearing sources and checks claimed results against raw evidence |

Only the coordinator edits shared catalog/index/relationship files during a round. Workers own separate artifacts; messages carry paths and blockers, not repeated research narratives. The referee does not certify its own original investigation. If independent review is unavailable, preserve the work with review pending rather than claim independent verification.

This is an invoked, bounded workflow, not an unattended fleet or scheduled automation. The owner's authorization permits this scoped research team. It does not authorize pushes, publication, deployment, upstream issues/PRs, real-person messaging, credentials, system probing or work outside the named repo. Use the configured model and tools; setup changes remain outside the research workflow.

## Integrate and verify

Turn reusable findings into structured cards using the [library contract](research-library.md). Each card connects the problem, mechanism, evidence, measured or untested limits, and possible adaptations back to maintained source artifacts. Keep observed facts separate from proposed uses. A search index does not upgrade an artifact's evidence status.

Before closing the round:

- Re-read every changed brief, card and relationship. Re-fetch load-bearing sources, seek disconfirming evidence, and log corrections in [verification/log.md](../verification/log.md), following the two sweeps in RULES.md.
- For experiments, verify the commands, pinned versions, raw output and stated limits. Confirm every completion claim says what was inspected, executed or only proposed.
- Integrate catalog, lanes, index and maps where affected. Rebuild the library and check it against the maintained records. Exercise a search and a project packet relevant to the round.
- Run the applicable checks in AGENTS.md, review the scoped diff and run `git diff --check`. Preserve unrelated work.
- Append the result, checks, remaining unknowns and one next bounded investigation to the same canonical handoff. End as `verified complete`, `blocked with evidence`, or `handed back for input`.

A round is complete when its question and declared artifacts pass these gates. The guide as a whole remains complete only relative to its declared public sources, scope and research date. Neither a count nor a well-written summary establishes exhaustive knowledge of ORNL.
