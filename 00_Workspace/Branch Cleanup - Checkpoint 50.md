# Branch Cleanup — Checkpoint BR-50: Validated Base Handoff and Negative-Test Specification

**Date:** 2026-10-12  
**Repository:** `spencerskelly/Test_Vault_`  
**Audit PR:** #41  
**Candidate:** `consolidation/step22-single-repo-cutover-2026-10-11` @ `58ab10870f11757cf1bf367ecd5868be9b60933d`  
**Status:** DESIGN PROPOSAL — not implemented, executed, or approved for release.

## Basis and current behavior

BR-48 verified that `Base Vault/Tools/v0.8.0-r2/build-base.py` refuses nonempty destinations, uses manifest allowlists, then writes generated files, but can leave partially populated output after a late failure. BR-49 verified that `Base Vault/Initialization/Initialize-Vault.sh` and `Initialize-Vault.ps1` check the presence of `.vault.yaml`, `UNINITIALIZED`, release tag and author-code shape, but do **not** enforce an earlier successful `check-release.py --base` result. The existing `Bootstrap/Testing/Base First-Open Test Sheet.md` requires that validation operationally.

## Proposed release-owner handoff (separate controlled tool, NOT inside engineer vault)

1. Pin the full Git source SHA and manifest, lock and builder blob hashes. Reject a dirty/unverified authority checkout for reproducible release generation. Check that required inputs are available and approved to handle; do not fetch/read the QEAX archive by default.
2. Select a new, private disposable staging directory under an approved root. Refuse an existing nonempty destination. Never delete or overwrite user content automatically.
3. Run the existing `build-base.py` into disposable staging. On nonzero exit, stop and classify the output as `BUILD_FAILED`. Retain only safe diagnostics; do not present the staging path as a usable Base.
4. Run the existing `check-release.py --base STAGING` **only** after build success. Require checker exit 0; retain the numeric FAIL/WARN counts and review each warning. A zero exit with warnings is *not* automatic promotion authorization.
5. Produce an external, release-owner-only evidence receipt; hold the staged artifact pending review. Receipt fields: source commit SHA, manifest SHA, plugin-lock SHA, builder SHA, validator SHA, generated Base deterministic file-list+hash digest, builder exit, checker exit and counts, warning dispositions, operator approval record identifier, and timestamp. **Do not put this receipt inside the generated Base**, which has an exact allowlist.
6. Reverify all receipt-bound artifact hashes at the handoff boundary. Only after validated artifact and authorized review, produce a separately named initialization candidate. Prevent accidental reuse of unvalidated staging.
7. Execute `Initialize-Vault.sh` or `Initialize-Vault.ps1` only on the validated candidate and verify initialized `vault_uid`, unchanged `mdse_release`, and non-overwrite idempotence. Treat output as candidate/model repository, **not** released engineering vault.
8. Run macOS and Windows Obsidian first-open checks from the existing 21-row test sheet; separately run importer, Workbench/Bootstrap and fail-closed tests, and obtain document/W plus QEAX/local-contributor approvals before release.

## Suggested evidence receipt (design only, external private approval record)

```yaml
schema: mdse-base-handoff-evidence/1
source_commit: "<full verified Git SHA>"
release_manifest_blob: "<Git blob SHA>"
plugin_lock_sha256: "<SHA-256>"
builder_blob: "<Git blob SHA>"
checker_blob: "<Git blob SHA>"
artifact_tree_sha256: "<canonical relative-path + size + SHA-256 digest>"
build_exit: 0
check_release_exit: 0
failures: 0
warnings: 0
warning_review: "<approved review reference if nonzero warnings>"
status: VALIDATED_NOT_RELEASED
review_reference: "<private opaque approval ID>"
```

Canonical digest rules must be specified before implementation: normalize relative path separators to `/`; sort paths by bytewise UTF-8; hash exact file bytes; reject symlinks or define an explicit symlink/containment policy; exclude metadata timestamps; include path names, sizes and file digests in a length-delimited canonical stream. Do **not** assert deterministic digest parity across Windows and macOS until tested.

## Required negative/positive acceptance tests

| Case | Fixture / stimulus | Expected safety outcome |
|---|---|---|
| T01 | Destination exists and contains a sentinel file | Builder/wrapper refuses, sentinel unchanged |
| T02 | Missing late manifest-mapped source | Build fails; no `VALIDATED` receipt; no initialize |
| T03 | Missing locked plugin payload | Build fails; no accepted artifact |
| T04 | Tampered plugin payload or stale lock | Checker fails; receipt never `VALIDATED` |
| T05 | Added ungoverned extra generated Base file | Checker fails; no handoff |
| T06 | Forbidden workspace-only file leaks into artifact | Builder/checker rejects |
| T07 | `.vault.yaml` missing or incorrectly marked initialized | Initialization refuses without changing files |
| T08 | Corrupted/wrong `mdse_release` | Receipt/release checker rejects mismatched artifact before initialize |
| T09 | Invalid 13-character author code | POSIX and PowerShell refuse, `.vault.yaml` unchanged |
| T10 | Validated Base initialized once, then initialized again | First initializes; second refuses, UID unchanged |
| T11 | Source/lock/artifact changes after receipt | Handoff digest comparison rejects |
| T12 | Checker exit 0 with warnings | Review/approval required; no silent release |
| T13 | Forced write/copy/permission failure mid-build | Failed staging quarantined; downstream never sees it as validated |
| T14 | Symlink or out-of-root file in included trees | Explicit containment policy enforced; no out-of-root copying |
| T15 | Approved clean Base + valid author code | End-to-end Stage 1→2 succeeds, release unchanged; still NOT an issued vault |
| T16 | First-open on actual Mac and Windows Obsidian | Execute all 21 existing first-open rows with recorded pass/fail |

All fixtures should use synthetic, non-sensitive data and disposable directories; do not use a real QEAX model. Cross-platform tests must run under actual POSIX shell and PowerShell, not simulate one platform's parser.

## Implementation boundaries

**No unreviewed governance change.** First implement tests and a standalone wrapper proposal in a dedicated topic PR, not in release-controlled scripts silently. Prefer the wrapper to coupling initialization scripts to the entire methodology workspace, because generated Base deliberately excludes `mdse-release.yaml` and `check-release.py`. The wrapper can refuse initialization when no valid external receipt is present and bound to the exact artifact. Avoid a receipt-only checkbox not cryptographically bound to current contents.

A stricter atomic build design can follow once tests characterize failure behavior: staging + verify + safe rename/publish, protecting existing destination and ensuring no partially published output. Do not automatically delete failed staging or user files without approval.

## Reviewer signoff gates

- [ ] Release owner approves external evidence schema and trust boundary.
- [ ] Source-code owner approves wrapper/test implementation and handling of symlinks/permissions.
- [ ] Both initializer paths have negative tests (Mac and Windows).
- [ ] Builder and release checker pass on the same exact SHA with approved warning dispositions.
- [ ] No sensitive model archive included in build/tests.
- [ ] Actual operator first-open tests complete.
- [ ] Existing S1 QEAX confidentiality, S2 private local Git preservation and W/document approvals complete.
- [ ] Separate PR review and release/promotion authorization documented.

**BR-50 outcome:** Detailed, bounded implementation/test specification prepared; **no code or CI execution occurred**.

**NEXT BR-51:** Review and prioritize this proposed guard against the current stability program, or create a separate code PR when explicitly authorized; keep BR-50 as source-quality design evidence.

**No operations:** No release code changed, merge, PR closure, branch deletion, model download, archival action or release promotion.
