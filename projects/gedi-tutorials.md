# GEDI Science Data Tutorials
- Official page: https://ornldaac.github.io/gedi_tutorials/ (GitHub API homepage) [KNOWN]
- Repo: https://github.com/ornldaac/gedi_tutorials [KNOWN]
- License: a UT-Battelle open source license (`LICENSE.md`; the copyright year is blank). GitHub shows NOASSERTION. [KNOWN: LICENSE.md, GitHub API]
- Status: active. v2.0.0 was released 2024-09-04, and the last commit was 2026-10-23. [KNOWN: CHANGELOG.md, git log]
- Scope (rule 13): `ornldaac` is a side org. The license names UT-Battelle, LLC (the company that runs ORNL for DOE) as copyright holder, and the README says the data products are "archived at the ORNL DAAC". [KNOWN: LICENSE.md, README] That passes rule 13 on the copyright line. No OSTI record turned up. [KNOWN: catalog note]

## Plain-language walkthrough
- **What it is:** a set of Jupyter notebooks and a few Python scripts that teach you how to find, download, slice and use NASA GEDI forest data. It's published as a small online book. [KNOWN: README, `myst.yml`]
- **Key terms:**
  - **GEDI:** NASA's Global Ecosystem Dynamics Investigation, a laser instrument on the International Space Station that measures forest height and structure. [KNOWN: ornl.gov DAAC 30-year news story]
  - **DAAC:** a NASA Distributed Active Archive Center. ORNL DAAC is NASA's center at Oak Ridge for land ecology and biogeochemistry data, and it's one of 12 in NASA's Earth data system. [KNOWN: NASA Earthdata ORNL DAAC page; ornl.gov news]
  - **Footprint:** one laser shot's patch of ground, roughly a small circle. "Gridded" products average footprints into map cells. [KNOWN: `docs/datasets.md` "Footprint" vs "Gridded"; INFERRED: the plain definition]
  - **AGBD:** aboveground biomass density, roughly how much plant material per hectare. It's what GEDI L4 products estimate. [KNOWN: README notebook titles]
  - **HDF5 / COG:** two file formats. HDF5 is a container for big science arrays, and a COG (cloud-optimized GeoTIFF) is a map image you can read in pieces over the web. [KNOWN: `docs/datasets.md` footnote]
- **The problem:** GEDI data is huge and complex (levels L1B through L4D, footprints and grids, quality flags, version fixes), and new users need working examples. [KNOWN: dataset table; INFERRED: the need]
- **What goes in:** an area of interest as a GeoJSON polygon, plus the user's NASA Earthdata access. [KNOWN: script descriptions; INFERRED: that login is needed for downloads, which we didn't try]
- **What happens:** the notebooks show several ways to get data: search and download, subset to your area, direct cloud (S3) access, the OPeNDAP and Harmony subsetting services, and OGC map services. Then they explore variables and quality flags. [KNOWN: README list]
- **What comes out:** subsets and maps of biomass for your area, plus worked fixes when NASA revises a model, for example applying the revised R003 model to Version 3 L4A granules over South America. [KNOWN: README]
- **Where humans act:** a scientist or student runs each notebook step by step. DAAC staff update the notebooks when products change. The latest commit, from 2026-10-23, fixes negative biomass predictions. [KNOWN: git log subject; INFERRED: who]
- **What it is not:** it isn't the GEDI data itself or NASA's processing code. It's teaching material. [KNOWN: README]
- **What's unknown:** the Zenodo DOI. `citation.md` still shows a placeholder `zenodo.xxx`. [KNOWN: citation.md]
- **Example:** draw a polygon around a national park, run `gedi_l4a_search_download.py` and then `gedi_l4a_subsets.py`, and you get the biomass footprints inside it. [KNOWN: scripts README; INFERRED: the walk-through]

## How it works
- About ten L4A notebooks, one L4B notebook using OGC WMS and WCS map services, a cloud notebook that combines GEDI with ICESat-2 and field data, plus `full_orbits/`, `polygons/` and `subsets/` helper folders. [KNOWN: README, `notebooks/`]
- Three standalone scripts mirror the notebooks for batch use. [KNOWN: `scripts/`]
- `docs/` lists datasets (with NASA and ORNL DAAC DOIs), data services, prerequisites and resources. [KNOWN]

## How the project is organized
- Languages: Jupyter notebooks (Python), one R Markdown file, and Python scripts. The book is built with MyST and Jupyter Book, with a PDF export target. [KNOWN: tree, `myst.yml`, `requirements.txt`]
- Environment: a conda `environment.yml` (named `cms`), with Python 3.5 or newer plus pip requirements. [KNOWN] The env name might point to NASA's Carbon Monitoring System program. [INFERRED, low; not checked]
- History: 91 commits from 2021-08-26 to 2026-10-23. Per year: 2021: 18, 2022: 37, 2023: 21, 2024: 3, 2025: 5, 2026: 7. [KNOWN: git log] Tags are v1.0.0 (2023-03-23) and v2.0.0 (2024-09-04). [KNOWN: CHANGELOG, git tags]
- Contributors: 4 including anonymous authors, 3 accounts, and 6 distinct git author emails. [KNOWN: GitHub API, git log]
- 134 stars and 52 forks, the most stars of anything in this batch. [KNOWN: GitHub API, 2026-10-24]
- Org unit: ORNL DAAC. [KNOWN: README] ORNL's Earth System Informatics and Data Discovery section hosts the DAAC. [KNOWN: ornl.gov section page via search result; the direct fetch returned 403, so treat as unconfirmed]

