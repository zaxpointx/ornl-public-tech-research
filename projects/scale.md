# SCALE
- Official page: https://www.ornl.gov/scale
- Repo: none public; not openly distributed. [KNOWN: no public repo listed on https://www.ornl.gov/scale]
- Docs: the public SCALE 6.3 validation reports on OSTI (listed under Sources)
- License: not open source. SCALE is distributed under license; ORNL's public SCALE datasets say reproducing their results requires a SCALE license [KNOWN: OSTI 2572299, 2583965]. The license terms themselves are [UNKNOWN].
- Status: active [KNOWN: SCALE 6.3 validation reports came out 2024-2025, and SCALE benchmark datasets were posted to OSTI in 2026, see Sources]


## Plain-language walkthrough
- **What it is:** a large ORNL software suite for nuclear safety and design calculations. [KNOWN: https://www.ornl.gov/scale]
- **The problem:** engineers have to prove that a reactor core, a fuel storage cask or a shipping package is safe: that it won't start an uncontrolled chain reaction, and that radiation shielding is enough.
- **What goes in:** a text input file describing materials, geometry and the calculation "sequence" to run, plus nuclear data libraries (ENDF/B-VII.1 based). [KNOWN: SCALE manual and ornl.gov/scale; INFERRED: the general input style]
- **What happens:** modules like KENO (Monte Carlo criticality), Polaris (lattice physics) and Shift solve the physics. [KNOWN: OSTI 2575336, 2583839, 3007184]
- **What comes out:** numbers like k-effective (whether a chain reaction sustains itself), dose rates and spent-fuel isotope inventories. [INFERRED: from the four stated areas]
- **Where humans act:** analysts build the models, choose the sequences and judge the results against validation data.
- **What it is not:** it's not open-source software. It's not openly distributed. [KNOWN: ornl.gov/scale]
- **What's unknown:** the license terms.
- **Example:** to check a spent-fuel storage design for criticality safety, an analyst runs a KENO calculation and checks that k-effective stays well below 1. [INFERRED: a typical use within the stated criticality-safety area]

## What it is
SCALE is a big software toolkit for nuclear safety work. It's developed and maintained by ORNL under contract with the Nuclear Regulatory Commission (NRC), DOE and the National Nuclear Security Administration (NNSA). [KNOWN: https://www.ornl.gov/scale] Engineers use it to answer questions like "could this arrangement of nuclear fuel start a chain reaction by accident?" and "how much shielding does this storage cask need?" [INFERRED: plain-language restatement of the four application areas the page lists]

## How it works
The overview page names four jobs: [KNOWN: https://www.ornl.gov/scale]
- **Reactor physics** means predicting how neutrons behave in a reactor core, which sets how much power it makes and how its fuel burns up.
- **Criticality safety** means making sure fuel stored, shipped or processed outside a reactor can never reach "criticality", which is a self-sustaining chain reaction.
- **Radiation shielding** means working out how much radiation gets through walls, casks or containers.
- **Spent fuel characterization** means working out what's inside used fuel (which isotopes, how much heat, how radioactive) after it leaves a reactor.

SCALE is a suite, meaning several modules that each handle one part of the job. Public ORNL reports name some of them. KENO does criticality calculations and has been in use since the 1960s. [KNOWN: OSTI 2575336] Polaris does reactor-physics lattice calculations and is paired with the PARCS core simulator. [KNOWN: OSTI 2583839] Shift is a Monte Carlo transport engine. Monte Carlo means following huge numbers of simulated random neutrons and averaging the results. [CORROBORATED: SCALE 6.3.3 manual, CSAS-Shift section 2.2.1, "Shift is a massively parallel Monte Carlo radiation transport package in the Exnihilo radiation transport code suite" (https://scale-manual.ornl.gov/6.3.3/CSAS-Shift.html); OSTI 1237627 (J. Comput. Phys.) describes Shift the same way] Results depend on nuclear-data libraries, which are tables of how likely each atom is to absorb or scatter neutrons. The 6.3 validation uses ENDF/B-VII.1 libraries. [KNOWN: OSTI 2587031]

"Validation" means comparing the code's predictions against real measurements to show how accurate it is. SCALE 6.3 has a public multi-volume validation set covering reactor physics, criticality safety, spent fuel and shielding. [KNOWN: https://www.ornl.gov/scale; OSTI 2575336, 2587031, 2583839] OSTI calls the spent-fuel report "the fifth volume", while the ORNL page lists four volumes. [KNOWN: OSTI 2587031 vs https://www.ornl.gov/scale] The likely reason is that the series numbering counts a separate overview volume. The previous 6.2.4 series had a "Validation Overview" report (OSTI 1902803) alongside the four topic reports, and its reactor-physics report called itself the third volume (OSTI 1902818). [INFERRED: from the 6.2.4 pattern; no 6.3 overview record found on OSTI]

## How the project is organized
- Source layout, languages and build system: [UNKNOWN]. There's no public code to inspect.
- Owner: ORNL develops and maintains it. [KNOWN: https://www.ornl.gov/scale] The specific ORNL division or group isn't named on the overview page. [UNKNOWN]
- Versions: 6.3 is the version currently being validated, and 6.2.4 was the previous validated release. [KNOWN: OSTI 2587031]
- Parallel computing: an ORNL paper says SCALE added limited support for threads, OpenMP and MPI, and evaluates hybrid approaches for SCALE-Shift. [KNOWN: OSTI 3007184] (OpenMP shares work across the cores of one computer, and MPI splits work across many computers.)

## Who uses it / why it matters
OSTI's description says it's widely used by researchers, industry and regulators for criticality safety, reactor physics, shielding, source terms and inventory analysis. [KNOWN: OSTI 3007184] ORNL has published SCALE models of advanced (non-light-water) reactors for the NRC. [KNOWN: OSTI 2572299, 2583965] It's safety-critical software, so validation against real measurements matters as much as the code itself. [INFERRED]

## Related projects
- VERA (`vera`): also ORNL reactor simulation. Both are tied to the Shift transport code. [INFERRED: Shift appears in both SCALE-Shift (OSTI 3007184) and Scout's VERA component list, needs verification]
- Thermochimica (`thermochimica`): nuclear fuel chemistry, a different layer of the same field. [INFERRED]

## Known / Inferred / Unknown
- KNOWN: four application areas and the NRC/DOE/NNSA sponsors (ornl.gov/scale); 6.3 validation reports; the KENO, Polaris and SCALE-Shift module names (OSTI); not openly distributed.
- CORROBORATED: Shift is a Monte Carlo transport package used through SCALE's CSAS-Shift sequence (SCALE manual + OSTI 1237627).
- INFERRED: the overlap with VERA.
- UNKNOWN: code layout, languages, owning division, license terms, whether a 6.3 overview volume exists (see the volume note above).

## Sources (accessed 2026-10-24)
- https://www.ornl.gov/scale
- https://www.osti.gov/biblio/2575336 (SCALE 6.3 Validation: Nuclear Criticality Safety)
- https://www.osti.gov/biblio/2587031 (SCALE 6.3 Validation: Spent Nuclear Fuel)
- https://www.osti.gov/biblio/2583839 (SCALE 6.3 Validation: Reactor Physics)
- https://www.osti.gov/biblio/3007184 (Parallel programming models in SCALE-Shift)
- https://scale-manual.ornl.gov/6.3.3/CSAS-Shift.html (SCALE 6.3.3 manual, CSAS-Shift)
- https://www.osti.gov/biblio/1237627 (Shift, J. Comput. Phys. 2016)
- https://www.osti.gov/biblio/2572299 and https://www.osti.gov/biblio/2583965 (SCALE Non-LWR Models for NRC)

## Fact-check notes (ORNL Fact Checker, 2026-10-24)
- Verified via WebFetch of https://www.ornl.gov/scale (curl from my computer hit a Cloudflare block): the description, NRC/DOE/NNSA contract, four application areas, and the four-volume 6.3 list.
- Verified via the OSTI records API: 2575336 (KENO since the 1960s), 2583839 (Polaris-PARCS), 2587031 (fifth volume, ENDF/B-VII.1, update of 6.2.4), 3007184 (threads/OpenMP/MPI in SCALE-Shift), 2572299 and 2583965 (non-LWR NRC datasets).
- Corrected: the license changed from fully UNKNOWN to KNOWN licensed, not open source; the terms are still UNKNOWN. How to obtain it is deliberately left out.
- Corrected: four versus five volumes settled as the four topic reports plus a likely overview volume [INFERRED].
- Restricted-content screen: clean. Overview pages and public OSTI reports only.

## Sweep 2 notes (ORNL Fact Checker, 2026-10-24)
- Re-fetched OSTI 2587031, 2575336, 2583839, 3007184, 2572299 and the CSAS-Shift manual page. No contradictions found.
- Load-bearing quotes: license, OSTI 2572299 (Dataset, ORNL, NRC sponsor, 2025-07-29) description: "required to obtain a license to the SCALE code system". Fifth volume, OSTI 2587031 description: "This report is the fifth volume in a series documenting the validation of SCALE 6.3". Parallelism, OSTI 3007184 abstract: "limited support for shared- and distributed-memory parallel processing was introduced via C++ threading, OpenMP, and MPI".
- Corrected: Shift as Monte Carlo engine moved from INFERRED to CORROBORATED (SCALE manual section 2.2.1 plus OSTI 1237627).
- Maturity words: none upgraded; no "production" claims.
- Walkthrough present and complete.
