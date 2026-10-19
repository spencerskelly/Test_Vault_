#!/usr/bin/env python3
"""STEP-03X: one-command isolated V2 base + identity audit; no manual base setup."""
import argparse,importlib.util,json,shutil,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod
def stage(uid_ledger,crosswalk,destination):
    target=Path(destination).resolve()
    if target.exists():raise ValueError("Destination already exists")
    builder=load("20_Base Vault/build_v2_test_base.py","base_v2")
    auditor=load("21_Importer/v2_step03w_identity_reservation_audit.py","audit_v2")
    try:
        builder.build(target)
        report=auditor.audit(uid_ledger,crosswalk,target,target/"99_System"/"uid_audit.private.jsonl")
        status={"schema":"mdse-v2-step03x/1","base_generated":True,
                "plugin_ready":False,"native_import_ready":False,
                "candidate_identity_audit":report,
                "next_gate":"synchronized runtime plugins and destination-source-map reconciliation"}
        (target/"99_System"/"step03x_readiness.json").write_text(json.dumps(status,indent=2)+"\n")
        return status
    except BaseException:
        if target.exists():shutil.rmtree(target)
        raise
if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("uid_ledger");p.add_argument("identity_crosswalk");p.add_argument("output_base")
    a=p.parse_args()
    try:print(json.dumps(stage(a.uid_ledger,a.identity_crosswalk,a.output_base),indent=2))
    except (ValueError,OSError) as exc:
        print(json.dumps({"status":"BLOCKED","error":str(exc)}),file=sys.stderr);sys.exit(1)
