# Golden Import Step 2 — EA Part usage

Decision: APPROVED, 2026-10-17.

- Ordinary EA `Part` becomes native SysML v2 `PartUsage`, owned by its containing part/context/assembly; not `PartDefinition`.
- No independent MDSE note for PartUsage. Keep original EA type/stereotype and source provenance in owning model.
- Reduced QEAX contains 7 `Part` rows total: 6 are `Part:FlowProperty`, covered by separate approved item-usage rule; 1 ordinary `Part` (`CTRL`, source ID 92295) is nested under `Ramprunner Context` (source ID 92294; `Class:Physical Context`), ParentID=92294. No ordinary `Part` row is orphaned in this fixture.
- The ordinary Part has classifier=0 (no assigned classifier). Source has two NoteLinks only, which do not imply an instance type.
- Do not infer a reusable definition from the part name. Unresolved typed feature references remain explicit review items for native conformance.
- The 6 FlowProperty elements have ParentID=0 and require separate port ownership evidence; do not conflate with ordinary parts.
- Check native ownership and typing, provenance, and idempotence before import acceptance.
