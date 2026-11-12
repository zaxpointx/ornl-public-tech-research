# ORNL Atlas deep-research plan

**Purpose:** Build a complete public research guide to ORNL's technical ecosystem, originally kept in a separate working repository (ornl-atlas) and merged into this repository's `atlas/` folder on 2026-11-11.

## Deliverable shape

The finished atlas will have:

1. A portfolio map of ORNL research programs and project families.
2. Project dossiers with direct evidence, facilities, data, software, people, jobs, partners, timelines, and unknowns.
3. A public software registry with repository, release, license, citation, dependency, and safety notes.
4. A facilities and data map linking instruments, compute, manufacturing, networks, and public user programs.
5. A job-family and team map grounded in public role descriptions and official profiles.
6. A relationship graph showing which connections are direct and which are inferred.
7. An unusual-connections section that explains why scattered public facts matter together.
8. Optional local study/rebuild tracks attached to researched projects.

## Research lanes

### Lane A: Autonomous science and cross-facility workflows

Priority sources: INTERSECT, autonomous science, autonomous chemistry, additive manufacturing, AGILE, WES jobs, Flowcept, DataFed, Zambeze, AHPI, SciNet.

Status: direct-source portfolio pass completed for the main INTERSECT science, architecture, integration, field, quantum-edge, and software-deployment pages. Individual public repositories and remaining catalog entries still need repository-level review.

### Lane B: Scientific instruments and data loops

Priority sources: HFIR, SNS, VENUS, neutron workflows, automated microscopy, imaging, edge inference, instrument APIs, public papers.

### Lane C: Computing and scientific software

Priority sources: OLCF, Frontier, chatHPC, Codex/HPC records, ORNL Software Catalog, DOE CODE, public ORNL repositories, public release guidance.

### Lane D: Materials, manufacturing, chemistry, and biotechnology

Priority sources: MDF, autonomous chemistry, AutoFlowS, polymer enzymes, synthetic biology, quantum bioimaging, digital twins, job families.

### Lane E: Energy, grid, quantum, nuclear, and security

Priority sources: GRID-C, AWARE, quantum networking, isotope work, nuclear batteries, AI security, public technology-transfer records.

Status: first direct-source pass completed for AWARE/grid resilience, quantum networking, isotope and nuclear-battery work, AI security, and Situ/Heartbeat technology transfer. GRID-C remains a lead where the underlying page has not been directly fetched.

### Lane F: Public history and obscure work

Priority sources: OSTI, DOE technical reports, ORNL reports, public patents, historical archives, public software records, and primary papers.

## Pass order

1. **Architecture pass:** establish common vocabulary and shared layers.
2. **Project pass:** fetch every named project page and create dossiers.
3. **Software pass:** inspect public repositories individually. Do not infer from catalog presence.
4. **Facility/data pass:** map instruments, user facilities, data types, and public access boundaries.
5. **People/jobs pass:** separate authorship, job descriptions, team membership, and leadership claims.
6. **Connection pass:** add only source-backed or explicitly labeled inferred edges.
7. **Reconstruction pass:** attach safe local study paths after the public system is understood.
8. **Audit pass:** verify every concrete claim has a fetched URL, supporting quote/data, and fetch date.

## Promotion rules

- Search results are discovery leads only.
- A fetched primary source can support a DIRECT claim.
- Two independent primary sources can support a CORROBORATED claim.
- A cross-source connection is INFERRED unless a source explicitly states it.
- A job posting reveals a role's stated responsibilities, not necessarily completed project work.
- A project proposal reveals intended work, not a deployment result.
- A catalog listing reveals a public discovery surface, not a complete software estate or production status.
- Blocked, private, classified, export-controlled, PHI, PII, OUO, UCI, UCNI, NDA, and vendor-proprietary material stays out of scope.

## Acceptance criteria for the complete guide

- Every project dossier has a source URL and evidence label.
- Every facility, software, role, and researcher relationship points to a source or is marked inferred.
- Every source record preserves a supporting quote or data point and fetch date.
- Unknowns are listed instead of filled from plausible assumptions.
- The guide distinguishes public research architecture from local reconstruction.
- The atlas is useful without access to ORNL systems, credentials, private datasets, or restricted software.
- The registry and guide agree on identifiers and evidence state.


## Completed bounded batch, 2026-11-10

The [workflow software batch](../research/2026-11-10-workflow-systems/README.md) deepened Flowcept, Zambeze, INTERSECT SDK, and DataFed through pinned repository inspection and a second verification sweep. It adds a runnable, dependency-free local provenance experiment and a public-registry context query command. This completes a software-contract slice of lanes A/C; it does not complete all repository review, staff mapping, or other research lanes. Prioritized follow-ups are in the [integrated dossier](project-dossiers/workflow-software-and-local-reconstruction.md).
