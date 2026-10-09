# EA to MDSE Native Importer v0.8.13

v0.8.13 builds on v0.8.12 and implements W-377 / IMP-009.

## Change

Contextual EA Port occurrences no longer force the importer to create reusable first-class Port notes when no reusable Port definition is deterministically supported.

The resolution order remains conservative:

1. If `PDATA3` identifies a Port on the reusable block, reuse that Port definition.
2. Otherwise, if exactly one Port on the reusable block has the same non-blank name, reuse that Port definition.
3. Otherwise, preserve the EA Port as a Local Model 0.3 contextual endpoint with no `definition`.

The third case is no longer an "added Port" operation. No synthetic reusable Port note is created merely to satisfy Local Model storage.

## Local Model 0.3

v0.8.13 requires the selected base vault to carry `local-model.yaml` schema 0.3.

A definitionless contextual endpoint still preserves:
- stable local identity;
- containing owner / part / endpoint placement;
- source identifier;
- endpoint kind;
- multiplicity evidence;
- Local Model topology where the source supports it;
- source-map provenance.

A definitionless endpoint does not carry `usage`; variant/option semantics require a reusable definition.

Local Model 0.2 semantics are unchanged. Workbench compatibility for schema 0.3 is therefore a release dependency rather than an in-place reinterpretation of 0.2.

## Connector boundary

A note-level canonical relationship is not written when one of its connector endpoints is contextual-only and therefore has no first-class note key. Those connector plans are explicitly marked review-only instead of being silently skipped.

Supported occurrence-level Connector, BindingConnector, and flow topology continues to be reconstructed from EA source IDs into the Local Model.

## Review evidence

`Review - Definitionless Local Endpoints.csv` replaces the old `Review - Added Ports.csv` output for this condition.

It records the EA Port, reason no reusable definition was selected, owning note/local ID when materialized, assembly/block context, and available block Ports.

The run manifest also reports the count of definitionless contextual endpoints.

## Validation

- Embedded JavaScript syntax parse: PASS.
- Static regression checks verify Local Model 0.3 output, no synthetic `portgroup:` entities, no endpoint suppression, explicit review handling for note-level connectors, and the new review-evidence boundary.
- Workbench schema-0.3 compatibility is tracked independently and must pass before this importer candidate is release-ready.

A targeted browser run and fresh real-QEAX import are still required before IMP-009 can be closed.
