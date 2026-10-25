# KORC (Kinetic Orbit Runaway electrons Code)
- Official docs: http://ornl-fusion.github.io/KORC (generated from the repo's `docs/` folder with FORD, a Fortran documentation tool). [KNOWN: README, GitHub homepage field, `FORD_PF.md`]
- Repo: https://github.com/ORNL-Fusion/KORC (default branch `main`). GitHub's description is "Kinetic Orbit Runaway Code (KORC)". [KNOWN: GitHub API]
- License: MIT, "Copyright (c) 2021, Oak Ridge National Laboratory". The GitHub API also says MIT. [KNOWN: LICENSE line 1, GitHub API]
- Status: active (rule 14). The last commit was 2026-09-11 10:12 ET and the last push was 2026-10-22 00:33 UTC (8:33 PM ET on 2026-10-21). Not archived. [KNOWN: git log, GitHub API]
- Scope (rule 13): CORROBORATED. Oak Ridge National Laboratory is the copyright holder. [KNOWN: LICENSE] OSTI journal records on runaway electrons list ORNL as a research org (for example 2586907, 2025), but I didn't check whether they name KORC, so they aren't used as scope evidence. [KNOWN: OSTI search results; UNKNOWN: whether they name KORC]
- Org unit: ORNL-Fusion GitHub org. [INFERRED: a fusion energy group; no division named]

## Plain-language walkthrough
- **What it is:** a simulation code, mostly in Fortran, that follows very fast electrons through the electric and magnetic fields inside a fusion reactor, one particle at a time. [KNOWN: README]
- **Key terms:**
  - A *tokamak* is a doughnut-shaped fusion device that holds hot plasma with magnetic fields.
  - A *disruption* is a sudden loss of that plasma.
  - *Runaway electrons* are electrons that a disruption's electric field speeds up to nearly light speed. A beam of them can melt holes in the reactor wall.
  - *Relativistic* means fast enough that Einstein's corrections matter.
  - The *Lorentz force* is the push a charged particle feels from electric and magnetic fields.
  - *Kinetic orbit* means tracking each particle's actual path, not an average fluid. [KNOWN: README names the Lorentz force, collisions and radiation losses; INFERRED: the explanations]
- **The problem:** large future tokamaks like ITER need to predict and prevent runaway-electron damage. KORC follows sample electrons under the full physics (fields, collisions with the plasma, and energy lost to radiation) to see where they go and what they hit. [KNOWN: README; INFERRED: the motivation]
- **What goes in:** an input file describing the starting electrons (energy, angle and spatial spread), the plasma profiles, and the magnetic and electric fields. The fields can be simple analytic models or field data read from other codes. [KNOWN: `src/korc_input.f90`, `korc_spatial_distribution.f90`, `korc_velocity_distribution.f90`, `korc_profiles.f90`, `korc_fields.f90`, `FIO/` with `fusion_io` and `m3dc1_lib`; INFERRED: the grouping]
- **What happens:**
  1. A "particle pusher" (`korc_ppusher.f90`) steps each electron through time.
  2. Collision and diffusion models (`korc_collisions.f90`, `korc_diffusion.f90`) and an avalanche model (`korc_avalanche.f90`) add the effects of the background plasma. In an avalanche, runaways knock loose more runaways.
  3. The work is spread across processors with MPI and OpenMP, with optional OpenACC for GPUs. [KNOWN: file names, the CMake `USE_ACC` option, `build_scripts/build_nvhpc_gpu.sh`; INFERRED: the order]
- **What comes out:** HDF5 files (a common scientific data format) with particle positions, energies and other diagnostics, analyzed with the bundled MATLAB and Python scripts. [KNOWN: `korc_HDF5.f90`, `Matlab_Analysis/`, `Python_analysis/`]
- **Where humans act:** a fusion physicist picks the scenario and the field source, builds with the right compiler (GNU or NVIDIA HPC), and interprets the output. [KNOWN: build scripts; INFERRED]
- **What it is not:** it doesn't simulate the whole plasma. It follows test electrons in fields that other codes provide (the FIO path reads M3D-C1 output). [KNOWN: FIO folder; INFERRED: the test-particle framing]
- **What's unknown:** which machines it's routinely run on beyond what the build scripts show, and who uses it outside the group.
- **Example:** `Publication_Data/` keeps inputs tied to published papers, such as a 2020 and a 2024 set named after the journals, so results can be reproduced. [KNOWN: folder names; INFERRED: the reproducibility purpose]

