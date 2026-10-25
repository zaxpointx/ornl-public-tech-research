# GITR (Global Impurity Transport code)
- Official page / Repo: https://github.com/ORNL-Fusion/GITR (legacy archive: https://github.com/ORNL-Fusion/GITR_legacy)
- Docs: README only. There's no separate docs site. [KNOWN: repo homepage field is empty]
- License: GPL-2.0 [KNOWN: https://github.com/ORNL-Fusion/GITR/blob/main/LICENSE]
- Status: active but slow-moving [KNOWN: last push 2025-11-21, last release v1.3.0 on 2022-12-06, GitHub API]


## Plain-language walkthrough
- **What it is:** Global Impurity TRansport, a simulation code for fusion devices. [KNOWN: repo README]
- **The problem:** the hot plasma in a fusion machine wears away the wall material (erosion), and those loose atoms ("impurities") travel around, cool the plasma and land elsewhere.
- **What goes in:** a plasma background (density, temperature, fields), a wall geometry and a config file. [KNOWN: libconfig dependency and example input folders; INFERRED: the exact input roles]
- **What happens:** it tracks huge numbers of impurity particles through the plasma with a Boris pusher (a standard way to step charged particles through electric and magnetic fields), including sputtering and redeposition. It runs on GPUs with CUDA by default. [KNOWN: `src/`, CMake defaults]
- **What comes out:** where impurities go and where material is eroded or deposited. [KNOWN: README purpose]
- **Where humans act:** physicists prepare the plasma backgrounds and interpret the output.
- **What it is not:** it doesn't simulate the plasma itself. It assumes impurities are a "trace" amount that doesn't change the plasma. [KNOWN: README trace-impurity assumption]
- **What's unknown:** current main users, and the ORNL group.
- **Example:** the `d3d_sas_1d` example models a setup on the DIII-D tokamak. [KNOWN: repo examples; INFERRED: that "d3d" means DIII-D]

## What it is
In a fusion reactor, the hot plasma (electrically charged gas) hits the inner walls and knocks atoms off them. That's called erosion or sputtering. The knocked-off atoms are "impurities": they drift through the plasma, can cool it down, and eventually land somewhere else (redeposition). GITR simulates this whole loop of erosion, impurity transport, sputtering and redeposition. [KNOWN: README, https://github.com/ORNL-Fusion/GITR] Engineers need this to predict how long wall materials like tungsten will last and how much they'll contaminate the plasma. [INFERRED]

## How it works
- **Inputs:** a background plasma profile, the magnetic "equilibrium" (the shape of the field that holds the plasma), the device geometry, and a surface model describing how the wall material responds when hit. [KNOWN: README]
- **Trace-impurity assumption:** GITR assumes there are so few impurities that they don't change the background plasma. That lets it move each particle through fixed fields, which is far cheaper than simulating everything together. [KNOWN: README; INFERRED: the cost reasoning]
- **Particle loop:** starting from initial conditions, each particle is stepped through a series of "operators" (push, ionize, collide, diffuse and so on) until it hits a wall or times out. [KNOWN: README] The source files match that list: `boris.cpp` (the Boris pusher, a standard method for moving a charged particle in electric and magnetic fields), `ionize.cpp`, `coulomb_data_broker.cpp` (Coulomb collisions), `cross_field_diffusion_broker.cpp`, `surface_model.cpp` and `spectroscopy.cpp`. [KNOWN: repo `src/`; INFERRED: what each file does, based on its name]
- **Hardware:** it's C++ that you compile for your machine, with CPU or GPU parallelism. [KNOWN: README] The default compile options turn CUDA (NVIDIA GPU programming) on and OpenMP and MPI off. [KNOWN: `CMake/compile_time_options.cmake`]

## How the project is organized
- Top level: `src/` (25 files), `include/`, `CMake/`, `dependencies/` (build scripts for HDF5, NetCDF, libconfig, zlib and m4), `containers/` (CPU and GPU Dockerfiles plus Podman scripts), `examples/` (9 cases, including `d3d_sas_1d` and `walldyn`), `test_src/`, `test_data/`, and `images/`. [KNOWN: repo tree]
- Languages: C++ 95.6%, CMake 3.6%, with small amounts of CUDA and C. [KNOWN: GitHub languages API]
- Build: CMake. The README strongly recommends installing with containers over a "bare-metal" build. [KNOWN: README]
- Releases: 1.0 (2019-02-25), pisces_example1.0 (2019-10-07), 1.1 (2020-04-21), v1.2.0 (2021-08-26), v1.3.0 (2022-12-06). [KNOWN: GitHub releases API]
- Contributors: about 36, counting anonymous ones. [KNOWN: GitHub contributors API, last page = 36]
- Org: the ORNL-Fusion GitHub organization. The ORNL division isn't named in the repo. [INFERRED: ORNL's fusion program; UNKNOWN: exact division]

