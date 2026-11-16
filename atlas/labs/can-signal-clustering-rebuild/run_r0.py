"""R0: Table II and Table III of OSTI 1866690, independent rebuild (not ORNL
code), plus sensitivity variants A2 (drop IDs < 9.5 Hz), A3 (per-pair element
set, Ward) and A4 (condensed distance 2(1-r)).
Usage: python -I run_r0.py <work dir> <prep_stats.json> <out.json> [--sensitivity | --a3]"""
import itertools
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402
import scs  # noqa: E402

LINKAGES = ["single", "complete", "average", "ward"]
CATS = ["correlated_signal", "max_speedometer", "max_engine_coolant_temp", "reverse_light_on", "reverse_light_off"]
PAPER_T2 = {  # p.5 Table II
    "correlated_signal": dict(single=0.005, complete=0.002, average=0.123, ward=0.000),
    "max_speedometer": dict(single=0.003, complete=0.017, average=0.007, ward=0.000),
    "max_engine_coolant_temp": dict(single=0.251, complete=0.065, average=0.006, ward=0.008),
    "reverse_light_on": dict(single=0.378, complete=0.007, average=0.057, ward=0.004),
    "reverse_light_off": dict(single=0.039, complete=0.004, average=0.004, ward=0.000),
}
PAPER_T3_TP = dict(correlated_signal=220, max_speedometer=220, max_engine_coolant_temp=204,
                   reverse_light_on=205, reverse_light_off=220)
CONV = ["two_sided", "greater", "legacy_half"]


def cat_of(name):
    name = name.split(":")[-1]  # strip run_q tags such as "pre_injection:"
    for c in CATS:
        if name.startswith(c):
            return c
    raise KeyError(name)


def build(work, names, segments=None, min_hz=None, exclude=None):
    """Resample each file (optionally a [t0, t1] segment from another file),
    return dfs, per-file non-constant sets, global sorted intersection."""
    dfs, nc, info = {}, {}, {}
    cache = {}
    for n in names:
        src, t0, t1 = (segments or {}).get(n, (n, None, None))
        if src not in cache:
            cache = {src: scs.load_npz(os.path.join(work, src + ".npz"))}
        parsed = cache[src]
        ex = (exclude or {}).get(n, ())
        grid, df = scs.resample(parsed, t0=t0, t1=t1, min_hz=min_hz, exclude_ids=ex)
        dfs[n] = df
        nc[n] = set(scs.nonconstant(df))
        info[n] = dict(grid_start=float(grid[0]), grid_end=float(grid[-1]), n_grid=int(len(grid)),
                       n_signals=int(df.shape[1]), n_nonconstant=len(nc[n]),
                       sporadic_dropped=scs.sporadic_ids(parsed))
    elements = sorted(set.intersection(*nc.values()), key=scs.sort_key)
    return dfs, nc, elements, info


def sim_matrix(dfs, names, elements, method, distance="rows"):
    affs = {}
    for n in names:
        c = scs.corr_matrix(dfs[n], elements)
        affs[n], _ = scs.affinity(scs.link(c, method, distance))
    k = len(names)
    S = np.eye(k)
    for i, j in itertools.combinations(range(k), 2):
        S[i, j] = S[j, i] = scs.sim_from_aff(affs[names[i]], affs[names[j]])
    return S


def table2(S, names, benign, attacks):
    idx = {n: i for i, n in enumerate(names)}
    b = [idx[x] for x in benign]
    bb = [S[i, j] for i, j in itertools.combinations(b, 2)]
    out = {}
    for c in CATS:
        a = [idx[x] for x in attacks if cat_of(x) == c]
        if not a:  # Q3 tests one target ID's categories at a time
            continue
        ab = [S[i, j] for i in a for j in b]
        out[c] = scs.mwu3(bb, ab)
    return out


def per_file(S, names, benign, attacks):
    idx = {n: i for i, n in enumerate(names)}
    b = [idx[x] for x in benign]
    bb = [S[i, j] for i, j in itertools.combinations(b, 2)]
    return {x: scs.mwu3(bb, [S[idx[x], j] for j in b]) for x in attacks}


