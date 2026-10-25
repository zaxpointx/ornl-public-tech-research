# XACC (eXtreme-scale ACCelerator programming framework)
- Official page: https://xacc.readthedocs.io (the repo homepage) and the Eclipse project page https://eclipse.org/xacc [KNOWN: GitHub API, NOTICE]
- Repo: https://github.com/eclipse-xacc/xacc (default branch `master`). The README and NOTICE still link the older path `github.com/eclipse/xacc`. [KNOWN: README, NOTICE]
- Docs: the Read the Docs site above, plus API docs at https://ornl-qci.github.io/xacc-api-docs/ [KNOWN: README]
- License: dual-licensed under the Eclipse Public License 1.0 (`LICENSE.EPL`) or the Eclipse Distribution License 1.0 (`LICENSE.EDL`, a BSD-3-style text). GitHub's API reports BSD-3-Clause, which matches only the EDL half. [KNOWN: NOTICE "Declared Project Licenses", LICENSE files, GitHub API]
- Copyright: NOTICE lists "Copyright (c) 2016-2018 UT-Battelle" as copyright holder. 471 source files carry UT-Battelle headers dated 2017 to 2021. The EDL file's own line names the Eclipse Foundation "and its licensors". [KNOWN: NOTICE, source headers, LICENSE.EDL line 1]
- Trademark: "Eclipse XACC" and "XACC" are trademarks of the Eclipse Foundation. [KNOWN: NOTICE]
- Status: unknown (rule 14).
  - The last commit on `master` was 2023-08-01 UTC, and the last commit on `xacc-devel` was 2023-03-02 UTC. [KNOWN: git log, GitHub API]
  - GitHub's last-push date is 2024-08-13 UTC, presumably a push to some other branch that I didn't trace. [KNOWN: date; INFERRED: cause]
  - It isn't archived, and there are no GitHub releases or tags. `VERSION` reads 0.1.16. [KNOWN]
  - Two-plus years of quiet doesn't prove it's dead; follow-on work may live in other repos. [INFERRED; rule 10, quiet vs. dead]
