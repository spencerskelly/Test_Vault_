#!/usr/bin/env python3
"""Build an uninitialized, standalone SysML v2 test base; never imports archived V1 files."""
import argparse, json, shutil, pathlib, hashlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
REQUIRED={
 "20_Base Vault/README.md":"99_System/README_Base_V2.md",
 "20_Base Vault/v2_base_release_manifest.json":"99_System/v2_base_release_manifest.json",
 "21_Importer/README.md":"99_System/README_Importer_V2.md",
 "23_Bootstrap/README.md":"99_System/README_Bootstrap_V2.md",
 "26_Definitions/APPROVED_V2_TRANSLATION_BASELINE_AND_TEST_HANDOFF_2026-10-18.md":"99_System/Approved_V2_Translation_Baseline.md",
 "24_Workbench/registry/sysml_v2_registry_pins.v0.1.json":"99_System/registry/sysml_v2_registry_pins.v0.1.json",
 "24_Workbench/registry/family_disposition_registry.v0.2.json":"99_System/registry/family_disposition_registry.v0.2.json",
 "24_Workbench/registry/sysml_v2_semantic_rules.v0.2.json":"99_System/registry/sysml_v2_semantic_rules.v0.2.json",
 "24_Workbench/registry/sysml_v2_semantic_decisions.v0.1.json":"99_System/registry/sysml_v2_semantic_decisions.v0.1.json",
}
def build(dest):
    dest=dest.resolve()
    if dest.exists():raise ValueError("OUTPUT_ALREADY_EXISTS")
    if ROOT==dest or ROOT in dest.parents:raise ValueError("NO_BUILD_INSIDE_REPOSITORY")
    if any("100_Archive" in x for x in REQUIRED):raise ValueError("ARCHIVE_NOT_ALLOWED")
    missing=[p for p in REQUIRED if not (ROOT/p).is_file()]
    if missing:raise ValueError("MISSING_V2_DEPENDENCIES: "+",".join(missing))
    try:
        dest.mkdir(parents=True)
        hashes={}
        for source,target in REQUIRED.items():
            data=(ROOT/source).read_bytes()
            out=dest/target
            out.parent.mkdir(parents=True,exist_ok=True)
            out.write_bytes(data)
            hashes[target]=hashlib.sha256(data).hexdigest()
        # Only built-in Obsidian settings are included. No plugin binary is claimed or enabled.
        obs=dest/".obsidian"
        obs.mkdir(exist_ok=True)
        configs={
            "app.json":{"showLineNumber":True,"strictLineBreaks":False},
            "appearance.json":{"baseFontSize":16,"cssTheme":""},
            "core-plugins.json":["file-explorer","global-search","switcher","graph","backlinks","outgoing-link","tag-pane","properties","page-preview","daily-notes","templates","note-composer","command-palette","slash-command"],
            "community-plugins.json":[],
        }
        for name,settings in configs.items():
            payload=json.dumps(settings,indent=2)+"\n"
            (obs/name).write_text(payload)
            hashes[".obsidian/"+name]=hashlib.sha256(payload.encode()).hexdigest()
        (dest/".mdse_v2_test_base.json").write_text(json.dumps({"schema":"mdse-v2-test-base/1","status":"uninitialized_test_only","native_import_ready":False,"plugin_ready":False,"files":hashes},indent=2)+"\n")
    except BaseException:
        shutil.rmtree(dest,ignore_errors=True)
        raise
    return {"status":"PASS","files":len(hashes),"output":str(dest),"native_import_ready":False}
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("destination",type=pathlib.Path)
    a=ap.parse_args()
    try:print(json.dumps(build(a.destination)))
    except (ValueError,OSError) as err:
        print(json.dumps({"status":"BLOCKED","error":str(err)}),file=sys.stderr)
        sys.exit(1)
