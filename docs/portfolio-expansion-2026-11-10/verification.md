# Verification and continuation: broader ORNL research map

Research date: 2026-11-10. **Verified complete for this cross-domain research expansion and map.** This is not a claim that ORNL has been exhaustively researched or that every existing brief is a deep reconstruction.

## Correct repository and starting point

The user identified `zaxpointx/ornl-public-tech-research` as the intended GitHub repository. Its local checkout is `/Users/cayden/Projects/ornl-public-tech-research`. GitHub was inspected through its connected read-only tools and local research was read before edits. This is distinct from the older `/Users/cayden/Projects/ornl-atlas` checkout used earlier in the conversation. That earlier work was neither overwritten nor silently imported.

The canonical checkout was clean when inspected, on `research/ornl-public-ecosystem`. Existing goal, rules, coverage matrix, research manifest, team plan, final batch and selected relationship ledger were read. Its structural audit reported 69 catalog entries, 67 briefs, 40 signals files and two OSTI-only entries without briefs. No relevant owner chat was returned in the available recent/history thread listings; the repository's own handoff and coverage notes supplied continuation context. Work proceeds on `codex/public-portfolio-map`. No commit, push, merge, publication, credential change or signing workaround was performed.

## What was added

- A deterministic human-readable and JSON map of all 69 catalog entries across ten research domains. Each entry links existing briefs/signals/case-study mentions without claiming equal depth.
- Export of the 33 inherited selected relationship propositions, retaining DIRECT/INFERRED/UNKNOWN, limitations, primary URLs and original source-ledger context. These old sources were not all re-fetched in this batch.
- Four new research chapters: computing/instruments, materials/biology, energy/Earth and geospatial uncertainty. Their source ledgers contain 20, 14, 12 and 3 source records respectively. Some records include more than one URL; this is 49 ledger entries, not 49 independent corroborating sources.
- Six new direct artifact relationships and two explicitly unestablished implementation links, available as JSON and a small diagram. The complete map includes these separately from the inherited graph.
- A source-backed reading entry point and navigation links in README, INDEX, the public research guide and coverage matrix. The existing catalog remains unchanged; candidate research is not silently promoted to formal project briefs.
- A regeneration/freshness command and CI freshness check, so future catalog changes cannot quietly leave this map stale.

## Discovery and separate verification

Three subagents researched computing/instruments, materials/biology and energy/Earth. The parent researched geospatial uncertainty, built the map, integrated navigation, read all chapter narratives and checked source boundaries. Subagents returned durable files rather than unsupported summaries.

Each chapter records a discovery and re-fetch/repair sweep. The materials researcher then independently refereed the energy chapter, and the energy researcher independently refereed the materials chapter. See [energy referee](referee-energy.md) and [materials referee](referee-materials.md) for exactly which claims were independently checked and which were outside those reviews.

The parent independently fetched the final nylon abstract, MIJAMP paper, HydraGNN release metadata, Daymet overview/calendar guide, Model America record, ADIOS2 queue documentation, LandScan paper, release announcement and time-series dataset metadata. Eight pinned computing source excerpts were additionally checked against raw source files; all eight matched. The [parent check artifact](parent-source-checks.json) records exact URLs and scope. A literal match checks the cited string, not all interpretations or runtime behavior.

Important repairs/qualifications retained:

- Selective nylon enzymes still have below-1% yield; selectivity is not practical throughput.
- HydraGNN's inspected writer uses BP5; this does not establish SST streaming. The fine-tuning README's v5.0 prerequisite is now stated separately from untested compatibility. The 2025 pretraining paper and 2026 artifact release remain distinct stages.
- SST blocking is conditional on reader/retention state and is not a durability guarantee.
- A selected quantum amplitude is not a full-state simulation. Truncation, numerical accuracy and memory constraints remain visible.
- Shape-valid microscopy axes are not necessarily physically calibrated; legacy and current data representations and fitting APIs remain distinct.
- AutoBEM's closed generator is separate from public generated artifacts and omitted upstream metadata.
- Daymet leap-day/calendar and daylight-radiation rules must survive downstream transformations. Funding by E3SM does not establish a specific forcing configuration.
- LandScan ambient and backcast populations are modeled quantities, not hourly observations or fifty independent censuses. The paper's request-only code/data statement is not relabeled open-source software.

