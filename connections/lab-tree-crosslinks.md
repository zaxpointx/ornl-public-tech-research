# Suggested cross-links for LAB-TREE.md

Independent research from public sources only; not affiliated with ORNL. Prepared 2026-10-24 (ET) from [map.md](map.md) (links cited as "map N"). First written before LAB-TREE.md existed; reconciled with map pass 22 and the tree on 2026-10-24 (ET). The list is organized as area, then facility or program, then project. It is a merge list for the tree's owner; nothing here edits LAB-TREE.md. Divisions or groups appear only where a source names them; otherwise the branch hangs off the lab directly. Arrow types: "uses" (dependency), "feeds" (data or file handoff), "at" (facility), "funded by", "same org" (GitHub org only; shared group is INFERRED).

## Named units (only those a source names)
- Neutron Sciences Directorate (NScD): Mantid copyright footer. map 53 [KNOWN]
- National Center for Computational Sciences (NCCS): OLCF Test Harness developers (map 76); DataFed authors with the Computer Science and Mathematics Division (map 128). [KNOWN]
- Radiation Transport Group, Reactor and Nuclear Systems Division: Shift (map 101, 2016 paper; current name UNKNOWN). [KNOWN]
- Computational Engineering and Energy Sciences group: Thermochimica's GitHub org (map 21). [KNOWN]
- ORNL DAAC: Daymet, TESViS, GEDI tutorials (map 44, 45). [KNOWN]

## Computing and HPC
### Facility: OLCF (Frontier, Summit, Constellation DOIs)
1. OLCF Test Harness at OLCF, NCCS. map 43, 76 [KNOWN]
2. Flowcept at OLCF (Frontier example). map 8 [CORROBORATED]
3. HydraGNN at OLCF Frontier. map 9, 26 [KNOWN]
4. ExaTN at OLCF Summit. map 10 [KNOWN]
5. ExaGO at OLCF Frontier (build scripts). map 170 [KNOWN]
6. DataFed at OLCF. map 51, 128 [CORROBORATED]
7. HeCBench uses OLCF training material. map 155 [KNOWN]
8. Shift/Exnihilo at OLCF Frontier. map 94 [KNOWN]
9. E3SM ELM datasets carry OLCF DOIs. map 78 [KNOWN]
10. AutoBEM / Model America: OLCF DOI only, compute at ALCF. map 99 [KNOWN]
### Program: ECP
11. ReSolve funded by ECP. map 7 [KNOWN]
12. Cabana from ECP CoPA (multi-lab). map 146 [CORROBORATED]
13. Finch uses Cabana (ECP tie indirect). map 32, 50 [KNOWN / INFERRED]
### Projects and tools
14. GridKit uses ReSolve (optional). map 1 [KNOWN]
15. HeCBench feeds from HydraGNN kernel. map 3, 157 [KNOWN]
16. MatRIS uses IRIS. map 120 [KNOWN]
17. IRIS uses QIR-EE (device backend). map 117 [CORROBORATED]
18. QIR-EE uses XACC (optional backend). map 144 [KNOWN]
19. TASMANIAN bundled in xSDK. map 134 [KNOWN]
20. Cabana, Xolotl, adamantine use Kokkos (outside). map 137, 146, 147 [KNOWN]

## Quantum
21. TNQVM plugs into XACC. map 162 [KNOWN]
22. TNQVM uses ExaTN (optional). map 162 [KNOWN]
23. QIR-EE and ExaTN same org (ORNL-QCI). map 42 [KNOWN org; group INFERRED]
24. IRIS reaches XACC via QIR-EE. map 151 [KNOWN]

## Neutron science
### Facilities: SNS and HFIR (NScD)
25. SNAPRed at SNS. map 23 [KNOWN]
26. PyRS at HFIR (HB2B). map 37 [KNOWN]
27. data-workflow at SNS and HFIR. map 36, 75 [KNOWN]
28. ONCat at SNS and HFIR. map 129 [KNOWN]
29. Mantid at SNS/HFIR. map 23 [INFERRED]
### Projects and tools
30. SNAPRed uses Mantid. map 2 [KNOWN]
31. PyRS uses Mantid. map 34 [KNOWN]
32. data-workflow uses Mantid via post-processing-agent. map 74 [KNOWN]
33. data-workflow uses post-processing-agent; sibling of live-data-server. map 91 [KNOWN]
34. post-processing-agent uses Mantid. map 74 [KNOWN]
35. post-processing-agent feeds ONCat. map 104 [KNOWN]
36. post-processing-agent feeds live-data-server. map 107 [INFERRED]
37. post-processing-agent continues mantidproject/autoreduce. map 105 [KNOWN]

