"""Step 14: exact-byte preserved Workbench roadmap/README source plus review banner.

These tests don't reinterpret WB/W decisions, change model semantics, or read the QEAX.
"""
from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from step14_doc_review import START, END, REVIEWED, banner_body, original_historical_bytes
from workbench_reference_policy import classify

ROOT = Path(__file__).resolve().parents[2]
NEW = {
    "00_Workspace/Workbench Performance and Stability Roadmap.md":
        "6a5da07c8c4ed411fd304cccd6d22ba7859a6414",
    "55_Workbench/docs/Definition/03 - Build Outline and Roadmap.md":
        "62d4f187b9f0fb6dbe0e33d5a1c6ba7665aa0efa",
    "55_Workbench/docs/README.md":
        "f0ec1263e7dea40d5ebbd741a6caf20a81400540",
}
HISTORICAL_HEADINGS = {
    "00_Workspace/Workbench Performance and Stability Roadmap.md":
        b"# Workbench Performance and Stability Roadmap\n\n",
    "55_Workbench/docs/Definition/03 - Build Outline and Roadmap.md":
        b"# Build Outline and Roadmap\n\n",
    "55_Workbench/docs/README.md": b"# MDSE Workbench\n\n",
}
MANIFEST = "Base Vault/Definition/mdse-release.yaml"
CONTRACT = "00_Workspace/MDSE v0.8 Unified Development Continuation Contract - PROPOSAL 2026-10-10.md"
LEDGER = "66_Testing/consolidation/step13_registry_transition.json"


def sha(data: bytes) -> str:
    return hashlib.sha1(("blob " + str(len(data)) + "\0").encode() + data).hexdigest()