## Checks and observed results

- `python3 scripts/audit_atlas.py`: structural checks PASS; catalog/brief/signal counts unchanged; the two known stubs remain explicit.
- `python3 scripts/build_portfolio_map.py --check`: map freshness passes.
- Exact set comparison confirms all 69 catalog IDs occur in the generated map, domain membership totals 69, four research chapters are indexed, and all three inherited evidence states survive export. Eight new propositions include exactly two UNKNOWN links.
- `python3 -m compileall -q scripts`: passes.
- `git diff --check`: passes.
- External links in the four new research chapters: **57 unique linked URLs, all HTTP 200** through direct curl GET checks. See [HTTP check record](http-source-checks.json). Historical extraction failures recorded in chapters remain historical observations; no access controls were bypassed. HTTP success does not establish a claim's truth, file availability or redistribution permission.
- The repository audit checks local Markdown links, including all new reading paths. JSON artifacts were parsed. Changes and new files were read back; no unrelated tracked changes were introduced.

No upstream scientific software, dataset download, facility experiment, network emulation or local numerical experiment was executed in this batch. The proposed experiments are deliberately labeled proposals. The earlier separate Atlas's toy runner is not represented as new research or as an ORNL implementation here.

## What remains and where to continue

The new map covers the declared catalog, not every ORNL project. Organizational coverage, experimental facilities, historical programs, code release completeness, outside usage and mature scientific replications remain uneven. CPAD and Cincinnatus retain their existing OSTI-only boundaries. Current operations, private implementation, universal numerical accuracy and complete cross-stack compatibility remain unknown unless a precise source supports them.

Continue with one full source-to-result case at a time, chosen from the new chapters: (1) scientific streaming loss versus rare-event recall; (2) AtomAI-style coordinate extraction with known synthetic ground truth; (3) Daymet held-out station errors and calendar/unit checks; (4) one version-pinned public building model; (5) quantum truncation versus exact small-circuit results. These priorities are editorial judgments, not ORNL roadmap claims. A future experiment should measure a scientific failure boundary and preserve inputs, versions and errors; it should not replace broad research with another generic workflow demo.

## Continuation, 2026-11-11: batch 13 and engineering patterns

This continued the work above on the same branch. The 2026-11-10 files were left as written, apart from navigation and count lines in README, INDEX and the coverage matrix, and a regenerated portfolio map.

- **New catalog rows.** Five rows, all verified with two sweeps: ADIOS2, Celeritas, DEDFoam, ChatHPC and MATEY. Totals are now 74 rows, 72 briefs and 45 signals files. See [batch 13](../../batches/batch-13.md).
- **Patterns guide.** [lessons/engineering-patterns.md](../../lessons/engineering-patterns.md) has 16 patterns pinned to commits in 15 public repositories, including two findings that update older work: SNS queue-contract drift (`EXPRESS`) and the test harness's `othctl` interface.
- **Connections.** Map Pass 33 adds links 226-241. The headline link is the ORANGE geometry engine shared by Celeritas and Shift (OSTI 3376506).
- **Checks.** `audit_atlas.py` PASS. `build_portfolio_map.py --check` valid at 74 projects. External links in the new files were checked with HTTP requests (see the batch file). Code was read, not built or run.
- **Next.** An ORANGE lineage deep dive; a cross-repo contract check for the SNS queue names; one small local experiment that measures a failure boundary (pattern D2 or D5) instead of demoing a workflow.

## Continuation, 2026-11-11 (later): ornl-atlas merged; focus lanes

