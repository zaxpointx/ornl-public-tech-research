# FAR3d

- Official page: DOE CODE record https://www.osti.gov/doecode/biblio/144364 (DOI 10.11578/dc.20240924.1) [KNOWN]
- Repo: https://github.com/DSfusion/FAR3d (a side account, not the main ORNL org; it qualifies under RULES 13 through the DOE CODE record, which lists ORNL) [KNOWN: DOE CODE record, accessed 2026-10-24]
- Docs: `User_guide.pdf` and the `Help/` PDFs in the repo [KNOWN: repo tree]
- License: no license file in the repo. The User's Guide says it is "a freely distributed code under the GNU license" without naming a version. The source header carries a 2024 copyright held by the developers personally, not UT-Battelle. [KNOWN: `User_guide.pdf` p.2; `src/far3d.f90` line 4; accessed 2026-10-28] The DOE CODE record's license field says "MIT License", which conflicts with the guide's GNU wording; GitHub's API reports no license. Which license really applies is [UNKNOWN]. [KNOWN: https://www.osti.gov/doecode/biblio/144364; GitHub API, accessed 2026-10-29] (corrected in a fact-check pass, 2026-10-29)
- Status: active (last push 2026-10-15) [KNOWN: GitHub API, accessed 2026-10-24]

## Walkthrough
FAR3d is a physics code for fusion reactors. It checks whether a magnetically trapped plasma will start to wobble because of a small group of very fast particles inside it. [KNOWN: User's Guide 1.1, paraphrased]
The problem: in a tokamak or stellarator (doughnut-shaped and twisted-doughnut-shaped magnetic bottles for fusion), the hot plasma contains "energetic particles", such as fusion-born alpha particles or ions from heating beams. They can push on the plasma's natural waves, called Alfvén modes (waves that run along the magnetic field lines, a bit like vibrations on a guitar string). If those waves grow, they knock the fast particles out before they can heat the plasma. [INFERRED: standard background, consistent with the `Help/` notes on Alfvén and acoustic modes]
What goes in: a magnetic "equilibrium" (the shape of the magnetic field, made by another code called VMEC and converted with the included BOOZ_XFORM tool), plasma profiles (density and temperature from the center out), and an input settings file called `Input_Model`. [KNOWN: User's Guide 0.2-0.3, 1.1]
What happens: FAR3d solves a simplified set of plasma fluid equations with extra terms for the fast particles, and looks for waves that grow. [KNOWN: User's Guide 1.1]
What comes out: the growth rate and frequency of the most unstable wave (in a file called `farprt`), plus the wave's shape. [KNOWN: User's Guide 0.2, 5]
Where humans act: a physicist prepares the equilibrium and profiles for a specific machine, picks the settings, and judges whether the result is physical. [INFERRED]
What it is not: not a full particle-by-particle (kinetic) simulation. It is a faster fluid model whose closure terms are tuned against fuller kinetic codes. [KNOWN: User's Guide 1.1]
Example: the guide's sample case loads a DIII-D tokamak (a US research machine) equilibrium and reports a "Toroidal Alfvén Eigenmode", with its frequency and growth rate. [KNOWN: User's Guide 0.2]
Unknown: who funds the current work beyond the DOE CODE sponsor field, and how widely it runs on ORNL supercomputers.

## What it is (plain English, 2-4 sentences)
A Fortran code that predicts whether fast particles in a fusion plasma will drive unstable waves, and how quickly those waves grow. The guide calls it "a fast tool" for linear stability studies. [KNOWN: User's Guide 1.1, short quote] Version 2.0 runs in parallel with MPI and has both CPU and GPU versions. [KNOWN: README]

## How it works (plain English, no jargon without definition)
1. Build the field map: start from a VMEC equilibrium and convert it with BOOZ_XFORM into "Boozer coordinates", a coordinate system where magnetic field lines look straight, which makes the math simpler. [KNOWN: `BOOZ_XFORM/` folder and its PDF; User's Guide 6]
2. Add the plasma: read the profiles (`profiles.dat`, `profiles_ex.dat`) and the `Input_Model` settings. [KNOWN: file names in `src/*.f90`; User's Guide 2-3]
3. Solve: evolve three reduced equations (for pressure, an electric-potential-like stream function and the magnetic flux), plus two moment equations for the fast ions' density and parallel speed. "Landau closure" terms stand in for the particle effects a fluid model can't see directly. [KNOWN: User's Guide 1.1]
4. Optional eigensolver: the `Eigensolver/` add-on (built on the JDQZ library) finds the modes directly instead of waiting for them to grow in time. [KNOWN: folder contents; User's Guide 7.1]
5. Output: `farprt` with growth rate and frequency, plus eigenfunction files. [KNOWN: User's Guide 5]
6. Where a person acts: preparing inputs and reading the results. [INFERRED]

## How the project is organized
- Layout: `src/` (35 entries: Fortran modules such as `equilibrium.f90`, `solve.f90`, `diagnostics.f90`, `output_mod.f90`, plus `Makefile`, `all_make` and `gpu_make`), top-level `matrix_cpu.f90` and `matrix_gpu.f90`, `Eigensolver/`, `BOOZ_XFORM/`, `Help/` (theory notes as PDFs), `User_guide.pdf`, `CMakeLists.txt`, and a 9-line README ending "(to be filled in)". [KNOWN: repo tree, 2026-10-28]
- Languages and build: Fortran with some C. CMake 3.10+ finds MPI and OpenMP, both marked REQUIRED (a comment calls OpenMP optional, but the line says REQUIRED). [KNOWN: `CMakeLists.txt`] The GPU build uses `ftn` with `-acc=gpu -cuda`, which are NVIDIA HPC compiler flags for OpenACC (directives that move loops onto the GPU). `ftn` is the Cray compiler wrapper used on HPE/Cray supercomputers. [KNOWN: `src/gpu_make`; the Cray reading is INFERRED]
- Docs drift: the guide's quick start describes an older layout (`Models/`, `Config.sh`, `Input_basic/`, a tar file) and a download link under another GitHub owner, none of which match the current tree. [KNOWN: User's Guide p.4 versus repo tree]
- Branches: PreviousFar3d (the old serial version), Nonlinear_helical_couplings, eigen_lib, imas, library, plus a merged patch branch, yashugh92-patch-1 (corrected in a fact-check pass, 2026-10-29). [KNOWN: GitHub branch list, 2026-10-24; fresh clone 2026-10-29] The `imas` branch name suggests work toward IMAS, ITER's data standard. [INFERRED from the name only]
- Contributors: 4 counting anonymous authors, 3 accounts. [KNOWN: GitHub contributors API] 8 stars, 4 forks, 1 open issue. [KNOWN: GitHub API, 2026-10-24]
- Releases: tag v2.0 on 2024-09-13. [KNOWN]
- Tests and CI: none visible. [KNOWN: repo tree]
- Why it was built this way: UNKNOWN.

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2020-05-18 | GitHub repo created | GitHub API | [KNOWN] |
| 2020-2022 | 44, 18 and 6 commits (committer date; by author date 44, 21 and 11; same on all branches and master) | git log, fresh clone 2026-10-29 | [KNOWN] (corrected in a fact-check pass, 2026-10-29) |
| 2024-09-13 | v2.0 tag (parallel MPI version) | GitHub tags | [KNOWN] |
| 2024-09-24 | DOE CODE record, DOI 10.11578/dc.20240924.1, ORNL, sponsor Fusion Energy Sciences | https://www.osti.gov/doecode/biblio/144364 | [KNOWN] |
| 2026-03-13 | master commit "Replace with updated code" | git log | [KNOWN] |
| 2026-10-15 | latest push (on another branch) | GitHub API | [KNOWN] |

## Who uses it / why it matters
An OSTI search for "FAR3d" showed 20 hits on its first page; the OSTI records API reports 61 records matching "FAR3d" on 2026-10-29, so 20 was a page count, not a total (corrected in a fact-check pass, 2026-10-29). The hits include 2025-26 papers applying it to JET, LHD, ITER, TJ-II and ARC, many sponsored by DOE Fusion Energy Sciences. [KNOWN: OSTI search, accessed 2026-10-24; individual papers not re-read for this brief] That means it is used on real machines in Europe, Japan and the US, and on the ITER design. [INFERRED from the paper titles] Fast-particle-driven waves are a known risk for burning plasmas, so a quick stability check is useful before running expensive kinetic codes. [INFERRED: User's Guide 1.1 frames it as the fast option]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| VMEC | uses (equilibrium input; outside project) | User's Guide 1.1 | [KNOWN] |
| BOOZ_XFORM | bundled converter (outside project) | `BOOZ_XFORM/` | [KNOWN] |
| Stellarator-Tools | related topic (stellarator equilibria); map link 67 | https://github.com/ORNL-Fusion/Stellarator-Tools | [INFERRED] |

## What stands out
The paperwork lags the code: the README is a stub, the guide describes an older layout, and the license is stated only in a PDF. The physics output, meanwhile, is steady (papers on five machines in two years), and the build files show it is being moved onto GPU supercomputers. It looks like a small expert team's working code more than a packaged product.

## Ten questions (GOAL.md)
1. Problem and audience: fast-particle-driven instability in fusion plasmas, for fusion physicists. [KNOWN: guide]
2. Place in the tree: fusion energy science. The DOE CODE record lists ORNL and FES. [KNOWN]
3. Who pays: DOE Fusion Energy Sciences per DOE CODE. [KNOWN]
4. Code: Fortran plus MPI and OpenMP, OpenACC for GPUs, CMake and Makefiles. [KNOWN]
5. Alive: yes, with commits in 2026 and a v2.0 in 2024, though commits are sparse. [KNOWN]
6. Outside users: papers from European, Japanese and US groups per OSTI search titles. [INFERRED]
7. Connections: upstream VMEC and BOOZ_XFORM; downstream, papers and comparisons with kinetic codes. [KNOWN/INFERRED]
8. What it teaches: lab scientists may keep a code on a side GitHub account while registering it with DOE CODE under ORNL. [KNOWN]
9. Student path: hard. You'd need plasma physics, Fortran and MPI. A student could still help by updating the README to match the current tree. [INFERRED]
10. Still unknown: exact license version and which ORNL machines it targets. Searched without result: a public test-case folder in the current tree.

## Known / Inferred / Unknown
- KNOWN: the DOE CODE record (ORNL, FES), the physics model from the guide, the build files, the GPU flags, the history and the docs drift.
- INFERRED: the Cray reading of `ftn`, the IMAS branch purpose, and outside use from paper titles.
- UNKNOWN: which license applies (guide says GNU with no version, DOE CODE says MIT, no license file), the GPU targets and the current funding level.

## Verification notes
Filled by the fact-check pass.

## Sources (URL, title, accessed date, what it supports)
- https://www.osti.gov/doecode/biblio/144364, DOE CODE record "FAR3d", accessed 2026-10-24, supports the DOI, ORNL, FES and the date
- https://github.com/DSfusion/FAR3d, the repo (README, CMakeLists.txt, src/gpu_make, User_guide.pdf, Help/), accessed 2026-10-28, supports the code, build and docs facts
- https://api.github.com/repos/DSfusion/FAR3d, repo metadata, accessed 2026-10-24, supports dates, stars, forks and issues
- https://www.osti.gov/search/semantic:FAR3d, OSTI search, accessed 2026-10-24, supports the 20 hits and the machine names in titles

## Quality gate
- [x] Every load-bearing claim has a source and a tag
- [x] Facts are kept apart from interpretation
- [x] ORNL relationship is not overstated, and maturity verbs match the source
- [x] Walkthrough, flow, timeline and unknowns are present
- [x] Ten questions answered or marked UNKNOWN
- [x] No copied text beyond short cited quotes; people by role only
- [ ] Two fact-check sweeps done
- [ ] INDEX, catalog, LAB-TREE and connections map updated

## Fact-check notes (2026-10-29)
- Re-checked against GitHub API, a fresh `--filter=blob:none` clone, DOE CODE 144364 and the User's Guide text. Verified: no LICENSE or COPYING file and no GitHub license; guide wording "freely distributed code under the GNU license" with no version; developer copyright line in `src/far3d.f90`; created 2020-05-18; last push 2026-10-15 on Nonlinear_helical_couplings; master's last commits 2026-03-12/13; v2.0 tag; 8 stars, 4 forks, 1 open issue; 4 contributors (3 accounts); 35 `src/` entries; MPI and OpenMP both REQUIRED in CMake; VMEC input stated in the guide; DOE CODE ORNL research org, FES sponsor, 2024-09-24.
- Corrected: DOE CODE lists the license as MIT, so the license is now tagged as a source conflict, not as GNU; commit counts labelled by date type; branch list completed.
- DOE CODE also lists developers at two universities alongside ORNL. Noted for the record only.
- connections/map.md link 67 said VMEC input was unverified; the guide states it, so that line was corrected inline.

### Second pass (2026-10-29)
- Re-verified with new sources: v2.0 tag date (git tag, 2024-09-13); OSTI hit count via the records API (corrected: 61 total, not 20); license conflict and commit-count labels from the first pass are in place. No affiliation or copying issues found.
