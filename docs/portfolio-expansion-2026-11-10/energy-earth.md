# Energy and Earth systems: four reproducible research boundaries

Independent public-source research, accessed **2026-11-10**. This chapter extends existing AutoBEM, Daymet, ExaGO and ReSolve briefs and the grid deep dive. It adds concrete data contracts, numerical failure boundaries, and bounded experiments. It does not claim ORNL affiliation or report a local execution of these tools.

## What connects these systems

[KNOWN] AutoBEM generates building-specific simulation models, Daymet estimates spatial weather, ExaGO formulates grid optimization, and ReSolve solves numerical linear systems. Their inputs and outputs occupy different layers, as documented separately in sources E01–E12 below. [INFERRED] They suggest a useful research progression: characterize an environment, model demand, optimize decisions, and verify the numerical work. This is a proposed comparison, not evidence of one deployed ORNL stack.

[UNKNOWN] No reviewed source establishes that AutoBEM consumes Daymet, that Model America building loads are connected to ExaGO, or that the current ExaGO installation necessarily uses ReSolve. The existing grid deep dive already documents the optional HiOp/ReSolve path. This chapter does not promote that optional connection to a mandatory dependency.

## 1. AutoBEM and Model America: an open artifact does not imply an open generator

[KNOWN, E01–E03] AutoBEM addresses the cost of preparing physics-based building simulations individually. Inputs include geographic building geometry and prototype-based assumptions; generation produces EnergyPlus/OpenStudio models, then simulation and post-processing estimate energy, emissions and retrofit consequences. Humans choose assumptions, weather, pricing and interventions. The generator is closed source, while an archive of generated models is publicly described. It is not a collection of measured building energy consumption.

```text
GIS geometry + building descriptors + prototypes
  -> AutoBEM generation (closed source)
  -> OpenStudio / EnergyPlus model artifacts
  -> selected weather and simulation
  -> consumption / emissions / retrofit screening
```

[KNOWN, E02] The April 2021 Model America archive describes 122,930,327 successful building simulations out of 125,714,640 detected buildings, or 97.8%. Its model artifacts target OpenStudio 3.1.0 and EnergyPlus 9.4 and are grouped into state/county ZIP archives. The generating metadata table is explicitly not included in the dataset. Descriptors include estimated construction year, prototype type, footprint, height, floor count, vintage and window ratios. Models embed roughly 3,000 inputs. The cited compute resource is Argonne Leadership Computing Facility, not evidence of a Frontier run.

[INFERRED, E02] Reproducibility should begin from a supplied model artifact and its simulator version, not a claim that the original geographic inference pipeline can be recreated exactly. Missing upstream metadata limits explaining why a particular assumption was assigned. A newer simulator may translate inputs; that translation becomes a new experimental step that needs its own recorded version and comparison.

[KNOWN, E03] The October 2026 paper abstract describes 151 conservation measures, localized prices, and typical/future weather scenarios. It reports short modeled paybacks for selected Phoenix building types and standards, and scenario-specific changes by 2100: electricity +11.3%, gas −32%. These are reported simulation results under the paper's scenario, not guaranteed savings or a national forecast. [UNKNOWN] The fetched abstract does not establish all assumptions needed to reproduce those percentages, so this chapter does not claim a full-paper audit.

[KNOWN, E01] DOE CODE reports throughput exceeding one million buildings per hour and validation against 15-minute observations for 178,000 buildings. [UNKNOWN] The record does not supply the hardware, cost allocation, error distributions, or per-building validation records needed to independently reproduce that performance/accuracy claim.

**Proposed experiment, not executed.** [INFERRED] Use one openly obtained model or an official simulator example, pin the relevant EnergyPlus version, and compare a baseline with one envelope/HVAC change under identical weather. Preserve input hashes, simulation warnings, unmet-load indicators, energy units and output comparison. Acceptance is a reproducible result with explained assumptions; it is not reproducing AutoBEM's national generator. The landing page names Globus for the archive; no login or bulk download was attempted. [UNKNOWN] A standalone archive license identifier is not established here; the page states free/open availability and an as-is warranty boundary [E02].

