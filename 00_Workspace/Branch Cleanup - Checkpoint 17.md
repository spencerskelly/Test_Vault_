# Branch cleanup — checkpoint BR-17: historical Base Vault snapshots

Date: 2026-10-12
Status: PARTIAL — ancestry and source classification verified; exclusive commit IDs and full tree comparison pending
Candidate: consolidation/step22-single-repo-cutover-2026-10-11

## Live GitHub comparisons
| Historical branch | Branch-only commits | Step22-only commits | Status |
|---|---:|---:|---|
| base-vault-2026-09-30-rel132-v04 | 1 | 2242 | diverged |
| base-vault-2026-09-30-rel133-v05 | 1 | 2232 | diverged |
| base-vault-2026-09-30-rel133-v051 | 1 | 2225 | diverged |

Between historical snapshots: rel132-v04 to rel133-v05 yields 11 ahead / 1 behind, rel133-v05 to rel133-v051 yields 8 ahead / 1 behind. These branch histories are not linear ancestors of one another.

Each candidate/old-branch comparison had a 300-file listing cap, precluding exhaustive file-difference claims. Historical branch comparisons likewise had truncated file listings, including older importer versions and schemas.

## Exact identity evidence
Fetched .vault.yaml from all three and verified identical blob 9f02c8ea09e187c0f44cfc768d6d97ed6a37867b:

```yaml
# This file MUST be initialized once when a new vault is created.
# Do not copy a real vault_uid from another vault.
vault_uid: UNINITIALIZED
name: MDSE_Base_Vault
default_branch: main
```

These are uninitialized historical Base Vault templates, not active populated user vaults, based on the inspected vault identity files. This does not establish that all other files are safe to discard.

## Disposition
HOLD all three until unique commit and full-tree provenance checks. Do not bulk-merge historical generated vault snapshots into the current methodology authority. Preserve their refs until exact historical snapshot retention policy and any release/testing cross-references are resolved.

BR-15 remains blocked: 15 recovery documents were retrieved but no copy was committed. No merges/deletions were performed.

## Handoff
STEP: BR-17
STATUS: PARTIAL
CHECK: 3 branch comparisons + 2 peer comparisons + 3 vault identity files
NEXT: BR-18 — establish concise branch/PR retention decision ledger and enumerate exclusive commits using a trusted clone; prioritize preserving recovery documentation.
