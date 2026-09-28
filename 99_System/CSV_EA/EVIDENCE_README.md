# EA Comprehensive Evidence Bundle

Generated directly from the selected `.qea`/`.qeax` file. No manual Enterprise Architect CSV export is required.

## Start here

- `extract_manifest.json` — source fingerprint, build, options, and row counts.
- `table_inventory.csv` — which high-value EA tables were present and their schemas.
- `connector_endpoints_enriched.csv` — primary relationship-analysis file with human-readable source/target context.
- `relationship_pattern_summary.csv` — recurring connector patterns for translator rule review.
- `element_connectivity_audit.csv` — direct plus embedded-child connectivity, diagram placement, notes and tagged values.
- `package_coupling.csv` — package-level internal/incoming/outgoing coupling for segmentation.
- `requirement_connectivity_audit.csv` — requirement-specific connectivity evidence.
- `invalid_connector_endpoints.csv` — connectors with zero or unresolved endpoints.

## Raw evidence

Core translator tables are always exported. Additional EA tables such as `t_xref`, `t_attribute`, connector tags/constraints, operations, scenarios, tests/risks/problems/metrics/effort, project issues/tasks, glossary entries, documents and files are exported when present. Diagram geometry and link routing are included only when diagram-derived outputs are enabled.

The raw files are evidence, not MDSE semantics. Use translator rules and reconciliation reports to decide how each EA pattern should map.
