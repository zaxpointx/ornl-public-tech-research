# ORNL lab tree

A top-down map of the public technology in this repo: lab, then a division or directorate (only where a public source names one), then research area, then facility or program, then project, then the tools each project uses or feeds. Every project links to its brief. Verification status for each brief is in [INDEX.md](INDEX.md). This is independent research from public sources only, with no ORNL affiliation.

How to read it:
- A **division or group** appears only when a cited source names it. Otherwise the branch stops at the research area.
- A **GitHub org** (like ORNL-MDF or ORNL-Fusion) is where the code lives, not proof of which division owns it. Where it's the only clue, the branch says so and the tie is [INFERRED].
- **Outside** marks projects that aren't ORNL's but connect to ORNL ones. Link numbers like (map 171) point to [connections/map.md](connections/map.md), where each tie has its tag and source.
- The research areas match the catalog's domain labels.

## Oak Ridge National Laboratory

### Neutron science
- **NScD** is named in Mantid's site footer and in post-processing-agent's license [KNOWN, map 53 and projects/post-processing-agent.md]. That it stands for the neutron sciences directorate is [INFERRED].
- **Facilities: SNS (Spallation Neutron Source) and HFIR (High Flux Isotope Reactor)**
  - The data path at the facilities:
    - [Live Data Server](projects/live-data-server.md): serves plots of experiment data while runs are in progress (see brief).
    - [Post Processing Agent](projects/post-processing-agent.md): runs automated data reduction and cataloging when SNS and HFIR runs finish (see brief).
    - [SNS Data Workflow Manager](projects/data-workflow.md): tracks and reports on runs at SNS and HFIR [KNOWN, map 36 and 75].
    - [ONCat](projects/oncat.md): the catalog of neutron experiment data at SNS and HFIR [KNOWN, map 129].
  - Analysis:
    - [Mantid](projects/mantid.md): the shared reduction and analysis framework, built by several institutions [KNOWN, map 53].
      - [SNAPRed](projects/snapred.md): built on Mantid, for the SNAP instrument at SNS [KNOWN, map 4 and 23].
      - [PyRS](projects/pyrs.md): built on Mantid, for residual stress on HFIR's HB2B instrument [KNOWN, map 34 and 37].
  - Unplaced: django-remote-submission (no brief yet), which lives in the ornl-ndav GitHub org. Its tie to the facility tools is [UNKNOWN] (map 38).
- Planned deep dive: this whole branch (GOAL.md, ranking item 1).

### Computing (HPC)
- **NCCS** is named in the OLCF Test Harness developer affiliations [KNOWN, map 76]. CSMD and NCCS/OLCF are named for DataFed [KNOWN, catalog: ORNL/TM-166131].
- **Facility: OLCF (Oak Ridge Leadership Computing Facility), with the supercomputers Summit and Frontier**
  - Operations:
    - [OLCF Test Harness](projects/olcf-test-harness.md): acceptance and regression tests for each new machine, including Frontier test suites [KNOWN, map 43].
    - OLCF User Documentation (no brief yet): the user docs [KNOWN, repo description].
  - Services hosted at OLCF:
    - [DataFed](projects/datafed.md): research data management, with its central services in OLCF [CORROBORATED, map 51 and 128].
  - Projects that build for or run on OLCF machines:
    - [HydraGNN](projects/hydragnn.md): has Frontier install scripts [KNOWN, map 26]. It also feeds power-grid examples (see Grid and energy).
    - [ExaGO](projects/exago.md): has Frontier build scripts [KNOWN, map 170].
    - [ExaTN](projects/exatn.md): has Summit build instructions [KNOWN, map 10]. See Quantum.
    - [Flowcept](projects/flowcept.md): acknowledges OLCF resources [KNOWN, map 8].
    - [HeCBench](projects/hecbench.md): GPU benchmark kernels, several taken from OLCF training material [KNOWN, map 155]. An older README credited ExCL (Experimental Computing Laboratory), but the current one doesn't, so that tie is [UNKNOWN] now (map 11).
    - [Shift / Exnihilo](projects/shift-exnihilo.md): GPU transport work on Frontier [KNOWN, map 94]. See Nuclear.
