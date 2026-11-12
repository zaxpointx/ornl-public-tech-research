# INTERSECT and the smart-lab architecture

**Evidence state:** DIRECT for the architecture, CORROBORATED for the cross-facility pattern.
**Primary sources:** [INTERSECT](https://www.ornl.gov/intersect), [INTERSECT projects](https://www.ornl.gov/intersect/projects), [adaptive additive manufacturing](https://www.ornl.gov/projects/enabling-adaptively-controlled-additive-manufacturing-through-automation/). Fetched 2026-10-31. See `../source-ledger.md` entries S01, S02, and S04.

## What ORNL publicly says

ORNL describes INTERSECT as an interconnected "Smart Labs of the Future" initiative. Its public architecture combines self-driving experiments, advanced computing, instruments, facilities, real-time AI/ML feedback, experiment-management software, autonomous science applications, and big-data management.

The public page explicitly names a human-AI-machine interface, experiment-management software, data-driven feedback, and a common secure infrastructure intended to scale across facilities and science domains. [S01]

The project index names an autonomous chemistry lab, AutoFlowS continuous-flow reactor synthesis, adaptive additive manufacturing, open federated architecture, and integration projects. [S04]

## Cross-layer system map

```text
scientific question
  -> experiment or manufacturing process
  -> instrument and sensor streams
  -> edge analysis / AI feedback
  -> HPC or simulation
  -> decision and next action
  -> provenance, data management, and review
```

The adaptive additive-manufacturing project directly connects MDF, OLCF, and SNS. It describes robotics, in-situ characterization, simulations, applied mathematics, and INTERSECT microservices coordinating the workflow. [S02]

## Software layer

Public INTERSECT pages establish the need for experiment-management software, data-management software, workflow tools, and AI/ML integration. They do not identify the complete internal stack. Public software candidates that map to this architecture include Flowcept, DataFed, and Zambeze, but their exact integration with INTERSECT requires repository-level research.

## Facilities and data

- MDF: manufacturing process and in-situ characterization context.
- OLCF: leadership computing and simulation context.
- SNS: neutron-based characterization context.
- Data: process telemetry, images, simulation results, experiment metadata, and provenance.

The exact schemas, APIs, controls, and access rules are UNKNOWN.

## Job families implied by the public record

The architecture requires computer scientists, data scientists, domain scientists, instrument specialists, controls engineers, facilities engineers, technicians, and project managers. ORNL's operations article directly describes F&O workers, instrument technicians, engineers, and skilled trades as participants in autonomous-lab infrastructure. [S05]

## Safe study path

Do not build a physical autonomous lab. Build a synthetic three-stage workflow that represents MDF, OLCF, and SNS as services. Require:

- a provenance record for every transition;
- a human approval gate before the next stage;
- deterministic fixtures instead of real instrument data;
- failure injection and recovery behavior;
- a clear label that the result is a local study proxy, not ORNL software.

## Unknowns

- Complete INTERSECT software inventory
- Internal APIs and control protocols
- Production maturity of each project
- Safety certification and facility-control boundaries
- Which components are public, internal, or partner-restricted