## 2. Daymet: weather forcing with an inspectable uncertainty product

[KNOWN, E04–E06] Daymet is an ORNL Environmental Sciences Division research product, distributed by ORNL DAAC. Daily station temperature and precipitation, elevation, horizon and land/water information enter an interpolation/extrapolation pipeline. Temperature and precipitation are handled separately; estimated radiation, vapor pressure and snow water equivalent are derived using theory and empirical relationships. Output is a 1-km grid with seven daily variables in CF-compatible netCDF. Humans select location, period, variables and application-specific error checks. These are estimates at uninstrumented locations, not direct measurements everywhere.

[KNOWN, E04] V4 chooses station search radii using precomputed station distances, replacing an older iterative station-density calculation. [KNOWN, E05] The data calendar retains February 29 but omits December 31 in leap years, preserving 365 records per year. Software and data versions are separate file attributes, and data are provisional. [INFERRED] Joining by an assumed generic 365-day calendar can misalign observations around leap years; record dates explicitly rather than relabeling every year's day 365 as December 31.

[KNOWN, E05] Shortwave radiation `srad` is a daylight-period mean in W/m². Daily energy in MJ/m² is `srad × dayl / 1,000,000`, where `dayl` is seconds of daylight. [INFERRED] Multiplying by 86,400 instead inflates energy whenever daylight is shorter than a full day. For a purely illustrative 200 W/m² and 36,000-second day, the correct result is 7.2 MJ/m², compared with 17.28 from that mistaken conversion. These numbers are arithmetic examples, not fetched Daymet observations.

[KNOWN, E06] The separate station-level product contains input observations and held-out predictions for `tmin`, `tmax`, and precipitation. Its specific protocol withholds a variable-station-year record, generates daily predictions, and excludes missing observations when calculating error statistics. It supports MAE, RMSE and bias by location or season. [INFERRED] This is a stronger starting point for a local uncertainty study than visually inspecting a weather map or quoting one favorable correlation plot. [UNKNOWN] These three-variable cross-validation records alone do not establish accuracy for every derived radiation, humidity or snow value.

**Proposed experiment, not executed.** [INFERRED] With one accessible station/year subset, calculate signed bias, MAE, RMSE and valid-day count separately by season. Test missing-data handling and leap-year date mapping. Pair a one-pixel weather series with ecological heat/rainfall indicators only after unit/calendar checks. This directly studies published outputs without pretending to reimplement Daymet's generator. [UNKNOWN] No generator-source license or separate dataset license identifier was established in this pass; cite the dataset DOI and check its current terms before redistribution. ORNL DAAC distribution does not by itself prove that every access route is anonymous [E05–E06].

## 3. ExaGO OPFLOW: optimizing a model requires preserving its constraints

[KNOWN, E07–E08] ExaGO exposes different applications for single-period, multi-period, contingency and stochastic optimization. OPFLOW's default objective minimizes generation cost with AC network balance, line-flow, generation-capacity and voltage constraints. A human supplies the network, chooses model/solver combinations and interprets feasibility and output. This is mathematical analysis; no reviewed evidence here establishes utility operation or a deployed control service.

[KNOWN, E08] OPFLOW accepts MATPOWER network cases via `-netfile`, defaults to a nine-bus case, and supports printed or saved results. The options table includes MATPOWER/JSON output configuration, optimization tolerance, load-loss variables, power imbalance, line-flow exclusions and penalty terms. [INFERRED] A cheaper objective after permitting load loss or removing line limits is not an improved solution to the original problem. An experiment manifest must record these toggles, not only network filename and final cost.

