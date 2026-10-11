# Historical GitHub Actions — Workbench consolidation Step 11

**Status:** Reference-only, exact-byte archived workflow definitions. These files must not be copied back to `.github/workflows/` without a separate approved CI-governance decision.

**Archived on:** 2026-10-10, from `spencerskelly/Test_Vault_` Step 10 staging SHA `34be43521b1579e0ced60e66cd234c87ba4c22c4`. The branch is review-only and must not be merged into public main until QEAX classification, local-clone signoffs, and runtime/Obsidian acceptance.

These eight source workflows used frozen `spencerskelly/MDSE_Workbench` source or earlier migration routines. Three contained `contents: write` and explicit Git pushes. All original YAML bytes are retained as the same Git blobs at these **non-executable documentation paths**. GitHub Actions historical runs and earlier commits are unchanged.

| Original active workflow | Archived YAML Git blob SHA | Historical role |
|---|---|---|
| `.github/workflows/bom-a14-source-step15.yml` | `b0a138ecdb46a3a74587aa0ba04997a06d930455` | write/push source migration |
| `.github/workflows/wb128-gate3-representative-views.yml` | `0bdaa3b0feb5e6917f6cb42053f93ddbcac8cb06` | historical WB-128 acceptance |
| `.github/workflows/wb128-gate4-disposable-edits.yml` | `5afbcd3322f228889fd0ce57e66e14eb3c725598` | historical WB-128 acceptance |
| `.github/workflows/wb128-gate5-release-alignment.yml` | `abf0174b2af10d4f9974a584bfa12530f1721b47` | historical WB-128 release-alignment gate |
| `.github/workflows/wb128-real-vault-acceptance.yml` | `44b4c93f413ccf0478b8cfb162692fc0f40b0004` | historical WB-128 manual real-vault candidate |
| `.github/workflows/wb129-real-qeax-local-model-05.yml` | `7c14dc88cb3cd53fc317897cd260c3ed9113c2f7` | historical WB-129 QEAX contract |
| `.github/workflows/wb129-rehearsal.yml` | `7721087d6fc31cafd2390cdaa5ba8ae1fc97b09a` | write/push migration rehearsal |
| `.github/workflows/workbench-subtree-stage.yml` | `3e51e09147179ffed9a24c3f19b38d8705fb6fe1` | write/push subtree migration |

**Preservation mechanism:** On this isolated branch the eight original `.github/workflows/*.yml` paths are removed after the exact YAML blob IDs are installed under this reference directory. GitHub Actions loads workflow definitions from the root `.github/workflows/` directory, so these archived files are documentary evidence, not runnable workflows.

**Replacement authority:** root `.github/workflows/mdse-monorepo-workbench-ci.yml` and `.github/workflows/mdse-release-alignment-preflight.yml` are the active *candidate* monorepo CI definitions. This archive does not declare them approved for release, does not replace frozen WB-128/WB-129 test results with new tests, and does not authorize Workbench 0.6 writing.

**Critical limitation:** This move only affects the isolated Step 11 review branch. Workflows on other branches, old Git history, standalone repository configurations, external automation and GitHub settings are outside this change; a public-main cutover and separate archival approval remain necessary.

**Restoration:** To recover original contents, retrieve the corresponding blob SHA in the table or the parent staging commit. If a future historical run is explicitly authorized, run it in a separately constrained review environment; do not reactivate write-capable old workflows in the development authority.
