# Phase 9 — Verified nested hardware-component parent evidence

Read-only October 15 reduced QEAX audit (14,688 source connectors). Among the 1,677 same-stereotype generalization candidates, 16 endpoint appearances involve 8 distinct nested EA elements (source appearances 9, target appearances 7).

**Observed aggregates:** all 16 nested appearances have parent `Object_Type=Class`, `Stereotype=Hardware Component`; all 16 have an extended element stereotype record in `t_xref` (`Type=element property`, `Name=Stereotypes`); 0 of 16 have nonempty classifier references. All 16 occur in Hardware Component generalizations. The 16 figures are appearances and can repeat the same element.

These observations support consistent source conventions, **not** native definition qualification. Nesting is compatible with nested definitions or part usages. A recorded stereotype does not validate intended SysML v2 declaration semantics. Do not use this evidence to create usages, convert generalization to containment, or certify native syntax.

Next acceptance step: locally parse the `t_xref.Description` stereotype property payload for just these eight distinct elements, normalize stereotype identifiers/names without exporting identifiers, and compare parent and child declaration context. Count distinct elements separately from edge appearances; preserve approved Binding Port and port-as-part semantics.

Workbench: show both source generalization and lexical nesting in structural view; keep specialization separate from part containment on diagram; allow navigation to source and parent; annotate unresolved definition-versus-usage with evidence/provenance. Native emission stays disabled.