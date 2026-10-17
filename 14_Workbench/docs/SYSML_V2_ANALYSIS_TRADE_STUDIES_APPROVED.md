# SysML v2 Analysis Cases and Trade Studies — Approved Option A
Date: 2026-10-17
Status: Approved native capability and explicit-evidence EA import; not yet implemented or conformance-validated.
Authority: OMG SysML v2.0 Language §§7.23.2–7.23.3, AnalysisCases standard library and Analysis Domain Library / TradeStudies. https://www.omg.org/spec/SysML/2.0/Language/PDF

## Approved native constructs and distinctions
- AnalysisCaseDefinition and AnalysisCaseUsage (declared with `analysis def` and `analysis`) are specialized case modeling constructs, not arbitrary notes or generic binary relationships.
- Analysis case has an explicitly modeled subject, objective, and return/result features. The objective is evaluated against analysis results; avoid treating a preference statement as a requirement satisfaction or verification result.
- The standard Analysis Domain Library `TradeStudies::TradeStudy` provides trade-off analysis semantics, with alternatives as subjects, an evaluation function, and a study objective (such as MaximizeObjective/MinimizeObjective). The precise library version, dependencies, and syntax must be pinned and validated.
- Reuse approved Calculation definitions/usages, constraints/assertions, attributes, quantity kinds and units. A calculation result is not automatically verified evidence of requirement satisfaction.
- Variation/Variant declares configurable choices; a Trade Study evaluates alternatives. Requirement Satisfaction asserts satisfaction; Verification Case specifies how to verify; a test execution record is distinct historical evidence.
- Persist evaluation outputs, assumptions, input versions, and result provenance outside the reusable analysis definition as necessary, while retaining any native analysis result features in the modeled usage. No ad hoc core v2 relations.

## EA translator
- Identify explicit EA analysis/parametric artifacts, stereotyped analyses, activities/calculations, requirements and tagged criteria; use source evidence to map valid native analysis case definition/usage, subject, objective and result.
- Do not infer a TradeStudy from dependencies, generalizations, product family variants, BOM alternatives, part properties or similarity.
- Preserve EA GUIDs, original classifications, inputs, expressions, assumptions, results, diagrams, ownership and transform rule version.
- If source cannot justify a legal native analysis model, preserve evidence in exception ledger rather than fabricating a case or results. One disposition for every source element/connector.

## BOM translator
- Resolve candidate physical alternatives by canonical definition/part identity; retain BOM revision, quantity, unit and cost source provenance.
- BOM source may provide evaluated parameter values when explicitly supported and versioned, but does NOT automatically assert preference/selection, study conclusion, verification or satisfaction.
- Multiple versions of BOM data should not silently rewrite completed study results; flag stale inputs and offer reevaluation.
- Cross-import reproducibility and idempotence required.

## Vault
- Native reusable AnalysisCaseDefinitions, AnalysisCaseUsages, subject/objective/result features and TradeStudies domain-library references are versioned in the vault with stable IDs.
- Study notes may be separate named artifacts referencing native model elements, selected alternatives, input data, assumptions, calculation results and run/evaluation evidence; source truth and derived evaluation snapshots remain clearly distinguished.
- Analysis Domain Library is included or resolvable in pinned version; define index, qualified names and provenance. No hardcoded engineering attributes or enumerations.

## Workbench
- Dedicated Analysis View: choose a native analysis definition, establish a usage, select subject/alternatives from vault, link objective, assign weighted criteria and evaluation function if supported, inspect outputs, compare alternatives.
- Show a filterable table of criteria, units, normalized values, weightings, assumptions, scores and evidence. A chart may be a view-only projection.
- Define safe editor for native relationships/owned features instead of treating analysis as a generic drawn edge. Drag gesture can initiate selection of subjects or model references where valid.
- In-editor dismissible Definitions panel distinguishes Analysis vs Calculation, Constraint, Variation, Satisfaction, Verification, execution result.
- All views edit same canonical model; filters, charts and study layout are presentation data only. Edits produce preview, validations, undo/redo, and source traceability.

## Validation
1. Native AnalysisDefinition/Usage, subject, objective and return parse and satisfy metamodel.
2. TradeStudy uses pinned domain library `TradeStudy` and compatible objective/evaluation function.
3. Units, quantity types, criteria expressions and weightings validated; missing or incompatible values clearly flagged.
4. Candidate selection does not create variant, satisfaction, verification or allocation by inference.
5. Repeat analysis with same versioned inputs yields reproducible result and appropriately recorded evaluation evidence.
6. Changes to input BOM revision clearly mark results stale; do not silently overwrite.
7. EA import only explicit compatible constructs, all inputs and exceptions reconciled to source IDs.
8. EA/BOM import in either supported order preserves definitions, study usages and provenance.
9. Workbench chart/table/text and preview remain consistent without views changing semantics.
10. Regression against native SysML v2.0 and pinned standard libraries, including known upstream library issues.

## Follow-up tracker
ANA-01 Inventory source EA analyses, parametric models, engineering calculations and decision records.
ANA-02 Build complete metamodel + pinned Analysis Domain Library registry with exact normative syntax and tests.
ANA-03 Implement explicit-evidence EA import and exception/source-ledger classification.
ANA-04 Link BOM alternative identities and versioned input attributes without inferring study semantics.
ANA-05 Vault-native reusable analysis and local study/result/evidence schema.
ANA-06 Workbench Analysis View with alternative/criteria selection and native edit operations.
ANA-07 Workbench contextual Definitions panel entries and distinguish neighboring concepts.
ANA-08 Calculation/units/guard/evaluation type checking; stale-result detection.
ANA-09 Parser, native library, round-trip, reimport and controlled analysis test fixtures.
ANA-10 Cross-link review matrix; identify any manual conversions after real source inspection.

## Known normative caution
OMG 2.1 RTF issue SYSML21-318 describes an unresolved TradeStudy objective redefinition inheritance problem. The project targets released SysML v2.0; pin actual library and record conformance workarounds rather than inventing a different language behavior.
