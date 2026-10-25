# DataFed
- Official page / Docs: https://ornl.github.io/DataFed/ [KNOWN: README, GitHub API homepage]
- Repo: https://github.com/ORNL/DataFed
- License: a custom UT-Battelle permissive open-source license ("DataFed, Version 1"). It allows use, modification and redistribution, but requires keeping notices and noting changes, and bars using DOE or UT-Battelle names for endorsement. Copyright 2020 UT-Battelle, LLC [KNOWN: LICENSE.md, https://github.com/ORNL/DataFed/blob/master/LICENSE.md]. GitHub shows NOASSERTION because it isn't a standard SPDX license [INFERRED].
- Status: active, last push 2026-10-23 [KNOWN: GitHub API]

## What it is (plain English, 2-4 sentences)
DataFed is a system for keeping track of scientific data spread across many research facilities, so researchers can find, describe, share and move it in one consistent way no matter where it's stored [KNOWN: README]. "Federated" means many separately run storage sites are tied together by one shared catalog, instead of each lab keeping its own isolated "data silo" [KNOWN: docs overview uses the silo framing]. Its central services are hosted at ORNL's Oak Ridge Leadership Computing Facility (OLCF) [KNOWN: doc_source/source/system/overview.rst].

## How it works (plain English, no jargon without definition)
- There's a central Core Service plus a Core Database that store *records*. A record is the metadata about a dataset (what it is, who owns it, how it relates to other data), but not the raw data itself [KNOWN: README service list].
- The raw files stay in Repository Services that sit next to the storage at each facility [KNOWN: README].
- Actual file transfers are handed off to Globus, a widely used research data-transfer service, using GridFTP servers built for fast bulk transfers [KNOWN: overview.rst]. DataFed copies the data, it doesn't move it [KNOWN: overview.rst].
- Login and permissions go through Globus's federated identity system, based on OAuth2. OAuth2 is the "sign in with..." standard that lets you use one account across services without sharing your password [KNOWN: overview.rst; OAuth2 explanation is general background].
- Users get to it through a web portal, a command-line tool, and a Python package [KNOWN: README; python/datafed_pkg folder].

## How the project is organized (repo structure, languages, build, maintainers/org unit, release cadence)
- Languages: about 83% JavaScript (web portal and database logic), 9% C++ (core and repo servers) and 3% Python (client) [KNOWN: GitHub languages API].
- `core/` holds the core server and database, `repository/` the repository service, `web/` the portal (Node.js-style, with views and static assets) and `python/` the client package. `common/` has shared code and protobuf message definitions (protobuf is Google's format for sending structured messages between programs). The rest are `facility/`, `docker/` and `compose/` (container deployment), `doc_source/` (docs source) and `docs/` (built docs site) [KNOWN: repo tree; protobuf from the common/proto3 folder].
- Build: CMake, plus Docker Compose for deployment [KNOWN: CMakeLists.txt, compose/; README points to BUILD.md].
- Versioning: the README says components use semantic versions, while the overall release uses calendar-style tags (YEAR.MONTH.DAY.HOUR.MINUTE) [KNOWN: README]. Recent releases are v4.0.0 (2025-12-09), v5.0.0 (2026-03-02) and v5.1.0 to v5.1.2 (April 2026), plus calendar tags like v2025.11.17.14.00 [KNOWN: GitHub releases and tags API]. The repo was created 2019-05-16 [KNOWN].
- Contributors: about 22 per the GitHub API, counting anonymous ones [KNOWN: contributors pagination, accessed 2026-10-24].
- Org unit: OLCF hosts the central services [KNOWN: overview.rst]. DOE CODE record code-48776 (2019) lists ORNL as research org [KNOWN: https://www.osti.gov/api/v1/records?q=DataFed&product_type=Software, accessed 2026-10-24]. Whether OLCF also develops it is [UNKNOWN].

## Who uses it / why it matters
- Teams that run experiments at one facility, simulations at another and analysis somewhere else, and need to keep track of which data came from where [KNOWN: README mentions cross-facility experimentation, simulation and analytics]. Specific use cases are listed in docs `system/usecases.rst` [KNOWN: file exists; not summarized this pass].
- Security angle for a cyber student: logins and transfer permissions go through Globus, and users explicitly authorize DataFed to act for them [KNOWN: overview.rst]. That means DataFed doesn't need to hold user passwords itself [INFERRED: from the Globus OAuth2 design; the docs don't say this outright].

## Related projects
- Hosted at OLCF, see olcf-user-docs [KNOWN].
- Depends on Globus (external) [KNOWN].
- Flowcept (workflow provenance) is in a nearby data-management space [INFERRED: domain only].

## Known / Inferred / Unknown
- [KNOWN] Architecture (core, database, repositories, Globus, web, CLI, Python), central services at OLCF, custom UT-Battelle license, JS/C++/Python, active 2026 releases.
- [INFERRED] Relation to Flowcept.
- [UNKNOWN] Developing team or division, number of facilities currently connected, and user counts.

## Sources (URL, accessed date)
- https://github.com/ORNL/DataFed (README, LICENSE.md, doc_source/source/system/overview.rst, tree), accessed 2026-10-24
- https://ornl.github.io/DataFed/, linked, not opened this pass
- https://api.github.com/repos/ORNL/DataFed (+ /languages, /releases, /tags, /contributors), accessed 2026-10-24

## Fact-check notes (ORNL Fact Checker, 2026-10-24)
- Retagged: "never stores passwords" was KNOWN but isn't stated in overview.rst; rewrote as KNOWN Globus authorization + INFERRED no-password conclusion.
- Added: DOE CODE code-48776 confirms ORNL.
- Verified: custom UT-Battelle license (2020, DataFed Version 1), OLCF hosting, Globus/GridFTP transfers that copy not move, OAuth2 identity, data-silo framing, semantic + calendar versioning, release and tag dates, repo tree, ~22 contributors.
- Unverifiable: developing team or division.
- No restricted content or implied ORNL affiliation found.