[KNOWN, E07] Ipopt and HiOp support different applications; security/stochastic cases using HiOp still require Ipopt for the base problem. [KNOWN, E08] The OPFLOW page distinguishes model/solver compatibility and hybrid versus GPU modes. [UNKNOWN] The page says HIOPSPARSE is CPU-only, while broader project descriptions emphasize GPU capability. Treat that as a version-specific documentation constraint requiring source/build inspection before selecting an accelerator path, rather than assuming every solver runs on a GPU.

**Proposed experiment, not executed.** [INFERRED] On the shipped small network, compare identical demand with line limits enforced versus deliberately relaxed. Record feasibility status, total objective, generation limits, power balance, line loading and optional unmet demand. Acceptance requires explaining why results change. A synthetic stress test needs no real utility network data. The published source is available; its license is a custom UT-Battelle grant with notices and acknowledgment requirements, rather than something safely reduced to an unexamined standard-license badge [E12].

## 4. ReSolve: reusable structure and verified accuracy matter more than a fast isolated solve

[KNOWN, E09–E11] ReSolve originated in the ExaSGD/ECP effort to solve sequences of sparse linear systems from simulation and optimization. Each system supplies a matrix and right-hand side; direct/iterative solver components yield a solution. Repeated systems can share the locations of nonzero entries while their numerical values change. CPU symbolic analysis and reusable workspaces avoid repeated setup; GPU refactorization and refinement handle later systems. The library offers CPU, CUDA and HIP backends. It is not the AC power-flow model or the full nonlinear optimizer.

[KNOWN, E10] Direct-solver lifecycle includes symbolic analysis, numerical factorization, optional refactorization setup, solve and subsequent refactorization. Reusing analysis is conditional on unchanged sparsity. If structure changes, the caller must reallocate and redo analysis/factorization; symbolic nonzeros should remain stored even when numerically zero. GPU users must synchronize memory explicitly. [INFERRED] Dropping small entries during preprocessing or modifying a host array without synchronizing can break assumptions independently of the mathematical solver's quality.

[KNOWN, E11] The paper explains why constrained optimization generates ill-conditioned KKT systems. Its approach reuses a CPU-derived pivot structure, performs subsequent numerical refactorization on accelerators, and applies FGMRES-based iterative refinement with LU factors as a preconditioner. It reports outperforming a CPU MA57 baseline in its studied application/standalone settings. [UNKNOWN] No universal speedup factor or cross-machine ranking is asserted here. The paper explicitly distinguishes isolated linear-system timings from behavior in the surrounding optimizer; the two are not interchangeable performance claims.

**Proposed experiment, not executed.** [INFERRED] Pin one public matrix sequence, compare fresh factorization with structure-reusing solves, and measure total setup, transfer, factorization, solve and refinement costs separately. Independently calculate residual/backward error for every solution, then intentionally change sparsity to test reanalysis handling. Report CPU and GPU configurations separately. A local arithmetic demonstration may teach residual checking but cannot substantiate ReSolve GPU performance. The official guide links public NREL test matrices; no download/build occurred [E10]. The actual license includes acknowledgment and derivative-notice obligations [E12].

## Connections to promote, keep conditional, or leave unknown

| Connection | Evidence boundary | Useful next question |
|---|---|---|
| AutoBEM → OpenStudio/EnergyPlus | [KNOWN] Model generation and archived target versions explicitly stated [E02–E03] | Can one archived model be replayed without silent version conversion? |
| Daymet → ecological weather forcing | [KNOWN] Stated application of the distributed product [E04–E05] | Which seasonal uncertainty dominates a chosen downstream indicator? |
| Daymet → E3SM | [KNOWN] E3SM support of algorithm development stated in E05 acknowledgment; [UNKNOWN] a particular ELM experiment's forcing configuration | Find a publication/configuration naming Daymet files, rather than infer dependency from funding. |
| AutoBEM ↔ Daymet | [UNKNOWN] No direct pipeline established by reviewed sources | Do not present a proposed daily-weather adapter as existing ORNL implementation. |
| ExaGO → optimization solvers | [KNOWN] Ipopt/HiOp interfaces and compatibility restrictions [E07–E08] | Which built solver/options actually enforce the intended constraints? |
| ReSolve ↔ grid optimization | [KNOWN] ExaSGD origin and paper's ACOPF context [E09–E11]; current ExaGO use is configuration-dependent | Benchmark whole optimization and independent residuals, not only inner kernels. |