- **Merge.** The former `ornl-atlas` repository now lives in [atlas/](../../atlas/README.md). It was copied from its commit `f70741a` plus the uncommitted work present at 21:59 local time, including the Flowcept failure study.
  - Left out: a private personal context file, the old agent instruction files, and one archived, mis-scoped planning document.
  - Sanitized: two private local paths and three raw web-page scrapes.
  - The original checkout was not modified or deleted. Retiring it is a separate decision, best made once no agent is still working there.
- **Focus.** [discovery/lanes.csv](../../discovery/lanes.csv) tags all 74 projects (6 deep, 20 lead, 48 pool), and the audit checks that it covers the catalog.
- **Agent entry point.** The root [AGENTS.md](../../AGENTS.md) is now the single guide: lanes, a where-to-look table and all checks.
- **Patterns.** Pattern A4 now cites the lab's measured result: a killed offline Flowcept run leaves zero records.
- **Checks.** Audit PASS, map check valid, atlas registry valid, and the atlas query-tool and lab tests pass from the repository root. CI runs all of them.
- **Open.**
  - The catalog and `atlas/registry/` overlap on a few projects and have not been reconciled.
  - The atlas text says its drafts were not posted, but the lab README records upstream pull request ORNL/flowcept#357; the atlas README copy was corrected to match.
  - A second agent's untracked discovery scripts (`scripts/discover_*.py`, `discovery/snapshots/`) were present during this work and were deliberately left uncommitted.
- **Atlas link check, 2026-11-11.** 174 unique URLs: 158 returned 200, 1 redirected, 11 returned 403 and 4 returned 404.
  - The 403s come from sites that block automated requests (ACM, filtered ornl.gov publication pages, job aggregators), so they are not dead.
  - Dead (404), still to replace: `ornl.gov/labsofthefuture`, two `ornl.gov/staff-profile/...` pages, and `ornl.gov/project/autonomous-chemistry-lab-accelerated-materials-discovery-and-innovation`.
- **Rules conflict to reconcile.** The atlas registry cites job postings on third-party aggregators (CareerBuilder, ZipRecruiter, Teal). RULES.md item 16 accepts only official job boards. Those records should be re-sourced to the ORNL careers site or downgraded to `lead`.
- **Next.** The first lane deep dive: Cyberwheel (understand, run, find its failure boundary, write it up).


## Continuation, 2026-11-11: exploratory research team and searchable library

**Verified complete for this local setup and retrieval pilot.** This is not fifty completed investigations, a new ORNL experiment, or a freshly verified census of the laboratory.

### Owner decisions and bounded outcome

The owner wants exceptional discoveries that reveal things worth building or learning, with no predefined personal build target. Fifty exceptional projects would be more useful than hundreds of summaries; this is a quality preference, not a quota. Research depth is the investigator's judgment. Readable guides and agent retrieval should share maintained files. The owner authorized a bounded team inspired by the scout/reader/experimenter/referee workflow. These are owner/editorial decisions, not ORNL claims.

Question for this setup round: can Codex and Claude retrieve the existing public research, distinguish its evidence depth, and continue a small exploratory investigation without rebuilding the library or repeating prior work? Stop bound: working offline index, explicit identity joins, three evidence-backed pilot cards, reusable workflow, independent review and passing local checks. No new large research batch.

### Starting state and ownership

Started from d630f24 on `claude/merge-ornl-atlas`; created `codex/research-library` without changing history. Existing untracked `scripts/discover_software.py`, `scripts/discover_doecode.py` and `discovery/snapshots/` were left untouched and are excluded from the maintained search corpus. Existing Python cache files were preserved; generated bytecode and the local library database are now ignored.

Parent inspected the relevant Codex chat “Plan ORNL Atlas research workflow” and the latest relevant Claude history. Historical assistant instructions were treated as evidence, not new authorization. Their key reusable work already lives here: guides, catalog, patterns, registry and the Flowcept experiment. Claude's separate Cyberwheel-experiment report remains an unverified lead outside this repo. No external worktree was read or imported in this setup round.

