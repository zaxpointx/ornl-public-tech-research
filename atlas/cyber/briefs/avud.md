Short brief (RULES 21): report page. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# AVUD (Automated Vulnerability Detection for compiled smart grid software)

- Publication page: https://www.ornl.gov/publication/automated-vulnerability-detection-avud-compiled-smart-grid-software (2022-09) [1]
- License: Commercialized, per the page. [KNOWN: 1]
- Status: unknown
- ORNL relationship (RULES 13): KNOWN: ORNL publication page [1].
- Years visible in public sources: up to 2022

## Walkthrough (plain language)
- **What it is:** A system that finds vulnerabilities in smart-meter firmware by statically analyzing the compiled code, without running it. [KNOWN: 1]
- **The problem:** Utilities and vendors need to check firmware they can't read as source. [INFERRED]
- **What goes in:** Compiled firmware. [KNOWN: 1]
- **What happens:** Static analysis using computational models of what the code does. [KNOWN: 1]
- **What comes out:** Vulnerability findings. [KNOWN: 1]
- **Where humans act:** Analysts review the findings. [INFERRED]
- **What it is not:** Not fuzzing; it doesn't run the code. [KNOWN: static analysis]
- **Example:** Demonstrated on example firmware with a smart-meter manufacturer. [KNOWN: 1]
- **Unknown:** Code.

## How it works
1. Built into ORNL's smart-meter test bed. [KNOWN: 1]

## Outside-in signals
- The page reports an R&D 100 award and a national lab commercialization award. [KNOWN: 1]
- It shares the "work out what code does without running it" idea with [Hyperion](../../../projects/hyperion.md). [INFERRED: same idea and overlapping credited authors; authorship proves participation only]

## What stands out (interpretation)
Static firmware analysis is the skill behind CyTRICS-style testing.

## Related
- [Hyperion](../../../projects/hyperion.md), [CyTRICS at ORNL](cytrics-ornl.md). [INFERRED]

## Known / Inferred / Unknown
- KNOWN: Purpose, awards, commercialization.
- INFERRED: Hyperion link.
- UNKNOWN: Code.

## Sources (accessed 2026-11-21 unless noted)
1. https://www.ornl.gov/publication/automated-vulnerability-detection-avud-compiled-smart-grid-software (ORNL publication page); supports: all claims

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
