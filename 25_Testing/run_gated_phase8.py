#!/usr/bin/env python3
"""Gate Phase 8 connector ledger creation on exact source and disposition checks.
All outputs are local-only; Phase 8 evidence is NOT accepted native SysML v2.
"""
import argparse
import csv
import tempfile
import shutil
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
    # Destination must not exist. Stage as a sibling to permit same-volume rename.
    if out.exists():
        raise ValueError("Refusing existing Phase 8 ledger destination (even empty)")
    if not out.parent.is_dir():
        raise ValueError("Phase 8 output parent must already exist")
    stage_dir=Path(tempfile.mkdtemp(prefix=".phase8-staging-",dir=out.parent))
    try:
        spec=importlib.util.spec_from_file_location("phase8_normalize", PHASE8)
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        summary=module.reconcile(qeax,registry,stage_dir)
        ledger=stage_dir/"local_only_phase8_ledger.csv"
        aggregate=stage_dir/"aggregate_only.json"
        if not ledger.is_file() or not aggregate.is_file():
            raise RuntimeError("Phase 8 expected output files missing")
        with ledger.open(newline="",encoding="utf-8") as fp:
            reader=csv.DictReader(fp)
            required={"source_pk","source_guid","raw_from","raw_to","family","rule",
                      "role","status","normalized_from","normalized_to",
                      "source_kind","target_kind","diagnostics"}
            if not reader.fieldnames or set(reader.fieldnames)!=required:
                raise RuntimeError("Phase 8 ledger schema mismatch")
            count=0
            ids=set()
            for row in reader:
                if None in row or not row["source_pk"] or not row["status"]:
                    raise RuntimeError("Incomplete Phase 8 ledger row")
                if row["source_pk"] in ids:
                    raise RuntimeError("Duplicate Phase 8 source connector ID")
                ids.add(row["source_pk"])
                count+=1
        stored=json.loads(aggregate.read_text(encoding="utf-8"))
        expected=gate["connectorCount"]
        if count!=expected or summary["total"]!=expected or stored!=summary:
            raise RuntimeError("Phase 8 ledger/summary/source connector counts disagree")
        if summary.get("native_certified")!=0:
            raise RuntimeError("Phase 8 incorrectly claims native certification")
        # Atomically publish the complete output on the same filesystem.
        stage_dir.rename(out)
    finally:
        if stage_dir.exists():
            shutil.rmtree(stage_dir)
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
