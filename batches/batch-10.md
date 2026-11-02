# Batch 10 summary (closed: 5 of 5 verified)

Independent research from public sources only; not affiliated with ORNL. Date: 2026-10-24.

## What was researched
- Five briefs: [ReSolve](../projects/resolve.md) (GPU linear solvers that GridKit uses), [3DThesis](../projects/3dthesis.md), [Finch](../projects/finch.md) and [AdditiveFOAM](../projects/additivefoam.md) (the three 3D-printing heat models, fastest to fullest), and [TNQVM](../projects/tnqvm.md) (a tensor-network simulator that plugs into XACC).
- No new catalog rows. These five fed two deep dives opened the same day: [3D-printing timing](../deep-dives/additive-manufacturing-timing.md) and [connections](../deep-dives/additive-manufacturing-connections.md), and the [grid tools timing](../deep-dives/grid-tools-timing.md) and [connections](../deep-dives/grid-tools-connections.md).

## What was verified
- All five passed two fact-check sweeps with Sweep 2 rows in [verification/log.md](../verification/log.md).
- Corrections: ReSolve's license is a custom permissive UT-Battelle and Battelle license, not "no assertion"; AdditiveFOAM is GPL-3.0-or-later (it inherits OpenFOAM's), and "metal" in its description is now INFERRED; Finch's ORNL tie needed a second source (DOE CODE code-122647), and a later check found its funders are DOE Office of Science and NNSA. 3DThesis and TNQVM were clean.
- A later check identified Stork, a public ORNL go-between that turns heat data from 3DThesis and Finch into input for microstructure codes like ExaCA.
- Verified briefs in total after this batch: 45.

## Still unknown
- TNQVM's license: the README says BSD-3 but the repo has no LICENSE file. Status unknown.
- Whether TNQVM still builds against current XACC and ExaTN, both quiet too, and whether anyone maintains it.
- The owning unit for AdditiveFOAM and 3DThesis, whether 3DThesis's older GitLab.com history was fully moved over, and outside users for all five.

## What to investigate next
- The 3D-printing and grid walkthroughs, once the remaining briefs land.
- KORC, SNAPRed and PyRS, which became batch 11.
