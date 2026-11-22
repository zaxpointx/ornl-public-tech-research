"""Diagnostic for the A3 (per-pair element set) direction: does similarity
track the size of the pair's element set, and does a file's capture length
track its similarity to benign files? Independent rebuild, not ORNL code.
Usage: python -I diag_pairN.py <work> <a3.json> <r0.json> <out.json>"""
import itertools
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np  # noqa: E402
from scipy.stats import spearmanr  # noqa: E402
import scs  # noqa: E402
from run_r0 import build  # noqa: E402

work, a3p, r0p, out = sys.argv[1:5]
scs.install_guards()
a3, r0 = json.load(open(a3p)), json.load(open(r0p))
benign, attacks = a3["benign"], a3["attacks"]
names = benign + attacks
_, nc, _, info = build(work, names)
S3 = np.array(a3["A3_pairwise_ward"]["S"])
Sg = np.array(r0["primary"]["linkages"]["ward"]["S"])
idx = {n: i for i, n in enumerate(names)}
rows = []
for x, y in list(itertools.combinations(benign, 2)) + [(a, b) for a in attacks for b in benign]:
    rows.append(dict(a=x, b=y, kind="bb" if x in benign else "ab", N=len(nc[x] & nc[y]),
                     sim_pairwise=float(S3[idx[x], idx[y]]), sim_global=float(Sg[idx[x], idx[y]]),
                     min_grid=min(info[x]["n_grid"], info[y]["n_grid"])))
N = np.array([r["N"] for r in rows]); s = np.array([r["sim_pairwise"] for r in rows])
bb = np.array([r["kind"] == "bb" for r in rows])
res = dict(
    spearman_N_vs_sim_pairwise_all=spearmanr(N, s)._asdict(),
    spearman_N_vs_sim_pairwise_benign_pairs=spearmanr(N[bb], s[bb])._asdict(),
    median_N_benign_pairs=float(np.median(N[bb])), median_N_attack_benign_pairs=float(np.median(N[~bb])),
    spearman_mingrid_vs_sim_global_all=spearmanr([r["min_grid"] for r in rows], [r["sim_global"] for r in rows])._asdict(),
    per_file=[dict(file=n, n_grid=info[n]["n_grid"], n_nonconstant=len(nc[n]),
                   median_sim_to_benign_global=float(np.median([Sg[idx[n], idx[b]] for b in benign if b != n])),
                   median_sim_to_benign_pairwise=float(np.median([S3[idx[n], idx[b]] for b in benign if b != n])))
              for n in names],
    pairs=rows)
f = res["per_file"]
res["spearman_file_nonconstant_vs_median_sim_pairwise"] = spearmanr([r["n_nonconstant"] for r in f], [r["median_sim_to_benign_pairwise"] for r in f])._asdict()
res["spearman_file_ngrid_vs_median_sim_global"] = spearmanr([r["n_grid"] for r in f], [r["median_sim_to_benign_global"] for r in f])._asdict()
scs.dump(res, out)
print({k: v for k, v in res.items() if k not in ("pairs", "per_file")})
