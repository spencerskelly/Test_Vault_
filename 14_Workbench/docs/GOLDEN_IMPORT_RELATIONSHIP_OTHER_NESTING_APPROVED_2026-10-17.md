# Golden Import — Other EA element nesting

Decision date: 2026-10-17. Status: APPROVED policy; runtime enforcement pending.

- For EA elements nested directly inside another element, **default to organizational nesting only**, not semantic ownership, unless the element family and source evidence satisfy an explicitly approved relationship rule.
- Existing approved exceptions: direct nested States -> local StateUsage; Activities -> local ActionUsage; Ports within Parts -> PortUsage; Requirements within Requirements -> nested RequirementUsage. Explicit physical Aggregation/Composition may create owned PartUsage only with physical containment evidence.
- Package hierarchy remains organizational folders and never supplies physical or behavioral ownership.
- Do not infer specialization, connection, dependency, execution order, requirement decomposition outside the approved case, or other semantic relationships from generic nesting.
- Retain EA parent IDs, hierarchy and provenance independently of native semantic relationships. Unresolved ownership required by a native usage remains flagged for review.
- Validate this deny-by-default behavior against source fixture and prevent new native relationships absent applicable rule IDs.
