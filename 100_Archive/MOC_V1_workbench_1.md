# V1 archive inventory — 14_Workbench (1/2)

Read-only historical index. Every entry comes from the verified folder-migration path manifest; file presence does not establish functionality or approval. [Archive MOC](MOC_V1_ARCHIVE.md) · [Full manifest](../26_Definitions/V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json)


### .devcontainer
- [devcontainer.json](V1/14_Workbench/.devcontainer/devcontainer.json)

### Root
- [.gitattributes](V1/14_Workbench/.gitattributes)

### .github/workflows
- [bom-a14-verify.yml](V1/14_Workbench/.github/workflows/bom-a14-verify.yml)
- [bom-artifact-recovery-audit.yml](V1/14_Workbench/.github/workflows/bom-artifact-recovery-audit.yml)
- [build-artifact.yml](V1/14_Workbench/.github/workflows/build-artifact.yml)
- [integration-candidate-startup.yml](V1/14_Workbench/.github/workflows/integration-candidate-startup.yml)
- [integration-cold-start.yml](V1/14_Workbench/.github/workflows/integration-cold-start.yml)
- [integration-live-edit.yml](V1/14_Workbench/.github/workflows/integration-live-edit.yml)
- [integration-plugin-overlap.yml](V1/14_Workbench/.github/workflows/integration-plugin-overlap.yml)
- [integration-recovery.yml](V1/14_Workbench/.github/workflows/integration-recovery.yml)
- [integration-restart-cycles.yml](V1/14_Workbench/.github/workflows/integration-restart-cycles.yml)
- [integration-view-capability.yml](V1/14_Workbench/.github/workflows/integration-view-capability.yml)

### Root
- [.gitignore](V1/14_Workbench/.gitignore)
- [README.md](V1/14_Workbench/README.md)
- [RELEASE_NOTES.md](V1/14_Workbench/RELEASE_NOTES.md)
- [WB106_IMPLEMENTATION_CONTRACT.md](V1/14_Workbench/WB106_IMPLEMENTATION_CONTRACT.md)
- [artifact-sha256.txt](V1/14_Workbench/artifact-sha256.txt)

### bench
- [cache-bench.ts](V1/14_Workbench/bench/cache-bench.ts)
- [generate-vault.ts](V1/14_Workbench/bench/generate-vault.ts)
- [install-obsidian-plugin-release.mjs](V1/14_Workbench/bench/install-obsidian-plugin-release.mjs)
- [obsidian-e2e-activate.mjs](V1/14_Workbench/bench/obsidian-e2e-activate.mjs)
- [obsidian-e2e-observe.mjs](V1/14_Workbench/bench/obsidian-e2e-observe.mjs)
- [obsidian-e2e-setup.mjs](V1/14_Workbench/bench/obsidian-e2e-setup.mjs)
- [obsidian-live-edit-probe.mjs](V1/14_Workbench/bench/obsidian-live-edit-probe.mjs)
- [obsidian-plugin-overlap-probe.mjs](V1/14_Workbench/bench/obsidian-plugin-overlap-probe.mjs)
- [obsidian-recovery-probe.mjs](V1/14_Workbench/bench/obsidian-recovery-probe.mjs)
- [obsidian-restart-cycle-probe.mjs](V1/14_Workbench/bench/obsidian-restart-cycle-probe.mjs)
- [obsidian-view-capability-probe.mjs](V1/14_Workbench/bench/obsidian-view-capability-probe.mjs)
- [relationship-reresolution-bench.ts](V1/14_Workbench/bench/relationship-reresolution-bench.ts)
- [run-bench.ts](V1/14_Workbench/bench/run-bench.ts)
- [run-plugin-overlap.sh](V1/14_Workbench/bench/run-plugin-overlap.sh)
- [startup-bench.ts](V1/14_Workbench/bench/startup-bench.ts)

### ci-workflows
- [ci.yml](V1/14_Workbench/ci-workflows/ci.yml)
- [release.yml](V1/14_Workbench/ci-workflows/release.yml)

### docs/Architecture
- [MDSE Runtime Architecture.md](V1/14_Workbench/docs/Architecture/MDSE%20Runtime%20Architecture.md)

### docs
- [BASE_local_MDSE Workbench.base](V1/14_Workbench/docs/BASE_local_MDSE%20Workbench.base)

