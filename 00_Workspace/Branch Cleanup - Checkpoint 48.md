# Branch Cleanup — Checkpoint BR-48: Generated Base Builder Quality Review

**Date:** 2026-10-12
**Repository:** spencerskelly/Test_Vault_
**Audit PR:** #41
**Candidate:** consolidation/step22-single-repo-cutover-2026-10-11 @ 58ab10870f11757cf1bf367ecd5868be9b60933d
**Status:** STATIC SOURCE REVIEW — no generated vault built or modified in this step

## Verified source
- `Base Vault/Tools/v0.8.0-r2/build-base.py`, exact Git blob `67af4b69ea76a22b97db8851bd54ddc560b15784` on Step22.
- `Base Vault/Testing/Candidate Model Repository Preparation.md`, exact Git blob `77525b687b20127f07bb02f74ea9e582fde5e98f` on Step22.
- Corresponding release-checker implementation and optional `--base` scope verified in BR-43/44.

## Positive controls implemented in builder
1. Checks output target: if it exists but is not a directory, exit; if nonempty, refuse overwrite. Otherwise creates output directory.
2. Uses `runtimeBase` positive manifest entries: `includeFiles`, `mappedFiles`, `includeTrees` and `conditionalFiles`; source missing raises failure.
3. Excludes `.git` directories in included trees and ignores `.DS_Store`/`Thumbs.db` in copy_tree.
4. Reads plugin-lock schema 2, copies only named plugin runtime payload members (`main.js`, `manifest.json`, `styles.css`, `data.json`).
5. Writes generated `.gitignore`, `.vault.yaml` with `vault_uid: UNINITIALIZED`, and a release/version-specific README.
6. Checks manifest-listed `forbiddenPaths` for output leakage and validates Bootstrap availability / required WB-106-capable plugin lock condition for issued releases.

## Concrete quality issue — partial output on late failure

The script creates/populates the requested output directory **before** verifying every required source, plugin payload and final forbidden-path condition. A late `FileNotFoundError`, missing payload, or final `sys.exit` can leave an incomplete directory at the requested output path. There is no staging-directory + atomic publish/cleanup/rollback mechanism in this implementation.

- **Risk:** An operator or follow-on script could mistake existence of the generated directory for a successful build. The script's nonempty-output guard would prevent a simple retry at the same location, forcing manual cleanup/rebuild; never run a destructive cleanup automatically against a user-selected path.
- **Current mitigation:** Stage 1 of `Candidate Model Repository Preparation.md` already requires `check-release.py --base <folder>` with zero failures and `UNINITIALIZED` identity. The checker verifies an exact file set and hashes, rather than mere directory existence.
- **Proposed improvement (NOT IMPLEMENTED):** Create in a new controlled temporary sibling, validate exact output with release checker, then publish/rename to user-specified output only on success. Explicitly refuse nonempty destination and preserve diagnostic logs on failure without deleting user content. A safer first increment is a new negative regression test for missing included file, missing plugin payload, and permission/copy failure, asserting nonzero exit and no accepted/published output marker.
- **Separate potential review:** The builder uses `shutil.copy2` and walks includeTrees; assess source-tree symbolic links and containment before releasing on mixed Mac/Windows workstations. No symlink exploit or bad source tree is established by this audit.

## Required pass/fail test matrix

| Test | Expected |
|---|---|
| Existing nonempty destination | Build fails, old files unchanged |
| Fresh empty destination with all sources | Builder exits 0, checker `--base` exits 0 with approved warning dispositions |
| Missing late source include or plugin payload | Builder exits nonzero; no incomplete output may be accepted by downstream handoff |
| Workspace-only forbidden path present | Builder/validator rejects |
| Modified vendored plugin bytes | Checker detects SHA-256 lock mismatch |
| Extra unexpected file in generated Base | Checker `--base` rejects |
| Clean new Base initialized later | Release-owner workflow only; not a builder step or CI auto-promotion |

## Release and authority boundaries

Static inspection is not successful test execution. No build was run; no source or workflow was edited; any builder refactor or negative test must be separately proposed and reviewed. Preserve current `releaseStatus: pre-release`. Stage 2 model repository remains subject to importer/Workbench alignment and real Obsidian GUI acceptance, plus QEAX security and local contributor gates.

**BR-48 disposition:** Builder has useful manifest-driven controls; concrete partial-output transactionality gap documented with safe negative-test proposal.

**NEXT BR-49:** Trace generated Base failure handling into its existing initializer and Bootstrap first-open procedure and prioritize one testable integration guard, without editing release-controlled code unless explicitly authorized.

**NO ACTION:** No PR merges, closures, branch deletions, model downloads, releases or archives.
