"""Q1-Q3 for the independent rebuild (not ORNL code) of OSTI 1866690.
Usage:
  python -I run_q.py q1 <work> <signal_extractions> <out.json> --r0 r0.json --sens sens.json --a3 a3.json
  python -I run_q.py q2 <work> <signal_extractions> <out.json> --mode global|pairwise --reps N [--seed S]
  python -I run_q.py q3 <work> <signal_extractions> <out.json> --mode global|pairwise
Element-set modes: 'global' = intersection of non-constant signals over every
file in that test (pre-registered main choice); 'pairwise' = intersection of
the two files of each pair (A3)."""
import argparse
import itertools
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402
import scs  # noqa: E402
from run_r0 import CATS, cat_of, per_file, table2  # noqa: E402

TARGET = {"correlated_signal": 0x6E0, "max_speedometer": 0xD0, "max_engine_coolant_temp": 0x4E7,
          "reverse_light_on": 0xD0, "reverse_light_off": 0xD0}
LONG_MIN_S = 300.0  # benign captures used as crop parents (Q2b)


class Items:
    """name -> resampled DataFrame and non-constant set, for whole files,
    segments of files, and files with IDs excluded."""

    def __init__(self, work):
        self.work, self.cache, self.dfs, self.nc, self.info = work, {}, {}, {}, {}

    def parsed(self, src):
        if src not in self.cache:
            if len(self.cache) > 3:
                self.cache.pop(next(iter(self.cache)))
            self.cache[src] = scs.load_npz(os.path.join(self.work, src + ".npz"))
        return self.cache[src]

    def add(self, name, src, t0=None, t1=None, exclude=()):
        grid, df = scs.resample(self.parsed(src), t0=t0, t1=t1, exclude_ids=exclude)
        self.dfs[name] = df
        self.nc[name] = set(scs.nonconstant(df))
        self.info[name] = dict(src=src, t0=t0, t1=t1, exclude=list(exclude), grid_start=float(grid[0]),
                               grid_end=float(grid[-1]), n_grid=int(len(grid)), n_nonconstant=len(self.nc[name]))


PAIR_CACHE = {}


def sig(items, n):
    i = items.info[n]
    return (i["src"], i["t0"], i["t1"], tuple(i["exclude"]))


def sims(items, names, pairs, mode, method="ward"):
    """Return dict {(a, b): similarity} for the requested pairs. In pairwise
    mode, a pair's similarity depends only on the two items, so it is cached
    by item signature (src, t0, t1, excluded IDs) within one run."""
    out, meta = {}, {}
    if mode == "global":
        el = sorted(set.intersection(*(items.nc[n] for n in names)), key=scs.sort_key)
        aff = {n: scs.affinity(scs.link(scs.corr_matrix(items.dfs[n], el), method))[0] for n in names}
        for a, b in pairs:
            out[(a, b)] = scs.sim_from_aff(aff[a], aff[b])
        meta = dict(N=len(el), elements=el)
    else:
        ns = []
        for k, (a, b) in enumerate(pairs):
            el = sorted(items.nc[a] & items.nc[b], key=scs.sort_key)
            ns.append(len(el))
            key = frozenset([sig(items, a), sig(items, b)])
            if key in PAIR_CACHE:
                out[(a, b)] = PAIR_CACHE[key]
                continue
            aa = scs.affinity(scs.link(scs.corr_matrix(items.dfs[a], el), method))[0]
            ab = scs.affinity(scs.link(scs.corr_matrix(items.dfs[b], el), method))[0]
            out[(a, b)] = PAIR_CACHE[key] = scs.sim_from_aff(aa, ab)
        meta = dict(N_min=min(ns), N_median=float(np.median(ns)), N_max=max(ns))
    return out, meta


def to_matrix(s, names):
    idx = {n: i for i, n in enumerate(names)}
    S = np.full((len(names), len(names)), np.nan)
    np.fill_diagonal(S, 1.0)
    for (a, b), v in s.items():
        S[idx[a], idx[b]] = S[idx[b], idx[a]] = v
    return S