The coordinator owned the database, tests, integration, navigation and handoff. One worker inspected existing records and independently reviewed the implementation/cards; another owned only the workflow/skill/template; a third distilled only cards. Their file ownership was disjoint. The reviewer did not author the database or cards. Worker handoffs supplied paths and concrete findings.

### Changes

- `scripts/research_library.py` builds a disposable local SQLite FTS5 index and offers search, project packets, stats and freshness/integrity checks. Uses Python standard library only; no server, credentials or model/API calls.
- `discovery/registry-links.json` explicitly joins DataFed, ADIOS2, Flowcept and Zambeze identities. Catalog status, registry evidence and local study designs remain distinct. Other broad registry themes are not silently merged with projects.
- Three cards distill prior evidence: Flowcept offline buffer loss (recorded experiment), post-processing process-tree supervision (inspected code), and Cyberwheel simulation/emulation boundaries (documented reconstruction). Proposed adaptations remain inferred. No upstream software was executed in this round.
- `docs/research-team.md`, `.agents/skills/ornl-research/SKILL.md` and `templates/research-round.md` provide an invoked bounded team, evidence-dependent depth, disjoint ownership, fresh referee and file handoffs. The existing handoff remains the continuation record.
- `docs/research-library.md`, root GOAL/AGENTS/README and CI connect the human guide, cards and searchable index. AGENTS map check passed. Codex supports the repo-local skill; Claude can follow the same workflow through its existing AGENTS include. No global agent configuration was changed.

### Verification and repairs

Independent review re-fetched card sources and checked raw historical results; exact URLs, support and limits are in the latest section of `verification/log.md`. It found a collection/fingerprint race, repaired with before/after manifests and a regression test. It also found the historical Cyberwheel emulator README returns 404; the new card uses supported public sources and retains the historical boundary. Search indexing now includes the verification and not-found ledgers.

Passed checks: structural audit (74 catalog entries, 72 briefs, 45 signals); map freshness (74 projects, 33 selected relationships, ten domains); registry validator; ten new library tests; three existing query tests; twenty synthetic-runner tests; Python compilation; skill validation; AGENTS pointer check; scoped diff and whitespace review. Library build/check pass, and final integration exercises Flowcept context/source joins, filtered seed-card retrieval, process-limit and provenance queries, verification ledger search, and missing CPAD/Cincinnatus briefs. Freshness rejects changed, added or deleted inputs and modified recorded outputs. Invalid cards/crosswalks do not replace a working index. No broad scientific re-verification is implied.

### Remaining boundaries and next round

The index is lexical retrieval, not a semantic answer engine. Name/link associations only aid navigation. Registry source promotions, historical third-party job leads and existing dead links keep their inherited limitations. The unfinished discovery collectors were neither validated nor adopted by this outcome. No push, publication, deployment, outreach or upstream issue/PR was performed.

Next bounded investigation: at pinned post-processing-agent code, determine whether a short-lived child or polling interval can exceed the intended process-tree memory/time budget. Search the process-tree card first; inspect the dependency/configuration contract; choose a small synthetic local test only if feasible, with prediction, bounded child resources and raw results. Code inspection remains a valid outcome if execution needs unavailable services. Separately, harvesting claimed external Cyberwheel artifacts requires permission for inspection outside this named repo, then evidence verification before import. Do not repeat its setup based solely on the old assistant report.


## Round plan, 2026-11-15: off-catalog discovery, cybersecurity and software engineering

- Question to resolve: what public ORNL cybersecurity and software-engineering projects exist outside the GitHub software catalog and the two 2026-11-11 snapshots, and which have enough public material to study?
- Existing evidence searched and read: catalog, lanes, both snapshots, the library, and the OR-SAGE site (seeded in `discovery/leads.csv` as the model case: a standalone ornl.gov site absent from the catalog and snapshots).
- Selection rationale: the owner wants discovery across the whole institution, not only GitHub. Cyber work is mostly report-only, so off-catalog surfaces are where it lives.
- Depth: artifact study (candidate discovery only). No code is run this round.
- Work bound: two scouts with about 15 new candidates each, then one referee on the top leads. Stop after the leads merge and a ranked shortlist.
- Ownership:
  - Coordinator (Claude, Opus): `discovery/leads.csv`, `verification/not-found.md`, this handoff.
  - Scout A: `discovery/scouting/2026-11-15-ornl-web.md`, covering ornl.gov, standalone sites, tech transfer and sponsors.
  - Scout B: `discovery/scouting/2026-11-15-records-papers.md`, covering OSTI, DOE CODE, papers and artifact repositories.
  - Referee: an appended paragraph in `verification/log.md`.
