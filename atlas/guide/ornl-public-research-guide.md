# ORNL Public Research Atlas

**New technical deep dive (2026-11-10):** [Workflow software contracts and local reconstruction](project-dossiers/workflow-software-and-local-reconstruction.md) adds pinned repository research and a runnable synthetic provenance experiment. [Agent entry point](agent-entrypoint.md) provides bounded public-registry context for Codex and Hermes.


**Build:** 0.2 research guide
**Research date:** 2026-10-31
**Scope:** Public ORNL, DOE, OSTI, ORNL Impact, public job postings, public software catalog pages, and public papers. No private, classified, credentialed, or access-controlled sources.

## What this is

This is a connected guide to ORNL's public technical ecosystem. It is not a GitHub scraper and it is not a collection of AI-generated project summaries.

The guide follows five evidence layers:

1. **Research programs and projects:** what ORNL says it is trying to do.
2. **Software and data systems:** what makes the work executable, reproducible, and shareable.
3. **Facilities and instruments:** where experiments, compute, manufacturing, and measurement happen.
4. **Job families and teams:** the people and operational work that make the systems function.
5. **Safe study paths:** smaller, local reconstructions that teach the public architecture without touching ORNL systems or sensitive data.

Each claim is labeled as one of:

- **DIRECT:** stated in a fetched primary source.
- **CORROBORATED:** supported by more than one independent public source.
- **INFERRED:** a bounded connection drawn across direct sources.
- **UNKNOWN:** not established by the public evidence reviewed.

## Executive finding

The strongest public picture is not that ORNL is simply applying AI to science. ORNL is building a **shared control and data layer for science** that connects instruments, laboratories, simulations, leadership computing, cloud resources, networking, provenance, and operations staff.

This is DIRECT in the public INTERSECT description: ORNL lists human-AI-machine interfaces, experiment-management software, autonomous science applications, big-data management, and data-driven feedback as parts of a common infrastructure. It also says the system is intended to scale across facilities and science domains. [S01]

The public job family points to the same operating layer. The WES group is described as building workflow, data, and AI-agent technologies that connect leadership computing with experimental and observational science, while also developing provenance, benchmarking, and AI-ready data capabilities. [S07]

**Bounded interpretation:** ORNL's distinctive capability is increasingly the coordination of heterogeneous scientific systems, not any single model, instrument, or codebase. This is an INFERRED synthesis from the architecture, publication, facility, software, and job sources below.

## 1. The public operating model

### 1.1 INTERSECT is the connective architecture

ORNL describes INTERSECT as an interconnected "Smart Labs of the Future" initiative. Its public architecture includes:

- self-driving experiments using compute, instruments, and facilities;
- multi-domain and multi-modal experiments;
- real-time AI/ML analysis and feedback at the edge;
- a human-AI-machine interface;
- experiment-management software;
- autonomous science applications;
- big-data analysis and management;
- a common, secure infrastructure intended to scale across facilities and science domains. [S01]

The public project page describes the design as a system of systems and microservice architecture connecting instruments, robot-controlled laboratories, edge or center compute, and data resources. [S02]

This matters because it changes the unit of analysis. The interesting object is not "an AI project". It is a loop:

```text
scientific question
  -> instrument or process
  -> data stream
  -> analysis or simulation
  -> decision or control
  -> next experiment
  -> provenance and review
```

### 1.2 The architecture is applied to real facility chains

The public autonomous additive-manufacturing project connects three ORNL user facilities: the Manufacturing Demonstration Facility, the Oak Ridge Leadership Computing Facility, and the Spallation Neutron Source. ORNL says the system combines robotics, in-situ characterization, simulations, and applied mathematics to adaptively control metal-printing processes. [S02]

That is a direct cross-layer connection:

```text
MDF: manufacture or print
  -> OLCF: simulation and compute
  -> SNS: neutron-based characterization
  -> INTERSECT microservices: coordination and feedback
```

The page does not establish every implementation detail, production maturity, or exact data format. Those remain UNKNOWN.

### 1.3 Operations is part of the research system

