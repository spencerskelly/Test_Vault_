#!/usr/bin/env python3
"""Local Pass 6 acceptance runner: synthetic tests plus optional private QEAX audit.

No network, source upload, native emission, or writes to repository.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
REPO=HERE.parent
MODULES=[
 "test_phase8_deferred_evidence_compat",
 "test_phase8_raw_evidence_coverage",
 "test_phase8_original_field_mapping",
 "test_phase8_raw_evidence_values",
 "test_phase8_e2e_original_values",
 "test_phase8_atomic_publication",
 "test_phase8_input_attestation",
 "test_verify_phase8_private_ledger",
]

def execute(qeax=None,ledger=None):
    cmd=[sys.executable,"-m","unittest","-v",*MODULES]
    result=subprocess.run(cmd,cwd=HERE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    summary={"schema":"mdse-pass06-local-acceptance/1",
             "revision":"local-checkout-unattested",
             "syntheticTests":{"passed":result.returncode==0,
                "exitCode":result.returncode,
                "modules":MODULES},
             "nativeCertified":0}
    if (qeax is None)!=(ledger is None):
        raise ValueError("QEAX_AND_LEDGER_REQUIRED_TOGETHER")
    if qeax is not None and result.returncode==0:
        sys.path.insert(0,str(HERE))
        from verify_phase8_private_ledger import audit
        summary["privateFidelityAudit"]=audit(qeax,ledger)
    summary["status"]="PASS_SYNTHETIC_ONLY" if result.returncode==0 else "FAIL_TESTS"
    if "privateFidelityAudit" in summary:
        summary["status"]="PASS_SOURCE_FIDELITY" if summary["privateFidelityAudit"]["status"]=="PASS" else "FAIL_SOURCE_FIDELITY"
    return summary,result

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--qeax",type=Path)
    parser.add_argument("--ledger",type=Path)
    parser.add_argument("--report",type=Path,required=True,
                        help="Absolute or relative path OUTSIDE the repository.")
    args=parser.parse_args()
    target=args.report.resolve()
    if target.is_relative_to(REPO.resolve()):
        parser.error("REPORT_MUST_BE_OUTSIDE_REPOSITORY")
    if target.exists():parser.error("REPORT_ALREADY_EXISTS")
    summary,run=execute(args.qeax,args.ledger)
    print(run.stderr,file=sys.stderr,end="")
    print(run.stdout,end="")
    target.write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps({"status":summary["status"],"report":str(target),"nativeCertified":0}))
    raise SystemExit(0 if summary["status"].startswith("PASS") else 1)
