# Approved EA Object and Generalization translation rule
Date: 2026-10-16
Status: APPROVED. Supersedes the pending conditional-translation proposal in 2026-10-16-ea-generalization-import-audit-pending.md.

## Import defaults
1. Every EA element whose Object_Type is `Object` is initially imported as a reusable SysML v2 `part def`, rather than as a part usage/instance. This is an intentional project-level convention; retain original EA type, stereotype, GUID, name and classifier linkage in source metadata.
2. Every EA `Generalization` is initially represented as SysML v2 specialization. This is a default mapping, not a claim that every EA edge was correctly authored or is semantically valid. Retain EA GUID and endpoints.
3. Workbench supports changing a translated relationship to a more suitable native SysML v2 relationship (e.g. subsetting or redefinition), or a usage-typing/containment structure when necessary. Conversion is explicit, validated, reversible/audited and must not erase source evidence.
4. A small number of EA Objects may later be reclassified as usages/instances manually. Preserve links and dependent references during migration.
5. Never silently emit syntactically/semantically invalid v2. If source types/contexts cannot support a specialization, show it as a pending validation finding with the default intent retained, and do not claim a compliant export.

## Workbench
- Source EA facts are immutable provenance; target relation is editable mapping.
- Structural view: definitions vs usages; inheritance, subsetting and redefinition distinct; original vs effective relation and validity; definition links survive Object reclassification.
- Visual view: inheritance symbol for default generalization; when user changes classification immediately update edge notation, inspector, tree and generated text.
- Inspector: EA connector GUID, original endpoints, original type; mapped v2 construct; rationale, validation state, review status, decision author/date, history.
- Bulk actions: filter Generalizations and Objects; validate and reclassify individually or in reviewed batches; preview affected edges; undo.
- Track source counts, converted counts, exceptions and invalid-specialization findings.
- Golden tests: Object→Class originally modeled as Generalization, Object→Object, State→Activity, mixed stereotypes, compatible definition specialization, changed-to-redefinition, changed-to-subsetting, reclassification to usage.

## Vault guidance
Maintain a user-readable relationship catalog with definition, use conditions, examples, anti-patterns, EA origin, v2 representation, MDSE note relationship, structure/tree display, diagram display and validation.
