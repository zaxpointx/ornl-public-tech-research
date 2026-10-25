# VERA (Virtual Environment for Reactor Applications)
- Official page: https://vera.ornl.gov/
- Repo: none public. VERA is not openly distributed. [KNOWN: no public code link on https://vera.ornl.gov/]
- Docs: overview only (https://vera.ornl.gov/). The training and resource pages weren't reviewed.
- License: [UNKNOWN] (not open source)
- Status: active [KNOWN: ORNL reports using VERA were published in 2026, OSTI 3403165 and 3384956]


## Plain-language walkthrough
- **What it is:** the Virtual Environment for Reactor Applications, a set of coupled codes that simulate a full reactor core in fine detail. [KNOWN: VERA OSTI records, see body]
- **The problem:** real reactors are expensive and risky to experiment on, so utilities and regulators want trustworthy, fuel-rod-level predictions.
- **What goes in:** a description of the core (fuel assemblies, rods, materials, operating conditions). [INFERRED]
- **What happens:** separate physics codes for neutrons (MPACT), coolant flow and heat (CTF) and fuel behavior trade results with each other over and over until they agree. [KNOWN: MPACT, OSTI 3002716; INFERRED: CTF per the discovery pass]
- **What comes out:** power, temperature and related values for every rod. [KNOWN: "rod by rod" core simulation in the body sources]
- **Where humans act:** engineers set up models and compare the output with plant measurements. VERA was validated against PWR data. [KNOWN: body sources]
- **What it is not:** not openly distributed, and not a single program. [KNOWN/INFERRED as tagged in body]
- **What's unknown:** license, current component list, and the ornl.gov onramp page (blocked to us).
- **Example:** predicting where the hottest rod in a pressurized-water reactor core will be after a refueling. [INFERRED: an illustrative use]

## What it is
VERA is a reactor simulator that can model a whole commercial nuclear reactor core in detail, down to individual fuel rods. The site says that's far finer than typical industry tools. [KNOWN: https://vera.ornl.gov/] It came out of CASL (the Consortium for Advanced Simulation of Light Water Reactors), which DOE established in 2010 to support the nuclear industry. [KNOWN: https://vera.ornl.gov/] CASL is commonly described as a DOE Energy Innovation Hub. [INFERRED: not stated on vera.ornl.gov; needs a DOE source] A light water reactor (LWR) is the ordinary kind of US power reactor, cooled by regular water.

## How it works
VERA is "multiphysics", meaning it solves several kinds of physics together because they affect each other: [KNOWN: https://vera.ornl.gov/ lists neutronics, thermal-hydraulics, fuel performance and coupled physics]
- **Neutronics:** where the neutrons go, which sets where power is produced.
- **Thermal-hydraulics:** how the coolant water flows and heats up.
- **Fuel performance:** how the fuel pellets and their metal cladding swell, crack and change over time.
More power heats the water, and hotter water changes how neutrons behave, so running these models coupled gives a more realistic answer than running each one alone. [INFERRED: the standard reason for coupling, consistent with the site's "more realistic representation" wording]

VERA also includes uncertainty quantification, which means estimating how confident you can be in each answer. It's validated against data from operating pressurized-water reactors (PWRs), single-effect experiments and integral tests. [KNOWN: https://vera.ornl.gov/] It's designed to run on everything from leadership-class supercomputers to industry workstation clusters. [KNOWN: https://vera.ornl.gov/]

Components: MPACT is VERA's neutronics code, and ORNL reports describe BWR (boiling water reactor) "rod cusping" work in VERA-MPACT. [KNOWN: OSTI 3002716, 3027390] The discovery pass also lists CTF (thermal-hydraulics) and Shift. [INFERRED: from the catalog note, not yet confirmed from a VERA page] The Shift paper says Shift was benchmarked against the "CASL VERA criticality test suite" (OSTI 1237627). That shows Shift was tested on VERA benchmark problems, not that it ships as a VERA component, so the tag stays INFERRED.

## How the project is organized
- Code layout and languages: [UNKNOWN]. There's no public code.
- Owner: ORNL hosts the site and VERA support. [KNOWN: the contact block on https://vera.ornl.gov/ is ORNL] Whether ORNL is the sole current developer is [UNKNOWN], since CASL was a multi-institution hub.
- Community: a users group is mentioned in the reading-pass notes, but it isn't in the vera.ornl.gov homepage text I fetched. [UNKNOWN]
- OSTI has a "VERA Infrastructure" record with ORNL as the research org. [KNOWN: the discovery pass, https://www.osti.gov/biblio/1546053]

## Who uses it / why it matters
ORNL uses VERA for current safety questions. One example is full-core analyses of how high-burnup fuel behaves in a loss-of-coolant accident (LOCA), coupled with the TRACE and BISON codes. [KNOWN: OSTI 3384956] Another is depletion analysis for benchmarking accident-tolerant fuel rods. [KNOWN: OSTI 3403165] Utilities that want to run fuel longer or use new fuel types need evidence like this to satisfy regulators. [INFERRED]

## Related projects
- SCALE (`scale`): ORNL's other major nuclear code suite, and possibly linked through Shift. [INFERRED]
- Thermochimica (`thermochimica`): fuel chemistry. [INFERRED: possible chemistry link, unconfirmed]

## Known / Inferred / Unknown
- KNOWN: CASL origin (2010), rod-level full-core simulation, physics areas, PWR validation, MPACT, ORNL-hosted support, 2026 ORNL usage.
- INFERRED: CTF and Shift as components; why the coupling matters.
- UNKNOWN: license terms, code layout, current release, whether other labs still co-develop it.

## Sources (accessed 2026-10-24)
- https://vera.ornl.gov/
- https://www.osti.gov/biblio/1546053 (VERA Infrastructure, via the discovery pass)
- https://www.osti.gov/biblio/3002716 and https://www.osti.gov/biblio/3027390 (MPACT BWR cusping)
- https://www.osti.gov/biblio/3384956 (full-core BWR LOCA with VERA, TRACE and BISON)
- https://www.osti.gov/biblio/3403165 (high-burnup radiochemical assessment, VERA depletion)
- Note: https://www.ornl.gov/onramp/casl-vera returned a Cloudflare block from my computer and wasn't read.

## Fact-check notes (2026-10-24)
- Verified via WebFetch of https://vera.ornl.gov/ (curl hit a Cloudflare block): CASL in 2010, single-fuel-rod resolution beyond industry tools, the neutronics/thermal-hydraulics/fuel performance/coupled physics areas, UQ, validation against operating PWRs, single-effect experiments and integral tests, the platforms, and ORNL contact.
- Corrected: 'Energy Innovation Hub' isn't on vera.ornl.gov, so it was retagged INFERRED.
- Unverifiable: the users group isn't in the homepage text. CTF and Shift aren't named in OSTI 1546053 or VERA search results, so they stay INFERRED.
- Verified OSTI: 1546053 (VERA Infrastructure, ORNL, CASL), 3002716 and 3027390 (MPACT BWR cusping), 3384956 (VERA with TRACE and BISON, Limerick LBLOCA), 3403165 (VERA full-core depletion, ATF rod).
- Restricted-content screen: clean.

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Re-fetched OSTI 1546053, 3002716, 3384956, 3403165 and 1237627. No contradictions.
- Load-bearing quotes: ORNL ownership of the infrastructure, OSTI 1546053 (Software, 2018-12-18, research org ORNL): VERA Infrastructure provides "the infrastructure to build, configure, test, install, and package for release the VERAS suite of codes". MPACT, OSTI 3002716: "cusping treatments in the Michigan PArallel Characteristics Transport (MPACT) code". Coupling, OSTI 3384956: "full-core, rod-resolved neutronic, thermal hydraulic, and fuel performance models using the VERA, TRACE, and BISON codes".
- Disconfirming check: OSTI 1237627 mentions VERA only as a benchmark suite for Shift; added a note so nobody reads it as proof that Shift is in VERA.
- MPACT is a Michigan-named code (the M in MPACT), so "VERA's neutronics code" is fine, but ORNL as its sole developer is not claimed and should not be.
- Maturity words: kept as written ("validated", "performed"). Walkthrough present.
