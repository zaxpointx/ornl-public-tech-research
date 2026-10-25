# Batch 07-08 summary (closed: 5 of 5 verified)

Independent research from public sources only; not affiliated with ORNL. Date: 2026-10-24.

Editorial decision 2026-10-24: discovery batches 07 (zambeze, matris) and 08 (cabana, xacc, exago) are recorded as one combined batch. Catalog rows keep discovered_batch 07 or 08. The discovery-pass notes are in [discovery-notes/batch-07.md](discovery-notes/batch-07.md) and [discovery-notes/batch-08.md](discovery-notes/batch-08.md).

## What was researched
- The discovery pass added 5 rows that passed rule 13: zambeze and matris (batch 07), cabana, xacc and exago (batch 08). Kokkos was added and then removed (ORNL is a contributor, not the owner), and hiop was left out (LLNL copyright). Both are outside projects on the map.
- The discovery pass later added tnqvm (batch 08) after the connections pass flagged it: a tensor-network simulator that plugs into XACC. It is a stub with no brief; its license reads "BSD-3 per README, LICENSE file not in repo" (editorial wording). Catalog is now 68 projects.
- The reading pass wrote all five briefs, each with a rule 13 check first. All five have signals files with the discovery-pass and the connections-pass sections (RULES.md item 17).
- The connections pass added links 165-169 and edited 32, 114, 120, 146, 148, 150 and 162. Map totals: 169 links, 306 tags (173 KNOWN, 18 CORROBORATED, 67 INFERRED, 37 UNKNOWN, 11 UNRELATED). 6 rows added to not-found.md.

## What was verified
- All five briefs passed two fact-check sweeps with Sweep 2 rows in [verification/log.md](../verification/log.md): [XACC](../projects/xacc.md), [Cabana](../projects/cabana.md), [ExaGO](../projects/exago.md), [Zambeze](../projects/zambeze.md), [MatRIS](../projects/matris.md).
- Batch totals: 18 checks, 14 verified, 4 corrected, 0 unverifiable. Corrections: one on xacc, one on exago and two on zambeze; cabana and matris were clean (matris 4 of 4 on a fresh clone).
- OSTI 2477506 does not mention Zambeze. It was dropped from the zambeze catalog row (org_unit back to UNKNOWN) and from map link 114, which is now CORROBORATED from Zambeze's own code plus Flowcept's "zambeze" settings type.
- Verified briefs in total: 39 (37 full plus 2 OSTI-only drafts).

## Still unknown
- Status is unknown for xacc (last commit 2023-08-01; the 2024-08-13 push date matches no commit, likely housekeeping, INFERRED low), zambeze (commits stopped after 2024) and matris (editorial decision: no push since 2025-10-23, no tagged release; CHANGELOG 1.0.0 is a stated version, not a release).
- No public source names a successor to xacc or says Flowcept replaced Zambeze.
- Zambeze imports a ZambezeInterceptor class that current Flowcept no longer has: The fact-check pass found no such class or import in Flowcept `src/` at HEAD on 2026-10-24 (KNOWN as of that date). Whether Flowcept supports Zambeze some other way is the batch 09 question.
- That ORNL/ExaGO continues pnnl/ExaGO is INFERRED; the LICENSE says it uses code from ExaGO v1.6.0 but neither repo says successor.
- ExaGO and GridKit share a community (4 overlapping accounts, common outside libraries like Ipopt) but no code link; same grid-software community is INFERRED.

## Signals highlights
- ExaGO: commits went from 9 in 2025 to 255 in 2026 after the move to ORNL, active authors 5 to 24, counted across all branches; on `develop` alone 2026 has 47 commits from 10 authors (fact-check spot check). Frontier is the main build target.
- Cabana: 17 authors still active in 2025 after ECP ended; 24 papers cite its JOSS paper, 19 with no ORNL author; 0 Spack dependents.
- Zambeze: active authors fell 13, 10, 4 over 2022-2024; 12 PyPI downloads last month (downloads are not users).
- MatRIS: dormant (4 commits in 2025), no packages, 11 citing papers. Git history starts in 2022, before the repo was created in 2023-11.
- The PyPI names cabana and matris belong to unrelated projects.

## What to investigate next
- A GridKit brief, to firm up the grid cluster around ExaGO (batch 09; do not cite LLNL's OSTI 1340202).
- Whether current Flowcept still supports Zambeze (set for batch 09).
- ExaTN brief (batch 09), then a tnqvm brief.
- Finch (stub) now has a confirmed build dependency on Cabana::Grid and is a brief candidate.
