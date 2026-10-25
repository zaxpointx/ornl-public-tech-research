# Batch 08 discovery notes, 2026-10-24

Before starting, I re-read RULES.md through item 16, including the new limits. The rows were appended with CRLF line endings, so no other lines in the catalog changed.

## Added (3, after kokkos removal)
- **cabana:** passes rule 13 on two counts. Its README names ORNL among the developers in the ECP CoPA project, and DOE CODE record code-45702 lists ORNL as the research org. The repo belongs to the ECP-copa org, not to ORNL.
- **xacc:** DOE CODE code-5041 and OSTI 1339995 list ORNL as the research org. The repo now sits in the eclipse-xacc org. Status is unknown because the last push was 2024-08-13.
- **exago:** development moved from pnnl/ExaGO, which is now archived, to ORNL/ExaGO, created 2026-01-08. The LICENSE lists UT-Battelle (2026) and Battelle Memorial (2020-2025). DOE CODE record code-176348 lists ORNL. Status is active.
- **kokkos:** removed 2026-10-24 by editorial decision. ORNL is a contributor, not the owner, so it goes on the map as an outside dependency.

## Checked and not added
- **hiop:** the copyright holder is LLNS (Lawrence Livermore). ORNL shows up only through one contributor's affiliation in the README credits, which doesn't count as a named contributing lab, so it fails rule 13. It's a map candidate as an outside dependency of ExaGO.

## Next leads
- ORNL-QCI/xacc-vqe and tnqvm, to check whether they're separate projects
- pkpass
- OSTI searches on grid, microgrid, battery, isotope and HFIR topics
- OpenStudio and BEopt
- Denovo and ORANGE
- IRIS-MASH and IRIS-MEMFLOW
- **tnqvm:** added 2026-10-24 on a connections-pass tip. UT-Battelle 2019 header in CMakeLists. README says BSD-3, but no LICENSE file is in the repo. OSTI 2583844 names ORNL. Status unknown (last push 2025-03-05).
