"""Atlas-authored re-implementation of the time-based CAN detectors in
pmoriano/can-time-based-ids-benchmark @ e0c862d6c6cbb0d60ed2572a90dd483a3253ed0f
(code/helper_functions.py). This is NOT ORNL's code; each function cites the
lines it re-implements. equivalence_check.py compares it with the pinned module.

Vectorised so that the full run fits in well under an hour; semantics follow the
original, including its quirks (rolling windows that cross aid boundaries for
Mean/Gaussian, 6-gap Binning window, inclusive interval bounds).
"""
import re

import numpy as np
import pandas as pd
import scipy.stats
from sklearn.covariance import EllipticEnvelope

MEAN_P = np.linspace(0, 1, 19)          # get_results_mean_various_p L597
BIN_P = np.linspace(1, 10, 19)          # get_results_binning_various_p L807
GAUSS_P = sorted(list(np.arange(0.001, 0.01, 0.001)) + list(np.arange(0.01, 0.1, 0.01)))  # L712


def make_can_df(path):
    """make_can_df L96-L115: candump '(ts) can0 AID#DATA'; drop first and last line
    (skiprows=1, skipfooter=1); hex aid; zfill(16) data; time re-zeroed to the min
    of the remaining rows; keep aid <= 0x700 (after re-zeroing)."""
    raw = pd.read_csv(path, sep=" ", header=None, names=["ts", "bus", "frame"],
                      dtype=str, engine="c")
    raw = raw.iloc[1:-1]
    t = raw["ts"].str.slice(1, -1).astype(float)
    parts = raw["frame"].str.split("#", n=1, expand=True)
    aid = parts[0].map(lambda x: int(x, 16))
    data = parts[1].fillna("").str.zfill(16)
    df = pd.DataFrame({"time": t.values - t.min(), "aid": aid.values.astype(np.int64),
                       "data": data.values})
    return df[df.aid <= 0x700].reset_index(drop=True)


def add_time_diff_per_aid_col(df):
    """add_time_diff_per_aid_col L192-L205: sort (aid, time), diff, drop first frame
    of each aid. Result stays aid-major. (Original uses the default quicksort;
    a stable sort is used here so tied rows keep file order.)"""
    df = df.sort_values(["aid", "time"], kind="mergesort").copy()
    df["time_diffs"] = df["time"].diff()
    mask = df.aid == df.aid.shift(1)
    return df[mask].reset_index(drop=True)


def train(df):
    """train L289-L311, applied per aid in df.aid.unique() order (notebook cell 12).
    EllipticEnvelope(contamination=1e-4, support_fraction=0.999); mu, std (ddof 0)
    of inliers. Uses numpy's global RNG like the original (no random_state)."""
    d = {}
    for aid, g in df.groupby("aid", sort=False):
        x = g.time_diffs.values
        inl = EllipticEnvelope(contamination=0.0001, support_fraction=0.999).fit_predict(x.reshape(-1, 1))
        x = x[inl != -1]
        d[int(aid)] = {"mu": float(x.mean()), "std": float(x.std()), "n": int(len(x)),
                       "n_outliers": int((inl == -1).sum())}
    return d


def interval_mask(time, intervals):
    """add_actual_attack_col L255-L265 time test: inclusive [start, end]."""
    m = np.zeros(len(time), dtype=bool)
    for a, b in intervals:
        m |= (time >= a) & (time <= b)
    return m


def label_published(df, meta):
    """add_actual_attack_col: aid == injection_id in interval; for fuzzing ('XXX')
    data == injection_data_str exactly."""
    m = interval_mask(df.time.values, [tuple(meta["injection_interval"])])
    if meta["injection_id"] != "XXX":
        return m & (df.aid.values == int(meta["injection_id"], 16))
    return m & (df.data.values == meta["injection_data_str"])