## Materials and manufacturing
### Facility: MDF
38. Myna at MDF (Peregrine). map 30, 71 [KNOWN]
### Projects and tools
39. Myna drives 3DThesis. map 27 [KNOWN]
40. Myna drives AdditiveFOAM. map 28 [KNOWN]
41. Myna drives adamantine. map 70 [KNOWN]
42. Myna drives ExaCA (outside, LLNL). map 29 [KNOWN]
43. Finch feeds ExaCA (coupled build). map 171 [CORROBORATED]
44. 3DThesis feeds ExaCA (RDF files). map 172 [KNOWN]
45. AdditiveFOAM feeds ExaCA. map 173 [KNOWN]
46. Finch and 3DThesis use Stork (identity unknown). map 174 [KNOWN use; origin UNKNOWN]
47. Finch uses Cabana. map 32 [KNOWN]
48. adamantine funded by LDRD and EERE. map 125 [KNOWN]

## Nuclear and fusion
49. Shift/Exnihilo part of SCALE (Radiation Transport Group). map 82, 101 [CORROBORATED]
50. OLM uses SCALE/ORIGEN. map 62 [KNOWN]
51. Thermochimica feeds INL MOOSE. map 52 [CORROBORATED]
52. GITR part of STRIPE. map 92 [KNOWN]
53. Xolotl, GITR, KORC same org (ORNL-Fusion). map 22, 66 [KNOWN org; group INFERRED]
54. SCALE and VERA same domain. map 63 [INFERRED]

## Grid and energy
55. GridKit uses ReSolve. map 1 [KNOWN] (same as 14; place under both branches)
56. ExaGO continues archived PNNL ExaGO. map 148 [KNOWN code reuse; continuation INFERRED]
57. ExaGO and GridKit: no code link, shared contributor accounts. map 150 [KNOWN]
58. HydraGNN power-grid models funded by OE. map 127 [CORROBORATED]

## Workflows and data
59. Zambeze uses Flowcept (API drift). map 114 [CORROBORATED]
60. Flowcept and Zambeze funded by LDRD 11521. map 113, 114 [KNOWN]
61. DataFed uses Globus. map 17 [KNOWN]

## Cyber
62. Cyberwheel uses Sandia FIREWHEEL. map 54 [CORROBORATED]
63. Cyberwheel funded by LDRD 11049. map 56 [CORROBORATED]

## Buildings, transport, geospatial
64. AutoBEM feeds Model America feeds EnergyPlus/OpenStudio. map 98 [CORROBORATED]
65. Stor4Build uses EnergyPlus. map 59 [KNOWN]
66. Vivaldi uses Gauntlet. map 58 [KNOWN]
67. Gauntlet feeds USA Structures. map 90 [KNOWN]
68. Real-Twin uses SUMO/VISSIM/AIMSUN. map 80 [KNOWN]
69. Real-Twin and FIXS same org. map 79 [KNOWN org; joint use INFERRED]
70. LandScan HD/USA succeeded by Global/Mosaic. map 102 [KNOWN]

## Earth and climate (ORNL DAAC)
71. TESViS feeds Daymet subsets. map 72 [KNOWN]
72. TESViS feeds GEDI subsets. map 73 [KNOWN]
73. Daymet at ORNL DAAC. map 44 [KNOWN]
74. FATES (outside, LANL) runs inside E3SM ELM. map 46 [KNOWN]

## Pass 22 additions (SNAPRed, PyRS, KORC)
75. SNAPRed uses Mantid. map 2 [KNOWN]
76. SNAPRed at SNS. map 23 [CORROBORATED]
77. PyRS uses Mantid. map 34 [KNOWN]
78. PyRS at HFIR (HB2B). map 37 [KNOWN]
79. PyRS and the AM heat models share a domain only; untested pairing. map 175 [INFERRED]
80. KORC uses PSPLINE, fusion-io, HDF5, OpenACC (outside). map 176 [KNOWN]
81. KORC and GITR same org, no shared contributors, common domain. map 177 [KNOWN org; domain INFERRED]

## Not suggested (keep off the tree as links)
Map links tagged only [UNKNOWN] (18, 19, 20, 38, 47, 49) and [UNRELATED] namesakes (57 LLNL GridKit) should not become tree branches.
