"""Build results.csv (one row per claim) from raw/*.json. Atlas-authored.
Usage: python -I summarize.py <raw_dir> <out_csv>
"""
import csv
import json
import os
import sys

raw, out = sys.argv[1:3]
J = lambda n: json.load(open(os.path.join(raw, n)))  # noqa: E731
r0, q1, q2, q3 = J("r0_seed0.json")["r0"], J("q1.json"), J("q2.json"), J("q3.json")
rows = []


def add(q, item, m, src):
    rows.append({"q": q, "item": item, "cm": m.get("cm"), "prec": m.get("prec"), "recall": m.get("recall"),
                 "f1": m.get("f1"), "fpr": m.get("fpr"), "source": src})


add("R0", "Mean a=0.444 3of6, published labels", r0["optima"]["mean"], "r0_seed0.json:r0.optima.mean")
add("R0", "Binning a=3.5, published labels", r0["optima"]["binning"], "r0_seed0.json:r0.optima.binning")
add("R0", "Gaussian p=0.09 3consec, published labels", q2["gauss_3consec"]["0.09"], "q2.json:gauss_3consec['0.09']")
for k in ["mean", "binning", "gauss"]:
    add("Q1", f"{k} on 13 masquerade logs (aggregate)", q1["aggregate"][k], f"q1.json:aggregate.{k}")
for f in q1["per_file"]:
    rows.append({"q": "Q1", "item": f"{f['file']} recall mean/bin/gauss",
                 "recall": f"{f['mean']['recall']:.4f}/{f['binning']['recall']:.4f}/{f['gauss']['recall']:.4f}",
                 "prec": f"gauss {f['gauss']['prec']:.4f}", "fpr": f"gauss {f['gauss']['fpr']:.4f}",
                 "source": "q1.json:per_file"})
best = max(q2["gauss_3of6"].items(), key=lambda kv: kv[1]["f1"] or 0)
add("Q2", "Gaussian p=0.09 3of6", q2["gauss_3of6"]["0.09"], "q2.json:gauss_3of6['0.09']")
add("Q2", f"Gaussian 3of6 best (p={best[0]})", best[1], f"q2.json:gauss_3of6['{best[0]}']")
add("Q2", "Mean a=0.444 3consec", q2["mean_3consec"]["0.4444444444444444"], "q2.json:mean_3consec['0.4444444444444444']")
bm = max(q2["mean_3consec"].items(), key=lambda kv: kv[1]["f1"] or 0)
add("Q2", f"Mean 3consec best (a={bm[0]})", bm[1], f"q2.json:mean_3consec['{bm[0]}']")
for k in ["mean", "binning"]:
    add("Q3", f"{k} at optimum, payload labels, all 16", q3["payload_labels_all16"][k], f"q3.json:payload_labels_all16.{k}")
pp = sum(r["pos_pub"] for r in q3["per_file"])
pa = sum(r["pos_pay"] for r in q3["per_file"])
rows.append({"q": "Q3", "item": f"13 targeted logs: positives published {pp}, payload {pa}, share {pa / pp:.4f}",
             "source": "q3.json:per_file"})
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["q", "item", "cm", "prec", "recall", "f1", "fpr", "source"])
    w.writeheader()
    for r in rows:
        w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})
print(open(out).read())
