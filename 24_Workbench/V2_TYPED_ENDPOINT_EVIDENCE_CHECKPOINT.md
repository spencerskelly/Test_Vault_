# V2 endpoint evidence checkpoint

Implemented a bounded read-only EA connector endpoint type inventory.

Command:

```sh
python3 21_Importer/inspect_v2_source_endpoint_types.py source.qeax --limit 100
python3 -m unittest 25_Testing/test_v2_source_endpoint_types.py
```

Output includes aggregate EA connector types, EA start element types, EA end element types, and missing endpoint counts. No element names, source identifiers, or native SysML statements are emitted.

EA Start/End is preserved as source evidence. It does not establish SysML semantic direction.

The new synthetic regression is in the v2 CI workflow, which now runs on pushes to main.

## Next step

Join typed endpoint evidence with exact connector stereotype rules, then explicitly evaluate generalization direction, aggregation ownership and multiplicity, satisfy/verify roles, and proxy/full port classifier roles. Keep all unresolved relationships deferred and retain the read-only boundary.
