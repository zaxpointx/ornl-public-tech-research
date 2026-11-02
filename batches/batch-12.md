# Batch 12: reactor software (closed: 3 of 3 verified)

Opened 2026-10-28. Closed 2026-10-29: all three briefs passed two fact-check sweeps (RULES 11).

## What was researched

- [TRANSFORM](../projects/transform-library.md): open Modelica library for reactor and energy-system thermal hydraulics (Apache-2.0, active).
- [Profugus](../projects/profugus.md): open mini-app holding the core kernels of the export-controlled Exnihilo suite, built for performance studies rather than real answers (BSD-2, last push 2018).
- [Molten Salt Database](../projects/molten-salt-database.md): short brief (RULES 21) from the public about and access pages only. The data files need an account plus a membership request, so nobody opened them.
- The 3D-printed reactor program (Transformational Challenge Reactor) is covered as history in the [reactor deep dive](../deep-dives/nuclear-reactor-software.md), with no catalog row (lead decision 2026-10-29).

## What was verified

- Sweep 1 (2026-10-29) on all three briefs and their related-projects tables: 19 held, 9 fixed, 3 unverifiable (GitHub rate limit). Nothing restricted.
- Sweep 2 (2026-10-29): two Profugus lines toned down ("a rare public window" into the locked codes, not "the only" one); Profugus star and fork counts confirmed.
- After sweep 1: OpenModelica for TRANSFORM is UNKNOWN (was INFERRED); "Profugus is not in SCALE" is UNKNOWN (an absence, not a proof); the salt database's funding programs apply to the thermochemical side only; Profugus funding is DOE's advanced scientific computing office.
- Map side: Shift is part of SCALE is back to KNOWN (SCALE manual's Shift chapter plus a second source). Nothing public says Profugus ships with SCALE.

## Still unknown

- Whether OpenModelica can run TRANSFORM, or only paid Dymola (UNKNOWN; the repo only links a course list).
- Whether Profugus still builds; its macOS scripts date from about 2017.
- Whether Profugus is a cut-down twin of Shift (INFERRED in the brief).
- Whether the failing Thermochimica salt tests on a Mac need a file from the gated Molten Salt Database (INFERRED; four salt tests load a file not in the public data folder and one example input names an MSTDB file).
- Which ORNL unit owns TRANSFORM.

## Investigate next

- The deep dive's "what can be built and run at home" section, after the checks.
- The 3D-printing and grid walkthroughs.
