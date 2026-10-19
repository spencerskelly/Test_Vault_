#!/usr/bin/env python3
"""STEP-03V: deterministic EA8647 note UID allocation for interim crosswalk.

Read-only QEAX; writes new private identity ledger; never renames notes.
"""
import argparse,datetime,json,re,sqlite3
from pathlib import Path

VALID=re.compile(r"^[0-9]{17}[a-z-]{13}$")
BASE=datetime.datetime(2026,9,11,0,0,0,1000)

def author_code(value):
    raw=str(value or "").strip().lower()
    if "," in raw:
        family,given=raw.split(",",1)
        s=re.sub("[^a-z]","",family+given)
    else:
        words=re.findall("[a-z]+",raw)
        s=(words[-1]+"".join(words[:-1])) if len(words)>1 else "".join(words)
    return (s or "skellyspencer")[:13].ljust(13,"-")

def seed_date(value):
    if value is None or not str(value).strip():return BASE
    value=str(value).strip()
    for fmt in ("%Y-%m-%d %H:%M:%S.%f","%Y-%m-%d %H:%M:%S","%Y-%m-%dT%H:%M:%S.%f","%Y-%m-%dT%H:%M:%S"):
        try:return datetime.datetime.strptime(value,fmt)
        except ValueError:pass
    raise ValueError("Unrecognized EA CreatedDate")

def allocate(qeax,crosswalk,out):
    source=Path(qeax).resolve();dest=Path(out).resolve()
    if dest.exists():raise ValueError("Output exists; preserve allocated identity map")
    db=sqlite3.connect(source.as_uri()+"?mode=ro",uri=True)
    try:
        cols={r[1] for r in db.execute("PRAGMA table_info(t_object)")}
        if not {"Object_ID","ea_guid","CreatedDate","Author"}<=cols:
            raise ValueError("QEAX creation/author provenance fields missing")
        obj={oid:(guid,created,author) for oid,guid,created,author in db.execute("SELECT Object_ID,ea_guid,CreatedDate,Author FROM t_object")}
    finally:db.close()
    source_rows=[json.loads(x) for x in Path(crosswalk).read_text(encoding="utf8").splitlines() if x.strip()]
    if not source_rows:raise ValueError("Empty crosswalk")
    if len({r["eaObjectID"] for r in source_rows})!=len(source_rows):
        raise ValueError("Duplicate source IDs")
    jobs=[];held=[]
    for row in source_rows:
        oid=row["eaObjectID"]
        if oid not in obj or obj[oid][0]!=row.get("eaGUID"):
            raise ValueError("Source identity mismatch")
        state=row["migrationStatus"]
        if state!="identity_and_placement_pending":
            held.append({"eaObjectID":oid,"eaGUID":obj[oid][0],"migrationStatus":state,"uid":None})
            continue
        guid,created,author=obj[oid]
        jobs.append((seed_date(created),str(guid),oid,author))
    used=set();assigned=[]
    for dt,guid,oid,author in sorted(jobs,key=lambda x:(x[0],x[1])):
        suffix=author_code(author)
        while True:
            candidate=dt.strftime("%Y%m%d%H%M%S")+f"{dt.microsecond//1000:03d}"+suffix
            if candidate not in used:break
            dt+=datetime.timedelta(milliseconds=1)
        if not VALID.fullmatch(candidate):raise ValueError("Invalid allocated UID")
        used.add(candidate)
        assigned.append({"eaObjectID":oid,"eaGUID":guid,"sourceKey":"EA8647:"+guid,
                         "uid":candidate,"migrationStatus":"uid_allocated_path_pending"})
    dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open("x",encoding="utf8") as f:
        for row in sorted(assigned+held,key=lambda x:x["eaObjectID"]):
            f.write(json.dumps(row,ensure_ascii=False)+"\n")
    return {"crosswalk_records":len(source_rows),"uids_allocated":len(assigned),
            "held_for_folder_or_boundary":len(held),"unique_uids":len(used),
            "paths_assigned":0,"files_moved":0,"diagram_processed":False}

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("qeax");p.add_argument("identity_crosswalk");p.add_argument("private_uid_ledger")
    a=p.parse_args()
    print(json.dumps(allocate(a.qeax,a.identity_crosswalk,a.private_uid_ledger),indent=2))
