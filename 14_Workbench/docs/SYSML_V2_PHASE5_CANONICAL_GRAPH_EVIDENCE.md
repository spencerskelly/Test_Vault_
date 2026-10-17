# Phase 5 — Canonical typed graph and EA evidence contract
Date: 2026-10-17
Status: synthetic implementation tested; not deployed in Workbench.
Files: `registry/runtime/canonical-model.mjs`, `registry/runtime/canonical-model.test.mjs`.
## Canonical structure
Node: stable `id`, `kind`, optional `definitionId` for Usage, optional `ownerId`, with graph `version`. Reusable definitions are never cloned because of additional usages; owned usages refer to a reusable definition. Reject missing/duplicate identities, incompatible definition kind, missing owner, untyped usage, and ownership cycles.
## Formal source evidence envelope (v0.1)
`{family,sourceId,targetId,connectorId,roles:{orientation,meaning,normalizedMeaning?},ownerId?,evidence:{direction?,aggregationKind?,multiplicity?,classifierId?,semanticJustification?}}`.
Directions are required explicit `source-to-target` or `target-to-source`; the contract does not infer semantics from endpoint type alone. For Realisation, reversal to approved requirement-to-implementation policy requires explicitly recorded `normalizedMeaning`. Other specialized role strings are asserted by a trusted adapter, not inferred by the engine.
## Runtime operations
`validateGraph(graph)`, `normalizeEA(envelope)`, `evaluateOnGraph(registry,graph,envelope)`, `menuOnGraph(registry,graph,envelope)`. No writes. Full Phase 3 registry used by synthetic integration tests.
## Trust and limitations
Current checks do not yet independently verify `roles.meaning` or EA SQL connector direction/tag provenance. The lexical Phase 4 evidence-key resolver remains provisional; generic `Element` eligibility is broad. Aggregation review gate is never automatically approved. The graph has no separate semantic ownership edge store or insertion validation for arbitrary moves; it checks extant ownerId chains and one proposed aggregation cycle. No official SysML v2 parser, native serialization, BOM reconciliation, rename redirects, manual editing conflict merge or idempotence integration yet.
## Phase 2 corpus reconciliation
838 distinct directed EA endpoint family patterns exist in local fixture. The Phase 3 registry covers only prioritized families (Aggregation, Realisation, Abstraction:allocate, Dependency:satisfy, Generalization, Dependency); every other Phase 2 family remains explicit `UNKNOWN_FAMILY` until registry expansion. The methods repo must not contain per-model identities or source rows. A fixture-local coverage runner should map EA classifier + stereotype to canonical node kinds using the approved element registry, then run each connector through the full engine and write a local-only disposition ledger. Mapping this source via heuristic keywords would produce misleading success statistics, so no per-pattern pass claim is made here.
## Gates to next phase
P0: formal kind registry/EA direction extractor and evidence schema validator; P0: operation simulation for every ownership change and cycle check; P0: automated corpus-local 838-shape summary by rule and diagnostic; P0: full official v2 grammar/library parser conformance; P0: Workbench integration and reimport three-way merge.
Run tests: `node --test 14_Workbench/registry/runtime/*.test.mjs`. Synthetic tests are no proof of golden-import acceptance.
