#!/usr/bin/env python3
"""Prepare private Mac/Windows synthetic GUI session on an isolated local copy.

Runs only controlled builders/structural checks. It never launches Obsidian,
initializes an author ID, creates a Git remote, uploads evidence or sets PASS.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from step21_evidence import blank_record, evaluate

ROOT=Path(__file__).resolve().parents[2]
FOLDER="88_Step20_Synthetic_GUI_Model"
GENERATOR=ROOT/"66_Testing/consolidation/step20_synthetic_vault.py"
VALIDATOR=ROOT/"66_Testing/consolidation/step20_validate_fixture.py"
BUILDER=ROOT/"Base Vault/Tools/v0.8.0-r2/build-base.py"
NATIVE=ROOT/"Base Vault/Testing/check-release.py"
LOCK=ROOT/".obsidian/plugin-lock.yaml"

def git_commit():
    got=subprocess.run(["git","-C",str(ROOT),"rev-parse","HEAD"],
                       check=True,capture_output=True,text=True).stdout.strip()
    if not re.fullmatch(r"[a-f0-9]{40}",got):
        raise ValueError("Missing exact checkout SHA")
    return got

def fixture_snapshot(folder):
    paths=sorted(x for x in folder.iterdir() if x.is_file())
    model=[x for x in paths if x.name.startswith("Step20 - ") and x.suffix==".md"]
    extras={x.name for x in paths if x not in model}
    if len(model)!=12 or extras!={"README_TEST_ONLY.md","STEP20_GUI_ACCEPTANCE.md","FIXTURE_PROVENANCE.json"}:
        raise ValueError("Unexpected synthetic model footprint")
    h=hashlib.sha256()
    for path in paths:
        data=path.read_bytes()
        h.update(path.name.encode("utf-8")+b"\0"+str(len(data)).encode()+b"\0"+data)
    return h.hexdigest()

def invoke(*args,output=None):
    x=subprocess.run([sys.executable,*map(str,args)],cwd=ROOT,
                     capture_output=True,text=True,check=False)
    if output is not None:
        output.write_text(x.stdout+"\n"+x.stderr,encoding="utf-8")
    if x.returncode:
        # no source/model content dumped by this wrapper
        raise ValueError("Step21 controlled prerequisite failed; inspect private diagnostic")
    return x.stdout

def prepare(workspace,platform,*,expected_commit=None):
    work=Path(workspace).expanduser().absolute()
    if platform not in ("macos","windows"):
        raise ValueError("Unknown target platform")
    if ROOT==work or ROOT in work.parents:
        raise ValueError("Private sessions cannot be written into tracked repository")
    if work.exists():
        raise ValueError("Refusing to overwrite an existing session")
    commit=git_commit()
    if expected_commit and expected_commit!=commit:
        raise ValueError("Checked out commit differs from requested acceptance baseline")
    work.mkdir(parents=True,exist_ok=False)
    clean=work/"01_Clean_Uninitialized_Base"
    test=work/"02_Synthetic_GUI_Vault"
    invoke(BUILDER,clean,output=work/"PRIVATE_BASE_BUILD.log")
    native=invoke(NATIVE,"--workbench","55_Workbench","--base",clean,
                  output=work/"PRIVATE_RELEASE_CHECK.log")
    if "0 fail," not in native:
        raise ValueError("Native checker did not report zero failures")
    invoke(GENERATOR,"--base",clean,"--out",test,
           output=work/"PRIVATE_SYNTHETIC_GENERATION.log")
    invoke(VALIDATOR,"--vault",test,
           output=work/"PRIVATE_STRUCTURAL_VALIDATION.log")
    lockhash=hashlib.sha256((test/".obsidian/plugin-lock.yaml").read_bytes()).hexdigest()
    if (test/".obsidian/plugin-lock.yaml").read_bytes()!=LOCK.read_bytes():
        raise ValueError("Generated lock differs from authoritative lock")
    fixture=fixture_snapshot(test/FOLDER)
    evidence=blank_record(platform,commit,lockhash,fixture)
    evaluate(evidence,expected_platform=platform)
    (work/"PRIVATE_GUI_RESULTS.json").write_text(
        json.dumps(evidence,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    (work/"README_PRIVATE_SESSION.txt").write_text(
      "PRIVATE STEP21 GUI SESSION - PREPARED, NO GUI EXECUTED\n"
      "1. Keep this folder local; never commit, sync to GitHub, or upload logs.\n"
      "2. Back up 02_Synthetic_GUI_Vault before initializing it.\n"
      "3. Change directory into 02_Synthetic_GUI_Vault and run its bundled "
      "Initialize-Vault.sh (macOS) or Initialize-Vault.ps1 (Windows) with a valid "
      "13-character lowercase author code; do not initialize the clean Base.\n"
      "4. Open only the initialized synthetic vault in desktop Obsidian.\n"
      "5. Perform G20-01 through G20-14 and the relevant G20-15 or G20-16 "
      "using STEP20_GUI_ACCEPTANCE.md in the fixture folder.\n"
      "6. Record ACTUAL observations and private evidence references in "
      "PRIVATE_GUI_RESULTS.json (metadata and timestamp required for PASS).\n"
      "7. Run step21_evidence.py --check PRIVATE_GUI_RESULTS.json from a clean checkout "
      "to validate the evidence form; it never grants release/promotion authority.\n"
      "8. The other-platform G20 case stays NOT RUN in this session.\n",
      encoding="utf-8")
    print("STEP21_SESSION_PREPARED="+json.dumps({
        "targetPlatform":platform,"sourceCommit":commit,
        "fixtureNotes":12,"recordCount":16,
        "guiExecuted":False,"results":"NOT_RUN",
        "privateEvidenceCreated":True,"trackedRepoModified":False},
        sort_keys=True))
    return work

def main():
    a=argparse.ArgumentParser()
    a.add_argument("--workspace",required=True,help="new private path OUTSIDE repository")
    a.add_argument("--platform",required=True,choices=["macos","windows"])
    a.add_argument("--expected-commit")
    x=a.parse_args()
    prepare(x.workspace,x.platform,expected_commit=x.expected_commit)

if __name__=="__main__":
    main()
