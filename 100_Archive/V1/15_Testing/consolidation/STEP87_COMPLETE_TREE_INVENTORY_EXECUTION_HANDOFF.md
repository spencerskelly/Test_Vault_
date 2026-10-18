# Step 87 — Full four-ref Git tree inventory: execution handoff (2026-10-14)

**Status: script committed; exhaustive comparison NOT YET EXECUTED.** The existing GitHub compare API truncates path lists at 300, so it cannot establish full coverage for Step22/PR43. A new exact tracked-tree inventory script was committed at `66_Testing/consolidation/step87_full_tree_inventory.py` (last update c3f962f832d7678fd8748e8f8ca8df7934ea1cf8). An attempt to commit the CI runner was blocked by the tool safety check. No runner/workflow was created, no classification report exists, and counts must not be inferred.

## Read-only execution

In a local fresh repository clone with access to these four Git branch refs, fetch only tree metadata (no blob content):

```bash
git -c protocol.version=2 fetch --no-tags --filter=blob:none origin \
  refs/heads/main:refs/remotes/origin/main \
  refs/heads/consolidation/step22-single-repo-cutover-2026-10-11:refs/remotes/origin/consolidation/step22-single-repo-cutover-2026-10-11 \
  refs/heads/integration/lean-test-infrastructure-20261013:refs/remotes/origin/integration/lean-test-infrastructure-20261013 \
  refs/heads/integration/p03-legacy-compat-tests-20261013:refs/remotes/origin/integration/p03-legacy-compat-tests-20261013
python3 66_Testing/consolidation/step87_full_tree_inventory.py
```

Output paths: `66_Testing/consolidation/reports/step87-full-tree.json` and `step87-summary.md`. These reports include path names and Git object SHA identities, NOT file contents. Do not commit raw reports until reviewed for filename sensitivity. Avoid checkout of historic QEAX and sensitive model archive contents.

## Interim collision conclusions (verified in Step86)

- Two PR42 test scripts have identical blob SHAs with PR43.
- Two same-named P03/P04 CI workflows have divergent blob SHAs in PR42 and PR43.
- Main and PR42 use Local Model 0.2, while Step22/PR43 use 0.5, and release/plugin lock blobs also differ.
- Additional divergent paths remain **unknown**, not zero.

## Step88 acceptance

Run the metadata inventory, capture all ref SHAs and counts, verify output path count equal to union of four trees, summarize divergent clusters and validate ambiguous source conflicts. Only then authorize assembly of a main-based integration candidate. No merges, tag creations, main edits, PR state changes or branch deletions.
