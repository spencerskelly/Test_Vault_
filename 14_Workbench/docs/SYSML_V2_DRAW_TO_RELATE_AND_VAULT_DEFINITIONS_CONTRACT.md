# SysML v2 Workbench and EA Migration — Approved Interaction Contract
Status: approved direction, implementation pending
Date: 2026-10-17
Authority: OMG SysML v2.0 Language, Transformation, and relevant KerML libraries
Reference: https://www.omg.org/spec/SysML/2.0

## Decision records
- DR-001: Workbench uses draw-line-first interaction. From source element or feature to target element or feature, release the line and display eligible semantic operations filtered by actual source/target context. Never treat the gesture as itself establishing semantic direction. The chosen native operation drives textual model, structure, and graphical representation.
- DR-002: Native SysML v2 binding semantics are approved. Do not substitute arbitrary `exposes` links for bindings; where an EA relation cannot genuinely be represented by binding, retain source evidence and flag the exception.
- DR-003: Import all EA elements and connectors with deterministic mapping disposition and provenance. No silent drop, invented type, or automatic reclassification not supported by evidence. Track exact input counts, produced outputs, and explicit exceptions.
- DR-004: SysML v2 and KerML determine semantics; supporting concepts may be added in a separately identified extension namespace/registry, never misleadingly labeled native.
- DR-005: Engineering model definitions, usage instances, attribute definitions, enumeration definitions and literals, unit/quantity definitions, and permitted values are represented within the Obsidian vault in an authoritative machine-readable format. Workbench derives menus from this registry; no hardcoded engineering enumerations.
- DR-006: Engineer usability and navigable structural, graphical, tabular, and text views are first-class requirements; all views edit the same canonical model rather than maintaining divergent copies.

## Relationship creation sequence
1. Start a drag at an element, port, feature or relationship endpoint.
2. End on another valid hit target.
3. Resolve canonical model identities, owning namespaces, definitions/usages, role, direction, context, inherited features, and relevant constraints.
4. Query a semantic operation registry keyed by the standard metamodel and model version. Include connection, binding, feature typing, membership, specialization, subsetting, redefinition and other operations only when the gesture makes sense; some operations require an additional owner or intermediate element.
5. Show only eligible operations (alphabetic initially), with short native meaning and optionally a suggested/common section later. Explain why an operation is unavailable on request.
6. Preview owning location, generated/updated features, direction, syntax, graphical form, and validation consequences. Accept/cancel, never commit an ambiguous edge implicitly.
7. On accept, make one atomic change to canonical vault model; refresh text, graph, tables, backlinks, and provenance. Support undo/redo, Git diff, validation, and round trip.
8. Preserve distinction between a feature-to-feature binding and a structural connection; don't flatten all operations to a two-ended generic graph edge.

## Attributes and enumerations
- Definition, usage and assigned value are separate concepts.
- The vault registry holds semantic type, namespace, declared members, values/literals, quantities, units, dimensional constraints, applicable contexts, and source/provenance.
- Attribute picking: filter applicable definitions/usages by type and context, show qualified names for collisions; sort alphabetically.
- Enumeration value picking: only show literals of the effective enumeration type, including valid inherited values according to semantics. Preserve stable identifiers across renames.
- Later ranking can put frequent/context-compatible items first without bypassing validation.
- A change to a shared definition updates all projections and triggers validation of dependent usages; no implicit coercion.
- Provide forms and underlying SysML v2 text for inspection/editing, plus diff and impact preview.

## EA mapping coverage ledger
Every source row in t_object and t_connector and relevant source artifacts must have:
- source kind, ID/GUID, original EA type/stereotype, owner, endpoints where relevant, original notes/tags, source model identifier and extraction version;
- target canonical model ID(s), target SysML v2 construct and exact semantic rule ID/version;
- disposition: exact-native, native-with-preserved-source-metadata, modeled-extension, ambiguous-mapped-with-flag, or explicitly excluded (with rationale);
- warning/flag severity, original evidence snapshot, suggested repair, round-trip provenance, validation results.
- Reconcile input total with disposition counts, independently checking no missing/duplicated source records. Many-to-one and one-to-many mappings require explicit trace links.
- Do not confuse complete row-accounting with native semantic equivalence. Non-conformant EA input must remain identifiable.

## Viewing and editing
- Structural hierarchy: ownership, definition/usage, inherited members, composition and referenced usages.
- Visual: standard diagram-specific graphical notation and editable endpoints.
- Relationship-centric view: incoming/outgoing relations with semantic type, roles, validation, and provenance.
- Attribute/table view: editable values, units, enumeration dropdowns, type navigation.
- Native textual view: editable SysML v2 backed by parse/semantic validation and canonical sync.
- EA evidence overlay: provenance and flagged ambiguities available without polluting canonical standard semantics.
- All views show references to same identities, support find/navigation and explicit edit preview, and cannot independently alter meaning.

## Acceptance tests
1. Draw port-to-port: present only semantically permitted operations; choose binding and verify native structure and text and reverse-navigation.
2. Draw between incompatible features: no invalid commit and clear reason.
3. Change a vault-defined enumeration: all selectors refresh and existing invalid values flag.
4. Two same-named attributes in different packages: qualified distinguishable choices.
5. Import one source EA connector that maps to multiple native semantic features: all output IDs trace to source GUID, correct count reconciliation.
6. Import invalid EA connector: preserve evidence, mapping disposition and visible flag; no silent conversion.
7. Modify model from graphic/text/table view, then reopen all views: identical canonical model and Git diff.
8. Validate native notation and semantics against OMG SysML v2.0 and transformations against official standard; exception register for unsupported cases.

## Implementation order
1. Inventory existing registry, model files, views and API surfaces in Test_Vault_.
2. Create a machine-readable metamodel operation catalog keyed to official SysML v2/ KerML constructs with normative references.
3. Create vault-native definition and value registry and indexing.
4. Implement endpoint resolution and eligible-operation query.
5. Add drag gesture + operation chooser and live preview.
6. Implement canonical edits and graphical/text synchronization.
7. Implement all-source EA reconciliation ledger and warnings.
8. Add automated conformance, migration, view-coherence and round-trip tests.

## Open verification
- Audit every approved mapping against formal language and v1-to-v2 transformation specification, including exact modeling of boundary ports, feature binding, nested states/actions and legacy EA connector variants.
- Decide display conventions separately from semantics.
