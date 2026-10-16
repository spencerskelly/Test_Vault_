# MDSE v2 — Structural Mapping Contract

**Status:** Draft for Gate A review (not approved mapping authority)  
**Scope:** SysML v1/EA structure → canonical SysML v2 structure while preserving current main-element-to-note mapping.  
**Updated:** 2026-10-15

## Governing principles

1. Markdown notes continue to represent the primary MDSE elements; names and folder positions are navigational, not formal ownership.
2. Native SysML v2 declarations, not frontmatter relationship lists or v1 Local Model records, are authoritative for structure and formal relationships.
3. Distinguish **definitions** from **usages**. A reusable part definition is not a use of that part inside an assembly.
4. Interpret each EA construct through its original metaclass, stereotype, owning context and classifier. No blanket transform based on the displayed MDSE note type.
5. Preserve source GUID, row IDs, attributes and unconverted semantics as audit evidence. Unknown structure never becomes an invented canonical assertion.
6. Workbench views and reverse navigations are derived, never independent editable copies.
7. Proposals applicable to v1 require explicit approval and separate v1 tests.

## Initial structural mapping decisions to validate

| Concept | EA / SysML v1 source evidence | Candidate native v2 meaning | Note and ownership rule | Status |
|---|---|---|---|---|
| Reusable physical definition | Block/Class with block semantics | `part def` | Retain its MDSE Object note; it owns a declaration | Candidate |
| Contextual component | Part typed by a reusable block | `part` usage typed by its definition | Owned by its containing assembly/context, not a second reusable definition | Candidate |
| Composition vs reference | Part property aggregation and multiplicity | Composite or referential usage, preserving upper/lower bound | Never infer composition from folder nesting | Review |
| Port boundary | SysML v1 ProxyPort / typed port | Port usage / port definition as appropriate | Keep owning context, direction and typing | Review |
| Full port | SysML v1 FullPort | OMG-guided part usage translation and related metadata | Do not indiscriminately convert to port usage | Review |
| Interface block | SysML v1 InterfaceBlock | Port definition in standard translation | Not automatically a SysML v2 interface relationship | Review |
| Connection | EA Connector between contextual endpoints | Native connection/interface/flow construct according to source semantics | Belongs to context declaring the endpoints | Review |
| Binding | BindingConnector | Binding/equality semantics where valid | Never silently infer connection or exposure | Review |
| Specialization | Generalization | Native specialization | Distinct from ownership and BOM similarity | Candidate |
| Package / namespace | EA package path / namespace | SysML namespace and owning membership | File folder does not define model namespace | Review |
| Manufacturing BOM line | Parent/child BOM use | Parent-owned part usage, with effectivity | Preserve revision/quantity ledger separately | Candidate |
| Alternate manufacturing line | Blank internal part number, populated manufacturing number | Candidate selection/variation, subject to qualification | Associate to preceding eligible primary line; do not double count | Candidate |

These are **proposed mappings** awaiting checked OMG transformation rule references and an independent parser fixture. They are not normative claims about every v1 source occurrence.

## Source-to-target mapping record (mandatory fields)

- `sourceKey`: source snapshot + source GUID/row.
- `sourceKind`, `sourceStereotypes`, `sourceOwner`, `sourceClassifier`.
- `targetNoteUid`, `targetQualifiedName`, `targetDeclarationKind`.
- `translationDisposition`: standard / approved-variation / review-required.
- `mappingRuleId`, `standardReference`, `confidenceEvidence`, `lossOrExtension`.
- `relationshipEndpoints` with formal owning context.
- `reviewOwner`, `reviewReason` when unresolved.

## Golden charger fixture — minimum coverage

A **Charger** definition with a **Controller** and **three PowerModule** usages, with their own reusable definitions. Each part exposes a typed boundary and connects through resolved contextual endpoints. The parent assembly also owns two contactor uses, with two manufacturer alternates listed as non-additive selection candidates. Represent each BOM effective revision without creating revision-specific duplicate part-definition notes.

### Gate A criteria

- Exactly one authoritative declaration for every created structure assertion.
- Source-faithful ownership, classifier, multiplicity and connector meaning.
- Native syntactic declarations generated and independently parsed.
- No duplicate BOM quantities caused by alternate rows.
- No v1 schema changes as a side effect.
- All path references in v2 documentation point to current numbered directories.

## References

- [V2 mapping / conformance worklist](Mapping%20and%20Conformance.md)
- [V2 BOM rules](BOM%20Integration.md)
- [V2 delivery plan](V2%20Delivery%20Plan.md)
- [V2 translator research](../29_SysMLv2_Translator_Workbench/README_SysMLv2_Translator_Workbench.md)
- [OMG SysML specification portal](https://www.omg.org/spec/SysML/2.0)
