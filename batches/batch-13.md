# Batch 13: 2025-2026 releases and engineering depth (closed: 5 of 5 verified)

Opened 2026-11-11. Closed 2026-11-11: all five briefs passed two fact-check sweeps (RULES 11).

## Why this batch
The catalog already covered 69 projects. This batch chose depth over count, and it fills two gaps.
- **Uncataloged projects.** ADIOS2 is cited across the repo but had no brief. A search of github.com/ORNL for repositories created since 2025 found newer public releases with no coverage: DEDFoam, ChatHPC and MATEY. Celeritas came up as a major ORNL-originated GPU code with no mention anywhere.
- **Reuse.** There was no write-up of the reusable engineering ideas in the code. That became [lessons/engineering-patterns.md](../lessons/engineering-patterns.md).

## What was researched
- [ADIOS2](../projects/adios2.md): multi-institution scientific I/O library. ORNL is listed first, and the copyright reads ORNL and Contributors. The engine (BP5 files, SST streaming and others) is chosen at run time. [Signals](../signals/adios2.md).
- [Celeritas](../projects/celeritas.md): GPU Monte Carlo transport that offloads tracks from Geant4. It was originally developed by ORNL, FNAL, ANL and LBNL. Its ORANGE geometry engine is shared with Shift. [Signals](../signals/celeritas.md).
- [DEDFoam](../projects/dedfoam.md): directed-energy-deposition printing on OpenFOAM, released 2026-07, sponsored by EERE AMMTO per DOE CODE. [Signals](../signals/dedfoam.md).
- [ChatHPC](../projects/chathpc.md): LoRA-tuned Code Llama assistants for HPC libraries, plus the SC25 Kokkos artifact. [Signals](../signals/chathpc.md).
- [MATEY](../projects/matey.md): adaptive-tokenization transformers for physical fields, with Frontier-scale runs. [Signals](../signals/matey.md).
- [Engineering patterns](../lessons/engineering-patterns.md): 16 patterns with pinned code citations, covering 15 public repositories.

## How it was done
- Two research agents ran the discovery and reading pass (sweep 1): one did ADIOS2 and Celeritas, the other did DEDFoam, ChatHPC and MATEY. Each read cloned code, OSTI and DOE CODE records and papers. They wrote only their own brief and signals files, plus rows in `verification/not-found.md`.
- The coordinator ran sweep 2 independently. It re-fetched the load-bearing claims from raw GitHub at the pinned commits and from the OSTI API, re-read paper full text where a claim depended on it, and recounted commits on fresh clones of Celeritas and MATEY. The details are in each brief's Verification notes and in [verification/log.md](../verification/log.md).
- The coordinator also wrote the patterns guide from pinned code and the existing deep dives, and integrated the catalog, INDEX, LAB-TREE and connections map (Pass 33, links 226-241).
- Nothing was built, run or benchmarked. No systems were touched.

## What was verified
- Ownership under rule 13 passed for all five. ADIOS2, Celeritas, DEDFoam and MATEY have a copyright line plus an OSTI or DOE CODE record. ChatHPC has a UT-Battelle copyright, the main ORNL org, and the SC25 paper with ORNL as research org (no DOE CODE record).
- Sweep 2 made no factual corrections. One rule-16 correction: an OLCF allocation ID quoted from MATEY's job scripts was removed from the brief and the signals file.
- External links: there are 177 unique URLs across the five briefs, the five signals files, the patterns guide and this file, all checked with HTTP GET on 2026-11-11. 176 returned 200. The one 404 is intended, because it is the negative evidence that Celeritas has no conda-forge package. An HTTP 200 shows the page exists, not that the claim is true.
- Commit spot checks (rule 17): Celeritas 2,699 commits on all branches and MATEY 171, both exact matches, with exact per-year matches.

## Findings worth knowing
- **One geometry engine spans reactor and particle physics.** An ORNL reactor paper says ORANGE "is shared between Shift and the Celeritas MC code" (OSTI 3376506), and QIR-EE carries Celeritas-derived headers. This is the clearest code lineage across domains in the catalog so far (map 229-231).
- **DEDFoam is not an AdditiveFOAM fork.** The two target different OpenFOAM lines (OpenCFD versus the Foundation), and AdditiveFOAM's heat sources are an optional plugin (map 234).
- **ChatHPC's library evaluates on its training file**, and its built-in verify step is a near-exact text match. The paper's held-out test prompts are the evidence to cite, not the training metrics.
- **Two SNS repos have drifted.** While pinning code for the patterns guide, the post-processing agent turned out to document an `EXPRESS` per-instrument lane that the workflow manager's split list doesn't include (pattern A1).
- **The OLCF test harness command changed.** The interface after its October 2026 reorganization is `othctl`, which resolves the open question in the 2026-10-29 fact-check of that deep dive (pattern B1).
- **AI tools show up in commit history.** Commit trailers from AI coding tools first appear in 2026 in both ADIOS2 and Celeritas, and Celeritas ships agent-instruction files (signals files). Read: lab teams adopted AI coding tools during 2026. [INFERRED, medium]

## Still unknown
- Validation data behind DEDFoam's "validated" claim and its ML training set. Whether its AdditiveFOAM plugin builds across OpenFOAM lines.
- Whether any experiment runs Celeritas in production. No source says so.
- Public data for ChatHPC's non-Kokkos assistants.
- Whether pretrained MATEY weights are public, and how much seed code remains.
- ADIOS2 download counts (rate-limited) and ORNL's true share of commits (personal email addresses make about 15% a lower bound).
- How the ORANGE sharing between Shift and Celeritas is organized.

## Investigate next
- A deep dive on the ORANGE lineage across Celeritas, Shift, SCALE and QIR-EE, under the reactor deep dive's controlled-distribution limits.
- A cross-repo contract check for the SNS queue names: what consumes `EXPRESS`?
- A small, reproducible local experiment from the patterns guide that measures a failure boundary rather than demoing a workflow. Candidates: D2's out-of-range surrogate behavior, or D5's SST queue policy under a slow reader.
