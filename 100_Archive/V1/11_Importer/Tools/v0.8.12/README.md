# EA to MDSE Native Importer v0.8.12

v0.8.12 builds on v0.8.11 and implements W-376 / IMP-002.

## Change

Uncertain EA relationship evidence no longer becomes canonical MDSE YAML.

Two protections are applied:

1. **Reviewed connector mappings are withheld up front.** If the connector planner already marks a mapping `review: true`, `applyConnectorRelations()` does not add that relationship or its inverse/symmetric mirror to the canonical graph.
2. **Remaining endpoint violations are removed after graph construction.** The importer collects provisional/off-rule relationship findings, records them, then removes the forward edge and its inverse/symmetric mirror before validation and Markdown rendering.

## Evidence preservation

Nothing is silently discarded.

Reviewed connectors remain traceable through:
- EA GUID/type and endpoints in `Review - Semantic and Connectors.csv`;
- connector name/notes/source evidence;
- note REVIEW/source lines;
- specialized review tables where applicable.

The semantic review CSV now distinguishes:
- reviewed source connectors that were never written to canonical YAML;
- off-rule graph relationships that were suppressed before write;
- Local Model/BindingConnector warnings.

The Run Manifest reports counts for the first two groups.

## Why

The v0.8.3 reference model demonstrated that a relationship could be present as authoritative YAML and simultaneously carry a REVIEW warning saying its endpoint types were invalid. Downstream tools cannot safely interpret that contradiction. v0.8.12 makes review evidence non-authoritative until meaning is accepted.

## Validation

- Embedded JavaScript syntax parse: PASS.
- Static ordering check confirms reviewed connectors are skipped before relationship writing.
- Static ordering check confirms endpoint-rule suppression occurs before graph validation/rendering.

A real-QEAX import is still required to quantify the relationship-count reduction and confirm the expected review populations.

## Next semantic decision

IMP-009: decide whether every Local Model endpoint must reference a reusable first-class Port definition, or whether a contextual endpoint may exist with source identity/configuration but no reusable Port note.