def table3(S, names, benign, attacks, alpha=0.05):
    idx = {n: i for i, n in enumerate(names)}
    folds = list(itertools.combinations(range(len(benign)), 9))
    res = {cv: dict(group=dict(FP=0, TN=0, TP={c: 0 for c in CATS}),
                    perfile=dict(FP=0, TN=0, TP={c: 0 for c in CATS}),
                    file_fp_group={x: 0 for x in benign}, file_fp_perfile={x: 0 for x in benign})
           for cv in CONV}
    for tr in folds:
        trn = [idx[benign[i]] for i in tr]
        held = [benign[i] for i in range(len(benign)) if i not in tr]
        base = [S[i, j] for i, j in itertools.combinations(trn, 2)]
        g = scs.mwu3(base, [S[idx[h], j] for h in held for j in trn])
        pf = {h: scs.mwu3(base, [S[idx[h], j] for j in trn]) for h in held}
        att = {c: scs.mwu3(base, [S[idx[x], j] for x in attacks if cat_of(x) == c for j in trn]) for c in CATS}
        attpf = {x: scs.mwu3(base, [S[idx[x], j] for j in trn]) for x in attacks}
        for cv in CONV:
            r = res[cv]
            if g[cv] < alpha:
                r["group"]["FP"] += 1
                for h in held:
                    r["file_fp_group"][h] += 1
            else:
                r["group"]["TN"] += 1
            for h in held:
                if pf[h][cv] < alpha:
                    r["perfile"]["FP"] += 1
                    r["file_fp_perfile"][h] += 1
                else:
                    r["perfile"]["TN"] += 1
            for c in CATS:
                r["group"]["TP"][c] += int(att[c][cv] < alpha)
            for x in attacks:
                r["perfile"]["TP"][cat_of(x)] += int(attpf[x][cv] < alpha)
    nf = len(folds)
    for cv in CONV:
        for mode, ntest_b in (("group", nf), ("perfile", 3 * nf)):
            r = res[cv][mode]
            r["FPR"] = r["FP"] / ntest_b
            r["metrics"] = {}
            for c in CATS:
                npos = nf * (1 if mode == "group" else sum(cat_of(x) == c for x in attacks))
                tp = r["TP"][c]
                prec = tp / (tp + r["FP"]) if tp + r["FP"] else float("nan")
                rec = tp / npos
                f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
                r["metrics"][c] = dict(TP=tp, FN=npos - tp, precision=prec, recall=rec, f1=f1)
        res[cv]["file_fpr_group"] = {x: v / 55 for x, v in res[cv]["file_fp_group"].items()}
        res[cv]["file_fpr_perfile"] = {x: v / 55 for x, v in res[cv]["file_fp_perfile"].items()}
    res["n_folds"] = nf
    return res


def fig3(S, names, benign):
    from scipy.cluster.hierarchy import fcluster, linkage
    Z = linkage(S, method="ward")
    lab = fcluster(Z, 4, criterion="maxclust")
    groups = {}
    for n, l in zip(names, lab):
        groups.setdefault(int(l), []).append(n)
    return dict(clusters=groups,
                benign_cluster_ids=sorted({int(l) for n, l in zip(names, lab) if n in benign}))


def target_survival(elements, nc):
    tgt = {"0x6e0 (1760) all": [f"1760_{k}" for k in range(1, 5)],
           "0xd0 (208) Signal_6 = byte 5 (max speedometer)": ["208_6"],
           "0xd0 (208) Signal_3 = byte 2 bit 3 (reverse light)": ["208_3"],
           "0x4e7 (1255) Signal_2 = byte 5 (coolant)": ["1255_2"]}
    out = {}
    for k, sigs in tgt.items():
        out[k] = {s: dict(in_global=s in elements,
                          constant_in=sorted(n for n, v in nc.items() if s not in v)) for s in sigs}
    out["all_target_id_signals_in_global"] = [e for e in elements if e.split("_")[0] in ("208", "1760", "1255")]
    return out


