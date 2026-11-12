"""Failure-provenance scenarios run against an installed upstream Flowcept.

Atlas-authored harness. Each scenario runs in its own child process, working
directory and HOME, so Flowcept's offline JSONL buffer and any settings it
creates stay inside a throwaway folder. Nothing here talks to a broker,
database or network service.

Usage: <python-with-flowcept> -I scenarios.py [--keep DIR]
Prints one JSON summary per scenario.
"""

import json
import os
import subprocess
import sys
import tempfile
import textwrap

PRELUDE = textwrap.dedent(
    """
    import os, sys
    from flowcept import Flowcept, flowcept_task
    from flowcept.instrumentation.flowcept_decorator import flowcept

    @flowcept_task(output_names="y")
    def measure(x):
        return x + 1

    @flowcept_task(output_names="z")
    def analyze(y):
        if os.environ.get("FAIL_ANALYZE") == "1":
            raise ValueError("synthetic analysis failure")
        if os.environ.get("KILL_IN_ANALYZE") == "1":
            os._exit(9)
        if os.environ.get("SIGTERM_IN_ANALYZE") == "1":
            import signal
            os.kill(os.getpid(), signal.SIGTERM)
        return y * 2

    _calls = {"n": 0}

    @flowcept_task(output_names="z")
    def flaky_analyze(y):
        _calls["n"] += 1
        if _calls["n"] == 1:
            raise RuntimeError("transient failure, attempt 1")
        return y * 2
    """
)

SCENARIOS = {
    "success": (
        """
        @flowcept
        def main():
            print("result", analyze(measure(3)))
        main()
        """,
        {},
    ),
    "uncaught_task_error": (
        """
        @flowcept
        def main():
            print("result", analyze(measure(3)))
        main()
        """,
        {"FAIL_ANALYZE": "1"},
    ),
    "caught_error_then_retry": (
        """
        @flowcept
        def main():
            y = measure(3)
            try:
                z = flaky_analyze(y)
            except RuntimeError:
                z = flaky_analyze(y)
            print("result", z)
        main()
        """,
        {},
    ),
    "hard_kill_mid_workflow": (
        """
        @flowcept
        def main():
            print("result", analyze(measure(3)))
        main()
        """,
        {"KILL_IN_ANALYZE": "1"},
    ),
    "sigterm_mid_workflow": (
        """
        @flowcept
        def main():
            print("result", analyze(measure(3)))
        main()
        """,
        {"SIGTERM_IN_ANALYZE": "1"},
    ),
    "hard_kill_after_200_tasks": (
        """
        @flowcept
        def main():
            for i in range(200):
                measure(i)
            analyze(1)
        main()
        """,
        {"KILL_IN_ANALYZE": "1"},
    ),
}

KEEP = ("activity_id", "status", "stderr", "used", "generated", "workflow_id", "task_id", "type")


def summarize(folder):
    records = []
    files = []
    for root, _, names in os.walk(folder):
        for name in sorted(names):
            if name.endswith(".jsonl"):
                path = os.path.join(root, name)
                files.append(os.path.relpath(path, folder))
                with open(path, encoding="utf-8") as fh:
                    for line in fh:
                        line = line.strip()
                        if line:
                            rec = json.loads(line)
                            records.append({k: rec.get(k) for k in KEEP if k in rec})
    return files, records


def run(name, keep_dir=None):
    body, env_extra = SCENARIOS[name]
    folder = tempfile.mkdtemp(prefix=f"fc-{name}-", dir=keep_dir)
    script = os.path.join(folder, "wf.py")
    with open(script, "w", encoding="utf-8") as fh:
        fh.write(PRELUDE + textwrap.dedent(body))
    env = {"PATH": os.environ.get("PATH", ""), "HOME": folder, **env_extra}
    proc = subprocess.run(
        [sys.executable, "-I", script], cwd=folder, env=env, capture_output=True, text=True, timeout=120
    )
    files, records = summarize(folder)
    return {
        "scenario": name,
        "exit_code": proc.returncode,
        "stdout_tail": proc.stdout.strip().splitlines()[-3:],
        "stderr_tail": proc.stderr.strip().splitlines()[-2:],
        "jsonl_files": files,
        "records": records,
        "folder": folder,
    }


if __name__ == "__main__":
    keep = sys.argv[2] if len(sys.argv) > 2 and sys.argv[1] == "--keep" else None
    for scenario in SCENARIOS:
        print(json.dumps(run(scenario, keep), indent=1, default=str))
