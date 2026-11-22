Short brief, no public code. Independent research, not affiliated with Y-12, CNS or NNSA. People by role only. Last checked: 2026-11-22.

# Digital twins and LLMs for predictive maintenance (Y-12 with UT Knoxville)

- Journal article 1: *Cross-domain digital twin architecture for predictive maintenance via machine learning and Large Language Models*, Computers and Industrial Engineering, 2026-05, DOI 10.1016/j.cie.2026.111914 [1]
- Journal article 2: *Generative large language models for predictive maintenance planning*, Computers and Industrial Engineering, 2026-08, DOI 10.1016/j.cie.2026.112095 [2]
- Sponsor: NNSA, Y-12 contract. Authors from UT Knoxville and Y-12. [KNOWN: 1, 2]
- Site story on digital twins: 2024-10-01 [3]
- Status: active research (2026 papers). [KNOWN]

## Walkthrough (plain language)
- **What it is:** A platform that builds a live 3D copy (digital twin) of plant equipment, streams sensor data into it, predicts failures with machine learning, and uses LLMs to help plan the maintenance. [KNOWN: 1, 2]
- **Stack named in the abstract:** Unreal Engine 5, Unity 3D, MQTT for telemetry, Random Forest models, LLMs, and a web portal for monitoring. [KNOWN: 1]
- **The LLM part:** Trains single and collaborating LLMs on past maintenance planning packages (from raw data to handwritten text) to draft new planning packages. [KNOWN: 2]
- **Training use:** The site story describes twins used to rehearse glovebox work and abnormal events, to plan a prototype shop layout in VR, and to let UPF workers walk spaces not yet built. It names a five-level maturity model, from "virtual twin" up to "autonomous twin". PDRD funds the work. [KNOWN: 3]
- **Unknown:** Which equipment, data volumes and results. Not pursued.

## What stands out (interpretation)
This is the most modern, most publishable software work tied to Y-12, and the architecture (MQTT + ML + LLM + game engine) is reproducible at home with public datasets. It also creates exactly the OT attack surface the [IIoT risk report](iiot-risk-report.md) warns about. [INFERRED]

## Sources (accessed 2026-11-22)
1. https://www.osti.gov/biblio/3376984 (OSTI API record); supports: stack, purpose
2. https://www.osti.gov/biblio/3377415 (OSTI API record); supports: LLM planning method
3. https://www.y12.doe.gov/news/blog/improving-y-12%E2%80%99s-production-future-one-twin-time (Y-12 news); supports: training uses, maturity model, PDRD

A conference slide deck on related Y-12 maintenance tools was found on a university site but carried a CUI marking, so it was not used. See [verification](../verification.md#skipped-on-purpose).

## Verification
Sweep 1 done on 2026-11-22: each load-bearing source above was fetched that day unless marked as seen in a search result. Sweep 2 (an independent re-read) has not been done, so this brief is not promoted to `discovery/catalog.csv`. See the [Y-12 atlas verification notes](../verification.md).
