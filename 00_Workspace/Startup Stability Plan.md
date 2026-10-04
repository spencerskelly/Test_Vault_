# Startup Stability Plan

**Priority:** stability before feature latency.

## Goal

Opening an MDSE vault must first produce a responsive, readable Obsidian workspace. MDSE capabilities may become ready afterward in explicit stages.

## Piece 1 — Startup safety gate

**Purpose:** guarantee that Workbench does not perform model/schema I/O in Obsidian's immediate layout-ready callback or before Obsidian's metadata startup lane is complete.

Required behavior:

1. Workbench `onload()` may load its small local settings and register commands/UI/listeners.
2. `onLayoutReady` only schedules a Workbench startup handoff and returns.
3. First-start model/schema I/O waits until Obsidian reports metadata resolution, or until the bounded quiet fallback is satisfied.
4. After that gate, Workbench may read schemas and begin core model work.
5. A Workbench startup failure must leave Obsidian usable and report the scoped failure.
6. Local Model hydration, assurance and cache persistence are outside this piece and may not be pulled into the immediate startup callback.

**Acceptance:** opening the vault never waits on Workbench schema reads, index construction, Local Model reads, cache restoration/persistence or assurance before Obsidian receives its normal startup/UI event-loop turns.

## Piece 2 — Core model readiness

Build/restore only the reusable-note semantic graph. Declare Workbench core ready when that graph is usable. No occurrence hydration requirement.

## Piece 3 — Deferred occurrence capability

Hydrate Local Model part/endpoint/connection/flow records after core readiness or on explicit demand. Occurrence-aware views wait when needed; unrelated views do not.

## Piece 4 — Background scheduling

Make deferred work activity-aware, cooperative and preemptible. Cache persistence and release verification run in separate quiet lanes.

## Piece 5 — Health and failure isolation

Expose core, occurrence, cache, schema and assurance state separately. Failure of a derived subsystem must not destabilize Obsidian or masquerade as valid results.

## Piece 6 — Warm-start optimization

Only after pieces 1–5 are accepted should warm semantic-cache restore be enabled and measured as a normal startup path.

## Piece 7 — Plugin-stack reduction

Measure overlapping third-party plugins one at a time. Remove or demote only after replacement capability and startup benefit are proven.

## Piece 8 — Integrated acceptance

Install one exact CI-built candidate in the disposable integration vault and test startup responsiveness, staged readiness, occurrence views, editing, recovery and restart behavior.

## Current execution

Piece 1 is the active slice. It is intentionally narrow; no additional runtime optimization belongs in this slice until its code/build gate is clean.
