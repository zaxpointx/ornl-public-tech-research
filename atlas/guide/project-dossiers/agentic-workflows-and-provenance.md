# Agentic workflows, provenance, and AI-ready science

**Evidence state:** DIRECT for public role and paper descriptions; INFERRED for the common operating model.
**Primary sources:** [Agentic workflows job](https://jobs.ornl.gov/job/Oak-Ridge-Research-Scientist%2C-Agentic-Workflows-TN-37830/1422626200/), [WES group leader job](https://jobs.ornl.gov/job/Oak-Ridge-Group-Leader-Workflow-and-Ecosystems-Services-TN-37830/1428494800/), [AI agents paper](https://impact.ornl.gov/en/publications/ai-agents-for-enabling-autonomous-experiments-at-ornls-hpc-and-ma/), [AHPI](https://impact.ornl.gov/en/projects/agentic-hpc-pipeline-initiative-ahpi-ai-driven-orchestration-of-d/). Fetched 2026-10-31. See `../source-ledger.md` entries S07, S08, S09, and S10.

## What the public evidence establishes

The WES job record places agentic workflow research inside NCCS and describes workflows that bridge leadership computing, instruments, and cloud platforms. It names provenance capture, W3C PROV-aligned models, data lineage, query/storage/streaming layers, open-source software leadership, and autonomous control systems. [S07]

The WES group-leader record describes workflow, data, and AI-agent technologies connecting leadership computing with experimental and observational science. It adds FAIR data, benchmarking, trustworthiness, and reliability at scale. [S08]

The peer-reviewed paper describes a modular architecture with an LLM interface, multi-agent decision making, programmable facility APIs, and provenance-aware infrastructure. Its evaluation uses a simulated manufacturing facility. [S09]

AHPI extends this pattern toward manufacturing simulation expertise. It describes agents that choose tools, configure and validate inputs, run simulations, return recommendations, and build digital twins. [S10]

## Actual job family

This is not a generic "prompt engineer" role. The public descriptions combine:

- distributed workflow systems;
- HPC schedulers and execution environments;
- data movement and APIs;
- provenance and runtime telemetry;
- AI-agent planning and tool use;
- open-source release and maintenance;
- scientific-domain collaboration;
- benchmarking and evaluation;
- documentation, training, and user support.

## Control-plane interpretation

A bounded interpretation of the public evidence is:

```text
intent
  -> plan
  -> select tool or facility
  -> validate inputs
  -> execute
  -> capture provenance
  -> inspect results
  -> adapt or stop
```

This is an INFERRED synthesis. The public sources establish the components and responsibilities, not one complete internal runtime.

## Software layer

The public ORNL catalog lists Flowcept as runtime provenance for AI and scientific workflows, DataFed as federated scientific data management, and Zambeze as distributed task orchestration. The catalog is a public discovery surface. It does not establish that these projects form one integrated production stack.

## Safe study path

Use a local synthetic workflow with three fake tools and one fake facility. Require the agent to:

1. choose a tool from a typed registry;
2. validate a JSON input schema;
3. run a deterministic function;
4. write lineage and runtime metadata;
5. stop on failed validation;
6. request human approval before any adaptive step.

This studies the public control-plane idea without facility credentials, external systems, or sensitive data.

## Unknowns

- Internal Flowcept deployment and ownership boundaries
- Exact WES APIs and service meshes
- Current production status of agentic workflows
- Which scientific domains have live autonomous control
- How public job responsibilities map to specific project assignments
