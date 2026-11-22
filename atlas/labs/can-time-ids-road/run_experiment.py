"""Atlas-authored driver for R0, Q1, Q2, Q3. Uses can_ids.py only (no checkout
code). Files are taken in sorted name order and keyed by name, not by bare
os.listdir position.

Usage: python -I run_experiment.py <road_dir> <out_dir> --seed N [--r0-only]
"""
import argparse
import json
import os
import sys
import time

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import can_ids as A  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("road")
ap.add_argument("out")
ap.add_argument("--seed", type=int, default=0)
ap.add_argument("--r0-only", action="store_true")
args = ap.parse_args()
os.makedirs(args.out, exist_ok=True)
T0 = time.time()
log = {"seed": args.seed, "timings_s": {}}


def tick(k):
    log["timings_s"][k] = round(time.time() - T0, 1)
    print(f"[{time.time() - T0:7.1f}s] {k}", flush=True)


def dump(name, obj):
    with open(os.path.join(args.out, name), "w") as f:
        json.dump(obj, f, indent=1, default=float)


def fix(o):
    """json-friendly metrics with nan -> None."""
    return {k: (None if isinstance(v, float) and np.isnan(v) else v) for k, v in o.items()}


# ---------- training (notebook cells 6, 12) ----------
amb = os.path.join(args.road, "ambient")
train_files = sorted(f for f in os.listdir(amb) if "dyno" in f and f.endswith(".log"))
parts = []
for f in train_files:
    df = A.add_time_diff_per_aid_col(A.make_can_df(os.path.join(amb, f)))
    parts.append(df[["time", "aid", "time_diffs"]])
train_df = pd.concat(parts, ignore_index=True)
del parts
log["train_files"] = train_files
log["train_rows"] = int(len(train_df))
tick("parsed training")
np.random.seed(args.seed)
D = A.train(train_df)
log["train_aids"] = len(D)
del train_df
tick("trained")
pd.DataFrame([{"aid": hex(a), **{k: v for k, v in D[a].items()}} for a in D]).to_csv(
    os.path.join(args.out, f"training_seed{args.seed}.csv"), index=False)

# ---------- test sets (cells 17, 21, 27) ----------
att = os.path.join(args.road, "attacks")
meta = json.load(open(os.path.join(att, "capture_metadata.json")))
logs = sorted(f for f in os.listdir(att) if f.endswith(".log"))
fab = [f[:-4] for f in logs if "masquerade" not in f and "accelerator" not in f]
masq = [f[:-4] for f in logs if "masquerade" in f]
log["fabrication_files"] = fab
log["masquerade_files"] = masq


def load(name):
    df = A.add_time_diff_per_aid_col(A.make_can_df(os.path.join(att, name + ".log")))
    unseen = sorted(set(df.aid.unique()) - set(D))
    n_unseen = int(df.aid.isin(unseen).sum())
    df = df[~df.aid.isin(unseen)].reset_index(drop=True)  # original would KeyError
    df["y_pub"] = A.label_published(df, meta[name])
    df["y_pay"] = A.label_payload(df, meta[name])
    return df, {"unseen_aids": [hex(a) for a in unseen], "unseen_rows": n_unseen}


FAB = {}
unseen_info = {}
for n in fab:
    FAB[n], unseen_info[n] = load(n)
tick("loaded fabrication")
log["fab_rows"] = int(sum(len(v) for v in FAB.values()))
log["fab_pos_published"] = int(sum(v.y_pub.sum() for v in FAB.values()))
log["fab_unseen"] = unseen_info

# precompute flags/alerts per file
MEAN_I, BIN_I = 8, 5
pm, pb = A.MEAN_P[MEAN_I], A.BIN_P[BIN_I]


def sweep(dfs, label, alert_fn, ps):
    out = {}
    for p in ps:
        c = np.zeros((2, 2), dtype=np.int64)
        for n, df in dfs.items():
            c += A.cm(df[label].values, alert_fn(df, p))
        out[repr(float(p))] = fix(A.metrics(c))
    return out