ORNL's operations-workforce article is unusually useful because it names the infrastructure labor behind autonomous science. It says Facilities and Operations workers include craft workers, skilled trades professionals, facility-maintenance technicians, engineers, and support personnel. The article describes them as helping design, operate, maintain, and evolve the ecosystem for continuous autonomous operations. [S05]

The same article describes instrument technicians wiring equipment to control computers, fabricating control systems, and connecting laboratories into a continuous control network. It quotes the goal of capturing institutional knowledge so systems become safer and more intuitive to operate. [S05]

**INFERRED connection:** A self-driving laboratory is not only a model plus a robot. It is a socio-technical system with electrical, mechanical, facility, controls, networking, safety, data, and software work.

## 2. Major public project families

### 2.1 Autonomous science and smart laboratories

**Direct evidence:** ORNL says autonomous laboratories combine AI, automated experimentation, advanced instrumentation, leadership-class computing, and shared software/data infrastructure. It also explicitly says security, transparency, data governance, cybersecurity, and responsible AI are central concerns. [S03]

**Public projects named by ORNL:**

- Autonomous chemistry lab for accelerated materials discovery
- Autonomous continuous-flow reactor synthesis, or AutoFlowS
- Adaptive additive manufacturing through automation
- Open federated architecture for the laboratory of the future
- Integration projects for combining domain-science technologies into working ecosystems [S04]

The individual public project pages are summarized in [`intersect-project-portfolio.md`](project-dossiers/intersect-project-portfolio.md). That dossier separates science projects from the shared architecture, testing, and deployment work instead of treating every page as the same kind of laboratory.

**What the public record supports:** ORNL is developing reusable infrastructure and multiple domain applications, not one isolated demonstration.

**What remains unknown:** exact control software, internal deployment topology, safety certification, instrument APIs, data schemas, and which components are open source.

### 2.2 Agentic HPC and advanced-manufacturing workflows

The Agentic HPC Pipeline Initiative, or AHPI, is a public ORNL Impact project with collaborators from Lawrence Berkeley National Laboratory, Lawrence Livermore National Laboratory, and Rescale. The project says agents will select appropriate DOE simulation tools, configure and validate inputs, run cloud simulations, and return recommendations. It also describes digital twins as simplified models that companies can continue using. [S10]

The project names three manufacturing challenges: semiconductor plasma processing, compact reactors that convert flare gas to liquid fuel, and longer-lasting turbine parts made through 3D printing. It states a goal of reducing expert time for a full simulation campaign by at least five times. [S10]

That last number is a **project goal**, not a verified result. The public page does not establish that the five-times target has been achieved.

### 2.3 Cross-facility AI-agent architecture

A peer-reviewed ORNL Impact record describes a modular architecture for autonomous cross-facility experimentation. The abstract names four pieces:

- an LLM natural-language interface;
- a multi-agent decision-making framework;
- programmable facility APIs;
- provenance-aware infrastructure for adaptive, explainable, and reproducible workflows. [S09]

The demonstration orchestrated additive-manufacturing experiments through near-real-time coordination between experimental and HPC resources. The evaluation used a **simulated version of the manufacturing facility**, which is important: the public evidence demonstrates an architecture and workflow evaluation, not unrestricted control of a live facility. [S09]

### 2.4 Autonomous neutron experiment steering

The public neutron-workflow paper describes a three-part system:

1. an inference service for real-time AI segmentation of experiment image streams;
2. a continuous-integration service that launches distributed training jobs on Summit using newly collected images;
3. a web service that displays AI-tagged images to experts. [S11]

The paper says feedback could be sent to edge equipment to decide the next experiment, and frames the work as a first step toward real-time experiment steering at ORNL neutron facilities. The source is explicit that the data used resources at HFIR. [S11]

**Important boundary:** the paper is evidence of a research workflow and architecture. It is not evidence that all neutron experiments at ORNL operate autonomously or without experts.

### 2.5 chatHPC and AI for scientific software

The public chatHPC record describes an end-to-end pipeline for building conversational and programmable AI agents on HPC platforms. It includes pretraining, fine-tuning, web/API deployment, and evaluation for coherence, semantic accuracy, hallucination detection, and privacy. The paper reports end-to-end LLM alignment in under an hour on Frontier for its demonstrated pipeline. [S12]

