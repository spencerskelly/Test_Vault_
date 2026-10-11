"""Step 13: fail-closed, non-mutating registry/canonical-source proposal checks."""
from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path

from step14_doc_review import original_historical_bytes

ROOT = Path(__file__).resolve().parents[2]
CONTRACT = "00_Workspace/MDSE v0.8 Unified Development Continuation Contract - PROPOSAL 2026-10-10.md"
PLAN = "00_Workspace/Consolidation Step 13 - Document Registry Transition Plan 2026-10-10.md"
LEDGER = "66_Testing/consolidation/step13_registry_transition.json"
MANIFEST = "Base Vault/Definition/mdse-release.yaml"
ORIGINAL_MANIFEST_SHA = "04f1fc2f4a087ccd2d1a49376c221979ee3469e3"
ORIGINAL_W_LOG_SHA = "49ab9bc513b27ce7e1c2beed6e039aad5c0bebbb"
ORIGINAL_LOCK_SHA = "c430670577318457972a154012d08c6d28e6d11b"
OLD = {
    "00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md": "d344fd38147efd03841acab547cac7bb579c2a1e",
    "00_Workspace/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md": "e133dcb2672eb6b8066b79d857d7e4e58d1a187f",
    "00_Workspace/Workbench Performance and Stability Roadmap.md": "4f41a03020efe011260dbb884a4c279106814142",
    "55_Workbench/docs/Definition/03 - Build Outline and Roadmap.md": "0ff206b531c7659b4b46757554a7f1d6d4b1b53f",
    "55_Workbench/docs/README.md": "2dc82f816e4626982016ed9453c3c5fad8da3f32",
}
ROW_CONTRACT = f'  - {{path: "{CONTRACT}", status: proposal}}\n'
ROW_PLAN = f'  - {{path: "{PLAN}", status: reference}}\n'


def git_blob_sha(data: bytes) -> str:
    header = ("blob " + str(len(data)) + "\0").encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def remove_proposal_rows(manifest: str) -> str:
    if manifest.count(ROW_CONTRACT) != 1 or manifest.count(ROW_PLAN) != 1:
        raise ValueError("Expected exactly two proposal registry entries")
    return manifest.replace(ROW_CONTRACT, "", 1).replace(ROW_PLAN, "", 1)


def apply_future_governance_in_memory(manifest: str, ledger: dict) -> str:
    if ledger["status"] != "PROPOSED_NOT_APPROVED":
        raise ValueError("Unexpected governance status")
    result = manifest
    for item in ledger["plannedGovernanceChanges"]:
        target = item["path"]
        previous = item["from"]
        new = item["to"]
        original = f'  - {{path: "{target}", status: {previous}}}'
        if item["operation"] == "supersede_old_current":
            replacement = f'  - {{path: "{target}", status: {new}, supersededBy: "{item["supersededBy"]}"}}'
        elif item["operation"] == "promote_to_current":
            replacement = f'  - {{path: "{target}", status: {new}}}'
        else:
            raise ValueError("Unrecognized governance operation")
        if result.count(original) != 1:
            raise ValueError("Governance mutation must hit exactly one complete registry line")
        result = result.replace(original, replacement, 1)
    return result


