# Pass 7 — First passing official native SysML v2 parser CI gate

GitHub Actions run: https://github.com/spencerskelly/Test_Vault_/actions/runs/39099574792/job/117592893088

Observed completed job steps (2026-10-17 Pacific / 2026-10-18 UTC): checkout success; Java 21 success; isolated Conda success; official SysML kernel install success; five diagnostic-classifier tests passed; positive fixture accepted; invalid fixture rejected; cleanup success.

**Positive fixture** `synthetic_part_definition_usage.sysml`: SHA-256 `6c1c8ab627bdf814a6b85d0140e62a6de8f8c5cc691e2cfb0ca7884cb373f130`, Jupyter `execute_reply=ok`, IOPub `execute_result=1`, no IOPub errors, no stream diagnostic categories, `status=ACCEPTED`.

**Negative fixture** `synthetic_invalid_syntax.sysml`: SHA-256 `d0b0031d219f45a99cd8a3e014c55a4d14c3d9206e0d2cb83c40435c857bb0b6`, Jupyter `execute_reply=ok`, three parser diagnostic stream messages, three `error_marker` and three `parser_recovery` category hits, `status=REJECTED`.

**Decision:** Close the first independently executed **positive/negative native parser fixture baseline** gate only. This confirms a functional Linux parser runner and diagnostic classification on the two synthetic fixtures; it does NOT establish a full SysML v2 conformance suite, semantic equivalence to EA relationships, definition/usage correctness across all supported types, round-trip validation, nor production-source eligibility. Parser statuses derive from kernel protocol plus classified textual diagnostics, not a standardized structured diagnostic API. False-negative and false-positive risks remain for other messages or severity formats. Keep `nativeCertified=false`, native emission disabled, source data and ledgers outside GitHub.

**Next:** Add additional valid/invalid synthetic fixtures for port-as-part, part usage, connectors, redefinition, multiplicity, nested state/action, typed requirement/verification, and inspect whether stream/display/result diagnostic channels are handled consistently. Then add provenance-preserving canonical model generation under independently approved eligibility registry rules. No proprietary model rows or GUIDs should be committed.
