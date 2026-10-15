# Consolidation Step 06 — Local Git audit hardening and sign-off framework

**Date:** 2026-10-10
**Status:** Source/checkpoint prepared for isolated GitHub review. **No real workstation audit, repository archive, schema approval, release, or `main` merge.**

## Baseline and change scope

Base: `spencerskelly/Test_Vault_` `consolidation/step05-qeax-security-local-clone-audit-2026-10-10`, commit `864532d13bdbd62be7afcfaad182921bf99191e8` (Step 05 / draft PR #22). Step 06 changes only the read-only Bash/POSIX and Windows PowerShell audit scripts under `66_Testing/consolidation`, and adds a reusable test script, blank sign-off template, and this checkpoint.

## Improvements to both script candidates

- Set `GIT_OPTIONAL_LOCKS=0` so a read-only audit avoids optional index refresh/write locks.
- Fail closed on invalid/unborn HEAD and status failure.
- Explicitly mark the audit **not certified**: local refs can be stale without an approved fetch, and a valid zero-ahead count is not publication evidence.
- Record `REMOTE_COUNT`, detached HEAD review, shallow state, dirty tracked/untracked counts, branch count, stash count and linked worktree count (never print file content or file paths).
- Classify every branch: no upstream, missing/unresolvable upstream, local-only upstream, ahead, behind, diverged, or apparently equal to local remote-tracking state.
- Parse branch names one per line, not `|`-separated Git fields (a valid branch name can include `|`). Git branch names cannot contain newlines.
- Treat any unusual condition as requiring manual review, not as permission to clean/reset, copy, fetch or archive.

## Verification evidence

- POSIX script: `sh -n` and `bash -n` (PASS).
- POSIX script: **15/15** offline automated disposable Git scenarios (PASS), including no upstream, local upstream, detached HEAD, ahead, behind, diverged, missing upstream reference, stash, additional worktree, shallow clone, newline-containing untracked filename, branch containing pipe (`|`), unborn repo, invalid path, staged/unstaged single entry and clean remote tracking.
- Index-immutability check: compare the disposable repo Git index bytes and modification timestamp before and after the script (PASS).
- PowerShell: manual/static review only. **Windows execution NOT RUN** — `pwsh`/`powershell` not installed in test environment. Run controlled Windows acceptance before citing it as verified.
- Tests generate local disposable commits/remotes/fetches for fixture setup; **the audit scripts themselves** use only local read commands and never call fetch/push/commit/reset/clean.

## Audit result limitations

- A branch marked `REMOTE_TRACKING_ONLY_NOT_VERIFIED` can still have unpublished work because remote-tracking refs may be stale. A separate owner-approved comparison to current GitHub is required.
- Current tests do not audit actual contributor workstations or the contents of stashes, ignored files, submodules, orphaned/unreferenced Git objects, other clones, or external non-Git files.
- Script output includes local branch names and repository directory basename. Completed reports must be reviewed/redacted and stored privately, never dumped into a public PR.
- Git object and SHA references are technical traceability, not evidence of QEAX content confidentiality or publication permission.

## Remaining gates and next task

1. Distribute the audit kit to each contributor; execute with actual cloned working directories; review all flagged work and separately establish current remote state after preserving local work.
2. Execute the PowerShell candidate on representative Windows Git installations; revise only via a controlled candidate and tests.
3. Complete private workstation register with owner/approver sign-offs. Current completed count: **0**.
4. Source archive `EA_2026_09_06_endgame.qeax.zip` is confirmed present in public branch history; content confidentiality remains **unassessed**. Owner/security decision required before public `main` consolidation.
5. Prepare the Step 07 exact ownership/CI cutover patch for separate review; keep release manifest pins, `.obsidian` plugin lock, schema 0.5 writer and production runtime unchanged until approval.
6. Integrate A-15.1–A-15.4 candidate code through Workbench full test/build and real Obsidian GUI acceptance before archiving the standalone repository.

**Next bounded action:** Step 07 — review-only atomic migration diff and negative test suite for active-vs-historical legacy repository references; no main merge, release promotion or standalone archive.
