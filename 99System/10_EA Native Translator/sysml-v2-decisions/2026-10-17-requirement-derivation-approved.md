# APPROVED — SysML v2 standard-library Requirement Derivation
Date: 2026-10-17
Status: APPROVED — Relationship #20

## Plain-language meaning
A derived requirement is developed from another requirement through engineering reasoning, analysis or decomposition of needs. The relationship preserves why a more detailed or supporting requirement exists, without claiming that it inherits all the source requirement's constraints.

## Native mapping
Use the standardized SysML v2 library's Derivation connection (`DerivationConnections::Derivation`) for compatible requirement-to-requirement derivation, not an invented `derive requirement` language keyword.
EA `«deriveReqt»` maps when valid and with confirmed derived → original requirement direction.
Validate endpoint roles and library syntax using standard SysML v2 grammar/library/parser before production import; flag ambiguous EA direction instead of silently reversing it.
Source EA connectors are migration material; authoritative model after migration is syntax in Obsidian note.

## Workbench
- Structural: navigate original requirement and all directly/indirectly derived requirements, with their rationale.
- Visual: distinct derivation edge directed from derived to original, not a generic dependency, inheritance, containment or satisfaction arrow.
- Inspector: endpoint roles, owning context, supporting rationale/evidence and validity.
- Any view editing a derivation modifies canonical SysML v2 syntax in owning note(s); structural and diagrams reparse/refresh.
- Avoid duplicate requirement definitions or per-relationship notes.

## Example
A system power-delivery requirement motivates a derived module power requirement and cooling requirement; derived requirements are distinct engineering statements, not inherited subtypes.

## Next relationship
Requirement decomposition / hierarchical requirement membership and how this differs from derivation, specialization and formal satisfaction.