This shows a different layer of the operating picture: ORNL is not only using AI to interpret scientific data. It is studying the engineering pipeline required to make AI assistants usable on HPC systems.

### 2.6 Science-aware network operations

SciNet treats the research network itself as part of the scientific system. Its public project page describes an AIOps platform that combines network telemetry, workflow metadata, and instrument data; predicts network requirements; feeds predictions back into workflow design; and performs root-cause analysis during execution. [S13]

SciNet proposes virtual testbeds and network digital twins, with validation against high-energy-physics workflows and agentic AI workflows on leadership computing facilities. It also introduces a science-specific service-level agreement based on scientific intent rather than only packets, flows, or uptime. [S13]

**Unusual connection:** the network is treated as an active participant in experiment quality and discovery speed, not just plumbing.

## 3. Facilities and data

### 3.1 Public facility map

- **OLCF / Frontier:** leadership computing and scientific-computing expertise. The WES job record places Frontier inside NCCS and describes it as the first supercomputer to break the exascale barrier. [S07]
- **HFIR:** reactor-based neutron source used for materials, chemistry, engineering, biology, and isotope work. [S15]
- **SNS:** accelerator-based neutron source with instruments used across physics, chemistry, biology, materials science, energy, and engineering. [S15]
- **MDF:** advanced-manufacturing environment used in the adaptive additive-manufacturing workflow. [S02]
- **Grid-C and related energy systems:** a search-discovered ORNL INTERSECT page identifies grid-emulation and energy-system workflows as an autonomous-lab application area. This remains a lead pending direct fetch of the page. [S06]

ORNL's user-facilities page says more than 3,200 scientists from universities, laboratories, and private industry conduct experiments at ORNL facilities each year. It presents facilities as a connected set of tools spanning biology, materials and energy sciences, physics, engineering, and chemistry. [S16]

### 3.2 Data types that repeatedly appear

Across the public architecture and job sources, the recurring data objects are:

- instrument and sensor streams;
- images and AI-tagged measurements;
- simulation inputs and outputs;
- workflow telemetry;
- runtime provenance;
- model artifacts;
- experiment metadata;
- network telemetry;
- manufacturing process data;
- data and metadata relationships for AI readiness. [S07][S09][S11][S13][S17]

The public evidence supports the existence of these data categories. It does not disclose ORNL's complete schemas, access controls, retention policies, or private datasets.

## 4. Software and public code

### 4.1 The public software surface

The ORNL Software Catalog describes itself as a hub for open-source projects and says the catalog is updated as repositories are added or modified. [S17]

The current catalog visibly includes software such as:

- **ADIOS2:** data movement and I/O ecosystem
- **DataFed:** federated scientific data management
- **flowcept:** runtime provenance for AI and scientific workflows
- **Zambeze:** distributed task orchestration across large-scale and edge systems
- **TASMANIAN:** adaptive stochastic modeling
- **HydraGNN:** distributed graph neural networks
- **iris:** a unified framework across programming platforms
- **OpenARC:** accelerator research compiler
- **Kelvin:** multiphysics sintering simulation code
- **HeCBench:** heterogeneous-computing benchmark suite [S17]

This list is a catalog observation, not a claim that every project is owned by the same ORNL group or used by every facility.

### 4.2 Software-release boundaries

The catalog FAQ says content should be reviewed and released through ORNL's Software Registration System before placement in an ORNL GitHub repository. It prohibits classified, export-controlled, OUO, HIPAA, PII, NDA/vendor-proprietary, UCI, and UCNI content in public GitHub repositories. [S18]

The licensing guidance says public ORNL repositories should include an ORNL release number in the README, a license, and recommended installation, contribution, and citation information. It also describes DOE CODE as the path through which OSTI assigns software DOIs after submission. [S19]

**Safe-study rule:** A public repository is evidence of a public software surface, not proof that the complete project is public, production-ready, safe for every input, or free of external dependency and license constraints.

## 5. Job families and public teams

