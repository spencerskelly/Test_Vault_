# Pass 5 — Semantic candidate differences

Created machine-readable decision register `14_Workbench/registry/sysml_v2_semantic_decisions.v0.1.json` (commit `cf39550`). It classifies all eleven source-versus-v2 candidate differences: four unspecified-to-candidate (allocation, aggregation, satisfy, generalization); two evidence-only labels (Connector and NoteLink); three straightforward vocabulary-normalizations (deriveReqt, use-case extend, use-case include); and two substantive semantic choices (Association and ControlFlow).

Classification is provisional; even vocabulary-normalizations still require endpoint/context evidence and independent native v2 parser validation. All eleven records explicitly prohibit native emission, preserve source provenance, and specify Workbench structural, visual, navigation, validation and round-trip obligations. The existing relationship registry remains unchanged.

A proposed automated consistency test file was blocked by the repository write interface. It was not committed or executed. Next pass should add it and check exact set coverage, no native emission, source registry parity, and evidence-only treatment. No real model data or source GUIDs were committed.

Release state: NO-GO. Reply y for next pass.
