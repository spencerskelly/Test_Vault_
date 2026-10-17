# APPROVED — Native SysML v2 Verification
Date: 2026-10-17
Status: APPROVED — Relationship #19

## Plain-language meaning
A verification case defines how one or more requirements are evaluated. An objective-level `verify` relationship identifies which requirement the case checks. The presence of a verify relationship DOES NOT mean a test has been executed or passed.

## Native modeling policy
- Support native Verification Case Definitions (reusable methods) and Verification Case Usages (context-specific application).
- Support objective-level native verify relationships targeting applicable requirement usages.
- Capture relevant verification methods (inspection, analysis, demonstration, test) and native verdict semantics where appropriate.
- Keep execution-specific actual observations, dates, equipment, outcomes and evidence separately represented from canonical verification definitions; do not overwrite method with test run results.
- Ensure exact syntax and scope legality against conforming SysML v2 parser before production output.

## EA mapping
- Translate compatible EA `«verify»` relationships into native objective-level verification within valid Verification Cases.
- Check the source EA type, target requirement type, owning context and existence of actual verification case. Do not fabricate execution evidence.
- Flag unsupported or ambiguous EA test relations for later correction, rather than changing to satisfaction/allocation automatically.
- EA Copy alias consolidation resolves canonical identities prior to mapping.
- Obsolete EA source links need not be permanently preserved once imported native syntax is correct.

## Workbench
- Structural view: link Verification Case Definition/Usage → objective → verified requirements; reverse index Requirement → verification cases.
- Visual view: distinct `verify` relationship from verification case to requirement, not an ordinary dependency or satisfaction edge.
- Inspector: verification method, subject, objective, test activities, expected criteria, related requirement and evidence references; differentiate defined vs executed vs pass/fail.
- Editors: edits from text/tree/diagram patch authoritative SysML v2 syntax in owner note; refresh all synchronized projections.
- Execution result UI/document links must not silently change the verified requirement relation or test definition.
- Validation: resolved requirement, subject compatibility, objective ownership, method and verdict compatibility, typed end references.
- Canonical reusable definition per type; not every verification usage or result needs an independent canonical definition note.

## Teaching example
Output Voltage Verification Case verifies Voltage Regulation Requirement. A separate test run records measured voltage, criteria, equipment, date, verdict, and artifacts. The `verify` link remains even if no run has happened or a run fails.

## Next relationship
Requirement derivation: native `derive requirement` semantics, derived vs source requirement direction, and distinction from specialization and dependency. Mapping from EA to be approved separately.
