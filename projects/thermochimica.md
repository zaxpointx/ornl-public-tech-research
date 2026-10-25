# Thermochimica
- Official page: none separate from the repo [KNOWN: GitHub API homepage empty]
- Repo: https://github.com/ORNL-CEES/thermochimica
- Docs: README, `doc/` folder, and a Doxygen config for generated code docs [KNOWN: repo tree]
- License: BSD 3-Clause, copyright 2017 UT-Battelle, LLC [KNOWN: LICENSE file, https://github.com/ORNL-CEES/thermochimica/blob/master/LICENSE]
- Status: active, last push 2026-07-23 [KNOWN: GitHub API]

## What it is (plain English, 2-4 sentences)
Thermochimica is a code library for chemical thermodynamics. Give it a mix of elements, a temperature and a pressure, and it works out which phases form (solid, liquid, gas, or different crystal types) and what each one is made of [KNOWN: README]. It's like asking "if I heat this alloy or fuel to 1500 °C, what will it actually turn into?" Other simulation programs use those answers to predict material behavior [KNOWN: README says the results feed into modeling of materials and processes].

## How it works (plain English, no jargon without definition)
- It finds the "equilibrium" state, the combination of phases where the system's Gibbs energy is lowest. Gibbs energy is the quantity nature tends to minimize at constant temperature and pressure [KNOWN: an INL report describes Thermochimica as a Gibbs energy minimizer, https://www.osti.gov/biblio/3374533, accessed 2026-10-24; Gibbs energy definition is general background].
- It reads thermodynamic databases (`.dat` files in `data/`, like AlMg or CsI) that describe how each phase's energy depends on composition and temperature [KNOWN: data folder contents; interpretation INFERRED].
- There are three ways to run it. You can write Fortran "driver" programs for full control, use simple text input scripts that can loop over ranges of temperature or pressure, or use Python GUIs [KNOWN: README].
- Results can be written as JSON so other tools can read them [KNOWN: README].

## How the project is organized (repo structure, languages, build, maintainers/org unit, release cadence)
- Languages: about 83% Fortran and 14% Python (for the GUIs), plus some C/C++ [KNOWN: GitHub languages API]. Fortran is an old but very fast language still common in science.
- `src/` holds the solver, split into `api`, `parser` (reads databases), `setup`, `gem` (the core minimizer), `ctz`, `postprocess`, `reinit`, `reset`, `debug`, `exec` and `module`. `test/` has driver programs and daily tests. `inputs/`, `outputs/`, `python/` (GUIs), `scripts/`, `doc/` and `data/` round it out [KNOWN: repo tree].
- Build: Makefile (`make test`) plus CMake files. Needs gfortran and LAPACK/BLAS, which are standard linear-algebra libraries [KNOWN: README].
- CI: the README build badge points to civet.inl.gov, a testing server at Idaho National Laboratory [KNOWN: README badge URL]. Thermochimica is integrated into INL's MOOSE multiphysics framework, including for molten salt reactor (MSR) modeling [KNOWN: https://www.osti.gov/biblio/3374533, INL 2025].
- Contributors: about 20 per the GitHub API, counting anonymous ones [KNOWN: contributors pagination, accessed 2026-10-24].
- Releases: no GitHub releases or tags. It's distributed straight from the main branch [KNOWN: releases and tags API return empty]. The repo was created 2017-09-28 [KNOWN].
- Org unit: it lives in the ORNL-CEES GitHub org, which describes itself as the Computational Engineering and Energy Sciences Group at ORNL [KNOWN: https://github.com/ORNL-CEES, accessed 2026-10-24]. Which division that group sits in is [UNKNOWN].

## Who uses it / why it matters
- Nuclear fuel and reactor-materials modeling, where you need to know what chemical compounds form inside hot fuel, for example from fission products like cesium and iodine [KNOWN: nuclear materials/MSR use per https://www.osti.gov/biblio/3374533; fission-product examples INFERRED from CsI and CsTe databases in data/].
- Also general alloy and materials processing work [INFERRED: AlMg, FeMnCaS databases].

## Related projects
- Coupled with INL's MOOSE framework [KNOWN: OSTI 3374533]. Bison specifically is [UNKNOWN].
- Same nuclear/materials domain as Xolotl (fusion materials) [INFERRED: domain only].

## Known / Inferred / Unknown
- [KNOWN] BSD-3, Fortran plus Python GUIs, three ways to run it, JSON output, no tagged releases, CI hosted at INL.
- [KNOWN] Gibbs-minimization method, nuclear materials use, MOOSE integration, CEES = Computational Engineering and Energy Sciences Group.
- [UNKNOWN] The owning division, and the published papers, which weren't pulled this pass.

## Sources (URL, accessed date)
- https://github.com/ORNL-CEES/thermochimica (README, LICENSE, repo tree), accessed 2026-10-24
- https://api.github.com/repos/ORNL-CEES/thermochimica (+ /languages, /releases, /tags, /contributors), accessed 2026-10-24

## Fact-check notes (ORNL Fact Checker, 2026-10-24)
- Retagged INFERRED -> KNOWN via INL report OSTI 3374533: Gibbs energy minimizer, MOOSE integration, nuclear (MSR) materials use.
- Corrected: CEES was UNKNOWN; GitHub org page says Computational Engineering and Energy Sciences Group at ORNL.
- Corrected: src/ list was missing debug, exec, module.
- Verified: BSD-3 (2017 UT-Battelle), three run methods, JSON output, gfortran + LAPACK/BLAS, civet.inl.gov CI badge, no releases or tags, ~83% Fortran/14% Python, ~20 contributors.
- Unverifiable: owning division.
- No restricted content or implied ORNL affiliation found.
