#!/usr/bin/env python3
"""Read-only EA snapshot and cross-table integrity audit; aggregate-only output."""
import argparse
import hashlib
import json
import pathlib
import sqlite3

def audit(path):
    path=pathlib.Path(path).resolve()
    h=hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda:stream.read(1024*1024),b""):
            h.update(chunk)
    c=sqlite3.connect("file:"+str(path)+"?mode=ro",uri=True)
    try:
        if c.execute("PRAGMA quick_check").fetchone()[0]!="ok":
            raise ValueError("SQLITE_INTEGRITY_FAILURE")
        checks={
          "connector_source_missing":"""SELECT COUNT(*) FROM t_connector x LEFT JOIN t_object o ON x.Start_Object_ID=o.Object_ID WHERE x.Start_Object_ID IS NOT NULL AND x.Start_Object_ID<>0 AND o.Object_ID IS NULL""",
          "connector_target_missing":"""SELECT COUNT(*) FROM t_connector x LEFT JOIN t_object o ON x.End_Object_ID=o.Object_ID WHERE x.End_Object_ID IS NOT NULL AND x.End_Object_ID<>0 AND o.Object_ID IS NULL""",
          "tag_owner_missing":"""SELECT COUNT(*) FROM t_objectproperties p LEFT JOIN t_object o ON p.Object_ID=o.Object_ID WHERE p.Object_ID IS NOT NULL AND p.Object_ID<>0 AND o.Object_ID IS NULL""",
          "element_package_missing":"""SELECT COUNT(*) FROM t_object o LEFT JOIN t_package p ON o.Package_ID=p.Package_ID WHERE o.Package_ID IS NOT NULL AND o.Package_ID<>0 AND p.Package_ID IS NULL""",
          "package_parent_missing":"""SELECT COUNT(*) FROM t_package c LEFT JOIN t_package p ON c.Parent_ID=p.Package_ID WHERE c.Parent_ID IS NOT NULL AND c.Parent_ID<>0 AND p.Package_ID IS NULL""",
        }
        bad={name:c.execute(query).fetchone()[0] for name,query in checks.items()}
        count={kind:c.execute("SELECT COUNT(*) FROM "+table).fetchone()[0] for kind,table in
               (("element","t_object"),("connector","t_connector"),("package","t_package"),("tag","t_objectproperties"))}
        return {"schema":"mdse-ea-snapshot-integrity-aggregate/1",
            "sourceSha256":h.hexdigest(),"sqliteQuickCheck":"ok","counts":count,
            "unresolvedReferences":bad,"unresolvedTotal":sum(bad.values()),
            "status":"PASS" if not any(bad.values()) else "REVIEW_REQUIRED",
            "nativeCertified":0}
    finally:
        c.close()

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("qeax",type=pathlib.Path)
    a=p.parse_args()
    print(json.dumps(audit(a.qeax),sort_keys=True,indent=2))
