Short brief, public code (dormant). Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# NV (Nessus Visualization) and the SAVA team repos

- Repo: https://github.com/ornl-sava/nv [1]
- Org: https://github.com/ornl-sava (described as the "ORNL Situation Awareness and Visual Analytics Team") [2]
- DOE CODE: https://www.osti.gov/doecode/biblio/2281 and OSTI https://www.osti.gov/biblio/1231616 [3]
- License: NOASSERTION per GitHub (custom license file). [KNOWN: 1]
- Status: unknown (last push 2016-01-25). [KNOWN: GitHub API]
- ORNL relationship (RULES 13): KNOWN: OSTI and DOE CODE list ORNL as research org [3]. The GitHub org name alone would not count (RULES 13); the OSTI record does.
- Years visible in public sources: 2012 to 2016

## Walkthrough (plain language)
- **What it is:** A web tool that turns vulnerability-scan results into interactive charts, so you can see which hosts and findings matter most. [KNOWN: 3]
- **The problem:** Scan reports are long lists; patterns across a network are hard to see. [INFERRED from 3]
- **What goes in:** Output from a vulnerability scanner such as Nessus. [KNOWN: 3]
- **What happens:** A browser app parses the file and draws linked views. [KNOWN: repo README, 1]
- **What comes out:** Visual summaries by host, port and severity. [INFERRED from README]
- **Where humans act:** An admin explores and decides what to patch first. [INFERRED]
- **What it is not:** Not a scanner; it only reads scan output. [KNOWN: 3]
- **Example:** Load a scan of your own home lab and spot that one old VM carries most of the critical findings. (Illustrative.)
- **Unknown:** Users beyond the 31 GitHub stars; sponsor beyond USDOE.

## How it works
1. Input: a Nessus export. [KNOWN: 3]
2. Parse and visualize in the browser (JavaScript). [KNOWN: GitHub language field]

## Outside-in signals
- `nv`: 100 or more commits from 2012-12 to 2016-01 under 3 author names, 31 stars. [KNOWN: GitHub API]
- The same org holds small Node.js stream modules (regex-stream, replay-stream, redis-pubsub-stream), most flagged archived, and an `argus-docker` image for the Argus flow tool (last push 2021). [KNOWN: GitHub API, 2]
- The older `ornl-situ` GitHub org's description reads "Repo Moved. See ORNL-SAVA". [KNOWN: GitHub API] So the Situ team's public code and NV share one home. [INFERRED from the redirect; this does not prove shared code]

## What stands out (interpretation)
A good small project to read: one input format, one job, readable JavaScript.

## Related
- [Situ](../../../projects/situ.md): org redirect from ornl-situ to ornl-sava. [INFERRED]
- [Stucco](stucco.md): same era. [INFERRED]

## Known / Inferred / Unknown
- KNOWN: Purpose, OSTI record, dates, org redirect.
- INFERRED: Tie to the Situ team.
- UNKNOWN: Users, sponsor detail.

## Sources (accessed 2026-11-21 unless noted)
1. https://github.com/ornl-sava/nv (GitHub repo and API); supports: dates, stars, license
2. https://github.com/ornl-sava (GitHub org); supports: team name, sibling repos
3. https://www.osti.gov/doecode/biblio/2281 (DOE CODE record); supports: ORNL, description

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
