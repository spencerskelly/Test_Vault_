# Branch Reduction — Batch 01 PR Dependency and Recovery Register

Date: 2026-10-12
Repository: spencerskelly/Test_Vault_
Audit PR: #41
Status: NON-DESTRUCTIVE REVIEW; 0 deleted, 0 merged, 0 PRs closed.

## Verified candidate branch tips and native PR associations

| Branch | Frozen branch tip SHA | Associated open PR | PR topic | Submitted reviews |
|---|---|---|---|---:|
| consolidation/step16-w341-w342-release-provenance-2026-10-10 | d6343f6fa1e73fc8083e6e88b0541bd909ff9759 | #33 https://github.com/spencerskelly/Test_Vault_/pull/33 | W-341 guide parity, W-342 pinned/candidate release rules | 0 |
| consolidation/step17-document-registry-proposal-2026-10-10 | 72fd3ef25d882f3e304b14ae36f126fa2d812c16 | #34 https://github.com/spencerskelly/Test_Vault_/pull/34 | 32 unregistered Workspace files proposed for document control | 0 |
| consolidation/step18-registry-application-rehearsal-2026-10-10 | cf47ab37fe549312669ad76095a2b229a2ee6b0e | #35 https://github.com/spencerskelly/Test_Vault_/pull/35 | 32 provisional registry entries staged in manifest, not owner approved | 0 |

These associations were confirmed by fetching the open PRs and matching their Step numbers, titles and described work to exact branch names; the API in this pass did NOT independently expose each PR's head-ref name, so final UI confirmation of exact PR heads remains necessary.

## Preservation

All three exact branch tips were previously compared against Step22: merge base equals each candidate tip; Step22 ahead 9, 8 and 7 respectively, behind 0. Thus every committed ancestor object is currently reachable via Step22 at its present ref. This is not a release approval and not permanent retention if the Step22 branch itself were later deleted without another permanent ref.

PR #33 is verification-only; #34 supplies *proposals*, 29 reference plus 3 unapproved proposals; #35 stages 32 registry rows but retains document-control pending status. Do not misrepresent staging as formal approval. Older PRs are not to be merged individually simply to reduce branches.

## Safe deletion gate for Batch 01

1. Establish a permanent owner-approved reachable ref (usually approved merged `main` or annotated preservation tag) containing all three exact SHAs; record its identifier and current tip.
2. Verify precise PR head/base refs and requirements in GitHub PR UI and any cross-PR dependencies; do not rely on title matching alone.
3. Independently review and decide PR #33/#34/#35 closure/supersession and retain their discussion and CI links. PR closure is separately owner-authorized and should link surviving commit and audit document.
4. Confirm contributor local branches/stashes are not using these refs as unpublished work and resolve the relevant public QEAX history security-owner decision; branch deletion does not remediate sensitive history.
5. Recompare tips against *the surviving ref* immediately before deletion to prevent stale-state cleanup.
6. Obtain explicit owner approval enumerating exactly these three names and SHAs; delete only authorized refs, verify remote after each small batch.

## Decision now

**CANDIDATE / HOLD FOR APPROVAL.** Zero committed ancestry loss relative to current Step22 branch, but no evidence of required permanent retention, open PR final disposition, or contributor signoff. The goal remains at most 1-3 active branches without loss of history; do not prematurely delete the candidate Step22 or audit ref.

Next: verify PR head/base via a supported read-only API or owner GitHub view, then prepare the exact first batch authorization request with durable retention evidence. No deletion or archival in this pass.
