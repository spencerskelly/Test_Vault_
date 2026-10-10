#!/usr/bin/env python3
"""Build two *disposable*, provenance-labelled Obsidian GUI test vaults.
Never changes canonical source, release pins, or plugin lock. No QEAX in output.
"""
import argparse
import hashlib
import json
import re
import shutil
import zipfile
from pathlib import Path

import yaml

p = argparse.ArgumentParser()
p.add_argument("--base", required=True)
p.add_argument("--workbench", required=True)
p.add_argument("--out", required=True)
p.add_argument("--source-sha", required=True)
a = p.parse_args()
base, wb, out = Path(a.base), Path(a.workbench), Path(a.out)
assert base.is_dir() and (base / ".vault.yaml").is_file()
assert (wb / "main.js").is_file()
assert len(a.source_sha) == 40 and all(c in "0123456789abcdef" for c in a.source_sha)
assert not out.exists(), "Refusing to overwrite existing acceptance kit"
out.mkdir(parents=True)

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def add(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    assert not path.exists(), f"Refuse overwrite: {path}"
    path.write_text(text, encoding="utf-8", newline="\n")

lock = yaml.safe_load((base / ".obsidian/plugin-lock.yaml").read_text())
assert lock["schema"] == 2
assert lock["plugins"]["mdse-bootstrap"]["version"] == "0.3.1"
locked = lock["plugins"]["mdse-workbench"]["sha256"]
controlled = base / ".obsidian/plugins/mdse-workbench"
assert all(digest(controlled / name) == locked[name] for name in ["main.js", "manifest.json", "styles.css"])
candidate_manifest = json.loads((wb / "manifest.json").read_text())
assert candidate_manifest["id"] == "mdse-workbench"
assert candidate_manifest["version"] == "0.1.18"
assert digest(wb / "main.js") != locked["main.js"], "Candidate main.js unexpectedly equals controlled release"
assert (base / "99_System/03_Schemas/local-model.yaml").read_text().find('schemaVersion: "0.5"') >= 0

controlled_vault = out / "01_Controlled_Base"
candidate_vault = out / "02_BOM_Candidate_Test_Only"
shutil.copytree(base, controlled_vault, symlinks=False, ignore=shutil.ignore_patterns(".git", ".DS_Store", "workspace.json"))
shutil.copytree(base, candidate_vault, symlinks=False, ignore=shutil.ignore_patterns(".git", ".DS_Store", "workspace.json"))
for name in ["main.js", "manifest.json", "styles.css"]:
    shutil.copyfile(wb / name, candidate_vault / ".obsidian/plugins/mdse-workbench" / name)
assert digest(controlled_vault / ".obsidian/plugins/mdse-workbench/main.js") == locked["main.js"]
assert digest(candidate_vault / ".obsidian/plugins/mdse-workbench/main.js") == digest(wb / "main.js")
# This is a deliberatively unapproved RELATIONSHIP SANDBOX, not a governed schema change.
rel_path = candidate_vault / "99_System/03_Schemas/relationships.yaml"
rel = rel_path.read_text(encoding="utf-8")
assert rel.startswith("schemaVersion: '1.36'") and "oneWay:\n" in rel
assert "field: variantOf" not in rel
rel = rel.replace("schemaVersion: '1.36'", "schemaVersion: '1.37'", 1)
rel = rel.replace("oneWay:\n", "oneWay:\n- {field: variantOf, from: [Object], to: [Object]}\n", 1)
rel_path.write_text("# TEST-ONLY EXPERIMENTAL variantOf schema, NOT APPROVED FOR RELEASE\n" + rel, encoding="utf-8", newline="\n")
assert yaml.safe_load(rel_path.read_text())["oneWay"][0] == {"field": "variantOf", "from": ["Object"], "to": ["Object"]}
assert yaml.safe_load((controlled_vault / "99_System/03_Schemas/relationships.yaml").read_text())["schemaVersion"] == "1.36"
token = "testfixturexx"
assert len(token) == 13
def uid(i):
    return f"202610091827{i:05d}" + token
def object_note(name, number, fields=""):
    return "---\ntype: Object\nsubtype: electrical\nid: OBJ-99" + str(number) + "\nuid: " + uid(number) + "\nstatus: Draft\ntags: []\n" + fields + "---\n\n# " + name + "\n\n## Definition\n\nStep 18 disposable test fixture only; not an engineering model.\n"
def requirement_note(name, number):
    return "---\ntype: Requirement\nsubtype: functional\nid: REQ-99" + str(number) + "\nuid: " + uid(number) + "\nstatus: Draft\ntags: []\n---\n\n# " + name + "\n\n## Definition\n\nStep 18 invalid-target fixture.\n"
fixture = candidate_vault / "88_Step18_Disposable_UI_Fixtures"
add(fixture / "Family.md", object_note("Family", 1))
add(fixture / "Product A.md", object_note("Product A", 2, 'variantOf: "[[Family]]"\n'))
add(fixture / "Product B.md", object_note("Product B", 3))
add(fixture / "Wire.md", object_note("Wire", 4))
add(fixture / "Non Object.md", requirement_note("Non Object", 5))
part_a = "20261009182710001" + token
part_b = "20261009182710002" + token
ep = "20261009182710003" + token
assert all(len(t) == 30 for t in (part_a, part_b, ep))
add(fixture / "Assembly 0.5.md", object_note("Assembly 0.5", 6) + "\n## Local Model\n<!-- MDSE:LOCAL-MODEL START schema=0.5 -->\n### Parts\n#### Wire\n- definition: [[Wire]]\n- multiplicity: 2\n^part-" + part_a + "\n### Interfaces\n#### Contextual Test Interface\n^ep-" + ep + "\n<!-- MDSE:LOCAL-MODEL END -->\n")
add(fixture / "Assembly 0.6 READ ONLY.md", object_note("Assembly 0.6 READ ONLY", 7) + "\n## Local Model\n<!-- MDSE:LOCAL-MODEL START schema=0.6 -->\n### Parts\n#### Wire\n- definition: [[Wire]]\n- multiplicity: 2\n- quantity: 0.3500000001\n- unitOfMeasure: m\n^part-" + part_b + "\n<!-- MDSE:LOCAL-MODEL END -->\n")
add(fixture / "README-TEST-ONLY.md", "# Step 18 disposable fixture set\n\nThis folder has invented test examples, not actual EA8647 model artifacts.\nThe experimental relationships.yaml includes unapproved variantOf, and the Workbench main.js differs from the controlled plugin lock. These are expected test drifts.\nEdit only in a disposable clone. No real Git remote, API key or company vault.\n")
# Preserve the Base's release-lock mismatch rather than silently 'correcting' it.
assert (candidate_vault / ".obsidian/plugin-lock.yaml").read_bytes() == (controlled_vault / ".obsidian/plugin-lock.yaml").read_bytes()
meta = {
    "status": "MANUAL_GUI_NOT_EXECUTED", "source_commit": a.source_sha,
    "candidate_plugin": {"version": candidate_manifest["version"],
                         "main_js_sha256": digest(wb / "main.js")},
    "controlled_plugin_main_sha256": locked["main.js"],
    "plugin_lock_unchanged": True,
    "controlled_schema": {"localModel": "0.5", "relationships": "1.36"},
    "candidate_experimental_relationship_version": "1.37 (TEST ONLY)",
    "writer_version": "0.5",
    "contains_original_qeax": False,
    "contains_actual_imported_model": False,
    "vaults": ["01_Controlled_Base", "02_BOM_Candidate_Test_Only"],
}
add(out / "ACCEPTANCE_BUILD_PROVENANCE.json", json.dumps(meta, indent=2, sort_keys=True) + "\n")
add(out / "README_START_HERE.md", """# Step 18 — disposable Obsidian GUI acceptance kit

**Nothing here proves an Obsidian UI test passed.** Do not open these files inside a production MDSE/Engineering vault.

1. Extract this artifact to a new disposable folder on your computer.
2. **01_Controlled_Base** retains exactly the pinned runtime plugin binaries, unchanged release lock and governed schema 0.5/1.36. Run normal first-open and Bootstrap tests here. The existing 0.3.0 manifest / 0.3.1 lock *pre-release* warning is an expected blocker, not a pass.
3. **02_BOM_Candidate_Test_Only** has a freshly built, unreleased Workbench plugin overlaid. This deliberately breaks the Workbench hash in the plugin lock; it also has a **test-only** variantOf relationship 1.37. Neither difference is approved for production. Record the Bootstrap drift warning rather than silencing it.
4. Before opening each copied vault, initialize its .vault.yaml using its bundled Initialize-Vault.sh with a real 13-character lowercase ASCII author code; use a distinct vault name. Initialize a **local-only Git repository** and initial commit in each, with no remote, if testing Bootstrap's Git behavior.
5. Open both as separate vaults in Obsidian 1.13.0+ on desktop; select Trust author and enable plugins in the disposable copies only.
6. Follow the Step 18 runbook in Test_Vault_ at 66_Testing/Step18_Obsidian_UI_Acceptance.md. Write observed results, screenshots, application version, and logs. Never substitute a Node CI pass for an observed Obsidian result.
7. The provided small fixture set is artificial. For the **real-QEAX definitionless Interface** UI case, import the already validated frozen QEAX into a separate disposable copy first; the big imported source model is **not included** in this ZIP. Do not use real business data in this test-only fixture set.

Do not push or merge a test vault or modify canonical schemas, approved runtime plugin payloads, release pins or source BOM files.
""")
zip_path = out.parent / "step18-obsidian-ui-acceptance-kit.zip"
with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for f in sorted(out.rglob("*")):
        if f.is_file():
            z.write(f, f.relative_to(out.parent))
with zipfile.ZipFile(zip_path) as z:
    assert z.testzip() is None
    assert "step18-obsidian-ui-acceptance-kit/ACCEPTANCE_BUILD_PROVENANCE.json" in z.namelist()
print("PASS: generated controlled+candidate isolated test vaults and byte-checked archive")
print("BUNDLE_SHA256", digest(zip_path))
print("CANDIDATE_PLUGIN_SHA256", digest(wb / "main.js"))
print("LOCKED_PLUGIN_SHA256", locked["main.js"])
print("NOTE: GUI NOT EXECUTED; candidate plugin/experimental relationship drift deliberately expected")
