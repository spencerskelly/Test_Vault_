#!/usr/bin/env python3
"""Step 19: inspect a disposable generated Base Vault without modifying it.

Separate from the controlled native check-release.py. All source-model archives,
user workstations, remote branches, and Obsidian GUI state are out of scope.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / "Base Vault/Definition/mdse-release.yaml"
LOCK_PATH = ROOT / ".obsidian/plugin-lock.yaml"
CONTROLLED_GUIDE = ROOT / "Base Vault/Definition/MDSE Workbench User Guide.md"
WORKBENCH_GUIDE = ROOT / "55_Workbench/docs/User Guide/MDSE Workbench User Guide.md"
MAPPED_GUIDE = "99_System/01_Admin/MDSE Workbench User Guide.md"
PAYLOAD_DIR = ROOT / "Base Vault/Runtime/Plugins"
RELEASE_CHECK = ROOT / "Base Vault/Testing/check-release.py"
EXPECTED_MANIFEST_BLOB = "6d06db25ed50ff390460c567b8fa769981aacc9e"
EXPECTED_LOCK_BLOB = "c430670577318457972a154012d08c6d28e6d11b"
EXPECTED_GUIDE_BLOB = "2a82d21f89a2e80e4df227760f85f1215cd76ec5"
TRACKED_PLUGIN_FILES = ("main.js", "manifest.json", "styles.css", "data.json")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def blob(data: bytes) -> str:
    return hashlib.sha1(("blob " + str(len(data)) + "\0").encode() + data).hexdigest()


def check_equal(a: bytes, b: bytes, description: str) -> None:
    if a != b:
        raise ValueError(description + " byte mismatch")


def inspect(base: Path) -> dict:
    if not base.is_dir() or base.resolve() == ROOT.resolve():
        raise ValueError("Base must be an existing, separate disposable output folder")
    man_raw = MANIFEST_PATH.read_bytes()
    lock_raw = LOCK_PATH.read_bytes()
    if blob(man_raw) != EXPECTED_MANIFEST_BLOB or blob(lock_raw) != EXPECTED_LOCK_BLOB:
        raise ValueError("Release manifest or lock changed from reviewed baseline")
    man = yaml.safe_load(man_raw)
    lock = yaml.safe_load(lock_raw)
    if man["mdseRelease"] != "0.8.0" or man["releaseStatus"] != "pre-release":
        raise ValueError("Unexpected release status")
    if man["schemas"] != {"relationships": "1.36", "elementTypes": "1.18", "localModel": "0.5"}:
        raise ValueError("Unexpected governed schema pins")
    guide = CONTROLLED_GUIDE.read_bytes()
    if blob(guide) != EXPECTED_GUIDE_BLOB:
        raise ValueError("Controlled guide changed")
    check_equal(guide, WORKBENCH_GUIDE.read_bytes(), "W341 source guide")
    target = base / MAPPED_GUIDE
    if not target.is_file():
        raise ValueError("Packaged Workbench guide missing")
    check_equal(guide, target.read_bytes(), "W341 generated guide")
    guide_maps = [m for m in man["runtimeBase"]["mappedFiles"]
                  if m["source"] == "Base Vault/Definition/MDSE Workbench User Guide.md"]
    if len(guide_maps) != 1 or guide_maps[0]["target"] != MAPPED_GUIDE:
        raise ValueError("W341 guide mapping changed")
    check_equal(lock_raw, (base / ".obsidian/plugin-lock.yaml").read_bytes(),
                "Generated plugin lock")
    if (base / "Base Vault/Definition/mdse-release.yaml").exists():
        raise ValueError("Release manifest leaked into generated vault")
    if (base / "00_Workspace").exists() or (base / "Importer").exists():
        raise ValueError("Tool/workspace source leaked into generated vault")
    if (base / ".git").exists():
        raise ValueError("Disposable uninitialized vault must not contain Git metadata")
    if (base / "EA_2026_09_06_endgame.qeax.zip").exists():
        raise ValueError("Source-model archive leaked into generated vault")
    identity = (base / ".vault.yaml").read_text(encoding="utf-8")
    if "vault_uid: UNINITIALIZED" not in identity or 'mdse_release: "0.8.0"' not in identity:
        raise ValueError("Generated identity unexpectedly initialized/released")
    plugins = lock["plugins"]
    enabled = json.loads((base / ".obsidian/community-plugins.json").read_text())
    if enabled != list(plugins):
        raise ValueError("Locked community plugin enablement changed")
    if plugins["mdse-workbench"]["version"] != "0.1.18":
        raise ValueError("Workbench 0.1.18 lock pin changed")
    plugin_counts = {}
    count = 0
    for pid,meta in plugins.items():
        manifest_path = base / ".obsidian/plugins" / pid / "manifest.json"
        plugin_meta = json.loads(manifest_path.read_text(encoding="utf-8"))
        if plugin_meta.get("version") != meta["version"]:
            raise ValueError("Plugin version mismatch for " + pid)
        reference = PAYLOAD_DIR / pid
        names = set(meta["sha256"])
        if not names or not names.issubset(set(TRACKED_PLUGIN_FILES)):
            raise ValueError("Unexpected pinned plugin files for " + pid)
        out_names = {f.name for f in (base / ".obsidian/plugins" / pid).iterdir() if f.is_file()}
        if out_names != names:
            raise ValueError("Packaged plugin file count/path mismatch for " + pid)
        for name,expected_sha in meta["sha256"].items():
            original = (reference / name).read_bytes()
            built = (base / ".obsidian/plugins" / pid / name).read_bytes()
            if digest(original) != expected_sha or digest(built) != expected_sha:
                raise ValueError("SHA-256 differs from pinned plugin lock: " + pid + "/" + name)
            check_equal(original,built,"Copied plugin " + pid + "/" + name)
            count += 1
        plugin_counts[pid]=len(names)
    if not (base / "README.md").is_file():
        raise ValueError("Generated README missing")
    if not (base / "99_System/03_Schemas/local-model.yaml").is_file():
        raise ValueError("Governed Local Model schema missing")
    return {
        "release": man["mdseRelease"],
        "releaseStatus": man["releaseStatus"],
        "vaultUid": "UNINITIALIZED",
        "sourceAndGeneratedGuideSha256": digest(guide),
        "userGuideByteExact": True,
        "lockByteExact": True,
        "pluginCount": len(plugins),
        "pluginFileHashesVerified": count,
        "pluginCounts": plugin_counts,
        "workspaceFilesExcluded": True,
        "qeaxArchiveExcluded": True,
        "guiAcceptancePerformed": False,
        "archiveApproved": False
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base",required=True)
    args=ap.parse_args()
    result=inspect(Path(args.base))
    print("STEP19_GENERATED_BASE="+json.dumps(result,sort_keys=True))
    print("STEP19_RELEASE_ISSUED=false")
    print("STEP19_OBSIDIAN_GUI_ACCEPTED=false")


if __name__ == "__main__":
    main()
