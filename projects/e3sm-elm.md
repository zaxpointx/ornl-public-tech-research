# E3SM Land Model (ELM)
- Official page: https://e3sm.org/
- Repo: https://github.com/E3SM-Project/E3SM. ELM lives in `components/elm/` inside the full E3SM repo [KNOWN: repo tree].
- Docs: ELM user, developer and technical guides in `components/elm/docs/` (index.md) [KNOWN]. They're early, and the index still has placeholder intro text [KNOWN: docs/index.md].
- License: BSD-3-Clause for E3SM, copyright UChicago Argonne, with some separable parts under other licenses [KNOWN: discovery-pass check of https://raw.githubusercontent.com/E3SM-Project/E3SM/master/LICENSE].
- Status: active, the E3SM repo was pushed 2026-10-24 [KNOWN: catalog/GitHub API].

## What it is (plain English, 2-4 sentences)
E3SM (Energy Exascale Earth System Model) is the Department of Energy's own climate model. It simulates the atmosphere, ocean, ice and land together on supercomputers [KNOWN: e3sm.org; Phase 1 page]. ELM is the land part. It models what happens on and under the ground surface, like soil water, plants growing and dying, snow, and carbon moving between plants, soil and air [INFERRED: from ELM source folders `biogeophys`, `biogeochem` and `dyn_subgrid`; the docs don't summarize this yet]. Other parts of the model need this, because land shapes how heat, water and carbon flow into the atmosphere.

## What exactly is ORNL's part?
This is an editorial question, and here's what the public record supports:
- [KNOWN] ORNL is one of the eight DOE labs in E3SM and has been since it started (as "ACME") [KNOWN: https://e3sm.org/about/organization/phase-1/]. ORNL is listed as an E3SM lab on every e3sm.org page footer [KNOWN].
- [KNOWN] ORNL is a research org on specific ELM work. One example is a 2026 journal article on running ELM at kilometer scale over North America, with Argonne, OSTI 3649369, DOI 10.1177/10943420261446003 [KNOWN: OSTI records API]. Another is the 1 km vegetation and land-unit input datasets for ELM (V1 and V2), published under OLCF DOIs, 10.13139/OLCF/3005830 (OSTI 3005830) and 10.13139/OLCF/3364821 (OSTI 3364821) [KNOWN: OSTI records API]. A third is an ELM uncertainty-quantification paper, with Brookhaven and the ORNL ARM Data Center [KNOWN: OSTI records API].
- [KNOWN] DOE CODE's E3SM software records list the developer as "E3SM Project, DOE" rather than any single lab [KNOWN: discovery-pass check of OSTI 148889/123310].
- [UNKNOWN] Whether ORNL leads or co-leads the E3SM land group, and which ORNL division does the work. I couldn't find a public page naming land-group leads. The leadership charts on the e3sm.org organization pages didn't come through as text.
- [INFERRED] ORNL's land contributions likely come from its Environmental Sciences Division, which also produces Daymet, a forcing dataset for land models. That's not confirmed for ELM.
- Bottom line: ELM is a multi-lab code. ORNL is a documented contributor to ELM research, input data and scaling work, but the public sources we found don't let us say ORNL "owns" ELM.

## How it works (plain English, no jargon without definition)
- ELM divides each grid cell of the Earth into sub-areas, such as forest, crops, lake, urban and glacier, and tracks each one separately. That's "subgrid" tiling, and `dyn_subgrid` handles how those areas change over time, like land-use change [INFERRED: folder names and general land-model design].
- `biogeophys` covers physical processes like energy, water and snow. `biogeochem` covers chemical and biological processes like carbon and nitrogen cycling in plants and soil [INFERRED: folder names].
- `external_models/` plugs in outside models. One is FATES, a more detailed vegetation-demographics model that tracks individual plant size and age groups. The other is EMI, an interface for attaching other external models [KNOWN: folder contents; FATES description general background, see the fates catalog row].
- It can run coupled inside full E3SM or on its own in "coupler-bypass" mode [KNOWN: docs/index.md].

## How the project is organized (repo structure, languages, build, maintainers/org unit, release cadence)
- `components/elm/` contains `src/` (with biogeochem, biogeophys, cpl (coupling to the rest of E3SM), data_types, dyn_subgrid, external_models, main and utils), plus `bld`, `cime_config` (build and config hooks for CIME, E3SM's case-setup system), `docs`, `test` and `tools` [KNOWN: GitHub contents API].
- Language: E3SM overall is about 79% Fortran and 10% C++ [KNOWN: GitHub languages API for E3SM-Project/E3SM]. ELM is mostly Fortran [INFERRED: E3SM language mix; not measured for ELM alone].
- Releases follow E3SM versions. DOE CODE lists v3.0.0 and v3.0.2 [KNOWN: OSTI check in the discovery pass].
- Maintainers: E3SM Project, multi-lab [KNOWN]. ORNL's specific team is [UNKNOWN].

## Who uses it / why it matters
- DOE uses E3SM to study climate questions relevant to energy, such as water availability and land-use effects [INFERRED: e3sm.org article topics like irrigation and groundwater].
- Land-surface feedbacks (plants, soil carbon, snow) are among the biggest uncertainties in climate projections, so the land model matters a lot [INFERRED: general climate-science context].

## Related projects
- fates (catalog row) is embedded in ELM through `external_models/fates` [KNOWN: folder].
- Daymet is a likely forcing data source [INFERRED].
- OLCF hosted the ELM 1 km input datasets (OLCF DOI) [KNOWN: OSTI].

## Known / Inferred / Unknown
- [KNOWN] ELM's location in the E3SM repo, its folder structure, coupler-bypass mode, FATES/EMI hooks, ORNL as a founding E3SM lab, and ORNL as a research org on specific ELM papers and datasets.
- [INFERRED] The process descriptions, Fortran share, and ESD as ORNL's home for the work.
- [UNKNOWN] Who leads the land group and ORNL's share of ELM code. A next step could be checking the land-group leadership text on e3sm.org or ELM tech-guide authors.

## Sources (URL, accessed date)
- https://e3sm.org/about/organization/phase-1/, accessed 2026-10-24
- https://github.com/E3SM-Project/E3SM/tree/master/components/elm (via the GitHub contents API), accessed 2026-10-24
- https://raw.githubusercontent.com/E3SM-Project/E3SM/master/components/elm/docs/index.md, accessed 2026-10-24
- https://www.osti.gov/biblio/3649369; OSTI records API queries "E3SM Land Model" and "Gridded Vegetation and Land Unit Datasets", accessed 2026-10-24

## Fact-check notes (2026-10-24)
- Corrected: the 1 km vegetation/land-unit datasets have two OSTI records (3005830 and 3364821), both ORNL. The brief cited only one DOI for V1 and V2.
- Verified: e3sm.org Phase 1 page names eight labs including Oak Ridge at ACME's start; the e3sm.org homepage links ornl.gov in its lab list; OSTI 3649369 is ANL + ORNL, DOI 10.1177/10943420261446003; OSTI 3025805 is BNL + ORNL ARM Data Center.
- Another ORNL example for later: OSTI 3022692, ELM runoff evaluation for Alaska permafrost (LANL + ORNL).
- Verified: LICENSE is BSD-3, copyright 2024 UChicago Argonne; components/elm and src folder lists match; external_models holds emi and fates; docs/index.md has placeholder intro and mentions Coupler-bypass mode; languages Fortran 79.4 / C++ 10.1.
- Land-group leadership stays [UNKNOWN]. ORNL 'owns ELM' is not supported by anything found, and the brief correctly doesn't claim it.
