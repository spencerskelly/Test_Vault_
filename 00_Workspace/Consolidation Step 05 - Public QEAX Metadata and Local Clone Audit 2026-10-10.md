# Consolidation Step 05 — Public QEAX metadata exposure and local-clone audit kit

**Date:** 2026-10-10  
**Status:** METADATA VERIFIED; QEAX CONTENT CLASSIFICATION AND LOCAL-WORKSTATION AUDIT STILL OPEN. **DO NOT ARCHIVE OR PROMOTE.**  
**Baseline:** `spencerskelly/Test_Vault_` consolidation Step 04 commit `212602377fb71a634a36bde57e5aa886e8d5b4c1`.  
**Related machine-readable evidence:** `66_Testing/consolidation/public-qeax-metadata-2026-10-10.json`.

## 1. Verified GitHub metadata only (no model extraction)

- GitHub reports `spencerskelly/Test_Vault_` is **public**, default branch `main`.
- Exact file path `EA_2026_09_06_endgame.qeax.zip` is a tracked file on the public consolidation staging branch, size **73,184,128 bytes** (~73.2 decimal MB).
- Git **blob** SHA reported by GitHub: `513b2d2d4696b1502fe482424f7c05985442e2b9`. This is a Git object identifier, **not** a verified SHA-256 digest of extracted QEAX contents.
- GitHub path-history query identifies commit `2f7c93ffed265349d599fc89efbc85fc7a46dd5e`, timestamp **2026-10-06T00:03:16Z** (October 5 local Pacific time), message `add qeax`.
- The ZIP path is **absent at the checked current `main` root**, commit `19f565859e4b9fb7ae63004f1b6f0a7de1b9144e`. This does **not** negate public visibility of the staging branch and its Git history.
- **No archive bytes were opened, downloaded, unzipped, copied or redistributed during this Step 05 inspection.** Repository API *metadata* was queried.

**Confidentiality: UNKNOWN.** Neither file size, suffix, nor public visibility establishes whether the archive contains restricted Ampure/source design data, individuals' information, credentials or other sensitive content. Only the authorized data owner/security reviewer can classify and approve publication. Do not imply such contents are present without inspection, and do not claim the archive is cleared for publication.

### Required owner/security decision

Record one of: `APPROVED_FOR_PUBLIC_RELEASE`, `RESTRICTED_REMEDIATION_REQUIRED`, or `PENDING_REVIEW` (current: `PENDING_REVIEW`). Require the reviewer, review date, approved source version/digest and disposition/remediation ticket in the **appropriate controlled/private system**; do not create a public record of sensitive findings. If restricted, coordinate exposure response for **public branch history and possible forks/caches**, not merely deletion from `main` or the latest branch tip. If actual secrets are found, follow incident procedures (including revocation/rotation) rather than relying on history rewriting alone.

**Stop:** No public-main merge, branch-history cleanup, repository archival or wider dissemination based on this metadata-only review.

## 2. Read-only local clone audit tools

Two candidate scripts are now preserved under `66_Testing/consolidation/`:

- `audit_local_git.sh` — macOS/Linux POSIX shell, tested locally on a **disposable** Git repository (shell syntax and dirty/untracked/no-upstream detection PASS).
- `audit_local_git.ps1` — Windows PowerShell 5.1+ syntax-reviewed, **not executed** in this environment because PowerShell was unavailable.

Both scripts only invoke local Git read commands; they **do not fetch, clean, reset, commit, push, upload, write reports to disk, open note/model contents or report working-file paths**. They print an abbreviated audit of HEAD, current branch, dirty/untracked entry counts, local branches, upstream comparisons, stashes, worktrees, and whether the clone is shallow. Branch names appear in the output; keep results private until redacted.

### Usage on every machine with a Workbench or Test_Vault_ clone

macOS/Linux (run script from a trusted checkout):

```sh 66_Testing/consolidation/audit_local_git.sh "/path/to/MDSE_Workbench"
sh 66_Testing/consolidation/audit_local_git.sh "/path/to/Test_Vault_"```

Windows PowerShell:

```powershell -NoProfile -File .\66_Testing\consolidation\audit_local_git.ps1 -Path "C:\path\to\MDSE_Workbench"
powershell -NoProfile -File .\66_Testing\consolidation\audit_local_git.ps1 -Path "C:\path\to\Test_Vault_"```

The scripts are on an **unmerged branch**. Obtain them via this branch/PR or the local checkpoint package, not by assuming they are on `main`.

For each contributor, record privately: machine/clone audited, current HEAD, each branch lacking an upstream, any ahead commits, dirty or untracked work, stash count, extra worktrees and review disposition. **Do not submit unredacted local audit logs or proprietary file paths to a public repository.**

### Accuracy limits

- Counts are relative to the machine's **last-fetched remote-tracking refs**; no network fetch occurs. `AHEAD=0` is **not proof of synchronization with current GitHub**.
- Ignored files, other local clones, remote-only branches, full stash contents, non-Git work files, sparse-checkout excluded contents and confidential files not represented by Git are **not** inspected.
- For branches with `UPSTREAM=NONE`, further human classification is mandatory.
- In a separate approved session, the owner can update remote-tracking refs, take a safe backup and compare local work against the authoritative remote; no automatic changes or deletion are authorized here.
- Audit status is **not complete** until every active development machine/clone is inventoried and signed off.

## 3. Step 05 verification and scope

| Check | Result |
|---|---|
| Public repo and archive metadata | Verified by connected GitHub API |
| Archive present at checked public staging tip | Yes |
| Archive absent from current `main` tip | Yes |
| Historical path introduction | GitHub records `2f7c93ffe...` |
| ZIP opened or classified | **No; PENDING** |
| POSIX shell syntax and disposable smoke test | **PASS** |
| PowerShell execution test | **NOT RUN** (runtime unavailable) |
| Every local workstation audited | **NO** |
| Changes to `main`, active schema/CI, production runtime | **NONE in this checkpoint** |

## 4. Next consolidation step

Resolve the **owner classification** of the QEAX archive and run the local-clone audits. While these gates remain open, subsequent development may continue on a review-only isolated branch **without** public-main merge or production release. Next bounded actionable step is Step 06: verify the read-only audit scripts on further edge cases, produce a per-machine sign-off register, and prepare the exact migration change set (not an unapproved schema or release edit). The standalone `MDSE_Workbench` repository remains unarchived.

**Principle:** Preserving Git history for migration is compatible with preventing unapproved deployment; it is not by itself a claim that public history is safe.
