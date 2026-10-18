#!/usr/bin/env python3
"""Gate Phase 8 connector ledger creation on exact source and disposition checks.
All outputs are local-only; Phase 8 evidence is NOT accepted native SysML v2.
"""
import argparse
import importlib.util
import json
from pathlib import Path

from gate_v2_qeax_reconciliation import assess, ensure_private_output
from profile_qeax_local import profile
from reconcile_qeax_dispositions import reconcile

ROOT=Path(__file__).resolve().parents[1]
PHASE8=ROOT/"14_Workbench/registry/runtime/normalize_qeax_phase8.py"

def execute(qeax, source_profile, disposition_policy, registry, out, stage=None):
    ensure_private_output(out,ROOT)
    if not qeax.is_file() or not source_profile.is_file() or not disposition_policy.is_file() or not registry.is_file():
        raise ValueError("Missing required QEAX, selected profile, policy or registry")
    observed=profile(qeax)
    selected=json.loads(source_profile.read_text(encoding="utf-8"))
    policy=json.loads(disposition_policy.read_text(encoding="utf-8"))
    gate=assess(observed,selected,reconcile(qeax,policy))
    if gate["status"]!="PASS":
        # MUST NOT create output directory/ledger on failure.
        return {"status":"BLOCKED","gate":gate,"ledgerWritten":False}
    if out.exists() and any(out.iterdir()):
        raise ValueError("Refusing to overwrite an existing Phase 8 ledger folder")
    spec=importlib.util.spec_from_file_location("phase8_normalize", PHASE8)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    summary=module.reconcile(qeax,registry,out)
    if summary["total"]!=gate["connectorCount"]:
        raise RuntimeError("Connector ledger count differs from admitted source snapshot")
    return {"status":"RECONCILED_EVIDENCE_ONLY","gate":gate,"aggregate":summary,
            "ledgerWritten":True,"nativeCertified":0}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--qeax",type=Path,required=True)
    parser.add_argument("--source-profile",type=Path,required=True)
    parser.add_argument("--disposition-policy",type=Path,required=True)
    parser.add_argument("--registry",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    result=execute(args.qeax,args.source_profile,args.disposition_policy,args.registry,args.out)
    print(json.dumps(result,indent=2))
    return 0 if result["status"]=="RECONCILED_EVIDENCE_ONLY" else 1

if __name__=="__main__":
    raise SystemExit(main())
