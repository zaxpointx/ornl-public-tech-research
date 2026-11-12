# Independent referee: energy and Earth systems chapter

Reviewed 2026-11-10. Artifact: [energy-earth.md](energy-earth.md). Read the complete chapter, connection table, source ledger and sweep notes. Independently fetched the three primary sources below and the AutoBEM software metadata. This is a targeted source audit, not a claim that every ExaGO/ReSolve statement or every source was independently rechecked.

## Findings

**No material factual correction found in the checked claims.** The chapter correctly preserves the distinction between published models and a closed generator, Daymet estimates and measurements, and proposed experiments versus executed results. The checked Daymet calendar and radiation rules are particularly important to retain.

| Checked claim | Independent result | Exact primary source and locator |
|---|---|---|
| Daymet leap years include February 29 but omit December 31 | [KNOWN] Confirmed. A consumer must not interpret the series as a no-leap calendar. | [Daymet Daily V4 guide](https://daac.ornl.gov/DAYMET/guides/Daymet_Daily_V4.html), The Daymet Calendar: “December 31 is discarded” |
| `srad` averages over daylight; multiply by `dayl`, not a full day's seconds | [KNOWN] Confirmed. The chapter's invented arithmetic example gives 7.2 MJ/m² correctly; it is explicitly not an observed record. | Same guide, Table 1 shortwave row: “average over the daylight period” |
| Weather files retain separate software/data version attributes and are provisional | [KNOWN] Confirmed. Old file counts in that guide should remain historical examples. | Same guide, Version Information and Data Characteristics |
| Cross-validation withholds variable-station-year records, then compares daily predictions only where observations are present | [KNOWN] Confirmed. Its coverage is the three primary variables, not an independent accuracy guarantee for derived radiation or snow. | [Station-Level Inputs and Cross-Validation V4 guide](https://daac.ornl.gov/DAYMET/guides/Daymet_V4_Stn_Level_CrossVal.html), Application and Derivation: “dropping that record from the input station list” |
| Model America publishes generated artifacts while excluding the metadata used to derive them | [KNOWN] Confirmed. Counts, target simulator versions and ALCF credit agree with the chapter. | [Model America dataset](https://doi.ccs.ornl.gov/dataset/9e968129-1ca9-5a71-93fa-24f009132a3a), Description: “which is not included in this dataset” |
| AutoBEM generator is listed as closed source | [KNOWN] Confirmed by DOE CODE metadata, retrieved through public extraction after browser retrieval returned HTTP 502. | [DOE CODE 115947](https://www.osti.gov/doecode/biblio/115947), Project Type: “Closed Source” |

## Boundaries retained

- [KNOWN] The Model America landing page describes 122,930,327 successful models and targets OpenStudio 3.1.0/EnergyPlus 9.4. Its public description establishes an artifact offering, not an independently tested download or replay. The reviewer did not follow Globus, log in, or retrieve any archive.
- [INFERRED] A future weather-to-building/grid pipeline remains a proposed local composition. Nothing in these checked sources establishes a Daymet -> AutoBEM -> ExaGO production chain.
- [UNKNOWN] The separate 2026 AutoBEM scenario results and ExaGO/ReSolve solver details were read in the chapter but not independently re-fetched in this referee pass. They retain the author's evidence limits; this report must not be cited as universal verification.

## Method and stopping point

Access date for all checked sources: 2026-11-10. The Daymet guides display documentation revision 2024-06-17; Model America displays release 2021-04-14; AutoBEM metadata displays release 2023-11-15. Checked surrounding source text rather than search snippets. No errors needing repair were identified in the sampled claims. More review could deepen solver/build compatibility, but the selected source audit is complete. No shared chapter was edited.