- Scope (rule 13): CORROBORATED. UT-Battelle is the copyright holder per NOTICE and the file headers, and DOE CODE code-5041 / OSTI 1339995 list ORNL as research org. [KNOWN: repo; https://www.osti.gov/biblio/code-5041 and https://www.osti.gov/biblio/1339995, both research org ORNL, contract AC05-00OR22725]

## Plain-language walkthrough
- **What it is:** a C++ framework (with a Python API) for writing programs that mix ordinary computing with quantum computing, then running the quantum parts on whichever quantum computer or simulator you choose. The README calls it "an extensible compilation framework for hybrid quantum-classical computing architectures". [KNOWN: README]
- **The problem:** every quantum hardware company has its own language and access method. Without a common layer, a program written for one machine has to be rewritten for the next. XACC is meant to be "language and hardware independent". [KNOWN: README heading; INFERRED: the framing]
- **Key terms:**
  - A *QPU* is a quantum processing unit, the quantum chip itself.
  - A *quantum kernel* is the small quantum routine that a normal program hands off to a QPU, much like a GPU kernel.
  - *Hybrid* means a classical loop runs the kernel many times and adjusts its settings between runs. [INFERRED: general definitions]
- **What goes in:** a quantum kernel written in one of several front-end languages (for example OpenQASM, a common quantum assembly language, or XACC's own XASM), a choice of backend (an "accelerator"), and a number of shots. [KNOWN: `quantum/plugins/xasm`, `staq` and the OpenQASM files in the language stats; README]
- **What happens:**
  1. A front-end compiler turns the kernel into XACC's intermediate representation (IR), a common in-between format.
  2. Optional passes rewrite or optimize the IR, for example fitting it to a chip's wiring ("placement").
  3. The chosen backend runs it.
  4. Results come back in a buffer. [KNOWN: README; folders `xacc/compiler`, `xacc/ir`, `quantum/plugins/placement`, `xacc/accelerator/AcceleratorBuffer.hpp`; INFERRED: the step order]
- **What comes out:** measurement counts and computed values, such as an estimated molecular energy from a chemistry algorithm. [KNOWN: the `python/examples/deuteronH2.py` and chemistry benchmark named in the README; INFERRED: the output type]
- **Where humans act:** a researcher writes the kernel and the classical loop, picks the backend, and supplies any vendor account themselves. [INFERRED] We didn't use any vendor account (rule 16).
- **What it is not:** it isn't a quantum computer, and it isn't tied to one vendor. [INFERRED]
- **What's unknown:** whether ORNL still develops it, and what replaced it, if anything.
- **Example:** the README's quick start runs a "deuteron" example. That's the textbook first test of the VQE algorithm, which estimates the energy of a deuteron (one proton plus one neutron) by repeatedly running a tiny quantum circuit and letting a classical optimizer tune it. [KNOWN: README example names; INFERRED: the VQE explanation]

## How it works
- **Plugin design:** almost everything is a plugin, registered through a service registry built on CppMicroServices, a C++ plugin system. So adding a new backend or language doesn't touch the core. [KNOWN: `xacc/service/ServiceRegistry.*`, `tpls/cppmicroservices`, the `manifest.json` files; INFERRED: the design intent]
- **Backends:** the README names IBM, Rigetti and D-Wave QPUs, plus simulators. [KNOWN: README] The plugin folders also include `ionq`, `honeywell`, `atos_qlm`, `iontrap`, `qpp`, `qsim`, `qrack` and a `noise_model`. [KNOWN: `quantum/plugins/`]
- **Two quantum styles:**
  - `quantum/gate` covers gate-model machines, which apply step-by-step logic gates to qubits.
  - `quantum/annealing` covers annealers like D-Wave's, which settle into a low-energy answer to an optimization problem. [KNOWN: folders; INFERRED: the definitions]
- **Algorithms:** ready-made hybrid algorithms including VQE, QAOA (an approach to optimization problems), QPE (phase estimation), QITE, ADAPT and others. [KNOWN: `quantum/plugins/algorithms/`]
- **Pulse level:** `quantum/gate/pulse` and `optimal_control` suggest XACC can also work below gates, at the level of the microwave pulses that drive qubits. [KNOWN: folders; INFERRED: the meaning]

## How the project is organized
- `xacc/` is the core: accelerator, algorithm, compiler, IR, optimizer and service interfaces. `quantum/` holds the quantum implementations: gate, annealing, observables (the quantities measured, such as Pauli and fermion operators), plugins and examples. The other folders are `python/` (the Python bindings, built with pybind11), `tpls/` (about 20 bundled third-party libraries such as Boost, Eigen, ANTLR, spdlog and qsim), `docs/`, `docker/`, `cmake/` and `scripts/`. [KNOWN: repo tree]
- Languages: C++ about 96.5% by bytes, plus CMake, Python, C and OpenQASM. [KNOWN: GitHub languages API; the bundled third-party code inflates the C++ share, INFERRED]
- Build: CMake 3.12 or newer, a C++17 compiler, and CURL with OpenSSL. BLAS, LAPACK and Python are optional. [KNOWN: README]
- CI: seven GitHub Actions workflows covering Linux, macOS, Linux on ARM (aarch64), MPI, Python, an Alpine Docker image and Docker deployment. [KNOWN: `.github/workflows/`] I didn't check whether they still pass.
- Contributors: 30 including anonymous commit authors, 21 GitHub accounts without them. Created 2017-09-19. 176 stars and 89 forks. [KNOWN: GitHub API]

## Who uses it / why it matters
XACC was an early attempt at a vendor-neutral quantum software stack from a national lab, which is useful when supercomputing centers want to bolt quantum machines onto classical ones. [INFERRED] Inside our catalog, QIR-EE uses it as an optional backend for hardware runs. [KNOWN: QIR-EE README]

## Related projects
- QIR-EE (`qiree`): depends on XACC optionally. [KNOWN]
- TNQVM (ornl-qci/tnqvm): a tensor-network simulator backend linked from the README. It isn't in our catalog. [KNOWN: catalog row note]

## Known / Inferred / Unknown
- KNOWN: license pair, UT-Battelle copyright, DOE CODE, backends, algorithms, layout, CI files, commit dates, counts.
- INFERRED: step order, what the pulse folders mean, why quiet doesn't mean dead.
- UNKNOWN: current maintenance, what caused the 2024 push, whether CI passes, successor.

## Sources (accessed 2026-10-24)
- https://github.com/eclipse-xacc/xacc (README.md, NOTICE, LICENSE.EPL, LICENSE.EDL, VERSION, xacc/, quantum/, python/, tpls/, .github/workflows/)
- https://api.github.com/repos/eclipse-xacc/xacc (plus /languages, /releases, /tags, /branches, /contributors)
- https://xacc.readthedocs.io (linked, not reviewed in depth)
- https://www.osti.gov/doecode/biblio/5041 (per the catalog row)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Confirmed the DOE CODE record: OSTI API code-5041 is "XACC - eXtreme-scale Accelerator Programming Framework", Software, dated 2017-01-20. OSTI 1339995 has the same title, dated 2016-11-18. Both list ORNL as research org, USDOE as sponsor and contract AC05-00OR22725. The rule 13 citation now points at the OSTI records instead of the catalog row.
- Verified: NOTICE (dual EPL-1.0/EDL-1.0, UT-Battelle 2016-2018, Eclipse trademarks), GitHub API BSD-3-Clause, not archived, created 2017-09-19, pushed 2024-08-13, 0 releases, 0 tags, VERSION 0.1.16, last master commit 2023-08-01 and last xacc-devel commit 2023-03-02 (commit feeds), contributors 30 with anonymous.
- The 2024-08-13 push stays INFERRED as cause unknown. No public page shows which ref it was, so I didn't guess.
- Successor: none found in the public sources checked, so it stays UNKNOWN.
