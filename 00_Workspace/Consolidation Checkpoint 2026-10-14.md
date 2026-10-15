# Consolidation checkpoint — 2026-10-14

## Scope and authority
Target: `spencerskelly/Test_Vault_` as the sole ongoing source authority for MDSE methods, tools, definitions, and tests. Do not include imported engineering-model data or real QEAX exports. Synthetic fixtures explicitly needed by automated tests are allowed.

## Verified repository observations
- `main` remains default but has not yet received the large staged consolidation.
- `integration/final-preservation-stage-20261014` is **one commit ahead** of `cleanup/remove-imported-model-data-20261014`; the single file change removes `EA_2026_09_06_endgame.qeax.zip`.
- Relative to `main`, final-preservation is divergent (1,948 ahead, 2 behind at the time of inspection). GitHub's compare result caps displayed changed files at 300, so this is *not* a complete file inventory.
- `55_Workbench/` exists on the staging candidate, and the candidate README identifies it as the consolidated Workbench source of authority. The original standalone repository remains preserved.
- `integration/lean-test-infrastructure-20261013` is 8 commits ahead / 2 behind `main`, with four observed changes: P03/P04 workflows and test scripts.
- The existing staging `.gitignore` does not explicitly exclude `*.qeax`, `*.qea`, or imported-model output folders.

## Release gates before promoting staging to main
1. Obtain a complete tracked-file list on the candidate (not only a capped compare view): `git ls-tree -r --name-only HEAD`. Flag actual QEAX/QEA files, imported notes and generated outputs; distinguish controlled tiny synthetic fixtures from real-source model data.
2. Record deletion commit and confirm `EA_2026_09_06_endgame.qeax.zip` is absent from the candidate tip. Check for other real-model data; remove it in a separate, reviewable commit.
3. Add specific `.gitignore` and CI rejection rules for real-source model archives/import outputs while allowing governed synthetic test fixtures.
4. Reconcile P03/P04 lean testing changes into the candidate and run gates. Avoid combining changes from obsolete consolidation step branches indiscriminately.
5. Audit open PRs, branch ancestry, required checks and main's two divergent commits. Merge only after test and tree verification.
6. Archive/retire branches **after** confirming contained work has a retained home in main. Do not delete branches or rewrite history as part of an unverified cleanup.
7. Update `main` README/current state to single-authority Workbench once promotion succeeds. Keep the old Workbench repository available as historical evidence until approved retirement.

## Next atomic task
Run a full **candidate tracked-tree classification** and produce counts for runtime/source/test/docs versus imported data. Address any remaining model data before the final merge.