- Expected checks: audit, library build/check, both test suites, and `search --kind lead` for merged leads.

## Result, 2026-11-15: off-catalog discovery round 1

**State: verified complete for the declared bound.** This is not a census of ORNL's off-catalog work.

- **Setup (commit 07137bb).**
  - Claude Code coordinator skill `/ornl-research` with discover, deep-dive, rebuild and triage modes.
  - Agents `ornl-scout`, `ornl-reader`, `ornl-experimenter` and `ornl-referee` in `.claude/agents/`.
  - `discovery/leads.csv`, validated by the audit and the library (`search --kind lead`). Scout reports in `discovery/scouting/` are indexed.
  - The audit link check now skips `.cache/`.
  - In this session the helpers ran as general-purpose agents that followed the role files. A fresh session should load them natively, but that hasn't been confirmed yet.
- **Discovery.**
  - Scout A (ornl.gov, standalone sites, tech transfer, sponsors) and scout B (OSTI, DOE CODE, papers, artifacts) found 33 new candidates.
  - All 33 were deduped against the catalog, leads and both snapshots.
  - Merged result: 39 leads in all, 32 of them candidates (11 deep, 20 lead, 1 pool).
  - 4 rejected: one duplicate, one repo that moved to a non-ORNL owner, one with no ORNL attribution, one personal project.
  - 2 out of scope: product- and facility-specific vulnerability assessments, logged and not opened.
  - 24 empty searches appended to `verification/not-found.md`.
- **Referee** (fresh agent, ten top leads): 3 verified as written, 7 corrected, no tier changes. The verdict table is in `verification/log.md`, and the corrections are applied to the leads.
  - ai-atac-cyber-range and cyber-ops-research-range are the same ICCWS 2021 paper, now merged.
  - UnifyFS meets RULES 13: its LICENSE names UT-Battelle as a copyright holder, and its OSTI record names ORNL. It's eligible for promotion once a brief and lanes row are written.
- **Flags.**
  - AMIGO generates evasive malware. Study only its published description; never reconstruct the generator.
  - Ranges and testbeds (AI ATAC range, SI-GRID) are paper-only studies.
  - Two DOE CODE candidates host code on code.ornl.gov, which hasn't been opened yet.
- **Collector gap.** DOE CODE lists 563 records with ORNL as site owner. 111 of them are missing from the 2026-11-11 snapshot, because its all-fields query selects a different set. `scripts/discover_doecode.py` should take the union of both queries.
- **Checks.** Audit PASS, map check valid, registry valid, 12 library tests and 3 atlas tests pass, and library build/check is current. Lead search returns `road-can-dataset` for "CAN intrusion dataset". No code was run, and nothing was pushed.
- **Next bounded investigation (deep-dive).** On the public ROAD dataset with the ORNL companion code `can-time-ids-benchmark` (DOE CODE 69319, GPL-3.0): does a time-based CAN IDS baseline detect ROAD's masquerade attacks, and where does it fail? This is cyber-first with public code and data, and it connects to catalog `can-d`. Alternatives:
  - stripped-bof-llm, rebuilt from its paper on Ghidra.
  - The post-processing-agent process-tree question from the earlier handoff.

## Round plan, 2026-11-15: deep dive, time-based CAN intrusion detection on ROAD

