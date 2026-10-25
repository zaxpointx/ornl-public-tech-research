# Batch 01 summary (2026-10-24)

Discovery notes are merged below.

## What was researched
- Discovery (the discovery pass): 18 projects cataloged from public GitHub orgs (ORNL, ORNL-CEES, ORNL-Fusion, neutrons, olcf, ORNL-QCI, ornldaac, mantidproject). The source was the unauthenticated GitHub API only, and DOE CODE and ornl.gov were not queried during discovery.
- Briefs (the reading pass): 6 written: [hydragnn](../projects/hydragnn.md), [mantid](../projects/mantid.md), [gridkit](../projects/gridkit.md), [thermochimica](../projects/thermochimica.md), [datafed](../projects/datafed.md), [cyberwheel](../projects/cyberwheel.md). Each license comes from the actual LICENSE file.
- Connections (the connections pass): 24 links across the 18 projects in [connections/map.md](../connections/map.md), of which 18 are KNOWN, 2 INFERRED and 4 UNKNOWN. Eight KNOWN links go to outside projects (PETSc, OpenFOAM, Globus, and others).

## What was verified
- Catalog spot-check (the fact-check pass) on 5 rows, with 10 checks: 3 verified, 6 corrected, 1 unverifiable. GitHub's NOASSERTION was hiding a real license in every case: resolve and gridkit/datafed have custom UT-Battelle licenses, tasmanian and xolotl are BSD-3, and additivefoam is GPL-3.0-or-later. exatn was changed from archived to unknown because GitHub doesn't flag it as archived. DOE CODE confirms ORNL as the research org for resolve, tasmanian, additivefoam and exatn.
- All 6 briefs were checked by the fact-check pass: 29 claims verified, 13 corrected, 6 unverifiable. The unverifiable ones are the owning ORNL division for each project, plus whether Cyberwheel is still being developed.
- Notable fixes: An INL OSTI report (3374533) confirms Thermochimica is built into INL's MOOSE framework for molten salt reactor modeling. Mantid has exactly five co-owners. SNAPRed's dependency on Mantid is now KNOWN. One overstated KNOWN claim each in datafed and cyberwheel was downgraded to INFERRED.
- DOE CODE confirms ORNL as the research org for every brief except mantid, which is multi-institution.
- No restricted content, implied affiliation or copied text was found.

## Still unknown
- Which ORNL division owns each project. None of the six repos states it.
- ORNL's ownership of xolotl has only one source, since there's no DOE CODE record.
- ORNL's exact share of Mantid. The homepage lists the Neutron Sciences Directorate as one of several co-owners.
- GridKit may come from an earlier LLNL version (2016 OSTI record, same author) [INFERRED].
- Cyberwheel may be LDRD-funded (FY2025 LDRD reports mention it, but nobody has read them yet).
- Cyberwheel, GEDI Tutorials and TASMANIAN have no connections yet.

## Investigate next
- Have the connections pass finish splitting shared-contributor links (contributor KNOWN, same group INFERRED), then the fact-check pass spot-checks map.md.
- Map these outside dependencies: HiOp, SUNDIALS, ExaGO, ADIOS2, DeepHyper.
- Confirm that GridKit and ReSolve come from the same group, and confirm funding (SciDAC, ECP) through OSTI records.
- Run a DOE CODE pass on every batch 1 row using the OSTI records API (`https://www.osti.gov/api/v1/records?q="NAME"&product_type=Software`).

## Discovery notes
### Sources checked (GitHub API, unauthenticated, 2026-10-24)
github.com/ORNL (3 pages), ORNL-CEES, ORNL-Fusion, neutrons, olcf, ORNL-QCI, ornldaac, mantidproject/mantid. DOE CODE / ornl.gov not yet queried.
### Dedupe notes
- PARVMEC, LIBSTELL folded into stellarator-tools.
- ORNL/E3SM is a stale fork (2023) of E3SM-Project; not added. ORNL-CEES/kokkos is an archived fork; skipped.
- olcf/cuda-training-series (1055 stars) is NVIDIA training material, skipped as not ORNL software.
- Many licenses show NOASSERTION in the API; verify LICENSE files during deep reading.
### Priority 6 for deep reading
1. hydragnn - active, well documented, flagship AI-for-materials code.
2. mantid - major neutron software, extensive docs, very active.
3. gridkit - covers the energy-grid domain, active.
4. thermochimica - nuclear/materials, active, has published papers.
5. datafed - cross-facility data infrastructure, active, has docs site.
6. cyberwheel - the cybersecurity entry, clear scope, MIT.
### Batch 02 leads
DOE CODE API (site ORNL); ornl.gov software and licensing pages; ORNL DAAC tools (Daymet, MODIS web service); E3SM/ELM land model and FATES (ORNL climate contributions); neutrons org beyond SNAPRed (data_workflow, PyRS); ORNL-MDF and ornl-ndav orgs (not checked); transportation/buildings repos (gauntlet, vivaldi, HydroFleetIntel).
