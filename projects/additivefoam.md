# AdditiveFOAM
- Official docs: https://ornl.github.io/AdditiveFOAM/ (GitHub Pages, built with the Just the Docs theme). It has a user guide, governing equations, heat-source models, adaptive mesh refinement, tutorials, and an archive of the 1.0.0 docs. [KNOWN: docs site, README]
- Repo: https://github.com/ORNL/AdditiveFOAM (default branch `main`). GitHub's description is "A continuum physics code for additive manufacturing built on OpenFOAM". [KNOWN: GitHub API]
- License: GPL version 3 or (at your option) any later version. The LICENSE file carries "Copyright (C) 2011-2017 OpenFOAM Foundation" and "Copyright (C) 2023-2026 Oak Ridge National Laboratory". The GitHub API says NOASSERTION. [KNOWN: LICENSE header, README License section, GitHub API]
- Status: active (rule 14). Release 2.0.0 came out 2026-08-31, and the last commit was 2026-09-21 11:34 ET. Not archived. [KNOWN: GitHub API, git log]
- Scope (rule 13): CORROBORATED, by three things:
  - The README calls it software "released by Oak Ridge National Laboratory".
  - ORNL is named as a copyright holder.
  - DOE CODE code-108345 (version 1.0.0, released 2023-06-13) lists "Research Org.: Oak Ridge National Laboratory (ORNL), Oak Ridge, TN" with sponsors DOE Office of Science and NNSA. [KNOWN: README, LICENSE, https://www.osti.gov/doecode/biblio/108345]
- Org unit: not stated. The README's wordmark image is hosted in an `ORNL-MDF/additivefoam-website-assets` repo, which ties it to the same GitHub org as Finch and 3DThesis. [KNOWN: README image URL; INFERRED: the manufacturing-group tie]

## Plain-language walkthrough
- **What it is:** a simulation code for metal 3D printing that models heat and the flow of molten metal in the tiny melt pool under a laser or electron beam. It's built as an add-on to OpenFOAM. [KNOWN: README, docs]
- **Key terms:**
  - *CFD* (computational fluid dynamics) means simulating liquids and gases by solving flow equations on a mesh.
  - *OpenFOAM* is a big free CFD toolkit from the OpenFOAM Foundation.
  - *Marangoni flow* is liquid pushed around by differences in surface tension between hot and cold spots. It strongly shapes a melt pool.
  - The *mushy zone* is the half-solid, half-liquid region.
  - *Adaptive mesh refinement* (AMR) means using small mesh cells only near the beam, where detail matters, to save compute. [KNOWN: the docs' capability list; INFERRED: the explanations]
- **The problem:** the conduction-only models (3DThesis, Finch) are fast but ignore fluid motion, which changes melt-pool shape and so the final grain structure. AdditiveFOAM includes that physics. DOE CODE's abstract stresses "process-structure relationships". [KNOWN: DOE CODE abstract; INFERRED: the comparison]
- **What goes in:** an OpenFOAM "case" folder, which holds the mesh, material files (bundled examples are AlSi10Mg, IN625 and SS316L), heat-source settings (beam profile, absorption, projection, refinement) and a scan path. A `createScanPath` utility helps make the path. [KNOWN: `etc/materials/`, `etc/heatSources/`, `applications/utilities/`, CHANGELOG 2.0.0]
- **What happens:** the `additiveFoam` solver steps time forward. Each step it:
  1. Moves the beam or beams.
  2. Adds their heat.
  3. Solves for temperature, phase change and flow.
  4. Refines the mesh around the hot region.
  5. Records melt-pool measurements. [KNOWN: `applications/solvers/additiveFoam/` file names, docs; INFERRED: the order]
- **What comes out:** temperature and flow fields, melt-pool size, solidification conditions, and thermal histories formatted for ExaCA (a grain-growth code). Helper scripts in `bin/` (for example `reconstructExaCAData`, `runLayers`, `plotCET`) post-process them. [KNOWN: docs, `bin/`]
- **Where humans act:** a researcher sets up the case and picks materials. They can also calibrate the heat-source model against experiments with the `calibrateHeatSource` tool, which uses a Bayesian workflow per CHANGELOG 2.0.0. [KNOWN: README, CHANGELOG]
- **What it is not:** it isn't a full-part distortion or stress model, and it isn't standalone: OpenFOAM-14 has to be installed first. [KNOWN: README install; INFERRED: the scope limit]
- **What's unknown:** how widely it's used outside ORNL. That's for signals.
- **Example:** the `AMB2018-02-B` tutorial is set up around a public AM benchmark case. `multiLayerPBF` runs several powder-bed layers. [KNOWN: tutorial folder names, docs; INFERRED: that AMB2018 is the NIST AM-Bench 2018 series]

## How it works
- The solver code (`applications/solvers/additiveFoam/`) is split into `movingHeatSource/` (beam path and profiles), `thermo/` (phase change), `pU/` (the pressure and velocity flow solve), `functionObjects/` (runtime measurements), `derivedFvPatchFields/` (boundary conditions) and `setDeltaT.H` (time-step control). [KNOWN: tree]
- Release 2.0.0 was a big rework:
  - It ported the code to OpenFOAM-14.
  - It added a general "projected" heat source with super-Gaussian, nLight AFX (a commercial adjustable laser) and measured tabulated beam profiles.
  - It added conversion of PRIMES beam-profiler measurements, and dynamic refinement.
  - It changed the input dictionary layout, so old cases need updating. [KNOWN: CHANGELOG 2.0.0]

## How the project is organized
- Top level: `applications/` (solver and utilities), `src/AdditiveFOAM/`, `etc/` (bashrc, materials, heat sources), `bin/` (Python and shell helpers), `tutorials/`, `test/marangoni`, `Allwmake` (the OpenFOAM-style build script), `requirements.txt`, `CHANGELOG.md` and `CITATION.bib`. [KNOWN: tree]
- Languages: C++ about 41.6% by bytes, C 36.3%, Python 17.6%, Shell 4.4%. GitHub counts OpenFOAM's `.H` headers as C, which likely explains the high C share. [KNOWN: GitHub languages API; INFERRED: the explanation]
- Build: OpenFOAM-14 from the OpenFOAM Foundation, then `./Allwmake`. The Python utilities need Python 3.10 to 3.12. [KNOWN: README]
- CI: one GitHub Actions workflow that installs OpenFOAM-14 and builds. [KNOWN: `.github/workflows/CI.yml`]
- Releases: 1.0.0 (2023-06-13), 1.1.0 (2025-05-14), 1.2.0 (2026-06-29) and 2.0.0 (2026-08-31). [KNOWN: GitHub API]
- History: 68 commits since 2023-03-28. By year there are 33 in 2023, 11 in 2024, 17 in 2025 and 7 in 2026. 78 stars and 22 forks. [KNOWN: git log, GitHub API]
- Contributors: 6 including anonymous commit authors, 5 GitHub accounts. The README credits a list of ORNL staff, which isn't reproduced here. [KNOWN: GitHub API, README]
- Citation: a JOSS (Journal of Open Source Software) paper, DOI 10.21105/joss.07770, plus Zenodo DOIs. [KNOWN: README]

## Who uses it / why it matters
It's the high-fidelity tier of the AM thermal tools in our catalog. It's slower than 3DThesis or Finch, but it captures melt-pool flow, and it feeds ExaCA for grain prediction. [INFERRED] Myna wraps it as an application. [KNOWN per myna brief] Usage evidence goes in `signals/additivefoam.md` once it exists.

## Related projects
- OpenFOAM (outside project): the base framework. [KNOWN: README, map link 16]
- ExaCA (outside project): consumes its thermal histories. [KNOWN: docs, DOE CODE abstract]
- Myna (`myna`): wraps it. [KNOWN per myna brief]
- 3DThesis and Finch: faster conduction-only siblings. [INFERRED: the tiering]
- HydraGNN: the map records a shared contributor. [KNOWN per map link 5]

## Known / Inferred / Unknown
- KNOWN: license and copyright lines, DOE CODE record, releases, dates, capabilities, layout, build, the 2.0.0 changes, counts, citation.
- INFERRED: the physics explanations, the tiering, the language-share explanation, the AMB2018 meaning, the MDF tie.
- UNKNOWN: org unit, users outside the team.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL/AdditiveFOAM (README.md, LICENSE, CHANGELOG.md, applications/, etc/, bin/, tutorials/, .github/workflows/CI.yml)
- https://api.github.com/repos/ORNL/AdditiveFOAM (plus /languages, /releases, /tags, /contributors with and without anon=1)
- https://ornl.github.io/AdditiveFOAM/ (home page capability list)
- https://www.osti.gov/doecode/biblio/108345 ("Research Org.: Oak Ridge National Laboratory (ORNL), Oak Ridge, TN (United States)")
- https://doi.org/10.21105/joss.07770 (JOSS paper, linked, not read)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified on a fresh clone of ORNL/AdditiveFOAM and public records: LICENSE copyright lines (OpenFOAM Foundation 2011-2017, ORNL 2023-2026) under GPL v3, README "released by Oak Ridge National Laboratory", OpenFOAM-14 and Python 3.10-3.12 requirements, wordmark hosted in ORNL-MDF, one CI workflow, tags 1.0.0 to 2.0.0, last commit 2026-09-21 11:34 ET, 68 commits (33/11/17/7 for 2023-2026), first 2023-03-28, contributors 6 with anonymous and 5 accounts. DOE CODE code-108345 refetched from the OSTI API: 2023-06-13, ORNL research org, sponsors DOE Office of Science and NNSA. Docs site resolves.
- No corrections.
