# EA to MDSE Native Importer v0.8.19

Status: hardening candidate; not release-accepted.

v0.8.19 implements W-384.

- All EA `Port` elements are Local Model Interface occurrences; no first-class Port notes are emitted.
- EA Interface Classes remain reusable definitions as `Object / interface`.
- Interface occurrences may reference a reusable `Object / interface` definition when deterministic EA evidence supports it; otherwise they remain definitionless.
- Ports directly owned by an EA Class become assembly-boundary Interface occurrences in that Class/Object note's Local Model.
- Local Model writer advances to schema 0.4 with `Parts`, `Interfaces`, and `Connections`.
- A Connection owns `exposes` and points to the boundary Interface through which the internal/context connection is exposed.
- Deterministic BindingConnector exposure is promoted to Connection `exposes`; ambiguous cases remain temporary `equals`/review evidence.
- `Behavior` replaces first-class Function/Action/Step classes with subtypes `function`, `activity`, `action`, `step`.
- An EA Activity is `Behavior / function` when its stereotype includes `function` regardless of package; Activity under `04 Product Function` is also `Behavior / function`.
- `Condition` replaces first-class State/State Machine/Design/Mode classes with subtypes `state`, `state machine`, `design`, `mode`.
- Semantic relationship names are retained but their endpoint rules use Behavior/Condition and no longer depend on first-class Port notes.

Acceptance still requires schema/base alignment, Workbench WB-128 Local Model 0.4 compatibility, static regression success, and a fresh real-QEAX whole-model import.