### 5.1 Workflow and ecosystem services

The Research Scientist, Agentic Workflows posting describes work on:

- provenance and runtime data capture;
- W3C PROV-aligned provenance models;
- query, storage, and streaming layers;
- cross-facility data lineage;
- platform architecture for OLCF efforts such as OPAL;
- agentic workflow design and autonomous control;
- open-source software leadership;
- scientific-domain support and user training. [S07]

The Group Leader posting describes WES as a research and development group connecting leadership computing with experimental and observational science. It also names efficiency, dependability, trustworthiness, FAIR data, orchestration, provenance, benchmarking, and large-scale distributed execution. [S08]

This makes the job family unusually informative. It reveals that the work is a blend of:

- distributed systems engineering;
- scientific workflow design;
- data engineering and provenance;
- HPC operations;
- AI-agent evaluation;
- open-source maintenance;
- domain-science collaboration;
- mentorship and research publication.

### 5.2 Workflow systems and AI-ready data

The Workflow Systems Group postdoctoral role emphasizes preserving relationships between data and metadata, automating scientific-data ingestion, optimizing the interaction between simulation, data, and AI, and validating distributed intelligence on Frontier. [S14]

### 5.3 Facilities and operations workforce

The autonomous-science operations article identifies craft and skilled-trade workers, facility-maintenance technicians, engineers, instrument technicians, architects, and project managers as part of the autonomous-lab ecosystem. [S05]

**Key lesson:** Job families are not separate from research. They are one of the best public windows into how ORNL turns a scientific idea into a reliable operating system.

## 6. The most important connections

### Connection A: autonomous science requires provenance

INTERSECT emphasizes common infrastructure and feedback. The AI-agent paper adds provenance-aware infrastructure. WES jobs add runtime capture, data lineage, and auditable records. Together, these show that autonomy is paired with traceability rather than treated as unrestricted model control. **CORROBORATED synthesis.** [S01][S07][S09]

### Connection B: facilities are becoming composable services

The adaptive additive-manufacturing project composes MDF, OLCF, and SNS. The agentic-workflow paper describes programmable facility APIs. The job descriptions describe APIs, service meshes, schedulers, data movement, and cross-facility integration. **INFERRED operating model:** facilities are being exposed as coordinated capabilities in a larger workflow, while exact APIs remain unknown. [S02][S07][S09]

### Connection C: operations knowledge is a data asset

The operations article says the goal is to capture institutional knowledge so complex systems become safer and more intuitive. The workflow roles emphasize provenance and runtime capture. **INFERRED connection:** operational know-how is being converted into structured data, automation, and reusable system behavior. [S05][S07]

### Connection D: the public software catalog mirrors the architecture

DataFed, flowcept, and Zambeze map naturally onto the public architecture's recurring needs: data management, provenance, and distributed task orchestration. This does not prove they form one integrated stack, but the alignment is a strong research lead. **INFERRED, not direct integration proof.** [S17]

### Connection E: digital twins are used as both product and test boundary

AHPI describes digital twins as deliverables for manufacturing users. SciNet describes network digital twins for testbeds. The AI-agent paper evaluates orchestration against a simulated manufacturing facility. **CORROBORATED pattern:** simulation and digital twins let teams test complex coordination without immediately controlling live systems. [S09][S10][S13]

## 7. Expanded project families

The first pass focused on autonomous laboratories and scientific workflows. This pass adds five more project families that show how ORNL connects science to real-world systems.

### 7.1 Quantum networking for utilities

ORNL has tested quantum communication on a real commercial fiber network in Chattanooga. In a 2025 demonstration with EPB and the University of Tennessee at Chattanooga, the team sent an entangled quantum signal through multiple wavelength channels and kept it stable for more than 30 hours without an interruption. [S21]

An earlier demonstration with Los Alamos, EPB, and Qubitekk tested quantum key distribution through substations. The public source says the systems had different hardware and software, so getting them to work together was part of the test. [S22]

**Plain-language meaning:** ORNL is studying whether future security tools can work on the same kind of network that carries electricity and communications. This is not proof that the national grid now uses quantum security. It is proof of a public, real-world demonstration with a utility partner.

