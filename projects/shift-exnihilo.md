# Shift / Exnihilo
- Official page: https://www.ornl.gov/publication/shift-massively-parallel-monte-carlo-radiation-transport-package
- Repo: none public. It ships as part of SCALE [KNOWN: SCALE manual CSAS-Shift chapter]. Not openly distributed [INFERRED: follows from SCALE's own licensing, not stated for Shift itself]
- Docs: public SCALE 6.3.3 manual, CSAS-Shift chapter: https://scale-manual.ornl.gov/6.3.3/CSAS-Shift.html
- License: [UNKNOWN] (not open source)
- Status: active [INFERRED: a 2025 GPU/Frontier paper, OSTI 3013520, shows ongoing development]


## Plain-language walkthrough
- **What it is:** ORNL's massively parallel Monte Carlo radiation transport code, part of the Exnihilo suite. [KNOWN: ornl.gov publication page, SCALE manual]
- **The problem:** tracking neutrons through complex nuclear systems accurately takes enormous computing power.
- **What goes in:** a SCALE-style model (geometry, materials, cross sections). Inside SCALE, you add `-shift` to a CSAS sequence. [KNOWN: SCALE manual]
- **What happens:** it simulates billions of random particle histories across many processors or GPUs. [INFERRED: general Monte Carlo; KNOWN: GPU runs on Frontier, OSTI 3013520]
- **What comes out:** k-effective or radiation levels, with error bars. [KNOWN: eigenvalue and fixed-source modes, SCALE manual]
- **Where humans act:** analysts build models and decide when the statistics are good enough.
- **What it is not:** not openly distributed. It ships with SCALE. [KNOWN]
- **What's unknown:** license, code layout.
- **Example:** a criticality-safety analyst reruns a KENO input with CSAS-Shift to use more cores. [KNOWN: the SCALE manual describes it as a KENO alternative; INFERRED: the motive]

## What it is
Shift is ORNL's high-speed radiation transport code. "Radiation transport" means tracking how neutrons and other particles travel through and interact with matter. [KNOWN: ornl.gov publication page] It's "massively parallel": it's built to spread one problem over a huge number of processors, from a laptop up to a supercomputer. [KNOWN: SCALE manual] Shift belongs to Exnihilo, a suite of transport codes that also includes Denovo, a "discrete ordinates" solver. [KNOWN: SCALE manual cites Shift as part of the Exnihilo suite, and cites the Denovo 2010 paper] Discrete ordinates means solving the transport equations on a fixed grid of directions instead of with random sampling. [INFERRED: standard definition]

## How it works
- **Monte Carlo:** Shift simulates huge numbers of individual particles with random choices (where they scatter, whether they get absorbed) and averages the results. More particles give less statistical noise. [KNOWN: "Monte Carlo" in the title of the ornl.gov page; INFERRED: the explanation]
- **Two problem types:** "eigenvalue" problems, which ask whether a system sustains a chain reaction (the k-effective number), and "fixed-source" problems, which ask how much radiation reaches a given spot. [KNOWN: SCALE manual]
- **Geometry engine:** ORANGE (Oak Ridge Adaptable Nested Geometry Engine) reads SCALE's existing KENO geometry formats, so old inputs keep working. It also adds features like randomly packing tiny TRISO fuel particles inside a pebble. [KNOWN: SCALE manual] TRISO particles are poppy-seed-sized coated fuel kernels used in some advanced reactors. [INFERRED: general definition]
- **Inside SCALE:** in SCALE's CSAS criticality-safety sequence, you switch from KENO to Shift by adding `-shift` to the sequence name. [KNOWN: SCALE manual] Shift computes k-effective uncertainty with a track-length estimator, which is different from KENO's estimators, so the two codes' error bars can differ slightly. [KNOWN: SCALE manual]
- **Variance reduction:** "hybrid" methods (CADIS and forward-weighted CADIS) first run a quick deterministic solve to steer the Monte Carlo particles toward the regions that matter. That cuts the computing time needed. [CORROBORATED: OSTI 3013520 and OSTI 1237627 both name CADIS and FW-CADIS; INFERRED: the plain explanation]
- **GPUs:** a 2025 paper ran Shift on Frontier. GPU "event-based" transport on AMD Instinct 250X GPUs (the abstract’s wording) gave about 9 to 11 times the throughput per graphics compute die of the best CPU run, and hard problems finished in under 2 minutes on 20 Frontier nodes. [KNOWN: OSTI 3013520, DOI 10.1080/00295639.2025.2484511]

## How the project is organized
- Code layout and languages: [UNKNOWN]. There's no public code.
- People and group: the 2016 JCP paper's author line reads "Radiation Transport Group, Reactor and Nuclear Systems Division", and its introduction says Shift is developed and maintained at ORNL by that group. [KNOWN: OSTI 1237627, Pandya et al., J. Comput. Phys. 308 (2016), author affiliations and introduction, full text checked by the fact-check pass 2026-10-24; single source, so not CORROBORATED] The group's current name is [UNKNOWN].
- Key papers: 2015 ANS conference paper (ornl.gov page) and 2016 JCP paper (cited in the SCALE manual).

## Who uses it / why it matters
SCALE users get it for criticality safety and reactor physics. The manual says it scales better on many cores than the KENO sequences. [KNOWN: SCALE manual] It's also one of the clearest public examples of a nuclear code moving onto exascale GPUs. [INFERRED from OSTI 3013520]

## Related projects
- SCALE (`scale`): Shift ships inside it. [KNOWN: SCALE manual]
- VERA (`vera`): The discovery pass lists Shift as a VERA component. [INFERRED: not confirmed from a VERA page. OSTI 1237627 only says Shift was benchmarked on the "CASL VERA criticality test suite", which shows a test link, not membership]
- Frontier/OLCF: hardware used in the 2025 study. [KNOWN: OSTI 3013520]

## Known / Inferred / Unknown
- KNOWN: Exnihilo membership, ORANGE, CSAS-Shift use, track-length estimator, CADIS, Frontier GPU results.
- INFERRED: plain definitions, the VERA link.
- UNKNOWN: license, code layout, current maintainers list, the group's current name.

## Sources (accessed 2026-10-24)
- https://www.ornl.gov/publication/shift-massively-parallel-monte-carlo-radiation-transport-package
- https://scale-manual.ornl.gov/6.3.3/CSAS-Shift.html
- https://www.osti.gov/biblio/3013520 (Nuclear Science and Engineering 2025)
- https://www.osti.gov/biblio/1237627 (Pandya et al., JCP 2016)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Sweeps 1 and 2 done.
- Status changed from KNOWN to INFERRED: one 2025 paper shows ongoing work but isn't a release statement.
- "Not openly distributed" changed to INFERRED. Ships-in-SCALE stays KNOWN.
- CADIS/FW-CADIS changed to CORROBORATED. OSTI 1237627 (JCP 2016, abstract): "Special features of Shift include hybrid capabilities for variance reduction such as CADIS and FW-CADIS". OSTI 3013520 (NSE 2025, abstract) names both too.
- Frontier results verified in OSTI 3013520 (abstract): "less than 2 min on 20 nodes of Frontier" and "9 to 11 times greater throughput per graphics compute die than the best CPU performance".
- I read the group credit myself in the OSTI 1237627 full text (Introduction): "developed and maintained at Oak Ridge National Laboratory (ORNL) by the Radiation Transport Group". It also says "Development of Shift began at ORNL in 2010". KNOWN, single source.
- The ornl.gov publication page is verified: Pandya et al., Trans. ANS, April 2015, M&C + SNA + MC conference, Nashville.
- Added a caveat to the VERA link: it's a benchmark-suite link only.