## Source ledger

All sources below were read directly, not accepted from search highlights. Access date for every row: **2026-11-10**. Short quotes are exact evidence anchors, not substitutes for the summaries above. Mutable repository files were pinned where available.

| ID | Source, publisher, date/version | Exact short excerpt and location | Supports / limitation |
|---|---|---|---|
| E01 | [AutoBEM DOE CODE 115947](https://www.osti.gov/doecode/biblio/115947), DOE OSTI, release 2023-11-15 | “Project Type:”; “Closed Source” (metadata fields) | ORNL research organization, closed generator, throughput/validation claims. No reproducible benchmark details. |
| E02 | [Model America](https://doi.ccs.ornl.gov/dataset/9e968129-1ca9-5a71-93fa-24f009132a3a), ORNL Constellation, release 2021-04-14, DOI 10.13139/ORNLNCCS/1774134 | “which is not included in this dataset” (Description, metadata paragraph) | Artifact counts, upstream-data exclusion, simulator versions, as-is/open statement, ALCF credit. No archive downloaded. |
| E03 | [AutoBEM scalable framework](https://www.osti.gov/biblio/3740812), OSTI journal record, 2026-10-01 | “prototype-based assumptions” (abstract) | EnergyPlus/OpenStudio generation, interventions and scenario results. Abstract-only analysis. |
| E04 | [Daymet overview](https://daymet.ornl.gov/overview), ORNL, undated | “two separate workflows” (Processing) | Inputs, interpolation, derived variables and units. Narrative page is not a source-code release. |
| E05 | [Daymet Daily V4 guide](https://daac.ornl.gov/DAYMET/guides/Daymet_Daily_V4.html), ORNL DAAC, documentation revision 2024-06-17 | “December 31 is discarded” (The Daymet Calendar) | Calendar, radiation conversion, revision attributes, ORNL scope, E3SM funding. Historical file-count/year examples are not current inventory. |
| E06 | [Daymet V4 station cross-validation](https://daac.ornl.gov/DAYMET/guides/Daymet_V4_Stn_Level_CrossVal.html), ORNL DAAC, revision 2024-06-17, DOI 10.3334/ORNLDAAC/1850 | “dropping that record from the input station list” (Application and Derivation) | Held-out variable-station-year methodology, missing-value handling, paired observations. No numerical analysis performed here. |
| E07 | [ExaGO README](https://github.com/ORNL/ExaGO), ORNL, mutable develop branch | “not all applications can utilize all solvers yet” (solver compatibility) | Application and solver roles, restrictions, public code. No installation verified. |
| E08 | [OPFLOW at inspected commit](https://github.com/ORNL/ExaGO/blob/43726da124c9d8fb092446ac4f1cc36fe00c4b7f/docs/web/opflow.md), ORNL, commit inspected 2026-11-10 | “Ignore line flow constraints” (Options table) | MATPOWER input, constraints/toggles, compatibility and execution modes. Documentation may lag implementation. |
| E09 | [ReSolve developer introduction](https://resolve.readthedocs.io/en/latest/doxygen/html/index.html), ReSolve documentation, undated | “same sparsity pattern” (introductory design explanation) | ExaSGD history, data/workspace abstractions and backend design. Not benchmark evidence. |
| E10 | [ReSolve User Guide at inspected commit](https://github.com/ORNL/ReSolve/blob/c2ccbca565bc3c2e3f4db48a7fe138df406f9e74/docs/sphinx/user_guide/index.rst), ORNL, commit inspected 2026-11-10 | “the examples/tests are correct” (General API Description) | Lifecycle, structure and synchronization preconditions; old clone URL versus current GitHub home. Prefer examples/tests if docs conflict. |
| E11 | [Iterative Methods preprint](https://arxiv.org/html/2401.13926), authors/arXiv v1, 2024-01-25; [published ORNL record](https://impact.ornl.gov/en/publications/iterative-methods-in-gpu-resident-linear-solvers-for-nonlinear-co/), Parallel Computing 123, March 2025, DOI 10.1016/j.parco.2024.103123 | “reusing the symbolic analysis and pivot sequence” (preprint §1.3); “Published - Mar 2025” (ORNL record) | Refactorization/refinement method and tested context; authorship includes ORNL. Preprint is not asserted identical to published version. |
| E12 | [ReSolve LICENSE](https://github.com/ORNL/ReSolve/blob/c2ccbca565bc3c2e3f4db48a7fe138df406f9e74/LICENSE); [ExaGO LICENSE](https://github.com/ORNL/ExaGO/blob/43726da124c9d8fb092446ac4f1cc36fe00c4b7f/LICENSE), repository copyright holders, 2023/2026 headers | “must include the following acknowledgment” (condition 3, each file) | Actual custom license text read. No standard SPDX equivalence asserted. |

## Sweep 2: verification, repair and stopping boundary

[KNOWN, method] Sweep 1 read existing coverage matrix, project briefs and grid-connections deep dive, then fetched the primary sources above. Two targeted searches requested Daymet calendar/uncertainty documentation and ReSolve refinement literature, yielding four leads each. All used claims came from subsequent full-page retrieval or raw repository content.

[KNOWN, method] Sweep 2 re-read this synthesis against the retrieved content and re-fetched the AutoBEM metadata, Model America, 2026 abstract, both Daymet guides, ReSolve design introduction and ExaGO README. Raw OPFLOW/User Guide sources were independently fetched again at API-resolved commits. Checked literal occurrences of the constraint, sparsity and synchronization anchors. License texts were read in full. No clone, credentials, external mutation, installed dependency, data download or experiment execution was needed.

Repairs and boundaries:

- [KNOWN] Model America already had a 2021 release; the 2026 abstract's future-tense availability wording must not be used to claim first release in 2026 [E02–E03].
- [KNOWN] Daymet guide examples include older coverage dates and file counts despite the rolling annual product description. This chapter avoids treating those historical counts as live totals [E05].
- [KNOWN] The ReSolve guide retains an older GitLab clone command despite declaring the current GitHub home. No access to that host was attempted; a command in documentation is not evidence that all endpoints are publicly usable [E10].
- [UNKNOWN] Generic ExaGO GPU support does not resolve every solver/model compatibility detail. Preserve the version-specific restriction until implementation/examples establish otherwise [E07–E08].
- [KNOWN] An initially requested ExaGO `docs/opflow.md` extraction returned CRAWL_NOT_FOUND. The public repository tree identified the actual `docs/web/opflow.md`, which was fetched successfully. A ReSolve examples-directory extraction also failed; the public User Guide supplied the lifecycle without inventing example-file contents.
- [UNKNOWN] Searches/readings did not establish a direct Daymet/AutoBEM pipeline, a specific Daymet/ELM forcing run, a complete AutoBEM generator release, or a universally applicable ReSolve speedup. This is bounded negative evidence, not proof of nonexistence. The search queries were “Daymet version 4 dataset 365 days leap year December 31 cross validation ORNL DAAC data guide” and “ReSolve GPU iterative refinement refactorization power grid KLU FGMRES ORNL linear solver paper”; they were targeted method searches, not exhaustive searches for every missing connection.

[INFERRED] Additional literature can deepen calibration and performance but is unlikely to change the core distinctions: open generated artifacts versus closed generation; estimated weather versus observations and held-out validation; constrained optimization versus relaxed feasibility; inner linear solve versus whole-application performance. The highest-value next execution is the small Daymet uncertainty/calendar study, followed by one version-pinned building model and one constraint-preserving OPFLOW comparison. These remain proposed experiments, not completed results.
