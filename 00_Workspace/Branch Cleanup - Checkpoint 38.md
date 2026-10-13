# Branch Cleanup — Checkpoint BR-38: Private Local Git Signoff Protocol

**Date:** 2026-10-12  
**Repo:** `spencerskelly/Test_Vault_`  
**Audit PR:** #41  
**Gate:** S2 — contributor-local unpublished work  
**Status:** PROCEDURE READY / **0 contributor signoffs verified in this checkpoint**  
**Safety:** Non-destructive instructions only. No local user machine was accessed.

## Purpose

The remote ancestry reviews show that many historical GitHub branch *tips* are already reachable from Step22. Remote evidence **cannot** establish whether a contributor has unpushed commits, untracked files, local branches, active worktrees, stashes, unpublished tags or detached-HEAD work. Those must be inspected **privately by each contributor** before source repository archival, branch deletion or PR closure. This gate is independent of QEAX confidentiality (S1) and governance/release acceptance.

## Step-by-step operator procedure (private workstation only)

1. **Inventory scope:** List every local clone of `Test_Vault_` and standalone `MDSE_Workbench`, including any extra worktrees and test/disposable clones. Explicitly state the machines and repos checked, privately; do not treat one clone as all machines.
2. **Freeze risky actions:** Do not run `git clean`, `git reset --hard`, force push, prune, delete branches, `stash clear`, or remove a worktree during inventory. Do not run a local audit script from an untrusted repository without reviewing it.
3. **Run existing read-only audit:** Use the audited POSIX/PowerShell tools from PR #23, installed in the approved checkout, following their documented arguments. The documented scripts set `ARCHIVE_SIGNOFF=NOT_CERTIFIED` regardless of results; they do not fetch and can have stale remote tracking refs. **Windows PowerShell execution remains unverified by this audit.**
4. **Check manually, inside each clone, with read-only Git commands:**
   ```sh
   git status --short --branch
   git branch -vv
   git worktree list --porcelain
   git stash list
   git log --all --oneline --decorate -n 30
   git remote -v
   git rev-parse --is-shallow-repository
   ```
   Avoid public posting of raw output; it may contain usernames, private local paths, remote URLs and sensitive file names.
5. **Check local-only Git history:** Confirm each local branch's actual upstream and freshness *privately*; inspect unpushed/unreachable commits with local comparisons appropriate to that clone. `git branch -vv` ahead/behind is only as current as the local tracking refs. Do not presume a missing upstream means no unpublished work. Inspect detached HEADs, orphan commits, stashes and uncommitted/untracked files.
6. **Classify every finding:** `PRESERVED_IN_APPROVED_GIT_HISTORY`, `PRESERVED_IN_PRIVATE_APPROVED_BACKUP`, `IN_PROGRESS_HOLD`, or `REQUIRES_OWNER_DECISION`. Do not upload private unpublished work to public GitHub merely to make the audit pass.
7. **Protect needed work:** Arrange owner-approved backup or reviewed PR intake without overwriting the source. Verify actual commit SHA or backup integrity and recovery ability. Keep sensitive work inside approved private storage.
8. **Second-person review:** Have the contributor and a designated repository/data owner verify inventory completeness, safe preservation and that no unreviewed local work could be lost by the *specific* proposed cleanup batch.
9. **Only then sign off:** Retain detailed private evidence under an approved record; publish only aggregate status and a non-sensitive opaque approval reference. Repeat if work changes before deletion/archival.

## Public-safe ledger (no contributor identities or machine paths)

| Scope | Required private audits | Verified complete | State | Non-sensitive record |
|---|---|---|---|---|
| `Test_Vault_` active contributor clones/worktrees | Unknown — owner to determine | 0 in this checkpoint | NOT_CERTIFIED | Pending |
| `MDSE_Workbench` historic/contributor clones/worktrees | Unknown — owner to determine | 0 in this checkpoint | NOT_CERTIFIED | Pending |
| Windows PowerShell audit behavior | Approved Windows execution/test evidence | None verified here | NOT_VERIFIED | Pending |
| Stashes/untracked/unpushed/detached history | All scoped checkouts | 0 in this checkpoint | NOT_CERTIFIED | Pending |
| Batch-specific deletion / standalone archival approval | Owner review after evidence | None | HOLD | Pending |

Do not enter names, raw `git remote -v` output, absolute home directories, logs with file contents, credentials, protected model data or personally identifying information in this public ledger.

## Conditions to pass S2

- Owner confirms **all relevant machines and clones** inventoried, including standalone Workbench.
- All unpublished state is classified and either safely retained/reviewed or explicitly excluded by authorized scope decision.
- Contributor/operator results are independently checked; any outstanding worktree/stash/branch is resolved or remains an explicit deletion HOLD.
- Audit evidence is stored privately; only a sanitized approval identifier and date appears publicly.
- Ref freshness and exact cleanup batch are revisited immediately before an authorized destructive action.

## Interaction with other gates

S2 **remains OPEN** until real verified contributor signoffs. S1 QEAX confidentiality, formal W/document-control governance, exact promotion-tip CI, Mac/Windows Obsidian GUI acceptance and standalone archive permission remain independent holds. A clean local `git status` is **not** sufficient proof of S2 completion.

## Handoff

**BR-38 result:** Created private-safe local Git audit and public reporting procedure. No signoff was obtained; no workstation, Git history, source model or binary archive was accessed by this step.

**NEXT BR-39:** Audit exact unique commits of held/divergent branches using an authorized trusted Git clone, or create an owner-ready approval packet that distinguishes checked facts from still-unverified gates.

**NO ACTION:** No PR closure, branch deletion, merge, rebase, force push, release promotion or old-repository archival.
