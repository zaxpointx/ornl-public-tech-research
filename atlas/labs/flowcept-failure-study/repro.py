"""Hands-on Flowcept failure reproduction. Run one mode at a time, then `check`.

    python repro.py ok           # normal run
    python repro.py error        # a task raises an exception
    python repro.py sigterm      # process gets SIGTERM mid-workflow
    python repro.py kill         # process dies instantly (like an OOM kill)
    python repro.py manual-dump  # same SIGTERM, but we call dump_buffer() first
    python repro.py check        # what made it to disk?

Every mode runs 200 quick `measure` tasks, then one `analyze` task.
"""

import glob
import json
import os
import signal
import sys

MODE = sys.argv[1] if len(sys.argv) > 1 else "ok"

if MODE == "check":
    files = glob.glob("flowcept_buffer*.jsonl")
    if not files:
        print("No buffer file on disk. Nothing was saved.")
    for path in files:
        with open(path) as fh:
            records = [json.loads(line) for line in fh if line.strip()]
        statuses = {}
        for r in records:
            statuses[r.get("status")] = statuses.get(r.get("status"), 0) + 1
        print(f"{path}: {len(records)} records {statuses}")
        for r in records:
            if r.get("status") == "ERROR":
                print("  error record:", r.get("activity_id"), "->", r.get("stderr"))
    sys.exit(0)

for old in glob.glob("flowcept_buffer*.jsonl"):
    os.remove(old)  # start each run clean so `check` only shows this run

from flowcept import Flowcept, flowcept_task  # noqa: E402


@flowcept_task(output_names="y")
def measure(x):
    return x + 1


@flowcept_task(output_names="z")
def analyze(y):
    if MODE == "error":
        raise ValueError("analysis failed on purpose")
    if MODE in ("sigterm", "manual-dump"):
        os.kill(os.getpid(), signal.SIGTERM)
    if MODE == "kill":
        os._exit(9)
    return y * 2


with Flowcept() as fc:
    for i in range(200):
        measure(i)
    if MODE == "manual-dump":
        fc.dump_buffer()
    analyze(1)

print("workflow finished normally")
