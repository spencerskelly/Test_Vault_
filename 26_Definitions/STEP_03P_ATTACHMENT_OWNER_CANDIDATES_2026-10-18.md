# STEP-03P — Attachment owner candidate staging

Date: 2026-10-18. The read-only source-identified STEP-03O ledger now feeds `25_Testing/v2_step03p_attachment_owner_candidates.py`, with synthetic regression tests. The stage creates a **separate local-only evidence ledger**, not notes or attachment files.

## Meaning of output

- `parent_owner_candidate`: a source Artifact has a valid EA ParentID pointing to an existing element; stage that element as the candidate responsible note (not yet accepted MDSE ownership).
- `connector_review`: the Artifact lacks a parent element but has source connectors. Preserve the full connector evidence without guessing owner or orientation.
- `unassigned_review`: neither source parent nor connector evidence. Preserve the artifact in the ledger for later review, without creating a phantom owner.

Expect 52 parent candidates, 91 connector reviews, and one unassigned review for the audited reduced QEAX. These are **not** evidence of completed attachment note linking, nor permission to add 92 flags to unrelated notes. Only create a flagNote on the actual responsible note after owner identification. Do not create duplicate notes for attachments; preserve provenance and underlying metadata.

## Mac step

From `Test_Vault_`:

```bash
git pull --ff-only origin main
python3 -m unittest discover -s 25_Testing -p 'test_v2_step03p_attachment_owner_candidates.py' -v
python3 25_Testing/v2_step03p_attachment_owner_candidates.py "$HOME/Documents/MDSE_Local_STEP03K/attachment_ownership.private.jsonl" "$HOME/Documents/MDSE_Local_STEP03K/attachment_owner_candidates.private.jsonl"
```

Input and output paths must differ and the output must be new. Do not commit ledger data.

## Remaining work

Evaluate connector direction using the already approved conditional relationship semantics; resolve each candidate to a responsible, retained MDSE note. Keep ambiguous artifacts in an evidence-backed review queue; do not block the golden import. Add actual note-side attachment reference serialization and flagNote staging, then run graph parity and Workbench browser checks. EA diagrams remain excluded.
