# TESViS (MODIS/VIIRS subsetting services)
- Official page: https://modis.ornl.gov/
- Repo: none found [UNKNOWN]. This is a hosted service, not a published codebase.
- Docs: https://modis.ornl.gov/documentation.html, REST docs at https://modis.ornl.gov/data/modis_webservice.html, OpenAPI UI at https://modis.ornl.gov/rst/ui/
- License: [UNKNOWN]. There's no code license. The service asks users to cite it as ORNL DAAC 2018, https://doi.org/10.3334/ORNLDAAC/1600 [KNOWN: web service page].
- Status: active, the live site responds [KNOWN: accessed 2026-10-24]

## What it is (plain English, 2-4 sentences)
TESViS, the Terrestrial Ecology Subsetting & Visualization Services, lets researchers grab just a small square of satellite data around a spot they care about, like a field station, instead of downloading huge global files [KNOWN: modis.ornl.gov]. It's run by the ORNL DAAC with NASA's Land Processes DAAC [KNOWN: modis.ornl.gov]. The stated goal is to help people validate models and satellite products and to characterize field sites [KNOWN: documentation page].

## How it works (plain English, no jargon without definition)
- Products offered include MODIS and VIIRS land products (from instruments on NASA/NOAA satellites), Daymet, SMAP (soil moisture), ECOSTRESS (plant temperature and water stress), GEDI (forest structure from lidar), solar-induced fluorescence (a glow plants give off during photosynthesis) and ICESat-2 [KNOWN: documentation page lists these product families; plain-English glosses are general background, INFERRED].
- There are three ways to use it. The Global Subsets tool lets you request any land location, the Fixed Sites tool has pre-made subsets for known research sites, and there's a REST web service [KNOWN: homepage].
- REST API means you request data with plain web URLs. The pattern is `https://modis.ornl.gov/rst/api/v1/...`, with endpoints to list products (`/products`), list bands (`/{product}/bands`), list available dates, fetch a subset (limited to ten dates per request), or order a bigger subset that's emailed to you when it's ready. Responses come as CSV or JSON [KNOWN: web service page].
- Because it's plain HTTP, you can call it from curl, R or Python and plug the data straight into analysis code [KNOWN: web service page].

## How the project is organized (repo structure, languages, build, maintainers/org unit, release cadence)
- No public source repo found, so the languages and structure are [UNKNOWN].
- Operator: ORNL DAAC in partnership with LP DAAC [KNOWN: homepage]. The ORNL division isn't stated on the pages read [UNKNOWN]. Daymet's page places the DAAC's science in the Environmental Sciences Division, which hints at the same home [INFERRED].
- API version v1 [KNOWN]. The tool citation is dated 2018 [KNOWN]. Release history: [UNKNOWN].

## Who uses it / why it matters
- Field ecologists, and modelers checking their models against satellite data at specific sites [KNOWN: documentation page goal statement].
- For a cyber or dev student, it's a clean real-world public REST API you can practice on with no login [KNOWN: GET https://modis.ornl.gov/rst/api/v1/products returned HTTP 200 with no key, tested 2026-10-24; the order endpoint asks for an email].

## Related projects
- It serves Daymet subsets [KNOWN: documentation page].
- It serves GEDI subsets, related to gedi-tutorials [KNOWN: documentation page lists GEDI; repo relation INFERRED].
- It overlaps with LP DAAC's AppEEARS tool, which the homepage points to as an alternative [KNOWN: homepage].

## Known / Inferred / Unknown
- [KNOWN] Purpose, partners, product families, three access modes, REST endpoints and limits, and the citation DOI.
- [INFERRED] Owning division.
- [UNKNOWN] Source code, license, tech stack and launch date.

## Sources (URL, accessed date)
- https://modis.ornl.gov/, accessed 2026-10-24
- https://modis.ornl.gov/documentation.html, accessed 2026-10-24
- https://modis.ornl.gov/data/modis_webservice.html, accessed 2026-10-24

## Fact-check notes (ORNL Fact Checker, 2026-10-24)
- Corrected: no-key access retagged KNOWN after a direct unauthenticated GET of /products returned 200.
- Verified: homepage names TESViS, the LP DAAC partnership, Global Subsets, Fixed Sites, the web service and AppEEARS; documentation page lists VIIRS, SMAP, ECOSTRESS, GEDI, SIF and ICESat-2 plus the validation and site-characterization goal; web service page has the ten-dates limit, CSV/JSON, email order, curl/R/Python examples and DOI 10.3334/ORNLDAAC/1600.
- Source code and tech stack stay [UNKNOWN].
