"""Step 15: fail-closed governance readiness and exact proposed redline review.

Never applies changes. Never opens source-model data. No approvals are inferred.
"""
from __future__ import annotations

import copy
import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTER = "00_Workspace/Consolidation Step 15 - Governance Gate Register 2026-10-10.json"
PROPOSAL = "00_Workspace/Consolidation Step 15 - Proposed W Decision and Authority Signoff 2026-10-10.md"
REDLINE = "00_Workspace/Consolidation Step 15 - Exact Registry Redline and Promotion Stops 2026-10-10.md"
MANIFEST = "Base Vault/Definition/mdse-release.yaml"
DECISIONS = "00_Workspace/Workspace Decision Log.md"
LOCK = ".obsidian/plugin-lock.yaml"
CONTRACT = "00_Workspace/MDSE v0.8 Unified Development Continuation Contract - PROPOSAL 2026-10-10.md"
OLD_HANDOFF = "00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md"
OLD_RECON = "00_Workspace/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md"
REQUIRED = {
    "W_DECISION_OWNER_APPROVAL",
    "WORKBENCH_PRODUCT_SOURCE_APPROVAL",
    "DOCUMENT_REGISTRY_APPROVAL",
    "W341_USER_GUIDE_PARITY",
    "W342_RUNTIME_CANDIDATE_SEPARATION",
    "QEAX_DATA_OWNER_SECURITY_DISPOSITION",
    "ALL_LOCAL_CLONE_WORKTREE_STASH_SIGNOFFS",
    "BOM_A15_LOCAL_WORK_INVENTORY",
    "INTEGRATED_RELEASE_ARTIFACT_CHECKS",
    "REAL_OBSIDIAN_MAC_WINDOWS_GUI",
    "REVIEWED_STACK_PROMOTION_APPROVAL",
    "SEPARATE_STANDALONE_ARCHIVE_AUTHORIZATION",
}


def load(path):
    return (ROOT / path).read_text(encoding="utf-8")


def blob_sha(raw: bytes) -> str:
    return hashlib.sha1(("blob " + str(len(raw)) + "\0").encode() + raw).hexdigest()


def readiness(record: dict) -> dict:
    """Read-only evaluation. Unknown, missing or unapproved evidence fail closed."""
    gates = record.get("gates", [])
    keyed = {g.get("id"): g for g in gates if isinstance(g, dict)}
    valid = len(gates) == len(REQUIRED) and len(keyed) == len(REQUIRED) and set(keyed) == REQUIRED
    approved = valid and all(
        keyed[g]["status"] == "APPROVED"
        and isinstance(keyed[g].get("evidenceRef"), str)
        and bool(keyed[g]["evidenceRef"].strip())
        and isinstance(keyed[g].get("approvedAt"), str)
        and bool(keyed[g]["approvedAt"].strip())
        for g in REQUIRED
    )
    workflow = record.get("workflow", {})
    decision = bool(approved and workflow.get("decisionApproved")
                    and record.get("decisionId")
                    and record.get("decisionApproval"))
    promotion = bool(decision and workflow.get("redlineApplied")
                     and workflow.get("mainPromotionApproved"))
    archive = bool(promotion and workflow.get("mainPromotionExecuted")
                   and workflow.get("standaloneArchiveAuthorized"))
    return {"governanceDecisionReady": decision,
            "publicMainPromotionReady": promotion,
            "standaloneArchiveReady": archive}


def exact_row(path, status, successor=None):
    extras = f', supersededBy: "{successor}"' if successor else ""
    return f'  - {{path: "{path}", status: {status}{extras}}}'


