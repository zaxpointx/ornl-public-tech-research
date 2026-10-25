# EnergyPlus
- Official page: https://energyplus.net/
- Repo: https://github.com/NatLabRockies/EnergyPlus
- Docs: https://energyplus.net/ (developer wiki: https://github.com/NatLabRockies/EnergyPlus/wiki)
- License: custom BSD-3-style with a US Government rights notice. The copyright holders are the University of Illinois, the University of California through LBNL, ORNL (managed by UT-Battelle), Alliance for Energy Innovation, LLC, "and other contributors". [KNOWN: https://github.com/NatLabRockies/EnergyPlus/blob/develop/LICENSE.txt]
- Status: active [KNOWN: v26.2.0 released 2026-09-30, last push 2026-10-24, GitHub API]


## Plain-language walkthrough
- **What it is:** an open-source program for simulating a whole building's energy and water use, with a public website maintained by DOE. [KNOWN: README "whole building energy simulation program" and "The Department of Energy maintains a public website for EnergyPlus"; OSTI 1395245] Calling it DOE's main or flagship tool is [INFERRED]; neither source says that.
- **The problem:** designers and researchers need to know how much heating, cooling, lighting and power a building will use before they build or retrofit it.
- **What goes in:** a text model of the building (geometry, walls, windows, HVAC, schedules, defined by the `idd` data dictionary) and a weather file. [KNOWN: repo `idd/` and `weather/` folders; INFERRED: the input roles]
- **What happens:** it simulates heat flow and equipment behavior, timestep by timestep, across the year. [INFERRED: standard description]
- **What comes out:** energy use, loads and comfort reports. [INFERRED]
- **Where humans act:** modelers build the input, often through other tools, and read the reports.
- **What it is not:** an ORNL-only project. ORNL is one of several named copyright holders [KNOWN: LICENSE.txt]. Who leads development is [INFERRED]: the repo sits in the National Laboratory of the Rockies GitHub org.
- **What's unknown:** ORNL's specific role.
- **Example:** comparing the yearly cooling energy of an office with and without better windows in a Tennessee climate file. [INFERRED: an illustrative use]

## What it is
EnergyPlus simulates how much energy and water a building uses (heating, cooling, ventilation, lighting, plug loads and processes) over time, usually hour by hour across a whole year of weather. [KNOWN: repo description and OSTI 1395245; INFERRED: the time-step detail] Architects and engineers use it to compare designs before construction. For example: what happens to the power bill if we add insulation or switch to a heat pump? [INFERRED] DOE maintains the public website. [KNOWN: README]

## How it works
- **Input:** a text model of the building (geometry, walls, windows, HVAC equipment, schedules) in IDF format. IDF is defined by a data dictionary, the IDD. [KNOWN: the `idd/` folder and `IDF_Editor` and `IDFVersionUpdater` tools in `src/`; INFERRED: format roles from the names] HVAC means heating, ventilation and air conditioning.
- **Weather:** you supply a weather file for the site. [KNOWN: `weather/` folder; INFERRED: its role]
- **Engine:** the core simulation (`src/EnergyPlus`) does heat-balance physics, adding up the heat flowing in and out of every zone at each step, and models the HVAC equipment. [INFERRED: standard description of how it's built, verify against the engineering reference in `doc/`]
- **Helper programs:** `src/` also holds `Basement` and `Slab` (ground heat transfer), `ExpandObjects` (expands template inputs), `ReadVars` and `ConvertESOMTR` (output processing), `EP-Launch` (a launcher), `HVAC-Diagram` and `EPDraw`. [KNOWN: repo `src/` listing; INFERRED: roles from the names]

## How the project is organized
- Top level: `src/`, `tst/` (tests), `testfiles/`, `datasets/`, `weather/`, `idd/`, `doc/`, `design/` (feature design documents), `third_party/`, `cmake/`, `scripts/` and `release/`. [KNOWN: GitHub contents API]
- Languages: C++ 86.3%, Fortran 8.6%, plus Jupyter, Python and a bit of Visual Basic 6.0. [KNOWN: GitHub languages API] The Fortran is probably left over from the original code, which was mostly translated to C++. [INFERRED]
- Build: CMake. [KNOWN: CMakeLists.txt]
- Releases: twice a year, usually March and September. Pre-release candidates come first, such as v26.2.0-RC1 to RC3 (2026-09-21 to 2026-09-29) before v26.2.0. [KNOWN: README; GitHub releases API]
- Testing: unit, integration, API and regression tests on every commit, through Decent CI and GitHub Actions. [KNOWN: README]
- Scale: about 144 contributors, about 1,600 stars, created 2013-11-22. [KNOWN: GitHub API]
- Lead institution: the repo is under the NatLabRockies GitHub org, whose profile name is National Laboratory of the Rockies (nlr.gov) [KNOWN: https://api.github.com/orgs/NatLabRockies]. That NLR is the renamed NREL and leads development is [INFERRED: Scout's note and Alliance for Energy Innovation, LLC in the copyright line; nlr.gov's homepage doesn't say "formerly NREL"]. ORNL is a named copyright holder, and the OSTI software record for EnergyPlus lists ORNL as research org. [KNOWN: LICENSE.txt; OSTI 1395245] ORNL's specific role (which modules, which group) is [UNKNOWN].

## Who uses it / why it matters
It's widely described as DOE's flagship building-energy engine [INFERRED: no fetched source says "flagship"]. Many users and developers are active on the Unmet Hours Q&A forum. [KNOWN: README] Buildings use a large share of US energy, so better design tools mean real savings. [INFERRED: general fact, no number cited]

## Related projects
- The ORNL buildings research projects in this catalog, such as `gauntlet` (building footprints). [INFERRED: same domain; a footprint-to-energy-model link is unconfirmed]

## Known / Inferred / Unknown
- KNOWN: purpose, license holders including ORNL, layout, languages, release cadence, testing, OSTI record naming ORNL.
- INFERRED: NREL as lead, the Fortran's origin, helper roles.
- UNKNOWN: ORNL's specific contribution, the governance model.

## Sources (accessed 2026-10-24)
- https://github.com/NatLabRockies/EnergyPlus (README.md, LICENSE.txt)
- https://api.github.com/repos/NatLabRockies/EnergyPlus (plus /languages, /releases, /contributors, /contents)
- https://www.osti.gov/biblio/1395245
- https://energyplus.net/

## Fact-check notes (ORNL Fact Checker, 2026-10-24)
- Corrected: the GitHub org's own name is National Laboratory of the Rockies. NREL as its former name is INFERRED.
- Verified: LICENSE.txt holders (Illinois, UC/LBNL, ORNL/UT-Battelle, Alliance for Energy Innovation, others) and the Government rights notice; v26.2.0 on 2026-09-30 with RC1 to RC3 (2026-09-21 to 09-29); twice-yearly March/September; unit, integration, API and regression tests via Decent CI; Unmet Hours; DOE website; C++ 86.3 / Fortran 8.6; 144 contributor pages; 1,607 stars; created 2013-11-22; OSTI 1395245 is a Software record with ORNL as research org.
- ORNL's specific role stays [UNKNOWN].

## Sweep 2 notes (ORNL Fact Checker, 2026-10-24)
- Corrected: "DOE's main open-source program" was tagged KNOWN, but neither the README nor OSTI 1395245 says "main" or "flagship". Retagged INFERRED and kept the sourced wording.
- Corrected: "not an ORNL-led project [KNOWN: LICENSE]" overstated what the license shows. A co-holder list proves ORNL is one of several holders, not who leads. Reworded to "not ORNL-only" (KNOWN) with lead INFERRED.
- Disconfirming check: OSTI 1395245 (Software, dated 2012-01-01) lists ORNL as the only research org. That does not support NREL-led, so map link 61 should not cite it for that.
- Load-bearing quotes: README line 7: "EnergyPlus is a whole building energy simulation program that engineers, architects, and researchers use to model both energy consumption and water use in buildings." Cadence, README line 33: "released twice annually, usually in March and September." CORROBORATED: the purpose wording appears in both the README and OSTI 1395245.
- Re-fetched the GitHub API (created 2013-11-22, last push 2026-10-24, v26.2.0 on 2026-09-30, 144 contributor pages, 1,607 stars; GitHub license field reads NOASSERTION because the license is custom). Walkthrough present.
