# Computing and instruments: streams, graph learning, quantum tensors, and microscopy data

Research/access date: 2026-11-10, America/New_York. Independent public-source research. No upstream code was installed, cloned, executed, or modified. Scope: four connected technology families, treating TNQVM and ExaTN as a documented two-layer family. Existing ExaTN, TNQVM, XACC, HydraGNN briefs and the coverage matrix were read first; this packet deepens algorithms and interfaces rather than repeating their repository inventory. Existing SNS/test-harness case studies are outside this batch.

## What this adds to the portfolio

[INFERRED] The strongest reusable connection across these systems is the treatment of a scientific array as more than bytes: ADIOS2 attaches variable/step semantics, HydraGNN turns atomic structures into learning data, ExaTN treats dimensions as contraction indices, and sidpy gives dimensions physical meaning. That is an architectural comparison, not a claim that these systems share a runtime or exchange data directly. Source-backed dependency edges are listed separately below.

[KNOWN] Four concrete discoveries change how a local reconstruction should work: SST's blocking queue is not inherently durable when no readers are connected; HydraGNN's inspected ADIOS example uses BP5 files, not demonstrated SST streaming; TNQVM exposes an accuracy/memory tradeoff through MPS truncation; microscopy analysis preserves axis meaning in a Dask-derived dataset instead of requiring every step to write USID/HDF5. Sources: [C01](https://github.com/ornladios/ADIOS2/blob/2d6d28a519905ac2e33ef4e91a308139c829d7f3/docs/user_guide/source/engines/sst.rst), [C05](https://github.com/ORNL/HydraGNN/blob/d49d934403f0cc3276750004c8dfbf3a502a10f1/examples/multidataset_hpo_sc26/inference_fused_write_adios.py), [C12](https://github.com/ORNL-QCI/tnqvm/blob/a70eed190a4448dbe3dae94189d066ac694dc798/tnqvm/visitors/exatn-mps/ExaTnMpsVisitor.cpp), [C20](https://pycroscopy.github.io/pycroscopy/about.html).

## 1. ADIOS2/SST: direct application streaming with scientifically consequential queue policy

[KNOWN] An application writes named multidimensional variables within steps. SST lets reader applications request selections of those variables directly from writers. Reader and writer MPI rank counts can differ; multiple reader cohorts can attach. Calls to BeginStep/EndStep delimit atomic steps, so a dropped step is dropped as a whole rather than partially delivered. This is in-situ/in-transit scientific data exchange, not a persistent message ledger. [C01](https://github.com/ornladios/ADIOS2/blob/2d6d28a519905ac2e33ef4e91a308139c829d7f3/docs/user_guide/source/engines/sst.rst).

```text
simulation ranks -> named arrays in a step -> writer-side buffered step
                         -> metadata/control -> reader selections
                         -> chosen data transport -> analysis/ML reader ranks
```

[KNOWN] Three implementation details matter locally. First, default rendezvous waits for one reader, and setting it to zero permits the writer to run alone. Second, default file registration exchanges connection information through a small shared file even though payloads stream over the network; saying SST uses no files whatsoever is too broad. Third, batching deferred Get operations avoids repeated many-writer communication that serial synchronous Gets may incur. The selected transport depends on build/platform availability. [C01](https://github.com/ornladios/ADIOS2/blob/2d6d28a519905ac2e33ef4e91a308139c829d7f3/docs/user_guide/source/engines/sst.rst).

[KNOWN] The inspected queue documentation makes loss conditional. With active readers and a finite queue, Block waits for reader consumption, and the slowest reader can govern progress. With no active readers and ReserveQueueLimit=0, submitted steps are immediately discarded even if QueueFullPolicy is Block. Under Discard with active readers, the newest submitted step is dropped; without readers, the documented eviction rule drops oldest queued data. ReserveQueueLimit can retain history for late readers. FirstTimestepPrecious preserves initial context but counts against QueueLimit. These distinctions are explicit parameters, not optional monitoring trivia. [C01](https://github.com/ornladios/ADIOS2/blob/2d6d28a519905ac2e33ef4e91a308139c829d7f3/docs/user_guide/source/engines/sst.rst).

[KNOWN] The 2024 SST paper identifies ORNL-affiliated authors and separates a control plane from data planes. Its Frontier plasma-simulation-to-ML benchmark reports perceived aggregate throughput of 20–30 TB/s for MPI and about 20 TB/s for libfabric, comparing that with a 10 TB/s theoretical filesystem limit. A faster libfabric submission strategy at 4096 nodes did not scale across the full machine without throttling. These are benchmark outcomes for specified runs, not laptop expectations, universal speedups, or today's facility status. [C02](https://arxiv.org/html/2410.00178v1).

[KNOWN] The pinned ADIOS2 license is Apache-2.0 and carries UT-Battelle copyright. The inspected default-branch snapshot is `2d6d28a519905ac2e33ef4e91a308139c829d7f3`, whose commit timestamp is 2026-11-11T01:31:31Z (2026-11-10 local date). It is a research snapshot, not an installed release. [C03](https://github.com/ornladios/ADIOS2/blob/2d6d28a519905ac2e33ef4e91a308139c829d7f3/LICENSE).

[INFERRED] Best local study: feed a deterministic stream whose last steps contain rare events into a slow consumer; compare Block, newest-drop, and late-reader retention on step IDs, event recall, peak queue length, and producer waiting. This would test how data-loss policy changes scientific conclusions, not reproduce SST's networking or throughput. No such experiment was run in this research track. [UNKNOWN] Durable replay guarantees and host-specific transport availability require separate upstream execution; this packet does not infer them from parameter names. [C01](https://github.com/ornladios/ADIOS2/blob/2d6d28a519905ac2e33ef4e91a308139c829d7f3/docs/user_guide/source/engines/sst.rst).

## 2. HydraGNN's ADIOS path: a verified bridge from scientific data movement into AI

[KNOWN] The existing HydraGNN brief established graph learning on atomistic data. New source inspection narrows the ADIOS connection: its ADIOS backend imports ADIOS2 optionally and checks whether the loaded build supports MPI. A serial ADIOS build is rejected for multi-rank use. The module also distinguishes API access across ADIOS versions. This is executable dependency code, stronger than a shared-paper/topic connection. [C04](https://github.com/ORNL/HydraGNN/blob/d49d934403f0cc3276750004c8dfbf3a502a10f1/hydragnn/data/adiosdataset/_backend.py).

[KNOWN] A pinned fused-inference example defines atom types, three coordinate arrays, three force arrays, formation energy, and branch weights, writing one atomistic structure per ADIOS step. It explicitly selects BP5 and writes per-GPU outputs toward node-local storage. Variables are resized for the current number of atoms. The output is a structured, step-based file series, not evidence of SST use by this example. Reference dimensions and scientific units are part of the example's contract. [C05](https://github.com/ORNL/HydraGNN/blob/d49d934403f0cc3276750004c8dfbf3a502a10f1/examples/multidataset_hpo_sc26/inference_fused_write_adios.py).

```text
atomistic structures -> trained HydraGNN/branch-weight inference
                    -> atom IDs + coordinates + forces + energy + weights
                    -> one structure per BP5 step -> later analysis/readback
```

[INFERRED] The engineering opportunity is to keep atom/coordinate/force alignment invariant while changing the data carrier. A small local fixture can test variable atom counts and mismatched array lengths before considering online streaming. Changing BP5 to SST would additionally require concurrent reader/writer processes, step cadence, and explicit loss/backpressure policy; ADIOS API similarity alone does not demonstrate a tested HydraGNN streaming configuration. [UNKNOWN] Exact performance and accuracy of the pinned fused-model example were not established here, and model weights/training provenance were not retrieved. [C04](https://github.com/ORNL/HydraGNN/blob/d49d934403f0cc3276750004c8dfbf3a502a10f1/hydragnn/data/adiosdataset/_backend.py), [C05](https://github.com/ORNL/HydraGNN/blob/d49d934403f0cc3276750004c8dfbf3a502a10f1/examples/multidataset_hpo_sc26/inference_fused_write_adios.py).

## 3. TNQVM + ExaTN: from circuit description to bounded numerical contractions

[INFERRED] Plain-language model: a tensor is an array with several axes. A tensor network represents a large calculation as smaller arrays sharing indices; contraction multiplies and sums along those shared indices. An MPS (matrix product state) arranges the pieces as a chain. Its bond dimension limits how much correlation neighboring pieces can retain. SVD (singular value decomposition) splits a combined array back into factors; discarding small components saves memory while introducing an accuracy tradeoff. This explanation interprets the numerical operations exposed by [TNQVM's MPS visitor](https://github.com/ORNL-QCI/tnqvm/blob/a70eed190a4448dbe3dae94189d066ac694dc798/tnqvm/visitors/exatn-mps/ExaTnMpsVisitor.cpp).

[KNOWN] XACC is the required programming frontend; TNQVM supplies a circuit simulator plugin; ExaTN is an optional numerical backend, not the quantum frontend. TNQVM's README specifies the ExaTN visitor selection and MPI prerequisites. Its build requires XACC and C++17/Fortran. The source header credits UT-Battelle. This establishes a real chain of dependencies rather than a same-organization relationship. [C09](https://github.com/ORNL-QCI/tnqvm/blob/a70eed190a4448dbe3dae94189d066ac694dc798/README.md), [C10](https://github.com/ORNL-QCI/tnqvm/blob/a70eed190a4448dbe3dae94189d066ac694dc798/CMakeLists.txt).

[KNOWN] ExaTN distinguishes declarations from execution: tensor/network descriptors do not allocate numerical storage, while the executive API allocates and processes values. External array initialization must follow column-major storage. Its network output gathers the uncontracted dimensions. CPU, BLAS, optional MPI and NVIDIA accelerator build paths are documented separately. A tensor-network contraction is not necessarily a compressed quantum state; the chosen representation and operation determine memory use. [C06](https://github.com/ORNL-QCI/exatn/blob/c528f7ec7323ab5f4485b85efcefa016c32e1a2d/README.md).

[KNOWN] TNQVM's MPS implementation exposes `svd-cutoff` and `max-bond-dim`. It calls ExaTN's SVD decomposition after merging tensors around a two-qubit operation. The paper explains contraction, decomposition, and truncation, with automatic nearest-neighbor conversion through SWAP insertion. It also demonstrates a selected amplitude of a 53-qubit circuit: one projected output, not the full state vector or every measurement outcome. [C11](https://arxiv.org/pdf/2104.10523), [C12](https://github.com/ORNL-QCI/tnqvm/blob/a70eed190a4448dbe3dae94189d066ac694dc798/tnqvm/visitors/exatn-mps/ExaTnMpsVisitor.cpp).

```text
XACC circuit -> TNQVM visitor -> gates as tensors
               -> exact selected contraction OR MPS gate update
               -> ExaTN tensor operations / SVD / contraction
               -> amplitude, expectation, or simulated measurements
```

[KNOWN] ExaTN's 2022 paper reports a specific 3:1 MERA fragment contracting on Summit in 77.11 seconds at 4 nodes and 3.96 seconds at 128 nodes; reported per-GPU performance declines from 10.743 to 7.333 TFlop/s across those endpoints. Its separate 53-qubit depth-14 comparison is for one amplitude with identified hardware and numerical precision. These demonstrations establish selected numerical workloads, not arbitrary circuit tractability or exascale hardware equivalence on a desktop. [C08](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2022.838601/full).

[KNOWN] ExaTN's inspected BSD-3-Clause license carries UT-Battelle copyright. TNQVM's README states BSD-3-Clause but its tree has no standalone LICENSE file; this repeats and reconfirms the existing brief's limitation. ExaTN's README labels macOS support poor and describes native compiler, Fortran, BLAS, optional CUDA/cuQuantum, and external install layout. A source snapshot's claimed build path is not a successful modern build. [C09](https://github.com/ORNL-QCI/tnqvm/blob/a70eed190a4448dbe3dae94189d066ac694dc798/README.md), [C10](https://github.com/ORNL-QCI/tnqvm/blob/a70eed190a4448dbe3dae94189d066ac694dc798/CMakeLists.txt), [C06](https://github.com/ORNL-QCI/exatn/blob/c528f7ec7323ab5f4485b85efcefa016c32e1a2d/README.md), [C07](https://github.com/ORNL-QCI/exatn/blob/c528f7ec7323ab5f4485b85efcefa016c32e1a2d/LICENSE).

[INFERRED] Most valuable local comparison: a small Bell/GHZ or shallow nearest-neighbor circuit, computed both as a dense state and as a deliberately truncated factorization, with normalization, expectation error, and retained bond dimension recorded. It would expose why “simulation completed” is weaker than “numerically adequate.” This is a proposed independent numerical study, not TNQVM benchmark reproduction. [UNKNOWN] Compatibility among today's XACC, ExaTN, compiler, and accelerator libraries remains untested. [C11](https://arxiv.org/pdf/2104.10523), [C12](https://github.com/ORNL-QCI/tnqvm/blob/a70eed190a4448dbe3dae94189d066ac694dc798/tnqvm/visitors/exatn-mps/ExaTnMpsVisitor.cpp).

## 4. Pycroscopy/sidpy: instrument data with explicit physical axes

[KNOWN] The ORNL-affiliated pycroscopy manuscript presents a common N-dimensional dataset implemented in sidpy, with concrete microscopy analysis examples. One workflow reads a vendor STEM image, crops it, applies sliding-window Fourier analysis, and factorizes texture using NMF (nonnegative matrix factorization, which separates data into additive weighted components); another fits scanning-probe current-voltage spectra in parallel, optionally using cluster-center fits to generate starting parameters. The banded texture's interpretation as oxygen-vacancy related is presented as a suggestion, not proved causation. The published demonstrations do not establish autonomous instrument control. [C13](https://www.osti.gov/servlets/purl/2478374).

[KNOWN] Current sidpy code subclasses Dask Array. Dataset attributes include quantity, units, source, data type, additional metadata, and original metadata. Dimension objects hold coordinate values, quantity, units, and a physical dimension type such as spatial or spectral. `set_dimension` checks that axis length matches data shape; it does not demonstrate that the supplied calibration is physically correct. Unknown dimension types are mapped to UNKNOWN with a warning rather than universally rejected. [C14](https://github.com/pycroscopy/sidpy/blob/06105426f780ed8c0da5054589cc7d22afbfcf85/sidpy/sid/dataset.py), [C15](https://github.com/pycroscopy/sidpy/blob/06105426f780ed8c0da5054589cc7d22afbfcf85/sidpy/sid/dimension.py).

[KNOWN] The pinned SidFitter takes a sidpy dataset plus a user-specified model, optional guess function, chosen dimensions and worker settings. It schedules SciPy curve fitting using Dask delayed calls and supports optional k-means-based starting parameters. The actual execution method inspected is `do_fit`, whereas the older manuscript describes a `fit()` call. Treat manuscript examples as historical behavior and inspect the pinned API before writing runnable examples. [C16](https://github.com/pycroscopy/sidpy/blob/06105426f780ed8c0da5054589cc7d22afbfcf85/sidpy/proc/fitter.py).

```text
vendor microscopy file -> SciFiReaders -> sidpy.Dataset
        -> physical coordinates + original metadata + lazy array
        -> image transforms / parallel user-model fits
        -> components, parameter maps, optional covariance/fitted values
        -> explicitly chosen persistence package
```

[KNOWN] The inspected pycroscopy manifest directly depends on sidpy and SciFiReaders. Project documentation distinguishes the legacy USID/HDF5-centric package (last legacy version 0.60.7) from newer sidpy.Dataset exchange and separately chosen pyUSID/pyNSID persistence. sidpy's license is MIT; pycroscopy's manifest declares MIT. ORNL provenance comes from the paper's affiliations, not from a GitHub organization name or the MIT copyright holder. [C17](https://github.com/pycroscopy/pycroscopy/blob/90e2d232acc9da634131c1793f082a70a04a3297/pyproject.toml), [C19](https://github.com/pycroscopy/sidpy/blob/06105426f780ed8c0da5054589cc7d22afbfcf85/LICENSE), [C20](https://pycroscopy.github.io/pycroscopy/about.html).

[INFERRED] Best local study: synthetic spectral image `(x, y, bias)` with known model parameters, realistic axis coordinates and controlled noise; fit parameter maps and check residuals and covariance, while deliberately swapping or miscalibrating axes. This tests the difference between shape-valid data and scientifically meaningful metadata. [UNKNOWN] The source code alone cannot establish calibration accuracy, vendor-reader completeness, or equivalence to any ORNL facility workflow. [C13](https://www.osti.gov/servlets/purl/2478374), [C14](https://github.com/pycroscopy/sidpy/blob/06105426f780ed8c0da5054589cc7d22afbfcf85/sidpy/sid/dataset.py), [C15](https://github.com/pycroscopy/sidpy/blob/06105426f780ed8c0da5054589cc7d22afbfcf85/sidpy/sid/dimension.py), [C16](https://github.com/pycroscopy/sidpy/blob/06105426f780ed8c0da5054589cc7d22afbfcf85/sidpy/proc/fitter.py).

## Connection matrix: code edges versus research analogies

| Connection | Evidence boundary | Practical implication |
|---|---|---|
| HydraGNN -> ADIOS2 | [KNOWN] direct import and typed writer calls, C04–C05 | Concrete AI/data-system bridge; inspected example is BP5 |
| TNQVM -> XACC | [KNOWN] required CMake dependency, C09–C10 | Cannot call TNQVM a standalone circuit frontend |
| TNQVM -> ExaTN | [KNOWN] optional build path and direct SVD calls, C09/C12 | Real circuit-to-tensor numerical bridge |
| pycroscopy -> sidpy/SciFiReaders | [KNOWN] manifest dependencies, C17 | Shared dataset representation connects ingestion and analysis |
| sidpy -> Dask/SciPy/scikit-learn | [KNOWN] inheritance/imports and fitting code, C14/C16/C18 | Lazy arrays and fitting dependencies, not a national-lab service |
| ADIOS2 -> microscopy ecosystem | [UNKNOWN] no direct adapter found in inspected artifacts | Do not add a code-dependency edge |
| ExaTN -> sidpy tensor analysis | [UNKNOWN] no direct dependency established | “Tensor” and multidimensional data are insufficient linkage |
| All four families -> reproducibility experiments | [INFERRED] common pressure to preserve representation semantics | Comparison only; independent reconstruction choices must be labeled |

## Sweep 2: verification, corrections, and missing evidence

[KNOWN] This packet's second sweep re-fetched all 20 ledger sources and confirmed all 20 short excerpts/code data (PDF whitespace and hosted HTML text normalized where needed). It reread the actual pipeline descriptions rather than relying on prior Atlas brief summaries. Corrections preserved here: (1) Block is conditional on reader/retention state, not durability; (2) HydraGNN's inspected writer is BP5, not SST; (3) a 53-qubit selected amplitude is not a full-state simulation; (4) pycroscopy's modern object exchange is not universally USID/HDF5; (5) manuscript `fit()` and pinned `do_fit()` are not interchangeable; (6) quiet repositories are not called abandoned, and README build instructions are not called passed tests.

[UNKNOWN] Bounded not-found record, 2026-11-10: source inspection of ADIOS2's SST documentation, HydraGNN's ADIOS dataset/writer paths, TNQVM's ExaTN visitors, and sidpy/pycroscopy manifests did not establish a joint SST–sidpy adapter, ExaTN–sidpy dependency, or one ORNL deployment combining these families. Web searches `"SST" "sidpy"` and `"ExaTN" "sidpy"` returned no relevant primary integration evidence; the SST query produced unrelated chemical-name/package-list collisions, not scientific-streaming linkage. Such results are not proof of absence. TNQVM HTML arXiv v2 returned 404, so the accessible v1 PDF was read instead. No private GitLab CI links were followed; no facility endpoints, credentials, or network topology were investigated.

[INFERRED] Stopping boundary: public sources now support specific algorithm/data boundaries and genuine dependency edges. Further broad summaries add little; targeted work on numerical error, step loss, axis semantics, and a pinned upstream build would materially improve this portfolio. Hardware-specific performance, instrument physics, present deployment maturity, and modern cross-version compatibility stay unknown. This batch adds research evidence and feasible experiments; it does not claim those upstream experiments were performed.

## Dated source ledger

All sources accessed 2026-11-10 local time. [KNOWN] means directly read public primary material, not necessarily runtime verification. Quotes remain under 25 words per source file. Source publication dates are stated only where established; “pinned snapshot” is a revision boundary, not a file publication date.

### C01. ADIOS2 SST engine documentation

- [KNOWN] Publisher: ornladios contributors. Publication/revision date: snapshot 2026-11-11 UTC. Accessed: 2026-11-10.
- Primary URL: [ADIOS2 SST engine documentation](https://github.com/ornladios/ADIOS2/blob/2d6d28a519905ac2e33ef4e91a308139c829d7f3/docs/user_guide/source/engines/sst.rst). Section/path: SST engine and parameter descriptions.
- Short supporting excerpt/code datum: `timesteps submitted when there are no active readers will be immediately discarded.`.
- Supports: Step atomicity, rendezvous, queue policy, non-durable streaming. Limit: source-level evidence; upstream execution not performed.

### C02. Streaming Data in HPC Workflows Using ADIOS

- [KNOWN] Publisher: Eisenhauer et al., ORNL and collaborating institutions. Publication/revision date: 2024-09-30, arXiv v1. Accessed: 2026-11-10.
- Primary URL: [Streaming Data in HPC Workflows Using ADIOS](https://arxiv.org/html/2410.00178v1). Section/path: III architecture; IV-C performance.
- Short supporting excerpt/code datum: `The full-scale throughput reaches between 20 and 30 TB/s for MPI`.
- Supports: ORNL author affiliations; SST mechanism and bounded Frontier benchmark. Limit: source-level evidence; upstream execution not performed.

### C03. ADIOS2 license

- [KNOWN] Publisher: UT-Battelle and ADIOS2 contributors. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [ADIOS2 license](https://github.com/ornladios/ADIOS2/blob/2d6d28a519905ac2e33ef4e91a308139c829d7f3/LICENSE). Section/path: license body and copyright.
- Short supporting excerpt/code datum: `Copyright 2019 UT-BATTELLE, LLC`.
- Supports: Apache-2.0 and ORNL-tied copyright boundary. Limit: source-level evidence; upstream execution not performed.

### C04. HydraGNN ADIOS backend

- [KNOWN] Publisher: ORNL HydraGNN contributors. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [HydraGNN ADIOS backend](https://github.com/ORNL/HydraGNN/blob/d49d934403f0cc3276750004c8dfbf3a502a10f1/hydragnn/data/adiosdataset/_backend.py). Section/path: optional imports and _comm_args.
- Short supporting excerpt/code datum: `import adios2`.
- Supports: Actual ADIOS dependency and serial-versus-MPI runtime guard. Limit: source-level evidence; upstream execution not performed.

### C05. HydraGNN fused inference ADIOS writer

- [KNOWN] Publisher: ORNL HydraGNN contributors. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [HydraGNN fused inference ADIOS writer](https://github.com/ORNL/HydraGNN/blob/d49d934403f0cc3276750004c8dfbf3a502a10f1/examples/multidataset_hpo_sc26/inference_fused_write_adios.py). Section/path: module docstring; _open_adios_writer.
- Short supporting excerpt/code datum: `Each GPU writes a BP5 file where every ADIOS step is one atomistic structure.`.
- Supports: File-based BP5 path; atom identities, positions, forces, energy and branch weights. Limit: source-level evidence; upstream execution not performed.

### C06. ExaTN README

- [KNOWN] Publisher: ORNL-QCI ExaTN contributors. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [ExaTN README](https://github.com/ORNL-QCI/exatn/blob/c528f7ec7323ab5f4485b85efcefa016c32e1a2d/README.md). Section/path: Concepts and Usage; Dependencies; Mac OS X build.
- Short supporting excerpt/code datum: `declarative API calls do not allocate storage for tensors.`.
- Supports: Descriptor versus execution API; column-major arrays; native-build constraints. Limit: source-level evidence; upstream execution not performed.

### C07. ExaTN license

- [KNOWN] Publisher: UT-Battelle. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [ExaTN license](https://github.com/ORNL-QCI/exatn/blob/c528f7ec7323ab5f4485b85efcefa016c32e1a2d/LICENSE). Section/path: license header.
- Short supporting excerpt/code datum: `Copyright (c) 2017, UT-Battelle`.
- Supports: BSD-3-Clause and non-org-name institutional tie. Limit: source-level evidence; upstream execution not performed.

### C08. ExaTN: Scalable GPU-Accelerated High-Performance Processing of General Tensor Networks at Exascale

- [KNOWN] Publisher: Lyakh et al.; Frontiers in Applied Mathematics and Statistics. Publication/revision date: 2022-07-06. Accessed: 2026-11-10.
- Primary URL: [ExaTN: Scalable GPU-Accelerated High-Performance Processing of General Tensor Networks at Exascale](https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2022.838601/full). Section/path: 3.1 Table 1; 3.3.1 Table 3.
- Short supporting excerpt/code datum: `Performance of numerical evaluation of the 3:1 MERA fragment on Summit supercomputer.`.
- Supports: ORNL affiliations; measured contraction scaling and single-amplitude benchmark limits. Limit: source-level evidence; upstream execution not performed.

### C09. TNQVM README

- [KNOWN] Publisher: ORNL-QCI TNQVM contributors. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [TNQVM README](https://github.com/ORNL-QCI/tnqvm/blob/a70eed190a4448dbe3dae94189d066ac694dc798/README.md). Section/path: Installation; MPI execution; License.
- Short supporting excerpt/code datum: `TNQVM can be built with`.
- Supports: Actual optional ExaTN link, XACC prerequisite, MPI build options; README license statement. Limit: source-level evidence; upstream execution not performed.

### C10. TNQVM CMake build

- [KNOWN] Publisher: UT-Battelle. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [TNQVM CMake build](https://github.com/ORNL-QCI/tnqvm/blob/a70eed190a4448dbe3dae94189d066ac694dc798/CMakeLists.txt). Section/path: copyright header; build configuration.
- Short supporting excerpt/code datum: `find_package(XACC REQUIRED)`.
- Supports: ORNL tie by copyright, C++17/Fortran build and required XACC. Limit: source-level evidence; upstream execution not performed.

### C11. Tensor Network Quantum Virtual Machine for Simulating Quantum Circuits at Exascale

- [KNOWN] Publisher: Nguyen et al., ORNL and NVIDIA. Publication/revision date: 2021-04-21, arXiv v1. Accessed: 2026-11-10.
- Primary URL: [Tensor Network Quantum Virtual Machine for Simulating Quantum Circuits at Exascale](https://arxiv.org/pdf/2104.10523). Section/path: 3.2 MPS; 4.3 single amplitude; Fig. 9.
- Short supporting excerpt/code datum: `maximum entanglement bond dimension`.
- Supports: Gate merge/SVD/truncation method; 53-qubit single-amplitude demonstration; ORNL affiliations. Limit: source-level evidence; upstream execution not performed.

### C12. ExaTN MPS visitor

- [KNOWN] Publisher: TNQVM contributors. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [ExaTN MPS visitor](https://github.com/ORNL-QCI/tnqvm/blob/a70eed190a4448dbe3dae94189d066ac694dc798/tnqvm/visitors/exatn-mps/ExaTnMpsVisitor.cpp). Section/path: initialization around lines 259–273; SVD call near 1625.
- Short supporting excerpt/code datum: `exatn::decomposeTensorSVDLRSync(mergeContractionPattern)`.
- Supports: svd-cutoff and max-bond-dim options; explicit ExaTN numerical call. Limit: source-level evidence; upstream execution not performed.

### C13. A processing and analytics system for microscopy data workflows: the Pycroscopy ecosystem of packages

- [KNOWN] Publisher: Vasudevan et al.; ORNL manuscript via OSTI. Publication/revision date: Exact publication date not established from fetched OSTI manuscript. Accessed: 2026-11-10.
- Primary URL: [A processing and analytics system for microscopy data workflows: the Pycroscopy ecosystem of packages](https://www.osti.gov/servlets/purl/2478374). Section/path: author affiliations; Workflow examples 1 and 2; Fig. 3–4.
- Short supporting excerpt/code datum: `Our data model, termed the N-dimensional spectral imaging data format, is realized in pycroscopy’s sidpy package.`.
- Supports: ORNL tie; common dataset representation; STEM texture analysis and parallel spectral fitting. Limit: source-level evidence; upstream execution not performed.

### C14. sidpy Dataset implementation

- [KNOWN] Publisher: Pycroscopy contributors. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [sidpy Dataset implementation](https://github.com/pycroscopy/sidpy/blob/06105426f780ed8c0da5054589cc7d22afbfcf85/sidpy/sid/dataset.py). Section/path: Dataset class; from_array; set_dimension.
- Short supporting excerpt/code datum: `class Dataset(da.Array):`.
- Supports: Actual Dask inheritance, metadata, dimension length validation. Limit: source-level evidence; upstream execution not performed.

### C15. sidpy Dimension implementation

- [KNOWN] Publisher: Pycroscopy contributors. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [sidpy Dimension implementation](https://github.com/pycroscopy/sidpy/blob/06105426f780ed8c0da5054589cc7d22afbfcf85/sidpy/sid/dimension.py). Section/path: DimensionType; Dimension; dimension_type setter.
- Short supporting excerpt/code datum: `class Dimension(np.ndarray):`.
- Supports: Axis values, quantity, units and physical type; unknown type degrades to UNKNOWN. Limit: source-level evidence; upstream execution not performed.

### C16. sidpy SidFitter implementation

- [KNOWN] Publisher: Pycroscopy contributors. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [sidpy SidFitter implementation](https://github.com/pycroscopy/sidpy/blob/06105426f780ed8c0da5054589cc7d22afbfcf85/sidpy/proc/fitter.py). Section/path: constructor; do_fit; k-means priors.
- Short supporting excerpt/code datum: `def do_fit(self, **kwargs):`.
- Supports: User model/guess functions; delayed SciPy fits and optional cluster-based priors. Limit: source-level evidence; upstream execution not performed.

### C17. Pycroscopy package manifest

- [KNOWN] Publisher: Pycroscopy contributors. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [Pycroscopy package manifest](https://github.com/pycroscopy/pycroscopy/blob/90e2d232acc9da634131c1793f082a70a04a3297/pyproject.toml). Section/path: dependencies; project metadata.
- Short supporting excerpt/code datum: `"sidpy",`.
- Supports: Explicit pycroscopy to sidpy and SciFiReaders dependencies; MIT declaration. Limit: source-level evidence; upstream execution not performed.

### C18. sidpy package dependencies

- [KNOWN] Publisher: Pycroscopy contributors. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [sidpy package dependencies](https://github.com/pycroscopy/sidpy/blob/06105426f780ed8c0da5054589cc7d22afbfcf85/setup.py). Section/path: requirements; development status classifier.
- Short supporting excerpt/code datum: `dask-ml>=2025.1.0`.
- Supports: Python analysis-stack requirements; pre-alpha classifier is publisher metadata, not runtime evaluation. Limit: source-level evidence; upstream execution not performed.

### C19. sidpy license

- [KNOWN] Publisher: Pycroscopy contributors. Publication/revision date: pinned snapshot. Accessed: 2026-11-10.
- Primary URL: [sidpy license](https://github.com/pycroscopy/sidpy/blob/06105426f780ed8c0da5054589cc7d22afbfcf85/LICENSE). Section/path: license header.
- Short supporting excerpt/code datum: `MIT License`.
- Supports: Inspected license; institutional tie comes from paper, not this copyright. Limit: source-level evidence; upstream execution not performed.

### C20. Pycroscopy reimagined documentation

- [KNOWN] Publisher: Pycroscopy contributors. Publication/revision date: hosted documentation accessed 2026-11-10. Accessed: 2026-11-10.
- Primary URL: [Pycroscopy reimagined documentation](https://pycroscopy.github.io/pycroscopy/about.html). Section/path: Pycroscopy reimagined; Legacy package.
- Short supporting excerpt/code datum: `V 0.60.7 is the last version of the legacy iteration`.
- Supports: USID/HDF5 legacy versus sidpy.Dataset current object boundary. Limit: source-level evidence; upstream execution not performed.

## Inspected revision map

[KNOWN] Revisions were resolved from GitHub's public repository/commit API, then source files fetched by hash. Default-branch heads at access time: ADIOS2 `2d6d28a519905ac2e33ef4e91a308139c829d7f3`; HydraGNN `d49d934403f0cc3276750004c8dfbf3a502a10f1`; ExaTN `c528f7ec7323ab5f4485b85efcefa016c32e1a2d`; TNQVM `a70eed190a4448dbe3dae94189d066ac694dc798`; sidpy `06105426f780ed8c0da5054589cc7d22afbfcf85`; pycroscopy `90e2d232acc9da634131c1793f082a70a04a3297`. These hashes are also embedded in source URLs. GitHub returned `archived=false` for each; this is a repository flag, not evidence of active maintenance or operational readiness. The new paper-level findings do not replace existing catalog statuses.

[KNOWN] Public API revision checks: [ADIOS2](https://api.github.com/repos/ornladios/ADIOS2/commits/2d6d28a519905ac2e33ef4e91a308139c829d7f3), [HydraGNN](https://api.github.com/repos/ORNL/HydraGNN/commits/d49d934403f0cc3276750004c8dfbf3a502a10f1), [ExaTN](https://api.github.com/repos/ORNL-QCI/exatn/commits/c528f7ec7323ab5f4485b85efcefa016c32e1a2d), [TNQVM](https://api.github.com/repos/ORNL-QCI/tnqvm/commits/a70eed190a4448dbe3dae94189d066ac694dc798), [sidpy](https://api.github.com/repos/pycroscopy/sidpy/commits/06105426f780ed8c0da5054589cc7d22afbfcf85), [pycroscopy](https://api.github.com/repos/pycroscopy/pycroscopy/commits/90e2d232acc9da634131c1793f082a70a04a3297). Accessed 2026-11-10.
