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

required_columns = {
    "id", "name", "url", "repo_url", "org_unit", "domain", "status",
    "discovered_batch", "notes",
}
actual_columns = set(catalog[0]) if catalog else set()
missing_columns = sorted(required_columns - actual_columns)
if missing_columns:
    errors.append(f"catalog is missing columns: {', '.join(missing_columns)}")

allowed_statuses = {"active", "draft-osti-only", "stub-osti-only", "unknown"}
invalid_statuses = sorted({row.get("status", "").strip() for row in catalog} - allowed_statuses)
if invalid_statuses:
    errors.append(f"catalog has invalid statuses: {', '.join(invalid_statuses)}")

duplicate_ids = sorted(
    value for value in {row.get("id", "").strip() for row in catalog}
    if value and sum(row.get("id", "").strip() == value for row in catalog) > 1
)
if duplicate_ids:
    errors.append(f"catalog has duplicate ids: {', '.join(duplicate_ids)}")

project_ids = {p.stem for p in (ROOT / "projects").glob("*.md")}
signal_ids = {p.stem for p in (ROOT / "signals").glob("*.md")}
catalog_ids = {row.get("id", "").strip() for row in catalog}
missing_briefs = sorted(catalog_ids - project_ids)
orphan_briefs = sorted(project_ids - catalog_ids)
if missing_briefs:
    print("catalog entries without briefs:", ", ".join(missing_briefs))
if orphan_briefs:
    errors.append(f"project briefs not present in catalog: {', '.join(orphan_briefs)}")

for required_file in (
    ROOT / "docs" / "book-plan.md",
    ROOT / "docs" / "publication-workflow.md",
    ROOT / "docs" / "research-manifest.md",
    ROOT / "docs" / "coverage-matrix.md",
    ROOT / "templates" / "chapter-checklist.md",
):
    if not required_file.exists():
        errors.append(f"required editorial file is missing: {required_file.relative_to(ROOT)}")

index = (ROOT / "INDEX.md").read_text()
readme = (ROOT / "README.md").read_text()
for name, text in (("INDEX.md", index), ("README.md", readme)):
    if "Independent" not in text and "independent" not in text:
        errors.append(f"{name} is missing an independence statement")

if not (ROOT / "docs" / "research-team.md").exists():
    errors.append("docs/research-team.md is missing")

if "docs/book-plan.md" not in readme:
    errors.append("README.md does not link to the canonical book plan")
if "docs/publication-workflow.md" not in readme:
    errors.append("README.md does not link to the publication workflow")
if "docs/coverage-matrix.md" not in readme:
    errors.append("README.md does not link to the coverage matrix")

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
