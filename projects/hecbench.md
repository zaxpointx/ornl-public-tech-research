# HeCBench
- Official page: none separate. The README is the main doc. [KNOWN: repo homepage field is empty, GitHub API]
- Repo: https://github.com/ORNL/HeCBench (default branch `master`)
- Docs: `README.md` (about 1,900 lines, mostly a per-benchmark reference), `CMAKE_BUILD.md`, `benchmarks.yaml`, `results/README.md`. [KNOWN: repo files]
- Paper: Z. Jin and J. S. Vetter, "A Benchmark Suite for Improving Performance Portability of the SYCL Programming Model", IEEE ISPASS 2023, pp. 325-327, doi:10.1109/ISPASS57527.2023.00041 [KNOWN: README; not read]
- License: BSD-3-Clause, and GitHub's API agrees. [KNOWN: LICENSE, GitHub API] Copyright is listed as "(c) 2020, Argonne National Laboratory" and "(c) 2020-, Oak Ridge National Laboratory", each with the same developer named. [KNOWN: LICENSE lines 3 and 4] Individual benchmarks are ported from other suites and may carry their own terms. [INFERRED: the README reference notes each benchmark's origin, e.g. "(opencl)" or "(cuda)"; not checked per folder]
- Status: active. The last commit was 2026-10-22, and the repo was created 2020-08-06 UTC. There are no GitHub releases, so it ships as a rolling repo. [KNOWN: GitHub API, git log]
- Scope (rule 13): ORNL is named as copyright holder in the LICENSE, and the repo sits under github.com/ORNL. [KNOWN] The discovery-pass OSTI search found no record, so ORNL as research org comes from the LICENSE only.

