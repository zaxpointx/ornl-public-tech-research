# Engineering patterns in ORNL's public code

Independent research from public sources only; not affiliated with ORNL. Written 2026-11-11.

[How ORNL works](how-ornl-works.md) is about the organization: funding, staffing, release habits. This file is about the code. Each pattern below is a design move that shows up in a public ORNL repository, explained well enough that you could use the idea in your own project.

How to read each pattern:
- **Where it shows up** cites code at a pinned commit, so the line numbers stay true even after the repo changes. [KNOWN] means the code or docs say it.
- **Why** gives the reason only when the source states it. Otherwise it is [UNKNOWN]. Code shows what was built, not why.
- **Reuse it when / watch out for** is our engineering reading, tagged [INFERRED]. It is advice drawn from the code, not an ORNL recommendation.
- Line numbers were checked against shallow clones on 2026-11-11. We read the code. We did not build, run or benchmark any of it.

The patterns are grouped by the problem they solve. The [lookup table](#lookup-if-you-are-building) at the end maps "I am building X" to the right pattern and the right files. It is meant for people and for coding agents.

---

## A. Moving work through a pipeline

### A1. Choreography through named queues, with a lane per tenant
**Problem.** Many instruments produce runs that all need cataloging and reduction. One busy instrument must not starve the others.

**Where it shows up.** At SNS, the workflow manager doesn't call the reduction code. It publishes a message to a named queue, and whichever agent listens on that queue does the work ([pipeline deep dive](../deep-dives/sns-neutron-pipeline.md)). The newer code splits three shared queues into one lane per instrument.
- `REDUCTION.DATA_READY` becomes `REDUCTION.EQSANS.DATA_READY`, and the high-memory tier keeps its own lane: [`states.py` L24-L57](https://github.com/neutrons/data_workflow/blob/37d0d524d40e90404f546fe07dfe06d39f224a7a/src/workflow_app/workflow/states.py#L24-L57). [KNOWN]
- The instrument name is checked against `^[a-z0-9_]+$` before it goes into a queue name, so a bad value can't inject queue delimiters or broker wildcards ([L19-L23](https://github.com/neutrons/data_workflow/blob/37d0d524d40e90404f546fe07dfe06d39f224a7a/src/workflow_app/workflow/states.py#L19-L23)). [KNOWN]
- Routing sits behind a flag that is read at call time. If the flag value can't be parsed, the code falls back to the old shared queues instead of crashing ([`states.py` L139-L170](https://github.com/neutrons/data_workflow/blob/37d0d524d40e90404f546fe07dfe06d39f224a7a/src/workflow_app/workflow/states.py#L139-L170); [`settings.py` L27-L71](https://github.com/neutrons/data_workflow/blob/37d0d524d40e90404f546fe07dfe06d39f224a7a/src/workflow_app/workflow/settings.py#L27-L71)). [KNOWN]
- Routing log lines are throttled with a count, not a timer. That way the message flood the feature exists for can't also flood the logs ([L60-L83](https://github.com/neutrons/data_workflow/blob/37d0d524d40e90404f546fe07dfe06d39f224a7a/src/workflow_app/workflow/states.py#L60-L83)). [KNOWN]
- On the consumer side, the reduction agent asks the broker's management API for per-instrument queues on an interval. New instruments get picked up without a restart ([`README_developer.md` L57-L72](https://github.com/neutrons/post_processing_agent/blob/0ec3642fcc811e06e8a12e58e7b101af7213dccd/README_developer.md#L57-L72); [`queue_discovery.py`](https://github.com/neutrons/post_processing_agent/blob/0ec3642fcc811e06e8a12e58e7b101af7213dccd/postprocessing/queue_discovery.py)). [KNOWN]

**Why.** Stated in the code: a flood of runs from one instrument shouldn't hold up the others. Cataloging stays on one shared queue because its target is "a single external service with no per-instrument fairness problem" ([`states.py` L30-L31](https://github.com/neutrons/data_workflow/blob/37d0d524d40e90404f546fe07dfe06d39f224a7a/src/workflow_app/workflow/states.py#L30-L31)). [KNOWN]

**Something new found while pinning.** The agent's docs list a fourth split queue, an `EXPRESS` "fast lane for instruments that temporarily need priority, served by a dedicated agent" ([`README_developer.md` L64-L72, L128-L136](https://github.com/neutrons/post_processing_agent/blob/0ec3642fcc811e06e8a12e58e7b101af7213dccd/README_developer.md#L128-L136)). The workflow manager's split list at the pinned commit has only three queues and doesn't include `EXPRESS`. [KNOWN: both files] Whether express runs are published some other way, or the two repos are simply out of step, is [UNKNOWN].

**Reuse it when** you have several producers sharing workers and fairness matters more than strict global order. The details worth copying:
- Use an explicit list of which queues split, not a pattern. The code comment explains this stops double-splitting an already-specific name.
- Validate anything that gets interpolated into a routing key.
- Make the new behavior a flag that fails safe.
[INFERRED]

**Watch out for** contracts that only exist as string conventions. Two separately released repos have to agree on queue names, and the `EXPRESS` gap above is exactly that kind of drift. A shared constants package or a contract test would catch it. [INFERRED]

### A2. Workers that police their own jobs
**Problem.** A reduction script written by an instrument scientist can hang or eat all the memory on a shared node.

**Where it shows up.** The post-processing agent launches each script as a subprocess and polls it.
- Each poll adds up the resident memory of the process and all its children with `psutil`. It kills the whole process tree when memory passes a percentage of system RAM or time passes a limit, and writes the reason into the run's error log ([`job_handling.py` L33-L88](https://github.com/neutrons/post_processing_agent/blob/0ec3642fcc811e06e8a12e58e7b101af7213dccd/postprocessing/processors/job_handling.py#L33-L88), memory helper [L127-L158](https://github.com/neutrons/post_processing_agent/blob/0ec3642fcc811e06e8a12e58e7b101af7213dccd/postprocessing/processors/job_handling.py#L127-L158)). [KNOWN]
- It blocks intake while the number of running subprocesses is over `max_procs`, which gives back-pressure at the worker ([`Consumer.py` L133-L146](https://github.com/neutrons/post_processing_agent/blob/0ec3642fcc811e06e8a12e58e7b101af7213dccd/postprocessing/Consumer.py#L133-L146)). [KNOWN]
- It sends heartbeats on a timer and answers pings, so the monitoring side can tell a live agent from a dead one ([`Consumer.py` L176-L206, L325-L342](https://github.com/neutrons/post_processing_agent/blob/0ec3642fcc811e06e8a12e58e7b101af7213dccd/postprocessing/Consumer.py#L176-L206)). [KNOWN]
- A run counts as successful when its stderr file is empty. Configurable regexes can whitelist known-harmless error lines ([`job_handling.py` L91-L125](https://github.com/neutrons/post_processing_agent/blob/0ec3642fcc811e06e8a12e58e7b101af7213dccd/postprocessing/processors/job_handling.py#L91-L125)). [KNOWN]

**Why.** [UNKNOWN]. The README gives the 60-minute and 70%-of-memory example values but no rationale.

**Reuse it when** you run untrusted or semi-trusted user scripts on shared hardware and can't count on cgroups or a batch scheduler. Measure the whole process tree, not just the parent, because scientific scripts spawn children. [INFERRED]

**Watch out for** using "stderr is empty" as the success test. It's simple and needs no cooperation from script authors, but it marks a run that wrote a harmless warning as failed and a run that crashed silently as passed. That's presumably why the whitelist exists. An explicit exit code or result manifest is sturdier. The OLCF harness in B1 takes that route. [INFERRED]

### A3. A typed component chain with swappable tools (the "fidelity ladder")
**Problem.** One question, such as "what grain structure will this printed part have?", can be answered by several codes of different speed and accuracy. You want to swap them without rewriting the workflow.

**Where it shows up.** Myna, the additive-manufacturing workflow tool ([deep dive](../deep-dives/additive-manufacturing.md)), has three kinds of pieces:
- **Components** are typed by the physical quantity they produce, not by the tool that makes it. A microstructure component declares that it needs `FileReducedSolidification` input and produces `FileVTK` output ([`component_microstructure.py` L21-L31](https://github.com/ORNL-MDF/Myna/blob/6a3fd4cf9dedc581ce635355ed4067537b43a07f/src/myna/core/components/component_microstructure.py#L21-L31)). [KNOWN]
- **Application wrappers** hold all tool-specific logic in `configure`/`execute`/`postprocess` stage modules.
- **Database adapters** hold all build-database parsing and the sync-back.

The stated goals are "Keep workflow orchestration generic across build database formats" and "Isolate external simulation-tool behavior in application wrappers" ([`ARCHITECTURE.md` L26-L37, L111-L145](https://github.com/ORNL-MDF/Myna/blob/6a3fd4cf9dedc581ce635355ed4067537b43a07f/ARCHITECTURE.md#L26-L37)). [KNOWN]

**Why.** Partly stated: the architecture goals above. The 2025 Myna paper shows the payoff. A cheap model (3DThesis) screened 54 parts, and slower models ran only on regions people picked ([deep dive, research update](../deep-dives/additive-manufacturing.md)). [KNOWN]

**Reuse it when** your pipeline has interchangeable solvers or models. Define the interface by the data contract between stages (the file types), then give each tool a three-stage wrapper. Keep "where inputs come from" (adapters) apart from "what runs" (wrappers). [INFERRED]

**Watch out for** the hidden cost: every intermediate format is a contract you maintain. The same deep dive notes that ExaCA's own docs don't name the heat models that feed it, so the contract lives on one side only. And the Myna paper's mismatch between predictions and the measured microstructure is a reminder: a well-plumbed chain can still be physically wrong. [KNOWN: deep dive; INFERRED: the lesson]

### A4. Capture provenance where the work already happens
**Problem.** Scientists won't rewrite workflows to record what used what. Without that record, results can't be traced or reproduced.

**Where it shows up.** Flowcept captures provenance two ways and funnels both into one stream.
- **Explicit instrumentation**: decorators, a context manager, loop and PyTorch hooks. The extension rules say "Instrument coarsely by default; tight loops and distributed workers can amplify overhead" ([`instrumentation/README.md` L14-L28](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/src/flowcept/instrumentation/README.md#L14-L28)). [KNOWN]
- **Adapters** that observe tools people already use: Dask, MLflow, TensorBoard and message brokers ([`flowceptor/adapters/`](https://github.com/ORNL/flowcept/tree/c000b10ea49659af6c5821b61918f3893bd46a92/src/flowcept/flowceptor/adapters)). [KNOWN]
- Records are buffered and published in bulk, msgpack-serialized and chunked, to a swappable message-queue backend: Redis, Kafka, RabbitMQ or Mofka ([`mq_dao/`](https://github.com/ORNL/flowcept/tree/c000b10ea49659af6c5821b61918f3893bd46a92/src/flowcept/commons/daos/mq_dao); [`mq_dao_base.py` L85-L98](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/src/flowcept/commons/daos/mq_dao/mq_dao_base.py#L85-L98)). [KNOWN]
- The data model follows W3C PROV and extends it for workflow, ML and agent contexts ([README L80](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/README.md#L80)). [KNOWN]

**Why.** Overhead is stated as the reason for coarse capture. The buffering reason is [UNKNOWN], though it fits the same overhead concern. [INFERRED]

**Reuse it when** you need lineage across ML and HPC steps. Three ideas carry over:
- Keep `used`/`generated` semantics fixed.
- Make capture asynchronous with buffering.
- Hook into the frameworks people already run before asking them to add decorators.
[INFERRED]

**Watch out for** what a buffer means for failures, and note that this is now measured, not just read. The [Flowcept failure study](../atlas/labs/flowcept-failure-study/README.md) ran Flowcept 1.0.3 with deliberately killed jobs. In offline mode the buffer is a plain list written only on a normal stop, so a process killed by SIGTERM or `os._exit` left **zero** records, including 200 tasks that had already finished. The project's docs say offline mode keeps everything in memory until dumped, so this is a documented limit, and calling `dump_buffer()` before the crash saved everything. The automatic flushing described above applies only to the online, broker-backed mode. The same study found that a workflow which raises an exception is still recorded as FINISHED. [KNOWN: lab results at the pinned revision; online mode not tested] For your own design: buffered telemetry needs a periodic flush or a signal handler, because the runs that die are the ones you most need records for. [INFERRED]

---

## B. Proving software works on a machine

### B1. Acceptance testing as a loop with an exit-code contract
**Problem.** A new supercomputer has to show it runs real applications correctly and fast enough, again and again, before users trust it.

**Where it shows up.** The OLCF Test Harness ([deep dive](../deep-dives/olcf-test-harness.md)) runs every test through fetch, build, submit, run, check, and optionally resubmit.
- The check script reports through a suggested set of exit codes: `0` passed, `1` failed, `2` wrong answer, `5` correct but missed a performance target. The harness itself only separates zero from non-zero ([`adding_new_test.rst` L471-L479](https://github.com/olcf/olcf-test-harness/blob/a5bbd1d79337f10465c155f854891ee3389df960/doc-sphinx/source/user_guide/adding_new_test.rst#L471-L479)). [KNOWN]
- Every stage writes a timestamped event, from `LOGGING_START` to `CHECK_END` ([`status_file.py` L78-L99](https://github.com/olcf/olcf-test-harness/blob/a5bbd1d79337f10465c155f854891ee3389df960/oth/libraries/status_file.py#L78-L99)). These events can stream to InfluxDB or Kafka. [KNOWN: deep dive]

**Update to the deep dive.** The 2026-10-29 fact-check left open whether `runtests.py --mode ...` still works after the October 2026 reorganization. At the pinned commit the docs say `othctl run --mode start`, and `bin/othctl` exists ([`adding_new_test.rst` L119](https://github.com/olcf/olcf-test-harness/blob/a5bbd1d79337f10465c155f854891ee3389df960/doc-sphinx/source/user_guide/adding_new_test.rst#L119); [`bin/`](https://github.com/olcf/olcf-test-harness/tree/a5bbd1d79337f10465c155f854891ee3389df960/bin)). [KNOWN] So the command interface is now `othctl`. Whether the old entry point survives as an alias was not checked. [UNKNOWN]

**Why.** Stated purpose: continuous mode simulates a production workload ([deep dive](../deep-dives/olcf-test-harness.md)). [KNOWN] The reason behind the specific exit codes is [UNKNOWN]. The docs call them "a standard".

**Reuse it when** you're validating any deployment target: a cluster, a container platform, a hardware lab. Separating "wrong answer" from "too slow" from "crashed" in the check contract is cheap, and it's the information you want at 2 a.m. Per-stage event files make it easy to see where a run stalled. [INFERRED]

**Watch out for** the split between public framework and private content. The framework is public, but the real test suites and pass rates aren't, so you can copy the method but not OLCF's thresholds. [KNOWN: deep dive]

### B2. Pin the shared engine through a facility channel, then fence it with a facade
**Problem.** Several instrument apps depend on one large, shared physics engine (Mantid). An engine upgrade or a thread-safety slip can break an instrument.

**Where it shows up.** SNAPRed, the reduction app for the SNAP instrument:
- It pins Mantid to a minor-version window (`>=6.16,<6.17`) and pulls it from an ORNL-specific conda channel with main, rc and nightly labels ([`pyproject.toml` L140-L150, L192, L319-L321](https://github.com/neutrons/SNAPRed/blob/44c3e3d577bd480670dd8b00037c7d6926608d3d/pyproject.toml#L140-L150)). [KNOWN]
- A lint rule bans importing `mantid.simpleapi` anywhere in the backend except named exceptions, so every call goes through one facade class, `MantidSnapper` ([`pyproject.toml` L91-L99](https://github.com/neutrons/SNAPRed/blob/44c3e3d577bd480670dd8b00037c7d6926608d3d/pyproject.toml#L91-L99)). [KNOWN]
- The facade lists the engine algorithms that aren't re-entrant (live-data loading) and the ones that can't run concurrently (NeXus saves, workspace renames), and guards each set with a mutex and a timeout ([`MantidSnapper.py` L53-L77](https://github.com/neutrons/SNAPRed/blob/44c3e3d577bd480670dd8b00037c7d6926608d3d/src/snapred/backend/recipe/algorithm/MantidSnapper.py#L53-L77)). [KNOWN]

**Why.** For the mutexes, partly stated: a code comment explains that execution, not construction, is locked because a live-data algorithm instance stays resident between calls. [KNOWN] The reason for a facility channel instead of the public Mantid channel is [UNKNOWN].

**Reuse it when** your app sits on a big dependency you don't control. Three moves:
- Pin it to a narrow window.
- Route every call through one module.
- Use the linter to enforce that boundary, because a convention alone won't hold it.
[INFERRED]

**Watch out for** the facade turning into a second copy of the engine's API. The lint exceptions list shows where the boundary already leaks. [INFERRED]

---

## C. Making numerical code fast and portable

### C1. Factor once on the CPU, refactor many times on the GPU
**Problem.** Grid simulation and optimization solve a long series of sparse linear systems. The sparsity pattern stays the same and only the values change.

**Where it shows up.** ReSolve's GPU example handles the first system with a full KLU factorization on the CPU: `setup`, `analyze`, `factorize`. It then pulls out the L and U factors and the P and Q orderings, hands them to a GPU refactorization solver, and solves every later system with refactorization on the device. An optional FGMRES step can be added ([`gpuRefactor.cpp` L1-L15, L267-L320](https://github.com/ORNL/ReSolve/blob/c2ccbca565bc3c2e3f4db48a7fe138df406f9e74/examples/gpuRefactor.cpp#L267-L320)). The CUDA or HIP backend is a template parameter picked at compile time ([L80-L95](https://github.com/ORNL/ReSolve/blob/c2ccbca565bc3c2e3f4db48a7fe138df406f9e74/examples/gpuRefactor.cpp#L80-L95)). [KNOWN]

**Why.** The general rationale, that refactorization reuses the work of the expensive symbolic step, is in the [grid deep dive](../deep-dives/grid-tools.md). [KNOWN: brief] We didn't find a ReSolve-specific statement explaining why the first factorization runs on the CPU. [UNKNOWN] A plausible reason is that pivoting-heavy symbolic analysis maps poorly to GPUs. That is our inference. [INFERRED, medium]

**Reuse it when** you solve the same structure many times: time stepping, Newton iterations, parameter sweeps. Split the "learn the structure" step from the "redo the numbers" step, and let each run where it's fastest. [INFERRED]

**Watch out for** the structure changing under you. If a contingency removes a line, the pattern changes and the cached factorization no longer applies. The example's "redo factorization" variants in `examples/experimental/` cover this case. [KNOWN: file names; INFERRED: purpose]

### C2. One data layout knob for CPUs and GPUs (array-of-structs-of-arrays)
**Problem.** Particle codes store many fields per particle. CPUs and GPUs want different memory layouts for speed, and maintaining two copies of the code is a bad trade.

**Where it shows up.** Cabana, built on Kokkos and co-developed under ECP's particle co-design center with ORNL among the developers ([README L8-L18](https://github.com/ECP-copa/Cabana/blob/2e52143b6c06f37502e7cddd37f50dcb374f1906/README.md#L8-L18); [LICENSE L36](https://github.com/ECP-copa/Cabana/blob/2e52143b6c06f37502e7cddd37f50dcb374f1906/LICENSE#L36)):
- Its `AoSoA` type takes the particle's member types, a Kokkos memory space and a `VectorLength`. If you leave the vector length out, it defaults to the preferred value for that memory space's execution space ([`Cabana_AoSoA.hpp` L95-L122](https://github.com/ECP-copa/Cabana/blob/2e52143b6c06f37502e7cddd37f50dcb374f1906/core/src/Cabana_AoSoA.hpp#L95-L122)). [KNOWN]
- The same header advises putting larger types first and grouping same-type members to cut padding. [KNOWN]
- Finch, the GPU heat model in the additive ladder, is built on Cabana ([Finch brief](../projects/finch.md)). [KNOWN]

**Why.** The general reason (portable performance across CPU and GPU) is stated in the README. The specific reason for AoSoA over plain struct-of-arrays is [UNKNOWN] in the sources we read.

**Reuse it when** you write performance-portable C++ with many small records. Make layout a compile-time parameter tied to the target, so the right default comes free. [INFERRED]

**Watch out for** template-heavy APIs, which raise the cost of entry for contributors. The header's own FIXME about Kokkos version compatibility shows the maintenance burden of tracking an upstream portability layer. [KNOWN: FIXME at L119-L120; INFERRED: the reading]

---

## D. Patterns from the 2025-2026 releases
These come from batch 13, which covers five projects that had no brief before 2026-11-11. Each entry links the full brief, where the evidence is laid out in more detail.

### D1. Extend a mature solver, and add acceleration at the linear-algebra seam
**Problem.** Simulating a new manufacturing process needs multiphase flow, heat transfer and phase change. Writing all of that from scratch would take years.

**Where it shows up.** [DEDFoam](../projects/dedfoam.md), released 2026, simulates blown-powder metal printing.
- It starts from OpenFOAM's `compressibleInterFoam` solver and adds only the process physics: powder capture, a laser flux, a Marangoni force and mushy-zone latent heat ([`DEDFoam.C` L32-L36](https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/DEDFoam.C#L32-L36)). [KNOWN]
- GPU acceleration doesn't touch the physics. It comes from swapping the linear solver for PETSc through petsc4Foam ([README L2-L5](https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/README.md#L2-L5)). [KNOWN]
- AdditiveFOAM's heat-source models are an opt-in build flag (`USE_ADDITIVEFOAM`), not a fork ([README L31-L34](https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/README.md#L31-L34)). The brief's file comparison found no code copied from AdditiveFOAM. [KNOWN: brief]

ReSolve (C1) is the same idea seen from the other side: a library built to be the swappable seam.

**Why.** [UNKNOWN]. No source says why DEDFoam targets the OpenCFD line of OpenFOAM while AdditiveFOAM targets the Foundation line. Those two lines aren't drop-in compatible, so whether the plugin builds across them is an open question in the brief.

**Reuse it when** the physics you need is a variation on a well-tested base solver. Put your additions in separate include files. Keep optional dependencies behind build switches. Get speed from the linear solver layer before rewriting kernels. [INFERRED]

### D2. A surrogate model that refuses to extrapolate
**Problem.** A small machine-learning model can stand in for an expensive sub-simulation. Outside the data it was trained on, though, it returns confident nonsense.

**Where it shows up.** DEDFoam can predict powder catchment efficiency with a TensorFlow Lite model.
- The training ranges for all four inputs are hard-coded beside the normalization constants ([`createMLmodel.H` L26-L44](https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/createMLmodel.H#L26-L44)).
- The run stops with a fatal error if any input falls outside its range ([L49-L72](https://github.com/ORNL/DEDFOAM/blob/d298a0020c8aea7e8024d6022a5cedfce12c049b/applications/solvers/DEDFoam/createMLmodel.H#L49-L72)).

[KNOWN]

**Why.** [UNKNOWN] in a stated form. The behavior speaks for itself.

**Reuse it when** you embed any learned model in a physics or engineering workflow. Ship the training envelope with the model, check it on every call, and fail loudly instead of clamping. [INFERRED]

**Watch out for** putting the envelope in source code. Retraining the model then means editing C++ constants in step with the model file, which is a mismatch waiting to happen. A model file that carries its own metadata avoids that. A comment hints that overrides were planned ("override via system/MLDict if desired"). [KNOWN: L26; INFERRED: the risk]

### D3. Small model plus curated expert data, and the evaluation trap
**Problem.** General code assistants are weak on niche HPC libraries such as Kokkos, and big hosted models can't always be used with sensitive code.

**Where it shows up.** [ChatHPC](../projects/chathpc.md) fine-tunes a 7-billion-parameter Code Llama with LoRA adapters, merges them into the base model, and serves the result locally.
- LoRA is applied with r=16 and alpha=16 on the attention projections, for 400 steps ([`app.py` L825-L889](https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/src/chathpc/app/app.py#L825-L889)), and the adapter is merged in afterwards ([L915-L923](https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/src/chathpc/app/app.py#L915-L923)). [KNOWN]
- The SC25 paper says initial training used "about 70" question-context-answer samples, and that an assistant is built "in a few minutes" on one node with two H100 GPUs ([OSTI 3682544](https://www.osti.gov/biblio/3682544)). [KNOWN: paper text, re-read 2026-11-11]

**Watch out for** how the library evaluates during training. Its evaluation dataset is the training file loaded a second time ([`app.py` L525-L526](https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/src/chathpc/app/app.py#L525-L526)), and its built-in verify step is a near-exact text match. [KNOWN] Training-time evaluation numbers from this library therefore measure memorization. The paper's separate test prompts are the evidence to read instead. [INFERRED]

**Reuse it when** you want a cheap specialist assistant for a narrow API and can curate a few dozen high-quality examples. Hold out a real test set from day one. [INFERRED]

### D4. Spend compute where the signal is (adaptive tokenization)
**Problem.** Physics fields such as turbulence are mostly smooth, with small regions of sharp detail. Uniform patching for a transformer wastes tokens on the smooth parts or blurs the sharp ones.

**Where it shows up.** [MATEY](../projects/matey.md), a spatiotemporal foundation-model codebase:
- It splits the field into patches, computes each patch's variance, and refines only the highest-variance patches. You choose the top fraction by a `refine_ratio`, or a threshold relative to the maximum variance ([`shared_utils.py` L106-L127](https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/matey/data_utils/shared_utils.py#L106-L127)). [KNOWN]
- Long token sequences are then spread across GPUs with sequence-parallel groups and a ring-attention module ([`distributed_utils.py`](https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/matey/utils/distributed_utils.py); [`ringX_attn.py`](https://github.com/ORNL/MATEY/blob/631a4139295d4f51e573d474cff7d6586f3aa310/matey/models/ringX_attn.py)).
- The project's exascale paper reports up to 1.1 EFLOPS on 32,768 AMD GPUs on Frontier ([OSTI 3367073](https://www.osti.gov/biblio/3367073)). [KNOWN: abstract, re-read 2026-11-11]

**Why.** The paper's framing is resolving small scales in long-context learning. [KNOWN: title and abstract] That variance is the right refinement signal for every physical system is not claimed. [UNKNOWN]

**Reuse it when** your inputs have uneven information density: images, simulation fields, sensor grids. A cheap per-region statistic can decide where the expensive model looks. This is the same instinct as adaptive mesh refinement in classical solvers. [INFERRED]

**Watch out for** variance as a proxy. It flags noise as readily as structure. The repo has no tests or CI, so you'd be adopting the idea, not a hardened implementation. [KNOWN: brief; INFERRED: the caution]

### D5. One I/O API, transport chosen at run time
**Problem.** The same simulation sometimes needs to write files for later, and sometimes needs to stream data straight into an analysis or ML job. Rewriting the I/O for each case is wasteful.

**Where it shows up.** [ADIOS2](../projects/adios2.md), the I/O library that HydraGNN and E3SM's atmosphere I/O layer build on.
- An application declares variables and steps once. An *engine* chosen by name or configuration then decides where the data goes: BP5 files, SST streaming, and others. Engines can also be registered at run time ([`IO.cpp` L203-L207](https://github.com/ornladios/ADIOS2/blob/e43363bd5596da4cf2d2c78d7c4940fb512fad2f/source/adios2/core/IO.cpp#L203-L207); [component overview](https://github.com/ornladios/ADIOS2/blob/e43363bd5596da4cf2d2c78d7c4940fb512fad2f/docs/user_guide/source/components/overview.rst#L11-L60)). [KNOWN]
- `Put` is deferred by default. The caller can't reuse the buffer until `EndStep`, `Close` or `PerformPuts`, which lets the engine batch and aggregate ([`Engine.h` L140-L162](https://github.com/ornladios/ADIOS2/blob/e43363bd5596da4cf2d2c78d7c4940fb512fad2f/source/adios2/core/Engine.h#L140-L162)). [KNOWN]
- Readers advance step by step and get back `OK`, `NotReady`, `EndOfStream` or `OtherError`. Because the API treats "nothing yet" and "finished" as normal states, the same loop works over a file or a live stream ([`ADIOSTypes.h` L101-L114](https://github.com/ornladios/ADIOS2/blob/e43363bd5596da4cf2d2c78d7c4940fb512fad2f/source/adios2/common/ADIOSTypes.h#L101-L114)). [KNOWN]
- Engine selection probes the filesystem on rank 0 only and broadcasts the result. A code comment says this is so a missing target "fails on every rank instead of a lone rank-0 throw that hangs the others" ([`IO.cpp` L605-L726](https://github.com/ornladios/ADIOS2/blob/e43363bd5596da4cf2d2c78d7c4940fb512fad2f/source/adios2/core/IO.cpp#L605-L726)). [KNOWN]

**Why.** The BP5 design notes state their own goals ([`bp5.rst` L5-L44](https://github.com/ornladios/ADIOS2/blob/e43363bd5596da4cf2d2c78d7c4940fb512fad2f/docs/user_guide/source/engines/bp5.rst#L5-L44)), and the comment above explains the rank-0 probe. [KNOWN] The [2026-11-10 computing chapter](../docs/portfolio-expansion-2026-11-10/computing-instruments.md) records an important boundary. SST's queue policy decides whether a slow reader blocks the writer or misses steps. It is not a durability guarantee. [KNOWN: that chapter's pinned SST docs]

**Reuse it when** you want one code path for "save it" and "stream it". Model data as named, typed variables in numbered steps, defer the writes, and make "not ready" a normal return value. In any MPI code, decide collectively and fail collectively. A single rank throwing alone is the classic way to hang a 10,000-node job. [INFERRED]

**Watch out for** binding churn downstream. HydraGNN carries a version shim because ADIOS2's Python bindings moved in 2.10 ([HydraGNN `_backend.py` L16-L22](https://github.com/ORNL/HydraGNN/blob/d49d934403f0cc3276750004c8dfbf3a502a10f1/hydragnn/data/adiosdataset/_backend.py#L16-L22)). [KNOWN] Swapping engines also changes failure semantics: a file outlives the reader, a stream may not. [INFERRED]

### D6. Turn the loop inside out for the GPU (steps outer, tracks inner)
**Problem.** Monte Carlo particle transport is naturally written one particle at a time, with branchy code and very different histories. That shape runs badly on GPUs.

**Where it shows up.** [Celeritas](../projects/celeritas.md), which accelerates high-energy-physics detector simulation.
- Its docs call the core algorithm "a loop interchange between particle tracks and steps". The outer loop runs over step iterations and the inner loop over a fixed-size vector of *track slots*, and each step is a sorted sequence of *actions*, usually one GPU kernel each ([`doc/index.rst` L200-L212](https://github.com/celeritas-project/celeritas/blob/e06590a2fa251851ffd3ce522bd374bac06c9b27/doc/index.rst#L200-L212)). [KNOWN]
- The action order is an explicit enum: generate, start, pre, along, the discrete selection, post, end. It includes "sort track slots" points between phases and "user" hooks ([`ActionInterface.hh` L28-L44](https://github.com/celeritas-project/celeritas/blob/e06590a2fa251851ffd3ce522bd374bac06c9b27/src/corecel/sys/ActionInterface.hh#L28-L44)). [KNOWN]
- The same source builds for CUDA or HIP through a thin macro and runtime layer ([`Macros.hh` L36-L40](https://github.com/celeritas-project/celeritas/blob/e06590a2fa251851ffd3ce522bd374bac06c9b27/src/corecel/Macros.hh#L36-L40); [`DeviceRuntimeApi.hh` L15-L55](https://github.com/celeritas-project/celeritas/blob/e06590a2fa251851ffd3ce522bd374bac06c9b27/src/corecel/DeviceRuntimeApi.hh#L15-L55)). [KNOWN]

**Why.** Stated in the docs: vectorizing the step loop over many tracks is what makes the GPU usable. [KNOWN] We found no stated reason for the sort points in the sources read. Grouping tracks that will take the same branch reduces divergence, but that is our inference. [INFERRED, medium]

**Reuse it when** you have many independent, branchy agents: particles, rays, simulated users, game entities. Store them as fixed slots, advance all of them one phase at a time, and make each phase its own kernel with a defined order. [INFERRED]

### D7. Accelerate inside the incumbent framework instead of replacing it
**Problem.** Physics experiments have years of detector models built on Geant4. A faster code that needs a rewrite won't be adopted.

**Where it shows up.** Celeritas plugs into Geant4 as a tracking manager. When Geant4 hands over a track of a type Celeritas handles, Celeritas pushes it into its own GPU transport and tells Geant4 to stop and kill its copy ([`TrackingManager.cc` L129-L158](https://github.com/celeritas-project/celeritas/blob/e06590a2fa251851ffd3ce522bd374bac06c9b27/src/accel/TrackingManager.cc#L129-L158)). The docs call this offload interface the "most stable and user-ready component" ([`doc/index.rst` L251-L256](https://github.com/celeritas-project/celeritas/blob/e06590a2fa251851ffd3ce522bd374bac06c9b27/doc/index.rst#L251-L256)). [KNOWN]

**Why.** [INFERRED] from what the project puts first: offload is the component it calls most ready, and its published benchmark is an ATLAS test-beam application speedup ([brief](../projects/celeritas.md), OSTI 2361202). We found no explicit statement of the adoption strategy.

**Reuse it when** the incumbent tool has an extension point. Take over the expensive inner work through that hook, keep the user's inputs and outputs unchanged, and make the fallback (CPU Geant4) the default when the accelerator isn't initialized. [INFERRED]

### D8. One geometry engine, shared across scientific fields
**Problem.** GPU particle tracking needs a geometry engine built for GPUs, and building one is a large investment.

**Where it shows up.** ORANGE (Oak Ridge Advanced Nested Geometry Engine) lives in the Celeritas repo. It "can be built via its interface to SCALE or constructed automatically from Geant4 geometry" ([`orange/README.rst` L12-L16](https://github.com/celeritas-project/celeritas/blob/e06590a2fa251851ffd3ce522bd374bac06c9b27/src/orange/README.rst#L12-L16)). An ORNL reactor-physics paper states in a footnote that "The ORANGE package is shared between Shift and the Celeritas MC code" ([OSTI 3376506](https://www.osti.gov/biblio/3376506), full text re-read 2026-11-11). [KNOWN] So the same geometry code serves GPU reactor neutronics ([Shift](../projects/shift-exnihilo.md)) and GPU detector simulation for high-energy physics. The Celeritas release notes call one version the first ORANGE release supporting GPU neutron transport in SCALE ([v0.4 notes L250-L252](https://github.com/celeritas-project/celeritas/blob/e06590a2fa251851ffd3ce522bd374bac06c9b27/doc/release-history/v0.4.rst#L250-L252)). [KNOWN]

QIR-EE, a quantum-computing execution engine already in this catalog, also carries Celeritas-derived headers ("UT-Battelle, LLC, and other Celeritas developers"), and its docs say its style should match Celeritas's ([`Assert.hh` L2-L3](https://github.com/ORNL-QCI/qiree/blob/78274099efde839cd9c134eb604011555bd08aee/src/qiree/Assert.hh#L2-L3)). [KNOWN] That gives three domains — reactors, particle physics and quantum — tied together by one code lineage.

**Why.** [UNKNOWN]. No public source explains how the sharing is organized.

**Reuse it when** two of your products need the same hard component. Extract it into a library with two thin front ends, one per input format, rather than maintaining parallel copies. [INFERRED]

**Watch out for** shared code making two release schedules depend on each other. The atlas has no evidence on how these projects coordinate releases. [UNKNOWN]

---

## Cross-cutting observations
- **Design reasons live in code comments more than in papers.** The clearest "why" statements in this file are inline comments: queue fairness, the OnCat exception, the mutex placement, coarse instrumentation. If you're studying an ORNL repo for its reasoning, grep the comments before searching the literature. [KNOWN: the cited comments; INFERRED: the habit]
- **Fail-safe defaults recur.** These include an unparseable flag treated as off, a missing instrument routed to the shared queue, and a vector length defaulting to the target's preference. The new behavior is opt-in, and the failure mode is the old behavior. [INFERRED from A1 and C2]
- **The newest projects lean on frameworks rather than replacing them.** DEDFoam extends OpenFOAM, Celeritas offloads from inside Geant4, and ChatHPC adapts an open base model. The 2025-2026 releases mostly add a specialized layer on top of an existing ecosystem. [INFERRED from D1, D3 and D7]
- **Contracts between repos are mostly strings.** These include queue names, file formats and exit codes. Few of them are enforced by a shared library or a contract test. That shows up as drift (A1's `EXPRESS` lane) and as one-sided documentation (A3). [INFERRED]

## Lookup: if you are building...
| You are building | Read pattern | Then open |
|---|---|---|
| A job queue where several sources share workers | A1, A2 | data_workflow `states.py`; post_processing_agent `job_handling.py`, `Consumer.py` |
| A runner for user-supplied scripts on shared machines | A2, B1 | `job_handling.py`; OTH `adding_new_test.rst` |
| A pipeline with interchangeable models or solvers | A3 | Myna `ARCHITECTURE.md`, `core/components/` |
| Lineage or provenance for ML/HPC workflows | A4 | Flowcept `instrumentation/README.md`, `mq_dao/` |
| An acceptance or regression suite for a cluster or lab | B1 | OTH `adding_new_test.rst`, `status_file.py` |
| An app on top of a big framework you don't control | B2 | SNAPRed `pyproject.toml`, `MantidSnapper.py` |
| Repeated sparse solves on GPUs | C1 | ReSolve `examples/gpuRefactor.cpp` |
| Performance-portable particle or record data in C++ | C2 | Cabana `core/src/Cabana_AoSoA.hpp` |
| A new solver built on an existing CFD or physics framework | D1 | DEDFoam `applications/solvers/DEDFoam/`, README build flags |
| An ML surrogate inside a simulation | D2 | DEDFoam `createMLmodel.H` |
| A small specialist code assistant | D3 | ChatHPC-app `src/chathpc/app/app.py` (and read its evaluation caveat) |
| A transformer over large physics fields | D4 | MATEY `matey/data_utils/shared_utils.py`, `matey/utils/distributed_utils.py` |
| Code that must both save and stream data | D5 | ADIOS2 `source/adios2/core/IO.cpp`, `Engine.h`, `ADIOSTypes.h` |
| GPU versions of branchy per-particle or per-agent code | D6 | Celeritas `doc/index.rst`, `src/corecel/sys/ActionInterface.hh` |
| An accelerator for a tool users already depend on | D7 | Celeritas `src/accel/TrackingManager.cc` |
| A component two products need | D8 | Celeritas `src/orange/`; OSTI 3376506 |

For coding agents: every row resolves to a pinned permalink above. When you cite a pattern in your own work, cite the permalink, not this file. If the upstream code has moved on, re-check it, because these lines describe the pinned commit only.

## Pinned commits (checked 2026-11-11)
| Repository | Commit |
|---|---|
| neutrons/data_workflow | `37d0d524d40e90404f546fe07dfe06d39f224a7a` |
| neutrons/post_processing_agent | `0ec3642fcc811e06e8a12e58e7b101af7213dccd` |
| neutrons/SNAPRed | `44c3e3d577bd480670dd8b00037c7d6926608d3d` |
| olcf/olcf-test-harness | `a5bbd1d79337f10465c155f854891ee3389df960` |
| ORNL-MDF/Myna | `6a3fd4cf9dedc581ce635355ed4067537b43a07f` |
| ORNL/flowcept | `c000b10ea49659af6c5821b61918f3893bd46a92` |
| ORNL/ReSolve | `c2ccbca565bc3c2e3f4db48a7fe138df406f9e74` |
| ECP-copa/Cabana | `2e52143b6c06f37502e7cddd37f50dcb374f1906` |
| ORNL/DEDFOAM | `d298a0020c8aea7e8024d6022a5cedfce12c049b` |
| ORNL/ChatHPC-app | `5c70d58242833f9083abfeded754c254375a79c3` |
| ORNL/MATEY | `631a4139295d4f51e573d474cff7d6586f3aa310` |
| ornladios/ADIOS2 | `e43363bd5596da4cf2d2c78d7c4940fb512fad2f` |
| celeritas-project/celeritas | `e06590a2fa251851ffd3ce522bd374bac06c9b27` |
| ORNL/HydraGNN | `d49d934403f0cc3276750004c8dfbf3a502a10f1` |
| ORNL-QCI/qiree | `78274099efde839cd9c134eb604011555bd08aee` |

Limits: we only read code at these commits. No hosts, ports or deployment details are named here, even where the public code contains defaults (rule 16). None of these patterns has been benchmarked by us.
