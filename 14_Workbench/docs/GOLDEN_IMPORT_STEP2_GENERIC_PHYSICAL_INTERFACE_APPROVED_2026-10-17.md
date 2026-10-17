# Golden Import Step 2 — Generic Physical Interface

Decision date: 2026-10-17. Status: APPROVED; implementation and parser validation pending.

- EA `Class:Generic Physical Interface` maps to a native SysML v2 `PortDefinition` representing a full port.
- An owning part contains a typed `PortUsage` referring to that reusable `PortDefinition`.
- Create exactly one MDSE note per port definition; do not create separate notes for port usages.
- Preserve MDSE type/subtype and original EA type/stereotype in YAML, plus source provenance.
- Preserve original explicitly modeled connections according to the approved connector translation rules, without inferring new ones.
- Validate ownership, typing, native serialization and repeat-import stability.