class Step13CandidateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = read(MANIFEST)
        cls.ledger = json.loads(read(LEDGER))

    def test_only_two_new_manifest_lines(self):
        cleaned = remove_proposal_rows(self.manifest)
        self.assertEqual(git_blob_sha(cleaned.encode("utf-8")), ORIGINAL_MANIFEST_SHA)

    def test_contract_registered_as_proposal_exactly_once(self):
        self.assertEqual(self.manifest.count(ROW_CONTRACT), 1)

    def test_transition_plan_registered_as_reference_exactly_once(self):
        self.assertEqual(self.manifest.count(ROW_PLAN), 1)

    def test_proposed_contract_and_plan_exist(self):
        self.assertTrue((ROOT / CONTRACT).is_file())
        self.assertTrue((ROOT / PLAN).is_file())

    def test_proposed_contract_has_review_only_header(self):
        doc = read(CONTRACT)
        self.assertIn("NOT AN APPROVED W DECISION", doc)
        self.assertIn("Status:** **PROPOSAL", doc)

    def test_no_new_current_registry_entries(self):
        self.assertIn('status: proposal}', ROW_CONTRACT)
        self.assertIn('status: reference}', ROW_PLAN)
        self.assertNotIn(f'path: "{CONTRACT}", status: current', self.manifest)

    def test_original_two_current_docs_not_prematurely_superseded(self):
        for old in list(OLD)[:2]:
            self.assertIn(f'  - {{path: "{old}", status: current}}', self.manifest)

    def test_roadmap_status_remains_reference(self):
        path = "00_Workspace/Workbench Performance and Stability Roadmap.md"
        self.assertIn(f'  - {{path: "{path}", status: reference}}', self.manifest)

    def test_all_five_original_document_bodies_preserved(self):
        for p, sha in OLD.items():
            with self.subTest(path=p):
                raw = (ROOT / p).read_bytes()
                original = original_historical_bytes(p, raw)
                self.assertEqual(git_blob_sha(original), sha)

    def test_legacy_W_log_unchanged(self):
        self.assertEqual(git_blob_sha((ROOT / "00_Workspace/Workspace Decision Log.md").read_bytes()), ORIGINAL_W_LOG_SHA)

    def test_plugin_lock_unchanged(self):
        self.assertEqual(git_blob_sha((ROOT / ".obsidian/plugin-lock.yaml").read_bytes()), ORIGINAL_LOCK_SHA)

    def test_release_pins_unchanged(self):
        for value in [
            'mdseRelease: "0.8.0"', 'releaseStatus: pre-release',
            'relationships: "1.36"', 'elementTypes: "1.18"',
            'localModel: "0.5"', 'candidateVersion: "0.8.19"',
            '    version: "0.1.18"', '    version: "0.3.0"'
        ]:
            with self.subTest(value=value):
                self.assertIn(value, self.manifest)

    def test_repo_authority_fields_still_consolidated_in_staging(self):
        self.assertIn('  workbench:\n    repo: "spencerskelly/Test_Vault_"', self.manifest)
        self.assertIn('repos:\n  authority: "spencerskelly/Test_Vault_"\n  workbench: "spencerskelly/Test_Vault_"', self.manifest)

    def test_ledger_keeps_w_decision_unapproved(self):
        self.assertEqual(self.ledger["status"], "PROPOSED_NOT_APPROVED")
        self.assertIsNone(self.ledger["approvals"]["supersedingWDecision"])
        self.assertFalse(self.ledger["approvals"]["standaloneArchiveApproval"])

    def test_ledger_baseline_manifest_blob_exact(self):
        self.assertEqual(self.ledger["baselineManifestBlob"], ORIGINAL_MANIFEST_SHA)

    def test_ledger_has_exact_three_future_operations(self):
        ops = self.ledger["plannedGovernanceChanges"]
        self.assertEqual(len(ops), 3)
        self.assertEqual([op["operation"] for op in ops],
                         ["promote_to_current", "supersede_old_current", "supersede_old_current"])

    def test_future_promotion_is_in_memory_only_and_reversible(self):
        before = self.manifest
        after = apply_future_governance_in_memory(before, self.ledger)
        self.assertNotEqual(after, before)
        for op in self.ledger["plannedGovernanceChanges"]:
            self.assertIn(f'path: "{op["path"]}", status: {op["to"]}', after)
        self.assertIn(ROW_PLAN, after)
        self.assertEqual(read(MANIFEST), before)

    def test_refuse_unknown_registry_row_rename(self):
        ledger = json.loads(json.dumps(self.ledger))
        ledger["plannedGovernanceChanges"][0]["path"] = "00_Workspace/Nonexistent.md"
        with self.assertRaises(ValueError):
            apply_future_governance_in_memory(self.manifest, ledger)

    def test_refuse_unapproved_governance_state_mismatch(self):
        ledger = json.loads(json.dumps(self.ledger))
        ledger["status"] = "APPROVED"
        with self.assertRaises(ValueError):
            apply_future_governance_in_memory(self.manifest, ledger)

    def test_manifest_mutation_detected_even_if_proposal_rows_removed(self):
        altered = self.manifest.replace("releaseStatus: pre-release", "releaseStatus: release", 1)
        base = remove_proposal_rows(altered)
        self.assertNotEqual(git_blob_sha(base.encode("utf-8")), ORIGINAL_MANIFEST_SHA)

    def test_contract_does_not_approve_local_model_06(self):
        doc = read(CONTRACT)
        self.assertIn("no writer 0.6 authority", doc)
        self.assertIn("**PROPOSAL / REVIEW ONLY", doc)

    def test_ledger_preserves_five_open_dispositions(self):
        docs = self.ledger["unresolvedDocuments"]
        self.assertEqual(len(docs), 5)
        self.assertEqual({x["path"] for x in docs}, set(OLD))

    def test_ledger_security_and_local_clone_gates_open(self):
        approvals = self.ledger["approvals"]
        self.assertIsNone(approvals["publicQEAXDataOwnerReview"])
        self.assertEqual(approvals["localCloneSignoffs"], 0)
        self.assertFalse(approvals["realObsidianGUIAcceptance"])

    def test_source_metadata_no_qeax_binary_read(self):
        test_source = Path(__file__).read_text(encoding="utf-8")
        self.assertNotIn("." + "qeax" + ".zip", test_source)


if __name__ == "__main__":
    unittest.main()
