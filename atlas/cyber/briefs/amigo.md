Short brief: news story and DOE CODE record; licensed; studied at description level only. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# AMIGO (Adversarial Malware Input Generator)

- News: https://www.ornl.gov/news/ornl-malware-vaccine-generator-licensed-evasiveai-platform (2023-03-23) [1]
- DOE CODE: https://www.osti.gov/doecode/biblio/95906 [2]
- License: Licensed to a startup for its commercial platform. [KNOWN: 1]
- Status: unknown at ORNL (commercialized)
- ORNL relationship (RULES 13): KNOWN: created in ORNL's Cyber Resilience and Intelligence Division [1]; OSTI research org ORNL [2].
- Years visible in public sources: 2019 to 2023

## Walkthrough (plain language)
- **What it is:** A tool that alters malware files without breaking them, to test whether malware detectors can be evaded, and that produces the training data detectors need to catch those variants. [KNOWN: 1, 2]
- **The problem:** Attackers already tweak malware to slip past ML-based antivirus. [KNOWN: 1]
- **What goes in:** Malware samples; the story cites more than 35 million. [KNOWN: 1]
- **What happens:** Binary changes that keep the program working. [KNOWN: 2] How it does this is not described or reconstructed here; that is out of scope.
- **What comes out:** Evasive variants plus the data needed to detect them. [KNOWN: 1]
- **Where humans act:** Evaluators use it to test products. [KNOWN: 1]
- **What it is not:** Not studied in this repo beyond its public description. [scope note]
- **Example:** It was the evaluation tool for a Navy (NAVWAR) challenge on AI that detects and quarantines threats. [KNOWN: 1]
- **Unknown:** Code (not public).

## How it works
1. Description level only. [KNOWN: 2]

## Outside-in signals
- A 2019 SULI undergraduate intern wrote its binary instrumentation code. [KNOWN: 1]
- It was built at the request of the Department of Defense. [KNOWN: 1]

## What stands out (interpretation)
The SULI detail is the lesson for Cayden: an undergraduate intern's code ended up inside a licensed product.

## Related
- [Photon](photon.md), [Lantern](lantern.md). [INFERRED: adversarial ML theme]
- [AI/ML cyber range](ai-ml-cyber-range.md). [INFERRED]

## Known / Inferred / Unknown
- KNOWN: Purpose, licensing, the intern's role.
- INFERRED: Range link.
- UNKNOWN: Implementation (deliberately not pursued).

## Sources (accessed 2026-11-21 unless noted)
1. https://www.ornl.gov/news/ornl-malware-vaccine-generator-licensed-evasiveai-platform (ORNL news, 2023-03-23); supports: licensing, intern, Navy challenge
2. https://www.osti.gov/doecode/biblio/95906 (DOE CODE record via OSTI API); supports: description

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
