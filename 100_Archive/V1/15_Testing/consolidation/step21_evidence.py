#!/usr/bin/env python3
"""Step21 private, read-only GUI evidence validation.

Preparing or running this tool is NOT human Obsidian acceptance. It does not
open Obsidian, alter recorded results, access QEAX, or publish private records.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

CASES=tuple(f"G20-{n:02d}" for n in range(1,17))
SHA_RE=re.compile(r"^[a-f0-9]{40}$")
HEX_RE=re.compile(r"^[a-f0-9]{64}$")
TERMINAL=("PASS","FAIL","BLOCKED")
PLATFORMS=("macos","windows")

def sha256(data:bytes)->str:
    return hashlib.sha256(data).hexdigest()

def parse_utc(value):
    if not isinstance(value,str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value.replace("Z","+00:00"))
        return True
    except (ValueError,TypeError):
        return False

def blank_record(platform,commit,lock_sha,fixture_sha):
    if platform not in PLATFORMS or not SHA_RE.fullmatch(commit):
        raise ValueError("Platform or source commit invalid")
    if not HEX_RE.fullmatch(lock_sha) or not HEX_RE.fullmatch(fixture_sha):
        raise ValueError("Missing controlled SHA-256 evidence")
    return {
      "schema":"mdse-step21-private-gui-session/1",
      "scope":"SYNTHETIC_ONLY",
      "platform":platform,
      "sourceCommit":commit,
      "pluginLockSha256":lock_sha,
      "fixtureSnapshotSha256":fixture_sha,
      "operatorAlias":None,
      "reviewerAlias":None,
      "osVersion":None,
      "obsidianVersion":None,
      "observedWorkbenchVersion":None,
      "observedBootstrapVersion":None,
      "sessionStartUtc":None,
      "securityAndLocalCloneGates":"NOT_CLEARED",
      "guiApproval":"NOT_APPROVED",
      "caseRecords":[{"id":ident,"status":"NOT RUN","observed":None,
                      "observedAtUtc":None,"evidenceRefs":[],
                      "defectRef":None} for ident in CASES],
      "note":"Private operator worksheet, not a source of automatic PASS."
    }

def evaluate(doc,*,expected_platform=None):
    """Reject incomplete or fabricated-ready records. No output of private paths."""
    if doc.get("schema")!="mdse-step21-private-gui-session/1" or doc.get("scope")!="SYNTHETIC_ONLY":
        raise ValueError("Unknown evidence schema/scope")
    platform=doc.get("platform")
    if platform not in PLATFORMS or (expected_platform and platform!=expected_platform):
        raise ValueError("Incorrect OS session")
    if not SHA_RE.fullmatch(str(doc.get("sourceCommit",""))):
        raise ValueError("Missing tested 40-character Git commit")
    for field in ("pluginLockSha256","fixtureSnapshotSha256"):
        if not HEX_RE.fullmatch(str(doc.get(field,""))):
            raise ValueError("Missing baseline file digest "+field)
    cases=doc.get("caseRecords")
    if not isinstance(cases,list) or len(cases)!=16 or [x.get("id") for x in cases]!=list(CASES):
        raise ValueError("Expected 16 uniquely ordered G20 records")
    count={"NOT RUN":0,"PASS":0,"FAIL":0,"BLOCKED":0}
    for item in cases:
        state=item.get("status")
        if state not in count:
            raise ValueError("Unknown result, including implicit acceptance")
        count[state]+=1
        if state=="NOT RUN":
            if item.get("observed") or item.get("observedAtUtc") or item.get("evidenceRefs") or item.get("defectRef"):
                raise ValueError("NOT RUN record contains claimed observation")
            continue
        if not item.get("observed") or not isinstance(item["observed"],str) or not item["observed"].strip():
            raise ValueError("Terminal result missing actual operator observation")
        if not parse_utc(item.get("observedAtUtc")):
            raise ValueError("Terminal result missing UTC observation time")
        refs=item.get("evidenceRefs")
        if not isinstance(refs,list) or not refs or any(not isinstance(ref,str) or not ref.strip() for ref in refs):
            raise ValueError("Terminal result missing private evidence reference")
        if state=="FAIL" and not item.get("defectRef"):
            raise ValueError("Failed scenario missing tracked defect reference")
    if count["NOT RUN"]<16:
        for field in ("operatorAlias","osVersion","obsidianVersion",
                      "observedWorkbenchVersion","observedBootstrapVersion","sessionStartUtc"):
            if not doc.get(field):
                raise ValueError("Observed results need actual session metadata: "+field)
        if not parse_utc(doc["sessionStartUtc"]):
            raise ValueError("Session start is not an ISO UTC time")
    own_platform="G20-15" if platform=="macos" else "G20-16"
    other_platform="G20-16" if platform=="macos" else "G20-15"
    case_index={x["id"]:x for x in cases}
    if case_index[other_platform]["status"]!="NOT RUN":
        raise ValueError("Other platform sign-off must not be claimed in this session")
    functional_complete=all(case_index[k]["status"]=="PASS" for k in CASES[:14])
    platform_complete=case_index[own_platform]["status"]=="PASS"
    # A syntactically complete record still requires private human review.
    evidence_ready=bool(functional_complete and platform_complete and
                        doc.get("reviewerAlias") and doc.get("guiApproval")=="REVIEWED")
    if doc.get("guiApproval")=="REVIEWED" and not evidence_ready:
        raise ValueError("Premature GUI reviewer approval")
    if doc.get("guiApproval") not in ("NOT_APPROVED","REVIEWED"):
        raise ValueError("Unrecognized GUI approval state")
    return {
      "platform":platform,"count":count,
      "functionalPass":functional_complete,
      "platformPass":platform_complete,
      "operatorEvidenceComplete":evidence_ready,
      "externalPromotionGatesCleared":False,
      "releaseIssued":False,
    }

def check_pair(mac,windows):
    a=evaluate(mac,expected_platform="macos")
    b=evaluate(windows,expected_platform="windows")
    if mac["sourceCommit"]!=windows["sourceCommit"] or mac["pluginLockSha256"]!=windows["pluginLockSha256"] or mac["fixtureSnapshotSha256"]!=windows["fixtureSnapshotSha256"]:
        raise ValueError("Different source revision/lock/synthetic fixture between platforms")
    return {"matchedSource":True,
            "bothGuiEvidenceReviewed":a["operatorEvidenceComplete"] and b["operatorEvidenceComplete"],
            "publicMainPromotionAllowed":False,"standaloneArchiveAllowed":False,
            "macos":a,"windows":b}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--check",nargs="+",required=True,help="one per-platform private JSON, or both for cross-platform summary")
    args=p.parse_args()
    docs=[json.loads(Path(x).read_text(encoding="utf-8")) for x in args.check]
    result=evaluate(docs[0]) if len(docs)==1 else check_pair(*sorted(docs,key=lambda x:x["platform"])) if len(docs)==2 else None
    if result is None:
        raise ValueError("Expected one or two private evidence files")
    print("STEP21_PRIVATE_EVIDENCE_SUMMARY="+json.dumps(result,sort_keys=True))
    print("STEP21_OBSIDIAN_GUI_EXECUTED_BY_CI=false")
    print("STEP21_PUBLIC_MAIN_PROMOTION=false")

if __name__=="__main__":
    main()
