"""Independent rebuild of the signal-clustering-similarity method of
Moriano, Bridges, Iannacone, "Detecting CAN Masquerade Attacks with Signal
Clustering Similarity", AutoSec 2022 (OSTI 1866690).

THIS IS NOT ORNL'S CODE. ORNL's implementation (DOE CODE 134139) is closed
source. Every step below is written from the paper's text plus the choices in
deep-dives/can-signal-clustering/artifact-study.md, which are marked there as
inferred. Paper citations are p.N section of the OSTI PDF.
"""
import json
import os
import resource
import signal
import sys
import threading
import time

import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage
from scipy.stats import mannwhitneyu

GRID_HZ = 10.0          # p.4 III-D1: "baseline frequency of 10 Hz"
ALPHA = 0.9             # p.3 III-B
R = -5.0                # p.3 III-B
SIG_COLS = [f"Signal_{k}_of_ID" for k in range(1, 23)]

MEM_CAP = 8 * 1024 ** 3
TIME_CAP = 1800


# ---------------------------------------------------------------- guards
def install_guards(mem_cap=MEM_CAP, time_cap=TIME_CAP):
    """8 GiB memory and 30 min wall caps. macOS does not enforce RLIMIT_AS,
    so a watchdog thread polls peak RSS (ru_maxrss, bytes on macOS) and
    hard-exits with code 97 above the cap; SIGALRM ends the run at time_cap."""
    info = {}
    try:
        resource.setrlimit(resource.RLIMIT_AS, (mem_cap, mem_cap))
        info["rlimit_as"] = "set"
    except Exception as e:  # noqa: BLE001
        info["rlimit_as"] = f"not set: {e!r}"
    signal.signal(signal.SIGALRM, lambda *a: (sys.stderr.write("TIME CAP HIT\n"), os._exit(98)))
    signal.alarm(time_cap)

    def watch():
        while True:
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            if sys.platform != "darwin":
                rss *= 1024
            if rss > mem_cap:
                sys.stderr.write(f"MEMORY CAP HIT {rss}\n")
                os._exit(97)
            time.sleep(0.2)

    threading.Thread(target=watch, daemon=True).start()
    info.update(mem_cap_bytes=mem_cap, time_cap_s=time_cap)
    return info


def peak_rss():
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return rss if sys.platform == "darwin" else rss * 1024


# ---------------------------------------------------------------- parsing
def parse_csv(path, chunksize=2_000_000):
    """Return {id: (times float64[n], values float64[n, k])} where k is the
    number of Signal_j columns that are not all-NaN for that ID. Signal key is
    f"{id}_{j}" with j 1-based (Signal_j_of_ID)."""
    acc = {}
    dtypes = {"Label": np.int8, "Time": np.float64, "ID": np.int32}
    dtypes.update({c: np.float64 for c in SIG_COLS})
    for ch in pd.read_csv(path, dtype=dtypes, chunksize=chunksize):
        for aid, g in ch.groupby("ID", sort=False):
            acc.setdefault(int(aid), []).append(
                (g["Time"].to_numpy(), g[SIG_COLS].to_numpy()))
    out = {}
    for aid, parts in acc.items():
        t = np.concatenate([p[0] for p in parts])
        v = np.concatenate([p[1] for p in parts])
        order = np.argsort(t, kind="stable")
        t, v = t[order], v[order]
        keep = ~np.all(np.isnan(v), axis=0)
        out[aid] = (t, v[:, keep], np.flatnonzero(keep) + 1)
    return out


def save_npz(parsed, path):
    arrs = {}
    for aid, (t, v, cols) in parsed.items():
        arrs[f"t_{aid}"] = t
        arrs[f"v_{aid}"] = v
        arrs[f"c_{aid}"] = cols
    np.savez(path, **arrs)


def load_npz(path):
    z = np.load(path)
    ids = sorted({int(k[2:]) for k in z.files if k.startswith("t_")})
    return {a: (z[f"t_{a}"], z[f"v_{a}"], z[f"c_{a}"]) for a in ids}


def id_rates(parsed):
    rates = {}
    for aid, (t, v, cols) in parsed.items():
        d = np.diff(t)
        med = float(np.median(d)) if len(d) else float("nan")
        rates[aid] = dict(n=int(len(t)), first=float(t[0]), last=float(t[-1]),
                          median_dt=med, hz=(1.0 / med if med > 0 else float("nan")),
                          n_signals=int(v.shape[1]),
                          nan_in_signals=int(np.isnan(v).sum()))
    return rates


# ---------------------------------------------------------------- resample
def sporadic_ids(parsed, min_mean_hz=0.5):
    """D1: IDs whose frame count / whole-capture duration < min_mean_hz."""
    dur = max(t[-1] for t, _, _ in parsed.values()) - min(t[0] for t, _, _ in parsed.values())
    return sorted(a for a, (t, _, _) in parsed.items() if len(t) / dur < min_mean_hz)


