# MDSE v2 — Gated Delivery Plan

**Status:** Working plan, 2026-10-15.

## A — Semantics (steps 1–4)
1. Complete SysML v1 / v2 / MDSE mapping workbook, including BOM concepts and allowed relationships.
2. Approve v2 definitions/usages, ownership, interfaces, connections, multiplicities and configuration model.
3. Review OMG-default translations versus already-approved MDSE reinterpretation, recording exceptions.
4. Finalize standard textual ownership, extraction and cross-note write-back. **Gate A:** no ambiguous basic structural ownership.

## B — Translator (5–7)
5. Normalize EA CSV/QEAX input and provenance through a reusable source model.
6. Translate structure to SysML v2 with deterministic semantic identity and explicit review exceptions.
7. Validate independent parsing, symbols, topology and round-trip semantics. **Gate B:** synthetic golden charger.

## C — BOM integration (8–10)
8. Reconcile BOM Work proposals with native SysML v2 usages, quantity/UOM and revision history.
9. Implement BOM continuation-row alternate rule BOM-ALT-001 and effective configuration selection.
10. Produce BOM / Where Used / revision comparison fixtures and output. **Gate C:** no double count or invented substitutions.

## D — Workbench (11–13)
11. Index and navigate authoritative SysML symbols, usages, and source evidence.
12. Safely create/edit definitions, parts, interfaces and connections through source edits; support undo/review.
13. Provide relationship and structural panels and first read-only diagrams. **Gate D:** engineer can make a valid model edit without hand-writing SysML.

## E — Visual + release (14–16)
14. Add connection routing and controlled graphical editing without a second semantic store.
15. Test system-of-systems, multi-level BOM, scale, rerun and migration against selected evidence.
16. Version/pin the v2 importer, runtime and Workbench with independent validation. **Gate E:** externally valid SysML and usable v2 vault.

## Cross-version governance
A proposed shared capability gets a **v1 + v2 applicability review**. Do not edit or migrate v1 automatically.
