# Golden Import Step 2 — ProxyConnector

Decision date: 2026-10-17. Status: APPROVED; implementation and semantic validation pending.

- EA `ProxyConnector` elements represent references to connections between existing elements, not standalone `PartDefinition` or `PortDefinition` declarations.
- Resolve referenced endpoints and preserve original EA source relationships, direction, identity and provenance.
- Apply the existing approved native SysML v2 connection/relationship rules only when endpoint typing and source evidence justify them; never invent a new relationship from diagram layout alone.
- No extra MDSE note per connection reference. Retain relationship/source evidence in the owning element's representation and source ledger.
- If endpoints or connection kind cannot be established, mark the record for review instead of creating a fabricated connection.
- Test source endpoint identity, duplicate prevention, links and idempotence.
