"""Compare can_ids.py (Atlas re-implementation) with the pinned ORNL
helper_functions.py on small ROAD inputs.

The pinned module is loaded by explicit file path with importlib; its top level
is only imports and defs (checked with grep). matplotlib.pyplot and cProfile are
imported there but never used by the functions called, so matplotlib is stubbed
rather than installed. Nothing else from the checkout is executed.

Usage: python -I equivalence_check.py <checkout_dir> <road_dir> <out_json>
"""
import contextlib
import importlib.util
import io
import json
import os
import sys
import types

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # lab folder only
import can_ids as A  # noqa: E402

checkout, road, out = sys.argv[1:4]
mpl = types.ModuleType("matplotlib")
mpl.pyplot = types.ModuleType("matplotlib.pyplot")
sys.modules["matplotlib"] = mpl
sys.modules["matplotlib.pyplot"] = mpl.pyplot
spec = importlib.util.spec_from_file_location("helper_functions_e0c862d",
                                              os.path.join(checkout, "code", "helper_functions.py"))
H = importlib.util.module_from_spec(spec)
spec.loader.exec_module(H)

meta = json.load(open(os.path.join(road, "attacks", "capture_metadata.json")))
res = {}

# 1. parsing + time diffs + labels on three small attack logs
for name in ["fuzzing_attack_3", "correlated_signal_attack_3", "max_engine_coolant_temp_attack"]:
    p = os.path.join(road, "attacks", name + ".log")
    o = H.add_time_diff_per_aid_col(H.make_can_df(p))
    m = A.add_time_diff_per_aid_col(A.make_can_df(p))
    mt = meta[name]
    aid = "XXX" if mt["injection_id"] == "XXX" else int(mt["injection_id"], 16)
    o = H.add_actual_attack_col(o, [tuple(mt["injection_interval"])], aid, mt["injection_data_str"])
    lab = A.label_published(m, mt)
    # compare on (aid, time) keys since quicksort vs mergesort may reorder exact ties
    ok_ = o.sort_values(["aid", "time"], kind="mergesort")
    r = {"rows_orig": int(len(o)), "rows_mine": int(len(m)),
         "aid_equal": bool((ok_.aid.values == m.aid.values).all()),
         "time_max_abs_diff": float(np.abs(ok_.time.values - m.time.values).max()),
         "tdiff_max_abs_diff": float(np.abs(ok_.time_diffs.values - m.time_diffs.values).max()),
         "labels_orig": int(o.actual_attack.sum()), "labels_mine": int(lab.sum()),
         "data_equal": bool((ok_.data.values == m.data.values).all())}
    res["parse_" + name] = r

# 2. training with an identical global seed, on one small ambient log
p = os.path.join(road, "ambient", "ambient_dyno_reverse.log")
tr = A.add_time_diff_per_aid_col(A.make_can_df(p))[["time", "aid", "time_diffs"]]
np.random.seed(123)
with contextlib.redirect_stdout(io.StringIO()):
    d_o = {aid: H.train(tr, aid) for aid in tr.aid.unique()}
np.random.seed(123)
d_m = A.train(tr)
res["train_mu_max_rel_diff"] = max(abs(d_o[a]["mu"] - d_m[a]["mu"]) / d_m[a]["mu"] for a in d_m)
res["train_std_max_rel_diff"] = max(abs(d_o[a]["std"] - d_m[a]["std"]) / max(d_m[a]["std"], 1e-12) for a in d_m)
res["train_aids"] = len(d_m)

# 3. detectors on one attack log, using d_m for both (aids seen in training only)
name = "max_engine_coolant_temp_attack"
pth = os.path.join(road, "attacks", name + ".log")
o = H.add_time_diff_per_aid_col(H.make_can_df(pth))
o = o[o.aid.isin(list(d_m))].copy()
mt = meta[name]
o = H.add_actual_attack_col(o, [tuple(mt["injection_interval"])], int(mt["injection_id"], 16), mt["injection_data_str"])
m = A.add_time_diff_per_aid_col(A.make_can_df(pth))
m = m[m.aid.isin(list(d_m))].reset_index(drop=True)
lab = A.label_published(m, mt)
pm = A.MEAN_P[8]
o = H.alert_by_mean_various_p(o, d_o, pm)
o["alert_window"] = o.predicted_attack.rolling(6).sum() >= 3
from sklearn.metrics import confusion_matrix  # noqa: E402
res["mean_cm_orig"] = confusion_matrix(o.actual_attack, o.alert_window, labels=[0, 1]).tolist()
res["mean_cm_mine"] = A.cm(lab, A.window_3of6(A.flags_mean(m, d_m, pm))).tolist()
pb = A.BIN_P[5]
res["bin_cm_orig"] = H.alert_by_bin_various_p(o, d_o, pb).tolist()
res["bin_cm_mine"] = A.cm(lab, A.alert_binning(m, d_m, pb)).tolist()
# Gaussian thresholds: original O(n^2) Python loop on 5 aids, all 18 p values
aids5 = list(d_m)[:5]
for a in aids5:
    d_o[a]["y_thresholds_gauss"] = {}
maxrel = 0.0
for p_ in A.GAUSS_P:
    for a in aids5:
        H.y_threshold_gauss(d_o, a, p_)
A.gauss_thresholds({a: d_m[a] for a in aids5}, A.GAUSS_P)
for p_ in A.GAUSS_P:
    for a in aids5:
        yo, ym = d_o[a]["y_thresholds_gauss"][p_], d_m[a]["y_thr_gauss"][p_]
        maxrel = max(maxrel, abs(yo - ym) / max(abs(yo), 1e-300))
res["gauss_thr_max_rel_diff_5aids_18p"] = maxrel
json.dump(res, open(out, "w"), indent=1)
print(json.dumps(res, indent=1))
