#!/usr/bin/env python3
"""Read-only EA connector endpoint type audit. No semantic direction or SysML emission."""
import argparse, collections, json, pathlib, sqlite3

def inspect(path, limit=100):
    if not 1 <= limit <= 1000:
        raise ValueError("INVALID_LIMIT")
    p=pathlib.Path(path).resolve()
    if not p.is_file():
        raise ValueError("SOURCE_NOT_FOUND")
    counts=collections.Counter()
    with sqlite3.connect(p.as_uri()+"?mode=ro",uri=True) as db:
        if not {"Object_ID","Object_Type"}.issubset(x[1] for x in db.execute("PRAGMA table_info(t_object)")):
            raise ValueError("UNSUPPORTED_OBJECT_SCHEMA")
        if not {"Connector_ID","Connector_Type","Start_Object_ID","End_Object_ID"}.issubset(x[1] for x in db.execute("PRAGMA table_info(t_connector)")):
            raise ValueError("UNSUPPORTED_CONNECTOR_SCHEMA")
        objects=dict(db.execute("SELECT Object_ID,Object_Type FROM t_object"))
        rows=db.execute("SELECT Connector_Type,Start_Object_ID,End_Object_ID FROM t_connector ORDER BY Connector_ID LIMIT ?",(limit,)).fetchall()
    missing=0
    for kind,start,end in rows:
        if start not in objects or end not in objects:
            missing+=1
        else:
            counts[(kind or "",objects[start] or "",objects[end] or "")]+=1
    return {"schema":"mdse-v2-source-endpoint-types/1","source_connectors":len(rows),
            "missing_endpoints":missing,
            "source_direction":"EA Start_Object_ID to End_Object_ID; no SysML orientation inferred",
            "typed_pairs":[{"connector_type":k,"ea_start_type":s,"ea_end_type":e,"count":n}
                           for (k,s,e),n in sorted(counts.items())],
            "native_relationships_emitted":0,"source_modified":False}

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("qeax");ap.add_argument("--limit",type=int,default=100)
    a=ap.parse_args()
    print(json.dumps(inspect(a.qeax,a.limit),indent=2))
