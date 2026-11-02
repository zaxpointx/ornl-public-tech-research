# Profugus

- Repo: https://github.com/ORNL-CEES/Profugus (a side org; qualifies under RULES 13 via DOE CODE code-10329, which lists ORNL) [KNOWN: catalog row; DOE CODE]
- Official record: DOE CODE https://www.osti.gov/doecode/biblio/10329 (2018-01-18, research org ORNL) [KNOWN: catalog row, OSTI API 2026-10-28]
- Docs: `README.rst` and `doc/` (Sphinx-style source) [KNOWN: repo tree]
- License: BSD-2-Clause; the copyright line names ORNL's Computational Engineering & Energy Sciences group, 2014 [KNOWN: LICENSE]
- Status: unknown (last push 2018-08-14, not archived; last commits in 2017) [KNOWN: GitHub API via catalog; git log]

## Walkthrough
Profugus is a stripped-down, open copy of the core math inside ORNL's Exnihilo reactor physics codes, which include Shift. [KNOWN: README.rst] The README says it exists because Exnihilo is export controlled, and that makes it hard to work with outside computer scientists. Profugus gives them the algorithms without the controlled code. [KNOWN: README.rst, paraphrased]
The problem it solves is a people problem, not a physics one: HPC experts want to tune the hot loops of radiation transport codes for new hardware, but they can't see the real ones. [KNOWN: README.rst]
What goes in: a problem description (geometry and material cross-sections, meaning the odds that a neutron hits and reacts with each material). [KNOWN: Matprop package "material properties (cross-sections)"] Input file format: see `doc/`, not read in detail. [UNKNOWN]
What happens: one of two mini-apps runs. SPn solves a simplified deterministic transport equation (simplified spherical harmonics, a fast approximation of how neutrons spread). MC tracks individual simulated neutrons with Monte Carlo (random sampling of each particle's path). [KNOWN: README package list; method definitions are standard background]
What comes out: flux results plus timing, since the point is performance. [INFERRED from README's purpose]
Where humans act: a researcher builds it, sets up a test problem and measures speed on new hardware. [INFERRED]
What it is not: not Shift and not for real reactor analysis. The README says the kernels are built to study "*performance*, not *correctness*". [KNOWN: README.rst, short quote]
Example: a computer scientist ports the MC kernel to a GPU (there's a `CudaUtils` package) and compares particles-per-second against the CPU version. (Illustrative; the package exists.)
Unknown: how closely Profugus's kernels track today's Shift, since nothing public compares them after 2018.

## What it is (plain English, 2-4 sentences)
An open-source "mini-app" (a small stand-in program that keeps the expensive core of a big code) for radiation transport. It holds Exnihilo's fundamental kernels and was used as a test bed for two DOE ASCR (Advanced Scientific Computing Research) projects, XPRESS and MCREX. [KNOWN: README.rst]

## How it works (plain English, no jargon without definition)
1. Build with TriBITS, the Trilinos build system on top of CMake, against Trilinos (open math solver libraries) and BLAS/LAPACK. MPI and HDF5 are optional. [KNOWN: README "TPLs" table]
2. Pick a mini-app: `SPn` (deterministic) or `MC` (Monte Carlo), backed by `Utils`, `Matprop`, `Alea` and `CudaUtils`. [KNOWN: `packages/`]
3. Run a test problem and measure. [INFERRED]
4. Related: the README points to Minisweep, a separate deterministic Sn sweep mini-app in another repo. [KNOWN: README.rst]

## How the project is organized
- Layout: `packages/` (Alea, CudaUtils, MC, Matprop, SPn, Utils), `install/` (example configure scripts), `doc/`, `cmake/`, and TriBITS files (`PackagesList.cmake`, `TPLsList.cmake`). [KNOWN: repo tree]
- Languages: C++ with CUDA pieces. [KNOWN: package names; INFERRED that CudaUtils is CUDA C++]
- Platforms: `install/` has scripts for macOS (`cmake_macosx.sh`, `cmake_macosx_clang.sh`), generic x86_64, Cray XK7 (Titan-era, with PGI), and several named lab clusters. [KNOWN: file names] So Mac builds were done at some point, but nothing since 2017 has been tested here. [INFERRED]
- Contributors: 10 distinct author names on the default branch (15 across all branches; git shortlog on a fresh clone, 2026-10-29). The README lists the development team; they aren't repeated here. [KNOWN: git shortlog; README]
- Releases: none. [KNOWN]
- Why it was built this way: stated. It keeps export-controlled code out while letting CS collaborators work on the algorithms. [KNOWN: README]

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2013-12-02 | first commit | git log | [KNOWN] |
| 2014 | busiest year, 312 commits (194 in 2015, 71 in 2016) | git log, author dates | [KNOWN] |
| 2017 | last 3 commits | git log | [KNOWN] |
| 2018-01-18 | DOE CODE record code-10329 | DOE CODE | [KNOWN] |
| 2018-08-14 | last push | GitHub API | [KNOWN] |

## Who uses it / why it matters
It was a test bed for ASCR's XPRESS and MCREX projects. [KNOWN: README] Other users are UNKNOWN. It matters as a rare public window into how ORNL's locked transport codes are built inside. [INFERRED] (corrected in a fact-check pass, 2026-10-29: "only" was not supported)

## How it relates to Shift (public sources only)
- Profugus holds "the fundamental computational kernels used in the Exnihilo code suite". [KNOWN: README.rst, short quote]
- The README says Exnihilo is export controlled. [KNOWN]
- Shift is part of the Exnihilo family. [KNOWN: per connections/map.md and the shift-exnihilo brief; not restated in the Profugus README]
- Read it as an open teaching and benchmarking copy of the core math, not a version of Shift you can use for analysis. [INFERRED, matching connections/map.md]
- Does Profugus ship inside SCALE or VERA? No public source says so. [UNKNOWN; the fact-check pass corrected the map on this, 2026-10-29]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| [Shift / Exnihilo](shift-exnihilo.md) | extends (open copy of its kernels for performance testing; exists because Exnihilo is export controlled); map links 208, 209 | https://github.com/ORNL-CEES/Profugus README.rst | [KNOWN] |
| [VERA](vera.md) | related topic (VERA bundles Shift, not Profugus); map link 204 | https://rsicc.ornl.gov/codes/ccc/ccc8/ccc-855.html | [INFERRED] |
| [SCALE](scale.md) | not shown shipping in SCALE; no public source found says it does; map link 208 | Profugus repo; SCALE manual CSAS-Shift chapter names Shift only | [UNKNOWN] (corrected in a fact-check pass, 2026-10-29) |
| Trilinos | uses (outside, open) | README TPL table | [KNOWN] |
| Minisweep | sibling mini-app, separate repo | README.rst | [KNOWN] |

## What stands out
It's an unusually honest README: it says the parent code is export controlled, that this copy is for speed testing and not for correctness, and why it exists. That makes it a clear example, among the projects read so far, of how a lab shares algorithms from controlled software. (Interpretation; softened from "cleanest in the catalog" in a fact-check pass, 2026-10-29.)

## Ten questions (GOAL.md)
1. Problem and audience: letting outside HPC researchers optimize transport kernels, for computer scientists. [KNOWN]
2. Place in the tree: ORNL's CEES group, reactor and radiation transport, HPC. [KNOWN: LICENSE; INFERRED placement]
3. Who pays: DOE CODE lists the sponsor as USDOE Office of Science, Advanced Scientific Computing Research (ASCR). [KNOWN: https://www.osti.gov/doecode/biblio/10329] (corrected in a fact-check pass, 2026-10-29)
4. Code: C++/CUDA, TriBITS/CMake, Trilinos. [KNOWN]
5. Alive: no, quiet since 2017-18. [KNOWN]
6. Outside users: ASCR XPRESS and MCREX. [KNOWN]
7. Connections: Exnihilo/Shift (locked), Trilinos, Minisweep. [KNOWN]
8. What it teaches: export control shapes how ORNL shares code, through open mini-apps. [KNOWN for this case]
9. Student path: a stretch. You'd need C++, CMake and an old Trilinos to build it, but the macOS scripts help, and reading `packages/MC` is a good way to learn how Monte Carlo transport is coded. [INFERRED; not built]
10. Still unknown: how it compares to today's Shift, and the input format. Searched without result: any post-2018 successor named publicly.

## Known / Inferred / Unknown
- KNOWN: purpose, the export-control reason, packages, dependencies, platform scripts, history and license.
- INFERRED: the teaching-copy reading, buildability today and outputs.
- UNKNOWN: kernel parity with Shift now, and current users.

## Verification notes
Filled by the fact-check pass.

## Sources (URL, title, accessed date, what it supports)
- https://github.com/ORNL-CEES/Profugus, repo (README.rst, LICENSE, packages/, install/), cloned 2026-10-29, supports everything code-side
- https://www.osti.gov/doecode/biblio/10329, DOE CODE record, accessed 2026-10-28 (discovery pass), supports ORNL and the date
- connections/map.md, team map, read 2026-10-29, supports the Shift-family framing

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
First-pass fact check against a fresh clone (2026-10-29), the public GitHub repo page, and the DOE CODE page for code-10329. The GitHub API hit its anonymous rate limit during this pass, so API-only numbers (stars, forks) were not re-read.
- Verified: README purpose, the export-control statement about Exnihilo, the "*performance*, not *correctness*" quote, XPRESS and MCREX, Minisweep as a separate repo; `packages/` and `install/` contents (macOS, x86_64, XK7/PGI and other cluster scripts); LICENSE copyright line (2014, CEES group) and BSD-2-Clause (also on DOE CODE); DOE CODE release date 2018-01-18 and ORNL research org; first commit 2013-12-02; yearly counts 2014 312, 2015 194, 2016 71, 2017 3 (author dates, default branch); last commit 2017-11-07 (author and committer date match).
- Commit count spot check (Rule 17): default branch 598 commits, all branches 1571 (29 remote branches), fresh clone 2026-10-29.
- Corrected: funding is not unknown; DOE CODE names ASCR as sponsor. Contributor count now says it counts the default branch. The SCALE row in Related projects was tagged KNOWN for an absence of evidence; it is now UNKNOWN, matching the brief's own Shift section.
- Kept: "open twin of Shift" reading stays INFERRED; Shift being part of SCALE is a separate, known fact from the SCALE manual's CSAS-Shift chapter and is not evidence that Profugus ships with SCALE.
- Restricted content: the brief describes only what the public README says about export control. It does not include or guess at any controlled code. Nothing removed.

### Second pass (2026-10-29)
Skeptical reread; first-pass fixes confirmed in place and reading cleanly.
- Retried GitHub API: last push 2018-08-14 UTC, 29 stars, 6 forks, not archived, BSD-2-Clause, 0 releases. All verified; these were unverifiable in the first pass. The clone also has no tags, which agrees with "no releases". (The rendered repo page fetched as "0 stars, 0 forks", which is a page-rendering artifact, not data; the API figures are used.)
- DOI 10.11578/dc.20180418.8: resolves. Verified.
- Corrected: "the only public window" into the controlled codes was an unsupported "only"; now "a rare public window". "Cleanest example in the catalog" softened to an interpretation limited to projects read so far.
- Export-control wording: the brief still repeats only what the public README says. Nothing restricted.