class WorkbenchStep14Tests(unittest.TestCase):
    def test_exactly_three_reviewed_documents(self):
        self.assertEqual(set(NEW), set(REVIEWED))

    def test_candidate_modified_git_sha_values(self):
        for p, new_sha in NEW.items():
            with self.subTest(path=p):
                self.assertEqual(sha((ROOT / p).read_bytes()), new_sha)

    def test_every_original_historical_document_byte_is_preserved(self):
        for p, old_sha in REVIEWED.items():
            with self.subTest(path=p):
                self.assertEqual(sha(original_historical_bytes(p, (ROOT / p).read_bytes())), old_sha)

    def test_original_heading_and_body_still_follow_banner(self):
        for p in REVIEWED:
            with self.subTest(path=p):
                result = original_historical_bytes(p, (ROOT / p).read_bytes())
                self.assertTrue(result.startswith(HISTORICAL_HEADINGS[p]))

    def test_one_proposed_notice_below_each_title(self):
        for p in REVIEWED:
            with self.subTest(path=p):
                raw = (ROOT / p).read_bytes()
                self.assertEqual(raw.count(START), 1)
                self.assertEqual(raw.count(END), 1)
                self.assertEqual(raw.index(START), raw.index(b"\n\n") + 2)

    def test_all_notices_warn_not_approved(self):
        for p in REVIEWED:
            with self.subTest(path=p):
                banner = banner_body(p, (ROOT / p).read_bytes())
                self.assertIn(b"PROPOSAL, NOT APPROVED", banner)
                self.assertIn(b"2026-10-10", banner)

    def test_each_notice_describes_staging_not_released_model(self):
        for p in REVIEWED:
            with self.subTest(path=p):
                banner = banner_body(p, (ROOT / p).read_bytes())
                for pin in (b"1.36", b"1.18", b"0.5", b"0.1.18"):
                    self.assertIn(pin, banner)

    def test_each_notice_links_consolidated_candidate_source(self):
        for p in REVIEWED:
            with self.subTest(path=p):
                banner = banner_body(p, (ROOT / p).read_bytes())
                self.assertIn(b"Test_Vault_/55_Workbench/", banner)

    def test_no_notice_claims_archive_completed(self):
        for p in REVIEWED:
            with self.subTest(path=p):
                banner = banner_body(p, (ROOT / p).read_bytes())
                self.assertNotIn(b"standalone repository is archived", banner.lower())

    def test_old_stability_execution_contract_still_attributable(self):
        p = "00_Workspace/Workbench Performance and Stability Roadmap.md"
        body = original_historical_bytes(p, (ROOT / p).read_bytes())
        self.assertIn(b"## Execution contract for future chats", body)
        self.assertIn(b"### Step 33 completion evidence", body)

    def test_old_approved_product_scope_still_attributable(self):
        p = "55_Workbench/docs/Definition/03 - Build Outline and Roadmap.md"
        body = original_historical_bytes(p, (ROOT / p).read_bytes())
        self.assertIn(b"approved direction (2026-09-30)", body)
        self.assertIn(b"2026-10-02 continuation boundary", body)

    def test_old_workbench_vintage_notes_still_attributable(self):
        p = "55_Workbench/docs/README.md"
        body = original_historical_bytes(p, (ROOT / p).read_bytes())
        self.assertIn(b"Local Model writer 0.2", body)
        self.assertIn(b"## Current v0.8 contract", body)

    def test_missing_marker_rejected(self):
        p = next(iter(REVIEWED))
        data = (ROOT / p).read_bytes().replace(START, b"", 1)
        with self.assertRaises(ValueError):
            original_historical_bytes(p, data)

    def test_changed_marker_position_rejected(self):
        p = next(iter(REVIEWED))
        raw = (ROOT / p).read_bytes()
        altered = raw.replace(START, b"extra\n" + START, 1)
        with self.assertRaises(ValueError):
            original_historical_bytes(p, altered)

    def test_duplicate_marker_rejected(self):
        p = next(iter(REVIEWED))
        raw = (ROOT / p).read_bytes()
        with self.assertRaises(ValueError):
            original_historical_bytes(p, raw.replace(START, START + START, 1))

    def test_changed_historical_body_detected(self):
        p = "55_Workbench/docs/README.md"
        raw = (ROOT / p).read_bytes().replace(b"## Purpose", b"## MUTATED Purpose", 1)
        restored = original_historical_bytes(p, raw)
        self.assertNotEqual(sha(restored), REVIEWED[p])

    def test_changed_banner_contract_rejected(self):
        p = next(iter(REVIEWED))
        raw = (ROOT / p).read_bytes()
        altered = raw.replace(b"PROPOSAL, NOT APPROVED", b"APPROVED", 1)
        with self.assertRaises(ValueError):
            original_historical_bytes(p, altered)

    def test_unexpected_banner_elsewhere_rejected(self):
        with self.assertRaises(ValueError):
            original_historical_bytes("00_Workspace/Unknown.md", START + b"test" + END)

    def test_original_two_current_handoffs_remain_unmodified(self):
        files = {
            "00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md":
                "d344fd38147efd03841acab547cac7bb579c2a1e",
            "00_Workspace/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md":
                "e133dcb2672eb6b8066b79d857d7e4e58d1a187f",
        }
        for p, expected in files.items():
            with self.subTest(path=p):
                self.assertEqual(sha((ROOT / p).read_bytes()), expected)

    def test_old_handoffs_still_registered_current_under_pending_governance(self):
        manifest = (ROOT / MANIFEST).read_text(encoding="utf-8")
        for p in (
            "00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md",
            "00_Workspace/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md",
        ):
            self.assertIn(f'path: "{p}", status: current', manifest)

    def test_proposed_successor_still_not_current(self):
        manifest = (ROOT / MANIFEST).read_text(encoding="utf-8")
        self.assertIn(f'path: "{CONTRACT}", status: proposal', manifest)
        self.assertNotIn(f'path: "{CONTRACT}", status: current', manifest)

    def test_release_manifest_and_plugin_lock_unchanged(self):
        expected = {
            MANIFEST: "29a05fc71c2f25108f07927870ac5d3d3bdd618b",
            ".obsidian/plugin-lock.yaml": "c430670577318457972a154012d08c6d28e6d11b",
        }
        for p, blob in expected.items():
            with self.subTest(path=p):
                self.assertEqual(sha((ROOT / p).read_bytes()), blob)

    def test_prior_W_log_unchanged(self):
        self.assertEqual(
            sha((ROOT / "00_Workspace/Workspace Decision Log.md").read_bytes()),
            "49ab9bc513b27ce7e1c2beed6e039aad5c0bebbb",
        )

    def test_governance_and_archive_approval_still_pending(self):
        record = json.loads((ROOT / LEDGER).read_text(encoding="utf-8"))
        self.assertEqual(record["status"], "PROPOSED_NOT_APPROVED")
        self.assertIsNone(record["approvals"]["supersedingWDecision"])
        self.assertFalse(record["approvals"]["standaloneArchiveApproval"])

    def test_three_mixed_purpose_docs_still_require_review(self):
        for p in REVIEWED:
            with self.subTest(path=p):
                self.assertEqual(classify(ROOT, p), "needs_review")


if __name__ == "__main__":
    unittest.main()
