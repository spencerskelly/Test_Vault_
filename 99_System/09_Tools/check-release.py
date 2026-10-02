#!/usr/bin/env python3
"""MDSE release consistency check (W-320, W-321).

Usage:
  python3 99_System/09_Tools/check-release.py
      [--workbench PATH_TO_MDSE_WORKBENCH]
      [--base PATH_TO_GENERATED_BASE]

PyYAML is required. Exit code 1 on any FAIL.
"""
import argparse, json, os, re, sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
fails, warns = [], []

def fail(m): fails.append(m); print("FAIL", m)
def warn(m): warns.append(m); print("WARN", m)
def ok(m): print("ok  ", m)
def full(root, p): return os.path.join(root, *p.split("/"))
def read_at(root, p):
    with open(full(root, p), encoding="utf-8") as f:
        return f.read()
def read(p): return read_at(ROOT, p)
def norm(s): return s.replace("\r\n", "\n").rstrip() + "\n"
def files_under(root, rel):
    base=full(root, rel)
    out=[]
    if not os.path.isdir(base): return out
    for d, dirs, names in os.walk(base):
        dirs[:] = [x for x in dirs if x != ".git"]
        for n in names:
            ap=os.path.join(d,n)
            out.append(os.path.relpath(ap,root).replace(os.sep,"/"))
    return out

ap=argparse.ArgumentParser()
ap.add_argument("--workbench")
ap.add_argument("--base")
a=ap.parse_args()

man=yaml.safe_load(read("99_System/03_Schemas/mdse-release.yaml"))

schema_paths={"relationships":"relationships.yaml","elementTypes":"element-types.yaml","localModel":"local-model.yaml"}
for key, fn in schema_paths.items():
    m=re.search(r"^schemaVersion:\s*['\"]?([0-9.]+)", read("99_System/03_Schemas/"+fn), re.M)
    got=m.group(1) if m else None
    (ok if got==man["schemas"][key] else fail)(f"{fn} schemaVersion {got} vs manifest {man['schemas'][key]}")

BANNER=re.compile(r"^> \[!(WARNING|NOTE)\].*$",re.M)
KEYWORD=re.compile(r"(SUPERSEDED|HISTORICAL|ARCHIVED|RETIRED)",re.I)
registered=set()
for d in man["documents"]:
    p,st=d["path"],d["status"]; registered.add(p)
    if not os.path.exists(full(ROOT,p)):
        fail(f"registered file missing: {p}"); continue
    if st in ("historical","superseded","retired"):
        txt=read(p); callouts=[]
        for m in BANNER.finditer(txt):
            nxt=txt[m.end():m.end()+600]
            callouts.append(m.group(0)+nxt.split("\n\n")[0])
        target=os.path.splitext(os.path.basename(d.get("supersededBy","")))[0]
        good=any(KEYWORD.search(c) and target and target in c for c in callouts)
        (ok if good else fail)(f"banner naming '{target}' in {os.path.basename(p)} ({st})")
    elif st=="current":
        head=read(p)[:600]
        if re.search(r"^> \[!WARNING\].*SUPERSEDED",head,re.M):
            fail(f"current file has a SUPERSEDED banner: {p}")

for fn in sorted(os.listdir(full(ROOT,"99_System/10_Docs"))):
    if fn.endswith(".md") and not fn.startswith("00 - Views") and not fn.startswith("00 - Folder"):
        p="99_System/10_Docs/"+fn
        (ok if p in registered else fail)(f"10_Docs file registered: {fn}")

log=read("99_System/10_Docs/Workspace Decision Log.md")
latest=max(int(n) for n in re.findall(r"^\*\*W-(\d+)\b",log,re.M))
td=read("99_System/10_Docs/Translator Definition.md")
m=re.search(r"Current through W-(\d+)",td)
(ok if m and int(m.group(1))==latest else fail)(f"Translator Definition current through W-{m.group(1) if m else '?'}; Decision Log latest W-{latest}")

stale={
    "schemaVersion 1.16":"element-types 1.16",
    "current clean base repository is":"obsolete base presented as current",
    "An EA author that is blank or not usable is":"obsolete EA8647 author fallback",
    "the region begins with <!-- MDSE:LOCAL-MODEL START schema=0.1":"obsolete Local Model writer marker",
    "It is regenerated with the import evidence and is not model authority.":"obsolete Source Map authority wording",
}
for needle,label in stale.items():
    (fail if needle in td else ok)(f"Translator Definition has no {label}")

for p in ("README.md","99_System/10_Docs/00 - Current State.md"):
    t=read(p)
    for v in (man["mdseRelease"],man["schemas"]["relationships"],man["schemas"]["elementTypes"],man["schemas"]["localModel"]):
        (ok if v in t else fail)(f"{os.path.basename(p)} mentions {v}")
t=read("99_System/10_Docs/00 - Current State.md")
(ok if f"W-{latest}" in t else fail)(f"Current State mentions W-{latest}")

