Short brief (RULES 21): publication page only, no public code. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# Lantern (CAISER adversarial AI workbench)

- Publication page: https://www.ornl.gov/publications/lantern-an-interactive-adversarial-ai-workbench/ (CSIAC Journal 9(1), February 2025) [1]
- Center page: https://www.ornl.gov/center-for-artificial-intelligence-security-research/ [2]
- License: UNKNOWN
- Status: unknown
- ORNL relationship (RULES 13): KNOWN: ORNL publication page and CAISER page [1, 2].
- Years visible in public sources: 2025

## Walkthrough (plain language)
- **What it is:** An interactive tool for designing one-off adversarial attacks against AI models, aimed at users who are not attack specialists. [KNOWN: 1]
- **The problem:** Existing tools test robustness across whole datasets; few help craft one tailored attack for a real scenario. [KNOWN: 1]
- **What goes in:** A model and a chosen attack type. [KNOWN: 1]
- **What happens:** The user adjusts and evaluates attacks interactively; models and attacks are swappable across ML frameworks. [KNOWN: 1]
- **What comes out:** An evaluated attack against that model. [KNOWN: 1]
- **Where humans act:** Central: it is built for a person to drive. [KNOWN: 1]
- **What it is not:** Not automated mass testing (that is Photon). [KNOWN: 1, 2]
- **Example:** UNKNOWN beyond the abstract.
- **Unknown:** Code, supported frameworks, availability.

## How it works
1. Interactive, modular attack and model interfaces. [KNOWN: 1]

## Outside-in signals
- Named on the CAISER page as an "interactive adversarial toolbox". [KNOWN: 2]

## What stands out (interpretation)
Lantern and Photon are two halves of one approach: a human-driven workbench and a machine-scale search.

## Related
- [Photon](photon.md). [KNOWN: 2]

## Known / Inferred / Unknown
- KNOWN: Purpose and design aim.
- INFERRED: Pairing with Photon.
- UNKNOWN: Code and release.

## Sources (accessed 2026-11-21 unless noted)
1. https://www.ornl.gov/publications/lantern-an-interactive-adversarial-ai-workbench/ (ORNL publication page); supports: purpose, venue, date
2. https://www.ornl.gov/center-for-artificial-intelligence-security-research/ (CAISER page); supports: tool naming

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