def label_payload(df, meta):
    """Q3 relabel: also require payload match, X -> regex '.', unanchored
    str.contains as in the commented-out get_injection_interval L234-L237."""
    if meta["injection_id"] == "XXX":
        return label_published(df, meta)
    m = label_published(df, meta)
    pat = meta["injection_data_str"].replace("X", ".")
    return m & df.data.str.contains(pat, regex=True).values


def _mu(df, d):
    return df.aid.map(lambda a: d[a]["mu"]).values


def flags_mean(df, d, p):
    """alert_by_mean_various_p L391-L396: time_diffs <= p*mu[aid]."""
    return df.time_diffs.values <= p * _mu(df, d)


def window_3of6(flags):
    """get_results_mean_various_p L606: rolling(6).sum() >= 3 over the whole
    aid-sorted frame (crosses aid boundaries, as in the original)."""
    return (pd.Series(flags.astype(float)).rolling(6).sum() >= 3).values


def window_3consec(flags):
    """get_results_gauss L723: rolling(3).sum() == 3."""
    return (pd.Series(flags.astype(float)).rolling(3).sum() == 3).values


def alert_binning(df, d, p, n=6):
    """alert_by_bin_various_p L524-L538: per aid, rolling(n).sum() of time_diffs
    <= p*mu. Rows are aid-major so per-aid results concatenate in row order."""
    out = np.zeros(len(df), dtype=bool)
    for aid, idx in df.groupby("aid", sort=False).indices.items():
        s = df.time_diffs.iloc[idx].rolling(n).sum()
        out[idx] = (s <= p * d[aid]["mu"]).values
    return out


def gauss_thresholds(d, ps):
    """y_threshold_gauss L366-L380, vectorised: grid arange(mu-5s, mu+5s, 10s/1000);
    pv_i = sum_{j: y_j <= y_i} y_j * step; threshold = max y_i with pv_i <= p."""
    for aid, v in d.items():
        mu, s = v["mu"], v["std"]
        step = 10 * s / 1000
        x = np.arange(mu - 5 * s, mu + 5 * s, step)
        y = scipy.stats.norm(loc=mu, scale=s).pdf(x)
        pvs = (y[None, :] * (y[None, :] <= y[:, None])).sum(axis=1) * step
        v["y_thr_gauss"] = {}
        for p in ps:
            sel = np.where(pvs <= p)[0]
            v["y_thr_gauss"][p] = float(np.max(y[sel])) if len(sel) else 0.0


def gauss_vals(df, d):
    """add_gauss_val_col L280-L286: Gaussian pdf of each frame's time_diff."""
    out = np.zeros(len(df))
    for aid, idx in df.groupby("aid", sort=False).indices.items():
        v = d[aid]
        out[idx] = scipy.stats.norm(loc=v["mu"], scale=v["std"]).pdf(df.time_diffs.values[idx])
    return out


def flags_gauss(df, vals, d, p):
    """alert_by_gauss L444-L449: pdf(x) <= y_thr[aid][p]."""
    thr = df.aid.map(lambda a: d[a]["y_thr_gauss"][p]).values
    return vals <= thr


def cm(actual, pred):
    """2x2 confusion matrix [[TN, FP], [FN, TP]] with fixed labels."""
    a = np.asarray(actual, bool)
    b = np.asarray(pred, bool)
    return np.array([[int((~a & ~b).sum()), int((~a & b).sum())],
                     [int((a & ~b).sum()), int((a & b).sum())]])


def metrics(c):
    tn, fp, fn, tp = int(c[0, 0]), int(c[0, 1]), int(c[1, 0]), int(c[1, 1])
    prec = tp / (tp + fp) if tp + fp else float("nan")
    rec = tp / (tp + fn) if tp + fn else float("nan")
    f1 = 2 * prec * rec / (prec + rec) if (tp + fp and tp + fn and prec + rec) else float("nan")
    fpr = fp / (fp + tn) if fp + tn else float("nan")
    return {"cm": [[tn, fp], [fn, tp]], "prec": prec, "recall": rec, "f1": f1, "fpr": fpr}