def table2_like(items, benign, tests, mode):
    """benign baseline = all benign pairs; each test name vs all benign.
    Returns category and per-file MWU results plus the matrix."""
    names = benign + tests
    pairs = list(itertools.combinations(benign, 2)) + [(t, b) for t in tests for b in benign]
    s, meta = sims(items, names, pairs, mode)
    S = to_matrix(s, names)
    return dict(meta=meta, table2=table2(S, names, benign, tests), per_file=per_file(S, names, benign, tests),
                S=np.nan_to_num(S, nan=-1).round(6).tolist())


# ------------------------------------------------------------------ Q1
def q1(a):
    res = {}
    for label, path, key in (("primary_global", a.r0, "primary"), ("A2_min_hz_9_5", a.sens, "A2_min_hz_9_5"),
                             ("A4_one_minus_r", a.sens, "A4_one_minus_r"), ("A3_pairwise", a.a3, "A3_pairwise_ward")):
        r = json.load(open(path))
        benign, attacks = r["benign"], r["attacks"]
        block = r[key] if key == "A3_pairwise_ward" else r[key]["linkages"]["ward"]
        S = np.array(block["S"], dtype=float)
        pf = per_file(S, benign + attacks, benign, attacks)
        res[label] = dict(per_file=pf, n_sig_greater=sum(v["greater"] < 0.05 for v in pf.values()),
                          n_sig_two_sided=sum(v["two_sided"] < 0.05 for v in pf.values()))
    return res


# ------------------------------------------------------------------ Q2
def q2(a, se):
    ameta = json.load(open(os.path.join(se, "attacks", "metadata.json")))
    bmeta = json.load(open(os.path.join(se, "ambient", "metadata.json")))
    benign = sorted(bmeta)
    attacks = sorted(k for k in ameta if k.endswith("_masquerade"))
    items = Items(a.work)
    for b in benign:
        items.add(b, b)
    res = dict(mode=a.mode, seed=a.seed, reps=a.reps, parts=a.parts)
    t0 = time.time()
    # full files and (a) pre-injection, (c) injection-only, in the same harness
    for tag, seg in (("full", lambda m: (None, None)), ("pre_injection", lambda m: (0.0, m["injection_interval"][0])),
                     ("injection_only", lambda m: tuple(m["injection_interval"]))):
        if tag not in a.parts:
            continue
        tests = []
        for x in attacks:
            n = f"{tag}:{x}"
            s0, s1 = seg(ameta[x])
            items.add(n, x, s0, s1)
            tests.append(n)
        r = table2_like(items, benign, tests, a.mode)
        r["segments"] = {n: items.info[n] for n in tests}
        res[tag] = r
        print(tag, round(time.time() - t0, 1), "s", {c: round(v["greater"], 4) for c, v in r["table2"].items()}, flush=True)
    # (b) benign crops matched in length to each attack file
    rng = np.random.default_rng(a.seed)
    parents = [b for b in benign if bmeta[b]["elapsed_sec"] >= LONG_MIN_S]
    res["crop_parents"] = parents
    reps = []
    for rep in range(a.reps if "crops" in a.parts else 0):
        crops, parent_of = [], {}
        for x in attacks:
            L = ameta[x]["elapsed_sec"]
            p = parents[rng.integers(len(parents))]
            gi = items.info[p]
            start = float(rng.uniform(gi["grid_start"], gi["grid_end"] - L))
            n = f"crop{rep}:{x}"
            items.add(n, p, start, start + L)
            crops.append(n)
            parent_of[n] = p
        # one element set per replicate (global mode) over benign + its crops
        names = benign + crops
        pairs = list(itertools.combinations(benign, 2)) + [(c, b) for c in crops for b in benign if b != parent_of[c]]
        s, meta = sims(items, names, pairs, a.mode)
        cat_res, file_res = {}, {}
        for cat in CATS:
            cc = [c for c in crops if cat_of(c.split(":", 1)[1]) == cat]
            excl = {parent_of[c] for c in cc}
            keep = [b for b in benign if b not in excl]
            base = [s[(x, y)] for x, y in itertools.combinations(benign, 2) if x in keep and y in keep]
            samp = [s[(c, b)] for c in cc for b in keep]
            cat_res[cat] = dict(scs.mwu3(base, samp), parents=sorted(excl))
        for c in crops:
            keep = [b for b in benign if b != parent_of[c]]
            base = [s[(x, y)] for x, y in itertools.combinations(keep, 2)]
            file_res[c] = dict(scs.mwu3(base, [s[(c, b)] for b in keep]), parent=parent_of[c],
                               start=items.info[c]["t0"], n_grid=items.info[c]["n_grid"])
        reps.append(dict(meta={k: v for k, v in meta.items() if k != "elements"}, category=cat_res, per_crop=file_res))
        for c in crops:
            for d in (items.dfs, items.nc):
                d.pop(c)
        print("crop rep", rep, round(time.time() - t0, 1), "s", meta.get("N", meta.get("N_median")),
              {c: round(v["greater"], 3) for c, v in cat_res.items()}, flush=True)
    res["crops"] = reps
    pc = [v for r in reps for v in r["per_crop"].values()]
    res["crop_summary"] = dict(
        n_crops=len(pc),
        frac_per_crop_sig_greater=float(np.mean([v["greater"] < 0.05 for v in pc])) if pc else None,
        frac_per_crop_sig_two_sided=float(np.mean([v["two_sided"] < 0.05 for v in pc])) if pc else None,
        frac_category_sig_greater=float(np.mean([v["greater"] < 0.05 for r in reps for v in r["category"].values()])) if reps else None,
        reps_with_ge3_cats_sig_greater=int(sum(sum(v["greater"] < 0.05 for v in r["category"].values()) >= 3 for r in reps)))
    return res


