# ONCat (ORNL Neutron Catalog)
- Official page: https://oncat.ornl.gov/ (public overview page) [KNOWN]
- Repo: none public found [KNOWN per the catalog note; not re-searched by me]. The public client is published only as a package on PyPI: https://pypi.org/project/pyoncat/
- Docs: the overview page above. It shows a "Release Notes" label, but release notes aren't linked from public pages in a form I followed (logged in not-found.md). Other docs weren't looked for past the public overview, per the editorial limits.
- License: the service has no stated license [UNKNOWN]. The `pyoncat` client package ships a GNU GPL v3 LICENSE file. [KNOWN: `pyoncat/LICENSE` in pyoncat-2.7.tar.gz on PyPI] PyPI's own license field is blank. [KNOWN: PyPI JSON]
- Status: active [KNOWN: the site is live; pyoncat 2.7 uploaded 2026-09-24 UTC, PyPI]
- Scope (rule 13): the site names itself "The ORNL Neutron Catalog" on an ornl.gov domain, for SNS and HFIR data. [KNOWN: https://oncat.ornl.gov/] Owning division: [UNKNOWN].
- Limits on this brief (editorial decision 2026-10-24, rule 16): built only from the public overview page and the public `pyoncat` package files. I didn't call the API, run the client or open any login page. Anything that needs credentials (what's inside the catalog, how sign-in works, who has access) is **out of scope** and isn't described here.

## Plain-language walkthrough
- **What it is:** a catalog (searchable index) of neutron experiment data. The site says it's "the catalog for neutron experiment data at SNS and HFIR". SNS (Spallation Neutron Source) and HFIR (High Flux Isotope Reactor) are ORNL facilities where scientists shoot neutrons at materials to see their structure. [KNOWN: overview page]
- **The problem:** each experiment produces many data files. Scientists need to find, search and download their own runs, and to publish datasets so others can cite them. [KNOWN: overview page mentions browse, download, search and DOIs]
- **What goes in:** metadata about experiments, runs and data files from the facilities. [INFERRED: from the client's resource names, such as Experiment, Run and Datafile]
- **What happens:** the catalog indexes that metadata so people and programs can look it up. It can mint DOIs (Digital Object Identifiers, permanent citable links) for datasets. [KNOWN: overview page]
- **What comes out:** search results, downloads for authorized users, and public DOIs for datasets the team chooses to release. [KNOWN: overview page]
- **Where humans act:** "Experiment teams and instrument staff" browse and search their data, and developers connect their tools through the API. [KNOWN: overview page, quote under 25 words]
- **What it is not:** it isn't open public data. The overview says teams access "their data", and the client has login functions, so most data isn't open to the public. [KNOWN: overview wording; `login`/`logout` methods in `pyoncat/__init__.py`] It isn't the analysis software either (that's Mantid and the reduction tools).
- **What's unknown:** the owning group, and everything behind credentials (out of scope).
- **Example:** after a beamtime, an experiment team searches ONCat for their runs, downloads the files, then mints a DOI for the dataset behind their paper so readers can cite and find it. [INFERRED: a typical sequence built from the features the overview lists]

## How it works (public client only)
- **API client:** `pyoncat` is "A Python Client for ONCat (the ORNL Neutron Catalog)". It needs Python 3.9 or newer, and the PyPI author field says "ONCat Support". [KNOWN: PyPI JSON]
- **Resource model:** the client has classes for Facility, Instrument, Experiment, Proposal, Run, Scan, Sample, Datafile, Reduction, Simulation, Cycle, Archive and more. Each wraps a kind of record with list, retrieve, create, update or remove operations, depending on the type. [KNOWN: class names in `pyoncat/__init__.py`] An *API* (application programming interface) is a defined way for programs to ask a service for data.
- **Reduction files:** `pyoncat/reduction.py` has a `ReductionFileBuilder` for describing a data-reduction run's inputs, outputs and metadata, then validating and writing it to a file. *Reduction* means turning raw detector counts into usable physics data. [KNOWN: method names `add_input`, `add_output`, `validate`, `write`; INFERRED: its role in registering reduced data]
- **Authentication:** the client handles sign-in and stored tokens. How that works isn't described here (out of scope, rule 16).

## How the project is organized
- No public source repo. The client package has two modules (`__init__.py`, about 2,100 lines, and `reduction.py`, about 720), a README, a LICENSE and `pyproject.toml`. [KNOWN: pyoncat-2.7 sdist]
- Client releases: 8 versions on PyPI, from 1.6.2 (2023-09-05) to 2.7 (2026-09-24). [KNOWN: PyPI JSON] Earlier history before 1.6.2 isn't on PyPI's current list. [UNKNOWN]
- Contributors and maintainers: [UNKNOWN] (no public repo).

## Who uses it / why it matters
It's the "find my data" layer for SNS and HFIR users. [KNOWN: overview page] For a security student it's a clean example of a service where the public front door and client code are open while the data behind them is gated, and studying it properly means stopping at that boundary. [INFERRED]

## Related projects
- Mantid (`mantid`), data-workflow (`data-workflow`), post-processing-agent (`post-processing-agent`) and live-data-server (`live-data-server`): all are parts of the neutron data pipeline. A direct ONCat tie in their code is [UNKNOWN]; I didn't grep them for ONCat.

## Known / Inferred / Unknown
- KNOWN: purpose, facilities, DOI feature, API existence, pyoncat client facts (GPL-3.0 file, versions, resource classes).
- INFERRED: data flow into the catalog, the example workflow, the role of reduction files.
- UNKNOWN: owning group, service license, maintainers.
- OUT OF SCOPE (rule 16): anything behind credentials, including catalog contents, access rules and how sign-in works.

## Sources (accessed 2026-10-24)
- https://oncat.ornl.gov/ (public overview page only)
- https://pypi.org/project/pyoncat/ and https://pypi.org/pypi/pyoncat/json
- pyoncat-2.7.tar.gz from PyPI (files read, not run)

## Sweep 2 notes (fact-check pass, 2026-10-24)
- Rechecked the overview quotes (catalog for SNS and HFIR data, "Experiment teams and instrument staff", DOIs, API) on the rendered public page, plus the PyPI JSON (summary, author "ONCat Support", Python 3.9+, blank license, 8 versions 1.6.2 on 2023-09-05 to 2.7 on 2026-09-24) and the 2.7 sdist (GPL v3 LICENSE, module line counts, class and method names, login/logout methods). All verified. Nothing was run, no API was called and no login page was opened.
- Corrected: the Docs line no longer cites a guessed URL. It now says release notes aren't linked from public pages (rule 16 editorial decision).
- Rule 3 check: the brief describes ONCat from the outside and implies no affiliation.
