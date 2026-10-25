# Roof Savings Calculator Suite

> DRAFT, `draft-osti-only` (2026-10-24, editorial decision). The only public source is an OSTI record, with no docs page. Kept as a draft, not counted as a full brief.
- Official page: https://www.osti.gov/biblio/1238771 (OSTI software record, 2013-11-22). Public web front end named in the record: www.roofcalc.com
- Repo: none found [KNOWN: catalog note]
- Docs: the OSTI abstract. roofcalc.com was unreachable on 2026-10-24 (one fetch returned a 404 "Site Not Configured" page). [KNOWN for that fetch]
- License: [UNKNOWN]
- Status: [UNKNOWN] (the record dates from 2013)

## Plain-language walkthrough
- What it is: a web calculator for how much energy a cool or better-insulated roof saves.
- Problem: roof savings depend on the attic's heat flow, which is hard to measure directly.
- In: building type, location, age, size, equipment, roof and attic settings, and utility prices (defaults are national averages).
- What happens: it simulates a base building and a comparison building with AtticSim plus DOE-2.1E.
- Out: estimated energy and cost savings.
- Humans: homeowners, contractors or roofers pick the inputs and compare results.
- Not: a measurement, and there's no public code.
- Unknown: whether any live version exists today.
- Example: comparing a dark roof with a white roof on a house in Phoenix.

## What it is
A calculator that estimates how much energy and money a building could save by changing its roof. Examples are a "cool roof" (a light, reflective surface that stays cooler in the sun), more attic insulation, or a radiant barrier. [KNOWN: OSTI 1238771 lists these inputs; INFERRED: the cool roof definition] It compares a base-case building against a modified one. [KNOWN: OSTI 1238771]

## How it works
- **Inputs:** it starts from national averages, and you can change them: residential or commercial, location, building age, floor area, floors, window-to-wall ratio, heating and cooling equipment and efficiency, duct location, insulation level, above-sheathing ventilation, radiant barrier, roof thermal mass, roof solar reflectance (how much sunlight bounces off) and thermal emittance (how well the roof sheds heat), roof pitch, and utility prices. [KNOWN: OSTI 1238771]
- **Engine:** it joins AtticSim (an attic heat-flow model) with DOE-2.1E, an older whole-building energy simulation program, and wraps them as a website and web service. [KNOWN: OSTI 1238771; INFERRED: the AtticSim description from its name]

## How the project is organized
- [UNKNOWN]: no public code. ORNL is the research org, and the sponsor is DOE EERE's Building Technologies Office. [KNOWN: OSTI 1238771]

## Who uses it / why it matters
Homeowners, roofers and building managers deciding whether a reflective roof pays off where they live. A cool roof helps a lot in hot climates and can raise heating bills in cold ones, so the location input matters. [INFERRED: general building-science reasoning]

## Related projects
- EnergyPlus (`energyplus`): the DOE engine that replaced DOE-2 for whole-building simulation. [INFERRED: general history, uncited]
- AutoBEM (`autobem`): ORNL building-energy modeling at much bigger scale. [INFERRED: same domain]

## Known / Inferred / Unknown
- KNOWN: purpose, input list, AtticSim plus DOE-2.1E engine, sponsor, ORNL record.
- INFERRED: definitions, the EnergyPlus succession.
- UNKNOWN: license, code, current status.
- Discovery update 2026-10-24: roofcalc.com returned a 404 "Site Not Configured" page on one fetch [KNOWN for that fetch]. OSTI 1651267 (2019, ORNL) says RSC is a web app first developed in 2010 [KNOWN: the fact-check pass read the OSTI 1651267 abstract]. There's no newer software record.

## Sources (accessed 2026-10-24)
- https://www.osti.gov/biblio/1238771

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Sweeps 1 and 2 done. OSTI 1238771 refetched: 2013-11-22, BTO sponsor, 4 authors, AtticSim + DOE-2.1E.
- Corrected: "attic ventilation" is now "above-sheathing ventilation", which is the input the record names.
- Reworded the roofcalc line to "unreachable on 2026-10-24", per editorial decision.
- OSTI 1651267 verified (2019-12-01, ORNL, USDOE): "a web-based application first developed in 2010" covering "over 200 U.S. locations".
- Added the rule 12 walkthrough.
