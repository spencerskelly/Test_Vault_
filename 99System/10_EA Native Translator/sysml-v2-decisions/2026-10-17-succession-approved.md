# APPROVED — Native SysML v2 Succession
Date: 2026-10-17
Status: APPROVED — relationship #15

## Plain English
Succession expresses temporal ordering: an occurrence/action happens before another. Ordering alone does not assert physical connectivity, dependency, item transfer, or a state-machine trigger.

## Native semantics and examples
Support native succession between valid occurrence/action endpoints, with source/target meaning earlier → later. Example: checkBattery before enableOutput before beginCharging. Validate exact emitted syntax and scoping against a conforming SysML v2 parser.

## EA migration
Map EA ordering relations such as suitable ControlFlow and Sequence connectors to native succession only after checking that the given edge actually describes temporal ordering. Do not blanket-map all ControlFlow, ObjectFlow, StateFlow or Sequence connectors. If transfer is expressed, assess Flow or Succession Flow instead. If state switching/guard/trigger is expressed, assess Transition. Preserve true ordering direction.

## Workbench
- Structure: show owning action/behavior context, predecessor and successor, optionally branching/concurrency; do not imply ownership.
- Visual: directional temporal sequencing edge in behavioral diagrams, distinct from flow or transition.
- Editing in any view writes native SysML v2 syntax in the owning Obsidian note and refreshes other projections.
- Validate action/occurrence endpoints, namespace and context, illegal chains, unresolved references, and semantics where timing/guards matter.
- Keep one canonical reusable definition per type; usage notes optional.

## Documentation
Explain Succession versus Succession Flow, Transition, Dependency, and Connection with one practical and one counterexample in future engineer-facing guide.
## Next review
State Transition: source/target states, triggers, guards, effects, and associated behavioral context.
