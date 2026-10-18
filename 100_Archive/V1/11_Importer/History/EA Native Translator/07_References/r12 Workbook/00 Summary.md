---
uid:
type: Info
status: Working
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# r12 — Summary

| Locked rule | Definition |  | Matrix Revision | 2026-09-27 r12 |
| --- | --- | --- | --- | --- |
| Bidirectional YAML | Every approved relationship is written explicitly in both endpoint notes whenever both endpoint notes exist. |  | Change | Participation standardized as one-sided `participants` YAML. |
| No connector notes | Connectors do not become notes. Semantic relationships live in YAML; approved connector detail lives in source/target note bodies. |  | Change | `subject/subjectOf` removed from automatic native import. |
| Collapsed elements | Meaningful incoming/outgoing relationships are transferred to the surviving element; duplicates and self-links are suppressed. |  | Change | Context elements remain source-faithful type during import. |
| Flow-control constructs | Initial/Final/Decision/Merge/Fork/Join/Timer/etc. do not become notes by default; preserve meaning as relationship/body detail. |  | Change | Context→Use Case / Where becomes post-import cleanup. |
| Unresolved semantics | Unknown/unsupported connector semantics go to Review Required; the importer must not guess. |  | Change | Every translator deviation must be revved in the in-model change note. |
| Dropped-data reporting | Any connector data not explicitly ignored must appear in traceability or exception reporting. |  | Change | `refines/refinedBy` retained only for Requirement→Requirement; `defines/definedBy` merged into `describes/describedBy`. |
| Item Flow | Postponed. Conveyed-item evidence remains source-only until Item Flow import rules are defined. |  | Change | BindingConnector → symmetric `equals`; Connector → symmetric `interfaces`. Documented source relationship coverage expanded with explicit missing/deferred patterns and catch-all review rules. |
| Diagram links | EA DiagramLink membership is retained for diagram/canvas imports. |  |  |  |
| Context-local participation | Explicit Use Case/Context participation is stored as one-sided YAML `participants` on the owning Use Case/Context element only. No reciprocal participation data is written to participating notes. |  |  |  |
| Subject handling | The native importer does not distinguish `subject` from `participant`. Existing source participation is imported cleanly as `participants`; `subject/subjectOf` may be introduced later during post-import cleanup if useful. |  |  |  |
| Source-faithful element typing | The native importer does not semantically reclassify elements. A Context modeled as a Block remains its EA-derived type during import. Post-import cleanup may later convert it to Use Case / Where. |  |  |  |
| Translator deviation record | Every deliberate deviation from the original translator must also be recorded in the model-visible `EA Import Changes From Original Translator.md` change note, which is revised as decisions evolve. |  |  |  |
| 2 | Source YAML and Target YAML are always both written for approved pairs. |  |  |  |
| 3 | Connector names/notes/roles/multiplicity/constraints/guards/triggers/effects are preserved in endpoint bodies per the Body Detail Rules sheet. |  |  |  |
| 4 | Where EA connector type is too generic (Association, Usage, trace, allocate), endpoint meaning controls the result. |  |  |  |
| 5 | Rows marked Review or Deferred are not auto-converted. |  |  |  |
| Relationship rule coverage | Full-model source coverage complete. No observed connector type/stereotype remains unrecognized. |  |  |  |
| Full-model completeness | Certified against t_connector/t_object/t_xref: 21,822 connectors; 30 raw connector-type/stereotype pairs; 1,000 endpoint combinations. Every combination has a matrix rule or explicit Review/Deferred/Exception disposition. |  |  |  |
| Completeness rule | Every observed source relationship combination must resolve to exactly one matrix rule or an explicit Review/Deferred/Ignore disposition; unmatched combinations are import exceptions. |  |  |  |
| Full-model connectors | 21822 |  | Observed raw source families | 30 |
| Observed endpoint combinations | 1000 |  | Settled connectors | 14444 |
| Review connectors | 4556 |  | Deferred connectors | 2813 |
| Endpoint exceptions | 9 |  | Missing endpoint connector rows | 9 |
| New verified relation | EA Dependency «verify»: testCase → Requirement → verifies / verifiedBy |  |  |  |
| Custom source relationships | RAAML RecoveryRequirement, RAAML ASILDecompose, StandardProfile Responsibility remain explicit Review items. |  |  |  |
| Completeness result | 0 unrecognized raw connector-type/stereotype pairs after reconciliation. |  |  |  |
