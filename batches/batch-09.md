# Batch 09 summary (closed: 2 of 2 verified, plus one support note)

Independent research from public sources only; not affiliated with ORNL. Date: 2026-10-24.

## What was researched
- Two briefs for rows already in the catalog from batch 01: [GridKit](../projects/gridkit.md) (rewritten) and [ExaTN](../projects/exatn.md) (new).
- A support note in the [Zambeze brief](../projects/zambeze.md) on whether current Flowcept still supports Zambeze, the open question from batch 07-08.
- No new catalog rows. Three reactor rows that carried discovered_batch 09 for a few hours on 2026-10-28 were moved to batch 12 (editorial decision).

## What was verified
- GridKit and ExaTN passed two fact-check sweeps with Sweep 2 rows in [verification/log.md](../verification/log.md).
- GridKit: 12 log rows, 9 verified, 2 corrected (the subfolder list gained Testing, and `Experimental` is an examples folder, not a model family), 1 unverifiable (owning division).
- ExaTN: 6 log rows, 5 verified, 1 corrected (the catalog said archived; GitHub says not archived, so status is unknown).
- Flowcept note: verified on a fresh clone. Current Flowcept has no ZambezeInterceptor and no FlowceptConsumerAPI, only leftover names in settings and docstrings (KNOWN as of 2026-07-20 UTC, the commit checked).
- Verified briefs in total after this batch: 40.

## Still unknown
- Which ORNL division owns GridKit (no public source says).
- Whether Flowcept supports Zambeze any other way, and whether anyone still runs the two together.
- Why ExaTN went quiet after 2023-07-24.

## What to investigate next
- Do not cite LLNL's OSTI 1340202 for GridKit; it is a different project.
- ReSolve (GridKit's solver library), the 3D-printing heat models and TNQVM, which became batch 10.