- **Program: ECP (Exascale Computing Project)**
  - [Cabana](projects/cabana.md): particle and grid library from the ECP CoPA project, built on Kokkos (outside) [KNOWN, map 146].
    - It feeds [Finch](projects/finch.md) (see Materials).
- **Program: ORNL LDRD (Laboratory Directed Research and Development), project 11521 (INTERSECT)**
  - [Flowcept](projects/flowcept.md) with [Zambeze](projects/zambeze.md): workflow tools paired in the same project [KNOWN, map 113 and 114]. Current Flowcept doesn't support Zambeze (projects/zambeze.md).
- Other computing tools (no facility named):
  - [IRIS](projects/iris.md): runtime for mixed hardware. It uses [QIR-EE](projects/qiree.md) as a device backend [KNOWN, map 117].
    - [MatRIS](projects/matris.md): BLAS and LAPACK math library built on IRIS (see brief). Status unknown.
  - [TASMANIAN](projects/tasmanian.md): sparse grids and uncertainty quantification.
  - [ReSolve](projects/resolve.md): GPU linear solvers. It feeds GridKit (see Grid and energy).
- Planned deep dive: supercomputer operations (GOAL.md, ranking item 2).

### Quantum computing
- **GitHub org ORNL-QCI** (it's the only placement clue for this whole branch) [KNOWN org; ownership INFERRED].
  - [XACC](projects/xacc.md): quantum programming framework [CORROBORATED ORNL tie, map 159].
    - [TNQVM](projects/tnqvm.md): XACC's tensor-network simulator backend. It uses [ExaTN](projects/exatn.md).
  - [QIR-EE](projects/qiree.md): runs quantum programs written in QIR. Used by [IRIS](projects/iris.md).

### Materials and manufacturing
- **Facility: MDF (Manufacturing Demonstration Facility)** [KNOWN for Myna, map 71]. The others live in the ORNL-MDF GitHub org [INFERRED placement].
  - [Myna](projects/myna.md): workflow tool built around MDF's Peregrine database. It drives the simulation codes below [KNOWN, map 27, 30 and 124].
    - The 3D-printing heat models, from fastest to most detailed:
      - [3DThesis](projects/3dthesis.md): quick thermal estimate. It feeds ExaCA (outside) [KNOWN, map 172].
      - [Finch](projects/finch.md): GPU grid model built on Cabana. It feeds ExaCA [CORROBORATED, map 171].
      - [AdditiveFOAM](projects/additivefoam.md): full heat and melt-pool flow, built on OpenFOAM (outside).
    - [adamantine](projects/adamantine.md): heat transfer and thermomechanics simulation, funded by LDRD and EERE [KNOWN, map 125].
  - Outside: ExaCA (grain growth) and Stork (an optional library whose identity is [UNKNOWN], map 174).
- Planned deep dive: the 3D-printing ladder (GOAL.md, ranking item 3).

### Nuclear and fusion
- **Reactor and Nuclear Systems Division, Radiation Transport Group** [KNOWN, single source, map 101]
  - [Shift / Exnihilo](projects/shift-exnihilo.md): Monte Carlo radiation transport. Shift ships inside SCALE [CORROBORATED, map 82].
- Reactor analysis (no division named):
  - [SCALE](projects/scale.md): nuclear safety and criticality suite (ornl.gov/scale).
    - ORIGEN Library Manager (OLM) (no brief yet): SCALE project group on code.ornl.gov [INFERRED].
  - [VERA](projects/vera.md): reactor multiphysics from the CASL program (ornl.gov/onramp/casl-vera).
- **CEES (Computational Engineering and Energy Sciences Group)**, named by its GitHub org [INFERRED]
  - [Thermochimica](projects/thermochimica.md): thermodynamic equilibrium solver, wired into nuclear fuel codes (signals/thermochimica.md).
- Fusion, in the GitHub org ORNL-Fusion [INFERRED placement]:
  - [Xolotl](projects/xolotl.md): plasma-surface materials. Multi-institution copyright with UT-Battelle first [KNOWN, map 136].
  - [GITR](projects/gitr.md): impurity transport. It's a component of the STRIPE framework (outside) [KNOWN, map 92].
  - [KORC](projects/korc.md): runaway electrons in fusion plasmas.
  - FAR3d (no brief yet): models plasma instabilities driven by fast particles (stub).

### Grid and energy
- No division named.
  - [GridKit](projects/gridkit.md): power grid dynamics. It uses [ReSolve](projects/resolve.md) and shares its lead developer [KNOWN, map 7].
  - [ExaGO](projects/exago.md): grid optimization, with Frontier builds.
  - [HydraGNN](projects/hydragnn.md): power-flow examples [CORROBORATED, map 127].
  - Hydropower Fleet Intelligence (no brief yet): status unknown.
  - URBAN-NET-TOOLKIT: OSTI record only (stub).
- Planned deep dive: the grid tools (GOAL.md, ranking item 4).

### Climate and earth
- **Environmental Sciences Division** [KNOWN, daymet.ornl.gov]
  - [Daymet](projects/daymet.md): daily weather surfaces for North America.
- **ORNL DAAC (Distributed Active Archive Center)** [KNOWN, map 44 and 45]
  - [Daymet](projects/daymet.md): listed twice on purpose. The science comes from Environmental Sciences, and ORNL DAAC distributes the data and hosts its helper repo.
  - [TESViS](projects/tesvis-modis.md): satellite data subsets, operated by ORNL DAAC with LP DAAC. It serves GEDI subsets [KNOWN, map 73].
  - ORNL DAAC GEDI Tutorials (no brief yet).
- Other:
  - [E3SM Land Model (ELM)](projects/e3sm-elm.md): a multi-lab model. ORNL is a research org on specific ELM work, and its datasets carry OLCF DOIs [KNOWN, map 77 and 78].
  - [LandScan](projects/landscan.md): population distribution datasets (a dataset, not software).

### Buildings and transportation
- No division named.
  - [EnergyPlus](projects/energyplus.md): building energy simulation. It's multi-lab, with ORNL as one co-owner [KNOWN, map 61].
  - [AutoBEM](projects/autobem.md): automatic building energy models.
  - [Roof Savings Calculator Suite](projects/roof-savings-calculator.md): OSTI-only draft.
  - WUFI-ORNL/IBP: a joint ORNL and Fraunhofer IBP program [KNOWN, map 89] (stub).
  - Stor4Build (no brief yet): co-developed with NREL [KNOWN, map 60].
  - [Real-Twin](projects/real-twin.md) and [FIXS](projects/fixs.md): transportation simulation tools.
  - [Gauntlet](projects/gauntlet.md): sponsored by FEMA and FEMP, per its OSTI record (signals/gauntlet.md).

### Cybersecurity
- **Program: ORNL LDRD**
  - [Cyberwheel](projects/cyberwheel.md): a reinforcement-learning network defense test bed [CORROBORATED, map 56]. There's a full deep dive in [deep-dives/cyberwheel](deep-dives/cyberwheel/).
- OSTI records only:
  - [Situ](projects/situ.md) (draft).
  - Stubs: Akatosh, CAN-D, Cincinnatus, Heartbeat Malware Detection, CPAD and Hyperion.
- Other: TASQC (no brief yet), status unknown.

### AI and data
- Vivaldi (no brief yet) and Mind the Gap (no brief yet): building-data machine learning tools [INFERRED common domain, map 48].
- Cross-listed above: [HydraGNN](projects/hydragnn.md), [Flowcept](projects/flowcept.md) and [DataFed](projects/datafed.md).

## Cross-links

These ties cross branches or add detail inside one. They're merged from [connections/lab-tree-crosslinks.md](connections/lab-tree-crosslinks.md), which the connections pass prepared, and each one cites its map link. Ties tagged only [UNKNOWN] and namesakes tagged [UNRELATED] are left out.

**Shared facilities beyond the main branches**
- E3SM ELM datasets carry OLCF DOIs (map 78) [KNOWN].
- AutoBEM's Model America dataset has an OLCF DOI, but its computing ran at ALCF (map 99) [KNOWN].

**Funding programs that cross areas**
- ECP funded ReSolve (map 7) [KNOWN] and Cabana's CoPA project (map 146) [CORROBORATED]. Finch's ECP tie is only indirect, through Cabana (map 50) [INFERRED].
- LDRD funded Cyberwheel (project 11049, map 56) [CORROBORATED], Flowcept and Zambeze (project 11521, map 113) [KNOWN], and adamantine, alongside EERE (map 125) [KNOWN].
- DOE's Office of Electricity funded HydraGNN's power-grid models (map 127) [CORROBORATED].

**Code handed from one project to the next**
- Inside the neutron pipeline: post-processing-agent uses Mantid and feeds ONCat (map 74 and 104) [KNOWN], and continues the older mantidproject/autoreduce code (map 105) [KNOWN]. data-workflow uses post-processing-agent and is a sibling of live-data-server (map 91) [KNOWN]. post-processing-agent probably feeds live-data-server (map 107) [INFERRED].
- In 3D printing, Myna drives 3DThesis, AdditiveFOAM, adamantine and ExaCA (map 27 to 29 and 70) [KNOWN]. AdditiveFOAM also feeds ExaCA (map 173) [KNOWN].
- ExaGO continues the archived PNNL ExaGO code (map 148). The code reuse is [KNOWN], but calling it a continuation is [INFERRED]. ExaGO and GridKit share contributor accounts but no code (map 150) [KNOWN].
- Thermochimica feeds INL's MOOSE (map 52) [CORROBORATED], and OLM uses SCALE's ORIGEN (map 62) [KNOWN].
- In quantum, QIR-EE can use XACC as a backend, so IRIS reaches XACC through QIR-EE (map 144 and 151) [KNOWN].
- HeCBench includes a kernel taken from HydraGNN (map 3 and 157) [KNOWN].
- LandScan HD/USA was succeeded by Global/Mosaic (map 102) [KNOWN].
- In buildings and geospatial: AutoBEM feeds Model America, which feeds EnergyPlus and OpenStudio (map 98) [CORROBORATED]. Stor4Build uses EnergyPlus (map 59) [KNOWN]. Vivaldi uses Gauntlet, and Gauntlet feeds USA Structures (map 58 and 90) [KNOWN].

**Shared outside tools**
- Kokkos sits under Cabana, Xolotl and adamantine (map 137, 146 and 147) [KNOWN]. TASMANIAN ships in xSDK (map 134) [KNOWN].
- DataFed uses Globus (map 17) [KNOWN]. Cyberwheel builds on Sandia's FIREWHEEL (map 54) [CORROBORATED]. Real-Twin uses SUMO, VISSIM and AIMSUN (map 80) [KNOWN].
- FATES (LANL) runs inside E3SM ELM (map 46) [KNOWN]. TESViS serves Daymet subsets (map 72) [KNOWN].

**Neutron and fusion ties added in pass 22**
- [SNAPRed](projects/snapred.md) uses [Mantid](projects/mantid.md) as its core backend (map 2) [KNOWN], and serves the SNAP instrument at SNS (map 23) [CORROBORATED].
- [PyRS](projects/pyrs.md) uses Mantid, including its peak fitting (map 34) [KNOWN], for the HB2B instrument at HFIR (map 37) [KNOWN].
- PyRS and the 3D-printing heat models ([AdditiveFOAM](projects/additivefoam.md), [3DThesis](projects/3dthesis.md), [Finch](projects/finch.md)) share a domain only: the models predict the heat history that causes residual stress, and PyRS measures it. This is an untested pairing with no code or file tie (map 175) [INFERRED].
- [KORC](projects/korc.md) uses outside libraries PSPLINE, fusion-io, HDF5 and OpenACC (map 176) [KNOWN].
- KORC and [GITR](projects/gitr.md) share the ORNL-Fusion GitHub org and no contributor accounts; both are particle-tracking codes for fusion devices, with no code tie (map 177) [KNOWN org; domain INFERRED].

## Not on the tree

Kokkos, HiOp, ExaCA, FATES, MOOSE, Stellarator-Tools and pyxodr3d are outside projects. See the Outside projects section in [INDEX.md](INDEX.md).
