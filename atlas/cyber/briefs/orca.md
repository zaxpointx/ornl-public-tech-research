Short brief, project page plus one small public repo. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# ORCA (Oak Ridge Cyber Analytics) and pcapmunger

- Official page: https://www.ornl.gov/projects/orca/ [1]
- Report page: https://www.ornl.gov/publications/oak-ridge-cyber-analytics-methods-for-advanced-intrusion-detection-and-cyber-security-data-analysis/ [2]
- Repo: https://github.com/ORNL/pcapmunger [3]
- License: pcapmunger: MIT [KNOWN: GitHub API, 3]. ORCA itself: UNKNOWN (no public code).
- Status: unknown. pcapmunger has a single commit (2022-05-09). [KNOWN: GitHub API]
- ORNL relationship (RULES 13): KNOWN: ORNL project page [1]; pcapmunger sits in the ORNL GitHub org and its README says the scripts came from the ORCA training pipeline [3].
- Years visible in public sources: about 2011 to 2022 (pcapmunger release)

## Walkthrough (plain language)
- **What it is:** An ORNL intrusion detection research system. Its Attack Variant Detector uses machine learning on network-flow features to flag new attacks and variants of known ones. [KNOWN: 1]
- **The problem:** Signature-based IDS tools only catch what someone already wrote a rule for. [KNOWN: 1]
- **What goes in:** Full packet captures, rolled up into flows (5-tuple, 2-second windows), plus alerts from other tools. [KNOWN: 1, 2]
- **What happens:** A configurable pipeline of feature, summation and alert blocks classifies traffic as normal or malicious. [KNOWN: 1]
- **What comes out:** Log-style alerts for a log aggregation system. [KNOWN: 1]
- **Where humans act:** Operators train it with examples of attack and normal traffic from their own network, then read the alerts. [KNOWN: 1]
- **What it is not:** pcapmunger is not ORCA. It is a helper that overlays attack packets onto background traffic to make training data. [KNOWN: 3]
- **Example:** Splice a capture of a port scan into a day of normal office traffic with pcapmunger and you get a labeled training file. (Illustrative; matches the README's sample folders, 3.)
- **Unknown:** Where ORCA ran beyond the page's "experimental military networks", and whether it was licensed.

## How it works
1. A capture card writes PCAP to disk at line rate. [KNOWN: 1]
2. Flows are aggregated per 5-tuple and time window and served by a web service. [KNOWN: 1]
3. Pipeline blocks pass a shared feature message downstream. [KNOWN: 1]
4. pcapmunger needs the Wireshark command-line tools, Bittwist and tcpdump on the PATH. [KNOWN: 3]

## Outside-in signals
- The ORNL page says ORCA-AVD was verified on experimental military networks. [KNOWN: 1] The maturity verb stays "verified", not "deployed" (RULES 10).
- pcapmunger was released "to facilitate the publication of PCAP datasets". [KNOWN: 3] The lab released the data-prep tool, not the detector. [INFERRED]

## What stands out (interpretation)
The clearest public case of ORNL open-sourcing the needed-but-boring tooling (data prep) while the detector itself stays unpublished.

## Related
- [Stucco](stucco.md), [NV](nessus-visualization.md): same analyst-tooling era. [INFERRED]
- [Data Driven User Emulator](data-driven-user-emulator.md): another way ORNL makes realistic background traffic. [INFERRED]

## Known / Inferred / Unknown
- KNOWN: Design, flow features, pipeline idea, pcapmunger's purpose and license.
- INFERRED: Why only the data tool was released.
- UNKNOWN: Deployment, licensing, sponsor.

## Sources (accessed 2026-11-21 unless noted)
1. https://www.ornl.gov/projects/orca/ (ORNL project page); supports: design and verification claim
2. https://www.ornl.gov/publications/oak-ridge-cyber-analytics-methods-for-advanced-intrusion-detection-and-cyber-security-data-analysis/ (ORNL publication page); supports: alert filtering, clustering, swarm analysis
3. https://github.com/ORNL/pcapmunger (GitHub repo and API); supports: license, commit, purpose

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
