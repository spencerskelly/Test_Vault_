"""Enumerate full tracked Workbench tree and audit P04 sparse CI inclusion.

Read-only. Requires repository checkout with Git metadata; outputs JSON to stdout.
No repository modifications and no model contents read.
"""
import json
import subprocess
from collections import Counter

ROOT = "55_Workbench/"
PREFIXES = ("src/", "test/", "bench/", "scripts/")
EXACT = {"package.json", "package-lock.json", "tsconfig.json",
         "esbuild.config.mjs", "manifest.json", "styles.css"}

def run():
    raw = subprocess.check_output(
        ["git", "ls-tree", "-r", "-z", "--name-only", "HEAD", "--", ROOT])
    paths = sorted(p.decode("utf-8") for p in raw.split(b"\0") if p)
    relative = [p[len(ROOT):] for p in paths]
    tracked_inputs = [p for p in relative
                      if p.startswith(PREFIXES) or p in EXACT]
    excluded = [p for p in relative if p.startswith("vault/")]
    workspace_only = [p for p in relative if p not in tracked_inputs
                      and not p.startswith("vault/")]
    counts = Counter(p.split("/")[0] for p in relative)
    # Audit the exact tracked source tree, including files unchanged from main.
    # Checkout can be sparse, but the commit tree metadata remains authoritative.
    report = {
        "commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True).strip(),
        "total_workbench_paths": len(paths),
        "source_checkout_candidates": len(tracked_inputs),
        "historic_vault_paths_excluded": len(excluded),
        "other_review_paths": len(workspace_only),
        "top_level_counts": dict(sorted(counts.items())),
        "source_checkout_paths": tracked_inputs,
        "other_review_paths_list": workspace_only,
        "historical_vault_pathnames_listed": False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if not any(x.startswith("src/") for x in tracked_inputs):
        raise SystemExit("Missing Workbench source tree")
    if not any(x.startswith("test/") for x in tracked_inputs):
        raise SystemExit("Missing Workbench test tree")
    if "package-lock.json" not in tracked_inputs:
        raise SystemExit("Missing lockfile")

if __name__ == "__main__":
    run()
