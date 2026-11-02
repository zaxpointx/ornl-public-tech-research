Short brief (RULES 21): built from the partner's product page and an OSTI software record; closed-source program.

# WUFI-ORNL/IBP

- Official page: https://wufi.de/en/service/free-wufi-versions/ (Fraunhofer IBP, the partner; lists "WUFI ORNL (Pro)") [KNOWN: fetched 2026-10-29]
- OSTI: https://www.osti.gov/biblio/1231793 (software record, 2014-05-20, ORNL, USDOE) [KNOWN: OSTI API, accessed 2026-10-29]
- Repo: none; it's a closed-source PC program. The product page says free licenses need a registration on the product page; that registration was not used. [KNOWN: product page] (corrected in a fact-check pass, 2026-10-29)
- License: free for non-commercial use, functionally limited [KNOWN: product page; OSTI]
- Status: unknown

## Walkthrough
WUFI-ORNL predicts how heat and moisture move through a wall over time. [KNOWN: OSTI description] WUFI is German shorthand for "transient heat and moisture". [KNOWN: OSTI title]
The problem: walls get wet from rain, humid air and condensation inside the layers. If they don't dry out, you get mold and rot. Builders need to know whether a wall design will stay dry in their climate. [INFERRED: standard building science background]
What goes in: the wall's layers and materials, plus weather. The ORNL version includes climate data for 62 US and Canadian cities. [KNOWN: product page]
What happens: it calculates one-dimensional heat and moisture transport (straight through the wall, layer by layer) as the weather changes. [KNOWN: OSTI]
What comes out: temperature and moisture over time in each layer. [INFERRED: what transient calculations produce]
Where humans act: an engineer picks the assembly and judges the risk. [INFERRED]
What it is not: not ORNL's own open code. It's a free limited edition of Fraunhofer's commercial WUFI Pro. [KNOWN: product page; OSTI]
Example: compare a brick wall with interior insulation in a humid southern city versus a cold northern one, and see whether moisture builds up behind the insulation each winter. (Illustrative.)
Unknown: exactly what ORNL contributed beyond co-developing the North American version.

## What it is (plain English, 2-4 sentences)
A North American edition of the WUFI building-moisture program, developed by Fraunhofer IBP together with ORNL. It's free for non-commercial use and has fewer features than WUFI Pro. [KNOWN: product page; OSTI 1231793] OSTI says the model was validated against lab and outdoor field measurements. [KNOWN: OSTI]

## How it works (plain English, no jargon without definition)
1. Define the wall layers and materials. [INFERRED: standard WUFI input]
2. Pick one of the 62 city climates. [KNOWN]
3. Simulate coupled heat and moisture flow through time, covering vapor diffusion (water vapor drifting through materials) and liquid transport (water wicking through pores). [KNOWN: OSTI]
4. Review the results. [INFERRED]

## How the project is organized
Closed source, so layout, languages and build are [UNKNOWN]. The program is "menu-driven" for PCs. [KNOWN: OSTI] Release history is UNKNOWN. Two older ORNL WUFI pages redirect or are blocked (stub-search-2026-10-24.md).

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2014-05-20 | OSTI software record 1231793 | https://www.osti.gov/biblio/1231793 | [KNOWN] |
| 2025-10-01 | product page last updated, still offering WUFI ORNL | wufi.de | [KNOWN] |

## Who uses it / why it matters
Building scientists and students in North America, non-commercially. [INFERRED from the license terms] Moisture failure is a common cause of building damage, so free access to a validated tool matters. [INFERRED]

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| WUFI Pro (Fraunhofer IBP) | parent commercial product; map links 89, 225 | https://wufi.de/en/service/free-wufi-versions/ ; OSTI 1231793 | [CORROBORATED] |
| [EnergyPlus](energyplus.md) | related topic (building energy); map link 85 | OSTI 1231793 | [INFERRED] |

## What stands out
This one shows ORNL as a partner on someone else's commercial software rather than the owner, a different relationship from most of the catalog. It still meets RULES 13 because OSTI names ORNL as the research org.

## Ten questions (GOAL.md)
1. Problem and audience: moisture risk in walls, for building designers and researchers. [KNOWN]
2. Place in the tree: ORNL building envelope research, with Fraunhofer. [KNOWN/INFERRED]
3. Who pays: USDOE per OSTI, program UNKNOWN.
4. Code: closed; UNKNOWN.
5. Alive: still offered as of the 2025 page update. [KNOWN]
6. Outside users: UNKNOWN numbers.
7. Connections: a free edition of WUFI Pro. [KNOWN]
8. What it teaches: ORNL co-develops with international institutes. [KNOWN]
9. Student path: register on the Fraunhofer site yourself (registration is required), download it free and model a wall. (corrected in a fact-check pass, 2026-10-29)  No code to contribute to. [KNOWN: free version]
10. Still unknown: ORNL's exact contribution. Searched without result: ORNL WUFI pages (redirect, 403).

## Known / Inferred / Unknown
- KNOWN: what it calculates, the partnership, the free limited license and the 62 cities.
- INFERRED: typical inputs and outputs, and users.
- UNKNOWN: ORNL's role details and versions.

## Verification notes
Filled by the fact-check pass.

## Sources (URL, title, accessed date, what it supports)
- https://wufi.de/en/service/free-wufi-versions/, Fraunhofer IBP free WUFI versions, accessed 2026-10-29, supports the free edition, partnership and 62 cities
- https://www.osti.gov/biblio/1231793, OSTI "WUFI-ORNL/IBP", accessed 2026-10-29, supports the description, validation and date

## Quality gate
- [x] Every load-bearing claim has a source and a tag
- [x] Facts are kept apart from interpretation
- [x] ORNL relationship is not overstated, and maturity verbs match the source
- [x] Walkthrough, flow, timeline and unknowns are present
- [x] Ten questions answered or marked UNKNOWN
- [x] No copied text beyond short cited quotes; people by role only
- [ ] Two fact-check sweeps done
- [ ] INDEX, catalog, LAB-TREE and connections map updated

## Fact-check notes (2026-10-29)
- Re-read the Fraunhofer IBP free versions page (last update 2025-10-01) and OSTI 1231793 (2014-05-20, ORNL, USDOE, software). Verified: joint North American version, functionally limited, free for non-commercial use, 62 US and Canadian cities, menu-driven PC program, one-dimensional transient heat and moisture, and validation against lab and outdoor measurements.
- Corrected: downloads need a registration, which wasn't stated. It's noted but wasn't used (no sign-ups or forms).
- Related-projects table checked against connections/map.md and its sources; rows match. (Map links 69, 84 and 86 got factual updates; see verification/log.md.)

### Second pass (2026-10-29)
- Reread: 62 cities, non-commercial, functionally limited and the registration note match the Fraunhofer page; the OSTI title spells "Wärme and Feuchte", and "transient heat and moisture" is a fair translation. The partner page is a primary source for the edition, not for ORNL's role, which stays UNKNOWN. No issues found.