mean36 = lambda df, p: A.window_3of6(A.flags_mean(df, D, p))  # noqa: E731
mean3c = lambda df, p: A.window_3consec(A.flags_mean(df, D, p))  # noqa: E731
binning = lambda df, p: A.alert_binning(df, D, p)  # noqa: E731

r0 = {"mean_3of6": sweep(FAB, "y_pub", mean36, A.MEAN_P)}
tick("R0 mean sweep")
r0["binning"] = sweep(FAB, "y_pub", binning, A.BIN_P)
tick("R0 binning sweep")
per_file = []
for n, df in FAB.items():
    per_file.append({"file": n, "rows": len(df), "pos_pub": int(df.y_pub.sum()),
                     "pos_pay": int(df.y_pay.sum()),
                     "mean_cm": A.cm(df.y_pub, mean36(df, pm)).tolist(),
                     "bin_cm": A.cm(df.y_pub, binning(df, pb)).tolist()})
r0["per_file_at_optima"] = per_file
r0["optima"] = {"mean_p": float(pm), "bin_p": float(pb),
                "mean": r0["mean_3of6"][repr(float(pm))], "binning": r0["binning"][repr(float(pb))]}
r0["published"] = {"mean": {"cm": [[1525274, 1473], [239, 61277]], "f1": 0.9862},
                   "binning": {"cm": [[1525895, 852], [514, 61002]], "f1": 0.9889},
                   "rows": 1588263, "positives": 61516}
dump(f"r0_seed{args.seed}.json", {"log": log, "r0": r0})
if args.r0_only:
    sys.exit(0)

# ---------- Q2: sufficiency-rule swap ----------
A.gauss_thresholds(D, A.GAUSS_P)
GV = {n: A.gauss_vals(df, D) for n, df in FAB.items()}
tick("gauss thresholds + vals")
g3c = lambda df, p: A.window_3consec(A.flags_gauss(df, GV[df.attrs["name"]], D, p))  # noqa: E731
g36 = lambda df, p: A.window_3of6(A.flags_gauss(df, GV[df.attrs["name"]], D, p))  # noqa: E731
for n, df in FAB.items():
    df.attrs["name"] = n
q2 = {"gauss_3consec": sweep(FAB, "y_pub", g3c, A.GAUSS_P),
      "gauss_3of6": sweep(FAB, "y_pub", g36, A.GAUSS_P),
      "mean_3consec": sweep(FAB, "y_pub", mean3c, A.MEAN_P),
      "published_gauss_p0.09": {"f1": 0.2600, "prec": 0.334, "recall": 0.213}}
tick("Q2 sweeps")
# supporting measure: isolated flags among in-interval target frames, 0xD0 capture
sm = {}
for n in [x for x in fab if x.startswith("max_speedometer") or x.startswith("reverse_light")]:
    df = FAB[n]
    aid = int(meta[n]["injection_id"], 16)
    fl = A.flags_gauss(df, GV[n], D, A.GAUSS_P[-1])
    fm = A.flags_mean(df, D, pm)
    sel = np.where(df.y_pub.values)[0]  # target aid, in interval; contiguous within aid block
    res = {}
    for k, f in [("gauss_p0.09", fl), ("mean_0.444", fm)]:
        s = f[sel]
        left = np.r_[False, s[:-1]]
        right = np.r_[s[1:], False]
        flagged = s.sum()
        res[k] = {"in_interval_target_frames": int(len(s)), "flagged": int(flagged),
                  "isolated_share": float((s & ~left & ~right).sum() / flagged) if flagged else None}
    sm[n] = res
q2["isolated_flag_measure"] = sm
dump("q2.json", q2)

