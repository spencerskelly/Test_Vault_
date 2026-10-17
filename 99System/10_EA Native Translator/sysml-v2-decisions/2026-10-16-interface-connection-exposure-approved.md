# Approved rule: Interface, Connection, and Exposure

Date: 2026-10-16
Status: APPROVED — semantic separation (Option A)

## Definitions and translation intent
- Port: system/part-owned interaction point represented using native SysML v2 port definition/usage.
- Connection: native SysML v2 connection definition/usage, connecting features.
- Interface: native SysML v2 interface definition/usage, a specialized connection with port ends. Do not collapse an interface into a port.
- Exposure: translation/workbench concept indicating how a higher-level boundary port makes an internal feature accessible. Exposure is NOT approved as a custom SysML v2 relationship or assumed to be a binding.

## Decision boundary
- Approved: preserve three distinguishable concepts and use native SysML v2 constructs where semantics permit.
- OPEN: select exact native SysML v2 feature/connection construct(s) for particular exposure scenarios after checking specification and examples. If semantics cannot be represented natively, record in separate extensions/metadata section; do not invent a SysML v2 keyword.
- Existing EA ProxyPort/FullPort classifications require semantic review rather than blanket conversion.

## Workbench structural view
- Port ownership and nested structure, distinct connection usages and interface usages.
- Show external port -> internal implementation trace path without asserting unsupported equivalence.
- Preserve EA GUID, source stereotype, type, owning context, and mapping evidence.

## Workbench visual view
- Display boundary ports on their owning system/part boundary.
- Render native connections and interfaces as distinct selectable objects.
- Provide drill-down/navigation from exposed port to internal feature implementation.
- If exposure mechanism remains unresolved, distinguish illustrative visual trace from actual SysML v2 model relation, label unresolved and prohibit lossful export.

## Acceptance criteria
- Imported port/interface/connection retain identity, ownership and type.
- In diagrams, selecting each feature opens matching structural element and inspector.
- Semantic validation checks port ends, context, reference integrity and consistency after edits.
- Round-trip only claims fidelity for constructs verified to be expressible in SysML v2.

## Next mapping review
Definition specialization vs usage subsetting vs usage redefinition, including workbench hierarchy/inheritance and contextual override.
