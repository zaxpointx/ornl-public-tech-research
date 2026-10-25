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
| 2026-10-24 | map.md #5,#31 | streeve top contributor to HydraGNN, AdditiveFOAM (and Myna) | GitHub contributors API | verified | same team correctly INFERRED |
| 2026-10-24 | map.md #6 | PhilipFackler top contributor to Xolotl and GridKit | GitHub contributors API | verified | split correct |
| 2026-10-24 | map.md #7 | pelesh top contributor to GridKit and ReSolve | GitHub contributors API | verified | split correct |
| 2026-10-24 | map.md #39,#40 | miniskar/wongey on QIR-EE+IRIS; sethrj on QIR-EE+TASMANIAN | GitHub contributors API | verified | split correct |
| 2026-10-24 | map.md #65 | cianciosa top contributor to KORC and Stellarator-Tools | GitHub contributors API | verified | split correct |
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
| 2026-10-24 | hecbench | Repo identity | github.com/zjin-lcf/HeCBench is a fork (API parent ORNL/HeCBench) | verified | namesake guard; cite ORNL repo |
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
