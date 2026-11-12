# PR for ORNL/flowcept: opened 2026-11-11 as https://github.com/ORNL/flowcept/pull/357

Base: `dev`. Head: `fix/workflow-status-on-exception` on a fork. Patch: `0001-Record-ERROR-workflow-status-when-the-Flowcept-conte.patch`.

**Title:** Record ERROR workflow status when the Flowcept context raises

**Body:**

When code inside `with Flowcept():` (or a `@flowcept`-decorated function) raises, the failed task is saved with `status: ERROR`, but the workflow record is saved with `status: FINISHED`. `__exit__` ignored the exception, and `stop()` always set `Status.FINISHED`. `WorkflowObject.status` is documented as "e.g., FINISHED, ERROR", so it looked like ERROR was intended but never set.

Repro on 1.0.3, default offline settings:

```python
from flowcept import Flowcept, flowcept_task

@flowcept_task(output_names="z")
def analyze(y):
    raise ValueError("analysis failed on purpose")

with Flowcept():
    analyze(1)
```

Buffer before: workflow RUNNING, task ERROR, workflow FINISHED. After: workflow RUNNING, task ERROR, workflow ERROR.

Change:
- `stop()` takes an optional `status` (default `Status.FINISHED`), so direct callers are unchanged.
- `__exit__` passes `Status.ERROR` when the block raised. `SystemExit(0)` / `SystemExit(None)` still count as FINISHED. `KeyboardInterrupt` counts as ERROR. Happy to change that if you'd rather treat it differently.
- Two `safeoffline` tests next to `test_workflow_start_end_fields`: raising block → ERROR, and clean exit plus `sys.exit(0)` → FINISHED.

Testing (macOS arm64, Python 3.12, `.[all]` + `.[ml_dev]`, `--config-profile full-offline`): the `make tests-offline` selection gives 11 passed, 1 skipped. The new error test fails on `dev` without the change. `ruff check` / `ruff format --check` report no new findings on the changed files. With the current unpinned Ruff, `ruff check src` already reports existing findings on `dev`, unrelated to this change. Online/MQ/Mongo test suites were not run.

I used an AI coding assistant (Claude Code) to investigate, write, and test this change.
