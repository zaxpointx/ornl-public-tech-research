# AI security and cyber resilience

## Plain-language summary

ORNL is researching how to make AI and critical systems harder to fool. The public work covers both AI itself and the systems that use AI, including the electric grid.

## What the public record shows

ORNL's Center for Artificial Intelligence Security Research says it studies weaknesses across the full AI pipeline: hardware, software, data supplies, connections to physical systems, and human processes. It also describes testing AI at the scale of Frontier and names public tools called Photon and Lantern. [S27]

A separate ORNL project called AI-PhyX applies machine learning to electric-grid cybersecurity. The public description says the tool suite is meant to support vulnerability analysis, attack detection, threat mitigation, and recovery. It uses a shared data pool so separate security applications do not remain isolated. [S28]

ORNL also publicly described Situ and Heartbeat, two technologies licensed to U2opia. Situ looks for suspicious behavior in streaming security data. Heartbeat measures physical power behavior from hardware to find signs of malware. [S29]

## Why it connects to the atlas

The connection is broader than “AI safety.” ORNL is treating trust as a systems problem:

- the model can be attacked;
- the data can be poisoned;
- the hardware can reveal or hide behavior;
- the network can change the result;
- the human operator still needs an understandable warning.

This links AI, supercomputing, power systems, hardware measurement, software, and technology transfer.

## People and teams named publicly

- Jamie Lian leads ORNL's Grid-Interactive Controls group contribution to AI-PhyX.
- Teja Kuruganti is identified as a project co-leader.
- Yan Liu is identified as developing software for AI-PhyX.
- John Goodall led the Situ development team.
- Stacy Prowell led the Heartbeat development team. [S28][S29]

## Unknowns

- The public descriptions do not disclose sensitive test data, internal network layouts, or defensive configurations.
- The CAISER page describes capabilities and tools but does not establish that every named tool is publicly installable.
- Licensing does not mean the underlying research, datasets, or full source code are public.

## Safe study path

Build a local classifier and then test it with synthetic data poisoning, distribution shifts, and sensor failure. Keep the system disconnected from real infrastructure. Record whether the detector can explain its warning and whether a human can reject a bad alert.
