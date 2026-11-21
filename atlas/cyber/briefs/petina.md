Short brief, public code and PyPI package. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# PETINA (Privacy prEservaTIoN Algorithms)

- Repo: https://github.com/ORNL/PETINA [1]
- DOE CODE: https://www.osti.gov/doecode/biblio/149859, DOI 10.11578/dc.20250116.1 [2]
- PyPI: https://pypi.org/project/PETINA/ [3]
- License: MIT [KNOWN: 1]
- Status: active: 157 commits, latest 2026-10-13, 5 author names in the latest 100 commits. [KNOWN: GitHub API]
- ORNL relationship (RULES 13): KNOWN: ORNL org repo; the README acknowledgement names DOE Office of Science ASCR under the ORNL contract. [1]
- Years visible in public sources: 2025 to 2026

## Walkthrough (plain language)
- **What it is:** A Python library of differential privacy tools: ways to add carefully sized noise to data or model updates so individual records can't be picked out. [KNOWN: README, 1]
- **The problem:** Sharing data, or training models on it, can leak details about individuals. [INFERRED: the standard motivation for differential privacy]
- **What goes in:** Numbers, lists, NumPy arrays or PyTorch tensors. [KNOWN: README]
- **What happens:** Mechanisms such as Laplace, Gaussian and exponential noise, plus clipping, pruning and count sketch. [KNOWN: README feature list]
- **What comes out:** Privatized data or gradients in the original shape. [KNOWN: README helpers]
- **Where humans act:** The developer picks the privacy budget (epsilon) and the mechanism. [INFERRED]
- **What it is not:** Not encryption and not access control. [INFERRED]
- **Example:** Add Laplace noise to a per-user count of failed logins before sharing it with another team. (Illustrative.)
- **Unknown:** Which ORNL projects use it.

## How it works
1. `pip install petina`. [KNOWN: 3]
2. Import a mechanism, set epsilon, apply it to data. [KNOWN: README]

## Outside-in signals
- 33 PyPI downloads in the last month as of the access date. [KNOWN: https://pypistats.org/api/packages/petina/recent]
- The README credits a former ORNL intern as a developer. [KNOWN: 1] Interns ship code that gets a DOE CODE DOI. [INFERRED]

## What stands out (interpretation)
Privacy engineering sits next to security at ORNL; the CRID fact sheet's identity science area mentions protecting citizens' privacy. [KNOWN: fact sheet] A tie between PETINA and CRID is UNKNOWN; PETINA is ASCR-funded.

## Related
- [Cyberwheel](../../../projects/cyberwheel.md): another current, pip-installable ORNL Python repo in the security area. [INFERRED: comparison only]

## Known / Inferred / Unknown
- KNOWN: Features, license, funding, activity.
- INFERRED: Low outside use (from downloads).
- UNKNOWN: Internal users, org unit.

## Sources (accessed 2026-11-21 unless noted)
1. https://github.com/ORNL/PETINA (GitHub repo and README); supports: features, license, acknowledgement
2. https://www.osti.gov/doecode/biblio/149859 (DOE CODE record); supports: DOI
3. https://pypi.org/project/PETINA/ (PyPI); supports: package

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
