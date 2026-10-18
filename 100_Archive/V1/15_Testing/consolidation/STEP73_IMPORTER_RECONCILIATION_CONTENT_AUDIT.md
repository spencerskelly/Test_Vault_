# Step 73 — Importer reconciliation content-level audit (2026-10-14)

Status: read-only provenance classification; no branch retirement authorized.

## Exact Git blob identity: functional checker already preserved

The file `66_Testing/check_importer_workbench_localmodel.py` has exactly the SAME Git blob `95c29b377ad8c7a0596e1c164db2e6bb66168b52` at:
- `integration/importer-reconciliation-2026-10-09`
- `consolidation/step22-single-repo-cutover-2026-10-11`
- `integration/p03-legacy-compat-tests-20261013`.

Thus the executable static compatibility checker is **content-preserved in Step22 and PR #43**, despite the importer-reconciliation branch having six exclusive commits. Its functionality tests manifest/schema/localmodel source version compatibility, including writable and readable versions. This is proof of file identity, NOT proof that any surviving CI workflow actually executes that script.

## Unique historical merge rehearsal not integrated

`.github/workflows/importer-monorepo-merge-rehearsal.yml` exists on the importer-reconciliation branch, blob `612cc78ee5c839def7dae9b343ef9c2f8dd9b8d2`, but is absent from Step22 and PR #43. It:
- pins original monorepo baseline and importer SHA, tests non-committing Git merge and no conflicts;
- asserts historical importer/schema/Workbench/bootstrap/plugin-lock pins;
- runs importer source-profile, headless code and acceptance regressions;
- assembles disposable Base vault and diagnoses historical release check;
- runs the EXACT compatibility checker above, Workbench tests/build and alignment check;
- produces diagnostic logs only, no push.

**Classification:** historical executable rehearsal/provenance; some controls are not proven equivalent to active consolidated CI. Hardcoded old SHAs and version pins mean it should NOT be blindly merged as a current authoritative workflow. Preserve the branch/ref or approved archival content until the specific assertions are mapped to replacement CI.

## Branch disposition

`integration/importer-reconciliation-2026-10-09`: HOLD. The checker source is preserved but its exclusive workflow and original merge evidence still need durable archival or approved equivalent checks. Six exclusive commits are an ancestry statement, not six unpreserved program changes.

## Step 74

Verify file-level preservation for the BOM and Workbench rehearsal branches and catalog original repository-recovery handoff documents. Determine whether historical workflow blobs and documents can be archived with provenance without activating outdated branch triggers. No branch deletion or merge without owner approval.
