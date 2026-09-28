---
uid:
type: Info
status: Active
workspace: EA Native Translator
documentRole: Governance
---
# Translator Governance

## Purpose

Define how human decisions, AI proposals, source evidence, executable rules, generated views, and verification results become authoritative in the EA Native Translator workspace.

## Authority order

When two artifacts disagree, use this order:

1. **Human Approved decision note**
2. **Implemented Translation Rule / MDSE contract**
3. **Current governance and taxonomy**
4. **Generated canvas/base/view**
5. **Current source evidence**
6. **Imported reference/historical handoff**
7. **Chat discussion or AI proposal not yet recorded**

Source evidence is authoritative about **what EA contained**, but not about **what MDSE meaning should be assigned**.

## Decision lifecycle

Use these values for `decisionState`:

- `Working` — being discussed; not approved.
- `Human Approved` — the human owner has approved the semantic decision.
- `Superseded` — replaced by a later explicit decision.

Use these values for `implementationState`:

- `Not Started`
- `Partial`
- `Implemented`

Use these values for `verificationState`:

- `Not Verified`
- `Fixture Defined`
- `Verified`

A decision is not complete merely because it is Human Approved. It becomes translator-ready when it is **Implemented** and, where practical, **Verified**.

## Decision-note frontmatter

Translator decision notes should use:

```yaml
type: Translation Decision
status: Working
decisionState: Working
decisionOwner: Human
implementationState: Not Started
verificationState: Not Verified
lastReviewed:
```

Optional:

```yaml
supersedes:
implementedBy:
verifiedBy:
sourceEvidence:
```

## Human editing rule

Human reviewers should edit decision notes directly in Obsidian.

A human decision should be recorded in the decision note itself, not only in:

- a canvas;
- a Git commit message;
- chat;
- an AI-generated summary.

Changing `decisionState` to `Human Approved` explicitly authorizes the decision.

## AI behavior

An AI working in this vault must:

1. Read [[AI Handoff - EA Native Translator]].
2. Read this governance note.
3. Read [[Translator Definition Tracker]].
4. Distinguish source evidence from approved semantics.
5. Never overwrite a `Human Approved` decision without explicit human instruction.
6. Propose changes in decision notes when semantics are unresolved.
7. Promote approved decisions into Translation Rules/contracts.
8. Update `implementationState` only after the dependent methodology artifacts are actually reconciled.
9. Update `verificationState` only when a fixture or actual verification exists.
10. Record material methodology changes in [[Translator Change Log]].

## Generated artifact rule

Generated source inventory notes, connector tables, Bases, and canvases are views/evidence. They may be regenerated.

Do not place unique authoritative semantic decisions only in generated artifacts.

## Imported-reference rule

Material copied from another project or earlier translator version is **reference input** unless explicitly adopted here.

An imported document's own statement that it is "authoritative" or "live" does not override this workspace's governance.

## Source evidence rule

Raw EA exports live in `99_System/CSV_EA`.

They are immutable evidence for the source extract. Derived methodology should reference them rather than modify them.

## Change acknowledgment

When the human pushes changes:

1. AI fetches current `main`.
2. AI compares changed decision/methodology files against the last reviewed state.
3. AI summarizes the human changes.
4. AI updates dependent rules/contracts/views.
5. AI updates the tracker and change log.
6. AI reports any contradictions or unresolved downstream effects.

This is how a pushed human change becomes acknowledged by the translator methodology.