## Plain-language walkthrough
- **What it is:** a large collection of small GPU programs ("benchmarks"), each written several times in different GPU programming styles: CUDA, HIP, SYCL and OpenMP target offload. The README says it's for "studying performance, portability, and productivity". [KNOWN: README]
- **The problem:** supercomputers now use GPUs from NVIDIA, AMD and Intel, and each vendor has its own programming model. *Performance portability* asks whether code written once runs fast on all of them. You can only answer that by running the same task in each model on each machine and comparing. [INFERRED: standard HPC framing; the paper title names performance portability]
- **The four models:** CUDA is NVIDIA's own GPU language. HIP is AMD's near-copy of CUDA. SYCL (with Intel's version, DPC++) is an open C++ standard meant to run anywhere. OpenMP target offload adds compiler hints to ordinary C or C++ that move work onto a GPU. [INFERRED: general knowledge; the README names all four]
- **What goes in:** one benchmark's source in one model, a compiler for that model, and sometimes a dataset (pulled with DVC, a tool for versioning large data files alongside code). [KNOWN: README]
- **What happens:** you build the benchmark, run it with set arguments, and it prints timings. A test pattern in `benchmarks.yaml` picks the time out of the output. [KNOWN: `benchmarks.yaml` regex and args fields]
- **What comes out:** run times per benchmark, per model and per GPU, which the `hecbench` tool can store, compare and export as JSON or CSV. [KNOWN: `tools/hecbench` usage text]
- **Where humans act:** a researcher picks benchmarks and hardware, runs them, and draws conclusions about compilers, hardware or programming models.
- **What it is not:** it's not an application or a library you build on, and its numbers aren't official vendor scores. [INFERRED]
- **What's unknown:** who uses it outside ORNL and Argonne, and any outside results.
- **Example:** you run the `black-scholes` (finance) benchmark in its CUDA version on an NVIDIA GPU and its HIP version on an AMD GPU, then compare times to see whether one model leaves speed on the table. [INFERRED: an illustrative use; black-scholes is a listed benchmark]

## How it works
- **One folder per benchmark per model:** `src/<name>-<model>`, for example `aes-cuda` and `aes-sycl`. That gives 555 distinct benchmark names, with 554 CUDA, 551 HIP, 542 SYCL and 361 OpenMP folders. [KNOWN: counted from `src/` on 2026-10-24]
- **Categories:** 19, from automotive and bioinformatics to cryptography, finance, machine learning and robotics. The README admits the grouping "is not accurate" but works as a starting point. [KNOWN: README headings, short quote]
- **Security-relevant kernels:** the Cryptography category includes AES, ChaCha20, SHA-style hashes, secp256k1 (the elliptic curve Bitcoin uses) and ECDH. [KNOWN: README reference entries; INFERRED: the curve's use]
- **Build:** each folder has its own Makefile, and there's a newer top-level CMake system with presets per GPU type. CUDA needs 12.2+, ROCm 7.0+ and CMake 3.21+. [KNOWN: `CMAKE_BUILD.md`]
- **Dependencies:** a few benchmarks need Boost, Eigen, GDAL, MPI, GPU-aware MPI or vendor collective-communication libraries like NCCL. [KNOWN: README]
- **Data:** large inputs live outside git and are fetched with `dvc pull`. Where they're stored isn't described here (rule 16). [KNOWN: README]

## How the project is organized
- `src/` (all benchmarks, plus shared `include/` and `scripts/`), `tools/` (the `hecbench` command-line tool, a results helper, a metadata generator), `cmake/`, `results/` (an older notes page comparing SYCL, DPCT and OpenMP on Intel integrated GPUs), `benchmarks.yaml` (auto-generated metadata), `convert_benchmarks.py`. [KNOWN: repo tree]
- Languages: C++ about 44% by bytes, CUDA 25%, C 22%, Makefile 6%, then small shares of others. [KNOWN: GitHub languages API]
- Contributors: 113 including anonymous commit authors, 29 GitHub accounts without them. The gap is large, which suggests many one-off commits under unlinked emails. [KNOWN: GitHub API; INFERRED: the reason]
- CI: no GitHub Actions workflow folder was found in the clone. [KNOWN: no `.github/workflows/`]
- Stars: 310. That shows attention, not users. [KNOWN: GitHub API]

## Who uses it / why it matters
Benchmark suites like this are how compiler teams and labs check whether a new GPU or toolchain is any good before trusting it with science codes. [INFERRED] Use beyond the ISPASS paper is [UNKNOWN]; the connections-pass usage section will cover public traces.

## Related projects
- IRIS (`iris`): another ORNL project about running one code on many kinds of hardware. I saw no source tying them. [INFERRED: shared theme only]
- TASMANIAN (`tasmanian`): also has CUDA, HIP and DPC++ backends. Same theme, no tie seen. [INFERRED]

## Known / Inferred / Unknown
- KNOWN: purpose quote, license and copyright lines, models, folder counts, categories, build requirements, tool commands, language split, counts.
- INFERRED: per-benchmark license variation, example use, what the contributor gap means.
- UNKNOWN: OSTI record, owning ORNL division, outside users.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL/HeCBench (README.md, LICENSE, CMAKE_BUILD.md, benchmarks.yaml, tools/hecbench, results/README.md, src/)
- https://api.github.com/repos/ORNL/HeCBench (plus /languages, /releases, /contributors)
- https://ieeexplore.ieee.org/document/10158214 (cited in README, not read)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Rechecked on a fresh shallow clone of ORNL/HeCBench and the GitHub API. Verified: the LICENSE copyright lines (Argonne 2020, ORNL "2020-"), BSD-3-Clause in the API, created 2020-08-06, last commit 2026-10-22, 0 releases, no `.github/` directory, contributors 113 with anonymous / 29 accounts, languages (C++ 44.4%, CUDA 25.1%, C 22.4%), 555 distinct benchmarks, and folder counts of 554 CUDA, 551 HIP, 542 SYCL and 361 OpenMP. All match.
- Namesake guard: https://github.com/zjin-lcf/HeCBench is a separate GitHub fork of ORNL/HeCBench with its own commit history, not a redirect. Sources should cite ORNL/HeCBench.
- Rule 13 rests on the LICENSE plus the github.com/ORNL owner. Both are GitHub artifacts, so it stays KNOWN rather than CORROBORATED. The OSTI search for "HeCBench" returns papers that use it (ORNL ChatPORT and ChatHPC, plus several LLNL papers) but no software record. Those are usage evidence for the signals file, not ownership.
- No corrections needed.