### 7.2 Nuclear batteries and isotope supply

ORNL's Nuclear Battery Initiative is about power sources that can operate for years in remote places, including deep space. The public work covers the radioactive fuel, energy conversion, heat management, manufacturing, and long-term aging of the hardware. [S23]

This connects to ORNL's wider isotope work. ORNL publicly links isotopes to cancer treatment, security screening, industrial inspection, space missions, energy, and scientific research. [S24]

**Unusual connection:** A retired generator can become a research object. ORNL says Hsin Wang is studying an older radioisotope thermoelectric generator to learn how the materials change over time. That turns old equipment into evidence for designing future systems. [S23]

### 7.3 Biology for materials reuse

A multidisciplinary ORNL team used AI, high-performance computing, synthetic biology, chemistry, imaging, and materials science to search for enzymes that break down nylon 66. The team started with 95 enzymes and reported that 40% showed a natural ability to degrade nylon. [S25]

The goal is not just to destroy waste. The public description says the process could help recover nylon for reuse and possibly recover carbon fiber from composite materials. [S25]

**Plain-language meaning:** ORNL used computers to narrow the search, biology to make and test candidates, chemistry to measure the results, and structural imaging to understand why the best candidates work. This is a clear example of one project crossing several ORNL capabilities.

### 7.4 Grid resilience and wildfire detection

ORNL's AWARE work analyzes electrical waveforms to find dangerous changes that can lead to equipment damage, outages, or wildfires. The public article says the system can classify seven kinds of faults and increased the visible signal strength from 6% to 72% in one test. It used more than 5,700 waveform signatures from the Grid Event Signature Library. [S26]

The project was being checked against five years of field data from Southern California Edison. ORNL also described a planned open-source data-analytics toolbox for utilities and researchers. [S26]

**Plain-language meaning:** the software is intended to turn a hard-to-see electrical signal into a warning that a utility worker can review. The public evidence does not prove that the final system is deployed everywhere or that it can prevent every wildfire.

### 7.5 AI security and cyber resilience

ORNL's Center for Artificial Intelligence Security Research studies weaknesses across the whole AI system, including hardware, software, data sources, physical connections, and human processes. Its public page describes testing at Frontier scale and names tools called Photon and Lantern. [S27]

ORNL is also part of AI-PhyX, a project applying machine learning to electric-grid cybersecurity. The public description covers vulnerability analysis, attack detection, threat mitigation, and recovery. It emphasizes a shared data pool so different security tools can work together instead of producing isolated results. [S28]

A separate technology-transfer example pairs Situ, which finds suspicious behavior in streaming security data, with Heartbeat, which measures hardware power behavior to find signs of malware. ORNL says both technologies were licensed to U2opia. [S29]

**Unusual connection:** ORNL treats trust as a property of the complete system, not just the AI model. That includes the data, the hardware, the network, and the person who must understand the warning.

## 8. Public researchers and teams

The public record now gives a partial people map. It is not a complete ORNL directory.

- **Joseph Chapman and Muneer Alshowkan:** quantum network stabilization and entangled-photon generation. [S21]
- **Brad Johnson and Hsin Wang:** nuclear batteries and long-term generator behavior. [S23]
- **Serena Chen:** computational lead named in the nylon-enzyme study. [S25]
- **Ali Ekti, Ozgur Alaca, Ali Boyaci, Aaron Wilson, and Omer Aziz:** grid waveform and wildfire-detection work. [S26]
- **Jamie Lian, Teja Kuruganti, and Yan Liu:** AI-PhyX electric-grid cybersecurity. [S28]
- **John Goodall and Stacy Prowell:** Situ and Heartbeat cyber-resilience technologies. [S29]

These names should be read narrowly. A source may establish that someone led one study or developed one tool. It does not automatically establish that they lead an entire ORNL division or that their current role is unchanged.

A fuller people map requires separate official staff profiles, publication records, and project pages. The current map is filed in [`public-researchers-and-teams.md`](public-researchers-and-teams.md).

## 9. New cross-project connections

