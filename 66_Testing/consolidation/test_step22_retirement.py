"""Step22 single active repository handoff integrity; archival remains unclaimed."""
from __future__ import annotations
import hashlib
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/"66_Testing/consolidation/step22_legacy_workbench_inventory.json"
NOTICE=ROOT/"66_Testing/consolidation/STEP22_SINGLE_REPO_CUTOVER.md"
OLD_MAIN="59fc6219b1d0586900aa7d38685e7087a9d47fec"
NEW_CANDIDATE="952aaecfc16891f2155b78f174340fd70e764683"
ARCHIVE_WORKFLOW="55_Workbench/docs/Reference/ARCHIVE_BOM_A14_BASELINE_CHECK.yml"

def sha(raw):
    return hashlib.sha1(("blob "+str(len(raw))+"\0").encode()+raw).hexdigest()

class Step22RetirementIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads(DATA.read_text(encoding="utf-8"))

    def test_inventory_review_only(self):
        self.assertEqual(self.data["status"],"DEVELOPMENT_SWITCH_PROPOSED_ARCHIVE_NOT_YET_PERFORMED")

    def test_source_repo_pinned(self):
        self.assertEqual(self.data["oldRepository"],"spencerskelly/MDSE_Workbench")
        self.assertEqual(self.data["oldRepositoryMain"],OLD_MAIN)

    def test_all_nineteen_remote_branch_tips_listed(self):
        branches=self.data["branches"]
        self.assertEqual(len(branches),19)
        self.assertEqual(len({x["branch"] for x in branches}),19)

    def test_three_open_prs_distinct(self):
        prs=self.data["openDraftPRs"]
        self.assertEqual(len(prs),3)
        self.assertEqual({x["number"] for x in prs},{6,7,15})
        self.assertTrue(all(x["status"]=="OPEN_DRAFT" for x in prs))

    def test_main_coverage_no_missing_source_paths(self):
        p=self.data["pathInventory"]
        self.assertEqual(p["sourceOldMainBlobCount"],60193)
        self.assertEqual(p["identicalPathAndBlobCount"],60175)
        self.assertEqual(p["changedPathCount"],18)
        self.assertEqual(p["missingOldMainPathCount"],0)
        self.assertEqual(p["stagedAdditionalFilePaths"],56)
        self.assertFalse(p["sourceTruncated"])
        self.assertFalse(p["stagedTruncated"])

    def test_candidate_source_root(self):
        a=self.data["proposedAuthority"]
        self.assertEqual(a["repository"],"spencerskelly/Test_Vault_")
        self.assertEqual(a["commit"],NEW_CANDIDATE)
        self.assertEqual(a["workbenchRoot"],"55_Workbench/")
        self.assertFalse(a["mainPromotionApproved"])

    def test_bom_workflow_exact_source_copy(self):
        self.assertTrue(self.data["historicalWorkflow"]["verifiedIdentical"])
        self.assertEqual(sha((ROOT/ARCHIVE_WORKFLOW).read_bytes()),
                         "3c58fa778d60b7e3d425f67972c136da726b7740")

    def test_runtime_lock_unchanged(self):
        self.assertEqual(sha((ROOT/".obsidian/plugin-lock.yaml").read_bytes()),
                         "c430670577318457972a154012d08c6d28e6d11b")

    def test_w_decision_log_unchanged(self):
        self.assertEqual(sha((ROOT/"00_Workspace/Workspace Decision Log.md").read_bytes()),
                         "49ab9bc513b27ce7e1c2beed6e039aad5c0bebbb")

    def test_model_remains_pre_release(self):
        s=(ROOT/"Base Vault/Definition/mdse-release.yaml").read_text()
        self.assertIn('mdseRelease: "0.8.0"',s)
        self.assertIn('releaseStatus: pre-release',s)

    def test_archival_gui_and_local_signoffs_not_claimed(self):
        d=self.data["blockerStates"]
        self.assertEqual(d["workbenchStandaloneArchival"],"NOT_EXECUTED")
        self.assertEqual(d["actualMacWindowsObsidianGui"],"NOT_RUN")
        self.assertEqual(d["localUnpushedWorkSignoffs"],"UNKNOWN_NOT_REMOTE_VERIFIABLE")

    def test_old_pr_proposals_not_approved(self):
        self.assertTrue(all("explicit new Test_Vault approval" in x["disposition"]
                            for x in self.data["openDraftPRs"]))

    def test_single_repo_handoff_instructions_present(self):
        s=NOTICE.read_text()
        self.assertIn("Use "+chr(96)+"spencerskelly/Test_Vault_"+chr(96)+" for all NEW",s)
        self.assertIn("Archive this repository",s)
        self.assertIn("Test_Vault_/main",s)

    def test_public_model_owner_gate_still_open(self):
        self.assertEqual(self.data["blockerStates"]["publicQEAXOwnerSecurityDisposition"],"PENDING")

if __name__=="__main__":
    unittest.main()
