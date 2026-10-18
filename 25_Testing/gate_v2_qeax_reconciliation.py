#!/usr/bin/env python3
"""Fail-closed, read-only preflight for SysML v2 connector reconciliation.

A selected source profile is mandatory. No native mapping or ledger is produced here.
Source-specific report must remain outside repository checkout.
"""
import argparse
import json
from pathlib import Path
from check_qeax_source_profile import compare
from profile_qeax_local import profile
from reconcile_qeax_dispositions import reconcile

def assess(observed, selected, table_result):
    snapshot=compare(observed, selected)
    return {
        "schema":"mdse-v2-qeax-preflight/1",
        "status":"PASS" if snapshot["status"]=="PASS" and table_result["status"]=="PASS" else "BLOCKED",
        "checks":{"snapshot":snapshot,"tableDispositions":table_result},
        "connectorCount":observed["expected"]["tables"]["t_connector"],
        "nextStage":"CONNECTOR_RECONCILIATION_NOT_EXECUTED",
    }

def ensure_private_output(output, root):
    if output is None: return
    resolved=output.resolve()
    if resolved.is_relative_to(root.resolve()):
        raise ValueError("Local evidence report must be outside Test_Vault_ checkout")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("qeax",type=Path)
    ap.add_argument("--source-profile",type=Path,required=True)
    ap.add_argument("--disposition-policy",type=Path,required=True)
    ap.add_argument("--report",type=Path)
    args=ap.parse_args()
    root=Path(__file__).resolve().parents[1]
    ensure_private_output(args.report,root)
    if not args.qeax.is_file(): ap.error("QEAX not found")
    selected=json.loads(args.source_profile.read_text(encoding="utf-8"))
    policy=json.loads(args.disposition_policy.read_text(encoding="utf-8"))
    result=assess(profile(args.qeax),selected,reconcile(args.qeax,policy))
    payload=json.dumps(result,indent=2)+"\n"
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True)
        args.report.write_text(payload,encoding="utf-8")
    print(payload,end="")
    return 0 if result["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
