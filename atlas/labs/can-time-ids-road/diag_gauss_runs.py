"""Diagnostic for Q2: why does Gaussian+3-consecutive miss flam attacks when it
flags ~70% of in-interval target frames? Reports, for one capture, the target
aid's training mu/std, the Gaussian p=0.09 acceptance band, run lengths of
flagged frames inside the interval, and the gap pattern (gap/mu) of the first
24 in-interval frames. Atlas-authored.

Usage: python -I diag_gauss_runs.py <road_dir> <training_csv> <capture> <out_json>
"""
import json
import os
import sys
from collections import Counter

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import can_ids as A  # noqa: E402

road, tcsv, name, out = sys.argv[1:5]
tr = pd.read_csv(tcsv)
D = {int(r.aid, 16): {"mu": r.mu, "std": r["std"]} for _, r in tr.iterrows()}
A.gauss_thresholds(D, A.GAUSS_P)
meta = json.load(open(os.path.join(road, "attacks", "capture_metadata.json")))[name]
df = A.add_time_diff_per_aid_col(A.make_can_df(os.path.join(road, "attacks", name + ".log")))
df = df[df.aid.isin(list(D))].reset_index(drop=True)
df["y"] = A.label_published(df, meta)
df["pay"] = A.label_payload(df, meta)
aid = int(meta["injection_id"], 16)
v = D[aid]
p = A.GAUSS_P[-1]
gv = A.gauss_vals(df, D)
fl = A.flags_gauss(df, gv, D, p)
alert = A.window_3consec(fl)
sel = np.where(df.y.values)[0]
s = fl[sel]
runs = Counter()
k = 0
for b in list(s) + [False]:
    if b:
        k += 1
    elif k:
        runs[k] += 1
        k = 0
# acceptance band in units of std, from the threshold density
yt = v["y_thr_gauss"][p]
z = float(np.sqrt(-2 * np.log(yt * v["std"] * np.sqrt(2 * np.pi)))) if yt > 0 else None
seq = df.iloc[sel[:24]]
res = {"capture": name, "aid": hex(aid), "mu": v["mu"], "std": v["std"], "std_over_mu": v["std"] / v["mu"],
       "p": p, "flag_if_abs_z_ge": z,
       "in_interval_frames": int(len(sel)), "flagged": int(s.sum()),
       "flag_run_length_counts": {str(a): b for a, b in sorted(runs.items())},
       "alerts_on_in_interval_frames": int(alert[sel].sum()),
       "first24_gap_over_mu": [round(x / v["mu"], 3) for x in seq.time_diffs],
       "first24_is_payload_match": [bool(x) for x in seq.pay],
       "first24_flag": [bool(x) for x in fl[sel[:24]]],
       "flag_rate_payload_frames": float(fl[sel][df.pay.values[sel]].mean()),
       "flag_rate_legit_frames": float(fl[sel][~df.pay.values[sel]].mean())}
json.dump(res, open(out, "w"), indent=1)
print(json.dumps(res, indent=1))
