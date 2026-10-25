# ORNL Public Technology Research: Index

Curated entry point. Independent research from public sources only. We are not affiliated with ORNL.

Status key: **verified** means the brief was fact-checked (see [verification/log.md](verification/log.md)). **unverified** means a brief exists but hasn't been checked yet. **sweep 1 done** means the fact-check pass finished the first check; it counts as verified only after sweep 2 (RULES.md item 11). **stub** means the project is only in the catalog, with no brief. **row checked** means the catalog row itself was spot-checked. **OSTI-only stub** (catalog status `stub-osti-only`) means the only public source is an OSTI record; it gets a brief only once a public docs page exists.

Projects: 68 cataloged, 46 full briefs linked (43 verified, 3 unverified) plus 2 OSTI-only drafts (both verified), so 45 verified briefs in total. After batch 04 the total was 24 (22 full plus 2 drafts); batch 05 brings it to 28, batch 06 to 34, batch 07-08 to 39 batch 09 (ExaTN, new; GridKit, rewritten) to 40, and batch 10 (ReSolve, 3DThesis, Finch, AdditiveFOAM, TNQVM) to 45. Batches: [01](batches/batch-01.md), [02](batches/batch-02.md), [03](batches/batch-03.md), [04](batches/batch-04.md), [05](batches/batch-05.md) (closed: 4 of 4 verified), [06](batches/batch-06.md) (closed: 6 of 6 verified), [07-08](batches/batch-07-08.md) (combined; closed: 5 of 5 verified; kokkos and hiop kept off the catalog under rule 13). Batch 09 (open): gridkit rewrite and exatn verified; the note on whether current Flowcept supports Zambeze is in the zambeze brief, awaiting its check. Catalog scope rule: RULES.md item 13.

## AI/data
- [HydraGNN](projects/hydragnn.md): graph neural networks that predict material and molecule properties, trained at supercomputer scale. Verified; one line on outside use changed 2026-10-24 from the signals pilot (mostly in-house use, INFERRED), the fact-check pass rechecked and confirmed.
- [DataFed](projects/datafed.md): one shared catalog for finding, sharing and moving scientific data across facilities, with central services at OLCF. Verified.
- [Flowcept](projects/flowcept.md): records what happened during AI and science workflow runs (provenance), MIT licensed. Batch 06. Verified (two sweeps, 2026-10-24). [Signals](signals/flowcept.md).
- Vivaldi: machine learning that estimates building heights. Stub, stale.
- Mind the Gap: finds areas missing from building-footprint datasets. Stub.

## HPC
- [HeCBench](projects/hecbench.md): 555 small GPU benchmarks, each in some or all of CUDA, HIP, SYCL and OpenMP, for comparing NVIDIA, AMD and Intel GPUs (ORNL and Argonne in LICENSE). Batch 06. Verified (two sweeps, 2026-10-24). [Signals](signals/hecbench.md).
- [ReSolve](projects/resolve.md): GPU linear-equation solvers, used by GridKit. Batch 10. Verified (two sweeps, 2026-10-24).
- [TASMANIAN](projects/tasmanian.md): sparse-grid stand-in models and DREAM sampling for estimating uncertainty in simulations. Batch 06. Verified (two sweeps, 2026-10-24). [Signals](signals/tasmanian.md).
- [Zambeze](projects/zambeze.md): orchestrates workflow tasks across large HPC systems and edge devices; can load Flowcept to record runs. Batch 07-08. Status unknown (last push 2024-09-13). Verified (two sweeps, 2026-10-24). [Signals](signals/zambeze.md).
- [MatRIS](projects/matris.md): BLAS and LAPACK math library built on the IRIS runtime (IRIS is a required build dependency); GEMM demo is a proof of concept. Batch 07-08. Status unknown (editorial decision 2026-10-24: no push since 2025-10-23, no tagged release). Verified (two sweeps, 2026-10-24). [Signals](signals/matris.md).
- [Cabana](projects/cabana.md): particle-simulation library from the multi-lab CoPA co-design center, built on Kokkos (ORNL is a named lab and DOE CODE research org). Batch 07-08. Verified (two sweeps, 2026-10-24). [Signals](signals/cabana.md).
- [IRIS](projects/iris.md): a runtime that lets one program use several kinds of processors. Batch 06. Verified (two sweeps, 2026-10-24). [Signals](signals/iris.md).
- OLCF User Documentation: source for the public user guides of OLCF systems like Frontier. Stub.
- [OLCF Test Harness](projects/olcf-test-harness.md): runs test suites on OLCF supercomputers like Frontier (NCCS developers). Verified.

