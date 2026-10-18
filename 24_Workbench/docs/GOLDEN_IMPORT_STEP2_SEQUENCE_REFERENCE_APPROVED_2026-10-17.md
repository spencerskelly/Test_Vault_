# Golden Import Step 2 — Sequence interaction reference

> **Scope update (ADR-V2-05, October 18):** EA diagrams and their layout/sequence/Canvas translation are **deferred** until all tools and golden-import testing are complete. This document retains its approved semantic and future view-design decisions, but the first-release importer must use only non-diagram source elements/connectors. [Scope lock](../../26_Definitions/STEP_02A_EA_DIAGRAM_DEFERRED_2026-10-18.md).

Decision date: 2026-10-17. Status: APPROVED; implementation pending.

- EA `Sequence` and associated sequence diagrams are **reference-only interaction views**, not executable or simulated workflows.
- Preserve represented participants, messages, order, and references to defined elements where supported by source evidence, in a local MDSE workflow/interaction view.
- Do **not** infer executable native SysML v2 ActionUsages, Succession, scheduling, control flow or simulation semantics solely from presentation order.
- Existing explicitly modeled semantic relationships retain their separate translation rules; this decision applies to the sequence diagram/view interpretation.
- Preserve source provenance, links to defined elements, and view identities; avoid extra MDSE notes for mere usage occurrences.
- If no trustworthy semantic message information exists, retain as non-native reference/view evidence.
- Acceptance: no generated executable behavior from diagram-only ordering; references resolve, view remains inspectable and repeat import stable.