## How it works
- About 28 Fortran and C++ files in `src/`. Each `korc_*.f90` module does one job: constants, types, units, coordinates, fields, interpolation (PSPLINE or FIO), profiles, random numbers, particle pusher, collisions, diffusion, avalanche, HDF5 output, and HPC setup. [KNOWN: tree]
- Build options: `USE_ACC` (OpenACC, off by default), `USE_PSPLINE` (on), `USE_FIO` (off), HDF5 precision (FLOAT or DOUBLE), a set of sanitizer options for catching memory and math bugs, and `KORC_BUILD_TESTS`. [KNOWN: CMakeLists.txt lines 40-96]
- Recent work: the latest commits (September 2026) add OpenACC versions of the diffusion routines and fix a coordinate-conversion bug. [KNOWN: commit messages]

## How the project is organized
- Top level: `src/`, `FIO/` (fusion-io interface), `test/`, `docs/` (generated site), `User_Documentation/`, `Matlab_Analysis/`, `Python_analysis/`, `Publication_Data/`, `build_scripts/`, `spackenv/` and `spackpack/`, `setup_cmake`, and `build.sh`. [KNOWN: tree]
- Languages: Fortran about 70.8% by bytes, MATLAB 11.4%, C++ 9.1%, Python 6.6%, then small amounts of Shell, CMake and C. [KNOWN: GitHub languages API]
- Build: the README's quick start uses Spack (a package manager for supercomputers) to get gcc 13.1, CMake, and HDF5 with Fortran and MPI. Other scripts cover NVIDIA HPC compilers, including a GPU build. [KNOWN: README, `build_scripts/`]
- CI: three GitHub Actions workflows (`agate.yml`, `cachepoke.yml`, `onyx.yml`). The README badge points to a `spack.yml` that isn't in the folder anymore. The `spackenv/` folders are named for specific test machines. I didn't look further, since that's build-target territory and rule 16 bars mapping infrastructure. [KNOWN: file list, README badge]
- Releases: two GitHub releases, "NF_2020" (2020-04-23) and "Pre_DevOps_Merge" (2022-03-04), and five tags in total (also v0.0.1, archive and hocus). No numbered release series. [KNOWN: GitHub API, git tags]
- History: 975 commits. The repo was created 2016-03-14, but the first commit in history is 2019-07-22. By year there are 66 in 2019, 126 in 2020, 76 in 2021, 167 in 2022, 133 in 2023, 311 in 2024, 31 in 2025 and 65 in 2026. 9 stars and 2 forks. [KNOWN: git log, GitHub API; INFERRED: that older history wasn't carried over]
- Contributors: 8 including anonymous commit authors, 5 GitHub accounts. [KNOWN: GitHub API]

## Who uses it / why it matters
Runaway electrons are one of the main risks for large tokamaks, so codes that predict where they go feed straight into reactor safety design. [INFERRED] The repo is small and steady, with commits every year since 2019 and a 2024 spike, which looks like an in-house research code more than a community package. [KNOWN: commit counts; INFERRED: the reading] Usage evidence goes in `signals/korc.md` once it exists.

## Related projects
- GITR (`gitr`): another ORNL-Fusion particle-tracking code (impurities rather than electrons). [KNOWN: same org; INFERRED: the domain similarity]
- FAR3d (`far3d`, catalog row): another fusion code in the catalog. No code tie found. [UNKNOWN]
- M3D-C1 and fusion-io (outside projects): field sources through the FIO interface. [KNOWN: `FIO/`]

## Known / Inferred / Unknown
- KNOWN: license and copyright, dates, file layout, build options, build scripts, releases and tags, counts, docs site.
- INFERRED: the physics explanations, the org unit, the in-house reading, the missing pre-2019 history.
- UNKNOWN: whether ORNL's runaway-electron papers name KORC, outside users, the next release plans.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL-Fusion/KORC (README.md, LICENSE, CMakeLists.txt, src/, FIO/, build_scripts/, User_Documentation/, .github/workflows/)
- https://api.github.com/repos/ORNL-Fusion/KORC (plus /languages, /releases, /contributors with and without anon=1)
- http://ornl-fusion.github.io/KORC (linked docs site, not read in depth)
- https://www.osti.gov/api/v1/records?q=KORC%20runaway (search only; records not tied to KORC)