# ------------------------------------------------------------------ Q3
def q3(a, se):
    ameta = json.load(open(os.path.join(se, "attacks", "metadata.json")))
    benign = sorted(json.load(open(os.path.join(se, "ambient", "metadata.json"))))
    attacks = sorted(k for k in ameta if k.endswith("_masquerade"))
    items = Items(a.work)
    res = dict(mode=a.mode)
    t0 = time.time()
    for tid in sorted(set(TARGET.values())):
        cats = [c for c in CATS if TARGET[c] == tid]
        files = [x for x in attacks if cat_of(x) in cats]
        variants = (("with_target", ()), ("without_target", (tid,)))
        if a.mode == "pairwise":  # with_target pairs are exactly A3 (a3.json); not recomputed
            variants = variants[1:]
        for tag, ex in variants:
            for n in benign + files:
                items.add(f"{tag}:{n}", n, exclude=ex)
            bn = [f"{tag}:{b}" for b in benign]
            tn = [f"{tag}:{x}" for x in files]
            r = table2_like(items, bn, tn, a.mode)
            r["table2"] = {c: v for c, v in r["table2"].items() if c in cats}
            r.pop("S")
            res[f"{hex(tid)}:{tag}"] = r
            for n in bn + tn:
                items.dfs.pop(n), items.nc.pop(n)
            print(hex(tid), tag, round(time.time() - t0, 1), "s", r["meta"].get("N", r["meta"].get("N_median")),
                  {c: round(v["greater"], 4) for c, v in r["table2"].items()}, flush=True)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("q")
    ap.add_argument("work")
    ap.add_argument("se")
    ap.add_argument("out")
    ap.add_argument("--mode", default="global", choices=["global", "pairwise"])
    ap.add_argument("--reps", type=int, default=20)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--parts", default="full,pre_injection,injection_only,crops")
    ap.add_argument("--r0")
    ap.add_argument("--sens")
    ap.add_argument("--a3")
    a = ap.parse_args()
    a.parts = a.parts.split(",")
    guard = scs.install_guards()
    t0 = time.time()
    res = {"q1": lambda: q1(a), "q2": lambda: q2(a, a.se), "q3": lambda: q3(a, a.se)}[a.q]()
    res.update(guard=guard, wall_s=round(time.time() - t0, 1), peak_rss_bytes=scs.peak_rss(), argv=sys.argv)
    scs.dump(res, a.out)


if __name__ == "__main__":
    main()