## Who uses it / why it matters
The `d3d_sas_1d` example points to DIII-D, General Atomics' tokamak in San Diego. [INFERRED: from the example name] ORNL and General Atomics publish DIII-D impurity-transport studies, for example carbon from helicon antenna surfaces (2026). That paper's workflow couples SOLPS, COMSOL, RustBCA, GITR and GITRm. [KNOWN: OSTI 3452355, DOI 10.1088/1741-4326/ae9322] Wall erosion is one of the main lifetime limits for future reactors like ITER. [INFERRED]

## Related projects
- Fusion and RF-sheath erosion work at ORNL, such as the STRIPE framework, which also couples plasma backgrounds to erosion. STRIPE uses GITR for impurity transport. [KNOWN: OSTI 3013481 description]
- Thermochimica (`thermochimica`) and other materials codes model what walls are made of, while GITR models how they wear. [INFERRED]

## Known / Inferred / Unknown
- KNOWN: purpose, inputs, trace-impurity assumption, layout, languages, GPL-2.0, releases, CUDA default.
- INFERRED: what each operator file does, the DIII-D use from the example name, the org unit.
- UNKNOWN: active maintainers, ORNL division, DOE CODE record.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL-Fusion/GITR (README, LICENSE, src/, CMake/)
- https://api.github.com/repos/ORNL-Fusion/GITR (plus /languages, /releases, /contributors)
- https://www.osti.gov/biblio/3452355
- https://www.osti.gov/biblio/3013481

## Fact-check notes (2026-10-24)
- Corrected: releases list was missing 1.0 (2019-02-25); five releases in all.
- Corrected: OSTI 3452355 (GA + ORNL, DIII-D helicon carbon) and OSTI 3013481 (ORNL, WEST tungsten erosion via STRIPE) both name GITR in their descriptions, so both links are now KNOWN.
- Verified: GPL-2.0; README inputs, trace-impurity assumption, operator loop, container-recommended install; CUDA=1, OpenMP=0, MPI=0 defaults; 25 src files; 9 examples; C++ 95.6 / CMake 3.6; 36 contributor pages; last push 2025-11-21.
- No DOE CODE software record found for GITR; ORNL division stays [UNKNOWN].

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Re-fetched the GitHub API (GPL-2.0, last push 2025-11-21, 5 releases, 36 contributor pages), README, and OSTI 3452355 and 3013481. No contradictions.
- Load-bearing quotes: README "Description": "performs large scale simulation of plasma induced erosion, plasma transport of those impurities, sputtering, and redeposition"; trace assumption: "The density of impurities created in the GITR code is negligible in its effect on the background plasma parameters." OSTI 3013481 (ORNL, 2026): STRIPE integrates "GITR for impurity transport". OSTI 3452355 (GA + ORNL, 2026-08-12): workflow "couples SOLPS, COMSOL, RustBCA, GITR, and GITRm".
- Not CORROBORATED: both OSTI papers come from the same STRIPE group, so they are not independent sources (agrees with map link 92).
- Walkthrough present. No maturity upgrades.
