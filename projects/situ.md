# Situ

> DRAFT, `draft-osti-only` (2026-10-24, lead's call). The only public source is an OSTI record, with no docs page. Kept as a draft, not counted as a full brief.
- Official page: https://www.osti.gov/biblio/1232450 (OSTI software record, dated 2014-06-16)
- Repo: none found [KNOWN: Scout catalog note; OSTI record only]
- Docs: the OSTI abstract only
- License: [UNKNOWN]
- Status: [UNKNOWN]. The only public record is from 2014, so it may be dormant [INFERRED]

## Plain-language walkthrough
- What it is: a 2014 ORNL prototype that scores security events by how unusual they are.
- Problem: new attacks hide in huge streams of normal-looking data.
- In: streaming, mixed-format event data.
- What happens: unsupervised probability models score each event at several scales.
- Out: anomaly scores with a reason, pushed live to a web view.
- Humans: analysts read the flagged events and decide what's real.
- Not: a product, and there's no public code.
- Unknown: whether it's still used or evolved into something else.
- Example: an odd event gets a high score plus a note on what made it unusual.

## What it is
Situ is an ORNL cyber-defense prototype that scores incoming events (network activity is the likely case [INFERRED]; the record just says "events") and flags events that look unusual. It also explains why each one looks unusual, so a human analyst understands what's going on. [KNOWN: OSTI 1232450] "Situational awareness" in security means knowing what's happening on your network right now and why it matters. [INFERRED: standard definition]

## How it works
- **Anomaly detection, not signatures:** antivirus-style tools match known attack patterns (signatures). Situ instead learns what "normal" looks like and scores how typical each event is, so it can catch new attacks that have no signature yet. [KNOWN: OSTI abstract says it scores events by how typical they are; INFERRED: the contrast with signatures]
- **Unsupervised probabilistic models:** it learns from unlabeled data. Nobody has to tag examples as "attack" or "benign" first. [KNOWN: OSTI abstract]
- **Multiple scales:** events are scored at several levels of detail (for example a single connection, a host, a subnet). That surfaces events that would be hidden at one level and lets the system explain the score. [KNOWN: OSTI abstract for multi-scale scoring and explanations; INFERRED: the example levels]
- **Real time:** it's designed for very high-volume, mixed, streaming data, and pushes scored events to a web-based visualization for analysts. [KNOWN: OSTI abstract]

## How the project is organized
- [UNKNOWN]: no public code, languages or team details beyond ORNL as research org. [KNOWN: OSTI 1232450 research org]
- The sponsor field in the API record is malformed (it just says "u"). [KNOWN: OSTI records API output]

## Who uses it / why it matters
It's a clear public example of the ORNL cyber group's machine-learning approach to intrusion detection, and the explanation part (why something is anomalous) is still a hot topic in security. [INFERRED] Real deployments are [UNKNOWN].

## Related projects
- Cyberwheel (`cyberwheel`): a newer ORNL cyber-defense tool using reinforcement learning, a different approach to the same problem. [INFERRED: same domain, no link found]
- The other batch 4 cyber rows (cincinnatus, heartbeat-malware, cpad, hyperion) are also OSTI-only. [KNOWN: Scout notes]

## Known / Inferred / Unknown
- KNOWN: purpose, unsupervised multi-scale anomaly scoring, streaming design, web visualization, ORNL record.
- INFERRED: dormancy, explanatory definitions.
- UNKNOWN: code, license, team, deployments, sponsor.

## Sources (accessed 2026-10-24)
- https://www.osti.gov/biblio/1232450

## Sweep 2 notes (ORNL Fact Checker, 2026-10-24)
- Sweeps 1 and 2 done. OSTI 1232450 refetched. Facts match: Software, 2014-06-16, ORNL, sponsor field just "u", no authors listed.
- Narrowed "network activity" to INFERRED. The record says it "scores events in real-time based on probabilistic models".
- Added the rule 12 walkthrough. No restricted content found.
