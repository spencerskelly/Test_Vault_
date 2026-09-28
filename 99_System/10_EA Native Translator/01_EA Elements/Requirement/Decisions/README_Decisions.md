---
uid:
type: Info
status: Active
workspace: EA Native Translator
---
# Requirement Translation Decisions

These notes are the human-editable authority for Requirement translation decisions.

Read [[Translator Governance]] before editing.

## Workflow

1. Edit the decision content directly.
2. When you approve the semantic decision, set:
   `decisionState: Human Approved`
3. Push normally.
4. AI/reviewer reconciles the decision into Translation Rules/contracts.
5. After reconciliation, `implementationState` becomes `Implemented`.
6. After a fixture/result confirms behavior, `verificationState` becomes `Verified`.

## Do not use canvases as the only decision record

Canvases are visual review surfaces. The authoritative decision must exist in these notes.
