# Search and build from the research

The library connects readable guides, structured findings and an offline search database. Maintained files in Git are authoritative. SQLite is a disposable index, built with Python's standard library; it has no server, credentials, model calls or new dependencies.

The owner's focus is exploration: discover capabilities and mechanisms that suggest things worth building. A few exceptional investigations matter more than a large inventory. The [research workflow](research-team.md) explains selection, experiments and independent verification. In Codex, invoke `$ornl-research` from this repo, or ask it to run an ORNL exploration round. Claude Code reads the same workflow through the root agent instructions.

## Read and explore

- [Engineering patterns](../lessons/engineering-patterns.md): reusable mechanisms with pinned code and limitations.
- [Project index](../INDEX.md): project explanations and the difference between briefs and stubs.
- [Focus lanes](../discovery/lanes.csv): editorial priorities, not completed research depth.
- [Recorded Flowcept experiment](../atlas/labs/flowcept-failure-study/README.md): what survives workflow termination, with raw results and reproduction instructions.
- [Cyberwheel reconstruction](../deep-dives/cyberwheel/synthesis.md): simulation, emulation and what public evidence leaves unresolved.

Initial findings cards distill existing evidence. They are not three newly executed experiments or fresh upstream certifications:

| Finding | Evidence depth | Readable evidence | Structured card |
|---|---|---|---|
| Unflushed offline provenance can disappear with its process | Historical recorded experiment | [Flowcept lab](../atlas/labs/flowcept-failure-study/README.md) | [Buffer loss](../cards/flowcept-offline-buffer-loss.json) |
| Supervise resource use across the job's process tree | Pinned code inspection, untested here | [Pattern A2](../lessons/engineering-patterns.md#a2-workers-that-police-their-own-jobs) | [Process supervision](../cards/post-processing-process-tree-limits.json) |
| Evaluate simulated learning separately from emulated behavior | Historical public-source reconstruction | [Cyberwheel boundaries](../deep-dives/cyberwheel/claim-boundary.md) | [Simulation and emulation](../cards/cyberwheel-simulation-to-emulation.json) |

## Query from the repository root

```bash
python3 scripts/research_library.py build
python3 scripts/research_library.py search "offline provenance SIGTERM" --limit 5
python3 scripts/research_library.py search "process memory limit" --lane linux-infra
python3 scripts/research_library.py search "defender simulation" --kind card
python3 scripts/research_library.py search "siting" --kind lead
python3 scripts/research_library.py project flowcept
python3 scripts/research_library.py project cincinnatus
python3 scripts/research_library.py stats
python3 scripts/research_library.py check
```

Commands emit JSON with a boundary statement. Search ranks literal word matches using SQLite FTS5 (any supplied word, relevance ordered); it is not semantic search and cannot guarantee all relevant evidence is returned. Try related terms and follow project packets. Results include repository-relative file paths, original section line numbers, excerpts and project associations. Filters apply to associated catalog projects; a multi-project section can match more than one lane. Associations inferred from names or links are navigation only, not typed relationships. Unassociated institutional context is available without lane filters.

A project packet returns catalog identity/status, lanes, editorial priority, cards, relevant document paths, and explicitly cross-linked registry nodes with their one-hop relationships and sources. It reports when the brief is missing. Large documents and raw experiment outputs are linked rather than embedded. Search within the returned files for detailed claims. A `deep` lane tier is a research priority, not proof that code has been run.

The default database is `.cache/research-library.sqlite3`, ignored by Git. Every read checks a content-hash manifest; edited, added or removed corpus files and referenced experiment outputs require a rebuild. Build validates cards and crosswalk targets before replacing the generated database. It refuses to overwrite an unrelated SQLite database. `--root` and `--db` precede the subcommand when testing a separate local fixture. Rebuild after changing maintained research; `check` verifies freshness and SQLite integrity, not scientific truth.

## Source ownership and identity

| Data | Authority |
|---|---|
| Project IDs, recorded status and affiliation evidence | `discovery/catalog.csv` |
| Lanes, priority tier and selection reason | `discovery/lanes.csv` |
| Sources, role/facility/software nodes and typed edges | `atlas/registry/` |
| Explicit overlap between registry and catalog | [Registry crosswalk](../discovery/registry-links.json) |
| Explanations, evidence ledgers, experiments and limitations | Existing Markdown and lab artifacts |
| Reusable findings | `cards/*.json`, backed by those artifacts |
| Off-catalog candidates and how they were found | `discovery/leads.csv` (a lead is not a catalog project until promoted under RULES 13) |

The crosswalk currently joins DataFed, ADIOS2, Flowcept and Zambeze without merging their records or evidence fields. Broad registry themes, such as agentic workflows, remain separate from catalog projects. An identity match establishes neither a working integration nor an ORNL deployment. The original [registry query tool](../atlas/scripts/atlas_query.py) remains available for registry-only packets.

The index reads explicitly selected public research directories: briefs, signals, deep dives, lessons, connections, docs, verification ledgers, Atlas guides/projects/research/sources/labs, and the root orientation files. It indexes registry records, typed edges and cards separately. Referenced result files contribute freshness hashes; they are not interpreted as newly verified measurements. It does not ingest local chat histories, private context, arbitrary files, untracked discovery snapshots or the unfinished discovery scripts. Historical blocked sources, third-party job leads and unresolved links retain their existing status; indexing does not fix the inherited issues noted in the handoff.

## Card contract, schema version 1

Each `cards/<id>.json` has:

| Field | Meaning |
|---|---|
| `schema_version`, `id`, `project_ids`, `title` | Version 1, filename slug, existing catalog IDs and a concrete finding title |
| `problem`, `mechanism`, `finding` | The problem, how the mechanism works, and exactly what the evidence establishes; retain evidence tags |
| `evidence_level` | `documented`, `code-inspected`, or `experiment-recorded`; not a verification or maturity badge |
| `source_urls`, `code_refs`, `supporting_paths` | Primary URLs, full-commit-pinned code URLs, and existing repository-relative evidence files |
| `experiment` | `status` (`not-run` or `recorded`), `revision`, `command`, `results_path`, and explicit `limitations` |
| `adaptation`, `unknowns` | Proposed reuse marked inferred, plus unresolved questions |

Sources, local evidence and unknowns are required. `code-inspected` requires a pinned code reference. `experiment-recorded` requires recorded status, a revision, reproduction command and an existing results artifact. A historical experiment remains historical; a fresh run records its own inputs, environment, command, outputs and review. The validator checks structure and references. The referee checks whether they support the claim, including licenses and attribution before code reuse.

There is no automatic promotion to “verified.” Source access dates and substantive review belong in the underlying ledgers and [verification log](../verification/log.md). Preserve observed outcomes separately from proposed adaptations and original ORNL implementations separately from our own systems.

## Continue with a team

Ask Codex or Claude:

> Run one bounded ORNL exploration round using docs/research-team.md. Search the library first. Choose a mechanism worth investigating, explain the selection, assign disjoint worker files, and use an independent referee. Save the plan and result in the existing handoff. Finish the scoped artifacts and checks.

This invokes a research process, not a scheduled fleet. Shared files carry evidence between tools; historical chat instructions do not authorize new actions. Pushes, publication, outreach, deployment and work outside this repo retain their existing approval boundaries.
