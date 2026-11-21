Short brief, public code. Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# Systemd Snapshot

- Repo: https://github.com/ORNL/Systemd_Snapshot [1]
- License: UNKNOWN. The repo has no LICENSE file and GitHub reports none. [KNOWN: GitHub contents API, 1] Without a license, reuse rights are not granted by default. [INFERRED: general copyright rule]
- Status: quiet: 3 commits, 2025-03-04 to 2025-08-25, one author name. [KNOWN: GitHub API]
- ORNL relationship (RULES 13): KNOWN: the repo is in the main ORNL GitHub org (counts under RULES 13).
- Years visible in public sources: 2024 (repo created) to 2025

## Walkthrough (plain language)
- **What it is:** A Linux forensics helper that reads every systemd unit file on a disk image or mounted file system and maps what starts what. [KNOWN: README, 1]
- **The problem:** On a broken or compromised Linux box you often can't run `systemctl`, but you still need to know what starts at boot and in what order. [KNOWN: README]
- **What goes in:** A root path to the local system or a mounted ("remotely hosted") file system. [KNOWN: README]
- **What happens:** It parses unit files in the default system paths, records explicit and implicit dependencies in one JSON "master struct", then walks the dependency tree from `default.target` or any unit you pick. [KNOWN: README]
- **What comes out:** A JSON dependency map, a Cytoscape graph file, optional networkx graphs, and a `diff` action to compare snapshots. [KNOWN: README usage]
- **Where humans act:** The analyst picks the start unit, reads the graph and compares snapshots. [KNOWN]
- **What it is not:** Not a live monitoring agent and not a malware detector by itself. [INFERRED from README scope]
- **Example:** Snapshot a clean server image, snapshot it again after an incident, run `diff`, and spot a new service wired into `multi-user.target`. (Illustrative. Persistence through systemd units is a well-known attacker technique.)
- **Unknown:** Which ORNL project it came from, and why there is no license.

## How it works
1. `-a master -p /mnt/image` builds the master struct. [KNOWN: README]
2. `-a deps` builds the dependency map and `-a graph` writes the graph. [KNOWN: README]
3. `-a diff` compares two snapshots. [KNOWN: README]
4. Pure Python, with tests in `unit_tests/`. [KNOWN: repo tree]

## Outside-in signals
- One author name across 3 commits points to a one-person tool released as-is. [INFERRED]
- The missing license is a real gap for reuse. Asking upstream counts as outreach and needs Cayden's OK first (AGENTS.md).

## What stands out (interpretation)
Probably the best ORNL repo for a Linux-minded cyber student to read and run this week: small, pure Python, and about a real forensics problem (boot persistence).

## Related
- [Akatosh](../../../projects/akatosh.md): the same before-and-after snapshot idea, for whole hosts. [INFERRED: same idea, no code tie]

## Known / Inferred / Unknown
- KNOWN: What it does, inputs and outputs, commit history.
- INFERRED: Its use for spotting persistence.
- UNKNOWN: Source project, license intent, users.

## Sources (accessed 2026-11-21 unless noted)
1. https://github.com/ORNL/Systemd_Snapshot (GitHub repo, README and API); supports: everything above

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
