# Decision: EA Function/Design Allocation to SysML v2 Part Behaviors
Status: APPROVED RULE — implementation pending
Date: 2026-10-17
Normative reference: OMG SysML v2.0 Language §§7.17.6 (Perform Action Usages), 7.18.4 (Exhibit State Usages). https://www.omg.org/spec/SysML/2.0/Language/PDF
Supersedes: any default translation of these specific EA allocations as SysML v2 AllocationUsage.

## Approved mapping
1. Existing EA Activity / MDSE Function allocated to an Object, when that activity is the behavior carried out by the object: produce a native SysML v2 PerformActionUsage owned by the corresponding part definition or usage, referencing the corresponding action usage. Keep EA connector provenance.
2. Existing EA Design modeled as EA State, allocated from Design (state) to Object: produce a native SysML v2 ExhibitStateUsage owned by the corresponding part definition or usage, referencing the corresponding state usage. Interpret the engineer-facing association as Object -> exhibited State even though the EA allocation arrow runs Design -> Object.
3. These operations are NOT generic AllocationUsage edges. Reference subsetting to the referenced behavior is part of the native semantic construction. Reuse the intended state/action rather than cloning the referenced shared definition.
4. For incorrect endpoint types, missing state/action, multiple plausible object owners, contradictory role direction, or ownership collision: retain mapping ledger records and original EA tags/connector data; create review flags and avoid fabricating a semantically invalid reference.
5. Other allocation relationships remain eligible for actual native SysML v2 allocation according to their semantics, reviewed separately.

## Example native textual patterns (illustrative)
```sysml
action def RegulateCurrent;
state def ChargingMode;
part def ChargerController {
    perform action regulateCurrent references ChargerFunctions::regulateCurrent;
    exhibit state chargingMode references ChargerStates::chargingMode;
}
```
Resolve valid names/qualified references from model during generation; do not interpret snippets as a complete compilable package.

## EA translator impact
- Inventory t_connector «allocate» and other prior MDSE association rules for Activity -> Object and State/Design -> Object, with actual connector direction and EA identifiers.
- Resolve part definition vs part usage ownership from model context; avoid globally attaching instance-specific behavior to every part of a type.
- Ensure reusable action/state definitions and relevant usages exist before creating referencing features.
- Use deterministic stable IDs for generated features, source EA connector GUID, source/target GUID, original roles/direction, transformation rule version, original stereotypes/tags and source package.
- Produce one disposition per EA connector, including a successful native usage with preserved source metadata or explicit flagged exception.
- Count both source connectors and output feature records; permit one-to-many mapping only with explicit provenance.

## BOM translator impact
- BOM parser produces part/assembly definitions, composition, quantity and units, and variant/revision evidence according to BOM rules.
- Reuse same canonical part identity and feature registry as EA translator; preserve source and BOM-specific provenance independently.
- Do not infer perform/exhibit associations from BOM parent-child, part number, descriptions, or quantities.
- If BOM imports refer to an already modeled object with action/state usages, merge by canonical identity and preserve references; report collisions and source disagreement.
- Add cross-import regression test for stable IDs, untouched behaviors, and same rendered links.

## Workbench impact
- Gesture: drag from either part/object or activity/state onto its intended counterpart; evaluate type/context before offering Perform or Exhibit. Graphic gesture direction does not determine semantic ownership.
- Choose Perform or Exhibit, preview the part that owns the new usage, reference target, source EA evidence if applicable, and generated SysML text.
- Commit canonical native features; maintain editable relationship-style visual projection rather than storing merely a generic edge.
- Allow inspection/edit/repoint/remove with ownership and referential integrity validation; editing all views updates one model.
- Part-centric inspection: performed actions and exhibited states; behavior-centric reverse list of performers/exhibitors.
- Distinguish native allocation, perform action usage, exhibit state usage in legend, filters, export and detail panes.

## Validation/QA
1. EA Design-to-Object allocation -> Object exhibits State; check the EA GUID and direction remain in provenance.
2. EA Activity-to-Object allocation -> Object performs Action.
3. Shared reusable action/state used by several objects -> independent usage per owner, shared referenced behavior; no cloned definition.
4. Definition-vs-usage part object -> owner choice deterministic, or flagged if not.
5. Import EA + BOM in either supported order -> stable canonical part identity and preserved association.
6. Malformed or ambiguous EA endpoints -> clearly flagged, evidence preserved and accounted for.
7. Workbench round-trip graphic/table/text change -> identical canonical model with source provenance preserved.
8. Every source connector accounted for in complete export coverage ledger.

## Follow-up work tracker
- F01 [EA translator]: extract baseline counts and sample source records for Activity/State -> Object allocations.
- F02 [Semantic registry]: implement typed TransformRule IDs for Perform and Exhibit including metamodel constraints.
- F03 [Native model]: canonical definition/usage/ownership/reference schemas and stable IDs.
- F04 [Workbench]: gesture-pair eligible choices; part-first and behavior-first both supported.
- F05 [Workbench]: edit/remove preview and reverse navigation; text/visual sync.
- F06 [BOM translator]: canonical object identity and merge, behavior preservation test.
- F07 [Validator]: complete disposition ledger and exception queue, including EA connector evidence.
- F08 [Conformance]: test generated native text and serialization against SysML v2 tooling and official examples.
- F09 [Docs]: central relationship matrix row with EA old endpoints, SysML new semantic structure, restrictions, exceptions, and acceptance tests.

## Pending review
- Actual SysML v2 AllocationUsage: retain as distinct for genuine allocation semantics not covered by Perform/Exhibit.
- Additional unusual EA design classifications and legacy manually created MDSE connections need representative data review, not automatic coercion.
