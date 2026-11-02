# Thermochimica
- Official page: none separate from the repo [KNOWN: GitHub API homepage empty]
- Repo: https://github.com/ORNL-CEES/thermochimica
- Docs: README, `doc/` folder, and a Doxygen config for generated code docs [KNOWN: repo tree]
- License: BSD 3-Clause, copyright 2017 UT-Battelle, LLC [KNOWN: LICENSE file, https://github.com/ORNL-CEES/thermochimica/blob/master/LICENSE]
- Status: active, last push 2026-10-27 [KNOWN: GitHub API, accessed 2026-10-29] (corrected in a fact-check pass, 2026-10-29)
- ORNL relationship: KNOWN (repo in ORNL-CEES org, which names itself an ORNL group; LICENSE copyright UT-Battelle, ORNL's operator) [KNOWN: https://github.com/ORNL-CEES ; LICENSE]
- Years visible in public sources: 2014 (OSTI reports on the THERMOCHIMICA module in MOOSE/BISON, records 1157131 and 1163165) (corrected in a fact-check pass, 2026-10-29) to 2026 (last push) [KNOWN: signals/thermochimica.md; GitHub API]
- Last checked: 2026-10-29 (template upgrade; facts carried over from the 2026-10-24/28/29 passes)

## Walkthrough (plain language)
- **What it is:** a free, open-source Fortran library that predicts what a hot mix of chemicals settles into. [KNOWN: README]
- **The problem:** engineers designing reactor fuel or alloys need to know which compounds and phases (solid, liquid, gas, crystal types) form at a given temperature and pressure. Measuring every case is slow and sometimes dangerous. [INFERRED from the README's stated purpose and OSTI 3374533's nuclear use]
- **What goes in:** the amounts of each element, a temperature, a pressure, and a thermodynamic database file (`.dat`, in the ChemSage format) describing each phase's energy. [KNOWN: README; data/ folder]
- **What happens:** the solver searches for the mix of phases with the lowest Gibbs energy (the "energy budget" nature minimizes at fixed temperature and pressure). That lowest-energy state is called equilibrium. [KNOWN: https://www.osti.gov/biblio/3374533]
- **What comes out:** which phases exist, how much of each, what each is made of, plus totals like Gibbs energy, entropy, enthalpy and heat capacity; optionally as JSON. [KNOWN: README; tested run, see below]
- **Where humans act:** a person picks or obtains the database, writes the input script or Fortran driver, and judges whether the answer makes physical sense. [INFERRED]
- **What it is not:** not a full reactor simulator, not a database itself (big data sets like the Molten Salt Database are separate and login-gated), and not packaged on PyPI, conda-forge or Spack. [KNOWN: signals/thermochimica.md registry checks; https://msd.ornl.gov/access-instructions/] It does not model how fast reactions happen (kinetics). [INFERRED: equilibrium-only method]
- **What's unknown:** the owning ORNL division; why TestThermo90 failed in our build; whether it builds cleanly on Apple Silicon hardware.
- **Example:** carbon plus oxygen at 900-1000 K: the shipped example (after a path fix) reported mostly CO2 and CO gas with some graphite left over. [KNOWN: tested, 2026-10-28]

## What it is (plain English, 2-4 sentences)
Thermochimica is a code library for chemical thermodynamics. Give it a mix of elements, a temperature and a pressure, and it works out which phases form (solid, liquid, gas, or different crystal types) and what each one is made of [KNOWN: README]. It's like asking "if I heat this alloy or fuel to 1500 °C, what will it actually turn into?" Other simulation programs use those answers to predict material behavior [KNOWN: README says the results feed into modeling of materials and processes].

## How it works (plain English, no jargon without definition)
1. **Input:** choose a database from `data/` (or your own) plus element amounts, temperature and pressure, via a Fortran driver, a `.ti` text input script (can loop over temperature/pressure ranges), or the Python GUIs. [KNOWN: README]
2. **Parse:** the `parser` code reads the database's energy models. [KNOWN: src/parser in repo tree; role INFERRED from the name and README]
3. **Solve:** the `gem` (Gibbs energy minimization) core finds the lowest-energy phase mix. [KNOWN: repo tree; https://www.osti.gov/biblio/3374533]
4. **Output:** results printed and optionally written as JSON for other tools. [KNOWN: README]
5. **Human check:** the user reads the result and compares with known phase diagrams. [INFERRED]

Details carried from the earlier brief:
- It finds the "equilibrium" state, the combination of phases where the system's Gibbs energy is lowest. Gibbs energy is the quantity nature tends to minimize at constant temperature and pressure [KNOWN: an INL report describes Thermochimica as a Gibbs energy minimizer, https://www.osti.gov/biblio/3374533, accessed 2026-10-24; Gibbs energy definition is general background].
- It reads thermodynamic databases (`.dat` files in `data/`, like AlMg or CsI) that describe how each phase's energy depends on composition and temperature [KNOWN: data folder contents; interpretation INFERRED].
- There are three ways to run it. You can write Fortran "driver" programs for full control, use simple text input scripts that can loop over ranges of temperature or pressure, or use Python GUIs [KNOWN: README].
- Results can be written as JSON so other tools can read them [KNOWN: README].

## How the project is organized
- Languages: about 83% Fortran and 14% Python (for the GUIs), plus some C/C++ [KNOWN: GitHub languages API]. Fortran is an old but very fast language still common in science.
- `src/` holds the solver, split into `api`, `parser` (reads databases), `setup`, `gem` (the core minimizer), `ctz`, `postprocess`, `reinit`, `reset`, `debug`, `exec` and `module`. `test/` has driver programs and daily tests. `inputs/`, `outputs/`, `python/` (GUIs), `scripts/`, `doc/` and `data/` round it out [KNOWN: repo tree].
- Build: Makefile (`make test`) plus CMake files. Needs gfortran and LAPACK/BLAS, which are standard linear-algebra libraries [KNOWN: README].
- CI: the README build badge points to civet.inl.gov, a testing server at Idaho National Laboratory [KNOWN: README badge URL]. Thermochimica is integrated into INL's MOOSE multiphysics framework, including for molten salt reactor (MSR) modeling [KNOWN: https://www.osti.gov/biblio/3374533, INL 2025].
- Contributors: about 20 per the GitHub API, counting anonymous ones [KNOWN: contributors pagination, accessed 2026-10-24].
- Releases: no GitHub releases or tags. It's distributed straight from the main branch [KNOWN: releases and tags API return empty]. The repo was created 2017-09-28 [KNOWN].
- Org unit: it lives in the ORNL-CEES GitHub org, which describes itself as the Computational Engineering and Energy Sciences Group at ORNL [KNOWN: https://github.com/ORNL-CEES, accessed 2026-10-24]. Which division that group sits in is [UNKNOWN].
- Outside-in history: first commit 2018-01-06, about 2,234 commits on all branches, peak years 2021-2022, then 16-46 a year; 5-8 active authors every year; one author has 74% of commits. [KNOWN: signals/thermochimica.md, git log] Read as a mature library kept up by a small group. [INFERRED, medium]
- Note on CI: the signals pass found no CI workflow files in the repo; the README's badge points to INL's civet server, so testing runs outside GitHub. These agree. [KNOWN: signals; README] [INFERRED reconciliation]
- Why Fortran, why no releases: [UNKNOWN] (no source states the reason, RULES 19).

## Running it on a Mac
Who this is for: someone on a Mac mini M4 who wants to try it. Our tests ran on the team's Linux box, not a Mac. Mac-only steps come from the README and Makefile. Jargon: *gfortran* is the free Fortran compiler; *LAPACK/BLAS* are standard math libraries for matrices; *Homebrew* is a Mac package installer.
Tested on the team's Linux box, not a Mac. Mac-only steps come from the README and Makefile. [KNOWN: tested; README; Makefile]
1. **Tools:** install Xcode Command Line Tools (`xcode-select --install`), then `brew install make gcc`. Homebrew's gcc provides gfortran. [KNOWN: README "MacOS" section]
2. **Math libraries:** nothing extra is needed on a Mac. The Makefile's Darwin branch links Apple's built-in Accelerate framework (`-framework Accelerate`) for LAPACK/BLAS. On Linux it links `-llapack -lblas`. [KNOWN: Makefile lines 31-41]
3. **Build:** `make test`, then `./run_tests`. [KNOWN: README] Build serially. A parallel `make -j8` failed for us because Fortran module files weren't ready in time. [KNOWN: tested] The C/C++ wrappers need `g++` too. [KNOWN: Makefile CC = g++; tested]
4. **Our test result (local Linux test build, 2026-10-28; not a Mac, not re-run since):** 73 test programs built. Running every test binary one at a time gave 63 passes and 5 fails; the other 5 binaries aren't accounted for in the notes [UNKNOWN]. [KNOWN: dated local run] (corrected in a fact-check pass, 2026-10-29) `./run_tests` stops at the first failure because it uses `set -e`, so it hides the later results. [KNOWN: run_tests script]
   - TestMSTDB01-04 fail because their data file (`LiBeUPuThF_T1.dat`) isn't in the public `data/` folder. [KNOWN: test/daily source; data listing]
   - TestThermo90 failed even though its data file (`CsI-Pham.dat`) is present. The cause is [UNKNOWN] (we used conda-forge gfortran 16.2).
5. **Run a calculation:** `./bin/InputScriptMode inputs/<file>.ti`. The shipped examples `advanced-input.ti` and `json.ti` point at `data/C-O.dat`, but the repo file is `data/CO.dat`, so they fail with "data-file was not found" until you fix that path. [KNOWN: tested; data listing] With the fix, carbon plus oxygen at 900-1000 K printed the equilibrium gas mix (mostly CO2 and CO, with some graphite left over) plus Gibbs energy, entropy, enthalpy and heat capacity. [KNOWN: tested]
6. **JSON output** landed in `outputs/thermochimica_out.json`, not `thermoout.json` as the README says. [KNOWN: tested; README]
7. **GUIs:** `pip install -r python/requirements.txt` installed cleanly in a Python 3.12 venv. We didn't open the windows (no display test). [KNOWN: tested] On a Mac, the GUI needs a Python build with Tk. [INFERRED]
8. **M4 Mac mini outlook:** a realistic, small build. The only heavy dependency is gfortran. Apple Silicon support for Homebrew gcc is [INFERRED], not tested on hardware.

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2015 | OSTI report on coupling THERMOCHIMICA with MOOSE/BISON (ORNL research org) | https://www.osti.gov/api/v1/records/1214026 | [KNOWN] |
| 2017 | LICENSE copyright UT-Battelle 2017; GitHub repo created 2017-09-28 | LICENSE; GitHub API | [KNOWN] |
| 2017 | OSTI record 1507873 (coupling work) | https://www.osti.gov/api/v1/records/1507873 | [KNOWN] |
| 2018-01-06 | First commit in git history | signals/thermochimica.md | [KNOWN] |
| 2020 | "Acceleration of Thermochimica Calculations in Bison" report | https://www.osti.gov/api/v1/records/1615992 | [KNOWN] |
| 2021 | CALPHAD paper on molten salt developments (doi 10.1016/j.calphad.2021.102341); commit peak (837) | signals/thermochimica.md | [KNOWN] |
| 2025 | INL report: accelerating thermochemistry solves in MOOSE and Pronghorn | https://www.osti.gov/biblio/3374533 | [KNOWN] |
| 2026-10-27 | Last push per GitHub API | GitHub API, accessed 2026-10-29 | [KNOWN] |

## Who uses it / why it matters
- Nuclear fuel and reactor-materials modeling, where you need to know what chemical compounds form inside hot fuel, for example from fission products like cesium and iodine [KNOWN: nuclear materials/MSR use per https://www.osti.gov/biblio/3374533; fission-product examples INFERRED from CsI and CsTe databases in data/].
- Also general alloy and materials processing work [INFERRED: AlMg, FeMnCaS databases].
- Outside reach: 69 stars, 36 forks; the 2021 molten-salt paper has 21 citing works, 2 with an ORNL author; not in any package registry. [KNOWN: signals/thermochimica.md, accessed 2026-10-24]
- Funding: 6 of 7 OSTI hits list DOE's Office of Nuclear Energy, one the NRC. [KNOWN: signals/thermochimica.md, OSTI sponsor fields]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| INL MOOSE (outside project) | uses (Thermochimica is a MOOSE contrib submodule); map link 52 | MOOSE .gitmodules ; OSTI 3374533 | [CORROBORATED] |
| INL Pronghorn (outside project) | uses (thermochemistry solves accelerated in MOOSE and Pronghorn); map link 211 | https://www.osti.gov/api/v1/records/3374533 | [KNOWN] |
| INL BISON (outside project) | extends (ORNL-led coupling reports into BISON; OSTI research org ORNL); map link 212 | https://www.osti.gov/api/v1/records/1214026 ; https://www.osti.gov/api/v1/records/1615992 | [KNOWN] |
| Molten Salt Database (account required) | shares data (example inputs name an MSTDB file not in the repo); map link 213 | verification/not-found.md ; https://mstdb.ornl.gov/about/ | [INFERRED] |
| [Xolotl](xolotl.md) | related topic (nuclear materials); map link 21 | both repos | [INFERRED] |
| AM cluster (Myna, AdditiveFOAM, 3DThesis, Finch, ExaCA, adamantine) | none found; map links 191, 214 | greps of the six repos | [UNRELATED] |

## What stands out
- It's a small, long-lived open library that bigger INL and ORNL nuclear codes lean on, and it's the most realistic code in this repo for a student to build on a home Mac.
- The free code is open but the most valuable salt data is behind a login, which is exactly why four tests fail publicly.
- Small documentation drifts (C-O.dat vs CO.dat, JSON filename) suggest docs lag the code. [INFERRED]

## Ten questions (GOAL.md)
1. **Problem/for whom:** predicts equilibrium chemistry for nuclear fuel, molten salt and materials modelers. [KNOWN: README; OSTI 3374533]
2. **Where in the tree:** ORNL-CEES (Computational Engineering and Energy Sciences Group); division [UNKNOWN].
3. **Who pays:** mostly DOE Office of Nuclear Energy, one NRC record. [KNOWN: OSTI sponsor fields via signals]
4. **Code:** about 83% Fortran, 14% Python GUIs; Makefile + CMake; gfortran + LAPACK/BLAS. [KNOWN: GitHub API; README]
5. **Alive:** yes, last push 2026-10-27, low but steady commits, no tags or releases. [KNOWN]
6. **Outside users:** INL's MOOSE (submodule) and Pronghorn; 21 citing works for the 2021 paper. [KNOWN/CORROBORATED, see Related projects]
7. **Connections:** upstream: databases incl. the Molten Salt Database; downstream: MOOSE, Pronghorn, BISON. [see Related projects]
8. **What it teaches:** ORNL-written tools often live inside other labs' frameworks, and data access is controlled separately from code. [INFERRED]
9. **Student path:** yes: install Homebrew gcc, `make test`, run the C-O example; know basic command line and a little chemistry first. [KNOWN steps; INFERRED prerequisites]
10. **Unknown:** owning division, TestThermo90 cause, Apple Silicon behavior; papers beyond signals not pulled. Not-found searches: verification/not-found.md.

## Known / Inferred / Unknown
- [KNOWN] BSD-3, Fortran plus Python GUIs, three ways to run it, JSON output, no tagged releases. [INFERRED] CI hosted at INL, from the README badge pointing at civet.inl.gov (corrected in a fact-check pass, 2026-10-29).
- [KNOWN] Gibbs-minimization method, nuclear materials use, MOOSE integration, CEES = Computational Engineering and Energy Sciences Group.
- [UNKNOWN] The owning division, and the published papers, which weren't pulled this pass.
- [KNOWN] Mac build steps from README/Makefile; a dated Linux test build (2026-10-28) gave 63 pass / 5 fail of 73 built, not run on a Mac (corrected in a fact-check pass, 2026-10-29).
- [INFERRED] TestMSTDB failures come from a file in the login-gated Molten Salt Database (map link 213).
- [UNKNOWN] TestThermo90 failure cause; Apple Silicon build on real hardware.

## Verification notes
### Fact-check notes (2026-10-24)
- Retagged INFERRED -> KNOWN via INL report OSTI 3374533: Gibbs energy minimizer, MOOSE integration, nuclear (MSR) materials use.
- Corrected: CEES was UNKNOWN; GitHub org page says Computational Engineering and Energy Sciences Group at ORNL.
- Corrected: src/ list was missing debug, exec, module.
- Verified: BSD-3 (2017 UT-Battelle), three run methods, JSON output, gfortran + LAPACK/BLAS, civet.inl.gov CI badge, no releases or tags, ~83% Fortran/14% Python, ~20 contributors.
- Unverifiable: owning division.
- No restricted content or implied ORNL affiliation found.

### Fact-check notes (2026-10-29)
- Re-checked: BSD-3-Clause, created 2017-09-28, empty homepage, no tags (GitHub API). Last push date updated. OSTI 3374533 resolves. Contributor count (about 20) not re-checked: API rate limit.

### Template upgrade (2026-10-29, reading pass)
- Restructured into templates/project-brief.md. No facts dropped. Related projects table copied verbatim. Test results (Linux test build) not re-run (the local clone is at a 2026-05-28 commit, older than upstream). Needs one fact-check pass.

## Sources (URL, title, accessed date, what it supports)
- https://github.com/ORNL-CEES/thermochimica (README, LICENSE, repo tree), accessed 2026-10-24
- https://api.github.com/repos/ORNL-CEES/thermochimica (+ /languages, /releases, /tags, /contributors), accessed 2026-10-24
- https://www.osti.gov/biblio/3374533 (INL report, 2025), accessed 2026-10-24: Gibbs minimizer, MOOSE/Pronghorn, MSR use
- https://www.osti.gov/api/v1/records/1214026 ; https://www.osti.gov/api/v1/records/1615992 ; https://www.osti.gov/api/v1/records/1507873: BISON coupling reports
- https://github.com/ORNL-CEES: CEES group name, accessed 2026-10-24
- https://mstdb.ornl.gov/about/ ; https://msd.ornl.gov/access-instructions/: salt data format and access gate
- signals/thermochimica.md: git history, registries, citations, funding
- Local tests: a fresh clone built with conda-forge gfortran 16.2 on a Linux test machine, 2026-10-28

## Quality gate
- [x] Every load-bearing claim has a source and a tag
- [x] Facts are kept apart from interpretation
- [x] ORNL relationship is not overstated, and maturity verbs match the source (RULES item 10)
- [x] Walkthrough, flow, timeline and unknowns are present
- [x] Ten questions answered or marked UNKNOWN
- [x] No copied text beyond short cited quotes; people by role only
- [ ] Two fact-check sweeps done (RULES item 11)
- [ ] INDEX, catalog, LAB-TREE and connections map updated

## Fact-check notes (2026-10-29), template rewrite
- Full check of the rewritten brief against a fresh clone (2,237 commits on all branches, 2,014 on the default branch; first commit 2018-01-06 and last 2026-10-27, author and committer dates the same; 837 commits in 2021 on both date types, matching signals), the GitHub languages API (Fortran about 83%, Python about 14%), the MOOSE `.gitmodules` (Thermochimica is a submodule under `modules/chemical_reactions/contrib`), the README civet badge, and the OSTI API.
- Verified: last push 2026-10-27; no tags or releases; `.github/` holds only issue templates, so "no CI workflow files" is right, and the civet badge reconciliation is honestly tagged INFERRED; `LiBeUPuThF_T1.dat` isn't in `data/` (28 files) while TestMSTDB01-02 reference it; `data/CO.dat` exists and no `C-O.dat` does; the CEES org description.
- Corrected: earliest public year is 2014, not 2015; the 63/5 test numbers are now labelled as a dated local Linux run, not a Mac result and not re-verified, with 5 of 73 binaries unaccounted for; "CI hosted at INL" moved from KNOWN to INFERRED in the summary.
- The related-projects table matches map links 52 and 211-214, including the corrected BISON row. The local filesystem path on the Local tests line is already gone. No restricted, copied or affiliation issues found.
