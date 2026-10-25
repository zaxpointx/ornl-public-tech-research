# Mantid
- Official page: https://www.mantidproject.org
- Repo: https://github.com/mantidproject/mantid
- Docs: https://developer.mantidproject.org (developer docs) and user docs linked from the homepage
- License: GPL-3.0 [KNOWN: LICENSE.txt, https://github.com/mantidproject/mantid/blob/main/LICENSE.txt]
- Status: active, last push 2026-10-24 [KNOWN: GitHub API]

## What it is (plain English, 2-4 sentences)
Mantid is a large open-source program for turning raw data from neutron and muon experiments into results scientists can actually analyze [KNOWN: README]. At a neutron source, a material is hit with a beam of neutrons and detectors record where they scatter. Mantid "reduces" those millions of raw detector counts into clean plots, then helps fit and analyze them [INFERRED: general meaning of "data reduction", consistent with the README]. It's not just an ORNL project. The homepage copyright lists ISIS (UK), ORNL's Neutron Sciences Directorate (NScD), the European Spallation Source, Institut Laue-Langevin, and CSNS (Institute of High Energy Physics, Chinese Academy of Sciences) [KNOWN: https://www.mantidproject.org footer, accessed 2026-10-24].

## How it works (plain English, no jargon without definition)
- The core is a C++ framework of "algorithms", which are small named processing steps like loading a file, correcting for detector efficiency or converting time-of-flight to energy. Users chain these steps together [INFERRED: from Framework/Algorithms, DataHandling and WorkflowAlgorithms folder names].
- Data lives in "workspaces", which are in-memory containers for a dataset as it moves through the steps [INFERRED: Framework/DataObjects and the common Mantid terminology; not confirmed in docs this pass].
- Everything can be scripted in Python, so the same steps can run automatically for each experiment [KNOWN: Framework/PythonInterface exists; Python is 34.5% of the code per GitHub languages].
- "Workbench" is the desktop GUI, built with Qt, a cross-platform GUI toolkit (`qt/` folder) [KNOWN: DEPENDENCY_LICENSES.md mentions Workbench and PyQt].
- `instrument/` holds geometry descriptions of real beamline instruments, so Mantid knows where each detector sits [INFERRED: folder name and the Geometry/NexusGeometry modules].
- LiveData can process data while an experiment is still running [KNOWN: Framework/LiveData exists; "while running" INFERRED from the name].

## How the project is organized (repo structure, languages, build, maintainers/org unit, release cadence)
- Languages: about 64% C++ and 35% Python, plus CMake [KNOWN: GitHub languages API].
- `Framework/` holds the core libraries (API, Kernel, Algorithms, DataHandling, CurveFitting, Crystal, MDAlgorithms, Muon, Reflectometry and more). `qt/` is the GUI and its scientific interfaces. `docs/` and `dev-docs/` are documentation. `instrument/` has the instrument definitions, and `installers/` and `conda/` handle packaging [KNOWN: repo tree].
- Build: CMake (CMakeLists.txt, CMakePresets.json) with pixi/conda for dependencies [KNOWN: repo root files].
- Contributors: about 307 per the GitHub API, counting anonymous ones [KNOWN: contributors pagination, accessed 2026-10-24]. It's by far the biggest community of the six briefs in batch 1.
- Releases: stable versions like v6.16.0 (2026-06-25) and v6.16.1 (2026-07-03), plus frequent nightly-style tagged builds (several in October 2026) [KNOWN: GitHub releases API]. The repo dates from 2011-10-17 [KNOWN: GitHub API].
- It has an OpenSSF Best Practices badge, a security-maturity checklist from the Open Source Security Foundation [KNOWN: README badge, project 4316].
- Software DOI 10.5286/Software/Mantid6.16.1 [KNOWN: CITATION.cff].
- ORNL org unit: NScD (Neutron Sciences Directorate) is named as a copyright holder [KNOWN: homepage footer]. The exact ORNL team is [UNKNOWN].

## Who uses it / why it matters
- Scientists at ORNL's two neutron facilities, SNS (Spallation Neutron Source) and HFIR (High Flux Isotope Reactor), plus partner facilities worldwide [INFERRED: NScD co-ownership and the multi-facility copyright; SNS/HFIR use not directly quoted this pass].
- It's a shared standard, so data handling is consistent across facilities in several countries [INFERRED].

## Related projects
- SNAPRed, the data app for ORNL's SNAP instrument, is built on Mantid: its pyproject.toml routes calls to `mantid.simpleapi` [KNOWN: https://github.com/neutrons/SNAPRed/blob/main/pyproject.toml, accessed 2026-10-24].
- Other repos in the `neutrons` GitHub org likely depend on Mantid [INFERRED].

## Known / Inferred / Unknown
- [KNOWN] GPL-3.0, multi-institution copyright including ORNL NScD, C++/Python, about 307 contributors, active releases since 2011.
- [KNOWN] SNAPRed depends on Mantid.
- [INFERRED] Core use at SNS/HFIR and how the processing chain works.
- [UNKNOWN] What share of development ORNL does versus ISIS, and which ORNL group maintains it.

## Sources (URL, accessed date)
- https://github.com/mantidproject/mantid (README, LICENSE.txt, CITATION.cff, DEPENDENCY_LICENSES.md, tree), accessed 2026-10-24
- https://www.mantidproject.org (footer), accessed 2026-10-24
- https://api.github.com/repos/mantidproject/mantid (+ /languages, /releases, /contributors), accessed 2026-10-24

## Fact-check notes (2026-10-24)
- Corrected: homepage footer lists exactly five copyright holders (ISIS/UKRI, ORNL NScD, ESS, ILL, CSNS/IHEP CAS); removed "and others".
- Retagged: SNAPRed built on Mantid, INFERRED -> KNOWN (SNAPRed pyproject.toml).
- Verified: GPL-3.0, ~64% C++/35% Python, ~307 contributors, created 2011-10-17, v6.16.0/6.16.1 dates, DOI 10.5286/Software/Mantid6.16.1, OpenSSF badge 4316.
- Unverifiable: ORNL's share of development and which ORNL team maintains it.
- No restricted content or implied ORNL affiliation found.

## GOAL.md questions (added 2026-10-24)
- **Who pays (Q3):** the 2014 Mantid paper in Nuclear Instruments and Methods A is on OSTI twice. Record 1149396 lists research org "ORNL, Spallation Neutron Source" and sponsor USDOE Office of Science. Record 1556799 lists sponsor Office of Science, Basic Energy Sciences. [KNOWN: OSTI API, accessed 2026-10-24] It's a multi-institution project, so ORNL's share is the BES-funded part. Other partners' funders aren't covered here. [INFERRED]
- **Where in the tree (Q2):** ORNL, then the neutron facilities (SNS and HFIR), then the shared analysis engine under instrument tools like SNAPRed and PyRS. [KNOWN: their pyproject files]
- **What it teaches about ORNL (Q8):** the lab co-owns a community code with other neutron facilities instead of building its own, then ships ORNL-specific builds through its own conda channels. [KNOWN: multi-institution copyright, `mantid-ornl` channels in SNAPRed and PyRS; INFERRED: the pattern]
- **Student angle (Q9):** this is the most contributor-ready repo in the neutron branch. It has `.github/CONTRIBUTING.md`, issue and PR templates, `SECURITY.md`, dependabot, and Copilot instructions. It has no open issues labeled "good first issue". [KNOWN: GitHub contents and issues API, accessed 2026-10-24] It's a huge C++ and Python codebase, so a student would start with the Python algorithms and docs. [INFERRED]
- **Searched without result (Q10):** an OSTI software record giving current funding, and a breakdown of contributors by institution.