def run_variant(work, benign, attacks, method_list, distance="rows", min_hz=None, label=""):
    names = benign + attacks
    t0 = time.time()
    dfs, nc, elements, info = build(work, names, min_hz=min_hz)
    out = dict(N=len(elements), elements=elements, file_info=info, linkages={})
    print(label, "N", len(elements), "build", round(time.time() - t0, 1), "s", flush=True)
    for m in method_list:
        t1 = time.time()
        S = sim_matrix(dfs, names, elements, m, distance)
        o = dict(table2=table2(S, names, benign, attacks), S=S.round(6).tolist())
        if m == "ward":
            o["table3"] = table3(S, names, benign, attacks)
            o["per_file"] = per_file(S, names, benign, attacks)
            o["fig3"] = fig3(S, names, benign)
        o["seconds"] = round(time.time() - t1, 1)
        out["linkages"][m] = o
        print(label, m, o["seconds"], "s", {c: round(o["table2"][c]["two_sided"], 4) for c in CATS}, flush=True)
    return out, dfs, nc, elements


def pairwise_intersection_ward(work, benign, attacks):
    """A3: element set = intersection of the two files' non-constant sets."""
    names = benign + attacks
    dfs, nc, _, _ = build(work, names)
    idx = {n: i for i, n in enumerate(names)}
    S = np.full((len(names), len(names)), np.nan)
    np.fill_diagonal(S, 1.0)
    pairs = list(itertools.combinations(benign, 2)) + [(a, b) for a in attacks for b in benign]
    sizes = []
    for x, y in pairs:
        el = sorted(nc[x] & nc[y], key=scs.sort_key)
        sizes.append(len(el))
        ax, _ = scs.affinity(scs.link(scs.corr_matrix(dfs[x], el), "ward"))
        ay, _ = scs.affinity(scs.link(scs.corr_matrix(dfs[y], el), "ward"))
        S[idx[x], idx[y]] = S[idx[y], idx[x]] = scs.sim_from_aff(ax, ay)
    return dict(table2=table2(S, names, benign, attacks), table3=table3(S, names, benign, attacks),
                pair_N_min=min(sizes), pair_N_max=max(sizes), pair_N_median=float(np.median(sizes)),
                S=np.nan_to_num(S, nan=-1).round(6).tolist())


def clusim_equiv(dfs, elements, names):
    import clusim.sim as csim
    rows = []
    for x, y in [(names[0], names[1]), (names[0], names[-1]), (names[5], names[15])]:
        Zx = scs.link(scs.corr_matrix(dfs[x], elements), "ward")
        Zy = scs.link(scs.corr_matrix(dfs[y], elements), "ward")
        ax, cx = scs.affinity(Zx)
        ay, cy = scs.affinity(Zy)
        rows.append(dict(pair=[x, y], cached=scs.sim_from_aff(ax, ay),
                         element_sim=float(csim.element_sim(cx, cy, alpha=scs.ALPHA, r=scs.R))))
    return rows


def main():
    work, stats_path, out_path = sys.argv[1:4]
    sens = "--sensitivity" in sys.argv
    a3 = "--a3" in sys.argv
    guard = scs.install_guards()
    stats = json.load(open(stats_path))
    benign, attacks = stats["benign"], stats["attacks"]
    t0 = time.time()
    res = dict(guard=guard, benign=benign, attacks=attacks, paper_table2=PAPER_T2, paper_table3_tp=PAPER_T3_TP)
    if a3:
        t1 = time.time()
        res["A3_pairwise_ward"] = pairwise_intersection_ward(work, benign, attacks)
        res["A3_pairwise_ward"]["seconds"] = round(time.time() - t1, 1)
        print("A3", res["A3_pairwise_ward"]["seconds"], "s", flush=True)
    elif not sens:
        out, dfs, nc, elements = run_variant(work, benign, attacks, LINKAGES, label="primary")
        out["target_survival"] = target_survival(elements, nc)
        out["clusim_equivalence"] = clusim_equiv(dfs, elements, benign + attacks)
        res["primary"] = out
    else:
        res["A2_min_hz_9_5"], *_ = run_variant(work, benign, attacks, LINKAGES, min_hz=9.5, label="A2")
        res["A4_one_minus_r"], *_ = run_variant(work, benign, attacks, LINKAGES, distance="one_minus_r", label="A4")
    res["wall_s"] = round(time.time() - t0, 1)
    res["peak_rss_bytes"] = scs.peak_rss()
    scs.dump(res, out_path)


if __name__ == "__main__":
    main()
