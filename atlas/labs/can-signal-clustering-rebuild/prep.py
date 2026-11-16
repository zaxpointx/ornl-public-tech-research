"""Parse the 12 benign and 13 masquerade signal CSVs once, cache them as npz,
and record per-ID rates and signal counts (vs the DBC SG_ count).
Independent rebuild; not ORNL code.
Usage: python -I prep.py <signal_extractions dir> <cache dir> <out stats.json>"""
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scs  # noqa: E402

root, cache, out = sys.argv[1:4]
guard = scs.install_guards()
t_start = time.time()
benign = sorted(json.load(open(os.path.join(root, "ambient", "metadata.json"))))
ameta = json.load(open(os.path.join(root, "attacks", "metadata.json")))
attacks = sorted(k for k in ameta if k.endswith("_masquerade"))

dbc = {}
cur = None
for line in open(os.path.join(root, "DBC", "anonymized.dbc")):
    m = re.match(r"BO_ (\d+) ", line)
    if m:
        cur = int(m.group(1)); dbc[cur] = 0
    elif line.startswith(" SG_") and cur is not None:
        dbc[cur] += 1

stats = dict(guard=guard, benign=benign, attacks=attacks, files={})
for name in benign + attacks:
    sub = "ambient" if name in benign else "attacks"
    t0 = time.time()
    parsed = scs.parse_csv(os.path.join(root, sub, name + ".csv"))
    scs.save_npz(parsed, os.path.join(cache, name + ".npz"))
    rates = scs.id_rates(parsed)
    mism = {a: (r["n_signals"], dbc.get(a)) for a, r in rates.items() if r["n_signals"] != dbc.get(a)}
    stats["files"][name] = dict(
        n_ids=len(rates), n_signals=sum(r["n_signals"] for r in rates.values()),
        first=min(r["first"] for r in rates.values()), last=max(r["last"] for r in rates.values()),
        span_max_first=max(r["first"] for r in rates.values()), span_min_last=min(r["last"] for r in rates.values()),
        ids_below_9_5hz={a: round(r["hz"], 3) for a, r in rates.items() if not r["hz"] >= 9.5},
        signal_count_vs_dbc_mismatch=mism,
        nan_cells_within_id=sum(r["nan_in_signals"] for r in rates.values()),
        rates={a: dict(n=r["n"], hz=round(r["hz"], 4), first=round(r["first"], 3), last=round(r["last"], 3), k=r["n_signals"]) for a, r in rates.items()},
        parse_s=round(time.time() - t0, 1))
    print(name, stats["files"][name]["n_ids"], stats["files"][name]["n_signals"], stats["files"][name]["parse_s"], "s", flush=True)
stats["dbc_messages"] = len(dbc)
stats["dbc_signals"] = sum(dbc.values())
stats["wall_s"] = round(time.time() - t_start, 1)
stats["peak_rss_bytes"] = scs.peak_rss()
scs.dump(stats, out)