### Connection F: ORNL tests advanced ideas in real operating environments

The quantum work uses a commercial utility network. The grid work uses utility waveform data. The autonomous-manufacturing work joins multiple user facilities. These are different fields, but they share a pattern: ORNL tries to test research where reliability, timing, and compatibility matter, not only in isolated laboratory demonstrations. **CORROBORATED pattern.** [S02][S21][S26]

### Connection G: the same public data loop appears in science and infrastructure

In autonomous science, data helps choose the next experiment. In grid resilience, waveforms help choose the next operational response. In AI security, telemetry helps identify suspicious behavior. **INFERRED connection:** ORNL repeatedly builds systems that turn raw signals into a reviewed decision, with the consequences of that decision treated as part of the research problem. [S01][S09][S26][S28][S29]

### Connection H: technology transfer is part of the research path

The public records show two routes out of the laboratory: public software catalogs and licensed technologies. The catalog makes selected software discoverable under release rules. The Situ and Heartbeat example shows a different route in which ORNL technologies move to a company through licensing. **DIRECT plus INFERRED synthesis.** [S17][S18][S19][S29]

### Connection I: aging and failure are research inputs

The nuclear-battery work studies an old generator's degradation. The grid work studies weak electrical events before they become failures. The autonomous-workflow work includes retries, provenance, and review. **INFERRED connection:** ORNL's public systems research is not only about peak performance. It also studies how systems behave when they age, drift, fail, or produce uncertain results. [S09][S23][S26]

## 10. Deeper evidence about the operating system

### 10.1 INTERSECT is a real program with several working demonstrations

The public record now goes beyond a high-level vision statement. In a 2023 demonstration, ORNL showed a sample-moving robot, a catalyst-development robot, and the AutoFlowS continuous-flow chemistry system. ORNL said the initiative had been established in 2022 and was building core infrastructure that other scientists could use. [S30]

AutoFlowS is described as a system that can design and carry out a viable chemical pathway. Its stated loop runs from hypothesis generation through experiment design, physical execution, analysis, and interpretation. [S31]

In 2025, ORNL reported version 1.0 of the INTERSECT architecture specification. The public description names three parts: use-case patterns, a system-of-systems architecture, and a microservice architecture. It also says the architecture is designed to connect instruments and robot labs to edge, cloud, and high-performance computing resources, with digital twins available for testing. [S32]

**What this changes:** INTERSECT should be understood as a growing program with public demonstrations and a published architecture, not only as a future-looking slogan. The public record still does not reveal every implementation detail or establish that all components are production-ready.

### 10.2 The data layer is not optional support work

The DataFed paper describes a distributed data-management system that spans storage at multiple scientific facilities while letting each facility keep control of its own storage. It includes interfaces for people and workflows, metadata and provenance, and reliable staging of the right data to the right environment. [S40]

The ADIOS 2 publication record places high-performance scientific data management in the same public ecosystem. The record identifies the work as a 2020 SoftwareX publication with a DOI and a large multi-institution author list. [S41]

**Plain-language meaning:** ORNL's computing story is not just “run a bigger simulation.” It also includes moving, describing, finding, and preserving the data that connects experiments, simulations, and teams.

### 10.3 Facilities are public resources with a formal access boundary

ORNL lists HFIR, MDF, CNMS, OLCF, and SNS among its user facilities and says more than 3,200 scientists use its facilities each year. Access is described as proposal-based and subject to scientific review, facility suitability, DOE objectives, and user agreements. [S34]

VENUS gives a concrete example of what a facility contributes. It is a hyperspectral neutron-imaging beamline at SNS used for energy materials, additive manufacturing, biology, transportation, geoscience, forensics, and other work. Its time-of-flight methods can support energy-selective imaging and shorten acquisition from days to hours in the described use cases. [S33]

This is why the atlas must separate **publicly documented capability** from **personal access**. A facility can be publicly described and available through a formal user program without being something a student can directly connect to or operate.

### 10.4 ORNL's history explains the repeated pattern