class Step15ReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads(load(REGISTER))
        cls.manifest = load(MANIFEST)
        cls.decision_log = load(DECISIONS)
        cls.proposal = load(PROPOSAL)
        cls.redline = load(REDLINE)

    def test_register_schema_and_state(self):
        self.assertEqual(self.registry["schema"], "mdse-consolidation-governance-gates/1")
        self.assertEqual(self.registry["state"], "REVIEW_ONLY_NOT_APPROVED")

    def test_no_fabricated_approval_id(self):
        self.assertIsNone(self.registry["decisionId"])
        self.assertIsNone(self.registry["decisionApproval"])
        self.assertIsNone(self.registry["approvalEvidence"])

    def test_exact_twelve_required_gates(self):
        gates = self.registry["gates"]
        self.assertEqual(len(gates), 12)
        self.assertEqual({g["id"] for g in gates}, REQUIRED)

    def test_every_gate_unapproved(self):
        for gate in self.registry["gates"]:
            with self.subTest(gate=gate["id"]):
                self.assertEqual(gate["status"], "NOT_APPROVED")
                self.assertIsNone(gate["evidenceRef"])
                self.assertIsNone(gate["approvedAt"])

    def test_readiness_is_fail_closed(self):
        self.assertEqual(readiness(self.registry), {
            "governanceDecisionReady": False,
            "publicMainPromotionReady": False,
            "standaloneArchiveReady": False})

    def test_registered_readiness_is_false(self):
        self.assertEqual(self.registry["readiness"], readiness(self.registry))

    def test_no_public_promotion_or_archive_side_effect(self):
        w = self.registry["workflow"]
        self.assertTrue(w["decisionTextPrepared"])
        self.assertTrue(w["redlinePrepared"])
        for key in ["decisionApproved", "redlineApplied", "mainPromotionApproved",
                    "mainPromotionExecuted", "standaloneArchiveAuthorized", "standaloneArchived"]:
            self.assertIs(w[key], False)

    def test_missing_or_duplicate_gate_rejects_all_readiness(self):
        for modified in (self.registry["gates"][:-1],
                         self.registry["gates"] + [self.registry["gates"][0]]):
            candidate = copy.deepcopy(self.registry)
            candidate["gates"] = modified
            self.assertFalse(any(readiness(candidate).values()))

    def test_single_approval_without_evidence_remains_blocked(self):
        candidate = copy.deepcopy(self.registry)
        candidate["gates"][0]["status"] = "APPROVED"
        self.assertFalse(any(readiness(candidate).values()))

    def test_all_approvals_missing_governance_still_blocked(self):
        candidate = copy.deepcopy(self.registry)
        for g in candidate["gates"]:
            g.update(status="APPROVED", evidenceRef="private-placeholder",
                     approvedAt="2026-10-10")
        self.assertFalse(any(readiness(candidate).values()))

    def test_governance_decision_alone_does_not_authorize_archive(self):
        candidate = copy.deepcopy(self.registry)
        for g in candidate["gates"]:
            g.update(status="APPROVED", evidenceRef="private-placeholder",
                     approvedAt="2026-10-10")
        candidate["decisionId"] = "W-TEST-ONLY"
        candidate["decisionApproval"] = "simulation"
        candidate["workflow"]["decisionApproved"] = True
        result = readiness(candidate)
        self.assertTrue(result["governanceDecisionReady"])
        self.assertFalse(result["publicMainPromotionReady"])
        self.assertFalse(result["standaloneArchiveReady"])

    def test_public_main_promotion_alone_not_archive(self):
        candidate = copy.deepcopy(self.registry)
        for g in candidate["gates"]:
            g.update(status="APPROVED", evidenceRef="private-placeholder",
                     approvedAt="2026-10-10")
        candidate["decisionId"] = "W-TEST-ONLY"
        candidate["decisionApproval"] = "simulation"
        candidate["workflow"].update(decisionApproved=True, redlineApplied=True,
                                      mainPromotionApproved=True)
        result = readiness(candidate)
        self.assertTrue(result["publicMainPromotionReady"])
        self.assertFalse(result["standaloneArchiveReady"])

    def test_proposal_explicitly_unapproved(self):
        self.assertIn("NOT ASSIGNED A W NUMBER", self.proposal)
        self.assertIn("PROPOSED FOR REVIEW", self.proposal)
        self.assertNotIn("Decision approved on:", self.proposal)

    def test_original_w_328_and_329_retained(self):
        for w in ["W-328", "W-329"]:
            self.assertIn("**" + w + " · 2026-10-03 ·", self.decision_log)
            self.assertIn(w, self.proposal)

    def test_w341_w342_release_controls_preserved(self):
        for w in ["W-341", "W-342"]:
            self.assertIn("**" + w + " · 2026-10-03 ·", self.decision_log)
            self.assertIn(w, self.proposal)
            self.assertIn(w, self.redline)

    def test_original_w_log_hash_untouched(self):
        self.assertEqual(blob_sha((ROOT / DECISIONS).read_bytes()),
                         "49ab9bc513b27ce7e1c2beed6e039aad5c0bebbb")

    def test_pinned_plugin_lock_hash_untouched(self):
        self.assertEqual(blob_sha((ROOT / LOCK).read_bytes()),
                         "c430670577318457972a154012d08c6d28e6d11b")

    def test_manifest_hash_untouched(self):
        self.assertEqual(blob_sha((ROOT / MANIFEST).read_bytes()),
                         "29a05fc71c2f25108f07927870ac5d3d3bdd618b")

    def test_two_old_docs_remain_current(self):
        for p in (OLD_HANDOFF, OLD_RECON):
            self.assertEqual(self.manifest.count(exact_row(p, "current")), 1)

    def test_successor_still_proposal(self):
        self.assertEqual(self.manifest.count(exact_row(CONTRACT, "proposal")), 1)
        self.assertEqual(self.manifest.count(exact_row(CONTRACT, "current")), 0)

    def test_exact_three_registry_preview_lines(self):
        old_rows = [exact_row(CONTRACT, "proposal"),
                    exact_row(OLD_HANDOFF, "current"),
                    exact_row(OLD_RECON, "current")]
        new_rows = [exact_row(CONTRACT, "current"),
                    exact_row(OLD_HANDOFF, "superseded", CONTRACT),
                    exact_row(OLD_RECON, "superseded", CONTRACT)]
        for original, replacement in zip(old_rows, new_rows):
            with self.subTest(row=original):
                self.assertIn("-" + original, self.redline)
                self.assertIn("+" + replacement, self.redline)
                self.assertIn(original, self.manifest)
                self.assertNotIn(replacement, self.manifest)

    def test_no_unreviewed_release_pin_promotion(self):
        for value in ['releaseStatus: pre-release', 'mdseRelease: "0.8.0"',
                      'relationships: "1.36"', 'elementTypes: "1.18"',
                      'localModel: "0.5"', 'candidateVersion: "0.8.19"',
                      '    version: "0.1.18"']:
            with self.subTest(value=value):
                self.assertIn(value, self.manifest)

    def test_no_06_writer_authorization(self):
        self.assertIn("0.6", self.proposal)
        self.assertIn("unsupported", self.proposal)
        self.assertIn("NOT APPROVED", self.proposal)

    def test_readiness_baseline_sha_anchors(self):
        base=self.registry["mainBaseline"]
        self.assertEqual(base["testVault"],
                         "19f565859e4b9fb7ae63004f1b6f0a7de1b9144e")
        self.assertEqual(base["standaloneWorkbench"],
                         "59fc6219b1d0586900aa7d38685e7087a9d47fec")

    def test_no_personal_signatures_or_local_paths(self):
        self.assertTrue(self.registry["roleAssignmentsPersonalDataExcluded"])
        self.assertIsNone(self.registry["approvalEvidence"])

    def test_exact_public_document_paths_in_register(self):
        self.assertEqual(self.registry["proposalPath"], PROPOSAL)
        self.assertEqual(self.registry["redlinePath"], REDLINE)


if __name__ == "__main__":
    unittest.main()
