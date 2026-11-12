# Neutron workflows, instruments, and facility data

**Evidence state:** DIRECT for the public neutron facility and workflow descriptions.
**Primary sources:** [Autonomous neutron workflow](https://impact.ornl.gov/en/publications/toward-anautonomous-workflow-forsingle-crystal-neutron-diffractio/), [Neutron Sciences](https://ornl.gov/neutrons), [NScD overview](https://neutrons.ornl.gov/about), [ORNL user facilities](https://www.ornl.gov/user-facilities/). Fetched 2026-10-31. See `../source-ledger.md` entries S11, S15, and S16.

## Facility context

ORNL's neutron program centers on HFIR and SNS. The public pages describe neutron scattering across quantum materials, chemistry and catalysis, materials and engineering, soft matter and polymers, biological materials and systems, and AI/ML. [S15]

ORNL says researchers use a suite of instruments to study materials and energy, and that user-facility proposals are selected through peer review. The NScD overview says selected researchers use the facilities and instruments free of charge in return for making data and findings public. [S15]

The public user-facilities page places HFIR, SNS, and OLCF in the larger user-facility map and describes use by universities, laboratories, and private industry. [S16]

## Autonomous workflow

The public paper describes a workflow for single-crystal neutron diffraction with three components:

1. Real-time AI segmentation on image streams.
2. Continuous integration that launches distributed training jobs on Summit using newly collected images.
3. A web frontend showing AI-tagged images to experts. [S11]

The paper says feedback could be sent to edge equipment to help decide the next experiment and calls the work a first step toward autonomous real-time experiment steering. The data used resources at HFIR. [S11]

## Why this matters

The instrument is not treated as a passive data source. The loop is:

```text
neutron measurement
  -> image stream
  -> segmentation
  -> model update
  -> expert-facing view
  -> possible next-step decision
```

The source supports this workflow pattern. It does not support the stronger claim that all neutron experiments are autonomous or that human experts have been removed from the loop.

## Public data objects

The paper and facility pages support these public data categories:

- image streams;
- AI-tagged images;
- model-training data;
- instrument and experiment metadata;
- workflow/service outputs;
- public findings and data associated with user-facility research.

Exact data schemas, access credentials, retention policies, and non-public datasets are UNKNOWN.

## Safe study path

Use synthetic or openly licensed image fixtures. Build segmentation, confidence scoring, expert review, and next-step recommendation. Keep the output advisory and local. Do not connect to beamlines, instruments, facility networks, or non-public data.

## Job families

A neutron workflow requires more than an ML model. The public facility pages identify physicists, engineers, technicians, operators, facilities experts, communicators, human-resource partners, and business professionals as part of the neutron-science team. [S15]

## Unknowns

- Current production status of the autonomous workflow
- Exact inference and CI implementation
- Instrument-control interface details
- Complete public data-release path for individual experiments
- Whether the workflow has expanded beyond the described single-crystal case
