#!/usr/bin/env python3
"""Fail-closed snapshot profile selector for a local QEAX (read-only).
Never auto-substitute another profile when selected expectations mismatch.
Profile output remains local. No imported model rows are emitted.
"""
import argparse
import hashlib
import json
import pathlib
import sys

from profile_qeax_local import profile

SECTIONS = ("tables", "elementTypes", "connectorTypes", "diagramTypes")

def compare(observed, selected, require_hash=True):
    problems=[]
    if selected.get("schema") not in ("mdse-ea-local-profile-evidence/1", "mdse-ea-source-profile/1"):
        problems.append({"category":"PROFILE_SCHEMA_INVALID"})
    expected=selected.get("expected")
    if not isinstance(expected,dict):
        return {"status":"BLOCKED","issues":[{"category":"PROFILE_EXPECTED_MISSING"}]}
    for section in SECTIONS:
        want=expected.get(section)
        actual=observed["expected"][section]
        if not isinstance(want,dict):
            problems.append({"category":"PROFILE_SECTION_MISSING","section":section})
            continue
        for key in sorted(set(want)|set(actual)):
            if key not in want:
                problems.append({"category":"UNEXPECTED_SOURCE_KIND","section":section,"kind":key})
            elif key not in actual:
                problems.append({"category":"EXPECTED_SOURCE_KIND_MISSING","section":section,"kind":key})
            elif want[key]!=actual[key]:
                problems.append({"category":"SOURCE_COUNT_DRIFT","section":section,"kind":key,
                                 "expected":want[key],"actual":actual[key]})
    pinned=selected.get("fileSha256")
    if require_hash and pinned and pinned!=observed["fileSha256"]:
        problems.append({"category":"SOURCE_FILE_HASH_MISMATCH"})
    return {"status":"PASS" if not problems else "BLOCKED",
            "profileId":selected.get("profileId","UNNAMED"),
            "issueCount":len(problems),"issues":problems}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("qeax",type=pathlib.Path)
    ap.add_argument("--profile",required=True,type=pathlib.Path)
    ap.add_argument("--report",type=pathlib.Path,
                    help="Optional local-only diagnostics report, never check in source snapshots")
    args=ap.parse_args()
    selected=json.loads(args.profile.read_text(encoding="utf-8"))
    result=compare(profile(args.qeax),selected)
    output=json.dumps(result,indent=2)+"\n"
    if args.report:
        args.report.write_text(output,encoding="utf-8")
    print(output,end="")
    return 0 if result["status"]=="PASS" else 1

if __name__=="__main__":
    sys.exit(main())
