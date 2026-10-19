#!/usr/bin/env python3
"""STEP-03D read-only source QEAX graph accounting; excludes diagrams."""
import argparse
import json
import sqlite3

def audit(path):
    db = sqlite3.connect("file:" + path + "?mode=ro", uri=True)
    try:
        integrity = db.execute("PRAGMA quick_check").fetchone()[0]
        types = dict(db.execute("SELECT Object_Type, COUNT(*) FROM t_object GROUP BY Object_Type"))
        objects = db.execute("SELECT COUNT(*) FROM t_object").fetchone()[0]
        unique_objects = db.execute("SELECT COUNT(DISTINCT Object_ID) FROM t_object").fetchone()[0]
        connectors = db.execute("SELECT COUNT(*) FROM t_connector").fetchone()[0]
        unique_connectors = db.execute("SELECT COUNT(DISTINCT Connector_ID) FROM t_connector").fetchone()[0]
        broken = db.execute("""SELECT COUNT(*) FROM t_connector c
            LEFT JOIN t_object s ON s.Object_ID=c.Start_Object_ID
            LEFT JOIN t_object t ON t.Object_ID=c.End_Object_ID
            WHERE s.Object_ID IS NULL OR t.Object_ID IS NULL""").fetchone()[0]
        blank_guids = db.execute("SELECT COUNT(*) FROM t_object WHERE ea_guid IS NULL OR TRIM(ea_guid)=''").fetchone()[0]
        return dict(integrity=integrity, objects=objects, unique_objects=unique_objects,
                    connectors=connectors, unique_connectors=unique_connectors,
                    broken_source_endpoints=broken, missing_object_guids=blank_guids,
                    boundary_elements=types.get("Boundary",0), artifact_elements=types.get("Artifact",0),
                    package_objects=types.get("Package",0))
    finally:
        db.close()

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("qeax")
    args=parser.parse_args()
    result=audit(args.qeax)
    print(json.dumps(result,sort_keys=True,indent=2))
    if result["integrity"] != "ok" or result["objects"] != result["unique_objects"] or result["connectors"] != result["unique_connectors"] or result["broken_source_endpoints"] or result["missing_object_guids"]:
        raise SystemExit(1)
