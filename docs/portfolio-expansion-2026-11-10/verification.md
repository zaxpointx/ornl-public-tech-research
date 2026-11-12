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