## Neutrons
- [Mantid](projects/mantid.md): multi-institution framework for reducing and analyzing neutron and muon scattering data. ORNL Neutron Sciences is one co-owner. Verified.
- [SNAPRed](projects/snapred.md): app for handling data from the SNAP instrument at SNS, built on Mantid. Batch 11. Unverified.
- [SNS Data Workflow Manager](projects/data-workflow.md): tracks automated processing of SNS and HFIR experiment data and ties into Mantid through livereduce. Verified.
- [PyRS](projects/pyrs.md): works out hidden stress inside metal parts from neutron scans on HFIR's HB2B instrument, without cutting them open. Batch 11. Unverified.
- [ONCat](projects/oncat.md): searchable catalog of SNS and HFIR neutron experiment data, with an API and Python client (pyoncat on PyPI). No public source repo; the pyoncat client ships GPL-3.0. Batch 05. Verified. Editorial decision 2026-10-24: public overview/docs pages and any public client repo only; no API calls, no logins; anything needing credentials is out of scope (RULES.md item 16).
- [Post Processing Agent](projects/post-processing-agent.md): runs automated data reduction and cataloging when SNS and HFIR runs finish. Verified.
- [Live Data Server](projects/live-data-server.md): serves plots of neutron experiment data while runs are in progress (Django and Postgres). Verified.
- django-remote-submission: job queue for sending work to remote servers from a Django web app. Stub, stale.

## Nuclear/fusion
- [Thermochimica](projects/thermochimica.md): calculates chemical equilibrium (which phases and compounds form), used in nuclear fuel modeling. Verified.
- [Xolotl](projects/xolotl.md): simulates damage building up in fusion-reactor walls and fission fuel as clusters of trapped atoms move and merge (C++ on PETSc and Kokkos; README says under development). Batch 06. Verified (two sweeps, 2026-10-24). [Signals](signals/xolotl.md).
- Stellarator-Tools: community codes for modeling stellarator fusion devices (includes PARVMEC and LIBSTELL). Stub.
- FAR3d: models plasma instabilities driven by fast particles in tokamaks and stellarators. Stub.
- [KORC](projects/korc.md): follows runaway electrons in fusion plasmas. Batch 11. Unverified.
- [GITR](projects/gitr.md): tracks impurity particles worn off fusion device walls. Verified.
- [SCALE](projects/scale.md): nuclear safety analysis suite (reactor physics, criticality, shielding, spent fuel). Public overview only, since the software is distributed through a controlled channel. Verified.
- ORIGEN Library Manager (OLM): manages the reactor data libraries SCALE uses for fast spent-fuel calculations. Stub.
- [VERA](projects/vera.md): couples several physics codes to simulate a whole reactor core rod by rod. Public overview only. Verified.
- [Shift / Exnihilo](projects/shift-exnihilo.md): parallel Monte Carlo radiation transport (runs on GPUs like Frontier), distributed within SCALE. Public pages only; Radiation Transport Group credit per OSTI 1237627. Verified.

## Grid/energy
- [GridKit](projects/gridkit.md): simulates how a power grid reacts when something fails, like a line dropping out for a split second, and whether generators settle back down; young (v0.2) but actively developed. Rewritten in batch 09. Verified (two sweeps, 2026-10-24).
- Hydropower Fleet Intelligence: brings hydropower plant data together for fleet-wide analysis. Stub, stale.
- [ExaGO](projects/exago.md): power grid optimization at large scale; moved from PNNL to ORNL (UT-Battelle 2026); v2.1 adds an experimental LLM-driven tool (AgentiGrid). Batch 07-08. Verified (two sweeps, 2026-10-24). [Signals](signals/exago.md).
- URBAN-NET-TOOLKIT: geospatial tool for how critical infrastructure systems depend on each other [INFERRED from title]. OSTI-only stub.

## Climate/earth
- GEDI Tutorials: how-tos for NASA GEDI forest structure and biomass data (ORNL DAAC). Stub.
- [Daymet](projects/daymet.md): daily 1 km weather grids for North America, plus a pixel-extraction tool. Verified.
- [TESViS](projects/tesvis-modis.md): web tool and API for small satellite land-data subsets (MODIS/VIIRS). Verified.
- [E3SM Land Model (ELM)](projects/e3sm-elm.md): the land part of DOE's E3SM climate model. Multi-lab code. ORNL's specific contributions (km-scale North America framework, 1 km input datasets) are KNOWN, but ownership and the land-group lead are unknown. Verified.
- [LandScan](projects/landscan.md): population distribution datasets down to about 100 m resolution (a dataset, not software). Licensed CC BY 4.0 per the site's own text. Verified.

