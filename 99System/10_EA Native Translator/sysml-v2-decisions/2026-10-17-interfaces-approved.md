# APPROVED — Native SysML v2 Interface Definitions and Usages
Date: 2026-10-17
Status: APPROVED — Relationship #12

## Meaning
An Interface is a specialized native SysML v2 Connection that describes an interaction with port ends. Ports are interaction points owned by parts; an interface usage relates participating ports. A general connection can connect other kinds of compatible features and need not assert an interface contract.

## Use and non-use
Use interface definitions to capture reusable interaction specifications and interface usages to apply them to compatible port ends in a specific owning context. Do not mistake a port for an interface, an interface for a physical cable, or a generic dependency for a connection. Do not infer messages, physical wiring, flow direction, or protocol from port names alone.

## Import policy
EA Connector defaults to native connection usage per approved #11 rule. When EA evidence clearly encodes an interface between ports, permit translation to native interface usage after classification and validation; do not automatically convert all connectors merely because ports are endpoints. Full original QEAX connectivity audit remains open; mini export is not representative.

## Workbench
- Structural view: show reusable interface definition, usage, owning context, participating port features and resolved nested feature paths.
- Visual view: show interface between ports distinct from ordinary connection, binding or dependency; select usage and navigate to both port definitions and owner.
- Properties: show type, ends, expected directions and interaction constraints when explicitly modeled, never guessed.
- Text/tree/diagram edits modify canonical SysML v2 syntax in owning Obsidian note and reparse synchronized views. AST-aware update; reject incompatible/non-port endpoints.
- A usage need not have a separate Markdown note; share canonical reusable definitions.
- Validate port end compatibility, context, imports, endpoint resolution, and canonical textual syntax with a conforming SysML v2 parser.

## Example — conceptual, syntax requires parser confirmation before production
```sysml
port def CANPort;
interface def CANInterface {
    end port a : CANPort;
    end port b : CANPort;
}
```

## Distinctions
- Port: one interaction point.
- Connection: relation among compatible features.
- Interface: specialized connection between ports with interaction semantics.
- Binding: constrains two features to equality, not physical connectivity.
- Flow: explicit conveyed items or transferred values when specified.

## Next review
Binding connectors: formal equality semantics, valid features and Workbench distinctions. Previous approval exists; revisit as SysML v2-first catalog entry rather than changing its meaning.
