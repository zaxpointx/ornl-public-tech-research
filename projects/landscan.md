# LandScan
- Official page: https://landscan.ornl.gov/ (viewer and downloads)
- Repo: none. It's a dataset, not software. [KNOWN: catalog note; no code link on the site]
- Docs: About, Metadata, Citations and Licensing pages on https://landscan.ornl.gov/ (single-page app; text read from the site's own bundled page content)
- License / terms of use: Creative Commons Attribution 4.0 International (CC BY 4.0). The licensing page says anyone may use, copy, share and adapt the data, including commercially, as long as the source is clearly credited. [KNOWN: https://landscan.ornl.gov/licensing]
- Status: active [KNOWN: LandScan Global 2026 released 2026-07-01, OSTI 17076155, DOI 10.48690/LSG/0EXD-MK45]


## Plain-language walkthrough
- **What it is:** ORNL's population maps, which estimate how many people are in each grid cell worldwide. [KNOWN: https://landscan.ornl.gov/]
- **The problem:** census counts come in big areas, at one point in time, and record where people sleep. Responders need to know where people actually are.
- **What goes in:** census totals plus clues such as land cover, roads, buildings and, for 2026, displaced-population data, all fed to machine-learning models. [KNOWN: About text, OSTI 17076155]
- **What happens:** about 100 model predictions per country are averaged and matched to official totals. [KNOWN: OSTI 17076155]
- **What comes out:** raster grids (30 arc-second for Global, down to about 100 m for others), free to download under CC BY 4.0. [KNOWN]
- **Where humans act:** analysts pick the inputs and check the results. Users must credit LandScan.
- **What it is not:** it isn't a head count, and it isn't open code.
- **What's unknown:** owning division, model code.
- **Example:** an aid group downloads LandScan Global 2026 to estimate how many people live inside a flood zone. [INFERRED: matches the stated disaster-response use]

## What it is
LandScan is ORNL's set of maps showing how many people are likely to be in each small square of land on Earth. The finest products go down to about 100 m squares. [KNOWN: https://landscan.ornl.gov/] The homepage lists disaster response, humanitarian aid, environmental analysis and urban planning as uses, and says it won an R&D 100 award. [KNOWN: https://landscan.ornl.gov/]

## How it works
- **Ambient population:** LandScan Global estimates where people are likely to be on average over a 24-hour day, not just where they sleep, which is what census counts record. [KNOWN: site About text; OSTI 17076155]
- **Raster grid:** the data is a raster, meaning a grid of cells, each with a number. Global cells are 30 arc-seconds, which is roughly 1 km at the equator. [KNOWN: OSTI 17076155 for 30 arc-seconds; INFERRED: the km conversion] Cells use latitude/longitude (WGS84) coordinates and aren't projected. The FAQ advises against converting cells to vector polygons. [KNOWN: site FAQ text]
- **Method:** it started in 2000 with "dasymetric mapping", which spreads official population counts onto the land using clues like roads, land cover and buildings. It now uses an ensemble of machine-learning models. For 2026, each country's estimate averages about 100 model predictions, checked against administrative population totals. [KNOWN: site About text; OSTI 17076155]
- **Products:** LandScan Global (updated every year since 2000), LandScan USA (finer resolution, with separate day and night maps), LandScan HD (high resolution, per country, started 2014, built from buildings detected in satellite imagery), plus Mosaic, Global Mosaic and Mosaic Time Series. [KNOWN: product list and About text on the site] HD and USA are now legacy datasets. They're no longer updated, and Global and Mosaic replace them. [KNOWN: landscan.ornl.gov Historical Datasets section, checked by the fact-check pass] LandScan USA covers the lower 48 states, Alaska and the territories, and its 2016 rework added day/night population. [KNOWN: per the discovery-pass read of the public LandScan pages, batches/discovery-notes/batch-05.md] The exact cell sizes for HD and USA are [UNKNOWN]; the site only says "down to 100 meter" overall. The day and night maps help emergency planning, because a downtown can be packed at noon and nearly empty at midnight. [KNOWN: the site cites emergency preparedness; INFERRED: the example]

## How the project is organized
- Delivery: a web map viewer (built on Leaflet, a JavaScript map library) and a free download form that asks for email, work sector and user type. [KNOWN: site page code] Not every dataset is in the viewer, but all can be downloaded. [KNOWN: https://landscan.ornl.gov/]
- Records: OSTI dataset records list ORNL as research org and DOE as sponsor. [KNOWN: OSTI 17076155]
- Owning division: [UNKNOWN]. The site doesn't name one.
- Release cadence: yearly for Global. [KNOWN: site About text]

## Who uses it / why it matters
It's widely cited for disaster response and humanitarian planning. [KNOWN: homepage uses] The 2026 release adds inputs on internally displaced people and refugees. [KNOWN: OSTI 17076155] Because it's CC BY 4.0, students can use it freely with credit, which makes it one of the easiest ORNL datasets to try. [KNOWN: license; INFERRED: the student angle]

## Related projects
- Gauntlet and USA Structures (`gauntlet`): building-footprint work in the same geospatial area. The About text says LandScan USA's framework led to building-level population modeling. [KNOWN: About text; INFERRED: a shared team or data with Gauntlet is unconfirmed]
- Daymet and TESViS (`daymet`, `tesvis-modis`): other ORNL gridded earth datasets. [INFERRED: same broad domain]

## Known / Inferred / Unknown
- KNOWN: CC BY 4.0, 100 m to 30 arc-second resolution, ambient population, ML ensemble, product family, yearly releases, 2026 record.
- INFERRED: km conversion, day/night example.
- UNKNOWN: owning division, any code behind the models (not public), and the HD and USA cell sizes.
- INFERRED: that USA's day and night layers use the same meaning as Mosaic's (day is work and school, night is home).

## Sources (accessed 2026-10-24)
- https://landscan.ornl.gov/ (home, plus About, Metadata, FAQ and Licensing text from the site's page bundle)
- https://landscan.ornl.gov/licensing
- https://www.osti.gov/biblio/17076155 (LandScan Global 2026)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Sweeps 1 and 2 done. landscan.ornl.gov/licensing returns 403 to direct fetches, so I checked the text in the site's public page bundle (landscan.ornl.gov/assets/index-*.js) instead.
- License verified: "These datasets are offered under the Creative Commons Attribution 4.0 International License." (landscan.ornl.gov, Licensing page)
- HD/USA legacy status is now cited to a primary page instead of the discovery notes file: "LandScan HD and LandScan USA are legacy datasets that are no longer actively updated" (landscan.ornl.gov, Historical Datasets section). KNOWN.
- R&D 100 verified: the site calls itself an "R&D100-winning population data platform developed at Oak Ridge National Laboratory". The award year is still UNKNOWN.
- LandScan Global 2026 is verified against OSTI 17076155 (Dataset, 2026-07-01, DOI 10.48690/LSG/0EXD-MK45): "an average of 100 model predictions is considered" and "30 arc-second resolution". The 2000 first release and the shift from dasymetric mapping to machine learning are both on the site's LandScan Global section.
- No download form was submitted.
