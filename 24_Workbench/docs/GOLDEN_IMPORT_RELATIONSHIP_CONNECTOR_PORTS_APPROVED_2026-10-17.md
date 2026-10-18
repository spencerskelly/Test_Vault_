# Golden Import — EA Connector between ports

Decision date: 2026-10-17. Status: APPROVED; implementation and native parser validation pending.

- Where an EA `Connector` resolves both endpoints to port usages, translate to native SysML v2 `ConnectionUsage` between the corresponding `PortUsage` endpoints.
- Preserve original EA connector identity, source and destination port references, direction, role and provenance.
- Do not infer the physical or logical connection if a port endpoint cannot be resolved; retain the source connector in an explicit review disposition.
- Connection usages are contained within the appropriate model context and do not create independent MDSE notes. Reusable port definitions remain single-note definitions.
- Validate endpoint identity, owning context, port typing, native syntax and repeat-import stability.
