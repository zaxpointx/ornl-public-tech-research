# Engineering checklist (for "How the project is organized")

Adapted 2026-10-24 from an outside review's engineering-analyst notes. Look only at public artifacts (repo, docs, release pages, package indexes). Never probe a live system (RULES item 16). For each line, write what you saw, with a file path or URL and the commit or release when there is one, or write "not found".

- Repo layout: top-level folders and what each holds
- Languages and the main dependencies (from build or package files)
- Build system and configuration (CMake, setup.py or pyproject, Spack, Makefile, config files)
- Tests: is there a test folder, what kind of tests, how they are run
- CI: which service, what it runs, any machine- or GPU-specific jobs (these feed the signals file)
- Documentation: README, docs site, examples, tutorials
- Releases: tags, release notes, versioning, how often
- Contribution path: CONTRIBUTING file, code of conduct, issue templates, good-first issues
- Data and reproducibility: sample data, notebooks, instructions to reproduce results
- Deployment statements: only what a source says (keep its maturity verb: studied, tested, deployed...)
- Why it was built this way: UNKNOWN unless a public source says so. Observed structure is KNOWN; the reasoning behind it is not.
