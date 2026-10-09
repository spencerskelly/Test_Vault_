#!/usr/bin/env python3
"""Read-only preflight for the proposed MDSE monorepo layout and release alignment.

Audit mode (default) reports candidate/pin drift and unmigrated paths but does
not promote versions or mutate any source. Strict mode is for a FUTURE release
gate, and rejects warnings or a pre-release manifest. Uses stdlib only.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "66_Testing" / "migration-path-plan.json"
MANIFEST = ROOT / "Base Vault" / "Definition" / "mdse-release.yaml"
PLUGIN_LOCK = ROOT / ".obsidian" / "plugin-lock.yaml"

def nested_block(text: str, name: str, indent: int) -> str:
    lines = text.splitlines()
    header = " " * indent + name + ":"
    start = next((i for i, s in enumerate(lines) if s.strip() == name + ":" and
                  len(s) - len(s.lstrip()) == indent), None)
    if start is None:
        raise ValueError("Missing YAML section: " + header)
    result = []
    for s in lines[start + 1:]:
        if s.strip() and not s.lstrip().startswith("#"):
            leading = len(s) - len(s.lstrip())
            if leading <= indent:
                break
        result.append(s)
    return "\n".join(result)

def scalar(text: str, name: str, indent: int | None = None) -> str | None:
    for line in text.splitlines():
        m = re.match(r"^(\s*)" + re.escape(name) + r":\s*(.*?)\s*(?:#.*)?$", line)
        if not m or (indent is not None and len(m.group(1)) != indent):
            continue
        v = m.group(2).strip().strip("\"'")
        return None if v in ("", "null", "~") else v
    return None

def read(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError("Missing required contract file: " + str(path.relative_to(ROOT)))
    return path.read_text(encoding="utf-8")

def grep_files(term: str) -> list[str]:
    command = ["git", "grep", "-I", "-l", "-F", "-e", term, "--", "."]
    p = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if p.returncode == 1:
        return []
    if p.returncode:
        raise RuntimeError("git grep failed: " + p.stderr.strip())
    return sorted(set(s.removeprefix("./") for s in p.stdout.splitlines()))

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", help="Write report JSON to this path")
    ap.add_argument("--strict", action="store_true",
                    help="Release mode: fail on pending migration, version drift or pre-release status")
    args = ap.parse_args()

    plan = json.loads(read(PLAN))
    manifest = read(MANIFEST)
    lock = read(PLUGIN_LOCK)
    wb_pkg = json.loads(read(ROOT / "55_Workbench" / "package.json"))
    wb_plugin = json.loads(read(ROOT / "55_Workbench" / "manifest.json"))

    report: dict = {
        "check": "mdse-monorepo-release-preflight",
        "mode": "strict" if args.strict else "audit",
        "authority": plan["releaseAuthority"],
        "versions": {},
        "roots": [],
        "dependencyReferences": {},
        "unregisteredWorkspaceDocs": [],
        "findings": [],
    }
    findings: list[dict] = report["findings"]

    def finding(level: str, code: str, detail: str) -> None:
        findings.append({"severity": level, "code": code, "detail": detail})

    for row in plan["roots"]:
        src, dst = row["source"], row["target"]
        source_exists = bool(src and (ROOT / src).exists())
        target_exists = (ROOT / dst).exists()
        disposition = ("retain" if src == dst else
                       "migrated" if target_exists and not source_exists else
                       "pending" if not target_exists else
                       "collision" if source_exists and target_exists else
                       "missing")
        report["roots"].append({"from": src, "to": dst, "state": disposition,
                                "policy": row["policy"]})
        if disposition in ("collision", "missing"):
            finding("error", "ROOT_INVALID", str(src) + " -> " + dst + ": " + disposition)
        elif disposition == "pending":
            finding("warning", "ROOT_PENDING", str(src) + " -> " + dst + " not moved/created")
    if (ROOT / "Cross-Vault").exists():
        finding("warning", "CROSS_VAULT_UNRESOLVED",
                "Cross-Vault still needs explicit classification, not automatic relocation to 88_Resources")

    schemas = nested_block(manifest, "schemas", 0)
    tools = nested_block(manifest, "tools", 0)
    wb = nested_block(tools, "workbench", 2)
    importer = nested_block(tools, "importer", 2)
    bootstrap = nested_block(tools, "bootstrap", 2)
    lock_wb = nested_block(nested_block(lock, "plugins", 0), "mdse-workbench", 2)
    lock_bootstrap = nested_block(nested_block(lock, "plugins", 0), "mdse-bootstrap", 2)

    status = scalar(manifest, "releaseStatus", 0)
    wb_pin = scalar(wb, "version", 4)
    wb_candidate = scalar(wb, "candidateVersion", 4)
    wb_locked = scalar(lock_wb, "version", 4)
    bootstrap_pin = scalar(bootstrap, "version", 4)
    bootstrap_lock = scalar(lock_bootstrap, "version", 4)
    schema_files = {
        "relationships": "relationships.yaml",
        "elementTypes": "element-types.yaml",
        "localModel": "local-model.yaml",
    }
    versions = {
        "releaseStatus": status,
        "mdseRelease": scalar(manifest, "mdseRelease", 0),
        "workbench": {
            "releasePin": wb_pin, "manifestCandidate": wb_candidate,
            "pluginLock": wb_locked, "importedPackage": wb_pkg.get("version"),
            "importedManifest": wb_plugin.get("version"),
        },
        "bootstrap": {"releasePin": bootstrap_pin, "pluginLock": bootstrap_lock,
                      "candidateSource": scalar(bootstrap, "candidateSource", 4)},
        "importer": {"releaseCandidate": scalar(importer, "candidate", 4),
                     "releasePin": scalar(importer, "release", 4)},
        "schemas": {},
    }
    report["versions"] = versions

    if wb_pkg.get("version") != wb_plugin.get("version"):
        finding("error", "WORKBENCH_SOURCE_METADATA",
                "55_Workbench package.json and manifest.json versions differ")
    if wb_pin != wb_locked:
        finding("warning", "WORKBENCH_RELEASE_LOCK_DRIFT",
                "Workbench release pin " + str(wb_pin) + " != generated lock " + str(wb_locked))
    if wb_pkg.get("version") != wb_pin:
        finding("warning", "WORKBENCH_CANDIDATE_NOT_PROMOTED",
                "Imported Workbench " + str(wb_pkg.get("version")) +
                " differs from declared release pin " + str(wb_pin))
    if wb_candidate != wb_pkg.get("version"):
        finding("warning", "WORKBENCH_CANDIDATE_RECORD_STALE",
                "Manifest candidate " + str(wb_candidate) +
                " differs from imported source " + str(wb_pkg.get("version")))
    if bootstrap_pin != bootstrap_lock:
        finding("warning", "BOOTSTRAP_RELEASE_LOCK_DRIFT",
                "Bootstrap manifest pin " + str(bootstrap_pin) +
                " != generated plugin lock " + str(bootstrap_lock))

    for key, filename in schema_files.items():
        declared = scalar(schemas, key, 2)
        actual = scalar(read(ROOT / "99_System" / "03_Schemas" / filename), "schemaVersion", 0)
        versions["schemas"][key] = {"releasePin": declared, "schemaFile": actual}
        if actual != declared:
            finding("warning", "SCHEMA_VERSION_DRIFT", filename + ": " +
                    str(actual) + " != manifest " + str(declared))

    if status != "release":
        finding("warning", "NOT_RELEASED", "Manifest status is " + str(status) +
                ", so Workbench standalone tests are not integrated-release approval")

    # This register is used by the existing release checker to decide whether
    # new workspace documentation is authoritative and complete.
    registered = set(re.findall(r'\{path:\s*["\x27]([^"\x27]+)', manifest))
    for p in sorted((ROOT / "00_Workspace").glob("*.md")):
        if p.name == "README.md":
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel not in registered:
            report["unregisteredWorkspaceDocs"].append(rel)
    if report["unregisteredWorkspaceDocs"]:
        finding("warning", "DOCUMENT_REGISTRY_PENDING",
                str(len(report["unregisteredWorkspaceDocs"])) +
                " workspace Markdown files missing from release-manifest documents registry")

    # Count *tracked textual* references that need relocation, not just paths.
    # Includes history/doc references for later disposition. This is a lower
    # bound: dynamic path construction, binaries, and Obsidian links require
    # additional tool-specific checks before any directory move.
    terms = ["Definitions/", "Importer/", "Base Vault/", "Bootstrap/", "Cross-Vault/",
             "spencerskelly/MDSE_Workbench"]
    for term in terms:
        matches = grep_files(term)
        report["dependencyReferences"][term] = {
            "trackedFiles": len(matches), "examples": matches[:10]
        }
    for term in terms:
        info = report["dependencyReferences"][term]
        print("DEPENDENCY", repr(term), info["trackedFiles"], "tracked files",
              "| examples:", ", ".join(info["examples"][:3]))
    if any(report["dependencyReferences"][k]["trackedFiles"] for k in terms):
        finding("warning", "OLD_PATH_REFERENCES",
                "Legacy references remain in tracked files; see dependencyReferences; " +
                "do not move folders without patching verified consumers")

    print("MDSE consolidated release preflight:", args.strict and "STRICT" or "AUDIT")
    print("Manifest state:", status, "| Workbench pinned:", wb_pin,
          "| Workbench source:", wb_pkg.get("version"))
    for f in findings:
        print(f["severity"].upper(), f["code"], f["detail"])
    print("Root map:", len(report["roots"]), "| Findings:", len(findings))
    print("Unregistered workspace docs:", len(report["unregisteredWorkspaceDocs"]))

    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    errors = sum(f["severity"] == "error" for f in findings)
    warnings = sum(f["severity"] == "warning" for f in findings)
    if errors or args.strict and warnings:
        return 1
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, RuntimeError, KeyError) as exc:
        print("ERROR release preflight:", exc, file=sys.stderr)
        sys.exit(2)
