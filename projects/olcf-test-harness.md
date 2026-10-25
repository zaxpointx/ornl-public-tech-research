# OLCF Test Harness (OTH)
- Official page / Docs: https://olcf.github.io/olcf-test-harness/ [KNOWN: README, GitHub API homepage]
- Repo: https://github.com/olcf/olcf-test-harness. Sample tests are in https://github.com/olcf/olcf-test-harness-examples [KNOWN: README].
- License: a UT-Battelle BSD-3-style license, copyright 2025 UT-Battelle, LLC. It adds a clause allowing administrative-cost fees for redistribution but banning royalties beyond cost recovery [KNOWN: LICENSE file, https://github.com/olcf/olcf-test-harness/blob/devel/LICENSE]. GitHub shows NOASSERTION because of that extra clause [INFERRED].
- Status: active, last push 2026-10-16, v3.2 released 2026-09-10 [KNOWN: GitHub API]
- DOE CODE: DOI 10.11578/dc.20250328.1, ORNL-CODE-153320 [KNOWN: README]. OSTI lists the research org as ORNL, and the listed developers are affiliated with ORNL's National Center for Computational Sciences (NCCS) [KNOWN: OSTI records API, code-153320].

## What it is (plain English, 2-4 sentences)
OTH is the tool OLCF uses to automatically test its supercomputers. It builds real science applications, submits them as jobs, and checks that the results are correct and fast enough [KNOWN: docs overview.rst; README]. The docs call it a lightweight templating framework that can run tests one at a time or keep a large set running continuously to simulate a real production workload [KNOWN: overview.rst]. In practice it's how a brand-new or upgraded machine like Frontier gets checked before users rely on it [INFERRED: the README's centralized install path is `/sw/acceptance/...`, and the catalog row calls it acceptance testing; "acceptance" is how HPC centers sign off on new systems].

## How it works (plain English, no jargon without definition)
- Each test is a small folder with three scripts: build the program, run the job, and check the output [KNOWN: overview.rst].
- You write an input file (`rgt.inp`) that lists which application tests to run, then call `runtests -i rgt.inp --mode start stop` for one round, or `--mode start` to keep resubmitting continuously [KNOWN: README, overview.rst].
- A machine config file (`.ini`) tells the harness about the system. Shipped examples are Frontier, Summit (Frontier's predecessor), and Frontier variants for Kubernetes and OpenShift [KNOWN: configs/olcf_examples].
- It submits jobs through the machine's job scheduler. A scheduler is the queue system that decides when your job gets nodes. It supports Slurm, LSF and PBS, plus Kubernetes and OpenShift for container platforms [KNOWN: harness/schedulers folder].
- After each run, a check script writes `output_check.txt` with pass/fail for correctness and performance. Results are archived under `Run_Archive/latest` [KNOWN: README]. Results can also be logged to a database [KNOWN: harness/libraries/rgt_database_loggers].
- The README's example runs LAMMPS, a molecular-dynamics code, on one Frontier node [KNOWN: README].

## How the project is organized (repo structure, languages, build, maintainers/org unit, release cadence)
- Languages: about 95% Python, plus small amounts of batch, Make and shell [KNOWN: GitHub languages API].
- `harness/bin/` has the entry points (runtests.py, test_harness_driver.py). `harness/libraries/` has the core logic (test objects, config parsing, status files, database loggers, output hub). Then there's `harness/machine_types/`, `harness/schedulers/`, `configs/`, `modulefiles/` (so it loads as an HPC environment module), `doc-sphinx/` (docs source), `tests/` and `scripts/` [KNOWN: repo tree].
- Build: `pyproject.toml`. It's loaded through `module load olcf_harness` or by adding it to PATH [KNOWN: README].
- Releases: v2.1 (2021-02-27), v3.0 (2025-03-31), v3.1 (2025-07-28) and v3.2 (2026-09-10) [KNOWN: GitHub releases API]. The README says v3.2 is expected to be the final version fully backward-compatible with 2.x [KNOWN: README note]. What the next major version changes isn't stated [UNKNOWN].
- Contributors: about 28 per the GitHub API, counting anonymous ones [KNOWN].
- Org unit: NCCS (National Center for Computational Sciences) at ORNL, per the developer affiliations on the OSTI record [KNOWN]. The repo is in the `olcf` org [KNOWN]. The docs' original file header calls it the "NCCS_Test_Harness", created 2016 [KNOWN: doc-sphinx/source/index.rst], so it predates the 2021 GitHub repo [INFERRED].

## Who uses it / why it matters
- OLCF staff testing systems like Frontier, and anyone running a test suite on an HPC cluster, since it supports adding new machines [KNOWN: README mentions adding a new machine; staff use INFERRED].
- Running suites continuously catches hardware or software problems after upgrades before they hit researchers [INFERRED].

## Related projects
- Tests run on the OLCF systems documented in olcf-user-docs [INFERRED].
- Same facility as DataFed's central services (OLCF) [KNOWN: DataFed docs].
- HeCBench (benchmarks) is a possible test source [INFERRED: not checked].

## Known / Inferred / Unknown
- [KNOWN] Purpose, build/run/check model, schedulers, machine configs, releases and the v3.2 compatibility note, NCCS research org, DOE CODE DOI, custom BSD-3-style license.
- [INFERRED] Its role in acceptance testing new systems, and its pre-2021 history.
- [UNKNOWN] Which test suites OLCF actually runs in production. Those aren't in the public repo.

## Sources (URL, accessed date)
- https://github.com/olcf/olcf-test-harness (README, LICENSE, doc-sphinx/source/index.rst and user_guide/overview.rst, tree), accessed 2026-10-24
- https://api.github.com/repos/olcf/olcf-test-harness (+ /languages, /releases, /contributors), accessed 2026-10-24
- https://www.osti.gov/biblio/code-153320 (via the catalog note), accessed 2026-10-24

## Fact-check notes (2026-10-24)
- Corrected: README doesn't mention a v4.0; it only says v3.2 is the last fully 2.x-compatible version.
- Corrected: OSTI's research_orgs field says ORNL only; NCCS comes from the developer affiliations on the same record.
- Verified: LICENSE text (2025 UT-Battelle, cost-recovery clause); releases v2.1, v3.0, v3.1, v3.2 with dates; created 2021-01-11; Python 94.7%; 28 contributor pages; DOI 10.11578/dc.20250328.1 and ORNL-CODE-153320 in README; schedulers (slurm, lsf, pbs, k8s, openshift); configs (frontier, frontier_k8s, frontier_openshift, summit); index.rst 'NCCS_Test_Harness' created 2016; overview.rst 'light-weight templating framework'; rgt.inp, --mode, output_check.txt, Run_Archive/latest, LAMMPS example.
- The /sw/acceptance path is from the public README, not restricted material.
