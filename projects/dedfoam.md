# DEDFoam (repo name DEDFOAM)

- Official page: none separate. The repo carries a Sphinx docs source in `doc/source/`, but no hosted docs site is linked from the repo or GitHub's homepage field. [KNOWN: GitHub API `homepage` empty; repo tree at d298a00]
- Repo: https://github.com/ORNL/DEDFOAM (default branch `main`, HEAD `d298a0020c8aea7e8024d6022a5cedfce12c049b`). GitHub description: "High-fidelity simulations of directed energy deposition in the OpenFOAM framework." [KNOWN: GitHub API, accessed 2026-11-11]
- Docs: README plus `doc/source/*.md` (installation, per-machine build guides, usage, input files). The `doc/source/license.md` page still reads "TODO: Add license info." [KNOWN: https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/doc/source/license.md]
- License: GPL version 3 or (at your option) any later version. LICENSE header: "Copyright (C) 2011-2017 OpenFOAM Foundation" and "Copyright (C) 2026 Oak Ridge National Laboratory". GitHub's API shows NOASSERTION; Zenodo lists gpl-3.0-or-later. [KNOWN: https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/LICENSE#L1-L8, README L39-L40, Zenodo record 21708850]
- Status: active (rule 14). Created 2026-07-28; one release, v1.0 (2026-07-30); last push 2026-07-30. Not archived. [KNOWN: GitHub API]
- ORNL relationship: CORROBORATED. (1) Repo owner is the main github.com/ORNL org. (2) LICENSE names ORNL as copyright holder. (3) DOE CODE code-186894 lists "Research Org.: Oak Ridge National Laboratory (ORNL), Oak Ridge, TN (United States)", sponsor EERE AMMTO, contract AC05-00OR22725. [KNOWN: GitHub API; LICENSE L3; https://www.osti.gov/doecode/biblio/186894 via OSTI API https://www.osti.gov/api/v1/records/code-186894]
- Years visible in public sources: 2026 to 2026
- Last checked: 2026-11-11

## Walkthrough (plain language)
- **What it is:** a simulation code for *directed energy deposition* (DED), a kind of metal 3D printing where metal powder is blown into a laser spot and melts onto the part. It is built on OpenFOAM, a free fluid-dynamics toolkit. [KNOWN: README L2]
- **The problem:** in DED, the laser melts a small pool on the part while powder streams in. How much powder actually lands and sticks (the *catchment efficiency*), how the melt pool flows, and how the new bead's surface takes shape all decide the printed geometry. Measuring this directly is hard, so engineers simulate it. [KNOWN: README names catchment efficiency; INFERRED: the framing]
- **Key terms:**
  - *VOF (volume of fluid)*: each mesh cell stores the fraction filled with metal versus gas (`alpha.metal`), which lets the code track a moving free surface. [KNOWN: README L2; field names in `regression_tests/.../restart/`]
  - *Lagrangian particles*: individual powder particles (or parcels of them) tracked as they fly, rather than as a smeared-out field. [KNOWN: README L2, `basicThermoCloud.H` include in DEDFoam.C]
  - *Marangoni force*: flow driven by surface-tension differences between hot and cold spots on the melt pool. [KNOWN: `Marangoni.H`; INFERRED: definition]
- **What goes in:** an OpenFOAM case folder: mesh, metal and air thermophysical properties, a powder-cloud description (`constant/powderProperties`), laser and powder settings in `constant/fvOptions` (for example catchment efficiency `eta_mass`, laser shape factor, powder source radius), and a scan path. [KNOWN: https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/tutorials/singleTrackDED/constant/fvOptions#L35-L38 and #L69-L71]
- **What happens:** each time step the solver moves the powder particles, decides which ones join the melt pool, then solves the metal fraction, momentum, temperature and pressure in turn (details under How it works). [KNOWN: DEDFoam.C L160-L206]
- **What comes out:** OpenFOAM time folders with temperature, velocity, metal fraction and source-term fields such as `q_laser`, `mDot`, `qDotPowder`. [KNOWN: regression gold/restart file names]
- **Where humans act:** a researcher builds the case, picks either a particle-resolved powder model or an assumed (Gaussian or uniform) powder distribution, and either sets catchment efficiency by hand or switches on a small ML model to predict it. [KNOWN: README L2; `alphaSuSp.H`; `createFieldsDEDFoam.H` L49-L91]
- **What it is not:** it is not a powder-bed (laser powder bed fusion) code, a residual-stress model, or a standalone program; it needs an existing OpenFOAM install. [KNOWN: README L5, L8; INFERRED: scope]
- **What's unknown:** who uses it outside the team, what validation data back the two tutorial cases (the README says "validated on a variety of material systems" without citations), and whether a paper describes it. [KNOWN: README L2; UNKNOWN: the rest]
- **Example:** `tutorials/singleTrackDED` prints one DED bead and has three run scripts: `Allrun` (assumed powder distribution), `AllrunLagrangian` (particle-resolved) and `AllrunML` (catchment efficiency from the ML model). [KNOWN: tutorials tree]

## What it is (plain English, 2-4 sentences)
DEDFoam is an OpenFOAM solver plus helpers for simulating blown-powder metal 3D printing at the scale of a single melt pool. It tracks the metal-gas surface with VOF, solves flow and heat, and adds powder either as tracked particles or as an assumed distribution. Optional add-ons offload the linear solves to GPUs through PETSc and predict powder catchment with a TensorFlow Lite model. [KNOWN: README L2, L5]

## How it works (plain English, no jargon without definition)
The solver `DEDFoam` started from OpenFOAM's `compressibleInterFoam` (a two-phase, compressible, non-isothermal VOF solver) and adds DED physics. [KNOWN: header "Solver for directed energy depositon. Based on the compressibleInterFoam solver", https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/DEDFoam.C#L32-L36]

1. **Powder flight.** If the Lagrangian cloud is active, the code stores particle positions and calls `powder.evolve()` to move parcels and update their heat. [KNOWN: DEDFoam.C L160-L168]
2. **Powder capture.** `powderInteraction.H` loops over cells and applies three rules: a particle hitting solid metal is deleted as lost; one hitting a cell already full of metal is deleted for now (a TODO notes a planned redistribution); one hitting a partly filled cell adds its mass and energy there, with a momentum term from a Reynolds-number drag estimate. [KNOWN: https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/powderInteraction.H#L57-L101]
3. **Assumed-distribution alternative.** Without particles, `alphaSuSp.H` adds a Gaussian or uniform mass source on the melt-pool surface, only in cells above liquidus temperature, scaled by catchment efficiency `eta_mass`. [KNOWN: https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/alphaSuSp.H#L1-L26]
4. **Inner PIMPLE loop** (OpenFOAM's pressure-velocity coupling loop): solve the metal fraction (`compressibleAlphaEqnSubCycle.H`), then momentum (`UEqn.H`, including surface tension and an optional Marangoni term), temperature (`TEqn.H`), and pressure (`pEqn.H`). [KNOWN: DEDFoam.C L185-L206; https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/Marangoni.H#L30-L36]
5. **Heat sources.** The built-in laser is a Gaussian-type surface flux applied through the interface gradient, minus the power already absorbed by the powder, plus convection and radiation losses. [KNOWN: https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/qDot.H#L66-L85] Phase change uses a liquidus/solidus mushy-zone latent-heat treatment. [KNOWN: `thermoSource.H` L14-L40] Optionally, AdditiveFOAM's moving heat-source library can be plugged in as an OpenFOAM `fvModel` (next section).
6. **ML catchment (optional).** With `useMLmodel` on, a TensorFlow Lite model maps four inputs (scan speed, laser power, mass flow, standoff distance, judging by the variable names and ranges) to a catchment efficiency at startup; inputs outside the training range stop the run. [KNOWN: https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/createMLmodel.H#L27-L44 and createFieldsDEDFoam.H L57-L91; INFERRED: the physical meaning of "scan", "laser", "mass"] The README says it was "trained on high-fidelity, powder-resolved simulations". [KNOWN: README L2]
7. **Output and timing.** Fields are written per OpenFOAM's normal time folders; the solver wraps each phase in `StopWatch` timers. [KNOWN: DEDFoam.C L106-L127]

**AdditiveFOAM relationship (checked, binding evidence only).**
- DEDFoam *optionally uses* AdditiveFOAM: the README says DEDFoam "supports the flexible dynamic heat source model used by the AdditiveFOAM package", and `Allwmake` builds `src/fvModels` only when `USE_ADDITIVEFOAM=1`, pointing at an AdditiveFOAM source tree. [KNOWN: https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/README.md#L5 and #L31-L34; Allwmake L15-L19, L31-L33]
- The bridge class `additiveFoamHeatSource` "creates a movingHeatSource from the additiveFoam heat transfer library" and links AdditiveFOAM's `movingBeamModels` library and headers. [KNOWN: https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/src/fvModels/additiveFoamHeatSource/additiveFoamHeatSource.H#L34-L42; src/fvModels/Make/options L2, `-lmovingBeamModels`]
- DEDFoam is **not shown to be derived from** AdditiveFOAM. Checks: no byte-identical file between DEDFoam HEAD and any of 127 AdditiveFOAM commits (blob hash comparison); DEDFoam's solver header credits OpenFOAM Foundation and OpenCFD (the openfoam.com line) and names `compressibleInterFoam` as its base; AdditiveFOAM's tree has no mention of DEDFoam; DEDFoam's public git history is two commits, the first "Add files from internal repository for OS release." [KNOWN: local comparison 2026-11-11; DEDFoam.C L1-L10; git log] So: [UNRELATED] as a code ancestor, [KNOWN] as an optional dependency.
- Different OpenFOAM lineage: DEDFoam is tested with OpenFOAM v2312 and v2606 (the OpenCFD/openfoam.com release line), while AdditiveFOAM 2.0.0 targets OpenFOAM-14 from the OpenFOAM Foundation. [KNOWN: DEDFoam README L5; AdditiveFOAM brief] Whether the AdditiveFOAM bridge builds against current AdditiveFOAM 2.x on the OpenCFD line is [UNKNOWN]; it was not built (repo treated as untrusted, read only).

## How the project is organized
From templates/engineering-checklist.md, at commit d298a00.
- **Repo layout:** `applications/solvers/DEDFoam/` (main solver, 15 headers plus `DEDFoam.C`), `applications/solvers/rhoSimpleMLFoam/` (a TFLite demo solver based on `rhoSimpleFoam`), `applications/utilities/calcDiffs/` (field-difference utility) and `applications/utilities/tflite/readUfield/`, `src/fvModels/additiveFoamHeatSource/`, `tutorials/` (AMB2018-02, MarangoniVerification, singleTrackDED), `regression_tests/`, `tests/gpuTests/` and `tests/tfliteTest/`, `doc/`. 430 files. [KNOWN: tree]
- **Languages:** C++ (OpenFOAM `.C`/`.H`), Python test scripts, shell `Allrun` scripts. GitHub reports "Metal" as the largest language (about 49 MB); this is almost certainly OpenFOAM field files named `*.metal` (for example `T.metal`, `alpha.metal`) being misread as Apple's Metal shading language. [KNOWN: GitHub languages API, file names; INFERRED: the cause]
- **Build:** OpenFOAM `wmake` via `Allwmake`, with user toggles `USE_TFL`, `TFL_DIR`, `USE_ADDITIVEFOAM`, `ADDITIVEFOAM_LIB`. `Makefile` adds `clang-format`/`yapf` format targets. [KNOWN: https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/Allwmake#L9-L43, Makefile]
- **GPU path:** GPU runs go through petsc4Foam (PETSc as OpenFOAM's linear solver) with Kokkos matrix and vector types (`mat_type mpiaijkokkos`, `vec_type kokkos`). [KNOWN: README L2, L5; https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/tests/gpuTests/test_depthCharge3D/depthCharge3D/system/fvSolution_gpu#L28-L37] So only the linear-algebra solves move to GPU, not the whole solver. [INFERRED from the PETSc-only offload path]
- **Target machines:** build guides for OLCF Frontier (AMD MI250X, `craype-accel-amd-gfx90a`, ROCm, PETSc `--with-hip`), NERSC Perlmutter (NVIDIA A100), ALCF Aurora (Intel oneAPI), and ORNL CADES condos. [KNOWN: `doc/source/build-openfoam-frontier.md` L9 and L40-L42, `build-openfoam-perlmutter.md` L220, `build-openfoam-aurora.md` L5, `build-openfoam-cades-condos.md`] The TFLite tests "have only been tested on OLCF Frontier". [KNOWN: README L29]
- **Tests:** `regression_tests/` (pytest; singleTrackDED with and without ML, and AMB2018-02, compared to gold fields); `tests/gpuTests/` (OpenFOAM's damBreak and depthCharge3D cases run CPU vs GPU, compared to gold files); `tests/tfliteTest/` (ML as pre-processing and in the time loop). [KNOWN: `regression_tests/test_singleTrackDED/test_singleTrackDED.py` L11, L34; `tests/gpuTests/README.md` L1-L9]
- **CI:** none in the public repo (no `.github/workflows`). [KNOWN: tree]
- **Docs:** README, Sphinx source in `doc/source/` (not seen hosted). [KNOWN]
- **Releases:** one tag, v1.0 (2026-07-30), archived to Zenodo DOI 10.5281/zenodo.21708850. [KNOWN: git tags, Zenodo]
- **Contribution path:** README asks users to open an issue; no CONTRIBUTING file, no issue templates. [KNOWN: README L42-L43]
- **Data and reproducibility:** tutorial cases and gold fields are in the repo; the ML model file `model.tflite` ships under `regression_tests/test_singleTrackDED/ML/`. The training data for that model is not in the repo. [KNOWN: tree; UNKNOWN: where training data lives]
- **Deployment statements:** "validated on a variety of material systems" and "tested with OpenFOAM v2312 and v2606". No deployment claim. [KNOWN: README L2, L5]
- **Why it was built this way:** [UNKNOWN]. No public source explains the choice of the OpenCFD OpenFOAM line, PETSc for GPU, or TFLite.

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2026-07-28 | GitHub repo created | GitHub API `created_at` | [KNOWN] |
| 2026-07-30 | First public commit, "Add files from internal repository for OS release." | git log e6f3c5b | [KNOWN] |
| 2026-07-30 | v1.0 release; Zenodo DOI 10.5281/zenodo.21708850 | GitHub releases API; Zenodo 21708850 | [KNOWN] |
| 2026-07-30 | DOE CODE record code-186894 published | OSTI API | [KNOWN] |
| 2025-04-15 | Date written in the GPU test README (predates the public repo) | `tests/gpuTests/README.md` L2 | [KNOWN]; meaning [INFERRED: internal development before release] |

## Who uses it / why it matters
No outside users found: 5 stars, 2 forks, 0 GitHub dependents, no papers citing the software DOI. [KNOWN: GitHub API and dependents page, OpenAlex, 2026-11-11] It matters to this catalog because it fills the DED gap next to the powder-bed-oriented AdditiveFOAM and the conduction-only 3DThesis and Finch, and because it is ORNL's first public AM code we have seen with a GPU solver path and an embedded ML surrogate. [INFERRED]

## Related projects
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| AdditiveFOAM (`additivefoam`) | uses (optional heat-source library); not a code ancestor | DEDFoam README L5, L31-L34; `src/fvModels`; blob comparison | [KNOWN] uses; [UNRELATED] as ancestor |
| OpenFOAM (outside, OpenCFD line v2312/v2606) | built on; solver derived from `compressibleInterFoam` | README L5; DEDFoam.C L32-L36 | [KNOWN] |
| petsc4Foam / PETSc (outside) | uses for GPU solves | README L2, L5; fvSolution_gpu | [KNOWN] |
| Kokkos (outside, via PETSc) | uses indirectly (PETSc Kokkos back end) | fvSolution_gpu L34-L35 | [KNOWN] |
| TensorFlow Lite (outside) | uses (optional) | README L5, L21-L29 | [KNOWN] |
| Myna (`myna`) | unknown; Myna's repo does not mention DEDFoam | grep of ORNL-MDF/Myna clone, 2026-11-11 | [UNKNOWN] |
| 3DThesis, Finch | related topic (AM thermal models) | catalog | [INFERRED] |
| Frontier (OLCF) | same facility target (build guide) | `doc/source/build-openfoam-frontier.md` | [KNOWN] |

## What stands out
- The DOE CODE record lists ten authors, nine at ORNL and one at Argonne; one AdditiveFOAM developer appears on both author lists. Shared authorship proves a shared contributor, not a shared team (rule 19). [KNOWN: OSTI code-186894; AdditiveFOAM README]
- The repo landed as a two-commit "OS release" dump from an internal repository, so public history says nothing about how long it was developed. The GPU test README's 2025 date hints at at least a year of internal work. [KNOWN: git log, README date; INFERRED: duration]
- The ML piece is small and specific: a fixed normalization table baked into C++ plus a `.tflite` file, called once at startup to set one scalar. That is a cheap way to put a learned surrogate inside a legacy solver without a Python runtime. [KNOWN: createMLmodel.H; INFERRED: the design reading]
- Sponsor is EERE's Advanced Materials & Manufacturing Technologies Office, the same office on several AdditiveFOAM-adjacent OSTI records. [KNOWN: OSTI code-186894, 3002891]

### Reusable ideas [INFERRED]
- Optional coupling through a plugin (`fvModel`) and a build flag lets a solver reuse a sibling project's physics without forking it. The same pattern works for any framework with runtime-selectable source terms.
- Range-checking ML inputs and stopping hard when outside the training envelope is a simple guard worth copying for any embedded surrogate.
- Offloading only the linear solver to GPU through PETSc is a low-effort first GPU port for a large CPU code; the CPU-vs-GPU gold-file tests show how to check it.
- Gold-file regression tests driven by pytest around `Allrun` scripts are a cheap test harness for case-based simulation codes.

## Ten questions (GOAL.md)
1. **What problem does it solve, and for whom?** High-fidelity single-track simulation of blown-powder DED, for AM researchers studying melt pools and powder catchment. [KNOWN: README L2]
2. **Where does it sit in the tree?** ORNL, materials / additive manufacturing; sponsor EERE AMMTO. Org unit not stated. [KNOWN: OSTI code-186894; UNKNOWN: org unit]
3. **Who pays for it?** EERE AMMTO per DOE CODE. [KNOWN: OSTI code-186894]
4. **How is the code organized?** OpenFOAM solver plus utilities, optional TFLite and AdditiveFOAM modules, `wmake` build, pytest regression tests, per-machine build guides. [KNOWN: tree]
5. **Is it alive?** Too young to say: two commits on one day and one release, nothing since 2026-07-30. [KNOWN: git log]
6. **Who outside ORNL uses or cites it?** None found; one Argonne co-author on the DOE CODE record. [KNOWN: OpenAlex, GitHub dependents, OSTI]
7. **What does it connect to?** OpenFOAM, PETSc/petsc4Foam, Kokkos (through PETSc), TensorFlow Lite, optionally AdditiveFOAM. [KNOWN: README]
8. **What does it teach about how ORNL works?** Code developed on an internal repository and released as a snapshot with a DOE CODE record and Zenodo DOI the same day. [KNOWN: git log, OSTI, Zenodo; INFERRED: the pattern]
9. **Could a student learn from it?** Yes, if they already know OpenFOAM: the solver is about 2,300 lines of readable headers and the tutorials are small. GPU and ML paths need PETSc or TensorFlow Lite builds. [KNOWN: line counts; INFERRED: difficulty]
10. **What is still unknown?** Validation evidence, papers, outside users, ML training data, whether the AdditiveFOAM bridge builds against AdditiveFOAM 2.x. Searches logged in verification/not-found.md.

## Known / Inferred / Unknown
- KNOWN: ownership (ORNL org, LICENSE, DOE CODE), license, sponsor, dates, solver base, physics modules, optional dependencies, machine build guides, tests, release.
- INFERRED: physical meaning of ML inputs, GPU offload scope, "Metal" language misclassification, internal development before release, reusable ideas.
- UNKNOWN: org unit, validation data, users, ML training data, why the OpenCFD line was chosen, bridge compatibility with AdditiveFOAM 2.x.

## Verification notes
Sweep 1 (discovery and reading pass, 2026-11-11): fresh `--filter=blob:none` clone at d298a00; read README, LICENSE, Allwmake, solver headers, tests, docs; OSTI API record fetched; Zenodo record fetched; blob comparison against AdditiveFOAM history. Code was read, not built or run. Sweep 2 not done.

Sweep 2 (fact-check pass, 2026-11-11, by the coordinator, independent of the discovery researcher): Re-fetched at d298a00 from raw GitHub: LICENSE L1-L8 (GPL-3.0-or-later; OpenFOAM Foundation plus ORNL copyright); README L1-L5 and L28-L40; `DEDFoam.C` L32-L36 (based on compressibleInterFoam); `createMLmodel.H` L26-L72 (training ranges and fatal out-of-range checks); the `src/fvModels/additiveFoamHeatSource/` plugin files exist. OSTI API code-186894: ORNL research org, EERE AMMTO sponsor. All match. Not re-checked: individual physics-file line ranges, the blob comparison against AdditiveFOAM, the Zenodo record. No corrections.

## Sources (URL, title, accessed date, what it supports)
All accessed 2026-11-11.
- https://github.com/ORNL/DEDFOAM and https://api.github.com/repos/ORNL/DEDFOAM (repo metadata, created/pushed dates, license NOASSERTION, stars/forks)
- https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/README.md (description, dependencies, AdditiveFOAM option, license)
- https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/LICENSE#L1-L8 (copyright lines)
- https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/DEDFoam.C#L32-L36 (based on compressibleInterFoam) and #L160-L206 (time loop)
- https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/powderInteraction.H#L57-L101 (powder capture rules)
- https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/alphaSuSp.H#L1-L26 (assumed powder distribution)
- https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/qDot.H#L66-L85 (laser and loss terms)
- https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/createMLmodel.H#L27-L44 (ML normalization ranges)
- https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/src/fvModels/additiveFoamHeatSource/additiveFoamHeatSource.H#L34-L42 (AdditiveFOAM bridge)
- https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/tests/gpuTests/test_depthCharge3D/depthCharge3D/system/fvSolution_gpu#L28-L37 (PETSc Kokkos solver settings)
- https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/doc/source/build-openfoam-frontier.md (Frontier build)
- https://www.osti.gov/doecode/biblio/186894 and https://www.osti.gov/api/v1/records/code-186894 (DOE CODE: ORNL research org, AMMTO sponsor, authors, contract)
- https://zenodo.org/records/21708850 (release 1.0 DOI, gpl-3.0-or-later)
- https://api.openalex.org/works/doi:10.5281/zenodo.21708850 (0 citations)
- https://github.com/ORNL/AdditiveFOAM (comparison clone at 8314d3c plus all branches)

## Quality gate
- [x] Every load-bearing claim has a source and a tag
- [x] Facts are kept apart from interpretation
- [x] ORNL relationship is not overstated, and maturity verbs match the source (RULES item 10)
- [x] Walkthrough, flow, timeline and unknowns are present
- [x] Ten questions answered or marked UNKNOWN
- [x] No copied text beyond short cited quotes; people by role only
- [x] Two fact-check sweeps done (RULES item 11): Sweep 1 and Sweep 2 both 2026-11-11
- [x] INDEX, catalog, LAB-TREE and connections map updated (batch 13) (coordinator)
