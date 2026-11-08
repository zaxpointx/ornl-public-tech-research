# Public research relationships: an evidence-bounded index

This is an independent, selected index of relationships already explained in the [human-readable guide](public-research-guide.md), not a map of live infrastructure, a staff hierarchy, or a complete knowledge graph. It is a regular Markdown table that people and automated readers can both navigate. Each row is one narrowly worded proposition; direction is expressed in the relationship itself, not assumed from the order of names. The [evidence ledger](public-research-sources.md) supplies directly read public URLs, short quotes, fetch dates, source maturity and limits. Sources have individual fetch dates, and some reports are historical or describe targets rather than present operations.

Status key: **DIRECT** = a source explicitly supports the exact proposition; **INFERRED** = our bounded synthesis of stated facts, not an additional source assertion; **UNKNOWN** = the identified relationship is not established by the sources cited, not a claim that no relationship exists. A source can document a plan, a capability or a past event directly without proving current operation. Professional credits concern only the exact published role or authorship; they do not establish a current appointment.

| ID | Subject | Relationship | Object | Status | Evidence | Boundary |
|---|---|---|---|---|---|---|
| R01 | INTERSECT autonomous additive manufacturing | reported deployed across | MDF, SNS and OLCF | DIRECT | S05, S06 | Reported research deployment; precise machine, current operation and independent performance are unknown. |
| R02 | INTERSECT additive workflow | targets | residual-stress improvement | DIRECT | S06 | Target, not a demonstrated result or completed qualification. |
| R03 | OpeN-AM reported experiment | used | VULCAN at SNS | DIRECT | S11 | Specific experiment on steel; it does not establish universal manufacturing performance. |
| R04 | OpeN-AM platform | designed and built at | MDF | DIRECT | S11 | Platform history, not proof the experiment was the INTERSECT deployment. |
| R05 | OpeN-AM experiment | same implementation as | INTERSECT additive workflow | UNKNOWN | S05, S11 | Similar facilities or scientific interests do not establish identity. |
| R06 | Myna | initially developed for | Peregrine database structure | DIRECT | S12 | Its use in the INTERSECT additive workflow remains unknown. |
| R07 | pyRS | supports automated data reduction for | HIDRA | DIRECT | F02, F10, F11 | Documented capability and workflow, not every measurement or live status. |
| R08 | specific post-processing-agent chain | invokes | HIDRA pyRS workflow | UNKNOWN | S14, F02, F10, F11 | The cited records do not establish this caller relationship. |
| R09 | HIDRA and isotope production | share | HFIR as an institutional facility context | INFERRED | F02, F07, S18 | Shared facility context does not establish a shared experiment, isotope campaign or data flow. |
| R10 | Cyberwheel software | includes | simulation and emulation capabilities | DIRECT | S10 | Software description, not a claim of production network deployment. |
| R11 | Cyberwheel 2024 paper | reports | initial simulated cyber-deception agent results | DIRECT | S09 | Results concern simulation; real-network deployment is not established. |
| R12 | 2022 ferroelectric active-learning paper | same implementation as | 2023 INTERSECT microscope-twin demonstration | UNKNOWN | A01, A04 | Similar feedback concepts are not evidence of shared software or instruments. |
| R13 | AutoFlowS reactor development | supported by | INTERSECT initiative | DIRECT | A06 | Research funding/development support; shared software with microscopy remains unknown. |
| R14 | 2022 ferroelectric paper and 2023 AutoFlowS paper | share | author Rama K. Vasudevan | DIRECT | A01, A06 | Shared authorship does not prove shared leadership, instrument or implementation. |
| R15 | 2022 ferroelectric paper and 2023 AutoFlowS paper | related as | examples of adaptive scientific research | INFERRED | A01, A06 | Conceptual comparison only; specific operational linkage is unknown. |
| R16 | Radioisotope Development Laboratory and HFIR | connected by | the reported actinium-227 pathway | DIRECT | S18 | Particular high-level pathway as described in the 2026 factsheet, not a facility layout or all campaigns. |
| R17 | ORNL-supplied actinium-227 | source of | radium-223 in the historical medical supply account | DIRECT | I01, I02 | Distinct isotopes; no assertion about current supply or treatment suitability. |
| R18 | californium-252 validation study | used | Shift and ORIGEN among its calculation codes | DIRECT | I04 | Use in that published study only, not in every production campaign. |
| R19 | ORNL's Frontier | used for | 2024 award-winning quantum molecular dynamics calculation | DIRECT | D03, D04 | A reported simulation by a multi-institution team, not a measured physical experiment. |
| R20 | Stephen DeWitt | listed as principal investigator of | specific INTERSECT additive-manufacturing project | DIRECT | S06 | Architecture-documentation designation as fetched, not proof of a present appointment or leadership of all INTERSECT. |
| R21 | 2024 model-protein paper | reports experiments performed at | BASIS spectrometer at SNS | DIRECT | N01 | One research study, not a clinical result or proof of current instrument use. |
| R22 | NOMAD data-challenge record | describes measurements made at | NOMAD at SNS | DIRECT | N03 | Public metadata was read; data files, access and reuse terms were not checked. |
| R23 | NOMAD data-challenge dataset | used by | 2024 BASIS model-protein paper | UNKNOWN | N01, N03 | Shared facility and neutron methods do not establish a dataset or workflow dependency. |
| R24 | Cyberwheel 2024 software output | listed on | Cybersecurity Research directory page associated with National Security Sciences | DIRECT | Z01 | Research-output listing as fetched, not proof of administrative ownership or live deployment. |
| R25 | Cyberwheel software and AI ATAC 1 paper | share | an ORNL Cybersecurity Research output listing | DIRECT | Z01 | Listing together does not establish integration or a common deployment. |
| R26 | 2025 INTERSECT additive demonstration | used | adamantine and Flowcept | DIRECT | H02 | The printer and sensing service were simulated; it does not establish use in every INTERSECT workflow. |
| R27 | 2025 simulated-printer demonstration | same implementation as | three-facility additive deployment | UNKNOWN | H02, S05 | Shared initiative or a common tool does not establish identity or a neutron-measurement link. |
| R28 | SPRUCE environmental dataset version 2.0 | supersedes and corrects | previous versions of the same dataset | DIRECT | E01 | Dataset metadata says the revision was released in 2026; files and reuse terms were not independently examined. |
| R29 | ORNL Cyberwheel v2.0 | supports emulation using | Sandia-developed FIREWHEEL | DIRECT | X01, X02 | Public release and repository descriptions, fetched 2026-11-07; no joint team, live deployment, current compatibility or personal run is established. |
| R30 | LLNL ExaCA | lists as an optional heat-transport model for coupled simulation | ORNL Finch | DIRECT | X03–X06 | A documented optional coupling, not evidence of a particular run, experimental validation or the INTERSECT workflow. Existing project briefs already record this connection. |

## How to use this index

Read the cited ledger entries before treating a row as a fact. `UNKNOWN` edges are research questions, not missing facts to fill by assumption; `INFERRED` edges must not be silently promoted to direct relationships. This selected table does not replace the existing project-level [catalog](../INDEX.md), [SNS pipeline](../deep-dives/sns-neutron-pipeline.md), [Cyberwheel synthesis](../deep-dives/cyberwheel/synthesis.md), [autonomy story](autonomous-science.md), or [isotope story](isotopes-and-hot-cells.md). Coverage remains incomplete; dates and maturity may need rechecking as public sources change.
