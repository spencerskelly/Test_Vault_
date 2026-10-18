# Golden Import Step 2 — Sequence interaction reference

Decision date: 2026-10-17. Status: APPROVED; implementation pending.

- EA `Sequence` and associated sequence diagrams are **reference-only interaction views**, not executable or simulated workflows.
- Preserve represented participants, messages, order, and references to defined elements where supported by source evidence, in a local MDSE workflow/interaction view.
- Do **not** infer executable native SysML v2 ActionUsages, Succession, scheduling, control flow or simulation semantics solely from presentation order.
- Existing explicitly modeled semantic relationships retain their separate translation rules; this decision applies to the sequence diagram/view interpretation.
- Preserve source provenance, links to defined elements, and view identities; avoid extra MDSE notes for mere usage occurrences.
- If no trustworthy semantic message information exists, retain as non-native reference/view evidence.
- Acceptance: no generated executable behavior from diagram-only ordering; references resolve, view remains inspectable and repeat import stable.
