#!/usr/bin/env python3
"""Select an auditable QEAX slice for V2 mapping, without fabricating native SysML."""
import argparse,hashlib,json,sqlite3,pathlib,sys
def collect(source,limit=20):
    p=pathlib.Path(source).resolve()
    if not p.is_file():raise ValueError("SOURCE_NOT_FOUND")
    if not 1<=limit<=100:raise ValueError("LIMIT_OUT_OF_RANGE")
    with sqlite3.connect(p.as_uri()+"?mode=ro",uri=True) as db:
        db.row_factory=sqlite3.Row
        cols={r["name"] for r in db.execute("PRAGMA table_info(t_object)")}
        needed={"Object_ID","Object_Type","Name","ea_guid"}
        if not needed.issubset(cols):raise ValueError("UNSUPPORTED_OBJECT_SCHEMA")
        rows=db.execute("SELECT Object_ID,Object_Type,Name,ea_guid FROM t_object ORDER BY Object_ID LIMIT ?",(limit,)).fetchall()
        ids={x["Object_ID"] for x in rows}
        concols={r["name"] for r in db.execute("PRAGMA table_info(t_connector)")}
        if not {"Connector_ID","Start_Object_ID","End_Object_ID"}.issubset(concols):raise ValueError("UNSUPPORTED_CONNECTOR_SCHEMA")
        connections=db.execute("SELECT Connector_ID,Start_Object_ID,End_Object_ID FROM t_connector ORDER BY Connector_ID").fetchall()
    internal=sum(x["Start_Object_ID"] in ids and x["End_Object_ID"] in ids for x in connections)
    boundary=sum((x["Start_Object_ID"] in ids)!=(x["End_Object_ID"] in ids) for x in connections)
    # Only aggregate diagnostics printed; original identities and names are never exported here.
    return {"schema":"mdse-v2-qeax-slice-review/1","source_sha256":hashlib.sha256(p.read_bytes()).hexdigest(),
        "selected_elements":len(rows),"source_connector_count":len(connections),
        "internal_connectors_review_required":internal,"boundary_connectors_review_required":boundary,
        "native_declarations_emitted":0,"native_relationships_emitted":0,
        "disposition":"SOURCE_EVIDENCE_ONLY"}
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("qeax");ap.add_argument("--limit",type=int,default=20)
    args=ap.parse_args()
    try:print(json.dumps(collect(args.qeax,args.limit),indent=2))
    except (ValueError,OSError,sqlite3.DatabaseError) as ex:
        print(json.dumps({"status":"BLOCKED","error":str(ex)}),file=sys.stderr);sys.exit(1)
