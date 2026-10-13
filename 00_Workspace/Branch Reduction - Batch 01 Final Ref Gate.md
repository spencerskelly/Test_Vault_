# Branch Reduction — Batch 01 Final Ref and PR Metadata Gate

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Status: REVERIFIED ANCESTRY / PR HEAD-BASE UNVERIFIED / NO DELETION APPROVED

## Fresh comparison against Step22

| Candidate branch | Remote tip | Merge-base SHA | Step22 ahead | Candidate exclusive |
|---|---|---|---:|---:|
| consolidation/step16-w341-w342-release-provenance-2026-10-10 | d6343f6fa1e73fc8083e6e88b0541bd909ff9759 | d6343f6fa1e73fc8083e6e88b0541bd909ff9759 | 9 | 0 |
| consolidation/step17-document-registry-proposal-2026-10-10 | 72fd3ef25d882f3e304b14ae36f126fa2d812c16 | 72fd3ef25d882f3e304b14ae36f126fa2d812c16 | 8 | 0 |
| consolidation/step18-registry-application-rehearsal-2026-10-10 | cf47ab37fe549312669ad76095a2b229a2ee6b0e | cf47ab37fe549312669ad76095a2b229a2ee6b0e | 7 | 0 |

The candidate tips and merge-base identities match exactly: committed history is reachable from Step22 at time of inspection.

## Open PR evidence

PR #33 Step16 W-341/W-342 parity; #34 Step17 registry proposal; #35 Step18 registry rehearsal, each open, no submitted reviews found in preceding pass. Issue fetch does not expose structured pull request head/base fields. The connected GitHub tool catalog has no read-only get_pull_request or generic GitHub API action. An attempted public GitHub API lookup was inaccessible. Therefore the exact PR head/base relationship and mergeability remain UNKNOWN. No PR was modified.

## Owner GitHub view / CLI completion gate

In GitHub UI, open each link:
- https://github.com/spencerskelly/Test_Vault_/pull/33
- https://github.com/spencerskelly/Test_Vault_/pull/34
- https://github.com/spencerskelly/Test_Vault_/pull/35

Record "base: ... <- head: ...", draft state, mergeability and checks and verify whether later stacked PRs are based on the branch proposed for retirement.

Alternatively on a trusted operator machine with read-only GitHub CLI access run:
```sh
for n in 33 34 35; do
  gh pr view "$n" --repo spencerskelly/Test_Vault_ \
    --json number,title,state,isDraft,headRefName,headRefOid,baseRefName,mergeable,reviewDecision,statusCheckRollup \
    --jq '{number,title,state,isDraft,headRefName,headRefOid,baseRefName,mergeable,reviewDecision,statusCheckRollup}'
done
```
Do not run CLI mutation commands or paste secrets, private local paths or model data into the public audit.

## Durable preservation policy before deletion

Reachability through Step22 is **not yet a permanent preservation plan** while Step22 is unmerged. First establish that owner-approved main or an archival ref will keep these exact commits reachable, and keep PR evidence/CI references. Check local contributor unpublished work. Then seek explicit owner approval for this exact three-name, full-SHA list, and remove in a batch of three or fewer, verifying remote refs after each action.

No deletion, PR closure, merge, release or archival was executed.

Recommended next action: human/UI confirmation of PR head/base and owner decision whether to preserve with a small set of tags prior to branch retirement, or to defer until Step22 is accepted into main.