## Who uses it / why it matters
- People learning GEDI, such as ecologists, remote-sensing students and carbon researchers. The star and fork counts suggest wide use for a tutorial repo. [KNOWN: counts; INFERRED: who]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship (uses, extends, shares data, same facility, related topic, unknown) | Source | Tag |
|---|---|---|---|
| Daymet | same facility (ORNL DAAC) | map link 44; https://github.com/ornldaac | KNOWN |
| TESViS MODIS subsets | shares data (serves GEDI subsets; no direct reference between the two) | map link 73; projects/tesvis-modis.md | INFERRED |

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2021-08-26 | First commit | git log | KNOWN |
| 2022 | Busiest year, 37 commits | git log | KNOWN |
| 2023-03-23 | v1.0.0 tag | CHANGELOG, git tags | KNOWN |
| 2024-09-04 | v2.0.0 tag | CHANGELOG, git tags | KNOWN |
| 2026-10-23 | Latest commit seen | git log | KNOWN |

## What stands out
- It's the most-starred project in this batch, and it isn't software at all. It's teaching material, which says a lot about what outsiders actually want from a data center. [KNOWN: counts; INFERRED]
- The Zenodo DOI is still a placeholder after two major versions, so the citation plumbing never got finished. [KNOWN: citation.md; INFERRED]

## Known / Inferred / Unknown
- [KNOWN] contents, formats, data services shown, history, license, DAAC role.
- [INFERRED] who uses it, and what the `cms` env name means.
- [UNKNOWN] the Zenodo DOI, and a funding line for the tutorials specifically.

## Verification notes
_Filled by the fact-check pass._

## Sources (accessed 2026-10-24)
- https://github.com/ornldaac/gedi_tutorials (README.md, LICENSE.md, CHANGELOG.md, citation.md, myst.yml, environment.yml, requirements.txt, docs/datasets.md)
- https://api.github.com/repos/ornldaac/gedi_tutorials (and /contributors)
- https://www.earthdata.nasa.gov/centers/ornl-daac (NASA page: the DAAC's mission, founded 1993, DOE as partner, archives data funded by NASA's Terrestrial Ecology program)
- https://www.ornl.gov/news/ornl-daac-marks-30-years-stewarding-nasa-terrestrial-ecology-data (GEDI was the DAAC's first orbital data product; one of 12 DAACs)

## GOAL.md questions (added 2026-10-24)
- **Problem and for whom (Q1):** getting new users productive with NASA GEDI biomass data. [INFERRED]
- **Where in the tree (Q2):** ORNL, then environmental and earth science, then ORNL DAAC (a NASA data center run at ORNL). [KNOWN: NASA Earthdata page]
- **Who pays (Q3):** the DAAC itself is NASA's. The NASA page calls it "NASA's Oak Ridge National Laboratory Distributed Active Archive Center". [KNOWN] No funding line for the tutorials specifically. [UNKNOWN] This makes it one of the few non-DOE-funded threads in the catalog. [INFERRED]
- **Organized how (Q4):** notebooks plus scripts, built into a MyST book. [KNOWN]
- **Alive? (Q5):** yes, but in maintenance mode: busy in 2021-23, then small updates whenever NASA revises products. [KNOWN: per-year counts; INFERRED: the pattern]
- **Outside users (Q6):** 134 stars and 52 forks. Citing works weren't checked, and the DOI is a placeholder. [KNOWN; UNKNOWN]
- **Connections (Q7):** upstream are NASA GEDI products and NASA cloud services (S3, OPeNDAP, Harmony, OGC). Neighbors are Daymet and TESViS at the same DAAC. [KNOWN]
- **What it teaches about ORNL (Q8):** ORNL also works for other agencies. Here it runs a NASA data center, and the teaching material is part of that job: the NASA page lists building "tools, and training" as a goal. [KNOWN: NASA Earthdata page; INFERRED: the lesson]
- **Student angle (Q9):** a good first data-science project. It's free data, Python notebooks and real cloud data-access patterns like S3 and APIs. You'd need a free NASA Earthdata account, which the team didn't create. [INFERRED] There's no CONTRIBUTING file. [KNOWN: tree]
- **Searched without result (Q10):** OSTI "GEDI" (no relevant record); Zenodo DOI (placeholder only).

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Verified: v2.0.0 2024-09-04 (CHANGELOG), last commit 2026-10-23, 134 stars and 52 forks, NOASSERTION license, the README's ORNL DAAC line, and the NASA Earthdata page's wording for the DAAC. No corrections.
