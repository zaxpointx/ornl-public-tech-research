Short brief (RULES 21): built from the database's public about and access pages only. The data files are behind an account and a membership request, and nobody on the team signed up.

# Molten Salt Database (MSD, formerly MSTDB)

- Official page: https://mstdb.ornl.gov/about/ [KNOWN: fetched 2026-10-29]
- Access page: https://msd.ornl.gov/access-instructions/ [KNOWN: fetched 2026-10-29]
- Repo: the files sit on ORNL's GitLab server, which needs an account plus MSD membership; not opened (team rule: don't follow code.ornl.gov) [KNOWN: access page]
- License: MSD-TC is copyrighted but available license-free and cannot be sold in whole or in part [KNOWN: about page]
- Status: unknown

## Walkthrough
MSD is a reference book of numbers for molten salt reactors (MSRs, reactors that use melted salt as coolant or even to carry the fuel). [KNOWN: about page]
The problem: to model an MSR you need to know how salt mixtures behave: when they melt, what compounds form, and how dense, thick (viscous) and heat-conducting they are at each temperature. That data is scattered across decades of papers. [INFERRED from the about page's description of what's collected]
What's inside: two parts. [KNOWN: about page]
- MSD-TC (thermochemical): Gibbs energy models (the math that predicts which chemical phases are stable) for chloride and fluoride salt systems, in the ChemSage .dat format. That format works with the commercial FactSage software and the open Thermochimica code.
- MSD-TP (thermophysical): a CSV of density, thermal conductivity, viscosity and heat capacity, with uncertainties and literature references. It also has an API called Saline for other NEAMS codes, and a GUI for browsing.
What happens: a researcher downloads the files and loads them into Thermochimica, FactSage or a NEAMS code. [KNOWN: about page]
What comes out: phase predictions and property values for their salt. [INFERRED]
Where humans act: requesting access, then choosing the salt system and checking results against the included published phase diagrams. [KNOWN: about page mentions companion diagrams for comparison]
What it is not: not freely downloadable without signing up, and not software by itself. [KNOWN: access page]
Example: check the melting point of a lithium-beryllium fluoride mix by loading its MSD-TC file into Thermochimica. (Illustrative.)
Unknown: file contents and versions, because we didn't sign up.

## What it is (plain English, 2-4 sentences)
A pair of public-use databases of molten salt properties for MSR research, hosted by ORNL. The about page says MSD-TC development is supported by DOE Nuclear Energy's MSR Campaign, NEAMS (Nuclear Energy Advanced Modeling and Simulation) and Nuclear Energy University Programs, and calls MSD-TP a product of DOE MSR-related research programs. [KNOWN: about page] (corrected in a fact-check pass, 2026-10-29)

## How it works (plain English, no jargon without definition)
1. Ask for access: the site says you need an account on ORNL's GitLab server and an MSD membership, granted on the closest Tuesday or Thursday after you submit a form. [KNOWN: access page] (The team did not do this.)
2. Download the TC .dat files (separate versions for FactSage up to 8.0 and 8.1 and later) and the TP CSV. [KNOWN: about page]
3. Use them in Thermochimica, FactSage or through the Saline API. [KNOWN]