## Materials
- [AdditiveFOAM](projects/additivefoam.md): full simulation of heat and molten-metal flow in 3D printing, built on OpenFOAM. Batch 10. Verified (two sweeps, 2026-10-24).
- [3DThesis](projects/3dthesis.md): fast thermal model of melt pools in 3D printing; the quick-estimate rung of the 3D-printing heat models. Batch 10. Verified (two sweeps, 2026-10-24).
- [Myna](projects/myna.md): links additive manufacturing simulations with experiment databases. Verified.
- [Finch](projects/finch.md): thermal solver for additive manufacturing, built on the Cabana library; faster GPU grid model between 3DThesis and AdditiveFOAM. Batch 10. Verified (two sweeps, 2026-10-24).
- [adamantine](projects/adamantine.md): simulates heat transfer and thermomechanics in additive manufacturing (ORNL is a research org per OSTI 2472702; Apache-2.0 with LLVM exception since release 1.1, 2026-01-23). Batch 05. Verified.

## Quantum
- [ExaTN](projects/exatn.md): breaks math too big for memory (tensor networks) into pieces that run across GPUs; it is the engine TNQVM uses to simulate quantum circuits for XACC. Status unknown (no commits since mid-2023, no tagged release). Batch 09. Verified (two sweeps, 2026-10-24).
- [QIR-EE](projects/qiree.md): runs quantum programs written in QIR (an LLVM-based format) on qsim, XACC backends or a Lightning simulator; one release, v0.1.0 (2026-05-05). Batch 06. Verified (two sweeps, 2026-10-24). [Signals](signals/qiree.md).
- [TNQVM](projects/tnqvm.md): tensor-network quantum circuit simulator that plugs into XACC (UT-Battelle header, OSTI names ORNL). Batch 10. Verified (two sweeps, 2026-10-24). Status unknown; README says BSD-3 but no LICENSE file in the repo.
- [XACC](projects/xacc.md): framework for programming quantum computers and simulators from C++ or Python; UT-Battelle copyright plus DOE CODE code-5041 (ORNL tie CORROBORATED); EPL-1.0 or EDL-1.0. Batch 07-08. Status unknown (last default-branch commit 2023-08-01); no successor named in public sources. Verified (two sweeps, 2026-10-24). [Signals](signals/xacc.md).

