# Branch Reduction — Batch 01: Decision Request / Stop Rechecking

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Status: CANDIDATE, NOT AUTHORIZED FOR DELETION

## What is confirmed

- Step 16 `consolidation/step16-w341-w342-release-provenance-2026-10-10` tip `d6343f6fa1e73fc8083e6e88b0541bd909ff9759` is an ancestor of Step22, 9 commits behind.
- Step 17 `consolidation/step17-document-registry-proposal-2026-10-10` tip `72fd3ef25d882f3e304b14ae36f126fa2d812c16` is an ancestor of Step22, 8 commits behind.
- Step 18 `consolidation/step18-registry-application-rehearsal-2026-10-10` tip `cf47ab37fe549312669ad76095a2b229a2ee6b0e` is an ancestor of Step22, 7 commits behind.
- Open PRs #33, #34 and #35 respectively describe corresponding steps. No submitted reviews were observed previously.
- Step22 `consolidation/step22-single-repo-cutover-2026-10-11` remains an unmerged engineering candidate. The exact committed history is reachable through its remote ref *today*.

## The one-time external confirmation needed

The available read-only GitHub tools lack structured PR head/base and repository protection details; public GitHub API lookup was inaccessible. On trusted operator computer execute:

```sh
for n in 33 34 35; do
  gh pr view "$n" -R spencerskelly/Test_Vault_ \
    --json number,state,isDraft,headRefName,headRefOid,baseRefName \
    --jq '{number,state,isDraft,headRefName,headRefOid,baseRefName}'
done
```

Record these fields in the ledger and check each branch's PR comments/CI links. If PR #36 or later uses these branch names as its base, retarget successor PRs before removing refs; do not assume inherited Git commits alone preserve GitHub PR topology.

## Proposed minimal decision

1. **Keep now:** main, Step22 candidate and audit; eight divergent branches held.
2. **Batch 01 candidates:** only the three names/SHAs above; do not expand scope by category.
3. **Permanent preservation:** wait until the accepted Step22 history is reachable from approved main, or the owner authorizes immutable annotated tags on exact tips, and confirms tags actually exist remotely. A proposed tag name in a Markdown file is not a real ref.
4. **Local unpublished work:** owner/contributors attest no unique work in local branches, stashes or worktrees depending on these refs.
5. **Deletion:** after steps 3–4, verify exact remote tips again, obtain explicit approval identifying all three branch names, and remove one branch at a time.
6. **Post-delete:** enumerate remote refs, verify surviving commit ancestry and issue/PR links, stop if any discrepancy. Preserve all eight divergent branches and the historical QEAX security hold.

## Current authorization status

NO DELETION APPROVAL. NO MERGE APPROVAL. No refs or PRs were changed in this pass. This is an operational holdpoint, not a request to continue rechecking these same facts.

## Highest-value next work

Resolve major 1806-commit baseline integration into approved main or a durable archival ref. This is more important for reducing the repository to 1–3 branches than further ancestry audits of these three candidates.
