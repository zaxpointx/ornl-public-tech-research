#!/usr/bin/env python3
"""Check structural consistency of the public research atlas."""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

with (ROOT / "discovery" / "catalog.csv").open(newline="") as fh:
    catalog = list(csv.DictReader(fh))

if not catalog:
    errors.append("catalog is empty")

project_ids = {p.stem for p in (ROOT / "projects").glob("*.md")}
signal_ids = {p.stem for p in (ROOT / "signals").glob("*.md")}
catalog_ids = {row.get("id", "").strip() for row in catalog}
missing_briefs = sorted(catalog_ids - project_ids)
if missing_briefs:
    print("catalog entries without briefs:", ", ".join(missing_briefs))

index = (ROOT / "INDEX.md").read_text()
readme = (ROOT / "README.md").read_text()
for name, text in (("INDEX.md", index), ("README.md", readme)):
    if "Independent" not in text and "independent" not in text:
        errors.append(f"{name} is missing an independence statement")

if not (ROOT / "AGENTS.md").exists():
    errors.append("AGENTS.md is missing")
if not (ROOT / "docs" / "research-team.md").exists():
    errors.append("docs/research-team.md is missing")

print(f"catalog rows: {len(catalog)}")
print(f"project briefs: {len(project_ids)}")
print(f"signal files: {len(signal_ids)}")
print(f"catalog entries without briefs: {len(missing_briefs)}")
print(f"catalog statuses: {dict(sorted((s, sum(r.get('status') == s for r in catalog)) for s in {r.get('status') for r in catalog}))}")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)
print("structure checks: PASS")
