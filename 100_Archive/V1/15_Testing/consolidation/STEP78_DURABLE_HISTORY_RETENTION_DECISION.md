# Step 78 — Durable history retention decision (2026-10-14)

Status: **proposed ref plan, not executed**. Four live branch heads were re-fetched and exactly match Step76's frozen tips.

| Hold branch | Verified current tip SHA | Proposed retained reference (not created) |
|---|---|---|
| `integration/bom-a14-reconciliation-2026-10-09` | `92a466df64b485b2f396a380593cc79ff161300f` | `archive/2026-10-14/bom-a14-reconciliation` |
| `integration/importer-reconciliation-2026-10-09` | `28215a58ff4757ad833ff54a4edf67dd35f13eb0` | `archive/2026-10-14/importer-reconciliation` |
| `integration/workbench-monorepo-rehearsal-2026-10-09` | `79dac2f69f97c3ac9ae8a1735640666e4047badb` | `archive/2026-10-14/workbench-rehearsal` |
| `recovery/repository-consolidation-2026-10-09` | `ffca1a2b8e8fe54da2191309f52a34286ad34648` | `archive/2026-10-14/repository-recovery` |

The four refs are a conservative **upper bound** on minimum retention. Fewer could suffice only after a full reachability proof showing one destination commit contains the exact others. Because each has exclusive history relative to Step22, content copies cannot replace ancestry retention. Prefer protected, annotated immutable archive tags if repository policy supports them; the proposed `archive/...` strings are logical labels and would be tag names under `refs/tags/`, **not** automatically branch refs.

## Existing preservation

- Three original workflows have been copied into non-executable archival files with exact Git blob matches, Step77 README.
- Recovery Steps 04B–18 are identical on recovery and Step22 (15/15 verified in Step75).
- PR39/PR41/PR42/PR43 and real-QEAX/GUI/release gates remain independent; no release candidate approval inferred.
- Frozen Step22 stays protected until an approved durable merge into main or approved archive ref.

## Owner approval decision, before creating refs

1. Approve or reject four exact tip SHA targets and archival tag naming/policy.
2. Confirm tag immutability/protection and whether tags are permitted as long-lived retention references.
3. Independently check current branch tips unchanged and that each tag, when created, resolves to the correct commit, then record verification.
4. Inspect PR dependencies and unpublished local work; tags preserve committed ancestry but neither local unpublished work nor CI artifacts.
5. Only after signed owner authorization for **each exact branch name+SHA**, permit branch deletion in a separately gated batch (max three per pass), verify branch absence and tag continued existence.
6. Do not delete or alter Step22, PR43 validation branch, `main`, or historic released artifacts in this stage.

## Next Step79

Review current PR dependency metadata for these four branch names and define conditional tag creation procedure and verification. **Do not create tags before explicit owner authorization.**

Step78 made no tags, merges, deletions, release changes, or model changes.
