# V2 connector-end evidence checkpoint

The read-only extractor is at `21_Importer/v2_connector_end_evidence.py`. The regression is at `25_Testing/test_v2_connector_end_evidence.py`, and the main-branch workflow invokes it.

Usage: `python3 21_Importer/v2_connector_end_evidence.py local.qeax --limit 100`

This produces aggregate counts for populated EA end roles, cardinalities, containment, aggregation flags, end role types, port stereotypes and classifier references. It checks that both endpoints exist. Source direction remains uninterpreted. Evidence presence does not establish evidence correctness or SysML semantic orientation. Nothing is written into the QEAX and native SysML emission remains disabled.

On the reduced source, the first 100 connectors contained 25 blank direction fields, 14 destination aggregation indicators, 1 populated source cardinality and 4 populated source roles. These are a bounded sample, not full-source totals. All 16 Port-typed elements in the full source have blank primary stereotypes.

Next: validate direction and composite-end evidence, parse multiplicity syntax, investigate port classification from classifier and additional tagged-property sources, and connect this evidence to registry-specific gates. Keep unresolved semantics deferred.
