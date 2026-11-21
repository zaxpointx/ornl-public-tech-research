Short brief, public code (security-adjacent: physical and nuclear security software). Independent research, not affiliated with ORNL. People by role only. Last checked: 2026-11-21.

# OSCAR (Open Source Central Alarm Monitoring) and its zero-trust hub

- Repo: https://github.com/ORNL/oscar [1]
- Federation hub: https://github.com/ORNL/oscar-federation-hub [2]
- Camera emulator for testing: https://github.com/ORNL/Camera-emulator [3]
- License: MPL-2.0 [KNOWN: GitHub API, 1, 2, 3]
- Status: active: 646 commits; repo created 2026-11-02; releases v3.11.0 to v3.11.3 between 2026-11-17 and 2026-11-21. [KNOWN: GitHub API]
- ORNL relationship (RULES 13): KNOWN: repos in the main ORNL org.
- Years visible in public sources: 2026

## Walkthrough (plain language)
- **What it is:** A central alarm station platform for radiation portal monitors (the detectors vehicles pass through at checkpoints), built on OpenSensorHub and packaged as a hardened Docker Compose deployment. [KNOWN: README, 1]
- **The problem:** Alarms from many portal monitors need one secure place to be seen and handled. [INFERRED from README]
- **What goes in:** Sensor and camera feeds from monitored lanes. [KNOWN: README; camera emulator, 3]
- **What happens:** OpenSensorHub modules store and serve data, a web viewer shows alarms, and a TLS gateway is the only published entry point. [KNOWN: README]
- **What comes out:** An operator console. [KNOWN: README]
- **Where humans act:** Alarm operators; admins manage roles (admins, operators, viewers). [KNOWN: 2]
- **What it is not:** Not cyber research. It is security software engineering, included for its security design. [scope note]
- **Example:** The federation hub lets remote sites dial out over TLS port 443 to an Octelium zero-trust hub, so field sites open no inbound firewall ports, with optional Authentik single sign-on and MFA. [KNOWN: 2]
- **Unknown:** Where it is used. Deployment locations are out of scope and were not pursued.

## How it works
1. PostgreSQL/PostGIS and the app stay on private Compose networks; only HTTPS is published. [KNOWN: README]
2. A sibling repo holds a Playwright and fault-injection regression suite. [KNOWN: README table]

## Outside-in signals
- Created three weeks before the access date, with near-daily releases: the most active ORNL security-related code on GitHub at the moment. [KNOWN: dates; INFERRED: the ranking within this atlas]
- The viewer ships in English, Spanish, French and Greek. [KNOWN: README] That suggests users outside the US. [INFERRED]

## What stands out (interpretation)
Real zero-trust and hardening patterns (outbound-only tunnels, private networks, SSO roles) in readable Docker Compose. Very relevant to a networking and Linux student.

## Related
- [Live Data Server](../../../projects/live-data-server.md): another small ORNL service with authenticated access. [INFERRED: comparison only]

## Known / Inferred / Unknown
- KNOWN: Architecture, license, activity.
- INFERRED: Ranking, users outside the US.
- UNKNOWN: Deployments (out of scope).

## Sources (accessed 2026-11-21 unless noted)
1. https://github.com/ORNL/oscar (GitHub repo, README and API); supports: architecture, releases
2. https://github.com/ORNL/oscar-federation-hub (GitHub repo README); supports: zero-trust design
3. https://github.com/ORNL/Camera-emulator (GitHub repo README); supports: test tooling

## Verification
Sweep 1 done on 2026-11-21: each load-bearing source above was fetched that day unless it is marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not yet promoted to `discovery/catalog.csv`. See the [cyber atlas verification notes](../verification.md).
