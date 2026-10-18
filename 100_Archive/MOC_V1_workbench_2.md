# V1 archive inventory — 14_Workbench (2/2)

Read-only historical index. Every entry comes from the verified folder-migration path manifest; file presence does not establish functionality or approval. [Archive MOC](MOC_V1_ARCHIVE.md) · [Full manifest](../26_Definitions/V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json)


### src/core
- [variantof-format.ts](V1/14_Workbench/src/core/variantof-format.ts)
- [variantof.ts](V1/14_Workbench/src/core/variantof.ts)
- [views.ts](V1/14_Workbench/src/core/views.ts)

### src
- [main.ts](V1/14_Workbench/src/main.ts)

### src/obsidian
- [assurance.ts](V1/14_Workbench/src/obsidian/assurance.ts)
- [cache.ts](V1/14_Workbench/src/obsidian/cache.ts)
- [detail.ts](V1/14_Workbench/src/obsidian/detail.ts)
- [edit-service.ts](V1/14_Workbench/src/obsidian/edit-service.ts)
- [indexer.ts](V1/14_Workbench/src/obsidian/indexer.ts)
- [localmodel.ts](V1/14_Workbench/src/obsidian/localmodel.ts)
- [probe.ts](V1/14_Workbench/src/obsidian/probe.ts)
- [review.ts](V1/14_Workbench/src/obsidian/review.ts)
- [ui.ts](V1/14_Workbench/src/obsidian/ui.ts)
- [writer.ts](V1/14_Workbench/src/obsidian/writer.ts)

### Root
- [styles.css](V1/14_Workbench/styles.css)

### test
- [assurance.test.ts](V1/14_Workbench/test/assurance.test.ts)
- [background.test.ts](V1/14_Workbench/test/background.test.ts)
- [bom-localmodel-06.test.ts](V1/14_Workbench/test/bom-localmodel-06.test.ts)
- [bom-variantof.test.ts](V1/14_Workbench/test/bom-variantof.test.ts)
- [cache-mutation.test.ts](V1/14_Workbench/test/cache-mutation.test.ts)
- [cache-persistence.test.ts](V1/14_Workbench/test/cache-persistence.test.ts)
- [cache-quantity06.test.ts](V1/14_Workbench/test/cache-quantity06.test.ts)
- [cache-size.test.ts](V1/14_Workbench/test/cache-size.test.ts)
- [cache-storage.test.ts](V1/14_Workbench/test/cache-storage.test.ts)
- [cache.test.ts](V1/14_Workbench/test/cache.test.ts)
- [capability-staging.test.ts](V1/14_Workbench/test/capability-staging.test.ts)
- [cooperative.test.ts](V1/14_Workbench/test/cooperative.test.ts)
- [core-readiness.test.ts](V1/14_Workbench/test/core-readiness.test.ts)
- [core.test.ts](V1/14_Workbench/test/core.test.ts)
- [definition-create.test.ts](V1/14_Workbench/test/definition-create.test.ts)
- [definition-delete.test.ts](V1/14_Workbench/test/definition-delete.test.ts)
- [definition-lifecycle.test.ts](V1/14_Workbench/test/definition-lifecycle.test.ts)
- [definition-migrate.test.ts](V1/14_Workbench/test/definition-migrate.test.ts)
- [definition-note-migrate-service.test.ts](V1/14_Workbench/test/definition-note-migrate-service.test.ts)
- [definition-note-migrate.test.ts](V1/14_Workbench/test/definition-note-migrate.test.ts)
- [definition-retire.test.ts](V1/14_Workbench/test/definition-retire.test.ts)
- [definition-supersede-service.test.ts](V1/14_Workbench/test/definition-supersede-service.test.ts)
- [definition-supersede.test.ts](V1/14_Workbench/test/definition-supersede.test.ts)

### test/fixtures
- [element-types-legacy.yaml](V1/14_Workbench/test/fixtures/element-types-legacy.yaml)
- [element-types.yaml](V1/14_Workbench/test/fixtures/element-types.yaml)
- [local-model-0.1.yaml](V1/14_Workbench/test/fixtures/local-model-0.1.yaml)
- [local-model.yaml](V1/14_Workbench/test/fixtures/local-model.yaml)
- [relationships-legacy.yaml](V1/14_Workbench/test/fixtures/relationships-legacy.yaml)
- [relationships.yaml](V1/14_Workbench/test/fixtures/relationships.yaml)

### test
- [helpers.ts](V1/14_Workbench/test/helpers.ts)
- [hydration-cancel.test.ts](V1/14_Workbench/test/hydration-cancel.test.ts)
- [hydration-metrics.test.ts](V1/14_Workbench/test/hydration-metrics.test.ts)
- [identity.test.ts](V1/14_Workbench/test/identity.test.ts)
- [local-identity.test.ts](V1/14_Workbench/test/local-identity.test.ts)
- [local-retention.test.ts](V1/14_Workbench/test/local-retention.test.ts)
- [localmodel-edit.test.ts](V1/14_Workbench/test/localmodel-edit.test.ts)
- [localmodel.test.ts](V1/14_Workbench/test/localmodel.test.ts)
- [localmodel06-quantity.test.ts](V1/14_Workbench/test/localmodel06-quantity.test.ts)
- [metadata-burst.test.ts](V1/14_Workbench/test/metadata-burst.test.ts)
- [model-edit.test.ts](V1/14_Workbench/test/model-edit.test.ts)
- [occurrence-hydration.test.ts](V1/14_Workbench/test/occurrence-hydration.test.ts)
- [relationship-dependencies.test.ts](V1/14_Workbench/test/relationship-dependencies.test.ts)
- [relationship-resolution.test.ts](V1/14_Workbench/test/relationship-resolution.test.ts)
- [runtime-health.test.ts](V1/14_Workbench/test/runtime-health.test.ts)
- [single-flight.test.ts](V1/14_Workbench/test/single-flight.test.ts)
- [source-reconciliation.test.ts](V1/14_Workbench/test/source-reconciliation.test.ts)
- [startup-handoff.test.ts](V1/14_Workbench/test/startup-handoff.test.ts)
- [startup-recovery.test.ts](V1/14_Workbench/test/startup-recovery.test.ts)
- [transaction.test.ts](V1/14_Workbench/test/transaction.test.ts)
- [variantof-regression.test.ts](V1/14_Workbench/test/variantof-regression.test.ts)

### Root
- [tsconfig.json](V1/14_Workbench/tsconfig.json)
- [versions.json](V1/14_Workbench/versions.json)
