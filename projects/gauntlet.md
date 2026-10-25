# Gauntlet (Geographic Augmentation of Extracted Building Features Tool)
- Official page: https://www.osti.gov/doecode/biblio/157761 (DOI 10.11578/dc.20250709.1)
- Repo: https://github.com/ORNL/gauntlet
- Docs: README only
- License: MIT, copyright 2025 Oak Ridge National Laboratory [KNOWN: https://github.com/ORNL/gauntlet/blob/main/LICENSE]
- Status: active but quiet [KNOWN: created 2025-07-09, last push 2025-07-18, GitHub API]


## Plain-language walkthrough
- **What it is:** a small ORNL Python script that measures building footprints. [KNOWN: repo `src/gauntlet.py`]
- **The problem:** a footprint polygon alone doesn't tell a model much. Shape and neighborhood measures help classify buildings, for example homes versus warehouses.
- **What goes in:** building footprint polygons (geospatial files read with geopandas). [KNOWN: code]
- **What happens:** it computes 65 features: shape measures, plus statistics within 50, 100, 250, 500 and 1000 m and a nearest-neighbor index. [KNOWN: README and code]
- **What comes out:** a table of features per building. [KNOWN]
- **Where humans act:** researchers feed the features into models like Vivaldi.
- **What it is not:** it doesn't detect buildings from imagery. It needs footprints already. [INFERRED: the code only reads polygons]
- **What's unknown:** who maintains it after the 2025 release.
- **Example:** footprints from the USA Structures dataset go in, and a feature table for Vivaldi's data comes out. [KNOWN: vivaldi README "built off the Gauntlet process"; INFERRED: that USA Structures is the specific input]

## What it is
Gauntlet takes building footprints (the outline of each building on a map, stored as a polygon) and calculates 65 numbers describing each building's shape and surroundings. [KNOWN: README, DOE CODE] Those numbers feed classification and modeling. For example, a big plain rectangle surrounded by other big rectangles is probably a warehouse, while a small complex shape in a dense cluster is probably a house. [KNOWN: DOE CODE says "classification tasks and modeling the built environment"; INFERRED: the example]

## How it works
- **Shape measures** of the building itself: area, perimeter, vertex count, bounding-box area, and ratios like the isoperimetric quotient, which scores how close a shape is to a circle (the most area for a given perimeter). [KNOWN: README feature table]
- **Neighborhood measures:** inside 50, 100, 250, 500 and 1000 meter buffers it counts nearby buildings, gets their size statistics (mean, standard deviation, min, max, coefficient of variation), and computes a nearest-neighbor index, a standard statistic that says whether buildings are clustered, random or evenly spread. [KNOWN: README feature table; INFERRED: the nearest-neighbor index explanation is the general GIS meaning]
- **Mechanics:** one Python script (`src/gauntlet.py`, about 315 lines) built on geopandas (pandas for map data), scipy and tqdm (progress bars). It splits the dataset across parallel worker processes. You configure it by editing a few lines in the script (input path, output CSV, ID field, core count, task size). [KNOWN: README; line count from the repo]

## How the project is organized
- Tiny repo: `src/gauntlet.py`, `requirements.txt`, `Dockerfile`, `docker-compose.yml`, `CITATION.cff`, README and LICENSE. [KNOWN: repo tree]
- Language: Python 98%, plus a Dockerfile. Python 3.10.15 is recommended. [KNOWN: GitHub languages API, README]
- Releases: none. [KNOWN: GitHub releases API returned none]
- Contributors: about 2. [KNOWN: GitHub contributors API]
- Maintainer: the README and CITATION.cff list one ORNL author as point of contact. [KNOWN] Name withheld here because it's a staff contact and we don't contact staff. The DOE CODE record also lists it publicly.
- Sponsors: FEMA and DOE's Federal Energy Management Program. [KNOWN: OSTI DOE CODE 157761]

## Who uses it / why it matters
FEMA sponsorship suggests disaster and emergency use, such as estimating which buildings are homes and which are businesses when planning a response to a hurricane. [INFERRED: from the sponsor] The README's example input is a statewide Alabama structures dataset, so it's built for millions of buildings. [KNOWN: the `AL_structures.gdb` example path; INFERRED: the scale] ORNL's Vivaldi tool builds on Gauntlet's morphology features; its README says its data comes from the Gauntlet process. [KNOWN: https://github.com/ORNL/vivaldi/blob/main/README.md]

## Related projects
- USA Structures (ORNL's national building-footprint database): Gauntlet features were computed for it and published as a dataset. [KNOWN: Scientific Data paper "Building morphologies of the USA structures database; a gauntlet feature set", DOI 10.1038/s41597-025-05925-6, OSTI 3001779; dataset DOI 10.6084/m9.figshare.28271483, OSTI 2587435]
- Real-Twin (`real-twin`): same buildings/transport domain. [INFERRED]

## Known / Inferred / Unknown
- KNOWN: 65 features, the feature groups, single-script design, MIT license, sponsors, DOI.
- KNOWN (added): Gauntlet features were published for USA Structures (OSTI 3001779).
- INFERRED: disaster-planning use.
- KNOWN (added): Vivaldi uses Gauntlet features (vivaldi README).
- UNKNOWN: downstream users outside ORNL.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL/gauntlet (README, LICENSE, CITATION.cff, src/gauntlet.py)
- https://api.github.com/repos/ORNL/gauntlet
- https://www.osti.gov/doecode/biblio/157761
- https://www.osti.gov/biblio/3001779 (Scientific Data 2025, DOI 10.1038/s41597-025-05925-6)
- https://www.osti.gov/biblio/2587435 (figshare dataset)
- https://github.com/ORNL/vivaldi/blob/main/README.md

## Fact-check notes (2026-10-24)
- Corrected: README feature table also has a 1000 m buffer.
- Verified: MIT 2025 ORNL; created 2025-07-09, last push 2025-07-18; Python 98.2%; no releases; 2 contributor pages; 65 measures; 315-line script; geopandas/scipy/tqdm; Python 3.10.15; AL_structures example; isoperimetric quotient and nearest-neighbor index rows; OSTI code-157761 DOI and FEMA + FEMP sponsors; OSTI 3001779 and 2587435 (ORNL); Vivaldi README naming Gauntlet.
- Staff name correctly withheld.

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Corrected: the walkthrough still listed buffers only to 500 m. The README feature table has 50, 100, 250, 500 and 1000 meter buffer rows, so the walkthrough now matches the body.
- Re-fetched the GitHub API (MIT, created 2025-07-09, last push 2025-07-18, 0 releases), README, OSTI code-157761 and 3001779. No contradictions.
- CORROBORATED: 65 features. README "Purpose: To generate 65 measurements from geospatial polygon data"; OSTI code-157761 "generates 65 measures of a building's morphology"; OSTI 3001779 (Scientific Data, 2025-11-07) "a set of 65 unique features for every building for more than 131 million buildings". The journal paper is an independent publication.
- Sponsors, OSTI code-157761: FEMA and "USDOE Office of Federal Energy Management Programs (FEMP)".
- Staff name still withheld. Walkthrough present.