## How the project is organized
Data files plus docs, source-tracing files and a phase diagram library on a gated server. [KNOWN: about page] Layout, versions and update history are [UNKNOWN] (not opened). The catalog notes the thermophysical part is managed by ORNL and the thermochemical part by the University of South Carolina, per an ORNL report. [KNOWN: catalog row, not re-read here]

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| UNKNOWN | renamed from MSTDB to MSD | site title | [KNOWN] name; date [UNKNOWN] |
| 2026 | ORNL news: new uranium-salt measurements added | catalog row (https://www.ornl.gov/news/new-measurements-advance-molten-salt-reactor-technologies) | [KNOWN], not re-read here |

## Who uses it / why it matters
MSR modelers using Thermochimica, FactSage and NEAMS codes. [KNOWN: about page names the tools] Our Thermochimica test build (on a Linux test machine, not a Mac) hit this: the 4 MSTDB tests failed because their data file isn't in the public Thermochimica repo. That file is most likely part of this gated database. [KNOWN: test failures, thermochimica.md; INFERRED link] Public repo evidence, checked 2026-10-29: the four `test/daily/TestMSTDB0*.F90` tests load `LiBeUPuThF_T1.dat`, which is not in the repo's `data/` folder, and an example input names a file called `MSTDB-TC_V1.3_Fluorides_8-0.dat`. That supports the link but no public page states it, so it stays INFERRED.

## Related projects
Filled by the connections pass, matching connections/map.md.
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| [Thermochimica](thermochimica.md) | shares data (Thermochimica reads MSD files); map link 213 | https://mstdb.ornl.gov/about/ | [KNOWN] |
| [Thermochimica](thermochimica.md) salt tests (Linux test build) | likely missing a gated MSD file; map link 213 | projects/thermochimica.md ; verification/not-found.md | [INFERRED] |
| Molten Salt Reactor Experiment | no public software tie shown; map link 220 | discovery/nuclear-reactor-scan-2026-10-28.md | [UNKNOWN] |

## What stands out
"Public use" and "freely downloadable" aren't the same thing. Anyone can apply, but the data sits behind an identity check, so Cayden would have to sign up himself if he wants it.

## Ten questions (GOAL.md)
1. Problem and audience: salt property data, for MSR modelers. [KNOWN]
2. Place in the tree: nuclear energy, MSR and NEAMS programs. [KNOWN]
3. Who pays: DOE-NE MSR Campaign, NEAMS and NEUP for MSD-TC; DOE MSR-related programs for MSD-TP. [KNOWN] (corrected in a fact-check pass, 2026-10-29)
4. Code: data, plus the Saline API and a GUI. [KNOWN] Details are UNKNOWN.
5. Alive: 2026 news of new data, per the catalog. [KNOWN, not re-read]
6. Outside users: UNKNOWN.
7. Connections: Thermochimica, FactSage and NEAMS codes. [KNOWN]
8. What it teaches: ORNL gates even public-use data behind accounts. [KNOWN]
9. Student path: apply yourself, then use it with Thermochimica. [KNOWN steps]
10. Still unknown: contents and versions. Not searched further, because it needs an account.

## Known / Inferred / Unknown
- KNOWN: the two parts, formats, tools, funding, license terms and the access requirement.
- INFERRED: the Thermochimica test file link.
- UNKNOWN: file contents, versions and users.

## Verification notes
Filled by the fact-check pass.

## Sources (URL, title, accessed date, what it supports)
- https://mstdb.ornl.gov/about/, "About, Molten Salt Database (MSD)", accessed 2026-10-29, supports contents, formats, license and funding
- https://msd.ornl.gov/access-instructions/, "Access Instructions", accessed 2026-10-29, supports the account and membership requirement

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
First-pass fact check against the public about page and access-instructions page (both fetched 2026-10-29) and the public Thermochimica GitHub repo (fresh clone). No account was created, no form was opened or submitted, and no link to the gated server was followed.
- Verified: the two parts (MSD-TC and MSD-TP) and what each holds; ChemSage .dat format for FactSage and Thermochimica; separate chloride and fluoride files; separate files for FactSage 8.0 and below and 8.1 and above; source-tracing files and the phase diagram library; Saline API and GUI; the license-free, cannot-be-sold terms for MSD-TC; the account plus membership requirement; access granted on the nearest Tuesday or Thursday after the form.
- Corrected: the funding line applied the named programs to both databases; the about page names them for MSD-TC only and describes MSD-TP as a product of DOE MSR-related research programs.
- The Thermochimica link stays INFERRED; public repo evidence added above.
- Unverifiable in this pass: the catalog's note on how the two parts are managed and the 2026 news item (not re-read; the brief already says so).
- Nothing restricted or non-public found. The brief contains no gated content.

### Second pass (2026-10-29)
Skeptical reread; first-pass fixes confirmed in place and reading cleanly.
- Access requirement (account plus membership, Tuesday/Thursday grant): the same steps appear on both the about page and the separate access-instructions page; both re-read. Verified.
- License terms (license-free, cannot be sold): re-read; applies to MSD-TC as stated. Verified.
- "formerly MSTDB": the access steps still say "Request MSTDB membership" and the about page sits at the mstdb.ornl.gov address, so the older name is supported. Verified (rename date still UNKNOWN).
- Thermochimica link: the public Thermochimica docs don't mention MSTDB or molten salt; only the tests and one example input do. Still INFERRED. Verified as tagged.
- No corrections in this pass. Nothing restricted; no account, form or gated link touched.
