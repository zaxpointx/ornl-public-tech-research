#!/usr/bin/env python3
"""Validate the ORNL Atlas registry graph without network access."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry"
FILES = {
    "sources": REGISTRY / "sources.json",
    "projects": REGISTRY / "projects.json",
    "facilities": REGISTRY / "facilities.json",
    "software": REGISTRY / "software.json",
    "roles": REGISTRY / "roles.json",
    "edges": REGISTRY / "edges.json",
}


def load(name: str, path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{name}: cannot read valid JSON: {exc}") from exc
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError(f"{name}: expected an object with schema_version=1")
    return data


def collect_ids(data: dict, key: str, name: str) -> set[str]:
    rows = data.get(key)
    if not isinstance(rows, list):
        raise ValueError(f"{name}: missing list {key!r}")
    ids: set[str] = set()
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            raise ValueError(f"{name}: every {key[:-1]} needs a string id")
        item_id = row["id"]
        if item_id in ids:
            raise ValueError(f"{name}: duplicate id {item_id!r}")
        ids.add(item_id)
    return ids


def check_url(url: object, source_id: str) -> None:
    if not isinstance(url, str) or not url:
        raise ValueError(f"sources: {source_id}: missing URL")
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"sources: {source_id}: invalid external URL {url!r}")


def main() -> int:
    try:
        loaded = {name: load(name, path) for name, path in FILES.items()}
        ids = {
            "source": collect_ids(loaded["sources"], "sources", "sources"),
            "project": collect_ids(loaded["projects"], "projects", "projects"),
            "facility": collect_ids(loaded["facilities"], "facilities", "facilities"),
            "software": collect_ids(loaded["software"], "software", "software"),
            "role": collect_ids(loaded["roles"], "roles", "roles"),
        }

        for source in loaded["sources"]["sources"]:
            check_url(source.get("url"), source["id"])
            if not source.get("local_record"):
                raise ValueError(f"sources: {source['id']}: missing local_record")
            if not source.get("evidence_excerpt"):
                raise ValueError(f"sources: {source['id']}: missing evidence_excerpt")

        for collection_name, key, id_set in (
            ("projects", "projects", ids["project"]),
            ("facilities", "facilities", ids["facility"]),
            ("software", "software", ids["software"]),
            ("roles", "roles", ids["role"]),
        ):
            for row in loaded[collection_name][key]:
                for source_id in row.get("source_ids", []):
                    if source_id not in ids["source"]:
                        raise ValueError(f"{collection_name}: {row['id']}: dangling source {source_id!r}")

        all_nodes = set().union(*ids.values())
        for edge in loaded["edges"]["edges"]:
            if edge.get("from") not in all_nodes:
                raise ValueError(f"edges: dangling from node {edge.get('from')!r}")
            if edge.get("to") not in all_nodes:
                raise ValueError(f"edges: dangling to node {edge.get('to')!r}")
            source_ids = edge.get("source_ids")
            if not isinstance(source_ids, list):
                raise ValueError(f"edges: {edge.get('from')} -> {edge.get('to')}: source_ids must be a list")
            if edge.get("evidence") != "local" and not source_ids:
                raise ValueError(f"edges: non-local edge {edge.get('from')} -> {edge.get('to')} needs a source")
            for source_id in source_ids:
                if source_id not in ids["source"]:
                    raise ValueError(f"edges: dangling source {source_id!r}")

    except ValueError as exc:
        print(f"registry validation failed: {exc}", file=sys.stderr)
        return 1

    counts = ", ".join(f"{name}={len(values)}" for name, values in ids.items())
    print(f"registry valid: {counts}, edges={len(loaded['edges']['edges'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
