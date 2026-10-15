#!/usr/bin/env python3
"""Read-only audit of tracked files in the current Git commit.

Uses git ls-tree (not a capped GitHub comparison). Emits deterministic JSON.
Exit 2 means tracked files require human review; no files are modified.
"""
import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

MODEL_EXTENSIONS = (".qea", ".qeax", ".eap", ".eapx", ".qea.zip", ".qeax.zip")
MODEL_DIRS = re.compile(r"(^|/)(imported[_ -]?model|generated[_ -]?vault|real[_ -]?model|ea[_ -]?export|model[_ -]?output)(/|$)", re.I)
GENERATED_DIRS = re.compile(r"(^|/)(node_modules|__pycache__|\.pytest_cache|dist|build)(/|$)", re.I)
SYNTHETIC = re.compile(r"(synthetic|fixture|sample|mock|tiny|toy)", re.I)

def inventory(ref):
    raw = subprocess.check_output(["git", "ls-tree", "-r", "-l", "-z", ref])
    for row in raw.split(b"\0"):
        if not row:
            continue
        meta, name = row.split(b"\t", 1)
        mode, kind, sha, size = meta.decode().split()
        yield {"path": name.decode("utf-8", "surrogateescape"),
               "bytes": int(size) if size.isdigit() else None,
               "mode": mode, "sha": sha, "kind": kind}

def categorize(entry):
    path = entry["path"]
    lower = path.lower()
    suffix_risk = lower.endswith(MODEL_EXTENSIONS)
    directory_risk = bool(MODEL_DIRS.search(path))
    if suffix_risk or directory_risk:
        return "review_model_data" if SYNTHETIC.search(path) else "suspected_real_model_data"
    if GENERATED_DIRS.search(path):
        return "generated_dependency"
    if lower.startswith((".github/", "66_testing/")) or "/testing/" in lower or "/tests/" in lower:
        return "testing_ci"
    if lower.endswith((".md", ".yaml", ".yml", ".json", ".txt", ".rst")):
        return "documentation_definition_or_config"
    return "source_or_other"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", default="HEAD", help="Git ref to inspect, default HEAD")
    parser.add_argument("--output", help="Write JSON to this path (otherwise stdout)")
    args = parser.parse_args()
    entries = list(inventory(args.ref))
    categories = Counter()
    bytes_by_category = Counter()
    flagged = []
    largest = sorted((x for x in entries if x["bytes"] is not None),
                     key=lambda x: (-x["bytes"], x["path"]))[:25]
    for entry in entries:
        category = categorize(entry)
        categories[category] += 1
        bytes_by_category[category] += entry["bytes"] or 0
        if category in ("suspected_real_model_data", "review_model_data", "generated_dependency"):
            flagged.append({"category": category, **entry})
    report = {
        "ref": args.ref, "tracked_files": len(entries),
        "tracked_blob_bytes": sum(x["bytes"] or 0 for x in entries),
        "category_counts": dict(sorted(categories.items())),
        "category_bytes": dict(sorted(bytes_by_category.items())),
        "flagged": sorted(flagged, key=lambda x: x["path"]),
        "largest_25": largest,
        "limitations": [
            "Checks only files tracked by the selected Git tree, not previous history or Git LFS payload sizes.",
            "Path-based flags are candidates for manual review, not proof that contents are real imported model data.",
            "A clean report is not proof that human-readable Markdown lacks copied model data.",
        ],
    }
    output = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 2 if any(x["category"] != "generated_dependency" for x in flagged) else 0

if __name__ == "__main__":
    sys.exit(main())
