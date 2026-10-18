# Pass 6 — Deferred EA ownership stereotype review

Date: 2026-10-17. Local read-only reduced QEAX; no native SysML v2 approval.

## Complete gap accounting

Of the 2,267 Aggregation connectors, the Phase 8 broad candidate set contains 1,408 and the stricter expanded taxonomy 1,195: exactly **213 deferred connectors**. An independent local SQLite analysis identifies these mutually exclusive *connector category sets*:

| Deferred category set | Connectors |
|---|---:|
| Physical Context | 73 |
| System Partner | 42 |
| Software Component | 41 |
| Unstereotyped Class | 16 |
| Platform | 8 |
| Physical Context + System Partner | 27 |
| Physical Context + Software Component | 4 |
| Physical Context + Platform | 1 |
| Platform + Software Component | 1 |
| **Total** | **213** |

An endpoint occurrence tally counts *both ends*, not distinct connectors: Physical Context 105; System Partner 100; Software Component 73; unstereotyped Class 16; Platform 10. Do not sum endpoint occurrences as connectors.

## Proposed semantics and explicit decision gates

- **Physical Context:** preserve use case/context semantics. Do not infer part composition from source Aggregation. Evaluate whether an EA context object should be represented by a SysML v2 use case, occurrence/usage, or separately retained context evidence, subject to actual source definition and approved relationship rule.
- **System Partner:** preserve actor/external participant distinction and structural system-boundary membership. Do not turn external actors into owned parts by default.
- **Software Component:** candidate software definition/usage or logical decomposition *only when evidence supports it*. Never automatically treat as physical PartDefinition from stereotype alone. Validate language-native construct and allocation/realization relationships.
- **Platform:** unresolved product/platform classification. Distinguish platform reference, generalization, variant, and actual owned part with traceable evidence; do not create an owned usage yet.
- **Unstereotyped Class:** no inferred target concept; require source-context or operator review.

These categories are **review proposals**, not approvals of native v2 mappings. No new custom v2 relationship is authorized. Genuine source concept evidence must determine the v2 construct or placement in a separate, non-v2 extension section.

## Workbench obligations for each reviewed category

Structural view must display definition vs usage, containment vs connection, and external/reference boundaries without silently converting connectors. Visual view must distinguish context, software, platform and ambiguous classes from physical part boxes; preserve native part/port distinction. Navigation must reveal source element, original endpoints, EA stereotype and pending rule; validation must show why each connector remains deferred; round trip/provenance must retain source IDs and rule version locally. Cross-source BOM linkage requires explicit identity adjudication.

## Artifacts and acceptance

- `15_Testing/audit_deferred_owner_stereotypes.py` commit `0fd5138`: aggregate-only source taxonomy accounting.
- `15_Testing/test_audit_deferred_owner_stereotypes.py` commit `a7cb6fc`: seven synthetic tests.
- Local SQLite analysis produced the aggregate table above; **the exact committed files have not been executed in a full checkout**.
- Model-specific ledger, GUIDs and source files were not committed. NativeCertified=0. Pass 6 remains open.

Next: execute exact committed suites, review the candidate categories against full SysML v2 specification and approved MDSE rules, then make *explicit* mapping decisions before changing eligibility.
