"""Classify *tracked* references to the former Workbench repository.

This is a narrow read-only classifier for release preflight, not a content
scanner or a certification that remote Git history/local machines are safe.
Unknown and altered references are never silently allowed.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

LEGACY_REPO = "/".join(("spencerskelly", "MDSE_Workbench"))

# These three complete file revisions have already been checked as frozen
# release provenance in the Step 08-09 reviews. An edit invalidates exemption.
PROVENANCE_BLOBS = {
    ".obsidian/plugin-lock.yaml": "c430670577318457972a154012d08c6d28e6d11b",
    "Base Vault/Tools/v0.8.0-r2/update-plugin-lock.py": "74f18af673263d87d123d31056251ddbab265d4b",
    "Base Vault/Tools/v0.8.0/update-plugin-lock.py": "e687515dad5215781df55a3cdfcb38008b0780f4",
}
CURRENT_DOCS = {
    "README.md", "AGENTS.md", "00_Workspace/README.md",
    "00_Workspace/00 - Current State.md",
    "00_Workspace/MDSE Tool Definitions and Boundaries.md",
    "55_Workbench/README.md", "55_Workbench/docs/INDEX.md",
    "55_Workbench/docs/Definition/04 - Architecture and Model Boundary.md",
    "Base Vault/Definition/mdse-release.yaml",
}
HISTORICAL_FILES = {
    "00_Workspace/Workspace Decision Log.md",
    "00_Workspace/GitHub Consolidation Recovery Inventory 2026-10-09.md",
    "55_Workbench/docs/bom/A01-A14_ORIGINAL_HANDOFF_ARCHIVE_VERIFICATION_2026-10-09.md",
    "55_Workbench/docs/bom/A01-A14_RECOVERY_STATUS_2026-10-09.md",
    "66_Testing/consolidation/STEP08_REFERENCE_DISPOSITIONS.json",
}
HISTORICAL_PREFIXES = (
    "00_Workspace/History/", "Importer/History/",
    "55_Workbench/docs/Reference/ARCHIVE_",
    "55_Workbench/docs/bom/a01-a14/",
    "00_Workspace/GitHub Consolidation Step ",
    "00_Workspace/Consolidation Step ",
)
EXECUTABLE_SUFFIXES = (".py", ".js", ".cjs", ".mjs", ".ts", ".tsx", ".sh",
                       ".ps1", ".yaml", ".yml", ".json", ".toml", ".ini")


def git_blob_sha(data: bytes) -> str:
    header = ("blob " + str(len(data)) + "\0").encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def classify(root: Path, relative_path: str) -> str:
    p = relative_path.replace("\\", "/").removeprefix("./")
    # Caller provides git-grep paths. Reject path traversal if used directly.
    if not p or p.startswith("/") or ".." in Path(p).parts:
        return "needs_review"
    if p in PROVENANCE_BLOBS:
        file_path = root / p
        try:
            data = file_path.read_bytes()
        except OSError:
            return "blocking"
        return ("verified_provenance" if git_blob_sha(data) == PROVENANCE_BLOBS[p]
                else "blocking")
    if p.startswith(".github/workflows/"):
        # GitHub Actions can be invoked: historical pinned checkout != inert file.
        return "blocking"
    if p in CURRENT_DOCS:
        return "blocking"
    if p in HISTORICAL_FILES or any(p.startswith(s) for s in HISTORICAL_PREFIXES):
        return "historical"
    if p.endswith(EXECUTABLE_SUFFIXES):
        return "blocking"
    return "needs_review"


def analyze(root: Path, matching_paths: list[str]) -> dict:
    categories = {"blocking": [], "needs_review": [],
                  "verified_provenance": [], "historical": []}
    for p in sorted(set(matching_paths)):
        categories[classify(root, p)].append(p)
    return {
        "schema": "mdse-workbench-references/1",
        "counts": {key: len(value) for key, value in categories.items()},
        "categories": categories,
        "strictReady": not (categories["blocking"] or categories["needs_review"]),
        "limitations": (
            "Tracked literal matches only; stored release provenance hashes are pinned. "
            "Historical workflow files remain blocking while under .github/workflows. "
            "No local clone, untracked file, dynamic URL, QEAX content, or external CI audited."
        ),
    }
