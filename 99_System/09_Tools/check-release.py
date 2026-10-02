#!/usr/bin/env python3
"""MDSE release consistency check (W-320).

Run from anywhere:  python3 99_System/09_Tools/check-release.py [--workbench PATH]
Needs PyYAML (pip install pyyaml). Exit code 1 if any FAIL.
Checks: schema versions vs manifest; registered documents exist and carry the right banner;
every doc in 10_Docs is registered; Translator Definition 'Current through' matches the Decision Log;
entry docs state the release and schema versions; optional Workbench fixtures/version sync.
"""
import argparse, os, re, sys
try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
fails, warns = [], []
def fail(m): fails.append(m); print("FAIL", m)
def warn(m): warns.append(m); print("WARN", m)
def ok(m): print("ok  ", m)
def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f: return f.read()

man = yaml.safe_load(read("99_System/03_Schemas/mdse-release.yaml"))

# 1. schema versions
for key, path in (("relationships", "relationships.yaml"), ("elementTypes", "element-types.yaml"), ("localModel", "local-model.yaml")):
    m = re.search(r"^schemaVersion:\s*['\"]?([0-9.]+)", read("99_System/03_Schemas/" + path), re.M)
    got = m.group(1) if m else None
    (ok if got == man["schemas"][key] else fail)(f"{path} schemaVersion {got} vs manifest {man['schemas'][key]}")

# 2. documents exist, banners
BANNER = re.compile(r"^> \[!(WARNING|NOTE)\].*$", re.M)
KEYWORD = re.compile(r"(SUPERSEDED|HISTORICAL|ARCHIVED|RETIRED)", re.I)
registered = set()
for d in man["documents"]:
    p, st = d["path"], d["status"]
    registered.add(p)
    if not os.path.exists(os.path.join(ROOT, p)):
        fail(f"registered file missing: {p}"); continue
    if st in ("historical", "superseded", "retired"):
        txt = read(p)
        callouts = []
        for m in BANNER.finditer(txt):
            nxt = txt[m.end():m.end() + 600]
            block = m.group(0) + nxt.split("\n\n")[0]
            callouts.append(block)
        target = os.path.splitext(os.path.basename(d.get("supersededBy", "")))[0]
        good = any(KEYWORD.search(c) and target and target in c for c in callouts)
        (ok if good else fail)(f"banner naming '{target}' in {os.path.basename(p)} ({st})")
    elif st == "current":
        head = read(p)[:600]
        if re.search(r"^> \[!WARNING\].*SUPERSEDED", head, re.M): fail(f"current file has a SUPERSEDED banner: {p}")

# 3. every doc in 10_Docs registered
for f in sorted(os.listdir(os.path.join(ROOT, "99_System/10_Docs"))):
    if f.endswith(".md") and not f.startswith("00 - Views") and not f.startswith("00 - Folder"):
        p = "99_System/10_Docs/" + f
        (ok if p in registered else fail)(f"10_Docs file registered: {f}")

# 4. Translator Definition vs decision log
log = read("99_System/10_Docs/Workspace Decision Log.md")
latest = max(int(n) for n in re.findall(r"^\*\*W-(\d+)\b", log, re.M))
m = re.search(r"Current through W-(\d+)", read("99_System/10_Docs/Translator Definition.md"))
(ok if m and int(m.group(1)) == latest else fail)(f"Translator Definition current through W-{m.group(1) if m else '?'}; Decision Log latest W-{latest}")

# 5. entry docs state release + versions
for p in ("README.md", "99_System/10_Docs/00 - Current State.md"):
    t = read(p)
    for v in (man["mdseRelease"], man["schemas"]["relationships"], man["schemas"]["elementTypes"], man["schemas"]["localModel"]):
        (ok if v in t else fail)(f"{os.path.basename(p)} mentions {v}")
t = read("99_System/10_Docs/00 - Current State.md")
(ok if f"W-{latest}" in t else fail)(f"Current State mentions W-{latest}")

# 6. plugin lock and tool warnings
lock = read(".obsidian/plugin-lock.yaml")
if "mdse-workbench" not in lock: warn("plugin-lock.yaml does not pin mdse-workbench (needed before the clean base is issued)")
if man["tools"]["bootstrap"]["sourceAvailable"] is False: warn("mdse-bootstrap has no retrievable source")
if man["tools"]["importer"]["release"] is None: warn("no release-conformant importer yet (v0.8.0 not built)")
if man["tools"]["cleanBase"]["repo"] is None: warn("clean 0.8.0 base vault not built yet")
for k in ("planned", "acceptedFallback", "evidenceOnly"):
    p = man["tools"]["importer"][k]
    if k != "planned" and not os.path.exists(os.path.join(ROOT, p)): fail(f"importer file missing: {p}")

# 7. optional workbench sync
ap = argparse.ArgumentParser(); ap.add_argument("--workbench"); a = ap.parse_args()
if a.workbench:
    norm = lambda s: s.replace("\r\n", "\n").rstrip() + "\n"
    for f in ("relationships.yaml", "element-types.yaml"):
        auth = norm(read("99_System/03_Schemas/" + f))
        with open(os.path.join(a.workbench, "test/fixtures", f), encoding="utf-8") as fh: fx = norm(fh.read())
        (ok if auth == fx else fail)(f"Workbench fixture {f} equals authority")
    import json
    pv = json.load(open(os.path.join(a.workbench, "package.json")))["version"]
    mv = json.load(open(os.path.join(a.workbench, "manifest.json")))["version"]
    (ok if pv == mv == man["tools"]["workbench"]["version"] else fail)(f"Workbench package {pv}, manifest {mv}, release manifest {man['tools']['workbench']['version']}")

print(f"\n{len(fails)} fail, {len(warns)} warn")
sys.exit(1 if fails else 0)
