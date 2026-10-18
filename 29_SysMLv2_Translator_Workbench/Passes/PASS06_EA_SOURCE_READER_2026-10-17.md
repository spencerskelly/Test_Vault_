# Pass 6 — Shared EA source reader, first increment

Created `15_Testing/ea_source_reader.py` (commit `0baf7e6`) and `15_Testing/test_ea_source_reader.py` (commit `1b2eb99`). Reader is read-only SQLite, batches source rows, and keeps EA IDs, source orientation, metadata and notes without interpreting any SysML v2 semantics. Categories: element, connector, package and object tagged-value records. Source-specific output must remain outside GitHub.

The local reduced QEAX was inspected directly: t_object 11,447 rows, t_connector 14,688, t_package 1,389 and t_objectproperties 43,634. All required columns exist. This is a schema/count verification, not execution of the committed reader test suite.

Five synthetic tests cover raw orientation, row counting, invalid category, invalid batch size and write refusal. Test execution from full checkout is still pending.

Next increment: source-evidence contract for cross-table references, then a separate BOM Excel adapter returning the same neutral source envelope, not guessed physical ownership. Neither source adapter may auto-approve SysML v2 output. Pass 5 runtime checkout and native parser gates remain open.
