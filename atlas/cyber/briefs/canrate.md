Short brief, public code. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# CANRate

- Repo: https://github.com/ORNL/CANRate [1]
- DOE CODE: https://www.osti.gov/doecode/biblio/177813 [2]
- License: GPL-3.0 [KNOWN: 1]
- Status: quiet: 9 commits, 2025-10-09 to 2026-02-19, one author name. [KNOWN: GitHub API]
- ORNL relationship (RULES 13): KNOWN: ORNL org repo; OSTI sponsor NNSA [2].
- Years visible in public sources: 2025 to 2026

## Walkthrough (plain language)
- **What it is:** A Rust command-line tool that measures the fastest rate a CAN network can reliably send and receive messages. [KNOWN: 1, 2]
- **The problem:** Before testing attacks or detectors, you need to know the bus's real throughput limit. [INFERRED]
- **What goes in:** A Linux SocketCAN interface such as `can0`, run once as sender and once as receiver. [KNOWN: README]
- **What happens:** It sends and checks frames, warning on failed sends or wrong data. [KNOWN: README flags]
- **What comes out:** The maximum stable message rate. [KNOWN: 2]
- **Where humans act:** A tester runs both ends. [KNOWN]
- **What it is not:** Not an attack tool. [KNOWN: description]
- **Example:** `canrate --warn can0 tx` on one machine and `canrate --warn can0 rx` on the other. [KNOWN: README]
- **Unknown:** Which ORNL project uses it.

## How it works
1. Rust and Cargo over SocketCAN. [KNOWN: repo tree]

## Outside-in signals
- It ships a THIRD_PARTY_LICENSES file, a sign of a formal release review. [INFERRED]

## What stands out (interpretation)
Runs on two Raspberry Pis with CAN add-on boards, so it is a realistic first ORNL tool to run on real hardware. Whether it works on Linux's virtual `vcan` interface is UNKNOWN until tried.

## Related
- [ELDSentry](eldsentry.md). [KNOWN: same sponsor]

## Known / Inferred / Unknown
- KNOWN: Function, license, sponsor.
- INFERRED: Use case.
- UNKNOWN: Users.

## Sources (accessed 2026-11-21 unless noted)
1. https://github.com/ORNL/CANRate (GitHub repo and README); supports: usage, license
2. https://www.osti.gov/doecode/biblio/177813 (DOE CODE record); supports: sponsor, description

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