### docs/Definition
- [01 - Workbench Product Definition.md](V1/14_Workbench/docs/Definition/01%20-%20Workbench%20Product%20Definition.md)
- [02 - Workbench Decision Log.md](V1/14_Workbench/docs/Definition/02%20-%20Workbench%20Decision%20Log.md)
- [03 - Build Outline and Roadmap.md](V1/14_Workbench/docs/Definition/03%20-%20Build%20Outline%20and%20Roadmap.md)
- [04 - Architecture and Model Boundary.md](V1/14_Workbench/docs/Definition/04%20-%20Architecture%20and%20Model%20Boundary.md)

### docs
- [INDEX.md](V1/14_Workbench/docs/INDEX.md)
- [README.md](V1/14_Workbench/docs/README.md)

### docs/Reference
- [05 - Reference Plugin Findings.md](V1/14_Workbench/docs/Reference/05%20-%20Reference%20Plugin%20Findings.md)
- [ARCHIVE_BOM_A14_BASELINE_CHECK.yml](V1/14_Workbench/docs/Reference/ARCHIVE_BOM_A14_BASELINE_CHECK.yml)
- [ARCHIVE_CI_PROBE_RUNTIME_ARCHITECTURE.md](V1/14_Workbench/docs/Reference/ARCHIVE_CI_PROBE_RUNTIME_ARCHITECTURE.md)

### docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10
- [README.md](V1/14_Workbench/docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10/README.md)
- [bom-a14-source-step15.yml](V1/14_Workbench/docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10/bom-a14-source-step15.yml)
- [wb128-gate3-representative-views.yml](V1/14_Workbench/docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10/wb128-gate3-representative-views.yml)
- [wb128-gate4-disposable-edits.yml](V1/14_Workbench/docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10/wb128-gate4-disposable-edits.yml)
- [wb128-gate5-release-alignment.yml](V1/14_Workbench/docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10/wb128-gate5-release-alignment.yml)
- [wb128-real-vault-acceptance.yml](V1/14_Workbench/docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10/wb128-real-vault-acceptance.yml)
- [wb129-real-qeax-local-model-05.yml](V1/14_Workbench/docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10/wb129-real-qeax-local-model-05.yml)
- [wb129-rehearsal.yml](V1/14_Workbench/docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10/wb129-rehearsal.yml)
- [workbench-subtree-stage.yml](V1/14_Workbench/docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10/workbench-subtree-stage.yml)

### docs/Reference
- [ARCHIVE_RTA2_CI_PROBE.md](V1/14_Workbench/docs/Reference/ARCHIVE_RTA2_CI_PROBE.md)
- [ARCHIVE_WB106_BUILD_SHA256.txt](V1/14_Workbench/docs/Reference/ARCHIVE_WB106_BUILD_SHA256.txt)
- [ARCHIVE_WB106_RUNTIME_BUILD.yml](V1/14_Workbench/docs/Reference/ARCHIVE_WB106_RUNTIME_BUILD.yml)

### docs/Testing
- [06 - Test Sheet.md](V1/14_Workbench/docs/Testing/06%20-%20Test%20Sheet.md)
- [RTA Startup Acceptance.md](V1/14_Workbench/docs/Testing/RTA%20Startup%20Acceptance.md)
- [RTA Startup and Semantic Cache Test Sheet.md](V1/14_Workbench/docs/Testing/RTA%20Startup%20and%20Semantic%20Cache%20Test%20Sheet.md)

### docs/User Guide
- [MDSE Workbench User Guide.md](V1/14_Workbench/docs/User%20Guide/MDSE%20Workbench%20User%20Guide.md)

### docs/bom
- [A01-A14_ARTIFACT_SHA256.md](V1/14_Workbench/docs/bom/A01-A14_ARTIFACT_SHA256.md)
- [A01-A14_GIT_PERSISTENCE_AUDIT.md](V1/14_Workbench/docs/bom/A01-A14_GIT_PERSISTENCE_AUDIT.md)
- [A01-A14_ORIGINAL_HANDOFF_ARCHIVE_VERIFICATION_2026-10-09.md](V1/14_Workbench/docs/bom/A01-A14_ORIGINAL_HANDOFF_ARCHIVE_VERIFICATION_2026-10-09.md)
- [A01-A14_RECOVERY_STATUS_2026-10-09.md](V1/14_Workbench/docs/bom/A01-A14_RECOVERY_STATUS_2026-10-09.md)

