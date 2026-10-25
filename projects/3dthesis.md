# 3DThesis (3D THErmal Simulation Software)
- Official page: none separate. The README is the docs. The original release is on DOE CODE, and later releases are on Zenodo (https://doi.org/10.5281/zenodo.13686743). [KNOWN: README]
- Repo: https://github.com/ORNL-MDF/3DThesis (default branch `master`). GitHub's description is "Heat transfer code utilizing a nondimensionalized semi-analytic solution to moving heat sources with a 3D Gaussian power density". [KNOWN: GitHub API]
- License: BSD 3-Clause, "Copyright 2019 UT-Battelle, LLC". The GitHub API also says BSD-3-Clause. [KNOWN: LICENSE lines 1-3, GitHub API]
- Status: active (rule 14). Release 4.0.0 came out 2025-05-29, and the last commit and push were on 2026-08-26 (commit at 15:02 ET). Not archived. [KNOWN: GitHub API, git log]
- Scope (rule 13): CORROBORATED.
  - DOE CODE code-26241 ("3DThesis (3D THErmal Simulation Software)", released 2018-12-21, version 1.0, DOI 10.11578/dc.20200909.3) lists "Research Org.: Oak Ridge National Laboratory (ORNL), Oak Ridge, TN" and sponsor USDOE. [KNOWN: https://www.osti.gov/doecode/biblio/26241, reached through the README's DOI]
  - The README's acknowledgment says it was authored by UT-Battelle under DOE contract DE-AC05-00OR22725. [KNOWN: README]
  - The DOE CODE record points to an earlier GitLab.com repository under an individual account, not this GitHub repo. That's an older home, recorded as stated and not followed further. [KNOWN: DOE CODE record]
- Original sponsors, per the README: DOE's Office of Energy Efficiency and Renewable Energy Advanced Manufacturing Office, and the Office of Electricity's Transformer Resilience and Advanced Components (TRAC) program. [KNOWN: README Acknowledgements]
- Org unit: ORNL-MDF GitHub org, same as Finch. [INFERRED: Manufacturing Demonstration Facility, not stated]

## Plain-language walkthrough
- **What it is:** a fast C++ calculator for temperatures inside a metal part while a laser or electron beam scans across it during metal 3D printing. [KNOWN: README, DOE CODE abstract]
- **Key terms:**
  - *Semi-analytic* means it uses a known math formula for heat spreading from a moving hot spot and only does the time integration numerically. It doesn't simulate every grid cell step by step.
  - *Nondimensionalized* means the equations are rescaled so units cancel out, which makes the math cleaner and faster.
  - A *Gaussian* heat source is a beam that's hottest in the middle and fades smoothly outward, like a bell curve in 3-D.
  - *Conduction-only* means heat moves through the solid by conduction. It ignores the swirling of liquid metal. [KNOWN: description, DOE CODE abstract says "analytic, conduction-only approach"; INFERRED: the explanations]
- **The problem:** DOE CODE's abstract says fluid-dynamics models of a whole build layer "may take months to finish a simulation." 3DThesis trades some physics for speed, so researchers can get the temperature and solidification conditions for a whole layer. [KNOWN: DOE CODE abstract]
- **What goes in:** a set of small text files.
  - Required: a mode file (Solidification or Snapshots), a material file (temperatures, conductivity, specific heat, density), a beam file (width, depth, power, absorption efficiency) and a path file (line melts and spot melts with power and speed).
  - Optional: domain, output and settings files. Several beams can run at once using numbered beam and path files. [KNOWN: README Inputs]
- **What happens:**
  1. For each point in the domain, the code adds up the heat contributions from the beam's past path, using an adaptive time-integration scheme from the cited 2019 paper.
  2. It either takes temperature snapshots at chosen times, or searches for the moment each point cools past the liquidus temperature.
  3. Tracking modes (None, Volume, Surface) skip points that aren't molten, to save time. [KNOWN: README Mode file, CITATION.bib title "An adaptive integration scheme for heat conduction in additive manufacturing"]
- **What comes out:**
  - Temperatures or temperature histories.
  - Solidification time, thermal gradient (G), solidification-front speed (V), cooling rate, and the fraction of small round grains (equiaxed fraction).
  - Melt-pool size stats.
  - An "RDF" (Reduced Data Format) output that ExaCA can read. [KNOWN: README Output file]
- **Where humans act:** a researcher writes the input files, picks the absorption efficiency from published values, and tunes resolution against run time. The README warns that doubling resolution in each direction costs about 8 times more. [KNOWN: README]
- **What it is not:** it doesn't model melt-pool fluid flow (AdditiveFOAM does that). The README also calls its "Secondary" solidification option "experimental" and says it "should never be used". [KNOWN: README; INFERRED: the contrast]
- **What's unknown:** whether the GitLab.com history was fully moved over, and who uses it outside the team.
- **Example:** `examples/solidification` scans a beam along a path and writes G and V at every point. Those two numbers are what metallurgists use to predict grain shape. [KNOWN: examples folder, outputs; INFERRED: the metallurgy point]

## How it works
- The source in `src/` is small and flat: `Init` (reads the inputs), `Grid`, `Calc` (the heat formula and integration), `Melt`, `Run` (the modes, including a newer "Stork" tracking mode), `Out`, `Util`, `DataStructs` and `MpiStructs`. [KNOWN: tree, `src/Run.cpp` line 400]
- Parallelism: OpenMP threads on one machine, with optional MPI to split the domain across machines. [KNOWN: README Build]

## How the project is organized
- Top level: `src/`, `examples/` (snapshot, snapshot_T_hist, solidification, solidification_mpstats, solidification_multibeam, solidification_stork), `bin/`, `CMakeLists.txt`, a legacy `makefile` that's planned for removal, `BUILD.md` and `CITATION.bib`. [KNOWN: tree, README]
- Languages: C++ about 98.5% by bytes, then CMake, Makefile and Shell. [KNOWN: GitHub languages API]
- Build: a C++ compiler plus OpenMP, with MPI optional. CMake is the main path. [KNOWN: README]
- CI: GitHub Actions with g++ and clang++ in containers from the ORNL-MDF org, plus a Windows job. [KNOWN: `.github/workflows/CI.yml`]
- Releases: 1.0.0, 2.0.0 and 3.0.0 were all published 2024-09-04 (looks like back-filled history), then 4.0.0 on 2025-05-29. [KNOWN: GitHub API; INFERRED: the back-fill]
- History: 119 commits. The first is 2019-06-11, before the GitHub repo was created on 2024-08-28. By year there's 1 in 2019, 1 in 2020, 3 in 2021, 8 in 2023, 85 in 2024, 14 in 2025 and 7 in 2026. 17 stars and 3 forks. [KNOWN: git log, GitHub API]
- Contributors: 5 including anonymous commit authors, 5 GitHub accounts. [KNOWN: GitHub API]

## Who uses it / why it matters
It's the "quick estimate" tier of ORNL's AM thermal tools. It's fast enough to sweep a whole layer and hand G and V to grain-growth models. [INFERRED] Myna wraps it as one of its applications. [KNOWN per myna brief] Usage evidence goes in `signals/3dthesis.md` once it exists.

## Related projects
- Myna (`myna`): has a `thesis` application wrapper. [KNOWN per myna brief]
- ExaCA (an outside project in the map): reads its RDF output. [KNOWN: README]
- Finch and AdditiveFOAM: other AM thermal models in the catalog. Finch is grid-based and AdditiveFOAM handles fluid flow. [KNOWN: their READMEs; INFERRED: the tiering]
- "Stork": a tracking mode name shared with Finch's latest commit ("Optional coupling with stork for interpolation"). What stork is wasn't found on any page I read. [KNOWN: both repos; UNKNOWN: what stork is]

## Known / Inferred / Unknown
- KNOWN: license, DOE CODE record and abstract, sponsors, inputs and outputs, layout, build, CI, releases, dates, counts.
- INFERRED: the term explanations, the MDF meaning, the release back-fill, the tool tiering.
- UNKNOWN: org unit, what stork is, users outside ORNL.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL-MDF/3DThesis (README.md, LICENSE, CITATION.bib, src/, examples/, .github/workflows/CI.yml)
- https://api.github.com/repos/ORNL-MDF/3DThesis (plus /languages, /releases, /tags, /contributors with and without anon=1)
- https://www.osti.gov/doecode/biblio/26241 (abstract and "Research Org.: Oak Ridge National Laboratory (ORNL)")
- https://doi.org/10.1016/j.apm.2019.07.008 (the method paper cited in CITATION.bib, not read)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified on a fresh clone of ORNL-MDF/3DThesis and public records: BSD 3-Clause LICENSE, README DOE CODE and Zenodo links (Zenodo resolves), UT-Battelle contract acknowledgment, "experimental and should never be used" Secondary option, the Stork mode in `src/Run.cpp`, the six example folders, tags 1.0.0 to 4.0.0, last commit 2026-08-26 15:02 ET, 119 commits (1/1/3/8/85/14/7 for 2019-2026, none in 2022), first commit 2019-06-11, contributors 5 with and without anonymous. DOE CODE code-26241 refetched from the OSTI API: title as stated, 2018-12-21, DOI 10.11578/dc.20200909.3, ORNL research org, USDOE sponsor.
- No corrections. The older GitLab.com home listed on DOE CODE wasn't followed, which fits rule 16 and the no-profiling limit.
