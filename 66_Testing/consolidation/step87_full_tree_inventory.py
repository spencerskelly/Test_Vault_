#!/usr/bin/env python3
"""Compare full Git tree metadata for four pinned refs, without reading blobs."""
import collections
import json
import subprocess
from pathlib import Path

REFS = {
    "main": "main",
    "step22": "consolidation/step22-single-repo-cutover-2026-10-11",
    "pr42": "integration/lean-test-infrastructure-20261013",
    "pr43": "integration/p03-legacy-compat-tests-20261013",
}

def git(*args):
    return subprocess.check_output(["git", *args])

def inventory(ref):
    raw = git("ls-tree", "-r", "-z", "--full-tree", ref)
    result = {}
    for item in raw.split(b"\0"):
        if not item:
            continue
        entry, path = item.split(b"\t", 1)
        mode, typ, sha = entry.decode("ascii").split(" ")
        result[path.decode("utf-8", "surrogateescape")] = [mode, typ, sha]
    return result

def main():
    trees = {key: inventory(ref) for key, ref in REFS.items()}
    all_paths = sorted(set().union(*(set(t) for t in trees.values())))
    categories = collections.Counter()
    rows = []
    for path in all_paths:
        byref = {k: trees[k].get(path) for k in REFS}
        unique = {tuple(v) for v in byref.values() if v is not None}
        present = [k for k, v in byref.items() if v is not None]
        if len(unique) > 1:
            cat = "divergent-existing"
        elif len(present) == 4:
            cat = "identical-all-four"
        elif len(present) == 1:
            cat = "single-ref"
        else:
            cat = "same-content-subset"
        categories[cat] += 1
        rows.append({"path": path, "category": cat, "refs": byref})
    out = {
        "refs": {key: {"ref": ref, "commit": git("rev-parse", ref).decode().strip(), "paths": len(trees[key])} for key, ref in REFS.items()},
        "total_paths": len(all_paths),
        "categories": dict(categories),
        "rows": rows,
    }
    folder = Path("66_Testing/consolidation/reports")
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "step87-full-tree.json").write_text(json.dumps(out, indent=2) + "\n")
    summary = ["# Step 87 — Complete Git tree classification", "",
               f"All distinct paths: {len(all_paths)}", "",
               "| Category | Paths |", "|---|---:|"]
    summary += [f"| {key} | {count} |" for key, count in sorted(categories.items())]
    summary += ["", "| Ref | Commit | Tracked paths |", "|---|---|---:|"]
    summary += [f"| {key} | \`{val['commit']}\` | {val['paths']} |" for key, val in out["refs"].items()]
    summary += ["", "## Divergent path count by directory", ""]
    roots = collections.Counter(r["path"].split("/", 1)[0] for r in rows if r["category"] == "divergent-existing")
    summary += [f"- {key}: {count}" for key, count in roots.most_common()]
    summary += ["", "## Important limitations",
                "- This is an exhaustive tracked-tree path/mode/type/blob-ID comparison at four fetched commits.",
                "- It is not a merge simulation or semantic equivalence test.",
                "- No file contents, including QEAX archives, are read.",
                "- Output is an artifact attached to this CI run; refs must be rechecked before any merge."]
    (folder / "step87-summary.md").write_text("\n".join(summary) + "\n")
    print("\n".join(summary))
    with open("/dev/stdout", "a") as f:
        pass

if __name__ == "__main__":
    main()