### docs/bom/a01-a14
- [BOM_A06_Fixtures.zip](V1/14_Workbench/docs/bom/a01-a14/BOM_A06_Fixtures.zip)
- [BOM_A08_VariantOf_Test_Results.txt](V1/14_Workbench/docs/bom/a01-a14/BOM_A08_VariantOf_Test_Results.txt)
- [BOM_A08_variantof_fixture_check.py](V1/14_Workbench/docs/bom/a01-a14/BOM_A08_variantof_fixture_check.py)
- [BOM_A11_Canonical_Examples.zip](V1/14_Workbench/docs/bom/a01-a14/BOM_A11_Canonical_Examples.zip)
- [BOM_A14_Baseline_Comparison.md](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_Baseline_Comparison.md)
- [BOM_A14_CI_Verification_Checkpoint.md](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_CI_Verification_Checkpoint.md)
- [BOM_A14_Cache_Restoration_Checkpoint.md](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_Cache_Restoration_Checkpoint.md)
- [BOM_A14_Disposable_Obsidian_Vault.zip](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_Disposable_Obsidian_Vault.zip)
- [BOM_A14_Metadata_Boundary_Checkpoint.md](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_Metadata_Boundary_Checkpoint.md)
- [BOM_A14_Obsidian_Runtime_Acceptance.md](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_Obsidian_Runtime_Acceptance.md)
- [BOM_A14_Raw_Variant_YAML_Checkpoint.md](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_Raw_Variant_YAML_Checkpoint.md)
- [BOM_A14_Reader_Implementation_Checkpoint.md](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_Reader_Implementation_Checkpoint.md)
- [BOM_A14_Reader_Preflight.md](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_Reader_Preflight.md)
- [BOM_A14_Review_Integration_Checkpoint.md](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_Review_Integration_Checkpoint.md)
- [BOM_A14_Test_Continuation.md](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_Test_Continuation.md)
- [BOM_A14_Validation_Checkpoint.md](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_Validation_Checkpoint.md)
- [BOM_A14_VariantOf_Checkpoint.md](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_VariantOf_Checkpoint.md)
- [BOM_A14_Variant_Link_Evidence_Checkpoint.md](V1/14_Workbench/docs/bom/a01-a14/BOM_A14_Variant_Link_Evidence_Checkpoint.md)
- [BOM_AI_TEMPLATE_AMENDMENT_A-13.md](V1/14_Workbench/docs/bom/a01-a14/BOM_AI_TEMPLATE_AMENDMENT_A-13.md)
- [BOM_DECISION_AUTHORITY_A-03.md](V1/14_Workbench/docs/bom/a01-a14/BOM_DECISION_AUTHORITY_A-03.md)
- [BOM_LOCAL_MODEL_SCHEMA_PROPOSAL_A-05.md](V1/14_Workbench/docs/bom/a01-a14/BOM_LOCAL_MODEL_SCHEMA_PROPOSAL_A-05.md)
- [BOM_LOCAL_MODEL_UNITS_CONTRACT_A-04.md](V1/14_Workbench/docs/bom/a01-a14/BOM_LOCAL_MODEL_UNITS_CONTRACT_A-04.md)
- [BOM_MDSE_Vault_Implementation_Plan.md](V1/14_Workbench/docs/bom/a01-a14/BOM_MDSE_Vault_Implementation_Plan.md)
- [BOM_OBJECT_SUBTYPE_A-09.md](V1/14_Workbench/docs/bom/a01-a14/BOM_OBJECT_SUBTYPE_A-09.md)
- [BOM_RULESET_AMENDMENT_A-12.md](V1/14_Workbench/docs/bom/a01-a14/BOM_RULESET_AMENDMENT_A-12.md)
- [BOM_RUN_LOG.md](V1/14_Workbench/docs/bom/a01-a14/BOM_RUN_LOG.md)
- [BOM_SEMANTIC_DECISION_RECORD_A-02.md](V1/14_Workbench/docs/bom/a01-a14/BOM_SEMANTIC_DECISION_RECORD_A-02.md)
- [BOM_SOURCE_MANIFEST.json](V1/14_Workbench/docs/bom/a01-a14/BOM_SOURCE_MANIFEST.json)
- [BOM_VARIANTOF_CONTRACT_A-07.md](V1/14_Workbench/docs/bom/a01-a14/BOM_VARIANTOF_CONTRACT_A-07.md)
- [BOM_VARIANTOF_SCHEMA_PROPOSAL_A-08.md](V1/14_Workbench/docs/bom/a01-a14/BOM_VARIANTOF_SCHEMA_PROPOSAL_A-08.md)
- [BOM_VARIANT_COMPARISON_CONTRACT_A-10.md](V1/14_Workbench/docs/bom/a01-a14/BOM_VARIANT_COMPARISON_CONTRACT_A-10.md)

### Root
- [esbuild.config.mjs](V1/14_Workbench/esbuild.config.mjs)
- [manifest.json](V1/14_Workbench/manifest.json)
- [package-lock.json](V1/14_Workbench/package-lock.json)
- [package.json](V1/14_Workbench/package.json)

