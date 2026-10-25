# AutoBEM (Automatic Building Energy Modeling)

- Official page: https://www.osti.gov/doecode/biblio/115947 (DOI 10.11578/dc.20231116.1)
- Repo: none. DOE CODE lists the project type as Closed Source. [KNOWN: DOE CODE 115947]
- Docs: the public Model America v1.0 dataset page, https://doi.ccs.ornl.gov/dataset/9e968129-1ca9-5a71-93fa-24f009132a3a (DOI 10.13139/ORNLNCCS/1774134), plus the public papers in Sources
- License: [UNKNOWN] (closed source)
- Status: unknown (rule 14). ORNL journal papers dated 2026-10 use it (OSTI 3740812, 17315517), so it's likely in use [INFERRED], but there's no software release newer than the 2023 DOE CODE record.

## Plain-language walkthrough
- What it is: software that builds and runs an energy model for every building in an area, up to the whole US.
- Problem: you can't test retrofits on 120+ million real buildings one at a time.
- In: map data on building footprints and heights, plus typical assumptions for each building type and age.
- What happens: it makes an EnergyPlus/OpenStudio model for each building and simulates them on supercomputers.
- Out: energy use, demand, CO2 and cost per building, and how much each upgrade would save.
- Humans: they pick the area, the weather and the upgrades to test, and read the results.
- Not: open source, and not measured data. These are simulations.
- Unknown: code layout, license and current version.
- Example: a 2026 study modeled about 722,000 Phoenix buildings to map where and when building CO2 peaks.

## What it is
AutoBEM automatically builds an energy model for every building in a region, even the whole country, and runs them. Each model estimates a building's energy use, peak demand, emissions and costs, and what upgrades would save. [KNOWN: DOE CODE 115947] DOE CODE calls each model a "digital twin" made from a set of building descriptors. [KNOWN: DOE CODE 115947]

## How it works
- **From map data to model:** it takes building geometry from GIS data (GIS means geographic information system, map-based data), adds assumptions from "prototype" buildings of the same type and age, and generates a physics-based EnergyPlus/OpenStudio model for each individual building. [KNOWN: OSTI 3740812] OpenStudio is a toolkit that makes EnergyPlus models easier to build and run. [INFERRED: general description]
- **Scale through supercomputing:** DOE CODE claims over 1 million buildings per hour. [KNOWN: DOE CODE 115947] The 2026 paper simulated 122.9 million buildings, 97.8% of the US building stock, using high-performance computing and the Model America dataset. [KNOWN: OSTI 3740812]
- **Validation:** DOE CODE says it was checked against 15-minute meter data for 178,000 buildings and several cities. [KNOWN: DOE CODE 115947]
- **Outputs:** the national models are being released openly as the Model America v1.0 (MAv1) dataset, even though the generator code is closed. [KNOWN: OSTI 3740812]

## How the project is organized
- Code: closed source, so layout and languages are [UNKNOWN].
- Developers: DOE CODE lists three ORNL developers. [KNOWN: DOE CODE 115947] Names are left out here because they're staff contacts.
- Sponsor: USDOE. Research org: ORNL. Released 2023-11-15. [KNOWN: DOE CODE 115947]
- Owning division: [UNKNOWN] in the record.

## Who uses it / why it matters
Utilities, cities and policymakers can see building-by-building where retrofits would cut the most energy and CO2. [INFERRED: from the stated outputs] One 2026 study used AutoBEM to map building CO2 emissions across about 722,000 buildings in Phoenix, Arizona, by season and time of day. [KNOWN: OSTI 17315517, DOI 10.1016/j.scs.2026.107930] Another applies the same idea to US data centers at national scale. [KNOWN: OSTI 3384902 title; whether it uses AutoBEM directly is UNKNOWN]

## Related projects
- EnergyPlus (`energyplus`): the simulation engine AutoBEM generates models for. [KNOWN: OSTI 3740812]
- Gauntlet and USA Structures (`gauntlet`): ORNL building-footprint geometry, a likely input. [INFERRED: the papers say "GIS-derived geometry" without naming the source]
- LandScan (`landscan`): another ORNL national-scale geospatial product. [INFERRED: same domain]

## Known / Inferred / Unknown
- KNOWN: closed source, purpose, throughput claim, validation claim, 122.9 million building run, MAv1 dataset, Phoenix study.
- INFERRED: footprint inputs, who benefits.
- UNKNOWN: code, license, division.
- Discovery update 2026-10-24: Model America is publicly downloadable [CORROBORATED: https://doi.ccs.ornl.gov/dataset/9e968129-1ca9-5a71-93fa-24f009132a3a (DOI 10.13139/ORNLNCCS/1774134, via Globus) and https://doi.org/10.15485/2283980 (ESS-DIVE)]. The editorial review counted this dataset page as AutoBEM's public docs page (item 14), so this is a normal brief now.

## Sources (accessed 2026-10-24)
- https://www.osti.gov/doecode/biblio/115947
- https://www.osti.gov/biblio/3740812 (AutoBEM national framework, Sustainable Cities and Society 2026, DOI 10.1016/j.scs.2026.107700)
- https://www.osti.gov/biblio/17315517 (Phoenix CO2 study)
- https://www.osti.gov/biblio/3384902 (data center prototype models)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Sweeps 1 and 2 done.
- Added the plain-language walkthrough required by rule 12.
- Status changed from "active [KNOWN]" to `unknown` to match map.md and rule 14. Papers using AutoBEM aren't a statement that the software is maintained.
- 122.9M buildings and 97.8% are now CORROBORATED. OSTI 3740812 (abstract): "122.9 million buildings, representing 97.8% of the U.S. building stock". The Constellation Model America page: "this dataset contains 122,930,327 (97.8%) buildings" out of 125,714,640 detected.
- New from the Constellation page (released 2021-04-14): the 2021 national run "used resources of the Argonne Leadership Computing Facility", not OLCF. Its sponsors include ORNL LDRD, BTO, OE, BER and NNSA. Model America v1.0 has been public since 2021, so it isn't only "being released" now.
- DOE CODE 115947 verified: 1M buildings/hour, "178,000 buildings", 3 developers, 2023-11-15, sponsor USDOE.
- OSTI 17315517: 722,237 buildings. OSTI 3384902 (data centers) has no abstract, so whether it uses AutoBEM stays UNKNOWN.