lock=read(".obsidian/plugin-lock.yaml")
enabled=read(".obsidian/community-plugins.json")
bootstrap=man["tools"]["bootstrap"]
if bootstrap["sourceAvailable"] is False:
    (fail if "mdse-bootstrap" in lock or "mdse-bootstrap" in enabled else ok)("unavailable mdse-bootstrap is absent from runtime plugin baseline")
wbid=man["tools"]["workbench"]["runtimePluginId"]
if wbid not in lock:
    (fail if man["releaseStatus"]=="release" and man["tools"]["workbench"]["requiredForRelease"] else warn)(
        "plugin-lock.yaml does not yet pin the WB-106-capable Workbench release")
if man["tools"]["importer"]["release"] is None:
    (fail if man["releaseStatus"]=="release" else warn)("no release-conformant importer yet")
if man["tools"]["cleanBase"]["repo"] is None:
    (fail if man["releaseStatus"]=="release" else warn)("clean 0.8.0 base repository not issued yet")
for k in ("acceptedFallback","evidenceOnly"):
    p=man["tools"]["importer"][k]
    if not os.path.exists(full(ROOT,p)): fail(f"importer file missing: {p}")

if a.workbench:
    wb=os.path.abspath(a.workbench)
    for fn in ("relationships.yaml","element-types.yaml","local-model.yaml"):
        auth=norm(read("99_System/03_Schemas/"+fn))
        fp=full(wb,"test/fixtures/"+fn)
        if not os.path.exists(fp):
            fail(f"Workbench fixture missing: {fn}")
        else:
            fx=norm(read_at(wb,"test/fixtures/"+fn))
            (ok if auth==fx else fail)(f"Workbench fixture {fn} equals authority")
    old=full(wb,"test/fixtures/local-model-0.1.yaml")
    if not os.path.exists(old):
        fail("Workbench historical Local Model 0.1 fixture missing")
    else:
        m=re.search(r'^schemaVersion:\s*["\']?([0-9.]+)',read_at(wb,"test/fixtures/local-model-0.1.yaml"),re.M)
        (ok if m and m.group(1)=="0.1" else fail)("Workbench historical Local Model fixture is schema 0.1")
    pv=json.load(open(full(wb,"package.json")))["version"]
    mv=json.load(open(full(wb,"manifest.json")))["version"]
    (ok if pv==mv==man["tools"]["workbench"]["version"] else fail)(
        f"Workbench package {pv}, manifest {mv}, release manifest {man['tools']['workbench']['version']}")

if a.base:
    base=os.path.abspath(a.base)
    vf=full(base,".vault.yaml")
    if not os.path.exists(vf):
        fail("base .vault.yaml missing")
    else:
        vt=read_at(base,".vault.yaml")
        rm=re.search(r'(?m)^mdse_release:\s*["\']?([^"\'#\r\n]+)',vt)
        vr=rm.group(1).strip() if rm else None
        (ok if vr==man["mdseRelease"] else fail)(f"base mdse_release {vr} vs manifest {man['mdseRelease']}")
        (ok if "UNINITIALIZED" in vt else fail)("clean base vault_uid is UNINITIALIZED")

    rb=man["runtimeBase"]
    expected=set(rb["includeFiles"])
    for tree in rb["includeTrees"]:
        expected.update(files_under(ROOT,tree))
    for p in rb.get("conditionalFiles",[]):
        if os.path.exists(full(ROOT,p)): expected.add(p)
        elif man["releaseStatus"]=="release": fail(f"release runtime file missing from authority: {p}")
        else: warn(f"pre-release runtime file not built yet: {p}")
    expected.update(rb["generatedFiles"])

    actual=set()
    for d,dirs,names in os.walk(base):
        dirs[:]=[x for x in dirs if x!=".git"]
        for n in names:
            actual.add(os.path.relpath(os.path.join(d,n),base).replace(os.sep,"/"))
    missing=sorted(expected-actual); extra=sorted(actual-expected)
    if missing: fail("base missing files: "+", ".join(missing[:20]))
    else: ok("base contains every required runtime file")
    if extra: fail("base has ungoverned extra files: "+", ".join(extra[:20]))
    else: ok("base contains no ungoverned extra files")

    for p in sorted(expected-set(rb["generatedFiles"])):
        if p in actual and os.path.exists(full(ROOT,p)):
            (ok if norm(read_at(base,p))==norm(read(p)) else fail)(f"base file equals authority: {p}")

    for p in rb.get("forbiddenPaths",[]):
        if os.path.exists(full(base,p)): fail(f"workspace-only path leaked into base: {p}")
    br=full(base,"README.md")
    if os.path.exists(br):
        txt=read_at(base,"README.md")
        (ok if "MDSE Base Vault" in txt and man["mdseRelease"] in txt else fail)("base README identifies release")
    block=read_at(base,".obsidian/plugin-lock.yaml") if os.path.exists(full(base,".obsidian/plugin-lock.yaml")) else ""
    if man["releaseStatus"]=="release" and wbid not in block:
        fail("issued base does not pin required Workbench")
    if bootstrap["sourceAvailable"] is False and "mdse-bootstrap" in block:
        fail("issued base contains unavailable Bootstrap")

print(f"\n{len(fails)} fail, {len(warns)} warn")
sys.exit(1 if fails else 0)
