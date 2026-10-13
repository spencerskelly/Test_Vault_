# Branch Cleanup — Checkpoint BR-76: Disposable Base-Build Verification Procedure

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit PR: #41
Controlled input commit: `58ab10870f11757cf1bf367ecd5868be9b60933d`
Status: PROCEDURE READY, **NOT EXECUTED**. Does not grant release, GUI acceptance or merge permission.

## Purpose and guardrails

BR-73 verified the committed `55_Workbench/` bundle against the Workbench lock. BR-75 verified identical blobs in `Base Vault/Runtime/Plugins/mdse-workbench/`. BR-74 verified builder copy and release-checker verification code. This step closes the *procedural* gap with an exact-commit, non-destructive executable acceptance recipe. Do not confuse this with observed execution.

**Inputs:** complete local checkout of `spencerskelly/Test_Vault_` at exact SHA above; Python 3 and `PyYAML==6.0.2`; Git. Never unpack, open, upload, or transfer the historic public QEAX ZIP or real customer models for this test.

**Output:** new unique disposable directory created outside the repository by Python's `tempfile.mkdtemp`, with one generated clean Base, private diagnostic log and hashed Workbench Base artifact report. Preserve findings locally for review; do not automatically delete any directory or overwrite existing vault.

## Cross-platform runner (save outside checkout as `verify_step22_base.py`)

Run from a complete checked-out repository at the frozen SHA. On macOS use `python3 verify_step22_base.py`; on Windows use `py -3 verify_step22_base.py`. The script below is intended to be saved *outside* the repository; its own location does not define the repository root—use the current working directory.

```python
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path.cwd().resolve()
EXPECTED = "58ab10870f11757cf1bf367ecd5868be9b60933d"

def call(args, log):
    run = subprocess.run([str(x) for x in args], cwd=ROOT,
                         capture_output=True, text=True)
    log.write_text(run.stdout + "\n--- STDERR ---\n" + run.stderr,
                   encoding="utf-8")
    if run.returncode:
        raise RuntimeError(f"Command failed ({run.returncode}); inspect {log}")
    return run.stdout

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT,
                               text=True).strip()
if head != EXPECTED:
    raise SystemExit("STOP: checkout is not the approved frozen Step22 commit")
status = subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT,
                                 text=True)
if status.strip():
    raise SystemExit("STOP: use a clean checkout (no modified/untracked files)")

for p in ("Base Vault/Tools/v0.8.0-r2/build-base.py",
          "Base Vault/Testing/check-release.py",
          ".obsidian/plugin-lock.yaml"):
    if not (ROOT / p).is_file():
        raise SystemExit(f"STOP: missing controlled source file {p}")

out = pathlib.Path(tempfile.mkdtemp(prefix="mdse-br76-base-"))
base = out / "Clean_Uninitialized_Base"
summary = {"sourceCommit": head, "workspace": str(out),
           "builder": "NOT_RUN", "checker": "NOT_RUN",
           "runtimeHashes": {}, "guiExecuted": False,
           "releaseApproved": False}

try:
    call([sys.executable, ROOT / "Base Vault/Tools/v0.8.0-r2/build-base.py", base],
         out / "PRIVATE_BUILD.log")
    summary["builder"] = "PASS"
    report = call([sys.executable, ROOT / "Base Vault/Testing/check-release.py",
                   "--workbench", ROOT / "55_Workbench", "--base", base],
                  out / "PRIVATE_CHECK.log")
    # The checker exits 1 on FAIL. Keep warnings in PRIVATE_CHECK.log
    # and route them through release-owner disposition, not automatic approval.
    if "0 fail," not in report:
        raise RuntimeError("Checker did not report zero failures")

    import yaml
    lock = yaml.safe_load((ROOT / ".obsidian/plugin-lock.yaml").read_text(encoding="utf-8"))
    files = lock["plugins"]["mdse-workbench"]["sha256"]
    for filename, expected in files.items():
        vendored = ROOT / "Base Vault/Runtime/Plugins/mdse-workbench" / filename
        generated = base / ".obsidian/plugins/mdse-workbench" / filename
        source = ROOT / "55_Workbench" / filename
        actual = {"source": sha256(source), "vendored": sha256(vendored),
                  "generated": sha256(generated)}
        if any(h != expected for h in actual.values()):
            raise RuntimeError(f"Workbench digest mismatch for {filename}")
        summary["runtimeHashes"][filename] = actual
    summary["checker"] = "PASS"
except Exception as e:
    summary["failure"] = type(e).__name__ + ": " + str(e)
finally:
    (out / "PRIVATE_SUMMARY.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print("Private evidence location:", out)
    print("Builder:", summary["builder"], "Checker:", summary["checker"])
    print("Release approved: False; GUI executed: False")
if summary["builder"] != "PASS" or summary["checker"] != "PASS":
    raise SystemExit(1)
```

## Execution interpretation

1. `git rev-parse HEAD` must equal the exact frozen candidate SHA. `git status --porcelain` must be empty. Do not run over edited files or a different integration revision; do not force reset to achieve this.
2. Builder produces the new disposable Base outside the Git repository. A failed build leaves diagnostics for investigation; no automatic `rm -rf`.
3. Checker with both `--workbench` and `--base` must exit 0 and report **0 fail**. Record all WARN lines in local evidence; do not interpret a zero exit code as clearance of pre-release owner warnings.
4. Every `mdse-workbench` lock-listed file (currently main.js, manifest.json and styles.css) must match SHA-256 at three locations: 55_Workbench/, vendored payload/, and generated Base/.obsidian/plugins/.
5. Inspect generated `.vault.yaml`: `vault_uid` must remain `UNINITIALIZED` for a clean runtime Base. Do not initialize or open Obsidian during this mechanical test. The release checker must also detect generated-extra/missing-file and forbidden workspace path violations.
6. The private output folder's logs can contain host-specific file paths. Keep it local and scrub any excerpts shared to GitHub. Do not commit logs, Base artifacts or private session evidence.
7. **Failure handling:** retain the folder for diagnostics; re-run into a new disposable directory only after correcting a reviewed problem. Never delete anything in an existing user vault.
8. **Exit decision:** This check can demonstrate internally consistent, reproducible *copy/validation* at the source commit, but cannot approve MDSE 0.8.0, promotion of PR #39, actual GUI first-open, Local Model 0.5 real source import, or standalone Workbench archive.

## Evidence checklist

| Gate | Current evidence | Executed in BR-76 |
|---|---|---|
| 55_Workbench vs lock | BR-73 MATCH | no |
| Vendored Workbench vs source | BR-75 MATCH | no |
| Fresh generated Base | NOT YET BUILT | no |
| Checker with both flags | NOT RUN AT THIS STEP | no |
| Generated Base SHA-256 vs lock | NOT YET VERIFIED | no |
| Warning disposition | OWNER DECISION PENDING | no |
| Real macOS/Windows GUI acceptance | NOT RUN | no |

**NEXT BR-77:** If there is a complete isolated checkout, execute and capture sanitized pass/fail output. Otherwise inspect whether the current Base initialization contracts and manifest versions are consistent, without treating an unexecuted recipe as a test result.

No GitHub source code modified, PR approved/merged/closed, release promoted, branch deleted, QEAX opened or archive action taken.
