#!/usr/bin/env python3
"""Step17 proposed registry rows: read-only reconciliation, no apply mode.

The governed mdse-release.yaml is untouched until document owner approval.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / "Base Vault/Definition/mdse-release.yaml"
PROPOSAL_PATH = ROOT / "66_Testing/consolidation/step17_registry_proposal.json"
SCAN_FOLDERS = ("00_Workspace", "Importer/Definition")
PROPOSAL_STATUSES = frozenset(("proposal", "reference"))


def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(("blob " + str(len(raw)) + "\0").encode() + raw).hexdigest()


def tracked_md(folder: str) -> set[str]:
    p = subprocess.run(
        ["git", "-C", str(ROOT), "ls-tree", "-z", "--name-only", "HEAD:" + folder],
        check=True, capture_output=True,
    )
    names = [x.decode("utf-8") for x in p.stdout.split(b"\0") if x]
    return {folder + "/" + name for name in names
            if name.endswith(".md") and name != "README.md" and
            (ROOT / folder / name).is_file()}


def existing_rows(manifest: str) -> set[str]:
    # Keep one status assignment per listed file. The native checker examines
    # documents entries; this read-only parser intentionally limits itself
    # to normal one-line schema-v2 path entries.
    import re
    rows = list(re.finditer(
        r'(?m)^  - \{path: "([^"\n]+)", status: (current|reference|proposal|historical|superseded|retired)\b.*\}$',
        manifest,
    ))
    seen = [m.group(1) for m in rows]
    if len(seen) != len(set(seen)):
        raise ValueError("Duplicate existing release registry paths")
    return set(seen)


def render_rows(entries: list[dict]) -> str:
    return "".join(
        '  - {path: "' + x["path"] + '", status: ' + x["proposedStatus"] + '}\n'
        for x in entries
    )


def validate(manifest: str, inventory: dict, *, check_git=True) -> dict:
    if inventory.get("schema") != "mdse-consolidation-step17-registry-reconciliation/1":
        raise ValueError("Unexpected inventory schema")
    if inventory.get("changeStatus") != "PROPOSAL_ONLY_NO_LIVE_MANIFEST_MODIFICATION":
        raise ValueError("Unapproved inventory unexpectedly promoted")
    if git_blob_sha(manifest.encode("utf-8")) != inventory["baselineManifestBlob"]:
        raise ValueError("Live release manifest differed from reviewed baseline")
    entries = inventory["entries"]
    if len(entries) != 32 or inventory.get("baselineUnregisteredCount") != 32:
        raise ValueError("Unexpected inventory count")
    paths = [e["path"] for e in entries]
    if len(set(paths)) != len(paths):
        raise ValueError("Duplicate proposed registry path")
    approved = set()
    for e in entries:
        p = e["path"]
        if not p.startswith("00_Workspace/") or "/" in p.removeprefix("00_Workspace/"):
            raise ValueError("Unexpected registry path or nested directory")
        if not p.endswith(".md") or '"' in p or "\n" in p:
            raise ValueError("Unexpected proposed path")
        if e["proposedStatus"] not in PROPOSAL_STATUSES:
            raise ValueError("Attempted current/superseded/historical/retired promotion")
        if e["reviewDecision"] != "PENDING_DOCUMENT_CONTROL_APPROVAL":
            raise ValueError("Unexpected approval state")
        f = ROOT / p
        if not f.is_file() or git_blob_sha(f.read_bytes()) != e["sha"]:
            raise ValueError("Source blob drift: " + p)
        approved.add(p)
    if sum(x["proposedStatus"] == "proposal" for x in entries) != 3:
        raise ValueError("Expected exactly three explicitly unapproved proposals")
    if sum(x["proposedStatus"] == "reference" for x in entries) != 29:
        raise ValueError("Expected 29 dated evidence references")
    registered = existing_rows(manifest)
    if approved & registered:
        raise ValueError("Some proposed rows already exist in manifest")
    if check_git:
        actual = set().union(*(tracked_md(folder) for folder in SCAN_FOLDERS))
        missing = actual - registered
        if approved != missing:
            raise ValueError("Tree contains different missing files than 32-item inventory")
    return {
        "tracked_unregistered": len(approved),
        "reference_candidates": 29,
        "proposal_candidates": 3,
        "simulated_missing": 0,
        "release_status": "NOT_APPROVED",
    }


def simulate_manifest(manifest: str, inventory: dict) -> str:
    validate(manifest, inventory)
    anchor = "\ndocuments:\n"
    if manifest.count(anchor) != 1:
        raise ValueError("Missing/ambiguous documents anchor")
    return manifest.replace(anchor, anchor + render_rows(inventory["entries"]), 1)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--render", action="store_true",
                    help="Print candidate rows for human review; never write a file")
    args = ap.parse_args()
    manifest = MANIFEST_PATH.read_text(encoding="utf-8")
    inventory = json.loads(PROPOSAL_PATH.read_text(encoding="utf-8"))
    counts = validate(manifest, inventory)
    proposal = simulate_manifest(manifest, inventory)
    if existing_rows(proposal) != (existing_rows(manifest) |
                                   {x["path"] for x in inventory["entries"]}):
        raise ValueError("Simulated registry did not reconcile exactly")
    if args.render:
        print(render_rows(inventory["entries"]), end="")
    else:
        print("STEP17_REGISTRY_PROPOSAL=" + json.dumps(counts, sort_keys=True))
        print("STEP17_LIVE_MANIFEST_UNMODIFIED=TRUE")
        print("STEP17_APPLY_APPROVAL=NOT_GRANTED")


if __name__ == "__main__":
    main()
