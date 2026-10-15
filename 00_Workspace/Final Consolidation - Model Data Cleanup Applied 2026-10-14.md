# Final Consolidation — Active Model Data Cleanup 2026-10-14

Requested scope: remove imported model data from the proposed methodology/tools source authority; keep `main` intact.

## Completed on staging
1. Branch `integration/final-preservation-stage-20261014` fast-forwarded to prior cleanup commit `aefd546af72e1c7483804a8343c7b405bd361b0f`. This deletes `55_Workbench/vault/`, a 60,033-file synthetic Obsidian model, while preserving `55_Workbench/src/`.
2. A second commit `d0652acf1dbce3c169b2c5561e9f45e3fa3bb4ff` removes root `EA_2026_09_06_endgame.qeax.zip`, an engineering source-model archive. Both changes exist on the **active staging branch**, not only cleanup branch.
3. Draft PR #45 to main shrank from **60,611 changed files to 573**, verified in GitHub after refresh. Current remaining changed-path list is fully retrievable through the 3,000-file endpoint.
4. Reference methods, schemas, Workbench application source, importer code and tests remain in staging. Three Workbench BOM test ZIPs remain for dependency classification and should not be called real project model without inspection.
5. Exact commit `d0652ac` has fresh workflow runs launched; **new checks are pending**, so do not rely on preceding SHA's green tests as cleanup acceptance.

## IMPORTANT provenance/security boundary
These commits remove the files from the current tree but **do not erase blobs from Git history**. The standalone Workbench imported history includes the 60k synthetic vault, and source model archive may be retrievable in old commits / branches. If archive content is confidential, a separate security owner decision, repository access review and possible history rewrite is necessary. Such rewriting affects every clone/ref and must never be done as routine branch cleanup.

## Next consolidation
- Wait for and inspect exact-HEAD CI, especially any tests expecting the removed vault.
- Investigate remaining 573 paths, document any additional real imported model data; classify BOM fixture archives before removal.
- Correct any test dependency on the removed model by using small controlled synthetic fixtures.
- After approval, close superseded draft cleanup PR #46 and superseded validation PRs; pursue reviewed main promotion PR #45, create `develop`, and authorize small branch-retirement batches.
- Do not merge/promote until preservation, governance and security checks complete.
