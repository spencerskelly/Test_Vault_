#!/usr/bin/env python3
import hashlib
import sys
from pathlib import Path

if len(sys.argv) != 3:
    raise SystemExit("usage: compare_full_import_outputs.py OUTPUT_A OUTPUT_B")

a = Path(sys.argv[1]).resolve()
b = Path(sys.argv[2]).resolve()

VOLATILE = {
    "99_System/11_Import/Import State.json",
    "99_System/11_Import/Run Manifest.md",
}

def inventory(root):
    out = {}
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()
        if rel in VOLATILE:
            continue
        out[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out

ia, ib = inventory(a), inventory(b)
only_a = sorted(set(ia) - set(ib))
only_b = sorted(set(ib) - set(ia))
changed = sorted(k for k in set(ia) & set(ib) if ia[k] != ib[k])

print(f"determinism files A={len(ia)} B={len(ib)}")
print(f"onlyA={len(only_a)} onlyB={len(only_b)} changed={len(changed)}")
for label, items in (("onlyA", only_a), ("onlyB", only_b), ("changed", changed)):
    for item in items[:50]:
        print(label, item)

if only_a or only_b or changed:
    raise SystemExit("Deterministic rerun mismatch")

print("DETERMINISM PASS")
