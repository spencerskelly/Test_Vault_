#!/usr/bin/env python3
"""STEP-03W: audit UID candidate reservations and propose unique note filenames.

Read-only existing vault; no note moves, UID changes or native emission.
"""
import argparse,json,re
from pathlib import Path
from collections import Counter

UID=re.compile(r"^[0-9]{17}[a-z-]{13}$")
TOKEN=re.compile(r"(?<![a-z0-9])(?:part-|ep-|conn-|flow-)([0-9]{17}[a-z-]{13})(?![a-z0-9])")
def rows(path):
    return [json.loads(x) for x in Path(path).read_text(encoding="utf-8").splitlines() if x.strip()]
def audit(ledger,crosswalk,reference_vault,output):
    dest=Path(output)
    if dest.exists():raise ValueError("Output already exists")
    base=Path(reference_vault)
    if not base.is_dir():raise ValueError("Reference vault missing")
    allocations=rows(ledger);source=rows(crosswalk)
    by_oid={r["eaObjectID"]:r for r in source}
    if len(source)!=len(by_oid):raise ValueError("Duplicate source identities")
    seen=set();seen_uid=set();reserved=set();existing_basenames=set()
    for file in base.rglob("*.md"):
        existing_basenames.add(file.stem.casefold())
        content=file.read_text(encoding="utf-8",errors="replace")
        match=re.search(r"(?m)^uid:\s*['\"]?([0-9]{17}[a-z-]{13})",content)
        if match:reserved.add(match.group(1))
        reserved.update(TOKEN.findall(content))
    for file in base.rglob("*.base"):
        reserved.update(TOKEN.findall(file.read_text(encoding="utf-8",errors="replace")))
    outcomes=Counter();planned=[];names=set()
    for item in allocations:
        oid=item["eaObjectID"];uid=item.get("uid")
        if oid in seen or oid not in by_oid:raise ValueError("Duplicate/unmatched object ID")
        if item.get("eaGUID")!=by_oid[oid].get("eaGUID"):raise ValueError("Source GUID mismatch")
        seen.add(oid)
        if uid is None:
            planned.append({"eaObjectID":oid,"eaGUID":item["eaGUID"],"status":item["migrationStatus"],
                            "uid":None,"proposedFilename":None})
            outcomes["held"]+=1
            continue
        if not UID.fullmatch(uid):raise ValueError("Invalid UID syntax")
        if uid in seen_uid:raise ValueError("Duplicate candidate UID")
        seen_uid.add(uid)
        if uid in reserved:
            status="uid_collision_review";outcomes[status]+=1
        else:
            status="uid_candidate_available";outcomes[status]+=1
        # EA-<ID> remains stable placeholder. Human names require EA Name/Alias from QEAX,
        # destination-folder decisions, and global occupied filename scan.
        planned.append({"eaObjectID":oid,"eaGUID":item["eaGUID"],"uid":uid,"status":status,
                        "proposedFilename":None,"filenamePendingReason":"EA_NAME_AND_GOVERNED_FOLDER_NOT_RESOLVED"})
    if seen!=set(by_oid):raise ValueError("Crosswalk identity parity failure")
    dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open("x",encoding="utf-8") as f:
        for x in planned:f.write(json.dumps(x,ensure_ascii=False)+"\n")
    return {"identities":len(planned),"existing_reserved_uid_tokens":len(reserved),
            "existing_reserved_filenames":len(existing_basenames),
            "statuses":dict(sorted(outcomes.items())),"files_moved":0,"diagram_imported":False}
if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("uid_ledger","identity_crosswalk","reference_vault","output"):p.add_argument(name)
    a=p.parse_args()
    print(json.dumps(audit(a.uid_ledger,a.identity_crosswalk,a.reference_vault,a.output),indent=2))
