"""Verify the reader's claim that 17 of the 29 CSVs in
signal_extractions/ambient/ are byte-identical copies of attack CSVs and that
the 12 others are exactly the keys of ambient/metadata.json.
Usage: python -I check_dups.py <signal_extractions dir> <out.json>"""
import hashlib
import json
import os
import sys

root, out = sys.argv[1], sys.argv[2]


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


amb = {f: sha(os.path.join(root, "ambient", f)) for f in sorted(os.listdir(os.path.join(root, "ambient"))) if f.endswith(".csv")}
att = {f: sha(os.path.join(root, "attacks", f)) for f in sorted(os.listdir(os.path.join(root, "attacks"))) if f.endswith(".csv")}
meta = sorted(json.load(open(os.path.join(root, "ambient", "metadata.json"))))
att_hashes = {h: f for f, h in att.items()}
copies = {f: att_hashes[h] for f, h in amb.items() if h in att_hashes}
benign = sorted(f[:-4] for f in amb if f not in copies)
res = dict(n_ambient_csv=len(amb), n_attack_csv=len(att), n_ambient_identical_to_attack=len(copies),
           copies_same_name=all(a == b for a, b in copies.items()),
           benign_by_hash=benign, metadata_keys=meta, benign_equals_metadata=benign == meta,
           sha256_ambient=amb, sha256_attacks=att)
json.dump(res, open(out, "w"), indent=1)
print({k: v for k, v in res.items() if not k.startswith("sha256")})
