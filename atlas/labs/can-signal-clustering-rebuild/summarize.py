"""Flatten raw JSON outputs into results CSVs (one row per number reported in
the README, with the raw file and key it came from). Independent rebuild.
Usage: python -I summarize.py <raw dir> <lab dir>"""
import csv
import json
import os
import sys

raw, lab = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_r0 import CATS, CONV, PAPER_T2, PAPER_T3_TP  # noqa: E402


def load(n):
    p = os.path.join(raw, n)
    return json.load(open(p)) if os.path.exists(p) else None


rows = []
r0, sens, a3 = load("r0.json"), load("sens.json"), load("a3.json")
variants = []
if r0:
    variants.append(("primary_global", "r0.json", "primary", r0["primary"]["linkages"], r0["primary"]["N"]))
if sens:
    for k in ("A2_min_hz_9_5", "A4_one_minus_r"):
        variants.append((k, "sens.json", k, sens[k]["linkages"], sens[k]["N"]))
if a3:
    variants.append(("A3_pairwise", "a3.json", "A3_pairwise_ward", {"ward": a3["A3_pairwise_ward"]},
                     f'{a3["A3_pairwise_ward"]["pair_N_min"]}-{a3["A3_pairwise_ward"]["pair_N_max"]}'))
with open(os.path.join(lab, "results_table2.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["variant", "N", "linkage", "category", "paper_p", "p_two_sided", "p_greater", "p_legacy_half",
                "median_benign", "median_attack", "direction", "raw_file", "raw_key"])
    for v, fn, key, links, N in variants:
        for m, o in links.items():
            for c in CATS:
                t = o["table2"][c]
                w.writerow([v, N, m, c, PAPER_T2[c][m], f'{t["two_sided"]:.4g}', f'{t["greater"]:.4g}',
                            f'{t["legacy_half"]:.4g}', f'{t["median_benign"]:.4f}', f'{t["median_attack"]:.4f}',
                            "attack<benign" if t["median_attack"] < t["median_benign"] else "attack>=benign",
                            fn, f"{key}.linkages.{m}.table2.{c}" if fn != "a3.json" else f"{key}.table2.{c}"])
with open(os.path.join(lab, "results_table3.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["variant", "convention", "mode", "FP_of_tests", "FPR", "category", "paper_TP", "TP", "FN",
                "precision", "recall", "f1", "raw_file"])
    for v, fn, key, links, N in variants:
        if "ward" not in links or "table3" not in links["ward"]:
            continue
        t3 = links["ward"]["table3"]
        for cv in CONV:
            for mode in ("group", "perfile"):
                r = t3[cv][mode]
                for c in CATS:
                    mm = r["metrics"][c]
                    w.writerow([v, cv, mode, r["FP"], f'{r["FPR"]:.4f}', c, PAPER_T3_TP[c] if mode == "group" else "",
                                mm["TP"], mm["FN"], f'{mm["precision"]:.4f}', f'{mm["recall"]:.4f}', f'{mm["f1"]:.4f}', fn])
q1 = load("q1.json")
if q1:
    with open(os.path.join(lab, "results_q1.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["variant", "attack_file", "p_two_sided", "p_greater", "median_benign_pairs", "median_vs_benign", "raw_key"])
        for v, o in q1.items():
            if not isinstance(o, dict) or "per_file" not in o:
                continue
            for x, t in o["per_file"].items():
                w.writerow([v, x, f'{t["two_sided"]:.4g}', f'{t["greater"]:.4g}', f'{t["median_benign"]:.4f}',
                            f'{t["median_attack"]:.4f}', f"q1.json:{v}.per_file.{x}"])
with open(os.path.join(lab, "results_q2_q3.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["raw_file", "test", "category", "p_two_sided", "p_greater", "median_benign", "median_test", "n_benign", "n_test", "N"])
    for fn in sorted(os.listdir(raw)):
        if not (fn.startswith("q2") or fn.startswith("q3")) or not fn.endswith(".json"):
            continue
        d = load(fn)
        for k, o in d.items():
            if isinstance(o, dict) and "table2" in o:
                N = o["meta"].get("N", o["meta"].get("N_median"))
                for c, t in o["table2"].items():
                    w.writerow([fn, k, c, f'{t["two_sided"]:.4g}', f'{t["greater"]:.4g}', f'{t["median_benign"]:.4f}',
                                f'{t["median_attack"]:.4f}', t["n_benign"], t["n_attack"], N])
        for i, rep in enumerate(d.get("crops", [])):
            N = rep["meta"].get("N", rep["meta"].get("N_median"))
            for c, t in rep["category"].items():
                w.writerow([fn, f"crop_rep{i}", c, f'{t["two_sided"]:.4g}', f'{t["greater"]:.4g}', f'{t["median_benign"]:.4f}',
                            f'{t["median_attack"]:.4f}', t["n_benign"], t["n_attack"], N])
print("ok")

# pooled crop summaries (Q2b), one row per mode
pool = {}
for fn in sorted(os.listdir(raw)):
    if fn.startswith("q2_") and fn.endswith(".json"):
        d = load(fn)
        for rep in d.get("crops", []):
            p = pool.setdefault(d["mode"], dict(files=set(), reps=0, crops=[], cats=[]))
            p["files"].add(fn); p["reps"] += 1
            p["crops"] += list(rep["per_crop"].values()); p["cats"] += list(rep["category"].values())
with open(os.path.join(lab, "results_q2_crops_pooled.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["mode", "raw_files", "replicates", "crops", "per_crop_sig_greater", "per_crop_sig_two_sided",
                "category_tests", "category_sig_greater", "category_sig_two_sided", "category_sig_two_sided_crop_more_similar"])
    for m, p in pool.items():
        c, k = p["crops"], p["cats"]
        w.writerow([m, ";".join(sorted(p["files"])), p["reps"], len(c),
                    f'{sum(v["greater"] < 0.05 for v in c) / len(c):.4f}', f'{sum(v["two_sided"] < 0.05 for v in c) / len(c):.4f}',
                    len(k), f'{sum(v["greater"] < 0.05 for v in k) / len(k):.4f}', f'{sum(v["two_sided"] < 0.05 for v in k) / len(k):.4f}',
                    sum(v["two_sided"] < 0.05 and v["median_attack"] > v["median_benign"] for v in k)])
