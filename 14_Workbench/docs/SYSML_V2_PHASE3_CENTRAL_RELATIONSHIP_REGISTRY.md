# Phase 3 — Central SysML v2 Relationship and Operation Registry
Date: 2026-10-17
Registry: `14_Workbench/registry/sysml_v2_relationship_operations.v0.1.json`
Status: Machine-readable policy baseline; native grammar and runtime integration NOT yet verified.

## Architecture
A single eligibility engine serves EA translator, BOM translator, Workbench create/edit operations, the Definitions panel, and validation. Its output is an operation preview, never a silent write. Typed graph nodes distinguish canonical Definition versus contextual Usage. The visible relationship may be a native feature/owned usage rather than a binary connector. A valid drawn line **opens an eligible operation chooser**; drawing itself does not authorize a native edge.

Rule evaluation: source family and stereotype -> priority/exclusion -> endpoint kind compatibility -> orientation -> required semantic evidence -> ownership -> native construct -> schema and native parser -> staged preview -> commit. Ambiguity yields `deferred_review` and retained provenance, with no semantic mutation. A missing mapping is not a generic Dependency.

## Distinctions
- Aggregation creates parent-owned typed usage only when source ownership is established; shared definitions remain reusable. Relationship multiplicity is contextual, BOM quantity/UOM separate.
- Realisation to Requirement follows the previously approved Allocation direction if evidence supports it; it is **not** automatically Satisfaction.
- Object-to-Object Realisation maps to Allocation only if true implementation correspondence is supported; otherwise source evidence.
- Action/State allocation must use owned Perform/Exhibit when its approved source pattern matches; precedence prevents degrading to generic Allocation.
- Satisfy requires explicitly compatible requirement and satisfying subject; is neither Verification nor Allocation.
- Generalization maps to definition specialization without auto-redefinition or instance duplication.
- Plain Dependency can be native Dependency; trace/refine/recovery and other EA stereotype extensions require individual explicit handling.

## Workbench requirements
Structural tree displays owning namespace, feature usage and reusable definition references, plus side panels for source evidence and validation. Visual views project those same canonical identities, with distinct symbols and labels for specialize, owned usage, allocation, perform, exhibit, satisfy and dependency. Selection of line endpoints filters menu based on rule eligibility. Info/help explains why a candidate is disabled, and navigation exposes both directions, membership, owner and where-used. Undo/redo and Git diff touch canonical model, never only Canvas. Round-trip changes must preserve source links and individual rule IDs.

## Provenance and versioning
Persist rule registry version, rule ID, source GUID, original endpoint/direction/stereotype and evidence, canonical target ID, relationship/feature ownership, review decision, parser/library version and generated artifact hashes. Use EA/BOM/MDSE field ownership and three-way merge per Phase 1. No real model content belongs in this methods repository.

## Blockers to mark as NOT implemented
1. Exact SysML v2.0 grammar API binding and pinned libraries not established; registry `native` labels are candidate constructs, not literal syntax renderers.
2. Endpoint eligibility arrays are broad semantic categories, **not** a complete certified metamodel type system. Expand with subtype hierarchy and official legal-ownership constraints.
3. Runtime eligibility engine, Workbench menu and parser adapter are not yet wired.
4. Per-connector row evidence and 838 endpoint pattern reconciliations remain to be run locally.
5. Realisation / Aggregation / trace / refine / unexpected allocation need operator disposition, not guessed defaults.
6. Automated idempotence, BOM-order convergence, three-way merge and view round-trip need test fixtures.

## Acceptance test definitions
A1: Endpoints invalid -> no mutation and precise failure code.
A2: One shared definition typed by two parent-owned usages -> one definition and two usages; where-used correct.
A3: Part cardinality != BOM purchase/length/weight quantities.
A4: State-to-object source allocation -> Exhibit; action-to-object -> Perform; generic allocation only after exclusion rules.
A5: Realisation to Requirement never generates Satisfaction without separate explicit evidence.
A6: Trace/refine stereotype never automatically maps to generic Dependency.
A7: Generalization orientation and acyclic specialization verified.
A8: Workbench canvas line, menu, structural tree and native textual model project same target IDs and operation.
A9: Identical reimport yields empty semantic diff and preserves manually maintained annotations.
A10: Official native parser rejects illegal ownership/typing, and approval blocks deployment.
