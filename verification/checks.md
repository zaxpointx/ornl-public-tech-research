# Check ledger for deep dives and connections files

One row per file. **checks** is how many full fact-check passes the file has had (0, 1 or 2). The Fact Checker fills this in; the Librarian commits it. `python3 tools/audit.py --publish` fails on any file under deep-dives/, connections/ or discovery/ (notes files) that is missing here or has fewer than 2.

| File | Checks | Last check | Notes |
|---|---|---|---|
| deep-dives/additive-manufacturing-connections.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/additive-manufacturing-timing.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/additive-manufacturing.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/cyberwheel/claim-boundary.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/cyberwheel/lineage.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/cyberwheel/missing-artifacts.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/cyberwheel/people-roles.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/cyberwheel/source-ledger.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/cyberwheel/synthesis.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/cyberwheel/system-flow.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/cyberwheel/timeline.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/cyberwheel/verification-report.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/grid-tools-connections.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/grid-tools-timing.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/grid-tools.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/nuclear-reactor-software-connections.md | 2 | 2026-10-29 | two checks per the fact-check pass; OLM link swapped to PyPI and the ORNL mirror after the checks |
| deep-dives/nuclear-reactor-software.md | 2 | 2026-10-29 | filled in 2026-10-29; two checks, three small fixes |
| deep-dives/olcf-test-harness-connections.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/olcf-test-harness-timing.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/olcf-test-harness.md | 2 | 2026-10-29 | two checks per the fact-check pass; notes the Oct 15 repo reorganization |
| deep-dives/sns-neutron-pipeline-connections.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| deep-dives/sns-neutron-pipeline-timing.md | 3 | 2026-10-29 | SNS power figures now marked unverified |
| deep-dives/sns-neutron-pipeline.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| connections/lab-tree-crosslinks.md | 2 | 2026-10-29 | clean |
| connections/map.md | 2 | 2026-11-02 | second pass done on all 225 links (nine small fixes 2026-10-29; links 31 verified and 40 corrected 2026-11-02) |
| discovery/cyber-ai-mac-picks-2026-10-28.md | 2 | 2026-10-29 | two checks per the fact-check pass |
| discovery/nuclear-reactor-scan-2026-10-28.md | 2 | 2026-10-29 | two checks per the fact-check pass; afterwards one personal handle removed and the OLM link swapped to PyPI and the ORNL mirror |
| discovery/stub-search-2026-10-24.md | 2 | 2026-10-29 | three small fixes (Heartbeat dates, one license line, three search-only claims now INFERRED) |
