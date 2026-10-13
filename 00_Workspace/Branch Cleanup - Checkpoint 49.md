# Branch Cleanup — Checkpoint BR-49: Base Initialization and Bootstrap First-Open Handoff

**Date:** 2026-10-12
**Repository:** spencerskelly/Test_Vault_
**Audit PR:** #41
**Candidate:** consolidation/step22-single-repo-cutover-2026-10-11 @ 58ab10870f11757cf1bf367ecd5868be9b60933d
**Status:** STATIC SOURCE AND PROCEDURE REVIEW; no runtime modifications

## Evidence reviewed directly

| Source | Step22 Git blob |
|---|---|
| `Base Vault/Initialization/Initialize-Vault.sh` | `ff5ae878fb7086193a7546e73efc9d7541bcd98a` |
| `Base Vault/Initialization/Initialize-Vault.ps1` | `6009a25193ab81e44085f1540923dc4de4e631dc` |
| `Bootstrap/Testing/Base First-Open Test Sheet.md` | `ed666744a43f4de6d2a4ce6f3b37b035bac1587b` |
| `Bootstrap/Definition/README.md` | `44421c394e8548c3172ff12d24c5f9ce95593ad1` |

Related builder transactional-output risk: BR-48. Release-checker exact Base file set and hashes: BR-43/44.

## Verified initialization behavior

- POSIX initializer requires two args: display name and 13-character ASCII lowercase/dash author code; requires `.vault.yaml` and substring `UNINITIALIZED`; extracts `mdse_release`; writes a timestamp+author-code UID and preserves the release version, default branch and provided name.
- PowerShell initializer takes required `Name` and `AuthorCode`, checks the same author-code expression and basic `.vault.yaml`/release preconditions, then writes the initialized UID, name, branch and MDSE release.
- **Neither script calls `check-release.py --base`, checks a signed Stage-1 validation record, or checks all Base files/lock hashes before modifying `.vault.yaml`.**
- Both rely on `UNINITIALIZED` appearing somewhere in the current file, rather than parsing and verifying `vault_uid: UNINITIALIZED` specifically. The source text supports a guard-strengthening test proposal, but no exploit or production failure was reproduced in this pass.
- Both scripts are intended for one-time release-owner initialization on a validated clean artifact, NOT run by each engineer.

## Verified first-open contract

The `Base First-Open Test Sheet` explicitly requires a validated clean generated Base and successful `check-release.py --base` **before** release-owner initialization. Its 21 operator checks cover initial trust/enable, Bootstrap status, author registration and idempotence, typed note creation, Fileclass/Breadcrumbs, Git sync, Workbench diagnostics and plugin/hash drift behavior, including fail-closed handling of a disabled plugin with modified locked files.

The Bootstrap README defines:
- Active runtime Bootstrap `0.3.0`; candidate `0.3.1` staged and not auto-promoted.
- Safe activation repair enables only intact disabled locked plugins; it never downloads/replaces plugin files or silently overwrites governed settings.
- Release verification checks plugin versions and SHA-256 hashes, pinned plugin enablement, Obsidian version, core plugin settings, MDSE release, vault identity, Git state and author registration.
- Automatic full scan is deliberately deferred to a later startup lane; **manual Show release check performs immediate full verification**.
- First-open manual approval and governed W decision are needed before promoting a candidate Bootstrap payload.

## Concrete integration gap

**Documented procedure is sound, but initializer lacks an enforced Stage-1 proof.** Since the Base builder can leave partial output on late failure (BR-48), a partially built directory containing `.vault.yaml` could satisfy these initializer preconditions if the operator skips `check-release.py --base`. Bootstrap detection occurs only after the vault is initialized/opened and cannot substitute for the Stage-1 gate.

**Recommended proposed guard (NOT IMPLEMENTED):**
1. Add a release-owner wrapper/controlled handoff that runs a fresh Base builder and `check-release.py --base` on a disposable directory, requiring exit 0 and disposition of warnings before offering initialize.
2. Retain validation evidence with source SHA, generated Base tree digest, checker result, environment and timestamp in **approved release records outside the generated engineer vault**. Do not add ungoverned files to the Base include set.
3. Add cross-platform negative test cases: incomplete output, missing lock, altered plugin payload, absent `vault_uid: UNINITIALIZED`, previously initialized vault and invalid author code. Assert no initialization occurs and input remains unchanged on failure.
4. Retain the existing documented Stage 1 → Stage 2 → Stage 3 order and run the full 21-row first-open sheet on actual Mac and Windows Obsidian. Do not treat script unit tests as GUI acceptance.
5. Review PowerShell file encoding, YAML name escaping and parsing boundaries during implementation, without asserting those are observed defects until tested.

## Owner decisions and release holds

No change to `mdse-release.yaml`, importer/Workbench/Bootstrap source, schema or Workbench standalone archive in this audit. Developer convenience scripts must not be treated as release-authorized runtime changes without W governance. QEAX public exposure classification (BR-37) and private contributor local work (BR-38) remain independent blockers.

**BR-49 completed:** Verified both initialization sources and first-open contract; identified a concrete missing enforcement between Base validation and one-time initialization and proposed a testable non-invasive guard.
**NEXT BR-50:** Design an exact negative-test fixture and non-mutating release-owner wrapper proposal; choose controlled validation evidence format and safe boundary before editing code in a separate reviewed PR.
**NO ACTION:** No workflow change, initializer edit, artifact build, PR closure, merge, branch deletion, release promotion or repository archival.