### scripts
- [real-vault-05-acceptance.ts](V1/14_Workbench/scripts/real-vault-05-acceptance.ts)
- [real-vault-acceptance.ts](V1/14_Workbench/scripts/real-vault-acceptance.ts)
- [real-vault-edit-check.ts](V1/14_Workbench/scripts/real-vault-edit-check.ts)
- [real-vault-readonly-scan.ts](V1/14_Workbench/scripts/real-vault-readonly-scan.ts)
- [real-vault-view-check.ts](V1/14_Workbench/scripts/real-vault-view-check.ts)

### src/core
- [background.ts](V1/14_Workbench/src/core/background.ts)
- [cache-mutation.ts](V1/14_Workbench/src/core/cache-mutation.ts)
- [cache-persistence.ts](V1/14_Workbench/src/core/cache-persistence.ts)
- [cache-size.ts](V1/14_Workbench/src/core/cache-size.ts)
- [cache-storage.ts](V1/14_Workbench/src/core/cache-storage.ts)
- [cache.ts](V1/14_Workbench/src/core/cache.ts)
- [cooperative.ts](V1/14_Workbench/src/core/cooperative.ts)
- [core-readiness.ts](V1/14_Workbench/src/core/core-readiness.ts)
- [definition-create.ts](V1/14_Workbench/src/core/definition-create.ts)
- [definition-delete.ts](V1/14_Workbench/src/core/definition-delete.ts)
- [definition-lifecycle.ts](V1/14_Workbench/src/core/definition-lifecycle.ts)
- [definition-migrate.ts](V1/14_Workbench/src/core/definition-migrate.ts)
- [definition-note-migrate-service.ts](V1/14_Workbench/src/core/definition-note-migrate-service.ts)
- [definition-note-migrate.ts](V1/14_Workbench/src/core/definition-note-migrate.ts)
- [definition-retire.ts](V1/14_Workbench/src/core/definition-retire.ts)
- [definition-supersede-service.ts](V1/14_Workbench/src/core/definition-supersede-service.ts)
- [definition-supersede.ts](V1/14_Workbench/src/core/definition-supersede.ts)
- [detail.ts](V1/14_Workbench/src/core/detail.ts)
- [edit-availability.ts](V1/14_Workbench/src/core/edit-availability.ts)
- [edit.ts](V1/14_Workbench/src/core/edit.ts)
- [frontmatter.ts](V1/14_Workbench/src/core/frontmatter.ts)
- [hydration-cancel.ts](V1/14_Workbench/src/core/hydration-cancel.ts)
- [hydration-metrics.ts](V1/14_Workbench/src/core/hydration-metrics.ts)
- [identity.ts](V1/14_Workbench/src/core/identity.ts)
- [internal-view.ts](V1/14_Workbench/src/core/internal-view.ts)
- [local-identity.ts](V1/14_Workbench/src/core/local-identity.ts)
- [local-retention.ts](V1/14_Workbench/src/core/local-retention.ts)
- [localmodel-edit.ts](V1/14_Workbench/src/core/localmodel-edit.ts)
- [localmodel.ts](V1/14_Workbench/src/core/localmodel.ts)
- [metadata-burst.ts](V1/14_Workbench/src/core/metadata-burst.ts)
- [model-edit.ts](V1/14_Workbench/src/core/model-edit.ts)
- [model.ts](V1/14_Workbench/src/core/model.ts)
- [occurrence-hydration.ts](V1/14_Workbench/src/core/occurrence-hydration.ts)
- [relationship-dependencies.ts](V1/14_Workbench/src/core/relationship-dependencies.ts)
- [relationship-resolution.ts](V1/14_Workbench/src/core/relationship-resolution.ts)
- [review.ts](V1/14_Workbench/src/core/review.ts)
- [rules.ts](V1/14_Workbench/src/core/rules.ts)
- [runtime-health.ts](V1/14_Workbench/src/core/runtime-health.ts)
- [schema.ts](V1/14_Workbench/src/core/schema.ts)
- [single-flight.ts](V1/14_Workbench/src/core/single-flight.ts)
- [source-reconciliation.ts](V1/14_Workbench/src/core/source-reconciliation.ts)
- [startup-cache.ts](V1/14_Workbench/src/core/startup-cache.ts)
- [startup-handoff.ts](V1/14_Workbench/src/core/startup-handoff.ts)
- [startup-recovery.ts](V1/14_Workbench/src/core/startup-recovery.ts)
- [transaction.ts](V1/14_Workbench/src/core/transaction.ts)