## Cyber
- [Cyberwheel](projects/cyberwheel.md): a reinforcement-learning simulator for training AI agents that defend networks. Verified, borderline active (whether it's still developed is unverifiable).
- TASQC: uses quantum correlations to authenticate grid timing signals. Stub.
- Akatosh: pairs intrusion-detection alerts with automated forensic checks to cut false alarms. OSTI-only stub.
- CAN-D: works out what the signals in raw vehicle CAN bus logs mean. OSTI-only stub.
- Cincinnatus: flags changes in binary data that may mean a breach or fraud. OSTI-only stub.
- Heartbeat Malware Detection: aims to catch stealthy malware that signature tools miss. OSTI-only stub.
- CPAD: spots attacks by learning the physical relationships in sensor data. OSTI-only stub.
- Hyperion: works out what a program does without running it. OSTI-only stub.

## Buildings/transport
- [Gauntlet](projects/gauntlet.md): computes shape measures for each building footprint, used by Vivaldi. Verified.
- [Real-Twin](projects/real-twin.md): builds standard traffic-simulation scenarios for testing new mobility tech. Verified.
- Stor4Build: simulates thermal energy storage built into buildings (ORNL and NREL). Stub.
- [EnergyPlus](projects/energyplus.md): whole-building energy simulation. Multi-institution, with ORNL as one copyright holder. Verified.
- [FIXS](projects/fixs.md): links traffic simulators with real vehicle and hardware tests (formerly Real-Sim), MIT licensed. Verified.
- pyxodr3d: Python package for reading and converting OpenDRIVE road maps. Stub.
- [AutoBEM](projects/autobem.md): automatically builds energy models for huge numbers of buildings. The code is closed source per OSTI, but its Model America dataset (122.9M building models) has been publicly downloadable since 2021-04-14; those runs used Argonne's computing facility. Verified, status unknown.
- WUFI-ORNL/IBP: models heat and moisture moving through walls, with Fraunhofer IBP. OSTI-only stub.

## Signals (outside-in pilot)
Public traces each project leaves (git history, build targets, funding records, reverse dependencies, downloads, citing papers), per RULES.md items 15-16. The discovery pass writes history, build and funding; the connections pass writes who actually uses it. The fact-check pass swept all three on 2026-10-24 (8 verified, 2 corrected, job-trace and commit-metadata rows moved out of scope). From batch 06 every project gets a signals file (RULES.md item 17); all six batch 06 files and all five batch 07-08 files have both the discovery-pass and the connections-pass sections.
- [Cyberwheel](signals/cyberwheel.md): no commits since 2025-08-26, no CI or HPC targets, not on any package index; reads as a finished LDRD study, used by researchers who clone it plus 3 papers.
- [HydraGNN](signals/hydragnn.md): Frontier is the main build target and it is expanding into power grid models (OSTI 3377970, Office of Electricity); visible use is mostly in-house (INFERRED).
- [DataFed](signals/datafed.md): commits jumped from 58 (2022) to 1,406 (2024), pointing to new funding (INFERRED); org unit traceable to NCCS/OLCF with CSMD; one outside application (EcoKMER) names it.

## Deep dives
Full reconstructions per RULES.md (deep-dives section).
- Cyberwheel ([brief](projects/cyberwheel.md)): [synthesis](deep-dives/cyberwheel/synthesis.md), [timeline](deep-dives/cyberwheel/timeline.md), [system flow](deep-dives/cyberwheel/system-flow.md), [people and roles](deep-dives/cyberwheel/people-roles.md), [claim boundary](deep-dives/cyberwheel/claim-boundary.md) (the reading pass: what sources say vs. what we infer) and [lineage](deep-dives/cyberwheel/lineage.md) (the connections pass: FIREWHEEL origin, LDRD 11049). The fact-check pass: [source ledger](deep-dives/cyberwheel/source-ledger.md) (13 sources), [missing artifacts](deep-dives/cyberwheel/missing-artifacts.md) (11 gaps) and [verification report](deep-dives/cyberwheel/verification-report.md). Verified; open items are the exact Firewheel modification, division-level owner and outside authors' affiliations.

## Draft OSTI-only briefs
Written from OSTI records alone (no public docs page found). Kept so the work isn't lost; not full briefs.
- [Situ](projects/situ.md): finds new attacks in network traffic and gives analysts context. Records from 2013-14 only. Verified as a draft.
- [Roof Savings Calculator](projects/roof-savings-calculator.md): estimates energy savings from cool roofs and attic changes. roofcalc.com was unreachable on 2026-10-24. Verified as a draft.

## Outside projects (not in catalog)
These failed the scope rule (no primary source names ORNL) and live in [connections/map.md](connections/map.md) only.
- ExaCA: grain-structure simulation for additive manufacturing, LLNL repo and DOE CODE record. Driven by Myna.
- FATES: vegetation dynamics model that runs inside ELM. OSTI lists Los Alamos.
- Kokkos: C++ library for writing code once and running it on many CPUs and GPUs; multi-lab Linux Foundation project. ORNL is listed as a contributor organization, not owner; DOE CODE research org is Sandia. Used by Cabana, Xolotl and adamantine.
- HiOp: optimization solver, an optional outside dependency of ExaGO; LLNL holds the copyright.
- UQTk: Sandia uncertainty toolkit used by Xolotl's scripts.

## Repo map
- [RULES.md](RULES.md): team rules, brief template, layout
- [discovery/catalog.csv](discovery/catalog.csv): master project list
- [verification/log.md](verification/log.md): source checks
- [connections/map.md](connections/map.md): how projects relate
- [verification/not-found.md](verification/not-found.md): searches that came up empty
- [deep-dives/](deep-dives/): full project reconstructions
- [signals/](signals/): outside-in signals per project (RULES.md items 15-16)
- [batches/](batches/): per-batch summaries

Last updated: 2026-10-24 (batches 01-02 verified; batches 03-04 verified after two sweeps; batch 05 closed with all 4 verified; signals pilot swept; batch 06 briefs in progress; batch 04-05 rows listed as stubs; exaca and fates moved out under the scope rule)
