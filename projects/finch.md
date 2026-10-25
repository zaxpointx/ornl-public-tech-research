# Finch
- Official page: none separate. The README and `examples/README.md` are the docs. A Zenodo DOI for citing is linked: https://zenodo.org/doi/10.5281/zenodo.10698939 [KNOWN: README]
- Repo: https://github.com/ORNL-MDF/Finch (default branch `main`). GitHub's description is "Finite difference heat transfer using Cabana for additive manufacturing". [KNOWN: GitHub API]
- License: BSD 3-Clause, "Copyright (c) 2024, Oak Ridge National Laboratory". The GitHub API also says BSD-3-Clause. [KNOWN: LICENSE lines 1-3, GitHub API]
- Status: active (rule 14). The last commit was 2026-10-05 09:35 ET, and it isn't archived. The latest release is 0.2.0 from 2024-09-20, so the code still moves but releases have paused. [KNOWN: git log, GitHub API]
- Scope (rule 13): CORROBORATED. The copyright holder is Oak Ridge National Laboratory (LICENSE), and DOE CODE code-122647 ("Finch", 2024-02-23, DOI 10.5281/zenodo.10698940, same description as the repo) lists ORNL as research org under contract AC05-00OR22725. [KNOWN: LICENSE; https://www.osti.gov/doecode/biblio/122647, accessed 2026-10-24]
  - Org unit: the GitHub org is ORNL-MDF. Reading "MDF" as the Manufacturing Demonstration Facility is the catalog's guess. No page I read spells it out. [INFERRED]

## Plain-language walkthrough
- **What it is:** a C++ program that simulates how heat spreads through metal while a laser melts it, layer by layer, in metal 3D printing (additive manufacturing, AM). [KNOWN: README, description]
- **Key terms:**
  - *Finite difference* means chopping the part into a 3-D grid of tiny cubes and updating each cube's temperature from its neighbors every small time step.
  - A *scan path* is the route the laser takes.
  - *Solidus* and *liquidus* are the temperatures where the metal starts to melt and is fully melted.
  - The *Courant number* is a safety limit on how big a time step can be compared with the cube size, so the math stays stable. [KNOWN: input names and units in `examples/README.md`; INFERRED: the plain explanations]
- **The problem:** the grain structure of a printed metal part, and so its strength, depends on how fast each spot cools and solidifies. Measuring that inside a melt pool is hard, so people simulate it. Finch does that fast, on CPUs or GPUs. [KNOWN: the solidification outputs in the examples README; INFERRED: the motivation]
- **What goes in:** a JSON input file with time settings, grid size and cell size, material properties (density, specific heat, conductivity, latent heat, solidus and liquidus), laser settings (absorption and beam radius), and a scan-path file. A bundled utility can generate scan paths from a region, hatch spacing and angle. [KNOWN: `examples/README.md`, `utilities/CreateScanPaths/`]
- **What happens:**
  1. The grid is split across MPI processes.
  2. The moving-beam model adds laser heat along the path segments.
  3. The solver steps the heat equation forward in time.
  4. Optional sampling records, for each spot, when it melted and when it started solidifying, how fast it solidified, and its temperature gradients. [KNOWN: `src/Finch_*.hpp`, `src/MovingBeam/`, examples README]
- **What comes out:** temperature fields at chosen output steps, plus solidification data files. One output format, `exaca`, is cut down to what ExaCA (a grain-growth code) needs. [KNOWN: examples README]
- **Where humans act:** an AM researcher picks the material, the laser and the path, and decides what to sample. They also build Kokkos and Cabana first. [KNOWN: README build steps]
- **What it is not:** it doesn't simulate fluid flow in the melt pool. AdditiveFOAM does that with OpenFOAM. Finch also doesn't predict grains itself; it feeds ExaCA. [KNOWN: the exaca output option; INFERRED: the contrast with AdditiveFOAM]
- **What's unknown:** whether a 0.3 release is planned, and who runs it outside its own team. The newest commit (2026-10-05) adds "Optional coupling with stork for interpolation". 3DThesis also has a Stork mode, but no page I read says what stork is. [KNOWN: git log; UNKNOWN: what stork is]
- **Example:** the bundled `single_line` example melts one straight laser track on a small block and writes the solidification data along it. [KNOWN: `examples/single_line/`]

## How it works
- **Built on Cabana:** Finch uses Cabana's grid sub-package (Cabana::Grid) for the distributed 3-D mesh and halo exchange. Halo exchange means swapping edge cells with neighboring processes. Under Cabana, Kokkos provides "performance portability": one source code that compiles for serial, OpenMP, CUDA or HIP back ends. [KNOWN: README dependency table and build notes, CI.yml backends; INFERRED: the halo explanation]
- **Code pieces:** `Finch_Inputs` (JSON parsing), `Finch_Grid`, `Finch_Boundary`, `Finch_Solver`, `Finch_SolidificationData`, `Finch_Run`, and `MovingBeam/` (beam and path segments). `applications/SingleLayer.cpp` is the main program. [KNOWN: tree]

## How the project is organized
- Top level: `src/`, `applications/`, `utilities/CreateScanPaths/`, `examples/` (`single_line`, `create_scan_path`), `cmake/`, and `.github/workflows/` (CI, Weekly, format). [KNOWN: tree]
- Languages: C++ about 95.1% by bytes, CMake 3.9%, Shell 1.0%. [KNOWN: GitHub languages API]
- Build: CMake 3.12 or newer, plus Cabana 0.6.1 (with Kokkos and MPI) and nlohmann/json 3.10 or newer, which is downloaded automatically if it's missing. [KNOWN: README]
- CI: GitHub Actions builds with g++, clang++ and Intel icpx on Serial and OpenMP, plus HIP and CUDA 12.2 jobs, using containers from the ECP-copa (Cabana) org. [KNOWN: `.github/workflows/CI.yml`]
- Releases: 0.1.0 (2024-02-23) and 0.2.0 (2024-09-20). [KNOWN: GitHub API]
- History: 192 commits. The first is 2023-05-15 UTC (before the repo was created on 2024-02-23, so history came from somewhere else first). By year there are 98 in 2023, 86 in 2024, 4 in 2025 and 4 in 2026. 8 stars and 7 forks. [KNOWN: git log, GitHub API; INFERRED: the earlier-history point]
- Contributors: 4 including anonymous commit authors, 3 GitHub accounts. [KNOWN: GitHub API]

## Who uses it / why it matters
Fast thermal models let AM researchers try many laser paths before printing real parts. Finch's GPU support is what makes it fast at full-part scale. [INFERRED] Its `exaca` output format shows it was built to feed microstructure prediction. [KNOWN: examples README] Usage evidence goes in `signals/finch.md` once it exists.

## Related projects
- Cabana (`cabana`): Finch is built on it. [KNOWN: README]
- ExaCA (an outside project in the map): Finch has a dedicated output format for it. [KNOWN: examples README]
- Myna, AdditiveFOAM and 3DThesis: other AM thermal and workflow tools in the catalog. The map records shared developers with Myna. [KNOWN per map]

## Known / Inferred / Unknown
- KNOWN: license and copyright, dates, releases, inputs and outputs, code layout, dependencies, CI targets, counts.
- INFERRED: the MDF meaning, the physics explanations, the motivation, the earlier-history point.
- UNKNOWN: org unit, users, plans for the next release.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL-MDF/Finch (README.md, LICENSE, examples/README.md, src/, applications/, utilities/, .github/workflows/CI.yml)
- https://api.github.com/repos/ORNL-MDF/Finch (plus /languages, /releases, /tags, /contributors with and without anon=1)
- https://zenodo.org/doi/10.5281/zenodo.10698939 (linked from the README, not opened)
- https://www.osti.gov/doecode/biblio/122647 (added in the fact-check pass)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified on a fresh clone of ORNL-MDF/Finch: LICENSE "Copyright (c) 2024, Oak Ridge National Laboratory", tags 0.1.0 and 0.2.0, last commit 2026-10-05 09:35 ET with message "Optional coupling with stork for interpolation", 192 commits (98/86/4/4 for 2023-2026), first commit 2023-05-15, README requirements (CMake 3.12+, Cabana 0.6.1, json 3.10+), CI compilers and back ends, examples, contributors 4 with anonymous and 3 accounts. Zenodo link resolves.
- Corrected: the brief called scope CORROBORATED on the LICENSE alone, which is one source. Added DOE CODE code-122647 as the second, independent source, so CORROBORATED now holds.

## GOAL.md questions (added 2026-10-24)
- **Who pays (Q3):** the DOE CODE record (code-122647) lists the DOE Office of Science and the National Nuclear Security Administration as sponsors, with ORNL as the research org. [KNOWN: OSTI API records/code-122647, accessed 2026-10-24] Which program inside those offices is [UNKNOWN].
- **Where in the tree (Q2):** ORNL, then additive manufacturing, on the 3D-printing ladder. It's coupled with ExaCA and built on Cabana, from the exascale co-design center. [KNOWN, above]
- **What it teaches about ORNL (Q8):** exascale-era libraries (Kokkos, Cabana) became the base for new applied codes after the Exascale Computing Project. [KNOWN: dependencies; INFERRED: the lesson]
- **Student angle (Q9):** it has a CONTRIBUTING.md. [KNOWN: tree] To contribute you'd need modern C++, CMake, and Kokkos's way of writing code that runs on both CPUs and GPUs. [INFERRED]
- **Searched without result (Q10):** the specific program inside the sponsoring offices, what Stork is.

- Fact-check pass 2026-10-24 (GOAL questions): Q3 corrected. The OSTI API record code-122647 does fill sponsor_orgs (USDOE SC and NNSA); the earlier line said it was blank. Q9 CONTRIBUTING.md confirmed in a fresh clone.
