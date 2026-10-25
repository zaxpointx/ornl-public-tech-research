# Research-team plan

## What is already operational

The repository has a catalog, project briefs, evidence tags, verification logs, connection mapping, batch summaries, outside-in signals, and three completed deep dives. This is a strong public-source research base, but coverage is uneven: a brief is not the same thing as a deep reconstruction.

## Team roles

| Role | Output | Review gate |
|---|---|---|
| Editor / coordinator | scope decisions, batch assignments, merged index | resolves conflicts and stale counts |
| Discovery scout | primary project pages, repositories, docs, OSTI and paper records | no unsupported candidates enter the catalog |
| Project reader | standardized plain-English brief and system walkthrough | every claim has a source or is marked unknown |
| Signals analyst | release/commit history, CI/build targets, packages, citations, funding traces | separates observed signals from inferred activity |
| Relationship analyst | dependency, facility, dataset, funding, and downstream links | direct evidence required for each relationship |
| Evidence checker | two-pass source re-fetch and correction log | blocks unverified claims from trusted status |
| Deep-dive lead | synthesis, timeline, system flow, roles, ledgers, verification report | one project at a time; human editorial approval |

## Execution order

Use batches of up to five projects. Finish the current batch before starting another.

1. **Reconcile the atlas:** make catalog, brief files, signals files, index counts, and batch status agree. Add machine-checkable metadata where missing.
2. **Neutron facility pipeline:** Mantid, ONCat, Live Data Server, Post Processing Agent, and Data Workflow Manager. Follow data from experiment through reduction and cataloging.
3. **OLCF operations:** OLCF Test Harness, user documentation, HeCBench, IRIS, DataFed, and related workflow tools. Focus on how software is tested and moved across machines.
4. **Additive manufacturing:** 3DThesis, Finch, AdditiveFOAM, Myna, adamantine, and the explicitly outside-scope ExaCA connection. Compare model fidelity, speed, data flow, and evidence of use.
5. **Grid and energy:** GridKit, ReSolve, ExaGO, TASQC, EnergyPlus, AutoBEM, and Stor4Build. Separate direct dependencies from thematic similarity.
6. **Nuclear and fusion:** SCALE, VERA, Shift/Exnihilo, GITR, Thermochimica, Xolotl, KORC, and Stellarator-Tools. Respect controlled-distribution boundaries.
7. **Climate and data services:** Daymet, TESViS, E3SM/ELM, LandScan, GEDI, and related DAAC services.
8. **Quantum and cyber:** ExaTN, TNQVM, XACC, QIR-EE, Cyberwheel, and the OSTI-only cyber stubs.
9. **Buildings and transport:** Gauntlet, Vivaldi, Real-Twin, FIXS, EnergyPlus, AutoBEM, and Stor4Build.
10. **Synthesis:** publish `LAB-TREE.md`, `lessons/how-ornl-works.md`, `lessons/questions.md`, and `lessons/internship-angle.md` only after the underlying claims are verified.

## Review gates

Before a batch is called complete:

- catalog row, brief, and index entry agree;
- status and maturity wording match the sources;
- ownership, license, funding, and dependency claims are checked;
- every relationship is tagged and sourced;
- unsuccessful searches are logged;
- the validator passes;
- a second reviewer records corrections or confirms no changes;
- the editor states what was deeply read versus only inventoried.

## Honest completion criterion

The atlas is complete only relative to a declared public-source catalog and snapshot date. It must report remaining unknowns and cannot claim to reveal internal ORNL structure, current staffing, restricted work, or every project the laboratory has ever touched.