The public timeline links early nuclear work to radioisotopes, neutron science, mathematics and computing, parallel computing, user facilities, manufacturing, and exascale computing. It records the first radioisotope shipment in 1946, the early computing section in 1947, HFIR in 1965, OLCF in 2004, SNS in 2006, MDF in 2012, and Frontier's exascale milestone in 2022. [S35]

**Bounded interpretation:** ORNL's present-day cross-layer work did not appear from nowhere. The lab has repeatedly turned a mission-specific capability into a shared research platform. The historical record supports that pattern, but it does not prove that every current program is a direct continuation of one earlier project.

### 10.5 The public team map is becoming more precise

Ben Mintz's official profile identifies him as INTERSECT director and describes the program as connecting high-performance computing, edge computing, data analysis, and experimental instruments. [S36]

Daniel Rosendo's profile identifies a WES/NCCS research role focused on the Instrument-to-Edge-to-HPC Continuum, cross-facility workflows, agentic AI, FAIR workflows, benchmarking, and provenance. Tyler Skluzacek's profile describes automated workflows, scientific data management, secure programmatic access to OLCF computing, and Globus Compute. [S37][S38]

These are useful public role signals because they show the work is carried by several specialties: program leadership, workflow research, data management, secure access, and facility integration. They still do not constitute a complete ORNL organizational chart.

## 11. Safe study and reconstruction tracks

These are secondary to the research guide. They are ways to understand the public architecture, not attempts to reproduce ORNL's internal systems.

### Track 1: provenance-aware workflow notebook

Use synthetic jobs that generate files, metrics, model artifacts, and decisions. Record lineage, timestamps, inputs, outputs, retries, and human approval. Compare the result to the public WES/Flowcept concepts without claiming implementation equivalence.

### Track 2: simulated facility chain

Model MDF, OLCF, and SNS as three synthetic services. Send a manufactured-part record through print, simulation, and characterization stages. Inject failures and measure whether the workflow preserves provenance and stops safely.

### Track 3: neutron-image steering toy system

Use public or synthetic image fixtures. Build segmentation, confidence scoring, human review, and next-step recommendation. Do not connect to instruments, use restricted images, or automatically control hardware.

### Track 4: software-catalog study

Before installing any candidate repository, inspect its README, license, release identifier, citation metadata, dependencies, test instructions, and data requirements. Start with documentation or source inspection. Do not assume catalog listing means production readiness.

### Track 5: network digital twin

Build a local graph of synthetic facilities and links. Replay telemetry, inject latency or link failure, and compare science-level outcomes such as experiment delay and retry count. This studies the SciNet idea without touching real infrastructure.

## 12. Unknowns and research gaps

The public evidence reviewed here does not establish:

- the complete INTERSECT software stack;
- exact facility APIs or internal microservice names beyond public examples;
- whether every catalog project is actively maintained;
- private datasets, PHI, PII, export-controlled data, or classified work;
- internal team ownership of every project;
- production deployment status for each autonomous workflow;
- exact performance gains beyond stated project goals and reported paper results;
- the full list of public researchers and current responsibilities;
- which components can be installed safely without repository-by-repository review.

## 13. Research backlog

The next research passes should deepen the guide in this order:

1. Fetch every project page under the INTERSECT projects index and create one dossier per project.
2. Inspect the public repositories for flowcept, DataFed, Zambeze, ADIOS2, and the other catalog entries, recording license, release, citation, dependencies, and activity without using stars as evidence.
3. Build a staff and team map from official ORNL profiles and publication records, keeping job title, authorship, and project leadership separate.
4. Expand the facilities map with official user-facility pages, instrument pages, access rules, and public data or virtual-tour resources.
5. Search OSTI and DOE CODE for project-linked reports, software records, DOIs, and technical artifacts.
6. Convert verified relationships into the machine-readable registry and leave blocked or lead sources explicitly labeled.

The quantum, nuclear, polymer, grid, and AI-security lanes are now covered by a first direct-source pass. They still need deeper project pages, technical reports, software records, and researcher profiles before they can be considered complete.

## Source key

Full URLs, retrieval state, local provenance, fetch date, and supporting excerpts are in [`guide/source-ledger.md`](source-ledger.md).
