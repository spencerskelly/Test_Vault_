# Golden Import Phase 2 — EA Family and Endpoint Semantic Coverage
Date: 2026-10-17
Status: Source-family inventory and candidate mapping completed; no generated SysML parser conformance claimed.

## Fixture boundary
Read-only reduced QEAX SHA-256 `69222c060a81b3e35a3e25f365f2a1f4c3dd6eaa19d77fbbd5ba9abdf365a822` (local, excluded from repo). 11,447 elements, 14,688 connectors, 60 distinct (type, stereotype) element families, 26 connector families, 838 distinct directed endpoint-family patterns, 0 missing connector endpoints.
Element candidate-class counts: 7,206 conditional native; 1,807 require manual classification; 1,388 package placement review; 930 evidence review; 116 deferred inference.
Connector candidate-class counts: 8,549 conditional native; 5,910 manual classification; 229 evidence review. **Candidate classification is not a claim of successfully translated records.**

## Endpoint-pattern semantic controls
Use directed key (connector type, stereotype, source object type, source stereotype, destination object type, destination stereotype) plus original direction, source/dest roles, cardinality, aggregation flags and tags. Endpoint family alone cannot prove ownership or meaning.
Key observed patterns and review implications:
- Hardware Component -> Hardware Component Generalization: test specialization direction and shared-definition identity.
- Logical Signal -> Logical Signal Generalization: prove item specialization, not electrical connectivity.
- Hardware Component -> Module and Hardware Component -> Hardware Component Aggregation: determine owner, part usage multiplicity versus source association and shared references.
- State:System State -> Requirement:designConstraint `satisfy`: validate legal satisfaction direction and do not infer allocation.
- Software Component -> functionalRequirement Realisation: require explicit approved interpretation; not automatic satisfaction.
- State:System State -> Hardware Component `allocate`: distinguish ExhibitStateUsage from generic Allocation per approved policy.
- Activity:Hardware Function -> Hardware Component `allocate`: distinguish owned PerformActionUsage from generic Allocation.
- Requirement:designConstraint -> same `refine`: maintain explicit refinement evidence; not silently derivation.
- UseCase -> UseCase `include`/`extend`: reconstruct intended use-case behavior, not arbitrary Dependency.
- Aggregation Class:block -> Class:System Partner: inspect externality and ownership before turning partner into contained part.

## Required import implementation
1. Exact source ledger: every EA row gets unique disposition and canonical target references or a typed, actionable exception. Family-level classifications alone cannot close coverage.
2. Build shared relationship/operation eligibility registry with typed endpoints, owner requirements, source evidence, native construct, semantic action, visual presentation, validation and provenance; distinguish modeling approval, implementation and parser verification.
3. Use evidence-gated deterministic decisions, no generic fallback converting unknown association or trace into Dependency; exceptions are retained separately.
4. Define distinction between initial source `satisfy` and approved Object Realization -> Requirement Allocation policy. Legal semantics, rather than stereotype spelling, win.
5. Avoid EA source package-driven MDSE placement. Canonical reusable definitions, parent-owned usages and distinct view artifacts; stable GUID-to-target reconciliation.
6. Verify native syntactic examples with pinned SysML v2.0 parser/library; no unsupported custom core relations.
7. Keep model data and 838-pattern source corpus output outside this methods/tools repository; store only mapping rules, specifications and aggregate metrics here.

## Open ambiguities and implementation gaps
P0: Aggregation ownership flags and multiplicity (2,267); Realisation endpoints (884 including stereotyped variant); 596 `refine` and 414 `trace` dependencies; 395 Association; 597 include/extend UseCase relationships; atypical Allocation state/function context; 26 family rule certification; 838 endpoint shapes need per-shape diagnostics.
P0: SysML v2.0/KerML formal registry and grammar conformance not yet implemented; source-wide exception ledger and Workbench native editing not yet implemented; reimport idempotence, three-way merge, BOM/EA consistency and native round trip not tested.
P1: Automatic Variation/Variant and Redefinition deferred; advanced feature set operations and Analysis/Trade Study editing pending.

## Next acceptance thresholds
Family inventory 60/60 and 26/26 **meets inventory gate only**; require 838/838 endpoint shapes either evidence-validated for native translation or explicitly review/deferred/evidence-only, then 26,135/26,135 source rows ledgered, before golden-import certification. Acceptance requires official parser, round-trip and staging/reimport validation.
