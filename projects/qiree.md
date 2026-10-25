# QIR-EE (QIR Execution Engine)
- Official page: none live yet. The README links user and developer docs on GitHub Pages, but both are marked "(coming soon)". [KNOWN: README]
- Repo: https://github.com/ORNL-QCI/qiree (default branch `main`)
- Docs: RST files in `doc/` plus Doxygen comments in the source, which you can build yourself with `-DQIREE_BUILD_DOCS=ON`. [KNOWN: README]
- Paper: "A Cross-Platform Execution Engine for the Quantum Intermediate Representation", Journal of Supercomputing 81, 1521 (2025), https://doi.org/10.1007/s11227-025-07969-2 [KNOWN: README; author affiliations not checked]
- DOE CODE: https://www.osti.gov/doecode/biblio/149694 lists ORNL as research org. The README says the code went public on GitHub 2024-06-24 and was released to DOE CODE 2025-01-15. [KNOWN: catalog row, README]
- License: Apache-2.0 WITH LLVM-exception, or MIT, at the user's option, per `COPYRIGHT`. Individual files carry SPDX tags (short machine-readable license labels). The LICENSE-APACHE and LICENSE-MIT files it mentions aren't in the repo root, and GitHub's API shows NOASSERTION. OSTI's GPL-3.0 conflicts with the repo, and the fact-check pass ruled to trust the repo. [KNOWN: COPYRIGHT file, GitHub API, catalog fact-check note]
- Copyright: `COPYRIGHT` says rights "are retained by contributors". Source file headers read "Copyright 2024 UT-Battelle, LLC, and other QIR-EE developers" (51 files under `src/` and `app/`). [KNOWN: `COPYRIGHT`, `src/qiree/Executor.cc` line 2]
- Status: active, but young. There's one release, v0.1.0 (2026-05-05 UTC). The last commit on `main` was 2025-12-02 UTC and the last push was 2026-05-05 UTC (the release tag). It isn't archived. [KNOWN: GitHub API, git log]
- Scope (rule 13): passes two ways. OSTI names ORNL as research org, and UT-Battelle is a copyright holder in the file headers. [KNOWN]

