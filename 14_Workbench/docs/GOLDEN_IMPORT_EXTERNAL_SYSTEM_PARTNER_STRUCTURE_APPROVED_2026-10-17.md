# External System Partner internal structure

Decision: approved on 2026-10-17.

An external System Partner may contain its own parts through native SysML v2 owned PartUsages, when the source establishes actual structural containment. Its being external does not prevent modeling its internal composition. The partner itself is not thereby owned by the modeled charging system.

Keep one reusable PartDefinition note per defined part and represent each distinct usage in the owning definition. Preserve source connectors, roles, multiplicity, orientation and provenance. Do not infer ownership of the partner by the internal system, nor accept nonphysical grouping as physical containment. Ambiguous individual connections remain reviewable.

This rule applies to the aggregation audit's external-parent category. Parser and per-row validation remain pending.
