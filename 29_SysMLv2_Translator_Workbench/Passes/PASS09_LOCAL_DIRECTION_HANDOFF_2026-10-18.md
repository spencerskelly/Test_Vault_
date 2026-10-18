# Phase 9: Local direction evidence handoff

Added `15_Testing/phase9_local_direction_handoff.py`, a read-only comparison of Phase 8 ledger connector identity, raw endpoints, normalized orientation, family, disposition, and explicit EA source direction against the reduced QEAX. Reports aggregate categories only; no source records are published.

Six synthetic tests include success candidate, reversed normalization, altered identity, inappropriate ledger disposition, altered source direction, and missing ledger coverage.

**Trust boundary:** Direction matching is necessary, not proof of subtype semantics or trusted graph authorization. `canonical_mutation_authorized=false` and `native_certified=0`. There is deliberately no graph mutation. A future bridge requires immutable snapshot/ledger identity, independently checked endpoint semantics, and documented approval.

Workbench must preserve lexical parent, specialization, source evidence, navigation and round-trip as distinct concepts. Native emission remains disabled.
