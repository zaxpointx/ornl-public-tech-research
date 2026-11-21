Short brief (RULES 21): ORNL news story only, no public code. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# Photon (CAISER)

- News: https://www.ornl.gov/news/photon-framework-scales-ai-vulnerability-discovery/ (2026-03-24) [1]
- Center page: https://www.ornl.gov/center-for-artificial-intelligence-security-research/ [2]
- The public tool it was built from: https://github.com/deephyper/deephyper (DeepHyper) [3]
- License: UNKNOWN
- Status: unknown (no public repo found)
- ORNL relationship (RULES 13): KNOWN: ORNL's Center for AI Security Research (CAISER) developed it [1, 2].
- Years visible in public sources: 2025 (described as coming) to 2026

## Walkthrough (plain language)
- **What it is:** A framework that runs many attacks against an AI model at once on the Frontier supercomputer to find where the model breaks. [KNOWN: 1]
- **The problem:** Red-teaming AI by hand is slow; people can only try so many jailbreaks. [KNOWN: 1]
- **What goes in:** A target model and a catalog of attacks from published research. [KNOWN: 1]
- **What happens:** Attack agents start from known attacks, keep what works, explore nearby settings, and share results with each other with no central manager. It reuses DeepHyper, a hyperparameter-search tool, turned around to search for attack settings. [KNOWN: 1]
- **What comes out:** The most effective attack settings, so model developers can fix them. [KNOWN: 1]
- **Where humans act:** Researchers choose targets and read results. [INFERRED]
- **What it is not:** Not a tool you can download. [KNOWN: no repo found; see verification notes]
- **Example:** The story says Photon ran about 60,000 jailbreak prompts per hour and kept above 95% resource use across 1,920 GPUs. [KNOWN: 1]
- **Unknown:** Code, which models were tested, release plans.

## How it works
1. Seed with published attacks. [KNOWN: 1]
2. Exploit what works and explore around it. [KNOWN: 1]
3. Decentralized, asynchronous agents share findings. [KNOWN: 1]
4. Stop when the model stops getting worse. [KNOWN: 1]

## Outside-in signals
- A June 2025 trade-press interview said Photon would be released "in the coming months". [KNOWN-from-search-result: https://govciomedia.com/doe-accelerates-ai-research-to-defend-critical-infrastructure/] The March 2026 ORNL story announces it but links no code. [KNOWN: 1]
- DeepHyper is public, so the search pattern can be studied even though Photon can't. [KNOWN: 3]

## What stands out (interpretation)
The trick is reuse: a tool built to tune neural networks becomes a tool to attack them. The idea can be rebuilt at toy scale on a laptop against a small classifier (see the learn-and-build page).

## Related
- [Lantern](lantern.md): CAISER's interactive companion tool. [KNOWN: 2]
- [AMIGO](amigo.md): an earlier ORNL adversarial-ML tool. [INFERRED: same theme]

## Known / Inferred / Unknown
- KNOWN: Design idea, scale numbers, DeepHyper reuse.
- INFERRED: Release status, from the absence of a repo.
- UNKNOWN: Code, targets, licensing.

## Sources (accessed 2026-11-21 unless noted)
1. https://www.ornl.gov/news/photon-framework-scales-ai-vulnerability-discovery/ (ORNL news, 2026-03-24); supports: design and scale claims
2. https://www.ornl.gov/center-for-artificial-intelligence-security-research/ (CAISER page); supports: Photon and Lantern named as CAISER tools
3. https://github.com/deephyper/deephyper (DeepHyper repo); supports: public upstream

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
