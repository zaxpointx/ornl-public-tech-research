# Draft issues for ORNL/flowcept (NOT POSTED)

Fill in the results from your own run before posting. If anything differs from what's written here, trust your run and edit the draft.

---

## Issue A (bug): workflow status is FINISHED when the `with Flowcept()` block raises

**Environment:** flowcept 1.0.3 (PyPI), Python 3.11.x, macOS arm64, default settings (offline, no MQ/DB).

```python
from flowcept import Flowcept, flowcept_task

@flowcept_task(output_names="z")
def analyze(y):
    raise ValueError("analysis failed on purpose")

with Flowcept():
    analyze(1)
```

**Result:** the task record has `status: ERROR` as expected, but the workflow record written at the end has `status: FINISHED`, even though the block exited with an exception.

**Why:** `Flowcept.__exit__` calls `stop()` without checking `exc_type`, and `stop()` always sets `Status.FINISHED` on the workflow object. I didn't find workflow status semantics in the docs, so I may be misreading the intent.

**Suggestion:** in `__exit__`, set the workflow status to `ERROR` when `exc_type` is not None. Happy to open a small PR with a test if you'd like that.

---

## Issue B (docs / feature request): offline mode loses everything on SIGTERM or kill

I know the docs say offline mode keeps messages in memory until dumped and isn't meant for large runs, so this isn't a bug report. It's about the failure case.

**Environment:** same as above.

**What I ran:** 200 quick decorated tasks, then a task that sends SIGTERM to its own process (stand-in for a scheduler walltime limit). Variants: `os._exit(9)` (stand-in for an OOM kill), and calling `f.dump_buffer()` before the SIGTERM.

| Case | Records on disk |
|---|---|
| normal finish | 203 (201 tasks + 2 workflow records) |
| task raises | 203, failed task `ERROR` |
| SIGTERM | none, no file created |
| `os._exit(9)` | none |
| `dump_buffer()` then SIGTERM | 201 (200 tasks + workflow start) |

So the manual workaround works. But a user following the quickstart won't know that an abnormal exit throws away tasks that finished long before.

**Ask:** would you take either (1) a sentence in `prov_storage.rst` saying that abnormal termination loses anything not yet dumped, with the `dump_buffer()` pattern as the mitigation, or (2) an opt-in offline setting that appends records to the JSONL as they're captured? I'd be glad to do (1), and to try (2) if it fits the project's direction. I saw #319 moved MQ flushing to end-of-run, so I understand if (2) doesn't.

Not tested: online/MQ mode, adapters, Linux/HPC.
