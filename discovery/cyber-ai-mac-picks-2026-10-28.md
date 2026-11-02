# Cyber and AI repos worth running on a 32 GB M4 Mac (discovery pass) (accessed 2026-10-28)

Method: listed all 179 public repos in github.com/ORNL via the GitHub API and filtered names and descriptions for cyber and AI terms; one wider GitHub search for READMEs naming ORNL plus cyber; READMEs fetched for install notes. Stars and push dates from the API on 2026-10-28. Difficulty is [INFERRED] from README install notes, nothing was installed.

Main finding: Cyberwheel is the only public cybersecurity code in the ORNL GitHub org. ORNL's other cyber tools in our catalog (Situ, Hyperion, Heartbeat, Akatosh, CAN-D, CPAD, Cincinnatus) have no public code; they are known only from OSTI records and, for some, ORNL pages, news or paper pages (wording updated 2026-10-29, discovery pass). The wider search turned up only third-party repos that use ORNL-linked power grid data, not ORNL code.

| Repo | What it does | Activity | License | Mac difficulty |
|---|---|---|---|---|
| ORNL/cyberwheel | RL sim, red vs blue agents on simulated networks | last push 2025-08-26, 56 stars | MIT | [INFERRED] medium, already being installed |
| ORNL/tx2 | Notebook dashboard for seeing why a transformer text classifier makes its calls | last push 2024-10-24, 20 stars, ~115 commits | BSD-3-Clause | [INFERRED] easy, `pip install tx2`, PyTorch CPU or MPS |
| ORNL/icat | Interactive ML dashboard for labeling and exploring text data (Panel in Jupyter) | last push 2025-06-10, 7 stars, ~188 commits | BSD-3-Clause | [INFERRED] easy, `pip install icat-iml` |
| ORNL/flowcept | Records what AI and science workflows did (provenance) | last push 2026-08-12, 40 stars | MIT | [INFERRED] easy, `pip install flowcept`, README says the minimal example needs no database |
| ORNL/HydraGNN | Graph neural nets for materials and molecule properties | last push 2026-10-27, 128 stars | BSD-3-Clause | [INFERRED] medium, Python 3.11 to 3.14 and pinned PyTorch; small examples only on a Mac |
| ORNL/MATEY | Spatiotemporal foundation models for physics | last push 2026-09-17, 11 stars | MIT | [INFERRED] hard, built around Frontier and Slurm scripts |
| ORNL/superneuroabm | GPU neuromorphic multi-agent sim | last push 2026-10-26, 8 stars | BSD-3-Clause | not for this Mac: README requires NVIDIA CUDA or AMD ROCm |

Skipped: ORNL/ESP32-Traffic-Classifier (repo is empty per API), TASQC (stale 2019, hardware focus), AADL and DistGANs (no license in API).

## Fact-check notes (2026-10-29)
- Re-checked via GitHub API and READMEs on 2026-10-29: licenses, star counts and push dates for all seven repos match; ORNL org shows 179 public repos; ESP32-Traffic-Classifier is empty (size 0, no license); install lines for tx2, icat and HydraGNN Python range match READMEs; superneuroabm README requires NVIDIA CUDA or AMD ROCm; flowcept README describes file-based runs with no database. superneuroabm has pushed again since (2026-10-28 14:18 ET). Commit counts (~115, ~188) not re-counted this pass.

### Second pass (2026-10-29)
- Re-checked tx2 (20 stars, pushed 2024-10-24, BSD-3), icat (7, 2025-06-10, BSD-3), HydraGNN (128, 2026-10-27, BSD-3) and cyberwheel (56 stars, MIT, last commit 2025-08-26). Verified.
- The 179-repo count and "only public cybersecurity code in the ORNL org" could not be recounted: the GitHub API rate limit was hit. They stand on the first check. Unverifiable.
- No corrections.
