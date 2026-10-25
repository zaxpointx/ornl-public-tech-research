# Batch 06 summary (closed: 6 of 6 verified)

Independent research from public sources only; not affiliated with ORNL. Date: 2026-10-24.

## What was researched
- The reading pass wrote six briefs on rows from earlier batches: [Flowcept](../projects/flowcept.md), [IRIS](../projects/iris.md), [TASMANIAN](../projects/tasmanian.md), [Xolotl](../projects/xolotl.md), [QIR-EE](../projects/qiree.md) and [HeCBench](../projects/hecbench.md).
- In plain terms: Flowcept records what happened during workflow runs; IRIS lets one program use several kinds of processors; TASMANIAN builds cheap stand-in models to estimate uncertainty in simulations; Xolotl simulates radiation damage building up in reactor materials; QIR-EE runs quantum programs written in the QIR format on different simulators and backends; HeCBench is 555 small GPU benchmarks written in CUDA, HIP, SYCL and OpenMP.
- Signals became standard for every project from this batch (RULES.md item 17). The connections-pass usage sections are in signals/flowcept.md, iris.md, tasmanian.md, xolotl.md and qiree.md. The discovery-pass history, CI and funding sections were added above them.
- The connections pass added map links 122 to 151 (adamantine, HydraGNN grid use, DataFed, ONCat, TASMANIAN, Xolotl, QIR-EE, Cabana, Kokkos as an outside node, ExaGO, IRIS and XACC). hecbench links start at 152.

## What was verified
Details are in [verification/log.md](../verification/log.md). Each brief has a "Sweep 2 notes" section.
- 24 log rows: 22 verified, 2 corrected, 0 unverifiable (the fact-check tally).
- flowcept 3 verified (second source OSTI 3025007); iris 3 verified (OSTI 3018176; SLAC's new-iris is UNRELATED); tasmanian 3 verified, 1 corrected (DOE CODE code-6305 added, ORNL tie CORROBORATED); xolotl 4 verified, 1 corrected (OSTI 1513390, research org UNKNOWN to CORROBORATED); qiree 4 verified (DOE CODE code-149694, OSTI 3001783); hecbench 5 verified on a fresh clone (ORNL tie KNOWN, both sources on GitHub).
- The fact-check pass also spot-checked the discovery-pass Cyberwheel commit counts against a fresh clone; all match (the 2024/2025 split depends on author date versus commit date).
- Total verified briefs: 34 (32 full plus 2 OSTI-only drafts).

## Still unknown
- tasmanian: why the copyright line names one person.
- xolotl: where the history before the 2018 repo lived (LICENSE dates go back to 2012); no DOE CODE record.
- qiree: the LICENSE-APACHE and LICENSE-MIT files named in COPYRIGHT are missing from the repo. The fact-check pass reads the COPYRIGHT wording as consistent with the UT-Battelle headers (INFERRED).
- hecbench: whether ported benchmarks carry their own license terms (INFERRED possible); no OSTI software record. Dataset hosting left out under rule 16.

## What to investigate next
- The fact-check pass sweep of the batch 06 signals files (the discovery-pass counts use author date).
- The reading-pass proposed next set: cabana, xacc, exago, zambeze and matris (to be confirmed editorially).
- Kokkos row removed from the catalog (editorial decision: contributor, not owner) and listed under Outside projects in INDEX.
- hecbench usage: ORNL's ChatPORT and ChatHPC papers and several LLNL papers use it (the fact-check pass), for the connections-pass usage section.
