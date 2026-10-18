# V2 connector evidence validation checkpoint

The read-only implementation is `21_Importer/v2_validate_connector_evidence.py`; synthetic regression is `25_Testing/test_v2_validate_connector_evidence.py`. The V2 CI workflow runs the regression on main.

## Actual reduced-QEAX findings

The local full scan reviewed 14,688 connectors:
- Destination aggregate flag 2: 1,670.
- Destination aggregate flag 1: 597.
- Source cardinality present and syntactically valid: 53.
- Destination cardinality present and syntactically valid: 7.
- Port endpoint occurrences missing classifier and stereotype: 18. This is endpoint occurrences, not unique Port elements.
- No populated cardinalities failed the basic grammar check.

These flags do not themselves prove valid SysML v2 ownership or multiplicity. All aggregation and port semantics remain unverified. The checker does not write data or emit native SysML.

## Next

Interpret the EA end-flag conventions with independent evidence, then separately validate semantic direction, composition ownership and multiplicity placement. Investigate port type via additional model evidence rather than silently treating unclassified ports as proxy or full. Confirm the CI run and extend parser tests before native generation.
