#!/usr/bin/env python3
"""Profile a local Sparx QEAX read-only; do not commit the output JSON or source model."""
import argparse, collections, hashlib, json, pathlib, sqlite3

TABLES=("t_object","t_connector","t_package","t_diagram","t_diagramobjects",
        "t_diagramlinks","t_objectproperties","t_xref","t_document",
        "t_operation","t_attribute","t_operationparams")
GROUPS=(("elementTypes","t_object","Object_Type"),
        ("connectorTypes","t_connector","Connector_Type"),
        ("diagramTypes","t_diagram","Diagram_Type"))

def profile(path):
    with path.open("rb") as fp:
        h=hashlib.sha256()
        for chunk in iter(lambda:fp.read(1024*1024),b""):
            h.update(chunk)
    con=sqlite3.connect("file:"+str(path.resolve())+"?mode=ro",uri=True)
    try:
        integrity=con.execute("PRAGMA quick_check").fetchone()[0]
        if integrity!="ok": raise ValueError("QEAX SQLite quick_check failed: "+integrity)
        present={r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        missing=set(TABLES)-present
        if missing: raise ValueError("Missing EA tables: "+", ".join(sorted(missing)))
        tables={t:con.execute("SELECT COUNT(*) FROM "+t).fetchone()[0] for t in TABLES}
        kinds={}
        for key,t,col in GROUPS:
            kinds[key]={str(k if k is not None else "<null>"):n
                        for k,n in con.execute("SELECT "+col+", COUNT(*) FROM "+t+" GROUP BY "+col)}
            if sum(kinds[key].values())!=tables[t]:
                raise ValueError("Distribution mismatch: "+t)
        return {"schema":"mdse-ea-local-profile-evidence/1",
                "fileSha256":h.hexdigest(),
                "sqliteQuickCheck":"ok","expected":{"tables":tables,**kinds}}
    finally: con.close()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("qeax",type=pathlib.Path)
    ap.add_argument("--out",required=True,type=pathlib.Path,
                    help="LOCAL path outside Test_Vault_ checkout")
    args=ap.parse_args()
    if args.out.resolve().is_relative_to(pathlib.Path(__file__).resolve().parents[1]):
        raise SystemExit("Output must be outside Test_Vault_: source-specific evidence is local-only")
    result=profile(args.qeax)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("Local QEAX profile written. Counts:",{k:result["expected"]["tables"][k]
          for k in ("t_object","t_connector","t_package","t_diagram")})

if __name__=="__main__": main()
