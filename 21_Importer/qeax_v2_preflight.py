#!/usr/bin/env python3
"""V2 local QEAX source preflight, read-only. No native SysML emission is authorized."""
import argparse, json, sqlite3, pathlib, sys, hashlib
PROFILE={"elements":11447,"connectors":14688,"packages":1389}
TABLES={"elements":"t_object","connectors":"t_connector","packages":"t_package"}
def inspect(source,strict=True):
    source=pathlib.Path(source).resolve()
    if not source.is_file():raise ValueError("SOURCE_NOT_FOUND")
    uri=source.as_uri()+"?mode=ro"
    try:
        with sqlite3.connect(uri,uri=True) as db:
            integrity=db.execute("PRAGMA integrity_check").fetchone()[0]
            if integrity!="ok":raise ValueError("SQLITE_INTEGRITY_FAILED")
            counts={}
            for name,table in TABLES.items():
                counts[name]=db.execute("SELECT COUNT(*) FROM "+table).fetchone()[0]
    except sqlite3.DatabaseError as exc:raise ValueError("NOT_VALID_QEAX_SQLITE") from exc
    mismatch={k:{"expected":PROFILE[k],"actual":counts[k]} for k in PROFILE if counts[k]!=PROFILE[k]}
    result={"schema":"mdse-v2-qeax-preflight/1","status":"PASS" if not mismatch else "SOURCE_PROFILE_DRIFT","counts":counts,"profile":"EA_2026_10_15_endgame_mini","profile_mismatches":mismatch,"native_emission_authorized":False,"real_model_rows_exported":False,"ea_diagrams_in_scope":False}
    if strict and mismatch:raise ValueError("SOURCE_PROFILE_DRIFT: "+json.dumps(mismatch,sort_keys=True))
    return result
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("qeax",type=pathlib.Path)
    ap.add_argument("--allow-profile-drift",action="store_true",help="Diagnostic only, never emit a model")
    args=ap.parse_args()
    try: print(json.dumps(inspect(args.qeax,not args.allow_profile_drift),indent=2))
    except (ValueError,OSError) as exc:
        print(json.dumps({"status":"BLOCKED","reason":str(exc),"native_emission_authorized":False}),file=sys.stderr)
        return 1
    return 0
if __name__=="__main__":sys.exit(main())
