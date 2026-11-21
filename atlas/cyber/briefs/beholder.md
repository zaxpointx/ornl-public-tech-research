Stub (RULES 14): OSTI record only. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# Beholder IDS client

- OSTI: https://www.osti.gov/biblio/1440330 (2013-09-01) [1]
- License: UNKNOWN
- Status: stub-osti-only
- ORNL relationship (RULES 13): KNOWN: OSTI research org ORNL [1].
- Years visible in public sources: 2013

## Walkthrough (plain language)
- **What it is:** A host client that spots hidden malware by measuring timing changes in critical system functions and sending reports to a server that decides whether the host is infected. [KNOWN: 1]
- **The problem:** Rootkits hide by hooking the system's own functions. [KNOWN: 1]
- **What goes in:** Timing data for system functions. [KNOWN: 1]
- **What happens:** The client measures; the server post-processes. [KNOWN: 1]
- **What comes out:** An infection verdict. [KNOWN: 1]
- **Where humans act:** Admins act on verdicts. [INFERRED]
- **What it is not:** Not signature antivirus. [INFERRED]
- **Example:** UNKNOWN.
- **Unknown:** Everything beyond the record.

## How it works
1. Client-server timing analysis. [KNOWN: 1]

## Outside-in signals
- The same side-channel idea as [Heartbeat](../../../projects/heartbeat-malware.md), which uses power instead of timing. [INFERRED]

## What stands out (interpretation)
Hiding costs time, and time can be measured.

## Related
- [Heartbeat](../../../projects/heartbeat-malware.md). [INFERRED]

## Known / Inferred / Unknown
- KNOWN: The idea.
- INFERRED: Heartbeat link.
- UNKNOWN: All else.

## Sources (accessed 2026-11-21 unless noted)
1. https://www.osti.gov/biblio/1440330 (OSTI record via API); supports: description

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
