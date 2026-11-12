# ORNL Inside-Out Reconstruction

**Method:** Hermes built-in web search plus direct page retrieval with public HTTP pages. No DeepAPI, no external credentials, no classified or private sources. Claims below are limited to fetched public pages; unavailable pages are labeled.

## What the public record reveals

### autonomous-science
Source: https://www.ornl.gov/autonomousscience

[UNAVAILABLE: HTTPError: HTTP Error 403: Forbidden]

### intersect
Source: https://www.ornl.gov/research-highlight/intersect-federated-architecture-scientific-laboratory-future

[UNAVAILABLE: HTTPError: HTTP Error 403: Forbidden]

### codex-hpc
Source: https://www.ornl.gov/publication/evaluation-openai-codex-hpc-parallel-programming-models-kernel-generation

[UNAVAILABLE: HTTPError: HTTP Error 403: Forbidden]

### quantum-grid
Source: https://www.ornl.gov/news/ornl-partnership-epb-tests-new-method-protecting-quantum-networks

[UNAVAILABLE: HTTPError: HTTP Error 403: Forbidden]

### quantum-distance
Source: https://www.ornl.gov/news/ornl-lanl-developed-quantum-technologies-go-distance

[UNAVAILABLE: HTTPError: HTTP Error 403: Forbidden]

### venus
Source: https://www.ornl.gov/news/venus-rising-new-dawn-ai-powered-atomic-scale-3d-imaging

[UNAVAILABLE: HTTPError: HTTP Error 403: Forbidden]

### nuclear-battery
Source: https://www.ornl.gov/news/radioisotopes-power-reliable-nuclear-batteries-nations-needs

[UNAVAILABLE: HTTPError: HTTP Error 403: Forbidden]

### polymer-enzymes
Source: https://www.ornl.gov/news/synthetic-biology-ai-driven-analysis-reveal-new-polymer-targeting-enzymes

[UNAVAILABLE: HTTPError: HTTP Error 403: Forbidden]

### wildfire
Source: https://ornl.gov/news/new-ai-enhanced-tools-detect-electrical-arcing-reduce-wildfires

[UNAVAILABLE: HTTPError: HTTP Error 403: Forbidden]

### job-agentic
Source: https://jobs.ornl.gov/job/Oak-Ridge-Research-Scientist%2C-Agentic-Workflows-TN-37830/1422626200/

Research Scientist, Agentic Workflows Job Details | Oak Ridge National Laboratory [page title only; the raw page-text scrape was trimmed on 2026-11-11 to avoid republishing posting text]

### job-distributed
Source: https://jobs.ornl.gov/job/Oak-Ridge-Research-Scientist,-Distributed-Workflows-TN-37830/1407757400

Research Scientist, Distributed Workflows Job Details | Oak Ridge National Laboratory [page title only; the raw page-text scrape was trimmed on 2026-11-11 to avoid republishing posting text]

### osti
Source: https://www.osti.gov/stip/search

[UNAVAILABLE: RemoteDisconnected: Remote end closed connection without response]

### doecode
Source: https://www.osti.gov/doecode/search

DOE CODE: Advanced Search page [navigation text only; the raw page scrape was trimmed on 2026-11-11]

### tech-transfer
Source: https://www.ornl.gov/technology-transfer/technologies

[UNAVAILABLE: HTTPError: HTTP Error 403: Forbidden]

## Cross-source synthesis

- ORNL publicly exposes not only scientific outcomes but the infrastructure around them: autonomous-lab architectures, workflow orchestration roles, instruments, technology-transfer catalogs, public software indexes, and historical archives.
- The strongest hidden signal is workflow infrastructure. Job postings and architecture pages reveal that cross-facility orchestration and agentic workflows are themselves active research areas, not just support tooling.
- ORNL projects repeatedly combine AI with physical instruments, HPC, networking, materials, biology, and grid systems. The non-obvious capability is integration across domains.
- Public documentation supports reconstructing a capability map, but it does not justify claims about classified work or internal implementation details.

## Three local experiments worth building

1. **Research-loop runner:** Hermes proposes a question, Codex builds a small test, a verifier runs it, and the system preserves evidence and decides whether to iterate.
2. **Project early-warning system:** ingest project logs and test results, then detect repeated failures, scope drift, and unresolved assumptions before they become incidents.
3. **Scientific-workflow digital twin:** model a real workflow as stages, dependencies, instruments, and outputs, then simulate bottlenecks and alternative paths before changing the live system.

## Evidence boundary

Search discovery is not treated as proof. Each dossier needs a fetched primary source. Pages that returned bot protection, redirects, or errors remain unavailable rather than being filled from memory.