# ---------- Q3: payload relabel ----------
q3 = {"published_labels": {"mean": r0["optima"]["mean"], "binning": r0["optima"]["binning"]},
      "payload_labels_all16": {"mean": fix(A.metrics(sum(A.cm(df.y_pay, mean36(df, pm)) for df in FAB.values()))),
                               "binning": fix(A.metrics(sum(A.cm(df.y_pay, binning(df, pb)) for df in FAB.values())))}}
targ = [n for n in fab if meta[n]["injection_id"] != "XXX"]
q3["payload_labels_13targeted"] = {
    "mean": fix(A.metrics(sum(A.cm(FAB[n].y_pay, mean36(FAB[n], pm)) for n in targ))),
    "binning": fix(A.metrics(sum(A.cm(FAB[n].y_pay, binning(FAB[n], pb)) for n in targ)))}
q3["published_labels_13targeted"] = {
    "mean": fix(A.metrics(sum(A.cm(FAB[n].y_pub, mean36(FAB[n], pm)) for n in targ))),
    "binning": fix(A.metrics(sum(A.cm(FAB[n].y_pub, binning(FAB[n], pb)) for n in targ)))}
rows = []
for n in targ:
    df = FAB[n]
    raw_f = sum(1 for _ in open(os.path.join(att, n + ".log")))
    mq = n + "_masquerade"
    raw_m = sum(1 for _ in open(os.path.join(att, mq + ".log"))) if mq + ".log" in logs else None
    dl = df.time_diffs.values[df.y_pay.values]
    rows.append({"file": n, "pos_pub": int(df.y_pub.sum()), "pos_pay": int(df.y_pay.sum()),
                 "share": float(df.y_pay.sum() / df.y_pub.sum()),
                 "raw_lines_fab_minus_masq": (raw_f - raw_m) if raw_m is not None else None,
                 "pub_minus_pay": int(df.y_pub.sum() - df.y_pay.sum()),
                 "delta_median_s": float(np.median(dl)) if len(dl) else None,
                 "delta_p99_s": float(np.percentile(dl, 99)) if len(dl) else None,
                 "target_mu_s": D[int(meta[n]["injection_id"], 16)]["mu"]})
q3["per_file"] = rows
dump("q3.json", q3)
tick("Q3")

# ---------- Q1: masquerade ----------
q1 = []
agg = {k: np.zeros((2, 2), dtype=np.int64) for k in ["mean", "binning", "gauss"]}
for n in masq:
    df, ui = load(n)
    gv = A.gauss_vals(df, D)
    alerts = {"mean": mean36(df, pm), "binning": binning(df, pb),
              "gauss": A.window_3consec(A.flags_gauss(df, gv, D, A.GAUSS_P[-1]))}
    row = {"file": n, "rows": len(df), "pos": int(df.y_pub.sum()), **ui}
    pos_idx = np.where(df.y_pub.values)[0]
    for k, a in alerts.items():
        c = A.cm(df.y_pub, a)
        agg[k] += c
        m = A.metrics(c)
        tp_rank = np.where(a[pos_idx])[0]  # rank of TP among in-interval target frames
        row[k] = {"cm": m["cm"], "recall": m["recall"], "fpr": m["fpr"], "prec": m["prec"],
                  "tp_within5_of_edge": int(((tp_rank < 5) | (tp_rank >= len(pos_idx) - 5)).sum()),
                  "tp_total": int(len(tp_rank))}
    # timing check: target-aid gap stats inside vs outside the interval
    aid = int(meta[n]["injection_id"], 16)
    tgt = df[df.aid == aid]
    row["target_gap_median_in"] = float(tgt.time_diffs[tgt.y_pub].median())
    row["target_gap_median_out"] = float(tgt.time_diffs[~tgt.y_pub].median())
    row["target_mu"] = D[aid]["mu"]
    q1.append(row)
dump("q1.json", {"per_file": q1, "aggregate": {k: fix(A.metrics(v)) for k, v in agg.items()}})
tick("Q1")
dump(f"run_log_seed{args.seed}.json", log)