## Plain-language walkthrough
- **What it is:** a C++ library and set of command-line tools that take a quantum program written in QIR and run it on a simulator or on real quantum hardware. QIR (Quantum Intermediate Representation) is a common in-between language for quantum programs, built on LLVM, the compiler toolkit behind clang. [KNOWN: README; the QIR spec is linked to qir-alliance]
- **The problem:** quantum programming tools and hardware vendors each speak their own format. A shared format like QIR only helps if something can actually run it on many machines. The README describes the project as showing "the feasibility of a modular workflow at the lower end of the quantum software stack". [KNOWN: quote, README; INFERRED: the framing]
- **What goes in:** a `.ll` file (LLVM's human-readable code format) holding the quantum circuit, a choice of backend, and a number of *shots*. A shot is one run of the circuit; quantum results are random, so you repeat and count. [KNOWN: README usage; INFERRED: the shots explanation]
- **What happens:** QIR-EE loads the file with LLVM's execution engine, which runs the code directly without producing a separate program. Every time the program calls a quantum operation (a gate, a measurement), QIR-EE passes that call to the chosen backend. [KNOWN: README "using the LLVM execution engine"; INFERRED: the call-forwarding design, from `QuantumInterface.hh` and the per-backend folders]
- **What comes out:** a tally of measured bit strings, such as how often "00" versus "11" came up, or XACC's result buffer. [KNOWN: README "Understanding the Results"]
- **Where humans act:** someone writes or generates the QIR, picks the backend, and supplies any vendor credentials themselves, in a config file in their home folder. [KNOWN: README] We didn't use or test any vendor account (rule 16).
- **What it is not:** it isn't a quantum computer or a quantum compiler. It doesn't write your circuit, it runs one. [INFERRED]
- **What's unknown:** who uses it beyond the paper, and when the hosted docs will go live.
- **Example:** `qir-qsim examples/bell.ll -s 100` runs a two-qubit "Bell" circuit 100 times on Google's qsim simulator. You'd expect roughly half "00" and half "11", because the qubits are entangled. [KNOWN: README command pattern (shown there with teleport.ll); INFERRED: the expected result, from standard quantum physics]

## How it works
- **Backends:**
  - `qirqsim`: Google's qsim simulator, which handles measurements in the middle of a circuit. [KNOWN: README]
  - `qirxacc`: XACC, ORNL-QCI's framework that reaches many simulators and vendor machines. The README lists tested targets including aer, qpp, Quantinuum and IonQ devices. [KNOWN: README]
  - `qirlightning`: "Lightning", likely PennyLane Lightning, a fast state-vector simulator. [KNOWN: folder and `app/qir-lightning.cc`; INFERRED: which Lightning it is]
- **Core library (`src/qiree/`):** `Module` loads the LLVM code, `Executor` runs it, and `QuantumInterface` is the contract each backend implements. `ResultDistribution` and `RecordedResult` gather the outcomes. [KNOWN: file names; INFERRED: roles]
- **C interface (`src/cqiree/`):** lets other languages and tools call QIR-EE through plain C. [INFERRED: from `CQiree.h`] IRIS (`iris`) references qiree in its runtime build, matching the DeviceQIREE backend noted in the IRIS brief. [KNOWN: https://github.com/ORNL/iris/blob/main/src/runtime/CMakeLists.txt]

## How the project is organized
- `app/` (three command-line tools: `qir-qsim`, `qir-xacc`, `qir-lightning`), `src/` (library plus backends), `examples/` (QIR circuits such as bell, teleport and phase estimation, plus `qwerty/` and `unitaryhack2025/` subfolders), `test/`, `doc/`, `cmake/`, `scripts/`. [KNOWN: repo tree, README table]
- Languages: C++ about 66% by bytes, CMake 15%, LLVM IR 10%, plus a little Python, Shell and C. [KNOWN: GitHub languages API]
- Build: CMake. LLVM is required (versions 14 to 18 tested), and XACC is optional. [KNOWN: README]
- CI: three GitHub Actions workflows (`build-fast.yml`, `pr.yml`, `push.yml`). [KNOWN: `.github/workflows/`]
- Contributors: 8 including anonymous commit authors, and also 8 GitHub accounts without them. Created on GitHub 2024-06-20 UTC. [KNOWN: GitHub API]

## Who uses it / why it matters
Quantum hardware is fragmented, so a layer that runs one standard program format on many machines lowers the cost of trying each one. [INFERRED] The `unitaryhack2025` examples folder suggests outside contributions through the unitaryHACK open-source event. [INFERRED: folder name only] Real-world users are [UNKNOWN]. Example result data lives in a separate personal repo, which I didn't review. [KNOWN: README link]

## Related projects
- XACC (ORNL-QCI): an optional backend. The discovery pass has it queued. [KNOWN: README]
- IRIS (`iris`): has a QIR-EE device backend. [KNOWN: IRIS brief, IRIS CMake]

## Known / Inferred / Unknown
- KNOWN: purpose, license wording, copyright headers, backends, layout, CI, release, counts, paper, DOE CODE dates.
- INFERRED: internal class roles, Lightning's identity, the unitaryHACK tie, the example outcome.
- UNKNOWN: users, hosted docs date, why the license files are missing from the root.

## Sources (accessed 2026-10-24)
- https://github.com/ORNL-QCI/qiree (README.md, COPYRIGHT, src/, app/, examples/, test/, .github/workflows/)
- https://api.github.com/repos/ORNL-QCI/qiree (plus /languages, /releases, /contributors)
- https://www.osti.gov/doecode/biblio/149694
- https://doi.org/10.1007/s11227-025-07969-2 (cited, not read)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Rechecked: DOE CODE code-149694 ("QIR-EE", ORNL research org, 2025-01-15) via the OSTI API. The OSTI id is `code-149694`; the doecode URL in the brief is correct. COPYRIGHT text (Apache-2.0 with LLVM exception or MIT, "retained by contributors"), the UT-Battelle header in `src/qiree/Executor.cc` line 2, and the missing LICENSE-APACHE, LICENSE-MIT and LICENSE files (all 404 on main) were also checked, along with GitHub NOASSERTION, created 2024-06-20, 8 contributors, and languages (C++ 66.5%, CMake, LLVM IR). All verified.
- Second primary source: OSTI 3001783, "A cross-platform execution engine for the quantum intermediate representation" (2025, ORNL research org). Rule 13 is CORROBORATED.
- The "retained by contributors" wording next to UT-Battelle headers is not a contradiction: contributors keep their copyrights, and UT-Battelle is one of them. [INFERRED] The missing license files are a real repo gap and are worth noting, not fixing.
- No corrections needed.
