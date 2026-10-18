# Golden Import — Ownership cycle handling

Decision date: 2026-10-17. Status: APPROVED; implementation and fixture validation pending.

- Detect circular semantic ownership among assemblies and other owned usage structures before generating native SysML v2 containment.
- If A owns B and B owns A, or any longer semantic ownership cycle exists, flag all implicated ownership edges for review and **exclude those ownership usages from native output until resolved**.
- Retain every affected EA relationship with source endpoints, aggregate flags and provenance in the private disposition ledger. Do not delete source evidence or silently reorient edges to break cycles.
- Organizational EA package/folder nesting does not establish semantic ownership and does not participate in semantic ownership cycle detection.
- Independent reusable definitions and unrelated valid usages remain importable; report cycle diagnostics and block only affected native ownership constructs unless the overall atomic publish gate requires a clean review.
- Acceptance: deterministic graph cycle detection, clear diagnostics, no cycle-bearing native output, stable results on repeated reconciliation.
