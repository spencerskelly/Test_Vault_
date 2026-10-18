# Pass 7 — Structural parser fixture expansion (2026-10-17)

Following the first independently passing real parser gate (GitHub Actions run 39099574792), added three **synthetic, unverified** positive fixtures to `29_SysMLv2_Translator_Workbench/Fixtures/`:

1. `synthetic_nested_part_usages.sysml` — nested part usages and [1] multiplicity.
2. `synthetic_port_as_part.sysml` — a port definition and a typed port usage owned by a part. This establishes syntax evidence for part-contained ports; it does NOT imply a port is modeled as a part usage or certify Workbench IBD rendering.
3. `synthetic_connection_usage.sysml` — connection usage between two named parts.

Updated manually dispatched `.github/workflows/sysml2-native-fixtures.yml` to parse all three as positive fixtures before exercising the established negative-syntax fixture. **These three files have not yet been run through the actual kernel**; the next CI run may reveal a syntax issue, and that will inform corrections. Do not interpret provisional fixture text as approved syntax.

The registry remains authoritative for eligibility decisions. No EA-to-native relationship translation, semantic endorsement, or native generation is enabled. Next: trigger the workflow on main, inspect each real parser step; resolve parser failures; expand systematically to state/action nesting, redefinition, binding ports and requirements only after this structural baseline is stable. No private model records committed.
