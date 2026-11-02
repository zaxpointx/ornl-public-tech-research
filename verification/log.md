# Verification log

One row per claim checked. Verdicts: verified / corrected / unverifiable.

| Date | Project | Claim | Source checked | Verdict | Notes |
|---|---|---|---|---|---|
| 2026-10-24 | resolve (catalog) | License NOASSERTION | github.com/ORNL/ReSolve LICENSE | corrected | Custom permissive UT-Battelle + Battelle Memorial license |
| 2026-10-24 | resolve (catalog) | ORNL project, GPU linear solvers | osti.gov DOE CODE code-114681 | verified | ORNL listed as research org |
| 2026-10-24 | tasmanian (catalog) | License NOASSERTION | github.com/ORNL/TASMANIAN LICENSE | corrected | BSD-3-Clause |
| 2026-10-24 | tasmanian (catalog) | ORNL sparse-grid/UQ toolkit | osti.gov/biblio/1231809 | verified | ORNL research org, 2013 record |
| 2026-10-24 | additivefoam (catalog) | License NOASSERTION | github.com/ORNL/AdditiveFOAM LICENSE | corrected | GPL-3.0-or-later (inherits OpenFOAM) |
| 2026-10-24 | additivefoam (catalog) | Metal AM heat/mass transfer [KNOWN: repo description] | repo README + DOE CODE code-108345 | corrected | Heat/mass transfer for AM verified via README; "metal" retagged INFERRED |
| 2026-10-24 | xolotl (catalog) | License NOASSERTION | github.com/ORNL-Fusion/xolotl LICENSE | corrected | BSD-3-Clause, multi-institution copyright |
| 2026-10-24 | xolotl (catalog) | Second primary source for ORNL ownership | osti.gov software search | unverifiable | No DOE CODE record found |
| 2026-10-24 | exatn (catalog) | Status archived | GitHub API (archived=false) | corrected | Stale since 2023-07-24 but not archived; status set to unknown |
| 2026-10-24 | exatn (catalog) | ORNL tensor-network library, BSD-3 | osti.gov DOE CODE code-45739 + LICENSE | verified | |
| 2026-10-24 | hydragnn | License BSD-3, copyright 2021 ORNL | repo LICENSE + GitHub API | verified | |
| 2026-10-24 | hydragnn | Languages ~87% Python / 13% shell | GitHub /languages | verified | |
| 2026-10-24 | hydragnn | Releases v2.0.0, v3.0, v4.0, v5.0 with dates; created 2021-05-28 | GitHub releases API + DOE CODE code-121354/164024/180990 | verified | |
| 2026-10-24 | hydragnn | ~22 contributors; 127 stars, 48 forks | GitHub API | verified | |
| 2026-10-24 | hydragnn | DDP/FSDP/DeepSpeed, equivariant layers, MLIP, OPF training, ADIOS, Python 3.11-3.14 | README | verified | |
| 2026-10-24 | hydragnn | ~40 example datasets | GitHub contents API (examples/) | corrected | 35 example folders |
| 2026-10-24 | hydragnn | Package subfolders list | GitHub contents API | corrected | Added data, domain_losses, third_party |
| 2026-10-24 | hydragnn | Frontier uses AMD GPUs [INFERRED] | docs.olcf.ornl.gov Frontier user guide | corrected | Retagged KNOWN (MI250X) |
| 2026-10-24 | hydragnn | DOE CODE DOIs from CITATION.cff | osti.gov records API | verified | Also added v3.0/v4.0 records; ORNL research org confirmed |
| 2026-10-24 | hydragnn | Owning ORNL division [UNKNOWN] | repo + DOE CODE | unverifiable | Not stated in either |
| 2026-10-24 | mantid | GPL-3.0 license | LICENSE.txt + GitHub API | verified | |
| 2026-10-24 | mantid | Co-owners incl. ORNL NScD | mantidproject.org footer | verified | |
| 2026-10-24 | mantid | Languages, ~307 contributors, created 2011, releases | GitHub API | verified | |
| 2026-10-24 | mantid | DOI and OpenSSF badge | CITATION.cff + README | verified | |
| 2026-10-24 | mantid | "CSNS (China) and others" | mantidproject.org footer | corrected | Exactly five holders; removed "and others" |
| 2026-10-24 | mantid | SNAPRed built on Mantid [INFERRED] | neutrons/SNAPRed pyproject.toml | corrected | Retagged KNOWN |
| 2026-10-24 | mantid | ORNL share / maintaining team | repo + homepage | unverifiable | |
| 2026-10-24 | gridkit | Custom UT-Battelle license | LICENSE (develop) | verified | |
| 2026-10-24 | gridkit | Dependencies SUNDIALS/Ipopt/Enzyme/ReSolve | README | verified | |
| 2026-10-24 | gridkit | C++20, CMake 3.13 | README + CMakeLists.txt | verified | |
| 2026-10-24 | gridkit | Releases, contributors, ORNL ownership | GitHub API + DOE CODE code-152622 | verified | Also 2016 LLNL GridKit record, same author (INFERRED predecessor) |
| 2026-10-24 | gridkit | GridKit/ subfolder list | GitHub contents API | corrected | Added Testing |
| 2026-10-24 | gridkit | Owning division | repo + DOE CODE | unverifiable | |
| 2026-10-24 | thermochimica | BSD-3 license | LICENSE | verified | |
| 2026-10-24 | thermochimica | Three run methods, JSON, gfortran/LAPACK | README | verified | |
| 2026-10-24 | thermochimica | civet.inl.gov CI, no releases/tags | README + GitHub API | verified | |
| 2026-10-24 | thermochimica | Languages, ~20 contributors | GitHub API | verified | |
| 2026-10-24 | thermochimica | Gibbs minimization [INFERRED] | osti.gov/biblio/3374533 | corrected | Retagged KNOWN |
| 2026-10-24 | thermochimica | MOOSE integration [INFERRED] | osti.gov/biblio/3374533 | corrected | Retagged KNOWN |
| 2026-10-24 | thermochimica | Nuclear use [INFERRED] | osti.gov/biblio/3374533 | corrected | Retagged KNOWN (MSR) |
| 2026-10-24 | thermochimica | CEES meaning [UNKNOWN] | github.com/ORNL-CEES | corrected | Computational Engineering and Energy Sciences Group |
| 2026-10-24 | thermochimica | src/ folder list | GitHub contents API | corrected | Added debug, exec, module |
| 2026-10-24 | thermochimica | Owning division | repo + OSTI | unverifiable | |
| 2026-10-24 | datafed | Custom UT-Battelle license | LICENSE.md | verified | |
| 2026-10-24 | datafed | Central services at OLCF | doc_source overview.rst | verified | |
| 2026-10-24 | datafed | Globus/GridFTP, copy not move, OAuth2 | overview.rst | verified | |
| 2026-10-24 | datafed | Semantic + calendar versioning, releases/tags | README + GitHub API | verified | |
| 2026-10-24 | datafed | ORNL ownership | DOE CODE code-48776 | verified | |
| 2026-10-24 | datafed | "Never stores passwords" [KNOWN] | overview.rst | corrected | Not stated; retagged INFERRED |
| 2026-10-24 | datafed | Developing team | repo + docs + DOE CODE | unverifiable | |
| 2026-10-24 | cyberwheel | MIT, 2024 an individual developer (named in the LICENSE) | LICENSE | verified | |
| 2026-10-24 | cyberwheel | v2.0 multi-agent, multi-network sizes, FIREWHEEL | README | verified | |
| 2026-10-24 | cyberwheel | Python 3.10, Poetry, Graphviz, Gym/W&B/Dash | README | verified | |
| 2026-10-24 | cyberwheel | Tags, ~8 contributors, six ornl.gov contacts | GitHub API + README | verified | |
| 2026-10-24 | cyberwheel | Two 2024 papers | arXiv API + OSTI 2478356 | verified | ACM DOI 403 (publisher block) |
| 2026-10-24 | cyberwheel | ORNL ownership | DOE CODE code-134699 | verified | Possible LDRD funding (INFERRED) |
| 2026-10-24 | cyberwheel | Emulation "runs real VMs" [KNOWN] | README | corrected | Not stated; VMs retagged INFERRED |
| 2026-10-24 | cyberwheel | Owning division / continued development | repo + OSTI | unverifiable | |
| 2026-10-24 | scale (catalog) | Restricted-content screen | ornl.gov/scale; catalog row | verified | Overview facts only, no repo/download recorded; OK |
| 2026-10-24 | vera (catalog) | Restricted-content screen | vera.ornl.gov; OSTI 1546053 | verified | Public overview only; OK |
| 2026-10-24 | olm (catalog) | code.ornl.gov repo is public; BSD-3 license | code.ornl.gov GitLab API (visibility=public) + LICENSE file | verified | License file read directly: UT-Battelle 2024 BSD-style |
| 2026-10-24 | qiree (catalog) | License: OSTI says GPL-3.0, repo says Apache/MIT | repo COPYRIGHT + SPDX headers (clone) + OSTI code-149694 rights field | corrected | Trust repo: 73 files Apache-2.0 WITH LLVM-exception, 6 (Apache-2.0 OR MIT), 16 docs CC-BY-4.0, 0 GPL mentions; OSTI field likely a metadata error. LICENSE-APACHE/LICENSE-MIT files named in COPYRIGHT are missing from the repo |
| 2026-10-24 | daymet | Coverage 1980+/1950 PR, 1 km daily | daymet.ornl.gov, /overview | verified |  |
| 2026-10-24 | daymet | Research product of ORNL ESD, distributed by ORNL DAAC | daymet.ornl.gov | verified |  |
| 2026-10-24 | daymet | Funded by NASA ESDIS/TE and DOE BER; V3 2016-07-14, V4 2020-12-15 | daymet.ornl.gov, /overview | verified |  |
| 2026-10-24 | daymet | Inputs GHCN-Daily/NCEI, DEM; weighted interpolation | daymet.ornl.gov/overview | verified |  |
| 2026-10-24 | daymet | 2° tiles, netCDF/CF outputs, Single Pixel + REST access | daymet.ornl.gov, /overview | verified |  |
| 2026-10-24 | daymet | Helper repo custom UT-Battelle license | raw LICENSE.md | verified |  |
| 2026-10-24 | daymet | Helper repo languages and ~6 contributors | GitHub API | verified |  |
| 2026-10-24 | daymet | TESViS lists Daymet subsets | modis.ornl.gov/documentation.html | verified |  |
| 2026-10-24 | daymet | Generator code public? | OSTI records API, GitHub | unverifiable | no public code found |
| 2026-10-24 | e3sm-elm | ORNL among eight founding ACME labs | e3sm.org/about/organization/phase-1/ | verified |  |
| 2026-10-24 | e3sm-elm | ORNL listed in e3sm.org lab footer | e3sm.org homepage | verified | links ornl.gov |
| 2026-10-24 | e3sm-elm | km-scale ELM paper ANL+ORNL, DOI 10.1177/10943420261446003 | OSTI 3649369 | verified |  |
| 2026-10-24 | e3sm-elm | 1 km ELM input datasets V1/V2 under OLCF DOI | OSTI 3005830, 3364821 | corrected | added V1 DOI |
| 2026-10-24 | e3sm-elm | ELM UQ paper BNL + ORNL ARM Data Center | OSTI 3025805 | verified |  |
| 2026-10-24 | e3sm-elm | BSD-3, copyright UChicago Argonne | raw LICENSE | verified |  |
| 2026-10-24 | e3sm-elm | components/elm and src folder lists, emi+fates | GitHub contents API | verified |  |
| 2026-10-24 | e3sm-elm | Docs placeholder intro, coupler-bypass mode | docs/index.md | verified |  |
| 2026-10-24 | e3sm-elm | 79% Fortran, 10% C++ | GitHub languages API | verified |  |
| 2026-10-24 | e3sm-elm | Who leads land group / ORNL share | e3sm.org, OSTI | unverifiable |  |
| 2026-10-24 | myna | BSD-3, copyright 2024 ORNL | LICENSE.md | verified |  |
| 2026-10-24 | myna | Releases 1.0.0/1.1.0, created 2024-02-23, ~9 contributors | GitHub API | verified |  |
| 2026-10-24 | myna | Python 3.10+, not on PyPI, uv/pip | README | verified |  |
| 2026-10-24 | myna | config/run/sync workflow | ARCHITECTURE.md | verified |  |
| 2026-10-24 | myna | Wrapped apps list | src/myna/application | verified |  |
| 2026-10-24 | myna | 1.1.0 DB types and 3.9 baseline | CHANGELOG.md | verified |  |
| 2026-10-24 | myna | Paper, 7 authors, DOI | CITATION.bib | verified |  |
| 2026-10-24 | myna | MDF = Manufacturing Demonstration Facility | ornl.gov/facility/mdf | corrected | INFERRED to KNOWN; added code-141169 |
| 2026-10-24 | myna | ~20 example cases, AGENTS.md | GitHub contents API | verified | 21 cases |
| 2026-10-24 | tesvis-modis | Name, ORNL DAAC with LP DAAC | modis.ornl.gov | verified |  |
| 2026-10-24 | tesvis-modis | Global Subsets, Fixed Sites, REST, AppEEARS pointer | modis.ornl.gov | verified |  |
| 2026-10-24 | tesvis-modis | Product families incl. VIIRS, SMAP, ECOSTRESS, GEDI, SIF, ICESat-2 | documentation.html | verified |  |
| 2026-10-24 | tesvis-modis | REST pattern, ten-date limit, CSV/JSON, email orders | modis_webservice.html | verified |  |
| 2026-10-24 | tesvis-modis | Citation DOI 10.3334/ORNLDAAC/1600 | modis_webservice.html | verified |  |
| 2026-10-24 | tesvis-modis | GET endpoints need no key | GET /rst/api/v1/products (HTTP 200) | corrected | INFERRED to KNOWN |
| 2026-10-24 | tesvis-modis | Source repo / stack | web search of repos | unverifiable |  |
| 2026-10-24 | data-workflow | BSD-3, copyright 2022 ORNL | LICENSE (next) | verified |  |
| 2026-10-24 | data-workflow | Releases 3.10-3.12 with dates, created 2012-08-15 | GitHub API | verified |  |
| 2026-10-24 | data-workflow | Django, ActiveMQ/STOMP, PostgreSQL 17+/MySQL, badge 5504 | README.rst | verified |  |
| 2026-10-24 | data-workflow | WebMon at SNS and HFIR, DASMON PVs | docs/glossary.rst | verified |  |
| 2026-10-24 | data-workflow | monitor.sns.gov, sibling repos | docs/developer/index.rst | verified |  |
| 2026-10-24 | data-workflow | Languages, ~35 contributors | GitHub API | verified |  |
| 2026-10-24 | data-workflow | Dockerfiles, nginx, pixi | GitHub contents API | verified |  |
| 2026-10-24 | data-workflow | Mantid used in reduction | neutrons/post_processing_agent README | corrected | INFERRED to KNOWN |
| 2026-10-24 | data-workflow | Owning ORNL division | OSTI, docs | unverifiable | no DOE CODE record |
| 2026-10-24 | olcf-test-harness | UT-Battelle BSD-style with cost-recovery clause | LICENSE (devel) | verified |  |
| 2026-10-24 | olcf-test-harness | Releases v2.1-v3.2 with dates | GitHub API | verified |  |
| 2026-10-24 | olcf-test-harness | DOI 10.11578/dc.20250328.1, ORNL-CODE-153320 | README, OSTI code-153320 | verified |  |
| 2026-10-24 | olcf-test-harness | OSTI research org ORNL, NCCS | OSTI code-153320 | corrected | NCCS is in developer affiliations, not research_orgs |
| 2026-10-24 | olcf-test-harness | v3.2 last compatible before breaking v4.0 | README | corrected | README says last 2.x-compatible; no v4.0 mention |
| 2026-10-24 | olcf-test-harness | Schedulers and machine configs | GitHub contents API | verified |  |
| 2026-10-24 | olcf-test-harness | Templating framework; NCCS_Test_Harness 2016 header | doc-sphinx overview.rst, index.rst | verified |  |
| 2026-10-24 | olcf-test-harness | rgt.inp, --mode, output_check, Run_Archive, LAMMPS | README | verified |  |
| 2026-10-24 | olcf-test-harness | ~95% Python, ~28 contributors | GitHub API | verified |  |
| 2026-10-24 | map.md #5,#31 | one developer (top contributor to HydraGNN, AdditiveFOAM and Myna) top contributor to HydraGNN, AdditiveFOAM (and Myna) | GitHub contributors API | verified | same team correctly INFERRED |
| 2026-10-24 | map.md #6 | one developer (top contributor to Xolotl and GridKit) top contributor to Xolotl and GridKit | GitHub contributors API | verified | split correct |
| 2026-10-24 | map.md #7 | one developer (top contributor to GridKit and ReSolve) top contributor to GridKit and ReSolve | GitHub contributors API | verified | split correct |
| 2026-10-24 | map.md #39,#40 | a QIR-EE and IRIS developer/a second QIR-EE and IRIS developer on QIR-EE+IRIS; a QIR-EE and TASMANIAN developer on QIR-EE+TASMANIAN | GitHub contributors API | verified | split correct |
| 2026-10-24 | map.md #65 | one developer (top contributor to KORC and Stellarator-Tools) top contributor to KORC and Stellarator-Tools | GitHub contributors API | verified | split correct |
| 2026-10-24 | map.md #52 | Thermochimica is a MOOSE contrib submodule | idaholab/moose .gitmodules | verified |  |
| 2026-10-24 | map.md #57 | Cyberwheel is test bed of LDRD project 11049 | OSTI 3025007 PDF | verified | cyberwheel.md retagged KNOWN |
| 2026-10-24 | cyberwheel | Emulation runs virtual machines | OSTI 3025007 PDF (Firewheel built on QEMU) | corrected | INFERRED to KNOWN |
| 2026-10-24 | map.md #59 | Vivaldi uses Gauntlet, source DOE CODE 157761 | OSTI code-157761; ORNL/vivaldi README | corrected | OSTI record doesn't name Vivaldi; Vivaldi README does |
| 2026-10-24 | map.md #61 | Stor4Build 'same research group' KNOWN | OSTI code-170060 | corrected | ORNL+NREL co-development KNOWN; same group should be INFERRED |
| 2026-10-24 | map.md #55 | OSTI 1340202 is a different GridKit, don't conflate | OSTI 1340202, code-152622 | corrected | contradicts #58 framing; same author, separate record, predecessor INFERRED |
| 2026-10-24 | scale | Developed by ORNL under NRC/DOE/NNSA contract, four areas | ornl.gov/scale (WebFetch) | verified |  |
| 2026-10-24 | scale | Four-volume 6.3 validation set | ornl.gov/scale; OSTI search | verified |  |
| 2026-10-24 | scale | Four vs five volumes | OSTI 2587031, 1902803, 1902818 | corrected | likely overview volume, INFERRED |
| 2026-10-24 | scale | KENO since 1960s | OSTI 2575336 | verified |  |
| 2026-10-24 | scale | Polaris-PARCS reactor physics | OSTI 2583839 | verified |  |
| 2026-10-24 | scale | Threads/OpenMP/MPI in SCALE-Shift | OSTI 3007184 | verified |  |
| 2026-10-24 | scale | ENDF/B-VII.1, prior 6.2.4 | OSTI 2587031 | verified |  |
| 2026-10-24 | scale | Non-LWR NRC models | OSTI 2572299, 2583965 | verified |  |
| 2026-10-24 | scale | License UNKNOWN | OSTI 2572299, 2583965 | corrected | licensed, not open source KNOWN; terms UNKNOWN |
| 2026-10-24 | scale | Owning division | ornl.gov/scale | unverifiable |  |
| 2026-10-24 | vera | CASL 2010, single-rod resolution | vera.ornl.gov (WebFetch) | verified |  |
| 2026-10-24 | vera | Physics areas, UQ, PWR validation, platforms | vera.ornl.gov | verified |  |
| 2026-10-24 | vera | CASL an Energy Innovation Hub [KNOWN: vera.ornl.gov] | vera.ornl.gov | corrected | not on page, INFERRED |
| 2026-10-24 | vera | Site has a users group | vera.ornl.gov | unverifiable | not in homepage text |
| 2026-10-24 | vera | MPACT BWR cusping | OSTI 3002716, 3027390 | verified |  |
| 2026-10-24 | vera | VERA+TRACE+BISON LOCA; ATF depletion | OSTI 3384956, 3403165 | verified |  |
| 2026-10-24 | vera | VERA Infrastructure record, ORNL | OSTI 1546053 | verified |  |
| 2026-10-24 | vera | CTF and Shift as components | OSTI 1546053 + search | unverifiable | stays INFERRED |
| 2026-10-24 | gitr | GPL-2.0 | LICENSE | verified |  |
| 2026-10-24 | gitr | Inputs, trace-impurity, operator loop, containers | README | verified |  |
| 2026-10-24 | gitr | CUDA on, OpenMP/MPI off by default | CMake/compile_time_options.cmake | verified |  |
| 2026-10-24 | gitr | 25 src files, 9 examples | GitHub contents API | verified |  |
| 2026-10-24 | gitr | Languages, ~36 contributors | GitHub API | verified |  |
| 2026-10-24 | gitr | Release list | GitHub releases API | corrected | added 1.0 (2019-02-25) |
| 2026-10-24 | gitr | DIII-D helicon paper uses GITR? (UNKNOWN) | OSTI 3452355 | corrected | description names GITR, KNOWN |
| 2026-10-24 | gitr | STRIPE link to GITR (INFERRED) | OSTI 3013481 | corrected | description names GITR, KNOWN |
| 2026-10-24 | gitr | DOE CODE record / division | OSTI records API | unverifiable |  |
| 2026-10-24 | real-twin | Releases (API failed) | GitHub releases API; PyPI | corrected | 4 releases, PyPI 0.1.2 |
| 2026-10-24 | real-twin | func_lib stages a-h, datasets | GitHub contents API | verified |  |
| 2026-10-24 | real-twin | Platform-agnostic, SUMO/VISSIM/AIMSUN, calibration, AV | README | verified |  |
| 2026-10-24 | real-twin | Coverage 22%->38%, 90% goal | CHANGELOG.md | verified |  |
| 2026-10-24 | real-twin | VTO EEMS funding, ORNL research org, DOI | README; OSTI code-147051 | verified |  |
| 2026-10-24 | real-twin | GPL-3.0, Python 97.4, v0.1.2 | LICENSE; API; pyproject | verified |  |
| 2026-10-24 | real-twin | FIXS same org | GitHub API | verified |  |
| 2026-10-24 | gauntlet | MIT 2025 ORNL, dates, languages, no releases | LICENSE; GitHub API | verified |  |
| 2026-10-24 | gauntlet | 65 measures, 315-line script, deps, Python 3.10.15 | README; src | verified |  |
| 2026-10-24 | gauntlet | Buffers 50/100/250/500 m | README feature table | corrected | also 1000 m |
| 2026-10-24 | gauntlet | FEMA + FEMP sponsors, DOI | OSTI code-157761 | verified |  |
| 2026-10-24 | gauntlet | USA Structures paper and dataset | OSTI 3001779, 2587435 | verified |  |
| 2026-10-24 | gauntlet | Vivaldi uses Gauntlet | ORNL/vivaldi README | verified |  |
| 2026-10-24 | energyplus | License holders incl. ORNL, Gov rights | LICENSE.txt | verified |  |
| 2026-10-24 | energyplus | v26.2.0 and RCs, twice-yearly | GitHub releases API; README | verified |  |
| 2026-10-24 | energyplus | Testing, Decent CI, Unmet Hours, DOE site | README | verified |  |
| 2026-10-24 | energyplus | Languages, contributors, stars, created | GitHub API | verified |  |
| 2026-10-24 | energyplus | OSTI 1395245 ORNL research org | OSTI records API | verified |  |
| 2026-10-24 | energyplus | NatLabRockies = NREL | GitHub org API; nlr.gov | corrected | org is National Laboratory of the Rockies; NREL link INFERRED |
| 2026-10-24 | energyplus | ORNL's specific role | repo, OSTI | unverifiable |  |
| 2026-10-24 | scale | Sweep 2: license required, fifth volume, parallelism quotes | OSTI 2572299, 2587031, 3007184 (re-fetched) | verified | quotes added to brief |
| 2026-10-24 | scale | Shift is a Monte Carlo transport package (was INFERRED) | SCALE 6.3.3 manual CSAS-Shift 2.2.1 + OSTI 1237627 | corrected | retagged CORROBORATED |
| 2026-10-24 | map link 82 | Shift/Exnihilo used in SCALE via CSAS-Shift | https://scale-manual.ornl.gov/6.3.3/CSAS-Shift.html (HTTP 200) + OSTI 3007184 "SCALE-Shift Sequences" | verified | can be CORROBORATED; manual: "Shift is a massively parallel Monte Carlo radiation transport package in the Exnihilo radiation transport code suite" |
| 2026-10-24 | vera | Sweep 2: VERA Infrastructure (ORNL), MPACT, VERA+TRACE+BISON | OSTI 1546053, 3002716, 3384956, 3403165 (re-fetched) | verified | quotes added |
| 2026-10-24 | vera | Shift as VERA component | OSTI 1237627 | unverifiable | paper only says Shift was benchmarked on the "CASL VERA criticality test suite"; stays INFERRED, note added |
| 2026-10-24 | gitr | Sweep 2: purpose, trace assumption, GPL-2.0, releases, STRIPE/DIII-D links | README, GitHub API, OSTI 3013481, 3452355 | verified | two OSTI papers share the STRIPE group, so not CORROBORATED |
| 2026-10-24 | real-twin | Walkthrough said release history unknown | GitHub releases API (4 releases) | corrected | stale line fixed |
| 2026-10-24 | real-twin | "Real-Sim family" INFERRED | github.com/ORNL-Real-Sim | corrected | split: same org KNOWN, working together INFERRED |
| 2026-10-24 | real-twin | Sweep 2: EEMS114 funding, three simulators, ORNL research org | README Acknowledgement, OSTI code-147051 | verified | |
| 2026-10-24 | gauntlet | Walkthrough buffers 50-500 m | README feature table (1000 meter buffer rows present) | corrected | walkthrough now 50/100/250/500/1000 m |
| 2026-10-24 | gauntlet | 65 features | README + OSTI code-157761 + OSTI 3001779 (Scientific Data) | verified | CORROBORATED |
| 2026-10-24 | energyplus | "DOE's main open-source program" KNOWN | README, OSTI 1395245 | corrected | neither says main/flagship; retagged INFERRED |
| 2026-10-24 | energyplus | "not an ORNL-led project [KNOWN: LICENSE]" | LICENSE.txt | corrected | reworded to not ORNL-only (KNOWN), lead INFERRED |
| 2026-10-24 | energyplus | Sweep 2: purpose, cadence, release, license holders | README lines 7, 33; GitHub API; OSTI 1395245 | verified | purpose CORROBORATED (README + OSTI) |
| 2026-10-24 | map link 61 | NREL-led "per OSTI 1395245" | OSTI 1395245 | corrected | OSTI lists ORNL as only research org; does not support NREL-led. Flagged to the connections pass |
| 2026-10-24 | cyberwheel (deep dive) | Quote "autonomously deploy decoys in unseen network topologies that delay or deny adversarial actors" | OSTI 3025007 PDF p. 13 | verified | exact |
| 2026-10-24 | cyberwheel (deep dive) | Quote "modified version" of Firewheel, built on QEMU, >100,000 virtual nodes | OSTI 3025007 PDF p. 13 | verified | exact; what was modified is not stated |
| 2026-10-24 | cyberwheel (deep dive) | 11049 funding note on OSTI 2478356 or code-134699 | OSTI records API | unverifiable | neither record names 11049 or a contract; code-134699 sponsor is generic LDRD Program; 2478356 sponsor is USDOE |
| 2026-10-24 | map link 56 | Cyberwheel LDRD link CORROBORATED via CSET paper + shared authors | OSTI 2478356, code-134699 | corrected | shared authors prove team, not funding; LDRD funding CORROBORATED via report + DOE CODE sponsor field; 11049 number KNOWN single source. Flagged to the connections pass |
| 2026-10-24 | map link 108 | arXiv 2610.00590 runs Cyberwheel | https://arxiv.org/abs/2610.00590 (2026-09-30) abstract: "Using the high fidelity Cyberwheel environment" | verified | |
| 2026-10-24 | map link 108 | arXiv 2610.00557 evaluates in CybORG CAGE-4 and Cyberwheel | https://arxiv.org/abs/2610.00557 (2026-09-30) abstract: "in CybORG CAGE-4 and in Cyberwheel at two network scales" | verified | |
| 2026-10-24 | map link 108 | Entropy 2025 extends Cyberwheel | DOI 10.3390/e27060622 (Entropy, 2025-06-11) abstract: "the algorithm training environment Cyberwheel is extended by adding new fine-grained defense mechanisms" | verified | author affiliation not checked |
| 2026-10-24 | landscan | CC BY 4.0 | landscan.ornl.gov public page bundle, Licensing: "These datasets are offered under the Creative Commons Attribution 4.0 International License." | verified | /licensing returns 403 to fetches, so the bundle text was used |
| 2026-10-24 | landscan | HD and USA are legacy | landscan.ornl.gov Historical Datasets: "LandScan HD and LandScan USA are legacy datasets that are no longer actively updated" | corrected | citation moved from the discovery notes to the primary page |
| 2026-10-24 | landscan | R&D 100 award | landscan.ornl.gov: "R&D100-winning population data platform" | verified | |
| 2026-10-24 | landscan | R&D 100 award year | landscan.ornl.gov | unverifiable | not stated on the site |
| 2026-10-24 | landscan | LSG 2026: 30 arc-sec, ~100 predictions per country, DOI | OSTI 17076155 (Dataset, 2026-07-01) | verified | |
| 2026-10-24 | landscan | Unknown line on Mosaic and USA day/night | brief internal | corrected | split into a clean UNKNOWN line and an INFERRED line |
| 2026-10-24 | shift-exnihilo | status active | OSTI 3013520 | corrected | KNOWN to INFERRED |
| 2026-10-24 | shift-exnihilo | not openly distributed | SCALE manual | corrected | ships-in-SCALE stays KNOWN; not openly distributed is INFERRED |
| 2026-10-24 | shift-exnihilo | CADIS / FW-CADIS | OSTI 1237627 + OSTI 3013520 abstracts | corrected | KNOWN to CORROBORATED |
| 2026-10-24 | shift-exnihilo | under 2 min on 20 Frontier nodes; 9-11x per GCD on MI250X | OSTI 3013520 abstract | verified | |
| 2026-10-24 | shift-exnihilo | Radiation Transport Group | OSTI 1237627 full text, Introduction: "developed and maintained at Oak Ridge National Laboratory (ORNL) by the Radiation Transport Group" | verified | read directly; single source; development began 2010 |
| 2026-10-24 | shift-exnihilo | 2015 ANS paper page | https://www.ornl.gov/publication/shift-massively-parallel-monte-carlo-radiation-transport-package | verified | Trans. ANS, April 2015, Nashville |
| 2026-10-24 | shift-exnihilo | VERA component | OSTI 1237627 | corrected | caveat added: only a benchmark-suite link |
| 2026-10-24 | fixs | MIT, 2023 UT-Battelle, push 2026-10-23, languages | GitHub API + LICENSE | verified | |
| 2026-10-24 | fixs | ORNL leads; UGA and UTD team; UGA maintains; EEMS core tool | README: "Real-Sim Project Lead: Oak Ridge National Lab" | verified | DOE CODE 110562 sponsor VTO |
| 2026-10-24 | fixs | ProprietaryFiles is private and not MIT | README License section | verified | not opened |
| 2026-10-24 | fixs | tool versions; one-step SUMO delay | README; doc/FIXS_message_flow.md | verified | |
| 2026-10-24 | fixs | release history | GitHub releases API | corrected | added "stable" tag 2026-09-27 and v0.10.0-alpha; 9 releases |
| 2026-10-24 | autobem | walkthrough present (rule 12) | brief | corrected | walkthrough added |
| 2026-10-24 | autobem | status active [KNOWN] | DOE CODE 115947 + papers | corrected | set to unknown to match map.md |
| 2026-10-24 | autobem | 122.9M buildings, 97.8% | OSTI 3740812 + Constellation DOI 10.13139/ORNLNCCS/1774134 | verified | CORROBORATED |
| 2026-10-24 | autobem | 1M/hour, 178,000 buildings validated, 3 devs, 2023-11-15 | DOE CODE 115947 | verified | |
| 2026-10-24 | autobem | Phoenix ~722,000 buildings | OSTI 17315517 abstract (722,237) | verified | |
| 2026-10-24 | autobem | MAv1 "being released"; compute | Constellation page: released 2021-04-14; "used resources of the Argonne Leadership Computing Facility" | corrected | public since 2021; compute was ALCF |
| 2026-10-24 | autobem | data-center paper uses AutoBEM | OSTI 3384902 | unverifiable | no abstract |
| 2026-10-24 | situ | OSTI record facts | OSTI 1232450 | verified | sponsor field "u" |
| 2026-10-24 | situ | "watches network activity" | OSTI 1232450: "scores events in real-time based on probabilistic models" | corrected | network narrowed to INFERRED |
| 2026-10-24 | situ | walkthrough (rule 12) | brief | corrected | added |
| 2026-10-24 | roof-savings-calculator | OSTI record facts | OSTI 1238771 | verified | |
| 2026-10-24 | roof-savings-calculator | "attic ventilation" input | OSTI 1238771: "above-sheathing ventilation" | corrected | |
| 2026-10-24 | roof-savings-calculator | roofcalc.com status | single fetch 2026-10-24 | corrected | reworded to "unreachable on 2026-10-24" |
| 2026-10-24 | roof-savings-calculator | first developed 2010, 200+ locations | OSTI 1651267 abstract | verified | |
| 2026-10-24 | roof-savings-calculator | walkthrough (rule 12) | brief | corrected | added |
| 2026-10-24 | cyberwheel | claim-boundary row 7: "modified version" in v2.0 notes | GitHub v2.0 release notes: "now supports emulation with FIREWHEEL"; OSTI 3025007 p.13 | corrected | quote is from the LDRD report only |
| 2026-10-24 | cyberwheel | last commit 2025-08-26; first commit 2024-01-02; created 2024-07-08 | GitHub API | verified | |
| 2026-10-24 | cyberwheel | 11049 in FY 2025 Completed Projects report; "over 100,000 virtual nodes" | OSTI 3025007 PDF p.13 | verified | single source |
| 2026-10-24 | cyberwheel | v1.1.0 "inactive blue agent"; Poetry fallback; ART in code | GitHub release v1.1.0, README, red_agents/art_agent.py | verified | |
| 2026-10-24 | cyberwheel | ISDFS 2025 paper details | Crossref DOI 10.1109/ISDFS65363.2025.11012027 (2025-04-24) | verified | describes only |
| 2026-10-24 | cyberwheel | OSTI 3827147 as a successor | OSTI record (2026-09-01) | unverifiable | no source ties it to Cyberwheel |
| 2026-10-24 | live-data-server | license, dates, languages, contributors, releases | GitHub API + LICENSE on next | verified | |
| 2026-10-24 | live-data-server | README tagline, credentials check, HTML-only, 3-year expiry, instruments, docs links | raw files on next (views.py, models.py, settings.py, instruments.py); RTD 200 | verified | |
| 2026-10-24 | live-data-server | "public URL it runs at" listed as UNKNOWN | RULES 16 | corrected | out of scope, not to be researched |
| 2026-10-24 | post-processing-agent | MIT NScD, ORNL copyright in calvera_processor.py, created, push, contributors | GitHub API + raw files on main | verified | |
| 2026-10-24 | post-processing-agent | four tasks, per-instrument queues, heartbeats, processors, systemd file | README_developer.md, contents API | verified | |
| 2026-10-24 | post-processing-agent | 96% Python | languages API: 264,303 of 271,647 bytes | corrected | 97% |
| 2026-10-24 | post-processing-agent | releases v4.3.0 to v4.6.0 | releases API | corrected | 21 releases |
| 2026-10-24 | post-processing-agent | defaults 60 min / 70% | README example config | corrected | values KNOWN; "default" INFERRED |
| 2026-10-24 | post-processing-agent | deployment size UNKNOWN | RULES 16 | corrected | out of scope |
| 2026-10-24 | signals/hydragnn | PyPI 3.0, 26 downloads last month; no conda-forge or Spack | pypi.org JSON, pypistats.org recent, conda-forge and spack-packages 404 (path checked with py_numpy 200) | verified | download counts are not user counts |
| 2026-10-24 | signals/datafed | PyPI 5.1.0, 43 downloads last month; no conda-forge or Spack | same as above | verified | |
| 2026-10-24 | signals/cyberwheel | not on PyPI, conda-forge or Spack | PyPI 404, feedstock 404, spack-packages 404 | verified | |
| 2026-10-24 | signals/cyberwheel | "live networks" aim | OSTI 3025007 p.13: "autonomous defense agents deployable in live" networks | verified | source is the LDRD report, not the README |
| 2026-10-24 | hydragnn | stars/forks imply outside user base | signals/hydragnn.md (OpenAlex citing authors, GitHub dependents) | corrected | line already reworded by a teammate; I fixed "2 PyPI dependents" to "2 GitHub dependents are PyPI mirror repos" |
| 2026-10-24 | adamantine | License Apache-2.0 with LLVM exceptions, relicensed from BSD-3 in 1.1 | LICENSE line 2; PR 346 title; CHANGELOG 1.1 | verified | CITATION.cff still BSD-3; GitHub API NOASSERTION |
| 2026-10-24 | adamantine | ORNL research org; LDRD and EERE sponsors (rule 13 scope) | OSTI API 2472702 | verified | |
| 2026-10-24 | adamantine | 1.1 release date conflict | GitHub release object 2026-01-23; release/1.1 branch commits Jan 2026; CHANGELOG last edited 2026-01-23 | corrected | UNKNOWN changed to CORROBORATED 2026; CHANGELOG 2025 is an INFERRED typo |
| 2026-10-24 | adamantine | Contributors 11 incl. anonymous, 10 accounts; releases v1.0 and v1.1 | GitHub contributors Link headers, releases API | verified | |
| 2026-10-24 | adamantine | README "thermomechanical code for additive manufacturing", Ensemble Kalman filter | README.md raw | verified | |
| 2026-10-24 | adamantine | Project site and tutorials repo exist | HTTP 200 on both | verified | |
| 2026-10-24 | signals/hydragnn | Job trace from a LinkedIn post | linkedin.com/posts/<personal account> | corrected | rule 16: personal social media is out of scope; link removed, finding marked out of scope until an official ORNL job posting is found |
| 2026-10-24 | oncat | Overview quotes (SNS/HFIR catalog, teams browse their data, DOIs, API) | oncat.ornl.gov rendered public page | verified | no API call, no login page |
| 2026-10-24 | oncat | pyoncat: GPL v3 LICENSE, blank PyPI license, 8 versions 1.6.2 (2023-09-05) to 2.7 (2026-09-24), Python 3.9+, author "ONCat Support" | PyPI JSON; pyoncat-2.7 sdist | verified | files read, not run |
| 2026-10-24 | oncat | Client classes, ReductionFileBuilder methods, login/logout methods, module sizes | pyoncat-2.7 sdist source | verified | |
| 2026-10-24 | oncat | Release notes URL returned 404 | guessed path | corrected | rule 16 (editorial decision): reworded to "not linked from public pages" |
| 2026-10-24 | signals/hydragnn | Grid expansion: OSTI 3377970 OE + ASCR, 3239722 | OSTI API | verified | |
| 2026-10-24 | signals/hydragnn | AMD as research org | OSTI code-180990 | verified | |
| 2026-10-24 | signals/hydragnn | ornl.gov says development started 2022; AI Initiative funding | ornl.gov news, Jan 28 2025 | verified | |
| 2026-10-24 | signals/hydragnn | CI is CPU-only; tags v4.0 and v5.0; PyPI 3.0 | CI.yml raw; tags.atom; PyPI JSON | verified | |
| 2026-10-24 | signals/hydragnn | Commit author metadata from lab systems | git log | corrected | out of scope (rule 16, infrastructure); row removed |
| 2026-10-24 | signals/datafed | Org unit CSMD + NCCS, OLCF | TM-166131 PDF; OSTI 3412938 | verified | supports the catalog org_unit edit |
| 2026-10-24 | signals/datafed | Group name | ornl.gov staff page | verified | group name only |
| 2026-10-24 | signals/datafed | Sponsors ASCR, USDOE, BER + ASCR | OSTI 1820762, code-48776, 3412938 | verified | |
| 2026-10-24 | signals/datafed | Release dates | tags.atom; release pages | corrected | dates are tag commit dates; release objects 2025-12-09 and 2026-03-02 added |
| 2026-10-24 | signals/cyberwheel | Private classifier, no CI, tag dates, LDRD sponsor | pyproject.toml; tree 404s; tags.atom; OSTI code-134699, 2478356 | verified | |
| 2026-10-24 | tasmanian | License BSD-3, individual copyright, UT-Battelle disclaimer, NOASSERTION | LICENSE raw lines 3, 31; GitHub API | verified | |
| 2026-10-24 | tasmanian | Rule 13 ORNL tie | github.com/ORNL; DOE CODE code-6305 / OSTI 1231809 | corrected | added second source; CORROBORATED |
| 2026-10-24 | tasmanian | Status, v8.2 2025-12-09, yearly releases, 12/8 contributors, languages | GitHub API | verified | |
| 2026-10-24 | tasmanian | GPU backends CUDA, HIP, DPC++, MAGMA "stable"; README name and DREAM | CMakeLists.txt lines 16-19, 80-81; README | verified | |
| 2026-10-24 | xolotl | License BSD-3, six copyright holders with UT-Battelle first | LICENSE raw lines 1-8 | verified | |
| 2026-10-24 | xolotl | ORNL as research org UNKNOWN | OSTI 1513390 (ORNL, ASCR; abstract "Our cluster dynamics model, Xolotl") | corrected | now KNOWN; rule 13 CORROBORATED |
| 2026-10-24 | xolotl | Languages Jupyter ~67%, C++ ~30% | GitHub languages API (66.9 / 30.1) | verified | |
| 2026-10-24 | xolotl | 14 releases since 2021, v3.4.0 2026-09-03, 27/9 contributors, last push 2026-10-21 | GitHub API | verified | |
| 2026-10-24 | xolotl | README "under development", SciDAC, ITER, fission; C++20, Kokkos, PETSc | README; CMakeLists line 13 | verified | |
| 2026-10-24 | flowcept | MIT, ORNL copyright, dates, v1.0.3, 19/11 contributors, languages | LICENSE raw; GitHub API | verified | |
| 2026-10-24 | flowcept | README provenance quote; flowcept.org and readthedocs resolve | README raw; HTTP 200 | verified | |
| 2026-10-24 | flowcept | ORNL tie (rule 13) | LICENSE + LDRD report OSTI 3025007 | verified | CORROBORATED |
| 2026-10-24 | iris | BSD-3, UT-Battelle copyright, dates, releases, 12/9 contributors, languages incl. Julia/Rust/Fortran | LICENSE raw; GitHub API | verified | |
| 2026-10-24 | iris | README quote; official site resolves; DeviceQIREE.cpp exists | README raw; HTTP 200 | verified | |
| 2026-10-24 | iris | ORNL tie (rule 13) | LICENSE + OSTI 3018176 (Q-IRIS, ORNL) | verified | CORROBORATED; SLAC code-75005 UNRELATED |
| 2026-10-24 | qiree | ORNL research org; released to DOE CODE 2025-01-15 | OSTI API code-149694 | verified | id is code-149694 |
| 2026-10-24 | qiree | License dual Apache-2.0+LLVM / MIT; contributors retain copyright; UT-Battelle file headers; license files missing | COPYRIGHT, Executor.cc raw; 404 on LICENSE-APACHE, LICENSE-MIT, LICENSE | verified | |
| 2026-10-24 | qiree | Rule 13 second source | OSTI 3001783 (ORNL) | verified | CORROBORATED |
| 2026-10-24 | qiree | 8 contributors, created 2024-06-20, languages | GitHub API | verified | |
| 2026-10-24 | signals/cyberwheel | Discovery-pass commit counts (352 default, 398 all, 246 in 2024, 152 in 2025, 0 after 2025-08-26, 9 authors) | fresh clone of ORNL/cyberwheel, author dates | verified | by committer date the year split is 243/155; totals identical |
| 2026-10-24 | hecbench | LICENSE names Argonne 2020 and ORNL 2020-; BSD-3 | fresh clone of ORNL/HeCBench; GitHub API | verified | rule 13 stays KNOWN (both sources are GitHub) |
| 2026-10-24 | hecbench | 555 benchmarks; 554 CUDA, 551 HIP, 542 SYCL, 361 OpenMP folders | fresh clone src/ | verified | |
| 2026-10-24 | hecbench | Last commit 2026-10-22, no releases, no CI, 113/29 contributors, languages | clone; GitHub API | verified | |
| 2026-10-24 | hecbench | OSTI record | OSTI q=HeCBench | verified | no software record; ORNL and LLNL papers use it (usage only) |
| 2026-10-24 | hecbench | Repo identity | github.com/ORNL/HeCBench is a fork (API parent ORNL/HeCBench) | verified | namesake guard; cite ORNL repo |
| 2026-10-24 | flowcept | Sweep 2: reread brief plus refetch; ORNL tie via LDRD report | repo, OSTI 3025007 (re-fetched) | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | iris | Sweep 2: reread brief plus refetch; Q-IRIS second source | repo, OSTI 3018176 (re-fetched) | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable; SLAC new-iris UNRELATED |
| 2026-10-24 | tasmanian | Sweep 2: reread brief plus refetch; DOE CODE record added | repo, DOE CODE code-6305 / OSTI 1231809 | verified | 4 checks: 3 verified, 1 corrected (rule 13 now CORROBORATED), 0 unverifiable |
| 2026-10-24 | xolotl | Sweep 2: reread brief plus refetch; ORNL research org | repo, OSTI 1513390 | verified | 5 checks: 4 verified, 1 corrected (scope tag UNKNOWN to CORROBORATED), 0 unverifiable |
| 2026-10-24 | qiree | Sweep 2: reread brief plus refetch; DOE CODE record | repo, DOE CODE code-149694, OSTI 3001783 | verified | 4 checks: 4 verified, 0 corrected, 0 unverifiable; license files 404 noted as gap |
| 2026-10-24 | hecbench | Sweep 2: fresh clone of ORNL/HeCBench plus API and OSTI refetch | clone, GitHub API, OSTI search | verified | 5 checks: 5 verified, 0 corrected, 0 unverifiable; rule 13 stays KNOWN |
| 2026-10-24 | xacc | DOE CODE code-5041 / OSTI 1339995 name ORNL research org | OSTI API (both records) | corrected | citation moved from catalog row to OSTI; rule 13 CORROBORATED holds |
| 2026-10-24 | xacc | NOTICE dual license, UT-Battelle copyright; API BSD-3 | raw NOTICE; GitHub API | verified | |
| 2026-10-24 | xacc | Status unknown: master 2023-08-01, xacc-devel 2023-03-02, push 2024-08-13, no releases/tags, VERSION 0.1.16 | commit atom feeds; GitHub API; raw VERSION | verified | push cause not traced |
| 2026-10-24 | xacc | Contributors 30 with anon | GitHub API | verified | |
| 2026-10-24 | xacc | Sweep 2: refetch of OSTI, NOTICE, API, feeds | as above | verified | 4 checks: 3 verified, 1 corrected, 0 unverifiable |
| 2026-10-24 | cabana | Rule 13: ORNL named CoPA lab; DOE CODE code-45702 ORNL research org | raw README lines 15-18; OSTI API | verified | multi-lab, ECP-copa owner |
| 2026-10-24 | cabana | BSD-3 "the Cabana authors", NOASSERTION, 9 releases, 0.8.0 2026-05-29, last commit 2026-09-16, 43 contributors | raw LICENSE; API; master atom | verified | |
| 2026-10-24 | cabana | Sweep 2: refetch README, LICENSE, OSTI, API, feed | as above | verified | 2 checks: 2 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | exago | LICENSE UT-Battelle 2026 plus Battelle v1.6.0; OSTI code-176348 ORNL; pnnl/ExaGO archived | raw LICENSE; OSTI API; GitHub API | verified | |
| 2026-10-24 | exago | Releases, contributors 38, languages | GitHub API | verified | |
| 2026-10-24 | exago | Last commit 2026-10-19 | develop atom feed 2026-10-20T00:05Z | corrected | time zone labeled (ET and UTC) |
| 2026-10-24 | exago | AgentiGrid labeled experimental | CHANGELOG 2.1 line 17; agentigrid README | verified | label only in CHANGELOG |
| 2026-10-24 | exago | Sweep 2: refetch | as above | verified | 4 checks: 3 verified, 1 corrected, 0 unverifiable |
| 2026-10-24 | zambeze | MIT ORNL copyright, pyproject 0.2, PyPI 0.1, last commit 2024-09-13, 11/8 contributors | fresh clone; PyPI JSON; atom feed; API | verified | catalog's 2 contributors is wrong (flagged in the reading pass) |
| 2026-10-24 | zambeze | Flowcept hook in message_handler.py 70-77 | fresh clone | corrected | real path src/zambeze/orchestration/agent/message_handler.py lines 69-76 |
| 2026-10-24 | zambeze | Rule 13 via OSTI 2483434 | OSTI API (abstract names Zambeze, ORNL research org) | corrected | citation moved from the discovery-pass check to OSTI; 2477506 doesn't name Zambeze |
| 2026-10-24 | zambeze | Sweep 2: refetch | as above | verified | 3 checks: 1 verified, 2 corrected, 0 unverifiable |
| 2026-10-24 | matris | LICENSE UT-Battelle 2025, BSD-3; OSTI 2441045 and 2439841 ORNL, titled MatRIS | fresh clone; API; OSTI API | verified | rule 13 CORROBORATED |
| 2026-10-24 | matris | Last commit 2025-10-23, 0 tags/releases, CHANGELOG 1.0.0 2025-07-21, "proof of concept" | fresh clone | verified | status call left as an editorial decision |
| 2026-10-24 | matris | Contributors 8 with anon / 5 accounts | GitHub API Link headers | verified | room message said 2; brief already says 5 |
| 2026-10-24 | matris | CMake links iris | src/CMakeLists.txt lines 7-10, 27 | verified | |
| 2026-10-24 | matris | Sweep 2: clone plus refetch | as above | verified | 4 checks: 4 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | exago (signals) | 2025 9 commits/5 authors, 2026 255/24 (git log --all) | fresh clone of ORNL/ExaGO | verified | default branch only: 47/10 in 2026; note added |
| 2026-10-24 | matris (signals) | 4 commits in 2025; history starts 2022 | fresh full clone | verified | 247/181/133/4 for 2022-2025 |
| 2026-10-24 | zambeze/flowcept (map 114) | Current Flowcept lacks ZambezeInterceptor | fresh clone of ORNL/flowcept src | verified | no class or reference to ZambezeInterceptor in src; "zambeze" only in settings and vocabulary |
| 2026-10-24 | gridkit | License, tags v0.0.7/v0.1.0/v0.2.0, last commit 2026-10-23, CMake/C++20, options, CI, cases | fresh clone of ORNL/GridKit | verified | |
| 2026-10-24 | gridkit | Contributors 22 with anon / 17 accounts | GitHub contributors Link header | verified | |
| 2026-10-24 | gridkit | Rule 13: DOE CODE code-152622 lists ORNL | OSTI API code-152622 | verified | 2025-03-14, AC05-00OR22725 |
| 2026-10-24 | gridkit | `Experimental` is a model family under GridKit/Model | fresh clone, examples/README.md | corrected | it's an examples folder only |
| 2026-10-24 | gridkit | Sweep 2: rewrite re-checked | as above | verified | 4 checks: 3 verified, 1 corrected, 0 unverifiable |
| 2026-10-24 | exatn | License, dates, 1,202 commits, 12 branches, 0 tags, layout, CI, build reqs | fresh clone of ORNL-QCI/exatn, README | verified | 11 distinct author names vs 12 API entries noted |
| 2026-10-24 | exatn | Contributors 12 with anon / 2 accounts | GitHub contributors Link header | verified | |
| 2026-10-24 | exatn | Rule 13: DOE CODE code-45739 lists ORNL | OSTI API code-45739 | verified | 2018-10-01, AC05-00OR22725 |
| 2026-10-24 | exatn | Sweep 2: brief re-checked | as above | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | zambeze (batch 09 Flowcept note) | Current Flowcept (c000b10, 2026-07-20 UTC) lacks ZambezeInterceptor and FlowceptConsumerAPI; only leftover names | fresh clone of ORNL/flowcept | verified | vocabulary.py:15, settings_factory.py:45, mqtt_interceptor.py docstrings, sample_settings.yaml all confirmed |
| 2026-10-24 | gridkit (signals) | Commits per year 2017-2026 (git log --all) | fresh clone of ORNL/GridKit | verified | authors by name 3/19/21 vs signals 3/21/25 (likely by email); note added |
| 2026-10-24 | resolve | License, tags, dates, 283 commits by year, CMake 3.22, deps, workflows, HyKKT wording | fresh clone of ORNL/ReSolve, README | verified | |
| 2026-10-24 | resolve | Contributors 19 with anon / 15 accounts | GitHub contributors Link header | verified | |
| 2026-10-24 | resolve | Rule 13: DOE CODE code-114681 lists ORNL | OSTI API code-114681 | verified | 2023-10-16, AC05-00OR22725 |
| 2026-10-24 | resolve | Sweep 2: brief checked | as above | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | 3dthesis | License, tags, dates, 119 commits by year, examples, Stork mode, README quotes | fresh clone of ORNL-MDF/3DThesis, README | verified | |
| 2026-10-24 | 3dthesis | Contributors 5 / 5 | GitHub contributors Link header | verified | |
| 2026-10-24 | 3dthesis | Rule 13: DOE CODE code-26241 lists ORNL | OSTI API code-26241 | verified | 2018-12-21, DOI 10.11578/dc.20200909.3 |
| 2026-10-24 | 3dthesis | Sweep 2: brief checked | as above | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | finch | License, tags, dates, 192 commits by year, README deps, CI, latest commit message | fresh clone of ORNL-MDF/Finch, README | verified | |
| 2026-10-24 | finch | Contributors 4 with anon / 3 accounts | GitHub contributors Link header | verified | |
| 2026-10-24 | finch | Rule 13 CORROBORATED on LICENSE alone | OSTI API code-122647 | corrected | one source isn't CORROBORATED; added DOE CODE code-122647 (ORNL, 2024-02-23) as the second |
| 2026-10-24 | finch | Sweep 2: brief checked | as above | verified | 3 checks: 2 verified, 1 corrected, 0 unverifiable |
| 2026-10-24 | additivefoam | License lines, README scope quote, build needs, tags, dates, 68 commits by year, CI | fresh clone of ORNL/AdditiveFOAM, README | verified | |
| 2026-10-24 | additivefoam | Contributors 6 with anon / 5 accounts | GitHub contributors Link header | verified | |
| 2026-10-24 | additivefoam | Rule 13: DOE CODE code-108345 lists ORNL | OSTI API code-108345 | verified | 2023-06-13, sponsors SC and NNSA |
| 2026-10-24 | additivefoam | Sweep 2: brief checked | as above | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | tnqvm | No LICENSE, README BSD-3, header copyright, VERSION 0.1.9, no tags, 636 commits by year, dates, CI files | fresh clone of ORNL-QCI/tnqvm | verified | |
| 2026-10-24 | tnqvm | Contributors 11 with anon / 5 accounts | GitHub contributors Link header | verified | |
| 2026-10-24 | tnqvm | Rule 13 OSTI sources (were not re-fetched) | OSTI API 2583844, 2251617 | verified | both ORNL; 2251617 is a conference paper; citation updated |
| 2026-10-24 | tnqvm | Sweep 2: brief checked | as above | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | gauntlet (signals) | 6 commits 2025-07-09 to 2025-07-18, no tags or CI; DOE CODE code-157761 ORNL with FEMA and FEMP sponsors | fresh clone of ORNL/gauntlet; OSTI API code-157761 | verified | |
| 2026-10-24 | mantid (signals) | 2014 Mantid paper has 1,807 citing works, 696 with an ORNL author | OpenAlex works W2036295204, cites filter | verified | total 1,807 matches exactly; ORNL subset came out 689 using ORNL's ROR id, a small difference from filter choice or index drift; doesn't change the "mostly outside" reading |
| 2026-10-24 | korc | License, dates, 975 commits by year, tags, workflows, README build | fresh clone of ORNL-Fusion/KORC | verified | |
| 2026-10-24 | korc | Contributors 8 with anon / 5 accounts | GitHub contributors Link header | verified | |
| 2026-10-24 | korc | Rule 13 CORROBORATED on LICENSE alone | OSTI API 1870235, 2586907 | corrected | added OSTI 1870235 (ORNL research org, abstract names KORC) as second source |
| 2026-10-24 | korc | Docs link http://ornl-fusion.github.io/KORC | curl | corrected | http form didn't respond; https form returns 200 |
| 2026-10-24 | korc | Sweep 2: brief checked | as above | verified | 4 checks: 2 verified, 2 corrected, 0 unverifiable |
| 2026-10-24 | snapred | License, branch, dates, 889 commits, tags, workflows, Python 3.10+ | fresh clone of neutrons/SNAPRed | verified | per-year counts off by one at year edges (time zone) |
| 2026-10-24 | snapred | Contributors 20 with anon / 14 accounts | GitHub contributors Link header | verified | |
| 2026-10-24 | snapred | Rule 13: OSTI 3012509 lists ORNL | OSTI API 3012509 | verified | |
| 2026-10-24 | snapred | Sweep 2: brief checked | as above | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | pyrs | License, branch, dates, 3,332 commits, tags, pyproject HB2B and Python 3.12+, workflows | fresh clone of neutrons/PyRS | verified | per-year counts off by one at year edges (time zone) |
| 2026-10-24 | pyrs | Contributors 33 with anon / 19 accounts | GitHub contributors Link header | verified | |
| 2026-10-24 | pyrs | Rule 13: OSTI 17315105 lists ORNL | OSTI API 17315105 | verified | |
| 2026-10-24 | pyrs | Sweep 2: brief checked | as above | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | finch | GOAL Q3: DOE CODE record has no sponsor, funder unknown | https://www.osti.gov/api/v1/records/code-122647 | corrected | sponsor_orgs lists USDOE SC and NNSA; brief updated |
| 2026-10-24 | finch | GOAL Q9: has CONTRIBUTING.md | fresh clone of github.com/ORNL/Finch | verified | |
| 2026-10-24 | tnqvm | GOAL Q3: 2583844 lists USDOE, 2251617 lists USDOE SC | OSTI API records 2583844, 2251617 | verified | |
| 2026-10-24 | tnqvm | GOAL Q8/Q9: last push 2025-03, not archived, no CONTRIBUTING or LICENSE | api.github.com/repos/ORNL-QCI/tnqvm; fresh clone | verified | pushed_at 2025-03-05 |
| 2026-10-24 | 3dthesis | GOAL Q3: README credits EERE AMO and OE TRAC; DOE CODE lists USDOE | README line 16; OSTI API code-26241 | verified | |
| 2026-10-24 | 3dthesis | GOAL Q9: no CONTRIBUTING, six example folders | fresh clone | verified | |
| 2026-10-24 | finch, tnqvm, 3dthesis | Sweep 2: GOAL-questions sections | see rows above | verified | 6 checks: 5 verified, 1 corrected, 0 unverifiable |
| 2026-10-24 | sns-neutron-pipeline | Connections: Mantid main paper cited about 1,800 times, most with no ORNL author | api.openalex.org works/doi:10.1016/j.nima.2014.07.029; cites filter with ORNL ROR | verified | 1,809 citing works, 689 with an ORNL institution (about 62% without) |
| 2026-10-24 | sns-neutron-pipeline | Queue names and per-instrument split, OnCat shared-queue comment | github.com/neutrons/data_workflow workflow/settings.py, states.py | corrected | split also covers REDUCTION.HIMEM and REDUCTION_CATALOG queues; added |
| 2026-10-24 | sns-neutron-pipeline | Glossary quotes (SMS, STC, PVs) and livereduce line | data_workflow docs/glossary.rst, docs/developer/index.rst | verified | |
| 2026-10-24 | sns-neutron-pipeline | Agent processors, 60 min / 70% limits, heartbeats, autoreduce predecessor | github.com/neutrons/post_processing_agent README, README_developer.md, processors/ | verified | |
| 2026-10-24 | sns-neutron-pipeline | WebMon plot embedding, keyed link, live-data-server credentials and 3-year expiry | data_workflow view_util.py, settings/base.py; live_data_server config/settings.py, plots/views.py | verified | |
| 2026-10-24 | sns-neutron-pipeline | Creation years, next branches, contributor guides, zero good-first issues | api.github.com/repos/neutrons/*; fresh clones | verified | |
| 2026-10-24 | sns-neutron-pipeline | Sweep 2: deep dive walkthrough (connections and revival sections pending) | see rows above plus Mantid citation row | verified | 6 checks: 5 verified, 1 corrected, 0 unverifiable |
| 2026-10-24 | sns-neutron-pipeline (timing) | PPU outage Aug 2023 to Apr 2024, commissioning 2024-06-07, users 2024-07-11 at 1.7 MW, BES SUF funding | https://proceedings.jacow.org/linac2024/pdf/THPB045.pdf (DOI 10.18429/jacow-linac2024-thpb045) | verified | |
| 2026-10-24 | sns-neutron-pipeline (timing) | Monthly commit bursts (agent 28/68/38; live-data-server 28/11/53; data-workflow peak 33 in 2024-09) | fresh clones, git log --all | verified | exact match |
| 2026-10-24 | sns-neutron-pipeline (timing) | ORNL news and sns.gov timeline links resolve | ornl.gov news 2024-11-07; sns.gov/sts/timeline | verified | HTTP 200 |
| 2026-10-24 | sns-neutron-pipeline (timing) | Sweep 2: revival timing notes | see rows above | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable; causal link correctly left as a guess |
| 2026-10-24 | sns-neutron-pipeline (connections) | Funding for SNAPRed and PyRS unknown | OSTI API records 3012509, 17315105 | corrected | 3012509 lists BES SUF; 17315105 lists USDOE; line fixed |
| 2026-10-24 | sns-neutron-pipeline (connections) | live-data-server BSD-3 Copyright 2024 ORNL; pyoncat 2.7 | fresh clone LICENSE; pypi.org/pypi/pyoncat/json | verified | |
| 2026-10-24 | sns-neutron-pipeline (connections) | SNAPRed and PyRS stars/forks; MantidSnapper quote | api.github.com/repos/neutrons/SNAPRed, PyRS; SNAPRed pyproject.toml | verified | |
| 2026-10-24 | sns-neutron-pipeline (connections) | Queue names, glossary trigger quote, WebMon plot embedding | data_workflow settings.py, glossary.rst, view_util.py | verified | |
| 2026-10-24 | sns-neutron-pipeline (connections) | Sweep 2: connections and usage notes | see rows above | verified | 4 checks: 3 verified, 1 corrected, 0 unverifiable; Mantid count drift noted |
| 2026-10-24 | olcf-test-harness (timing) | Per-year commits, Sept 2016 burst of 96, tags v2.1 to v3.2 | fresh clone of github.com/olcf/olcf-test-harness, git log --all | verified | |
| 2026-10-24 | olcf-test-harness (timing) | summitdev support in the Sept 2016 burst | git log subjects | corrected | "Adding support for summitdev" is 2016-10-13 |
| 2026-10-24 | olcf-test-harness (timing) | 9 authors in early 2025 | git log --all %an vs %ae | corrected | two people by name; 8 to 10 distinct emails |
| 2026-10-24 | olcf-test-harness (timing) | code-153320 lists ASCR | https://www.osti.gov/api/v1/records/code-153320 | corrected | sponsor is USDOE Office of Science only; ASCR is on other OSTI hits |
| 2026-10-24 | olcf-test-harness (signals) | 10 active authors in 2025 | git log --all | corrected | 10 emails, two people by name |
| 2026-10-24 | olcf-test-harness (connections) | Configs, scheduler modules, pyproject, loggers, examples repo | fresh clone; api.github.com/repos/olcf/olcf-test-harness-examples | verified | |
| 2026-10-24 | olcf-test-harness | Sweep 2: timing, connections and signals notes (walkthrough not yet drafted) | see rows above | verified | 6 checks: 2 verified, 4 corrected, 0 unverifiable |
| 2026-10-24 | olcf-test-harness (walkthrough) | Exit codes 0/1/2/5 and zero vs non-zero caveat; .kill_test resubmit comment | doc-sphinx/source/user_guide/adding_new_test.rst | verified | |
| 2026-10-24 | olcf-test-harness (walkthrough) | Event files, five modes, 2016 docs header, repo created 2021, v3.2 note, contributing.rst | fresh clone; api.github.com/repos/olcf/olcf-test-harness | verified | modes file path corrected |
| 2026-10-24 | olcf-test-harness (walkthrough) | Funding: code-153320 names Office of Science, no program | OSTI API records/code-153320 | verified | already updated in the walkthrough before this check |
| 2026-10-24 | olcf-test-harness | Sweep 2: walkthrough | see rows above | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable; small fixes to a file path and the summitdev date |
| 2026-10-24 | finch, 3dthesis | Q10: what Stork is (searched without result) | https://github.com/ORNL/Stork README; Finch CMakeLists.txt lines 8-14; 3DThesis src/Run.cpp line 400 | corrected | Public ORNL/Stork repo (created 2026-09-20, BSD-3, C++/Kokkos): middleware converting sparse thermal data (SRDF) into fine-grid RDF events for microstructure codes; optional in Finch, a tracking mode in 3DThesis; paper DOI 10.1016/j.commatsci.2026.114832. Briefs not yet edited, flagged to the room |
| 2026-10-24 | additive-manufacturing (timing) | Per-year commits, first commits and tags for adamantine, 3DThesis, AdditiveFOAM, Finch, Myna | fresh clones (ORNL-MDF/Myna, adamantine-sim/adamantine, others) | corrected | 3DThesis 1.0.0 tag (2019-06-11) was missing; counts match |
| 2026-10-24 | additive-manufacturing (timing) | OSTI records code-26241, code-108345, code-122647, code-141169, 3002891, 3002570, 2472702, 1839327, 1813276, 1772644 | OSTI API | verified | dates and sponsors match |
| 2026-10-24 | additive-manufacturing (timing) | Every DOE CODE record filed the same day as a release tag | OSTI API dates vs git tags | corrected | true for 3 of 4; 3DThesis record predates repo |
| 2026-10-24 | additive-manufacturing (timing) | Monthly 2024 detail (Finch, Myna, 3DThesis) | git log by month | verified | Finch Mar 19 vs 20, Myna Aug 40 vs 43; edge drift noted |
| 2026-10-24 | additive-manufacturing | Sweep 2: timing notes | see rows above | verified | 4 checks: 2 verified, 2 corrected, 0 unverifiable |
| 2026-10-24 | additive-manufacturing (connections) | Spack additivefoam pins openfoam-org@10 while README requires OpenFOAM-14 | spack/spack-packages additivefoam/package.py line 34; AdditiveFOAM README line 22 | verified | |
| 2026-10-24 | additive-manufacturing (connections) | Myna wraps 3DThesis, AdditiveFOAM, ExaCA, adamantine; no Finch wrapper | fresh clone of ORNL-MDF/Myna src/myna/application | verified | |
| 2026-10-24 | additive-manufacturing (connections) | 3DThesis paper 69 citers, 24 ORNL; ExaCA paper 55 citers, 25 ORNL | api.openalex.org with ORNL ROR filter | verified | |
| 2026-10-24 | additive-manufacturing (connections) | 3DThesis Stork mode came first, in 2024 | git log -S Stork src/Run.cpp (2024-09-12) | verified | |
| 2026-10-24 | additive-manufacturing | Sweep 2: connections notes | see rows above | verified | 4 checks: 4 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | grid-tools (timing) | Per-year commits, first commits, tags for GridKit, ReSolve, ExaGO | fresh clones ORNL/GridKit, ORNL/ExaGO, ORNL/ReSolve | verified | exact match |
| 2026-10-24 | grid-tools (timing) | OSTI 1738891, 2441467, 3385022, code-152622, code-114681, code-176348 dates, sponsors, 3385022 abstract names neither tool | OSTI API | verified | |
| 2026-10-24 | grid-tools (timing) | GridKit Dec 2024 to May 2025 monthly, ExaGO Feb to Apr 2026 monthly | git log by month (author date, all branches) | verified | GridKit 19 commit names in 2025 |
| 2026-10-24 | grid-tools (timing) | ExaGO Sep to Nov 2023 was 4, 12, 18 | git log by month | corrected | 18, 32, 54 all branches; 9, 8, 14 default |
| 2026-10-24 | grid-tools (timing) | ReSolve README credits ECP; pnnl/ExaGO archived; ORNL/ExaGO created 2026-01-08 | README line 140; GitHub API | verified | |
| 2026-10-24 | grid-tools | Sweep 2: timing notes | see rows above | verified | 5 checks: 4 verified, 1 corrected, 0 unverifiable |
| 2026-10-24 | grid-tools (connections) | Spack exago deps (hiop, ipopt, raja/umpire; no resolve or gridkit) | spack-packages exago/package.py | verified | |
| 2026-10-24 | grid-tools (connections) | HiOp optional ReSolve support | LLNL/hiop CMakeLists.txt line 93; spack hiop cusolver_lu | verified | |
| 2026-10-24 | grid-tools (connections) | Star/fork counts and HydroFleetIntel last push 2024-03-12 | GitHub API | verified | |
| 2026-10-24 | grid-tools (connections) | ExaGO ORNL-era funding unknown | OSTI code-176348 | corrected | added: record names USDOE generically |
| 2026-10-24 | grid-tools | Sweep 2: connections notes | see rows above | verified | 4 checks: 3 verified, 1 corrected, 0 unverifiable |
| 2026-10-24 | gedi-tutorials | Status, release, stars/forks, license, DAAC scope and NASA ownership | GitHub API; fresh clone; earthdata.nasa.gov ORNL DAAC page | verified | |
| 2026-10-24 | gedi-tutorials | Sweep 2: GOAL brief | see row above | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | olcf-user-docs | No license, counts, active | GitHub API | verified | |
| 2026-10-24 | olcf-user-docs | Sweep 2: GOAL brief | see row above | verified | 2 checks: 2 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | django-remote-submission | Dates, ISC license, PyPI last release 2018, SNS Liquids Reflectometer case | GitHub API; PyPI JSON; paper.md line 34 | verified | |
| 2026-10-24 | django-remote-submission | Funding: OSTI 1394387 USDOE; 1470800 USDOE plus BES | OSTI API | verified | |
| 2026-10-24 | django-remote-submission | Sweep 2: GOAL brief | see rows above | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | hydrofleetintel | WPTO sponsor, 8 commits Mar 2024, synthetic data, PRs not reviewed | OSTI code-123550; fresh clone README lines 7, 57 | verified | staff contact in README kept out of brief |
| 2026-10-24 | hydrofleetintel | Sweep 2: GOAL brief | see row above | verified | 3 checks: 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-24 | mind-the-gap | NGA sponsor, dates, license, CI | OSTI code-152916; GitHub API; fresh clone | verified | |
| 2026-10-24 | mind-the-gap | Status "active-ish"; "single 941-line file"; "4 issues" | RULES 14; fresh clone; GitHub API | corrected | status unknown; two helper modules; issues plus PRs |
| 2026-10-24 | mind-the-gap | Sweep 2: GOAL brief | see rows above | verified | 3 checks: 2 verified, 1 corrected, 0 unverifiable |
| 2026-10-24 | heartbeat / situ (map link 198) | Story never says Heartbeat stays on the research license | ORNL news 2024-09-18 (U2opia license story), fetched via WebFetch | corrected | Story says the company "will continue to explore opportunities for Heartbeat... through a research and development license"; Scout's stub-search wording is right; map not edited (Connector's file), flagged in room |
| 2026-10-24 | heartbeat / situ (map link 198) | Heartbeat's funders are blank | same story | corrected | Story says Heartbeat was supported through ORNL's Technology Innovation Program (TIP); map not edited, flagged in room |
| 2026-10-24 | heartbeat / situ (map link 198) | 2023 R&D licenses for both; Situ commercial; Situ funded by LDRD, DOE, DoD, DHS; both from the same cyber division | same story | verified | |
| 2026-10-24 | first-five related-projects tables | Daymet repos in ornldaac org; ExaGO Frontier build scripts; HydroFleetIntel 222-row taxonomy; repo and DOE CODE same-day dates | GitHub API; fresh clones; OSTI API | verified | |
| 2026-10-28 | heartbeat / situ (map link 198) | Heartbeat license and funding lines | ORNL news 2024-09-18 (U2opia license story) | corrected | Map link 198 edited at the lead's request: research-license line and TIP funding now KNOWN |
| 2026-10-29 | nuclear-reactor-scan | SCALE export-controlled, RSICC licensed | ornl.gov SCALE order page (redirects now); RSICC CCC-860 listing; RSICC export control agreement | corrected | Call holds; dead-ish link noted, second source added |
| 2026-10-29 | nuclear-reactor-scan | VERA export-controlled, RSICC CCC-855, CASL approval | vera.ornl.gov/vera-license; rsicc CCC-855 | verified | |
| 2026-10-29 | nuclear-reactor-scan | Shift/Exnihilo export-controlled; ships inside SCALE | Profugus README.rst; RSICC CCC-855 | corrected | Export control holds; ships inside VERA confirmed, inside SCALE not confirmed |
| 2026-10-29 | nuclear-reactor-scan | Profugus BSD-2, DOE CODE 10329, last push 2018 | GitHub API; DOE CODE 10329 | verified | |
| 2026-10-29 | nuclear-reactor-scan | TRANSFORM Apache-2.0, UT-Battelle, DOE CODE 5745 | GitHub API; README; DOE CODE 5745 | verified | |
| 2026-10-29 | nuclear-reactor-scan | Thermochimica BSD-3; DataTransferKit BSD-3 archived | GitHub API | verified | |
| 2026-10-29 | nuclear-reactor-scan | OLM BSD-3 per GitLab metadata | DOE CODE 122128; GitHub API; README | corrected | Attribution fixed |
| 2026-10-29 | nuclear-reactor-scan | MSD free but account-gated | msd.ornl.gov/access-instructions | verified | Login and form not used |
| 2026-10-29 | nuclear-reactor-scan | MSRE TM-728 says none classified; Part XII limited distribution; TM-908 on ORNL server | OSTI 4654707; TM-728 PDF; Pub209949 | corrected | Pages marked UNCLASSIFIED; rest verified |
| 2026-10-29 | nuclear-reactor-scan | Kairos $27M, five years, fourth partnership | ORNL news 2026-02-19; ANS 2026-02-23 | verified | |
| 2026-10-29 | nuclear-reactor-scan | HFIR, MSIRT, NuCAMP, PHYSOR rows | links resolve only | unverifiable | Contents not re-read this pass |
| 2026-10-29 | nuclear-reactor-scan (file summary) | 13 checks | as above | corrected | 8 verified, 4 corrected, 1 unverifiable |
| 2026-10-29 | nuclear-reactor-software deep dive (file summary) | links and OLM status line | repo files | corrected | Placeholder sections; OLM line updated |
| 2026-10-29 | cyber-ai-mac-picks (file summary) | licenses, stars, push dates, install notes for 7 repos; org repo count | GitHub API; READMEs | verified | 9 verified, 0 corrected, 1 unverifiable (commit counts) |
| 2026-10-29 | olm (file summary) | license, dates, PyPI, DOE CODE, commit counts | GitHub API; PyPI; DOE CODE; fresh clone | corrected | 8 verified, 2 corrected (count labels, earliest commit) |
| 2026-10-29 | thermochimica (file summary) | license, created, tags, last push, contributors | GitHub API; OSTI 3374533 | corrected | 4 verified, 1 corrected (last push), 1 unverifiable (contributors) |
| 2026-10-29 | catalog rows transform-library, profugus, molten-salt-database (summary) | licenses, DOE CODE ids, copyright lines, access | GitHub API; DOE CODE; LICENSE files; MSD pages | verified | 3 verified |
| 2026-10-29 | vivaldi | repo dates, 10 commits same day, stars/forks, license, files, code lines, requirements, Docker details, Gauntlet input | GitHub API; fresh clone; README | verified | |
| 2026-10-29 | vivaldi | 1 contributor account | git shortlog | corrected | One person, two author names |
| 2026-10-29 | vivaldi | DOE CODE supports ORNL affiliation | DOE CODE 126052 | corrected | Developer affiliation only; no research-org field |
| 2026-10-29 | vivaldi (map links 48, 58, 87) | related-projects consistency | connections/map.md | verified | No edits |
| 2026-10-29 | vivaldi (file summary) | brief and map rows | as above | corrected | 2 verified groups (13 facts), 2 corrected, 0 unverifiable |
| 2026-10-29 | olm | GitHub is main dev repo, ORNL GitLab is a read-only mirror | README; readthedocs Contributing page; DOE CODE 122128 | verified | DOE CODE registers the GitLab mirror |
| 2026-10-29 | olm | GitLab 2026-09-11 is a mirror-sync date after the last real GitHub push | fresh clone (newest commit 2026-06-12); GitLab page shows no dates | unverifiable | Later than GitHub, yes; sync cause INFERRED only. GitLab API not queried (not linked from a public page). Catalog left alone |
| 2026-10-29 | far3d | no license file; guide says GNU with no version | repo tree; GitHub API; User_guide.pdf | verified | |
| 2026-10-29 | far3d | license per DOE CODE | DOE CODE 144364 | corrected | DOE CODE says MIT; license now tagged as a source conflict, UNKNOWN |
| 2026-10-29 | far3d | 2020-22 commits 44, 18, 6; branch list | fresh clone | corrected | Committer-date counts (author 44, 21, 11); patch branch added |
| 2026-10-29 | far3d (map link 67) | VMEC input unverified | User_guide.pdf | corrected | Guide states VMEC input; map line corrected inline |
| 2026-10-29 | far3d (file summary) | dates, tags, stars, contributors, build, DOE CODE fields | GitHub API; clone; DOE CODE | corrected | 12 verified, 4 corrected, 0 unverifiable |
| 2026-10-29 | tasqc | server accepts any authKey value | KeyResource.java (source read only, not run) | verified | Neutral design wording kept |
| 2026-10-29 | tasqc (file summary) | license, dates, OSTI 1339958, client defaults, queue size, map links 68/88 | GitHub API; clone; OSTI API | verified | 8 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | stor4build | yearly commit counts | fresh clone | corrected | Committer date; author 109, 136, 114 |
| 2026-10-29 | stor4build (file summary) | license, dates, tags, PyPI, models, measures, contributors, DOE CODE, map links 59/60 | GitHub API; clone; PyPI; DOE CODE | corrected | 11 verified, 1 corrected, 0 unverifiable |
| 2026-10-29 | reactor map 203-204 | VERA bundles SCALE's ORIGEN and Shift | RSICC CCC-855 | verified | Shift listed as a component; "all of Shift" not stated |
| 2026-10-29 | reactor map 208 | Shift ships inside SCALE | Profugus README; RSICC CCC-855 | corrected | Only inside VERA confirmed; README wording is about Exnihilo |
| 2026-10-29 | reactor map 209 | Profugus open Exnihilo kernels, BSD-2, last push 2018, 29 stars, 6 forks | README; GitHub API; DOE CODE 10329 | verified | |
| 2026-10-29 | reactor map 215 | TRANSFORM requires Dymola; OpenModelica | README; repo grep | verified | README lists only Dymola; repo has only an OpenModelica course link; scan row already says so |
| 2026-10-29 | reactor map | Thermochimica and GITR docs have Mac build steps | READMEs (Thermochimica "MacOS"; GITR "Mac OSx, No CUDA") | verified | |
| 2026-10-29 | reactor map 211-212 | INL plugs Thermochimica into MOOSE, Pronghorn, BISON | OSTI 3374533, 1214026, 1615992, 1507873 | corrected | INL-led: MOOSE and Pronghorn; BISON coupling reports are ORNL-led |
| 2026-10-29 | reactor map 222 | TCR moved to printed parts and an AI digital platform | OSTI 1831630; Pub166838 | verified | Peregrine tie stays INFERRED |
| 2026-10-29 | reactor map (file summary) | links 203-222 | as above | corrected | 6 verified, 2 corrected, 0 unverifiable |
| 2026-10-29 | hyperion (file summary) | purpose, inputs/outputs, expert review, OSTI fields; "not a sandbox" | ORNL project page; OSTI 1231925 | corrected | 5 verified, 1 corrected (KNOWN to INFERRED), 0 unverifiable; license dates not added |
| 2026-10-29 | urban-net-toolkit (file summary) | scope, example, lifelines, capabilities, EAGLE-I, LDRD 2015, OSTI fields | ORNL news 2022-08-04; OSTI 1467082 | verified | 7 verified, 0 corrected, 0 unverifiable; papers not added |
| 2026-10-29 | akatosh (file summary) | method, examples, timeline, group, TTP, licensing interest, OSTI fields | ORNL news 2018-08-28; OSTI 1419663 | verified | 8 verified, 0 corrected, 0 unverifiable; papers not added |
| 2026-10-29 | heartbeat-malware | OSTI record unread | OSTI 1574875; OSTI 2305827 | corrected | Both records loaded; software record added as second source; report number, sponsor and date conflict added |
| 2026-10-29 | heartbeat-malware | illustrative example | report abstract | corrected | Specific OS mechanism removed; kept at the report's high level |
| 2026-10-29 | heartbeat-malware (file summary) | method, status, licensing, TIP, division, OSTI | ORNL report page; ORNL news 2024-09-18; OSTI 1574875, 2305827 | corrected | 7 verified, 3 corrected, 0 unverifiable |
| 2026-10-29 | can-d (file summary) | journal details, method, numbers, OSTI fields | ORNL publication page; OSTI 1822873 | verified | 8 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | wufi-ornl (file summary) | partnership, license, 62 cities, physics, validation, page date | wufi.de free versions; OSTI 1231793 | corrected | 7 verified, 1 corrected (registration required), 0 unverifiable |
| 2026-10-29 | connections/map.md | Link 208: Shift/Exnihilo ships inside SCALE | https://scale-manual.ornl.gov/6.3.3/CSAS-Shift.html ; https://www.osti.gov/biblio/3007184 | verified | Reverses the earlier 208 correction from today. The SCALE 6.3.3 manual has a CSAS-Shift chapter run from inside SCALE, and OSTI 3007184 covers SCALE-Shift sequences; this already matched link 82 [CORROBORATED]. Map link 208 and the diagram edge may go back to known. |
| 2026-10-29 | map 223-224 (urban-net) | EAGLE-I planned integration; CESER/FEMA users; 2015 LDRD start | ORNL news 2022-08-04 | verified | |
| 2026-10-29 | map 225 (wufi-ornl) | free reduced edition of WUFI Pro; joint program corroborated | wufi.de free versions; OSTI 1231793 | verified | |
| 2026-10-29 | map 89, 85 (wufi-ornl) | joint ORNL/Fraunhofer; EnergyPlus domain-only | OSTI 1231793 | verified | |
| 2026-10-29 | map 84 (hyperion, heartbeat) | tools exist only as OSTI records | ORNL Hyperion page; ORNL Heartbeat report page and 2024 story | corrected | Both have ORNL pages; status labels left to catalog owner |
| 2026-10-29 | map 69 (akatosh, can-d) | both stub-osti-only | ORNL news 2018-08-28; ORNL CAN-D publication page | corrected | Both have ORNL pages and short briefs; labels left to catalog owner |
| 2026-10-29 | map 86 (urban-net) | description not read | OSTI 1467082 | corrected | Description read; still domain-only |
| 2026-10-29 | map 198 / heartbeat table | one small company | ORNL news 2024-09-18 | corrected | "Small" not stated; rest verified |
| 2026-10-29 | map 208 | Shift inside SCALE | OSTI 3007184; link 82 (SCALE manual CSAS-Shift) | verified | Already switched back to KNOWN; scan file's earlier UNKNOWN re-corrected to match |
| 2026-10-29 | Pass 32 and six related-projects tables (file summary) | 18 table rows and map links 69, 84-86, 89, 198, 223-225 | as above | corrected | 13 verified, 4 corrected, 0 unverifiable |
| 2026-10-29 | vivaldi (second pass) | n_estimators range; data access wording; first-pass fixes | vivaldi_bh.py; README | verified | 3 verified, 0 corrected, 1 unverifiable (languages API rate-limited) |
| 2026-10-29 | olm (second pass) | first tags vs PyPI; requires-python; home/mirror | git tags; pyproject.toml; readthedocs | verified | 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | far3d | OSTI search 20 hits | OSTI records API (61 matches) | corrected | 20 was a first-page count |
| 2026-10-29 | far3d (second pass) | v2.0 date; OSTI count; first-pass fixes | git tag; OSTI API | corrected | 2 verified, 1 corrected, 0 unverifiable |
| 2026-10-29 | tasqc | first commit is the 2017-02-03 import | fresh clone | corrected | First commit is 2016-10-06 "Initial commit"; import is second |
| 2026-10-29 | tasqc (second pass) | history, yearly counts (author = committer, all branches), wording | fresh clone | corrected | 3 verified, 1 corrected, 0 unverifiable |
| 2026-10-29 | stor4build | OpenStudio 3.11.0 / EnergyPlus 25.2.0 from repo test notes | docs/source/installation.md; tests.yml | corrected | Docs say 3.11 and 25.2 (plus Python 3.12); source relabelled |
| 2026-10-29 | stor4build (second pass) | CI matrix, runner, tool versions, first-pass fix | tests.yml; installation.md | corrected | 3 verified, 1 corrected, 0 unverifiable |
| 2026-10-29 | hyperion (second pass) | KNOWN claims, sandbox fix | ORNL page; OSTI | verified | 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | urban-net-toolkit (second pass) | users, timeline, EAGLE-I status | ORNL news | verified | 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | akatosh (second pass) | TTP, demos, licensing interest | ORNL news | verified | 3 verified, 0 corrected, 0 unverifiable; no independent source |
| 2026-10-29 | heartbeat-malware (second pass) | report date via Crossref; example; OSTI source | Crossref 10.2172/2305827 | verified | 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | can-d (second pass) | journal details via Crossref; numbers | Crossref 10.1109/TVT.2021.3092354 | verified | 4 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | wufi-ornl (second pass) | 62 cities, license, registration, title translation | wufi.de; OSTI | verified | 4 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | transform-library | Apache-2.0, 2017 UT-Battelle copyright | README; DOE CODE 5745 | verified | |
| 2026-10-29 | transform-library | Dymola only stated requirement; OpenModelica UNKNOWN | README; repo grep | verified | Only OpenModelica mention is a course link in UsersGuide/Resources.mo |
| 2026-10-29 | transform-library | DOE CODE 2017-09-26, ORNL, USDOE, DOI | https://www.osti.gov/doecode/biblio/5745 | verified | |
| 2026-10-29 | transform-library | created 2017-07-26, pushed 2026-10-14 | GitHub API | verified | |
| 2026-10-29 | transform-library | packages, Nuclear subpackages, example folders | fresh clone | verified | Empty source tag on examples filled |
| 2026-10-29 | transform-library | .mos tests, no CI (.github issue templates only) | README; clone | verified | |
| 2026-10-29 | transform-library | yearly commits 2018-20 and 2022-26 | fresh clone, author dates, default branch | verified | 915 default / 960 all branches |
| 2026-10-29 | transform-library | 17 contributors | git shortlog | corrected | 17 names default branch; 18 all branches; 20 name+email |
| 2026-10-29 | transform-library | latest activity | git log; GitHub API | corrected | Last commit 2026-09-30 (author=committer) added beside push date |
| 2026-10-29 | transform-library | related table: Dymola, OpenModelica, DOE CODE rows | README; DOE CODE | verified | |
| 2026-10-29 | map 215 | OpenModelica tagged INFERRED | README; repo grep | corrected | Now UNKNOWN |
| 2026-10-29 | profugus | purpose, export-control statement, quote, XPRESS/MCREX, Minisweep | README.rst | verified | |
| 2026-10-29 | profugus | BSD-2, 2014 CEES copyright | LICENSE; DOE CODE 10329 | verified | |
| 2026-10-29 | profugus | DOE CODE 2018-01-18, ORNL | https://www.osti.gov/doecode/biblio/10329 | verified | |
| 2026-10-29 | profugus | packages/, install/ scripts incl. macOS, XK7 | fresh clone | verified | |
| 2026-10-29 | profugus | first commit 2013-12-02; 312/194/71/3 by year | fresh clone, author dates, default branch | verified | 598 default / 1571 all branches |
| 2026-10-29 | profugus | 10 contributors | git shortlog | corrected | Default branch; 15 across all branches |
| 2026-10-29 | profugus | funding UNKNOWN | DOE CODE 10329 | corrected | Sponsor ASCR stated |
| 2026-10-29 | profugus | last push 2018-08-14, no releases | GitHub API | unverifiable | API rate-limited this pass; last commit 2017-11-07 verified |
| 2026-10-29 | profugus | related table: Shift/Exnihilo, VERA, Trilinos, Minisweep | README.rst; map | verified | |
| 2026-10-29 | profugus | related table: SCALE row KNOWN | map 208 | corrected | Absence of evidence, now UNKNOWN |
| 2026-10-29 | map 208 | Profugus only on GitHub [KNOWN] | Profugus repo | corrected | Now UNKNOWN wording; Shift-in-SCALE KNOWN unchanged |
| 2026-10-29 | map 209 | 29 stars, 6 forks | GitHub API | unverifiable | Rate-limited; rest of link verified |
| 2026-10-29 | molten-salt-database | two parts, formats, tools, Saline, GUI, FactSage versions | https://mstdb.ornl.gov/about/ | verified | |
| 2026-10-29 | molten-salt-database | license-free, not for sale | about page | verified | |
| 2026-10-29 | molten-salt-database | account + membership, Tue/Thu grant | https://msd.ornl.gov/access-instructions/ | verified | No signup, no form |
| 2026-10-29 | molten-salt-database | funding applies to both databases | about page | corrected | Named programs for MSD-TC; MSD-TP from DOE MSR programs |
| 2026-10-29 | molten-salt-database | Thermochimica salt tests miss gated file | Thermochimica repo test/daily, data/ | verified | Stays INFERRED; tests load LiBeUPuThF_T1.dat, absent |
| 2026-10-29 | molten-salt-database | catalog management note, 2026 news | catalog row | unverifiable | Not re-read |
| 2026-10-29 | molten-salt-database | related table: Thermochimica x2, MSRE rows | about page; Thermochimica repo | verified | |
| 2026-10-29 | map 213 | missing file named by example inputs | Thermochimica repo | corrected | It is the TestMSTDB tests' file |
| 2026-10-29 | transform-library (file summary) | brief + table + map 215 | as above | corrected | 9 verified, 3 corrected, 0 unverifiable |
| 2026-10-29 | profugus (file summary) | brief + table + maps 208-209 | as above | corrected | 6 verified, 4 corrected, 2 unverifiable |
| 2026-10-29 | molten-salt-database (file summary) | brief + table + map 213 | as above | corrected | 5 verified, 2 corrected, 1 unverifiable |
| 2026-10-29 | transform-library (file summary, recount) | row count above | log rows | corrected | Recount: 8 verified, 3 corrected, 0 unverifiable (summary row above overstated verified by 1) |
| 2026-10-29 | transform-library (pass 2) | Apache-2.0 | GitHub API license field | verified | Second source beyond README |
| 2026-10-29 | transform-library (pass 2) | DOI resolves | doi.org | verified | |
| 2026-10-29 | transform-library (pass 2) | 4 releases | clone tags v0.1-v0.4 beta | verified | |
| 2026-10-29 | transform-library (pass 2) | Dymola only; OpenModelica UNKNOWN | README reread | verified | |
| 2026-10-29 | transform-library (pass 2) | timeline dates | clone vs API created_at | verified | First commit 2017-08-14 |
| 2026-10-29 | profugus (pass 2) | last push 2018-08-14 | GitHub API retry | verified | Was unverifiable |
| 2026-10-29 | map 209 (pass 2) | 29 stars, 6 forks | GitHub API retry | verified | Was unverifiable; repo web page rendered 0/0, treated as artifact |
| 2026-10-29 | profugus (pass 2) | BSD-2, no releases, DOI | GitHub API; clone tags; doi.org | verified | |
| 2026-10-29 | profugus (pass 2) | "only public window" | none supports "only" | corrected | Now "a rare public window" |
| 2026-10-29 | profugus (pass 2) | "cleanest example in the catalog" | interpretation | corrected | Softened to projects read so far |
| 2026-10-29 | molten-salt-database (pass 2) | access requirement | about page + access page | verified | |
| 2026-10-29 | molten-salt-database (pass 2) | license terms | about page | verified | |
| 2026-10-29 | molten-salt-database (pass 2) | formerly MSTDB | access steps; mstdb.ornl.gov address | verified | Date UNKNOWN |
| 2026-10-29 | molten-salt-database (pass 2) | Thermochimica link INFERRED | Thermochimica docs grep | verified | Tag honest |
| 2026-10-29 | transform-library (second-pass summary) | 5 risky claims | as above | verified | 5 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | profugus (second-pass summary) | 5 risky claims incl. map 209 | as above | corrected | 3 verified, 2 corrected, 0 unverifiable |
| 2026-10-29 | molten-salt-database (second-pass summary) | 4 risky claims | as above | verified | 4 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | cyberwheel | commit counts 352 default / 398 all; yearly by author date | fresh clone | verified | Committer date gives 243 and 155 |
| 2026-10-29 | cyberwheel | license line names the copyright holder | LICENSE; GOAL.md people-by-role rule | corrected | Changed to role only |
| 2026-10-29 | cyberwheel (second pass) | counts, tags, license, fixes held | fresh clone; LICENSE | corrected | 4 verified, 1 corrected, 0 unverifiable |
| 2026-10-29 | datafed (second pass) | 6,210/3,713 commits; yearly counts; license; v5.1.3 | fresh clone | verified | 4 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | hydragnn (second pass) | 1,069/928 commits; yearly counts; v2.0.0, v3.0 dates; license | fresh clone; GitHub release pages | verified | 4 verified, 0 corrected, 0 unverifiable; release dates are publish dates |
| 2026-10-29 | mantid (second pass) | tags exist; dates, contributors, license | git ls-remote | unverifiable | 1 verified, 0 corrected, 3 unverifiable; no Rule 17 clone (repo size) |
| 2026-10-29 | olcf-test-harness (second pass) | 1,073/1,070 commits; yearly counts; release dates; license; last push | fresh clone; GitHub release pages | verified | 4 verified, 0 corrected, 1 unverifiable-as-stale (last push now 2026-10-28) |
| 2026-10-29 | thermochimica | earliest public year 2015 | OSTI API 1157131, 1163165 (2014) | corrected | Now 2014 |
| 2026-10-29 | thermochimica | 63 pass / 5 fail | prior local Linux run 2026-10-28 | corrected | Labelled dated Linux result, not Mac, not re-run; 5 of 73 unaccounted |
| 2026-10-29 | thermochimica | CI hosted at INL [KNOWN] | README badge; .github has issue templates only | corrected | Now INFERRED |
| 2026-10-29 | thermochimica | last push, no tags, missing LiBeUPuThF_T1.dat, CO.dat path, languages, MOOSE submodule, commit counts | fresh clone; GitHub API; MOOSE .gitmodules | verified | |
| 2026-10-29 | thermochimica (file summary, post-rewrite check) | whole brief | as above | corrected | 8 verified, 3 corrected, 0 unverifiable |
| 2026-10-29 | data-workflow (pass 2) | BSD-3 2022 ORNL | fresh clone LICENSE | verified | |
| 2026-10-29 | data-workflow (pass 2) | releases 3.10-3.12 dates | GitHub release publish dates; clone tags | verified | 3.10.0 tag commit 2026-07-15, release 2026-07-16 |
| 2026-10-29 | data-workflow (pass 2) | about 35 contributors | git shortlog default branch | verified | 35 names |
| 2026-10-29 | data-workflow (pass 2) | only pipeline repo with contributor guide | GitHub contents of two sibling repos | verified | |
| 2026-10-29 | data-workflow (pass 2) | commit spot check | fresh clone | verified | 1873 default (next) / 1891 all |
| 2026-10-29 | data-workflow (second-pass summary) | 5 claims | as above | verified | 5 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | daymet (pass 2) | permissive UT-Battelle license | LICENSE.md full text | verified | Grant is permissive despite header; no year |
| 2026-10-29 | daymet (pass 2) | V3 2016-07-14, V4 2020-12-15 | daymet.ornl.gov page source | verified | |
| 2026-10-29 | daymet (pass 2) | last push 2025-03-29 | GitHub API; clone | verified | |
| 2026-10-29 | daymet (pass 2) | commit spot check, 6 contributors | fresh clone | verified | 15 commits default=all |
| 2026-10-29 | daymet (second-pass summary) | 4 claims | as above | verified | 4 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | e3sm-elm (pass 2) | BSD-3 2024 UChicago Argonne | fresh clone LICENSE | verified | API shows NOASSERTION |
| 2026-10-29 | e3sm-elm (pass 2) | components/elm layout | clone tree | verified | |
| 2026-10-29 | e3sm-elm (pass 2) | active | GitHub API push 2026-10-29 | verified | 69163 default / 87337 all commits |
| 2026-10-29 | e3sm-elm (pass 2) | OSTI 3005830, 3364821, DOE CODE versions | OSTI API | unverifiable | Timed out |
| 2026-10-29 | e3sm-elm (second-pass summary) | 4 claims | as above | verified | 3 verified, 0 corrected, 1 unverifiable |
| 2026-10-29 | myna (pass 2) | BSD-3 2024 ORNL | clone; API | verified | |
| 2026-10-29 | myna (pass 2) | releases 1.0.0, 1.1.0 | API; tags | verified | |
| 2026-10-29 | myna (pass 2) | about 9 contributors | API (9); shortlog 13 names | verified | Method noted |
| 2026-10-29 | myna (pass 2) | docs links | HTTP check; README | corrected | myna-docs 404; /Myna/ works |
| 2026-10-29 | myna (second-pass summary) | 4 claims | as above | corrected | 3 verified, 1 corrected, 0 unverifiable |
| 2026-10-29 | tesvis-modis (pass 2) | four public pages resolve | HTTP | verified | |
| 2026-10-29 | tesvis-modis (pass 2) | citation DOI 1600 | doi.org; service page | verified | |
| 2026-10-29 | tesvis-modis (pass 2) | API v1 | service page | verified | |
| 2026-10-29 | tesvis-modis (second-pass summary) | 3 claims | as above | verified | 3 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | sns-neutron-pipeline-timing | PPU dates, Nov 2024 milestone | DOI; ORNL news 2024-11-07 | verified | |
| 2026-10-29 | sns-neutron-pipeline-timing | modernization commits | fresh clones | verified | |
| 2026-10-29 | sns-neutron-pipeline-timing | monthly bursts (ledger) | fresh clones, author dates, all branches | verified | Committer-date and default-branch variants noted |
| 2026-10-29 | sns-neutron-pipeline-timing | 1.9 MW Oct 2025, 2 MW May 2026 | sns.gov/sts/timeline | corrected | Source now redirects; tag lowered |
| 2026-10-29 | sns-neutron-pipeline-timing (file summary) | first pass | as above | corrected | 3 verified, 1 corrected, 0 unverifiable |
| 2026-10-29 | nuclear-reactor-software-connections | licensed/open calls, Profugus, TRANSFORM, MSD tags | briefs; RSICC; GitHub API; DOE CODE | verified | No tag upgrades |
| 2026-10-29 | nuclear-reactor-software-connections | star/fork counts | GitHub API | verified | |
| 2026-10-29 | nuclear-reactor-software-connections | link 213 "reads its files" | MSD about page | corrected | Page says "compatible with" |
| 2026-10-29 | nuclear-reactor-software-connections | no GitHub dependents; SCALE citations | signals pass | unverifiable | Not re-checked |
| 2026-10-29 | nuclear-reactor-software-connections (file summary) | first pass | as above | corrected | 2 verified, 1 corrected, 1 unverifiable |
| 2026-10-29 | nuclear-reactor-software | placeholder sections only | file | verified | Existing 2026-10-29 note stands; nothing new to check |
| 2026-10-29 | additive-manufacturing | Stork, ExaCA, adamantine, Myna facts | GitHub API; Myna clone | verified | |
| 2026-10-29 | additive-manufacturing | open questions stated open | file | verified | Peregrine public?, Finch funding after 2024 |
| 2026-10-29 | additive-manufacturing | repos all public in spring 2023 | GitHub API; git log | corrected | Finch/Myna repos created 2024-02-23; first commits spring 2023 |
| 2026-10-29 | additive-manufacturing (file summary) | first pass | as above | corrected | 2 verified, 1 corrected, 0 unverifiable |
| 2026-10-29 | grid-tools | pnnl/ExaGO archived; ReSolve 85 stars | GitHub API | verified | |
| 2026-10-29 | grid-tools | ExaGO-ReSolve open; no GridKit-ExaGO link | briefs; map | verified | |
| 2026-10-29 | grid-tools | ExaGO 33 commits 2024 | fresh clone | corrected | All branches; default 22 |
| 2026-10-29 | grid-tools | ORNL/ExaGO created 2026-01-08 | GitHub API | unverifiable | Rate-limited |
| 2026-10-29 | grid-tools (file summary) | first pass | as above | corrected | 2 verified, 1 corrected, 1 unverifiable |
| 2026-10-29 | mantid | v6.16.0 2026-06-25, v6.16.1 2026-07-03 | GitHub release pages | verified | v6.16.0 is 2026-06-25 UTC (2026-06-24 ET) |
| 2026-10-29 | mantid | about 307 contributors | GitHub contributors API pagination (anon=1) | verified | |
| 2026-10-29 | mantid | GPL-3.0 | LICENSE.txt; DataCite 10.5286/Software/Mantid6.16.1 | verified | |
| 2026-10-29 | mantid | 153,918 commits on main | GitHub repo page shows 153,944 (default branch) | verified | Page count, no author/committer split |
| 2026-10-29 | mantid (second pass, completed) | dates, contributors, license, commit count | as above | verified | 5 verified, 0 corrected, 0 unverifiable (replaces the earlier 3 unverifiable) |
| 2026-10-29 | nuclear-reactor-software (filled, pass 1) | current projects, MSRE, licensing, Shift in SCALE/VERA, Profugus, TRANSFORM, MSD, OpenMC/fusion, Kairos | briefs; scan; map | verified | Tags match sources |
| 2026-10-29 | nuclear-reactor-software (filled, pass 1) | Mac section and OLM install wording | Thermochimica and OLM briefs; README; PyPI | verified | Already Linux-labeled / INFERRED when checked |
| 2026-10-29 | nuclear-reactor-software (filled, pass 1) | Thermochimica via MOOSE and Pronghorn | Thermochimica brief; map 52, 211; OSTI 3374533 | verified | |
| 2026-10-29 | nuclear-reactor-software (filled, pass 1) | Thermochimica does not model reaction speed [KNOWN: README] | README; brief | corrected | Not stated; now INFERRED |
| 2026-10-29 | nuclear-reactor-software (filled, pass 1) | CASL built VERA's packaged pieces | map 218 | corrected | Softened to what map 218 supports |
| 2026-10-29 | nuclear-reactor-software (filled, pass 1) | HFIR project page source | neutrons.ornl.gov | corrected | Source note added; address now a home page |
| 2026-10-29 | nuclear-reactor-software (filled, pass 1) | mermaid diagram vs text | file | verified | Simplified, no conflict |
| 2026-10-29 | nuclear-reactor-software (filled, pass 1 summary) | first full check | as above | corrected | 4 verified, 3 corrected, 0 unverifiable |
| 2026-10-29 | nuclear-reactor-software (filled, pass 2) | Shift in VERA | RSICC CCC-855 | verified | |
| 2026-10-29 | nuclear-reactor-software (filled, pass 2) | Thermochimica README MacOS section | repo | verified | |
| 2026-10-29 | nuclear-reactor-software (filled, pass 2) | Pronghorn tie | OSTI 3374533 abstract | verified | |
| 2026-10-29 | nuclear-reactor-software (filled, pass 2) | OLM OS Independent | PyPI JSON 0.14.2 | verified | Supports INFERRED only |
| 2026-10-29 | nuclear-reactor-software (filled, pass 2) | Profugus macOS scripts | repo install/ | verified | |
| 2026-10-29 | nuclear-reactor-software (filled, pass 2 summary) | second pass | as above | verified | 5 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | shift-exnihilo | Shift part of VERA upgraded INFERRED to KNOWN | https://rsicc.ornl.gov/codes/ccc/ccc8/ccc-855.html | verified | Page says "integrated into VERA" and lists Shift as a VERA 4.3 component; edit made by another pass |
| 2026-10-29 | shift-exnihilo (file summary) | VERA tag recheck | as above | verified | 1 verified, 0 corrected, 0 unverifiable; stale line 63 caveat noted |
| 2026-10-29 | connections/map.md (whole file) | earlier summary row called the URL, diagram and spot-check pass the "second full pass" | log rows for map.md | corrected | No earlier full pass was logged, so that pass counts as map.md's first full pass. The rows below are the second. |
| 2026-10-29 | map.md links 1-26 | tags, sources, brief tables | READMEs, CMake, pyproject, .gitmodules (raw files); OSTI/DOE CODE API; contributors API; briefs' related-projects tables | corrected | Corrected: 11 (the ExCL acknowledgement is back in the HeCBench README). Verified: the rest. Brief weaker than map, map not changed: 9 and 26 (hydragnn.md says INFERRED for Frontier; the scripts exist, so KNOWN holds) |
| 2026-10-29 | map.md links 27-60 | tags, sources, brief tables | Myna README and pyproject; neutrons repos; QIR-EE, IRIS and TASMANIAN files; TESViS; FATES README; Cyberwheel README; OSTI 3025007; DOE CODE code-163934; Stor4Build README; contributors API | verified | 34 links checked, no corrections. Unverifiable: 40 (TASMANIAN contributors API hit the rate limit). 31 partly done (Finch contributors hit the rate limit; the Myna-AdditiveFOAM and Myna-HydraGNN overlaps confirmed) |
| 2026-10-29 | map.md links 61-100 | tags, sources, brief tables | OSTI API 1238771, 1231793, 3740812, 3013520, 3013481, 3452355, 1651267, 2283980, 1237627, 3001779; DOE CODE code-115947 and 122128; GITR/KORC/Xolotl LICENSE files; ORNL news on Constellation; contributors API | corrected | Corrected: 84 and 85 (status labels out of date), 86 (title said stub), 97 (LandScan brief now has sweep 2). Verified: the rest. 63 and 83 got superseding notes in the first pass |
| 2026-10-29 | map.md links 101-150 | tags, sources, brief tables | post-processing-agent, live-data-server, Flowcept, Zambeze, IRIS, MatRIS, adamantine, TASMANIAN, QIR-EE, TNQVM, Cabana and ExaGO repo files; OSTI 1513390, 1870235, 2472702, 3001783, 1231809; DOE CODE code-6305, 149694, 45702, 176348; contributors API | corrected | Corrected: 150 (ExaGO now has 22 contributor accounts, not 19; still 4 overlap with GridKit). Verified: the rest |
| 2026-10-29 | map.md links 151-200 | tags, sources, brief tables | XACC NOTICE; OSTI 1339995; DOE CODE code-5041; Cabana, 3DThesis, AdditiveFOAM bin/, ExaCA and OLCF Test Harness files; Crossref JOSS 10.21105/joss.00366; ReSolve README; contributors API | corrected | Corrected: 159 (the DOE CODE date is 2017-01-20; 2016-11-18 is the OSTI record's date), 182 (URL fixed in the first pass). Corrected in prose: 129 and 91 (brief status). Verified: the rest |
| 2026-10-29 | map.md links 201-225 | tags, sources, brief tables | RSICC CCC-855 (WebFetch); OSTI 1831630, 3374533, 1214026, 1615992; DOE CODE code-152916, 123550, 5745; Crossref PHYSOR24-43454; ORNL URBAN-NET news (WebFetch); wufi.de free versions page; TRANSFORM LICENSE.txt | verified | 25 links checked, no corrections. Line 518 (gaps list) corrected: MOOSE, Pronghorn and BISON are now covered by links 52, 211 and 212 |
| 2026-10-29 | map.md code links under personal accounts | swap to official addresses | grep of github.com owners; GitHub users API (type); OLM README; PyPI JSON; WebFetch of the GitLab page; DataCite 10.11578/dc.20240416.1 | verified | No personal-account GitHub links in map.md: all owners are organisations. OLM is already cited at DOE CODE and https://code.ornl.gov/scale/code/olm (copied exactly from the OLM README; WebFetch shows "SCALE / Code / OLM") plus https://pypi.org/project/scale-olm/. HeCBench and Vivaldi are cited at github.com/ORNL (org), so nothing was swapped |
| 2026-10-29 | connections/map.md (whole file, second full pass) | each link: tag no stronger than its source or brief, cited source supports the claim, agrees with the matching brief's table | as in the range rows above | corrected | Second full pass done. 225 links: 214 verified, 9 corrected (11, 84, 85, 86, 97, 150, 159, plus prose fixes in 91 and 129), 1 unverifiable (40), 1 partly done (31). Also corrected the gaps line. Earlier pass fixes: 63, 83, 182 |
| 2026-10-29 | lab-tree-crosslinks | every crosslink tag vs cited map link | connections/map.md | verified | No tag stronger than its map link |
| 2026-10-29 | lab-tree-crosslinks (pass 1 summary) | first full check | map.md | verified | 1 verified (all links), 0 corrected, 0 unverifiable |
| 2026-10-29 | lab-tree-crosslinks (pass 2) | IRIS, Zambeze, Flowcept, SNAPRed, Cabana corroborations | raw repo files | verified | |
| 2026-10-29 | lab-tree-crosslinks (pass 2 summary) | adversarial reread | repos | verified | 5 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | stub-search | six public pages resolve; WUFI facts; CPAD OSTI records; URBAN-NET DOI | HTTP; wufi.de; OSTI API; Crossref | verified | |
| 2026-10-29 | stub-search | Heartbeat report date | OSTI API 2305827 | corrected | OSTI 2022-10-01, ORNL page Feb 2024 |
| 2026-10-29 | stub-search | Heartbeat license: small company, stayed R&D | ORNL news 2024-09-18 (per map 198 fix) | corrected | Neither stated |
| 2026-10-29 | stub-search | KNOWN from unfetched search results (Hyperion licensing, KDD 2019, Akatosh CCS) | RULES 8; Crossref | corrected | Two to INFERRED; Akatosh DOI confirmed in Crossref |
| 2026-10-29 | stub-search | URBAN-NET paper page | doi.org | unverifiable | doi.org error; Crossref record exists |
| 2026-10-29 | stub-search (pass 1 summary) | first full check | as above | corrected | 4 verified, 3 corrected, 1 unverifiable |
| 2026-10-29 | stub-search (pass 2) | WUFI, CPAD, Cincinnatus tag, Heartbeat dates | wufi.de; OSTI API | verified | |
| 2026-10-29 | stub-search (pass 2 summary) | adversarial reread | as above | verified | 4 verified, 0 corrected, 0 unverifiable |
| 2026-10-29 | olm link (scan, reactor connections, OLM brief) | PyPI page + ORNL GitLab mirror | pypi.org; DOE CODE 122128 | verified | Both 200; DOE CODE lists https://code.ornl.gov/scale/code/olm as its repository; catalog row matches |
| 2026-10-29 | shift-exnihilo | lines 63 and 65 tidied | file | verified | Caveat marked superseded; bot name removed |
| 2026-10-29 | project-wide grep | old OLM personal-account URL | all files except log.md | verified | 0 hits |
| 2026-11-02 | connections/map.md link 31 | Myna/Finch/AdditiveFOAM/HydraGNN shared contributors (one in all four, one in Myna+Finch+AdditiveFOAM, one in Myna+AdditiveFOAM) | GitHub contributors API (unauthenticated), 4 repos | verified | All three overlaps confirmed; shared dev is in the top three of each repo |
| 2026-11-02 | connections/map.md link 40 | QIR-EE/TASMANIAN shared developer "a top contributor to both" | GitHub contributors API (unauthenticated), ORNL-QCI/qiree, ORNL/TASMANIAN | corrected | Shared contributor confirmed; top in QIR-EE but sixth of eight in TASMANIAN; wording narrowed, tags unchanged |
| 2026-11-02 | hydragnn | Frontier tie KNOWN (re-look of 2026-10-29 one-line fix) | GitHub contents API scripts/hpc/olcf/frontier/installation; docs.olcf.ornl.gov Frontier user guide | verified | ROCm install scripts present; MI250X in guide |
| 2026-11-02 | flowcept | DataFed tie UNKNOWN (re-look of 2026-10-29 one-line fix) | raw README on main; map link 19 | verified | No DataFed mention; brief matches map |
| 2026-11-02 | situ | cyber-row stub wording (re-look of 2026-10-29 one-line fix) | catalog.csv; projects/; map link 84 | verified | Heartbeat/Hyperion briefs exist; Cincinnatus/CPAD stub-osti-only |
| 2026-11-02 | connections/map.md (pass 2 close) | links 31 and 40 | as above | corrected | 1 verified, 1 corrected, 0 unverifiable; map now two checks on all 225 links |