- **Question.** Using ORNL's public benchmark code at a pinned commit and the public ROAD dataset, does a time-based CAN IDS detect ROAD's masquerade attacks? Where does detection fail, by attack type, signal and window?
- **Existing evidence read.**
  - Leads `can-time-ids-benchmark` (DOE CODE 69319, site ownership ORNL, GPL-3.0, HEAD e0c862d at 2026-11-15) and `road-can-dataset` (Zenodo 10462796, CC BY 4.0, road.zip 556.7 MB).
  - Catalog `can-d`.
  - Referee verdicts in `verification/log.md`.
- **Why.** It's cyber-first, with public ORNL code plus public real-vehicle data, and it connects to the existing CAN cluster.
- **Depth.** Code reconstruction, then experiment.
- **Bound.**
  - One reader, one experimenter, then one referee.
  - Run locally only, on public data. Cap the run's memory and time. No contact with any vehicle or ORNL system.
  - The dataset download needs the owner's OK.
- **Ownership.**
  - Coordinator: this handoff, cards and leads.
  - Reader: `deep-dives/can-time-ids/reconstruction.md`.
  - Experimenter: `atlas/labs/can-time-ids-road/`.
  - Referee: an appended paragraph in `verification/log.md`.
  - Clones and data go in `.cache/src/` and `.cache/data/`, which Git ignores.

## Result, 2026-11-15: deep dive, time-based CAN IDS on ROAD

**State: verified complete for the declared question.** The lab replayed one vehicle's dynamometer captures offline. That says nothing about live vehicles or the paper's plug-in.

- **Reader.** [Reconstruction](../../deep-dives/can-time-ids/reconstruction.md) of ORNL's benchmark at `e0c862d`, with line-pinned citations.
  - The code excludes masquerade and accelerator attacks.
  - The Binning code sums six gaps, unlike the paper's wording.
  - Labels ignore payload.
  - The "with outliers" results depend on pickles the repo doesn't ship.
- **Experimenter.** [Lab](../../atlas/labs/can-time-ids-road/README.md): an independent re-implementation, checked against the pinned helper code, run offline on ROAD (Zenodo md5 verified). Python 3.10 in an isolated venv; it took 43 s and 3.6 GB peak.
  - R0: the Mean and Binning confusion matrices reproduce exactly on two seeds. Gaussian is within 14 false positives.
  - Q1: Mean and Binning have recall 0 on all 13 masquerades. Gaussian catches part of the slow-injector coolant masquerade, at precision 0.32 or lower.
  - Q2: switching Gaussian to the 3-of-6 rule takes F1 from 0.26 to 0.92.
  - Q3: payload labels keep exactly 50.00% of positives in every targeted log, and F1 at the published optima falls to about 0.65.
  - Four of the predictions are scored wrong in the README.
- **Referee.** 11 verified, 3 corrected and 1 unverifiable; the table is in `verification/log.md`, and all the corrections are applied.
  - DOE CODE 69319 lists ORNL as site owner and developer affiliation, with the research-org field empty.
  - It couldn't prove the predictions were written before the results, because the README was edited after the runs started.
- **Integration.**
  - `can-time-ids-benchmark` promoted from the leads to the catalog under RULES 13 (DOE CODE ORNL site ownership plus ORNL author affiliations), with a lanes row (cybersecurity, deep), a [brief](../../projects/can-time-ids-benchmark.md), an INDEX entry and a rebuilt portfolio map.
  - New card `cards/can-time-ids-masquerade-blindspot.json`.
  - The ROAD data, the clone and the venv stay in the ignored `.cache/`.
- **Not done.**
  - The notebook itself was not run.
  - KDE was skipped (over 5 hours in the original run).
  - Only one referee sweep, not the full two-sweep brief standard.
  - No upstream issue was opened about the label or paper discrepancies. That would count as outreach and needs the owner's OK.
- **Next bounded question.** Can a one-sided slow-period or period-drift test on the target ID catch the coolant and correlated-signal masquerades at a false-positive rate of 1e-3 or less, while staying blind on the 0xD0 masquerades whose period matches the real one?
