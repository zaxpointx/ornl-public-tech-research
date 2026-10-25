# Daymet
- Official page: https://daymet.ornl.gov/
- Repo: https://github.com/ornldaac/daymet-single-pixel-batch. This holds helper scripts for downloading data, not the Daymet algorithm itself [KNOWN: repo README]. The code that generates the data isn't public as far as we found [UNKNOWN].
- Docs: https://daymet.ornl.gov/overview
- License: the helper-script repo uses a custom UT-Battelle permissive license [KNOWN: Scout's check of https://raw.githubusercontent.com/ornldaac/daymet-single-pixel-batch/master/LICENSE.md]. The data's use and citation terms are not covered here [UNKNOWN].
- Status: active. The product is updated through the most recent full calendar year [KNOWN: daymet.ornl.gov]. The helper repo's last push was 2025-03-29 [KNOWN: GitHub API].

## What it is (plain English, 2-4 sentences)
Daymet is a dataset of daily weather estimates for every 1 km × 1 km square of land in continental North America and Hawaii from 1980 onward, and Puerto Rico from 1950 [KNOWN: daymet.ornl.gov]. Weather stations are scattered, so most places have no direct measurements. Daymet fills those gaps by estimating values from nearby stations [KNOWN: overview page]. The site describes it as a research product of ORNL's Environmental Sciences Division, distributed by the ORNL DAAC [KNOWN: daymet.ornl.gov]. The DAAC is a NASA data archive hosted at ORNL.

## How it works (plain English, no jargon without definition)
- Inputs are daily max and min temperature and precipitation from ground stations, mainly the GHCN-Daily network run by NOAA's NCEI. It also uses a digital elevation model (a height map of the land) and a land/water mask [KNOWN: overview page].
- For each grid square, it picks nearby stations within a search radius sized to capture an average number of stations. It weights each station by how close it is in space and time, then interpolates (estimates between stations) or extrapolates (estimates beyond them) [KNOWN: overview page describes the V4 approach].
- Temperature and precipitation go through separate workflows. Other variables, namely shortwave radiation (sunlight energy), water vapor pressure (humidity) and snow water equivalent (how much water is stored in snowpack), are derived from those using physics and empirical relationships. Day length is calculated from location and date [KNOWN: overview page, citing Thornton et al. 2020].
- The continent is processed in 2° × 2° tiles. Outputs are converted to netCDF, a common self-describing format for gridded science data, following the CF (Climate and Forecast) metadata conventions [KNOWN: overview page].
- Data can be downloaded as whole files, as a single location's time series through the Single Pixel Extraction Tool, or through REST web services [KNOWN: homepage].

## How the project is organized (repo structure, languages, build, maintainers/org unit, release cadence)
- The public repo is just download helpers in `bash/`, `java/` and `python/`, each reading a text file of coordinates, optional variables and optional years [KNOWN: repo tree and README]. It's about 52% Java, 26% Python and 22% shell [KNOWN: GitHub languages API]. There are about 6 contributors, counting anonymous ones [KNOWN: contributors API].
- Data versions: V3 was released 2016-07-14 and V4 on 2020-12-15 [KNOWN: daymet.ornl.gov]. The yearly data extends through the most recent full year [KNOWN].
- Org unit: Environmental Sciences Division, ORNL [KNOWN: daymet.ornl.gov].
- Funding: NASA (ESDIS and the Terrestrial Ecology Program), plus DOE Office of Science, Biological and Environmental Research [KNOWN: daymet.ornl.gov].

## Who uses it / why it matters
- It drives ecosystem and land models. The site says it supplies driver data for biogeochemical terrestrial modeling [KNOWN: homepage]. It's also used in agriculture, natural-resource and biodiversity research [KNOWN: homepage].
- It may be an input to ORNL's land-modeling work such as E3SM's land model [INFERRED: same ESD and climate ecosystem and the "driver data" framing; not confirmed].

## Related projects
- TESViS (modis.ornl.gov) offers Daymet subsets alongside satellite products [KNOWN: TESViS documentation page lists "Daymet Subset Products"].
- GEDI Tutorials is from the same ORNL DAAC GitHub org [KNOWN: catalog].
- Possibly e3sm-elm [INFERRED].

## Known / Inferred / Unknown
- [KNOWN] Coverage, 1 km daily resolution, the seven variables, the inputs, the method outline, ESD ownership, funders, V4 date, and the access methods.
- [INFERRED] Use as E3SM/ELM forcing data.
- [UNKNOWN] Whether the generator code is public, and the license terms for the data itself.

## Sources (URL, accessed date)
- https://daymet.ornl.gov/, accessed 2026-10-24
- https://daymet.ornl.gov/overview, accessed 2026-10-24
- https://github.com/ornldaac/daymet-single-pixel-batch (README, tree) and https://api.github.com/repos/ornldaac/daymet-single-pixel-batch, accessed 2026-10-24
- https://modis.ornl.gov/documentation.html, accessed 2026-10-24

## Fact-check notes (ORNL Fact Checker, 2026-10-24)
- Re-checked against daymet.ornl.gov and /overview: coverage (1980 on for North America and Hawaii, 1950 on for Puerto Rico), ESD ownership, NASA and DOE BER funding, V3 (2016-07-14) and V4 (2020-12-15) dates, GHCN-Daily/NCEI inputs, 2° tiles and netCDF/CF outputs all match. Verified.
- Helper repo: LICENSE.md is UT-Battelle all-rights-reserved style custom text, languages Java 52.3 / Python 25.7 / Shell 22.0, 6 contributor pages. Verified.
- modis.ornl.gov/documentation.html does list Daymet Subset Products. Verified.
- Whether the Daymet generator code is public stays [UNKNOWN]; no OSTI software record found for it. No changes made.
