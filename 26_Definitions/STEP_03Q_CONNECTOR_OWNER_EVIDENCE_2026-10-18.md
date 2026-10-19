# STEP-03Q — Connector ownership evidence against approved registry

Date: 2026-10-18. Status: reusable source-identity preserving classifier and four regression tests committed; real Mac execution pending.

Source: STEP-03P private owner-candidate ledger. This stage loads the existing approved 60-element/26-connector-family registry through the existing resolver. It classifies *connector types and directions as evidence* while preserving EA object/connector IDs. Registry family approval does NOT by itself establish direction of attachment ownership. The 91 connector-only artifacts remain unconfirmed until relationship-specific row evidence supports an owner. The 52 parent owner candidates remain candidates, and the one unassigned artifact remains in review. No artifact note is created, and no flag is attached to an unrelated node. EA diagrams excluded.

New tool: `25_Testing/v2_step03q_connector_owner_evidence.py`.
Tests: `25_Testing/test_v2_step03q_connector_owner_evidence.py`.

From Test_Vault_:

```bash
git pull --ff-only origin main
python3 -m unittest discover -s 25_Testing -p 'test_v2_step03q_connector_owner_evidence.py' -v
python3 25_Testing/v2_step03q_connector_owner_evidence.py \
 "$HOME/Documents/MDSE_Local_STEP03K/attachment_owner_candidates.private.jsonl" \
 "$HOME/Documents/MDSE_Local_STEP03K/attachment_connector_evidence.private.jsonl"
```

This reports aggregate source connector-family occurrences and writes local-only per-artifact evidence. The output refuses overwrite. Do not push private ledgers or QEAX.

**Critical-path correction:** Repeated classification steps are not sufficient for a functional golden import. Next stage must focus on reference serialization into responsible notes, with an unresolved attachment review queue for any still unassigned. Avoid treating provisional owner suggestions as verified. Workbench navigation and full semantic mapping remain acceptance gates, with diagrams excluded.
