# STEP-02G — Local flag fallback adapter

Date: 2026-10-18. Status: implemented and synthetic-tested; not yet wired into real vault note writer, Workbench renderer or native parser.

Tool: [v2_flag_fallback.py](../25_Testing/v2_flag_fallback.py). Tests: [test_v2_flag_fallback.py](../25_Testing/test_v2_flag_fallback.py).

The adapter consumes a private STEP-02F disposition CSV with stable connector GUIDs and optional explicit element exceptions JSON. It writes local-only structured flagLink/flagNote review records. It will not reinterpret native candidates as exceptions. No native SysML serialization, QEAX access, diagram processing, source overwrite, or final note YAML emission occurs.

Design constraints: connector GUID is the durable identity for flagLink, element GUID/ID for flagNote; one record per problematic connector; original endpoint order/direction and explanation retained; explicit flagNote required for problematic element, never broad blanket classification. Native candidates remain separately gated. Five synthetic tests cover a flagged relation, native separation, explicit notes, stable reimport, duplicate rejection and output collision.

**Important**: this is a staging adapter, not complete importer integration. Future implementation must enrich records with roles, cardinality, aggregation flags and package provenance from the verified private Phase 8 ledger before writing final MDSE YAML/body notes. Use the source-backed ledger rather than discarding metadata. Workbench structural and visual views must render unresolved items distinctly, with navigation and review/resolve controls. Gate import on data preservation, not zero flags.

Next: connect the adapter to the local v2 note generator and Workbench presentation, then run synthetic end-to-end import. EA diagrams stay excluded.
