# Golden Import Step 2 — EA Actor

Decision date: 2026-10-17. Status: APPROVED; implementation and native parser validation pending.

- EA `Actor` translates to a reusable SysML v2 `PartDefinition`, with MDSE YAML `subtype: External Participant`, plus original `eaType`, `eaStereotype`, and provenance.
- SysML v2 *does* provide native `actor` syntax to designate an external-role **PartUsage** within a use case, case or requirement; it is not a separate reusable `ActorDefinition` kind.
- Where EA evidence relates an external actor to a use case, create a native typed actor usage referencing the existing PartDefinition. No additional MDSE note for usage.
- Do not treat actor usage as system-owned physical composition. Preserve source relationships and resolve actor roles from explicit evidence; ambiguous references remain reviewable.
- Example: `part def Operator; use case def ChargeBattery { actor operator : Operator; }` (illustrative, parser validation required).

Normative: https://www.omg.org/spec/SysML/2.0/Language/PDF section 7.25.2; OMG SysML2_-314 resolution identifies former UML Actor as PartDefinition.
