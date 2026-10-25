# Cabana
- Official page: no separate website. The repo wiki is the documentation home: https://github.com/ECP-copa/Cabana/wiki [KNOWN: README "Documentation"]
- Repo: https://github.com/ECP-copa/Cabana (default branch `master`, owned by the ECP-copa org, not ORNL) [KNOWN: GitHub API]
- License: BSD 3-Clause, "Copyright 2018-2023 the Cabana authors". GitHub's API reports NOASSERTION. [KNOWN: LICENSE lines 1-3, GitHub API]
- Status: active. The latest release is 0.8.0 (2026-05-29 UTC), the last commit was 2026-09-16, and the in-progress version is `0.8.99-dev`. There have been 9 GitHub releases since the first. [KNOWN: GitHub API releases, git log, CMakeLists.txt line 18]
- Scope (rule 13): passes because ORNL is a named contributing lab and a research org.
  - The README says it's developed in the ECP Co-Design Center for Particle Applications (CoPA): "a multi-institutional project with developers from ORNL, LANL, SNL, LLNL, PPNL, and ANL". [KNOWN: README]
  - DOE CODE code-45702 lists ORNL as research org. [KNOWN: Scout's catalog row, OSTI API]
  - ORNL doesn't own the repo or hold the copyright alone, so the brief describes it as multi-lab. [rule 10/13]

## Plain-language walkthrough
- **What it is:** a C++ toolkit for writing *particle simulations*, programs that model a system as huge numbers of moving points (atoms, plasma particles, chunks of material, galaxies). The same code runs fast on ordinary CPUs and on GPUs. [KNOWN: README]
- **The problem:** supercomputers now mix CPU and GPU vendors (NVIDIA, AMD, Intel). Hand-writing particle code for each one is slow and error-prone. Cabana provides the shared plumbing once: data layouts, neighbor finding, sorting, and passing particles between machines. [KNOWN: README; INFERRED: the framing]
- **Key terms:**
  - *Performance portable* means one source code that runs well on different hardware. Cabana gets this from Kokkos, an outside library (not an ORNL catalog project, rule 13) that maps loops onto whatever hardware is present. [KNOWN: README "built on Kokkos", `find_package(Kokkos 4.1 REQUIRED)`]
  - *MPI* is the standard way separate computers in a cluster pass messages. [INFERRED: general definition]
- **What goes in:** a scientist's own simulation code, which defines what each particle stores (position, velocity, charge and so on) and the physics rules. Cabana is a library, not a finished simulator. [INFERRED from the layout: headers plus tutorials, no standalone app]
- **What happens:**
  1. Particles are stored in Cabana's layouts.
  2. Cabana builds neighbor lists, meaning which particles are close enough to interact.
  3. Your physics runs in parallel loops.
  4. When particles cross into another node's region, Cabana migrates them and exchanges "halo" copies, the boundary particles each neighbor needs to see.
  5. Optionally, particle values are spread onto a grid and back (particle-grid interpolation). [KNOWN: README; `core/src` file names; INFERRED: the order]
- **What comes out:** updated particle data each step, plus optional output files in HDF5 or Silo, two common scientific data formats. [KNOWN: `Cabana_HDF5ParticleOutput.hpp`, `Cabana_SiloParticleOutput.hpp`]
- **Where humans act:** a developer writes the physics, chooses the hardware backend and dependencies at build time, and decides the run's size. [INFERRED]
- **What it is not:** it isn't a ready-to-run simulation program, a visualizer, or a Kokkos replacement. [INFERRED]
- **What's unknown:** which ORNL projects rely on it besides the ones in our catalog, and how the ECP's end affected funding (Scout's signals file covers funding).
- **Example:** the README lists molecular dynamics, particle-in-cell plasma physics, N-body cosmology and peridynamics (fracture modeling). [KNOWN: README] In our catalog, Finch, ORNL's additive-manufacturing heat solver, is built on Cabana. [KNOWN: Finch catalog row, repo description]

## How it works
- **Data layout ("AoSoA"):** Cabana's core container is an *array of structs of arrays*. Particles are grouped into small fixed-size chunks, and within each chunk every property sits in its own short array. That keeps memory access fast on both CPUs (vector instructions) and GPUs. [KNOWN: `Cabana_AoSoA.hpp`, `Cabana_SoA.hpp`, tutorials `03_struct_of_arrays` and `04_aosoa`; INFERRED: the performance reason]
- **A "slice"** is a view of one property across all particles, so a loop can touch just positions, for example. [KNOWN: `Cabana_Slice.hpp`, tutorial `05_slice`; INFERRED: the definition]
- **Neighbors:** linked-cell lists and Verlet lists (two classic ways to find nearby particles), plus an optional ArborX path. ArborX is an outside spatial-search library. [KNOWN: `Cabana_LinkedCellList.hpp`, `Cabana_VerletList.hpp`, CMake `ArborX` dependency]
- **Grid side (`grid/`):** structured and sparse grids, halos, load balancing (through the optional ALL library), FFTs (through heFFTe), linear solvers (through HYPRE), and spline interpolation. This part used to be called "Cajita". Release 0.8.0 removed the Cajita deprecation wrappers. [KNOWN: `grid/src` file names, CMake dependencies, CHANGELOG 0.8.0]

## How the project is organized
- `core/` holds the particle library, with `src` (about 30 public headers), `unit_test` and `performance_test`. `grid/` holds the grid library. `example/` has numbered tutorials (20 core, 17 grid). The other folders are `benchmark/`, `cmake/` and `docker/`. [KNOWN: repo tree]
- Mostly header-only C++: 134 `.hpp` versus 59 `.cpp` files. [KNOWN: file count; INFERRED: "header-only" because templates live in headers]
- Languages: C++ about 96.5% by bytes, plus CMake, Python, Dockerfile and C. [KNOWN: GitHub languages API]
- Build: CMake 3.16 or newer, and Kokkos 4.1 or newer is required. Optional: MPI, ArborX, ALL, HYPRE 2.22.1+, heFFTe 2.3.0+, Silo and HDF5. Tests use GoogleTest. [KNOWN: CMakeLists.txt]
- CI: GitHub Actions workflows `CI.yml`, `Nightly.yml`, `docker.yml` and `format-check.yml`. [KNOWN: `.github/workflows/`]
- Contributors: 43 including anonymous commit authors, 33 GitHub accounts without them. Created 2018-09-24. 284 stars and 68 forks. [KNOWN: GitHub API]
- Citation: a JOSS paper (`CITATION.bib`) and a Zenodo DOI for releases. [KNOWN: README]

## Who uses it / why it matters
Cabana packages the hard parts of GPU particle codes so lab teams don't each rebuild them. That matters for exascale machines like ORNL's Frontier, though the README doesn't name Frontier. [INFERRED] For usage evidence, see Connector's section in `signals/cabana.md` (rule 17).

## Related projects
- Finch (`finch`): built on Cabana. [KNOWN: catalog row]
- Kokkos: required dependency only, outside the catalog (rule 13).

## Known / Inferred / Unknown
- KNOWN: license, multi-lab README line, DOE CODE, releases, layout, dependencies, CI files, counts.
- INFERRED: the AoSoA performance rationale, step order, Frontier relevance.
- UNKNOWN: ORNL's share of the development, and post-ECP funding.

## Sources (accessed 2026-10-24)
- https://github.com/ECP-copa/Cabana (README.md, LICENSE, CHANGELOG.md, CMakeLists.txt, CITATION.bib, core/, grid/, example/, .github/workflows/)
- https://api.github.com/repos/ECP-copa/Cabana (plus /languages, /releases, /contributors)
- https://github.com/ECP-copa/Cabana/wiki (linked)
- https://www.osti.gov/doecode/biblio/45702 (per Scout's catalog row)

## Sweep 2 notes (ORNL Fact Checker, 2026-10-24)
- Verified: README CoPA lines name ORNL among the developer labs, DOE CODE code-45702 "Cabana" lists ORNL as research org (OSTI API, 2018-09-30), so rule 13 passes as a named contributing lab and research org. Also verified: LICENSE "Copyright 2018-2023 the Cabana authors", API NOASSERTION, 9 releases with 0.8.0 on 2026-05-29, last master commit 2026-09-16, contributors 43 with anonymous.
- The README's lab list says "PPNL". That's probably meant to be PNNL or PPPL (INFERRED). The quote stays as written.
- No corrections.
