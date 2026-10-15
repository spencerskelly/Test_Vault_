"""Read-only Step18 manifest reconciliation and rollback verification."""
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/"Base Vault/Definition/mdse-release.yaml"
INVENTORY=ROOT/"66_Testing/consolidation/step17_registry_proposal.json"
BASE="29a05fc71c2f25108f07927870ac5d3d3bdd618b"
CANDIDATE="6d06db25ed50ff390460c567b8fa769981aacc9e"
ANCHOR="\ndocuments:\n"

def sha(raw):
    return hashlib.sha1(("blob "+str(len(raw))+"\0").encode()+raw).hexdigest()

def rows(record):
    e=record["entries"]
    if len(e)!=32 or len({x["path"] for x in e})!=32:
        raise ValueError("Invalid row count")
    if sum(x["proposedStatus"]=="reference" for x in e)!=29:
        raise ValueError("Reference count changed")
    if sum(x["proposedStatus"]=="proposal" for x in e)!=3:
        raise ValueError("Proposal count changed")
    if any(x["reviewDecision"]!="PENDING_DOCUMENT_CONTROL_APPROVAL" for x in e):
        raise ValueError("Unreviewed disposition changed")
    return "".join('  - {path: "'+x["path"]+'", status: '+x["proposedStatus"]+'}\n' for x in e)

def baseline(manifest,record):
    ins=ANCHOR+rows(record)
    if manifest.count(ins)!=1:
        raise ValueError("Insertion mismatch")
    original=manifest.replace(ins,ANCHOR,1)
    if sha(original.encode())!=BASE:
        raise ValueError("Original manifest not recoverable")
    return original

def audit(manifest,record):
    if sha(manifest.encode())!=CANDIDATE:
        raise ValueError("Candidate manifest changed")
    if record["baselineManifestBlob"]!=BASE or record["changeStatus"]!="PROPOSAL_ONLY_NO_LIVE_MANIFEST_MODIFICATION":
        raise ValueError("Unreviewed registry source")
    original=baseline(manifest,record)
    for x in record["entries"]:
        p=x["path"]
        if not p.startswith("00_Workspace/") or p.count("/")!=1 or not p.endswith(".md"):
            raise ValueError("Unreviewed path")
        f=ROOT/p
        if not f.is_file() or sha(f.read_bytes())!=x["sha"]:
            raise ValueError("Source file drift")
    from step17_registry_review import existing_rows,tracked_md,SCAN_FOLDERS
    before=existing_rows(original)
    after=existing_rows(manifest)
    proposed={x["path"] for x in record["entries"]}
    if proposed&before or after!=before|proposed:
        raise ValueError("Unexpected registry change")
    all_docs=set().union(*(tracked_md(d) for d in SCAN_FOLDERS))
    if all_docs-after:
        raise ValueError("Unregistered files remain")
    return {"inserted":32,"reference":29,"proposal":3,"missing":0,"approved":False}

if __name__=="__main__":
    record=json.loads(INVENTORY.read_text())
    result=audit(MANIFEST.read_text(),record)
    print("STEP18_REGISTRY_CANDIDATE="+json.dumps(result,sort_keys=True))
    print("STEP18_LIVE_RELEASE_APPROVED=false")
