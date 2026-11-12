# ChatHPC (ChatHPC-app library and the ChatHPC for Kokkos SC25 artifact)

- Official page: https://ornl.github.io/ChatHPC/ (project page on GitHub Pages; links both repos and lists the project's papers) [KNOWN: fetched 2026-11-11]
- Repos (one catalog project, two repos; binding evidence below):
  - https://github.com/ORNL/ChatHPC-app, "Base ChatHPC Application and Library", default branch `main`, HEAD `5c70d58242833f9083abfeded754c254375a79c3` [KNOWN: GitHub API]
  - https://github.com/ORNL/ChatHPC-ChatHPCforKokkos-SC25, "Artifact repository for SC25 for the ChatHPC paper.", HEAD `1a4e6a2d7256a946983e446e3e6903e1dca03698` [KNOWN: GitHub API]
- Docs: https://chathpc-app.readthedocs.io/ (MkDocs; source in `docs/`) [KNOWN: README L16, mkdocs.yml]
- License: MIT for both repos, "Copyright (c) 2025 UT-BATTELLE, LLC" (UT-Battelle manages ORNL for DOE). [KNOWN: https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/LICENSE#L1-L3; https://github.com/ORNL/ChatHPC-ChatHPCforKokkos-SC25/blob/1a4e6a2d7256a946983e446e3e6903e1dca03698/LICENSE#L1-L3; the SC25 slides footer "ORNL is managed by UT-Battelle LLC for the US Department of Energy"] Model weights are not in either repo; the base model, Meta's CodeLlama-7b-hf, is gated on Hugging Face under Meta's own license terms. [KNOWN: SC25 README L66-L68; INFERRED: that Meta's terms apply to derived weights, not checked]
- Status: active (rule 14) for ChatHPC-app: last push 2026-02-06, not archived. The SC25 artifact is a frozen paper artifact (last push 2025-08-05), not archived. [KNOWN: GitHub API]
- ORNL relationship: CORROBORATED. Both repos are in the main github.com/ORNL org; LICENSE copyright is UT-Battelle; the SC25 paper (OSTI 3682544) lists "Oak Ridge National Laboratory (ORNL)" as research org with contract AC05-00OR22725 and all eight authors at ORNL; Zenodo lists ORNL as creator affiliation. No DOE CODE software record was found. [KNOWN: GitHub API; LICENSE; https://www.osti.gov/biblio/3682544 via OSTI API; Zenodo 16746629]
- One project, two repos: the project page describes ChatHPC-app as "the base CLI toolchain and Python API" and links the SC25 artifact as its paper repository; the artifact vendors ChatHPC-app v25.7.1 in `C1_ChatHPC_Lib/`. [KNOWN: https://ornl.github.io/ChatHPC/; SC25 tree]
- Namesake to keep apart: a 2024 Journal of Supercomputing paper titled "chatHPC: Empowering HPC users with large language models" (OSTI 2538074) comes from authors in ORNL's National Center for Computational Sciences and describes a different pipeline (pre-training, fine-tuning, web/API serving). The ChatHPC project page does not list it and none of its authors appear on the SC25 paper. Not merged (rule 10). [KNOWN: OSTI 2538074 abstract and author affiliations; project page publication list; tag UNKNOWN for any relation]
- Years visible in public sources: 2024 (earliest commit) to 2026
- Last checked: 2026-11-11

## Walkthrough (plain language)
- **What it is:** a small Python library and command-line tool for turning a general code-writing language model into a narrow assistant for one piece of HPC software, plus a paper artifact that does this for Kokkos. [KNOWN: project page, README]
- **The problem:** general chatbots often give wrong answers about specialized HPC libraries. The authors argue that small, expert-written datasets and a quick fine-tune on a 7-billion-parameter model can beat a much larger general model on these tasks. [KNOWN: OSTI 3682544 abstract]
- **Key terms:**
  - *Fine-tuning* means training an existing model a little more on new examples.
  - *LoRA (low-rank adaptation)* trains a small add-on (an *adapter*) instead of all the model's weights; the adapter can later be *merged* into the base model. [KNOWN: SC25 paper Section 4; INFERRED: definitions]
  - *Kokkos* is a C++ library for writing parallel code once and running it on CPUs or GPUs from different vendors (an outside project in this catalog, see the Cabana brief).
- **What goes in:** a JSON file of question, context and answer triples written by experts, a prompt template, and a config file pointing at a local copy of the base model. [KNOWN: SC25 `config_initial.json`, `prompt_template.txt`; docs/index.md L58-L66]
- **What happens:** `chathpc train` fine-tunes a LoRA adapter on the base model, saves it, merges it, and saves the merged model; `chathpc verify` replays the training questions; `chathpc test` answers a separate test set; `base test` and `openai test` run the same test set on the untuned base model and on an OpenAI model for comparison. [KNOWN: app.py L798-L923; SC25 scripts 2_train.sh to 5_evaluate_baseline.sh]
- **What comes out:** a LoRA adapter, a merged model, and JSON and Markdown reports pairing each question with the model's answer. [KNOWN: SC25 README "Output Artifacts"]
- **Where humans act:** experts write the training and test data, read the answers, and add "refinement" data where the assistant got things wrong. Scoring in the paper is the share of test prompts answered correctly, judged against expert-built answers. [KNOWN: OSTI 3682544 full text, Section 5 and Figure 1 description] The artifact's Markdown reports are for "the reviewer to look through". [KNOWN: SC25 paper appendix]
- **What it is not:** not a hosted chatbot service, not a training framework for large models, and not a ready model download. [KNOWN: no weights in either repo; INFERRED: scope]
- **What's unknown:** how many assistants beyond Kokkos have public code or data (others are linked only on an internal GitLab), and who uses the library outside ORNL.
- **Example:** test prompt "Can you translate this OpenACC code to Kokkos?" with a SAXPY loop; the refined assistant answers with a `Kokkos::parallel_for` over a `RangePolicy`. [KNOWN: https://github.com/ORNL/ChatHPC-ChatHPCforKokkos-SC25/blob/1a4e6a2d7256a946983e446e3e6903e1dca03698/C2_Kokkos_Dataset/kokkos_testing.yaml#L1-L8; example_evaluation_output/ChatHPCforKokkos_refinement_results.md]

## What it is (plain English, 2-4 sentences)
ChatHPC-app wraps Hugging Face Transformers, PEFT (LoRA) and Accelerate behind a config-driven CLI that trains, merges, chats with, and evaluates small domain assistants on Code Llama 7B. The SC25 artifact uses it to reproduce the "ChatHPC for Kokkos" results from the SC25 paper on a subset of the data. The paper reports results for several other assistants (ADIOS2, MAGMA, IRIS, TAU, ChatPORT) that are not in these public repos. [KNOWN: pyproject.toml L24-L28; SC25 README; OSTI 3682544 full text]

## How it works (plain English, no jargon without definition)
Pipeline, as written in the code at ChatHPC-app 5c70d58:

1. **Config.** A pydantic `AppConfig` reads `config.json` (data file, base model path, output paths, prompt template, token limits). [KNOWN: https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/src/chathpc/app/app.py#L57-L135]
2. **Load base model.** `AutoModelForCausalLM.from_pretrained(..., torch_dtype=torch.float16, device_map="auto")`. [KNOWN: app.py L418-L428]
3. **Load data.** The JSON file is loaded twice with `split="train"`, once as the training set and once as the evaluation set, so in-training evaluation runs on the training data. [KNOWN: https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/src/chathpc/app/app.py#L525-L526] Generalization is instead measured by the separate `test` command on a different file. [KNOWN: SC25 `4_evaluate.sh`]
4. **Prompt.** Each triple is rendered through a Jinja prompt template into a single instruction-style prompt. [KNOWN: `utils/template_utils.py`; docs/index.md L69-L85]
5. **Train.** LoRA with r=16, alpha=16, dropout 0.05 on the attention projections `q_proj`, `k_proj`, `v_proj`, `o_proj`; Hugging Face `Trainer` with 400 steps, learning rate 3e-4, fp16, effective batch 128 (32 per device, 4 accumulation steps), optional Weights & Biases logging. [KNOWN: https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/src/chathpc/app/app.py#L825-L889]
6. **Save and merge.** Saves the adapter, then `merge_and_unload()` and saves a merged full model. [KNOWN: app.py L915-L923]
7. **Serve.** Interactive chat from the CLI (`run`, `run-base`, `run-fine`, `run-merged`); optional export to GGUF and Ollama using the shipped `Modelfile`; optional OpenAI-compatible endpoint via `OPENAI_API_BASE_URL`. [KNOWN: README CLI section; Modelfile L1-L3; `openai_interface.py` L20-L24]
8. **Evaluate.** `verify` compares each response to the stored answer after stripping whitespace per line (`ignore_minor`), so it is a near-exact-match check; `test` saves responses for human review as JSON and Markdown. [KNOWN: app.py L1064; https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/src/chathpc/app/utils/verify_utils.py#L1-L5]

**What the Kokkos specialization is.** Not new code: a dataset plus config. The artifact's training files hold 18 (initial) and 27 (refinement) question-context-answer triples in four contexts (HIP to Kokkos, OpenMP to Kokkos, sequential to Kokkos translation, sequential to Kokkos parallelization), and the test file holds 45 prompts. [KNOWN: counts from `C2_Kokkos_Dataset/*.json`, `kokkos_testing.yaml`] The paper says the full initial training set had "about 70" samples and that the artifact provides "a subset" focused on Parallelization and Translation. [KNOWN: OSTI 3682544, Section 5.1 and Appendix B.1]

**What the SC25 artifact reproduces.** `run_all.sh` runs setup (uv environment, download CodeLlama-7b-hf), trains the initial and refinement assistants, verifies, tests both, then tests the base Code Llama and GPT-4o (needs `OPENAI_API_KEY`). The paper says results should be "very similar or even identical" to its Table 1 for the fine-tuned models, while GPT-4o results may drift over time. [KNOWN: https://github.com/ORNL/ChatHPC-ChatHPCforKokkos-SC25/blob/1a4e6a2d7256a946983e446e3e6903e1dca03698/README.md#L19-L73; OSTI 3682544 Appendix] Hardware tested: NVIDIA A100 and H100. [KNOWN: SC25 README L17]

## How the project is organized
From templates/engineering-checklist.md.
- **ChatHPC-app layout:** `src/chathpc/app/` (app.py 1,282 lines, CLI `__main__.py`, Ollama and OpenAI adapters, JSON-to-Markdown/YAML converters, utils), `tests/` (pytest), `scripts/` (training smoke tests, version bump), `examples/` (two Jupyter notebooks and a marimo app for Kokkos), `docs/`, `Dockerfile`, `Modelfile`. 57 files. [KNOWN: tree at 5c70d58]
- **SC25 layout:** numbered scripts `1_setup.sh` to `5_evaluate_baseline.sh` and `run_all.sh`; `C1_ChatHPC_Lib/ChatHPC-app-v25.7.1/` (vendored library); `C2_Kokkos_Dataset/`; two configs; `example_evaluation_output/` with expected results. 79 files. [KNOWN: tree at 1a4e6a2]
- **Languages and dependencies:** Python 3.10 to 3.12; `codellama` (from Meta's GitHub), `peft==0.14.0`, `transformers==4.48.0`, `accelerate==1.2.1`, `datasets`, `bitsandbytes`, `wandb`, `ollama`, `openai`, `pydantic-settings`, `jinja2`. Build backend hatchling; lock via uv. [KNOWN: https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/pyproject.toml#L1-L51]
- **Tests:** `tests/test_app.py`, `test_preferences.py`, `test_utils.py` run with `hatch run test`. [KNOWN: README]
- **CI:** GitHub Actions builds a Docker image (python:3.11-slim base), pushes to GitHub Container Registry as `ghcr.io/ornl/chathpc-app`, and smoke-imports the package; runs on `ubuntu-latest`, no GPU job. A `.gitlab-ci.yml` targets an internal GitLab with self-hosted runners; that system is out of scope (rule 16). [KNOWN: `.github/workflows/ci-github-runners.yml` L19-L56; Dockerfile L1; README L10-L14]
- **Docs:** README, ReadTheDocs site, docs/index.md "How to create a new ChatHPC/ChatX application repo". [KNOWN]
- **Releases:** ChatHPC-app tags v25.1.0 (2025-01-25) to v25.7.1 (2025-07-22), date-based versioning described in CHANGELOG; GitHub releases were all published on 2025-08-05. SC25 tags v0.0.1 (2025-04-15) to v0.0.3 (2025-08-05). Zenodo DOIs 10.5281/zenodo.16746629 (app) and 10.5281/zenodo.15226006 (artifact). [KNOWN: git tags, GitHub releases API, Zenodo] Zenodo titles the artifact release "v3.0.0" while the git tag is v0.0.3. [KNOWN: Zenodo 15226006; looks like a labeling slip, INFERRED]
- **Contribution path:** no CONTRIBUTING file; pre-commit hooks (ruff, markdownlint). The SC25 repo merged one outside typo-fix pull request. [KNOWN: `.pre-commit-config.yaml`; SC25 git log 87a1567]
- **Data and reproducibility:** Kokkos subset data and expected outputs are public; full data for other assistants is linked only on code.ornl.gov (not followed). [KNOWN: docs/index.md L7, L15]
- **Deployment statements:** the docs describe exporting to "Ollama on ExCL" and Open WebUI at ORNL's Experimental Computing Laboratory. [KNOWN: docs/index.md L116-L124] Maturity verbs from the paper: "created", "evaluated". The pyproject classifier says "Development Status :: 4 - Beta". [KNOWN]
- **Why it was built this way:** partly stated. The paper says it relies on "well-known, robust, efficient, and widely used tools" for interoperability with Ollama and Hugging Face, and chose Code Llama for cost and speed. [KNOWN: OSTI 3682544 Section 4 and abstract] Why in-training evaluation reuses the training file is [UNKNOWN].

## Timeline
| Date | Event | Source | Tag |
|---|---|---|---|
| 2024-03-13 | Earliest ChatHPC-app commit ("Ran hatch new."), before the GitHub repo existed | git log 668c386 | [KNOWN] |
| 2024-11-21 | Separate NCCS "chatHPC" journal paper published (namesake) | OSTI 2538074 | [KNOWN]; relation [UNKNOWN] |
| 2025-01-25 | ChatHPC-app v25.1.0 tag | git tags | [KNOWN] |
| 2025-04-15 | SC25 artifact repo created and v0.0.1 tagged | GitHub API; git tags | [KNOWN] |
| 2025-07-21 | ChatHPC-app GitHub repo created | GitHub API | [KNOWN] |
| 2025-07-22 | ChatHPC-app v25.7.1; artifact updated to it | git tags; SC25 git log 2a3b405 | [KNOWN] |
| 2025-08-05 | Artifact v0.0.3; GitHub releases published; Zenodo DOIs | GitHub API; Zenodo | [KNOWN] |
| 2025-11 | SC25 paper presented (St. Louis) | OSTI 3682544 conference_info | [KNOWN] |
| 2026-01 | ChatMPI paper (SCA/HPCAsia '26) uses the ChatHPC library | OSTI 3014267; project page | [KNOWN] |
| 2026-02-06 | Last ChatHPC-app commits (Docker CI, badges) | git log | [KNOWN] |

## Who uses it / why it matters
The SC25 paper has six citing works in OpenAlex, from Argonne (two PETSc agent papers), Nagoya University and the University of Tokyo, Sandia with Smith College, and ORNL. Citation shows awareness, not use. No GitHub dependents and no PyPI package. [KNOWN: OpenAlex, GitHub dependents page, PyPI 404] Within ORNL the same group reports ChatMPI built with the library, and the ChatHPC paper evaluates ChatIRIS for ORNL's IRIS runtime. [KNOWN: OSTI 3014267 abstract; OSTI 3682544 Section 5.4] It matters as a public, reproducible example of the "small model plus expert data" approach to HPC code assistants. [INFERRED]

## Related projects
| Related item | Relationship | Source | Tag |
|---|---|---|---|
| Kokkos (outside) | subject of the ChatHPC for Kokkos assistant and dataset | SC25 README, dataset | [KNOWN] |
| Cabana (`cabana`) | related topic only (also Kokkos-based); no reference either way | grep of both repos | [UNKNOWN] |
| IRIS (`iris`) | ChatIRIS assistant evaluated in the paper; IRIS cited as ref [6] | OSTI 3682544 Sections 1 and 5.4 | [KNOWN] |
| HeCBench (`hecbench`) | the HeCBench brief records a full-text OSTI match for 3682544; not re-confirmed in the paper text here | signals/hecbench.md | [UNKNOWN] pending sweep 2 |
| ChatPORT, ChatMPI, ChatADIOS2, ChatMAGMA, ChatTAU (ORNL papers) | sibling assistants built with or alongside the library | project page; OSTI 3682544, 3014267, 3009454 | [KNOWN] |
| "chatHPC" 2024 (NCCS, OSTI 2538074) | namesake; not merged | OSTI 2538074; project page | [UNKNOWN] |
| Code Llama 7B (Meta, outside) | base model | SC25 README L66-L68 | [KNOWN] |
| ExCL (ORNL Experimental Computing Laboratory) | hardware used; Ollama hosting described | OSTI 3682544 Appendix; docs/index.md L116 | [KNOWN] |

## What stands out
- The engineering is deliberately thin: about 2,500 lines of Python around standard Hugging Face tools, with almost everything assistant-specific living in data and a prompt template. [KNOWN: line counts; INFERRED: "deliberately"]
- The headline "trustworthiness" number is percent of test prompts judged correct, on test sets of tens of prompts per assistant, against expert answers. Small samples make single-point percentages noisy. [KNOWN: paper Section 5; artifact test set 45 prompts; INFERRED: the caution]
- The CUDA and OpenACC rows in the paper's Kokkos table are "self-learning": no CUDA or OpenACC data was used in fine-tuning. [KNOWN: OSTI 3682544 Table 1 caption]
- The README carries badges and links to an internal GitLab and internal docs host, showing that public GitHub is a mirror of internal development. Those systems are out of scope. [KNOWN: README L10-L20]
- Funding is not on the OSTI record beyond "USDOE"; the SC25 slides acknowledge ASCR programs (an AI-for-Science program with projects named Ellora and Durban, the Next Generation of Scientific Software Technologies program with S4PST and PESO, and SciDAC RAPIDS2). [KNOWN: OSTI 3682544 sponsor field; https://ornl.github.io/ChatHPC/assets/pdf/ChatHPC-SC25.pdf slide 15]

### Reusable ideas [INFERRED]
- Config plus prompt template plus dataset as the whole "app" makes new assistants cheap; the "ChatX" template in the docs is a reusable recipe.
- Keep a held-out test file separate from training data and run baselines (base model, a commercial model) with the same harness and output format.
- Emit both machine-readable JSON and human-readable Markdown for every evaluation, so experts can review answers quickly.
- A numbered-script artifact (`1_setup` to `5_evaluate_baseline`, plus `run_all.sh` and expected outputs) is a clean pattern for reproducible paper artifacts.
- Caution to copy deliberately: reusing the training file as the eval set during training only tracks fitting, not generalization.

## Ten questions (GOAL.md)
1. **What problem does it solve, and for whom?** Quickly building reliable, narrow AI coding assistants for HPC libraries, for HPC developers and library teams. [KNOWN: OSTI 3682544 abstract]
2. **Where does it sit in the tree?** ORNL computing research, AI for HPC software; uses ExCL hardware. Org unit not stated on OSTI. [KNOWN: OSTI 3682544; UNKNOWN: org unit]
3. **Who pays for it?** OSTI says only "USDOE"; slides acknowledge ASCR programs (see What stands out). [KNOWN]
4. **How is the code organized?** One Python package with a CLI over Transformers/PEFT; a separate scripted artifact repo with data. [KNOWN]
5. **Is it alive?** ChatHPC-app: 237 commits, 158 in 2025, 43 in early 2026, last 2026-02-06; no commits in the nine months since. [KNOWN: git log] Slowing, not dead. [INFERRED]
6. **Who outside ORNL uses or cites it?** Citations from Argonne, Sandia, Nagoya, Tokyo; no package dependents. [KNOWN: OpenAlex]
7. **What does it connect to?** Code Llama, Hugging Face stack, Ollama, OpenAI API; targets Kokkos, IRIS, ADIOS2, MAGMA, TAU, MPI. [KNOWN]
8. **What does it teach about how ORNL works?** Development on internal GitLab with public GitHub releases and Zenodo DOIs for papers; artifact-evaluation practice for SC. [KNOWN: README; INFERRED: the pattern]
9. **Could a student learn from it?** Yes: small, readable, and the artifact runs end to end with one GPU and a Hugging Face account approved for Code Llama. [KNOWN: SC25 README; INFERRED: difficulty]
10. **What is still unknown?** Public data for non-Kokkos assistants, outside users, exact funding split, relation to the 2024 NCCS chatHPC paper. Searches logged in verification/not-found.md.

## Known / Inferred / Unknown
- KNOWN: ownership, MIT license and UT-Battelle copyright, repos and tags, pipeline steps and hyperparameters, dataset sizes, artifact scripts, paper claims, citing institutions.
- INFERRED: design intent, maturity reading, Zenodo label slip, reusable ideas, meaning of the eval-on-train choice.
- UNKNOWN: org unit, funding detail on OSTI, non-Kokkos data, relation to the NCCS chatHPC paper, HeCBench link confirmation.

## Verification notes
Sweep 1 (discovery and reading pass, 2026-11-11): fresh clones of both repos; read README, pyproject, app.py, CLI, verify utils, CI, docs, artifact scripts and data; OSTI API records 3682544, 2538074, 3014267; OSTI full text of 3682544; project page and SC25 slides PDF; Zenodo 16746629 and 15226006. Code read, not run. Sweep 2 not done.

Sweep 2 (fact-check pass, 2026-11-11, by the coordinator, independent of the discovery researcher): Re-fetched: ChatHPC-app LICENSE (MIT, 2025 UT-Battelle); `app.py` L520-L526 (evaluation set is the training file), the LoRA settings (r=16, alpha=16, 400 steps, learning rate 3e-4, fp16) and `merge_and_unload` in L825-L923. Downloaded the OSTI 3682544 full text again and confirmed the ChatIRIS section, "about 70" initial samples, ExCL hardware and one node with two H100 GPUs. OSTI API: ORNL research org, sponsor field USDOE only. All match. Not re-checked: SC25 artifact data counts, slide-deck funding acknowledgments. No corrections.

## Sources (URL, title, accessed date, what it supports)
All accessed 2026-11-11.
- https://ornl.github.io/ChatHPC/ (project page: both repos, publications, collaborators)
- https://ornl.github.io/ChatHPC/assets/pdf/ChatHPC-SC25.pdf (SC25 slides: Kokkos table, acknowledgments)
- https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/README.md (CLI, Docker, GitLab mirror note)
- https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/pyproject.toml#L1-L51 (dependencies)
- https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/src/chathpc/app/app.py#L418-L428 (base model load), #L525-L526 (dataset load), #L825-L889 (LoRA and training args), #L915-L923 (save and merge), #L1064 (verify compare)
- https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/src/chathpc/app/utils/verify_utils.py#L1-L5 (ignore_minor)
- https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/.github/workflows/ci-github-runners.yml (CI)
- https://github.com/ORNL/ChatHPC-app/blob/5c70d58242833f9083abfeded754c254375a79c3/docs/index.md (ChatX recipe, ExCL Ollama)
- https://github.com/ORNL/ChatHPC-ChatHPCforKokkos-SC25/blob/1a4e6a2d7256a946983e446e3e6903e1dca03698/README.md#L1-L73 (artifact scope, hardware, reproduction steps)
- https://github.com/ORNL/ChatHPC-ChatHPCforKokkos-SC25/tree/1a4e6a2d7256a946983e446e3e6903e1dca03698/C2_Kokkos_Dataset (data)
- https://www.osti.gov/biblio/3682544 and https://www.osti.gov/servlets/purl/3682544 (SC25 paper: ORNL research org, abstract, Table 1, Appendix)
- https://www.osti.gov/biblio/2538074 (2024 NCCS chatHPC namesake)
- https://www.osti.gov/biblio/3014267 (ChatMPI)
- https://zenodo.org/records/16746629 and https://zenodo.org/records/15226006 (release DOIs)
- https://api.openalex.org/works/doi:10.1145/3712285.3759787 (6 citing works)

## Quality gate
- [x] Every load-bearing claim has a source and a tag
- [x] Facts are kept apart from interpretation
- [x] ORNL relationship is not overstated, and maturity verbs match the source (RULES item 10)
- [x] Walkthrough, flow, timeline and unknowns are present
- [x] Ten questions answered or marked UNKNOWN
- [x] No copied text beyond short cited quotes; people by role only
- [x] Two fact-check sweeps done (RULES item 11): Sweep 1 and Sweep 2 both 2026-11-11
- [x] INDEX, catalog, LAB-TREE and connections map updated (batch 13) (coordinator)