def resample(parsed, t0=None, t1=None, min_hz=None, exclude_ids=(), min_mean_hz=0.5):
    """Linear interpolation of every signal onto a common 10 Hz grid.
    Span (A1, my choice): [max first, min last] over the kept IDs, further
    clipped to [t0, t1] if given (segments). D1: IDs below min_mean_hz
    average rate over the whole capture are dropped first. min_hz (A2
    sensitivity) drops IDs with median rate below it. Returns (grid,
    DataFrame signals), with no constant filter applied yet."""
    keep = {}
    drop = set(sporadic_ids(parsed, min_mean_hz)) | set(exclude_ids)
    for aid, (t, v, cols) in parsed.items():
        if aid in drop:
            continue
        if t0 is not None:
            m = (t >= t0) & (t <= t1)
            # keep one sample either side so interpolation inside the segment
            # uses true neighbours, never extrapolation
            idx = np.flatnonzero(m)
            if len(idx) == 0:
                continue
            lo, hi = max(idx[0] - 1, 0), min(idx[-1] + 1, len(t) - 1)
            t, v = t[lo:hi + 1], v[lo:hi + 1]
        if len(t) < 2:
            continue
        if min_hz is not None:
            md = np.median(np.diff(t))
            if not (md > 0 and 1.0 / md >= min_hz):
                continue
        keep[aid] = (t, v, cols)
    first = max(t[0] for t, _, _ in keep.values())
    last = min(t[-1] for t, _, _ in keep.values())
    if t0 is not None:
        first, last = max(first, t0), min(last, t1)
    grid = np.arange(first, last + 1e-9, 1.0 / GRID_HZ)
    data = {}
    for aid, (t, v, cols) in keep.items():
        for j, c in enumerate(cols):
            col = v[:, j]
            ok = ~np.isnan(col)
            if ok.sum() < 2:
                continue
            data[f"{aid}_{c}"] = np.interp(grid, t[ok], col[ok])
    return grid, pd.DataFrame(data, index=grid)


def nonconstant(df):
    """p.4 III-D1: 'discarded any constant time series'."""
    a = df.to_numpy()
    return list(df.columns[np.ptp(a, axis=0) > 0])


def sort_key(s):
    a, k = s.split("_")
    return (int(a), int(k))


def corr_matrix(df, elements):
    """Unit-norm scaling (p.4 III-D1) then Pearson. Unit norm cannot change
    Pearson; it is applied only to follow the text."""
    x = df[elements].to_numpy()
    x = x / np.linalg.norm(x, axis=0)
    c = np.corrcoef(x, rowvar=False)
    if np.isnan(c).any():
        raise ValueError("NaN correlation (constant column in element set)")
    return c


def link(c, method, distance="rows"):
    """A4. 'rows' (primary): rows of C as observation vectors, Euclidean, i.e.
    scipy linkage on the 2-D array. 'one_minus_r': condensed d = 2(1-r)."""
    if distance == "rows":
        return linkage(c, method=method)
    if distance == "one_minus_r":
        d = 2.0 * (1.0 - c)
        np.fill_diagonal(d, 0.0)
        d = np.clip((d + d.T) / 2.0, 0.0, None)
        iu = np.triu_indices_from(d, 1)
        return linkage(d[iu], method=method)
    raise ValueError(distance)


# ---------------------------------------------------------------- clusim
def affinity(Z):
    """clusim element-centric affinity matrix of one dendrogram. Caching this
    per dendrogram and taking mean(cL1) is the same computation as
    clusim.sim.element_sim(c1, c2, alpha, r) (r2 = r); equivalence is
    checked by check_clusim_equiv in run_r0.py."""
    from clusim.clustering import Clustering
    from clusim.clusimelement import make_affinity_matrix
    clu = Clustering().from_scipy_linkage(Z, dist_rescaled=True)
    return make_affinity_matrix(clu, alpha=ALPHA, r=R, rescale_path_type="max",
                                ppr_implementation="prpack"), clu


def sim_from_aff(a1, a2):
    from clusim.clusimelement import cL1
    return float(np.mean(cL1(a1, a2, alpha=ALPHA)))


# ---------------------------------------------------------------- tests
def mwu3(benign, attack):
    """Two-sided, one-sided 'greater' (benign more similar), and the legacy
    scipy<=1.6 default (alternative=None): half the two-sided p.
    method='asymptotic' with continuity correction, as the legacy default."""
    b, a = np.asarray(benign), np.asarray(attack)
    two = mannwhitneyu(b, a, alternative="two-sided", method="asymptotic").pvalue
    gt = mannwhitneyu(b, a, alternative="greater", method="asymptotic").pvalue
    return dict(two_sided=float(two), greater=float(gt), legacy_half=float(two / 2.0),
                n_benign=int(len(b)), n_attack=int(len(a)),
                median_benign=float(np.median(b)), median_attack=float(np.median(a)))


def dump(obj, path):
    with open(path, "w") as f:
        json.dump(obj, f, indent=1, sort_keys=True, default=float)
