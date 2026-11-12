# Flowcept failure-provenance study

_Run commands from the `atlas/` folder of this repository (merged 2026-11-11)._

Date: 2026-11-11. First Atlas experiment that executes upstream ORNL software instead of a local stand-in.

Question: when a workflow fails, what does ORNL's Flowcept actually record in its documented offline mode? And can Zambeze's historical Flowcept hook still run?

`scenarios.py` is Atlas-authored. It wraps the README quickstart pattern (`@flowcept` around `main`, `@flowcept_task` on functions) and runs each scenario in its own child process, working directory and `HOME`. Upstream code was installed from PyPI into throwaway virtual environments outside the repo. No broker, database, facility or credential was used.

## Setup

- Flowcept 1.0.3 from PyPI, Python 3.11.15, macOS arm64. PyPI 1.0.3 matches the tag and the pinned revision `c000b10ea49659af6c5821b61918f3893bd46a92` ([repo](https://github.com/ORNL/flowcept)), which was also the `main` tip on the run date.
- Zambeze snapshot `13875a1e9186c9398df56faef0be3c84cd8bd1a9` ([repo](https://github.com/ORNL/Zambeze)), inspected but not run as an agent.
- Reproduce: `<venv-with-flowcept>/bin/python -I labs/flowcept-failure-study/scenarios.py`. Raw output is in `results-flowcept-1.0.3.json`.

## Result 1: raised errors are captured well

| Scenario | Exit | Records on disk |
|---|---|---|
| success | 0 | 2 FINISHED, `used`/`generated` correct |
| uncaught exception in second task | 1 | first FINISHED; failing task `status: ERROR`, `stderr: "synthetic analysis failure"`, `used` kept, no `generated` |
| caught exception, retried once | 0 | ERROR attempt plus FINISHED attempt, same `activity_id` |

DIRECT (observed): the buffer still reaches disk when `main` raises, because the `@flowcept` decorator closes Flowcept as a context manager.

Observed gaps, which are small: `stderr` stores only `str(e)`, so the exception type (`ValueError`) is lost. Retry attempts are two unrelated task records. Nothing marks the second as a retry of the first except a shared `activity_id` and identical `used`.

## Result 2: abnormal termination loses everything

| Scenario | Exit | Records on disk |
|---|---|---|
| `os._exit` inside the second task | 9 | **0** (no file) |
| SIGTERM to self inside the second task | -15 | **0** |
| `os._exit` after 200 finished tasks | 9 | **0** |

DIRECT (code): in offline mode the buffer is a plain list (`self.buffer = list()`), written only by `buffer_to_disk` inside `_close_buffer` during a normal stop ([mq_dao_base.py L158–195 at the pinned revision](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/src/flowcept/commons/daos/mq_dao/mq_dao_base.py#L158-L195)). `buffer_size` and `insertion_buffer_time_secs` apply only to the online `AutoflushBuffer`. No SIGTERM or atexit handler was found in `src/flowcept` outside the CLI.

INFERRED: batch schedulers usually send SIGTERM at walltime, and the OOM killer sends SIGKILL. So in offline mode, the runs that most need provenance (jobs that died) leave none, including tasks that finished well before the crash. Online mode with a broker was not tested and may behave differently.

Correction after the docs check (2026-11-11): this is a **documented design limit, not a bug**. [prov_storage.rst](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/docs/prov_storage.rst) says offline mode "keeps all messages in memory until they are dumped" and is "not intended for very large-scale runs". The "during or at the end of a run" wording refers to calling `dump_buffer()` manually. `repro.py manual-dump` confirms the workaround: calling `fc.dump_buffer()` before the SIGTERM saved all 200 finished tasks. What the docs don't say is that an abnormal exit loses everything since the last manual dump, and there's no automatic periodic dump in offline mode. [PR #319](https://github.com/ORNL/flowcept/pull/319) (May 2026, "enabling flushing only in the end while using MQ") suggests end-of-run flushing is a deliberate direction.

## Result 4: workflow marked FINISHED even when it raised

With `with Flowcept():`, the `error` run writes the workflow record with `status: FINISHED` even though the block exited with an exception. DIRECT (code): `__exit__` calls `stop()` without looking at `exc_type`, and `stop()` always sets `Status.FINISHED` ([flowcept_controller.py at the pinned revision](https://github.com/ORNL/flowcept/blob/c000b10ea49659af6c5821b61918f3893bd46a92/src/flowcept/flowcept_api/flowcept_controller.py)). `Status.ERROR` exists and is used for tasks. The workflow schema docs don't define workflow status, so this is an undocumented behavior rather than a broken promise, but it is the more clear-cut bug of the two.

## Result 3: Zambeze's hook works only with Flowcept ≤ v0.3.11

Zambeze's message handler runs `from flowcept import ZambezeInterceptor, FlowceptConsumerAPI` when Flowcept is enabled in its settings ([line 74](https://github.com/ORNL/Zambeze/blob/13875a1e9186c9398df56faef0be3c84cd8bd1a9/src/zambeze/orchestration/agent/message_handler.py#L74)).

| Flowcept | Import line | Notes |
|---|---|---|
| 1.0.3 | `ImportError: cannot import name 'ZambezeInterceptor'` | observed |
| 0.5.1 | not reached | `import flowcept` itself blocks 30 s, then fails trying MongoDB at localhost:27017 |
| 0.3.11 | both import; `ZambezeInterceptor()` constructs | only after adding `msgpack` (imported but not declared in requirements) and `numpy<2` (pinned pandas 2.0.3 is ABI-incompatible with NumPy 2) |

From Flowcept history (git tags inspected locally): `FlowceptConsumerAPI` left the exports in [a104a584](https://github.com/ORNL/flowcept/commit/a104a584a3d98646d1688e6230eddb8bcb2b09a1) (2024-09-23; first absent in v0.5.1). `ZambezeInterceptor` left the exports in [4fe1173c](https://github.com/ORNL/flowcept/commit/4fe1173c28d9f115b22d5a672947dd376ceab97c) (2025-03-14; first absent in v0.8.1). The adapter was deleted in [cb14547b](https://github.com/ORNL/flowcept/commit/cb14547b84f1a622967a4132351dceea25a276ad) (2025-06-10, "removing zambeze old code"; first absent in v0.8.11).

So Zambeze's final snapshot (2024-09-13) went out of sync with Flowcept ten days later. Flowcept has since removed the integration on purpose. This looks like a deliberate retirement, not a regression, so it is not worth an upstream bug report. INFERRED: with Flowcept enabled, a Zambeze agent on any Flowcept ≥ 0.5.1 would fail at startup with this ImportError. Not run, because the agent needs RabbitMQ and ZeroMQ peers.

## Limits

One machine, one Python, offline mode only. Online/broker modes, Dask/MLflow adapters, threads/async tasks and Flowcept's own test suite were not run. The scenarios are synthetic two-task workflows, not scientific workloads.

## Next

`repro.py` is the hand-run version: one mode per run, then `python repro.py check`. Drafts are in `upstream-issue-draft.md` and **not posted**; posting needs Cayden's OK. Result 4 is the stronger bug report and has a small, obvious fix. That fix and its tests are in `upstream-pr/` as a patch against `dev`, plus a PR description. It passes the offline suite locally and was opened upstream as https://github.com/ORNL/flowcept/pull/357 on 2026-11-11. Result 2 should go as a docs or feature request, not a bug. Recent outside issues (#352, #355, #356) had no replies when checked, so a response isn't guaranteed.
