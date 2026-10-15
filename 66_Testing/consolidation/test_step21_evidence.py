"""Step21 evidence gate: fail closed and never infer real Obsidian GUI results."""
from __future__ import annotations
import copy
import json
import os
import tempfile
import unittest
from pathlib import Path
from step21_evidence import CASES,blank_record,evaluate,check_pair
from step21_prepare_session import fixture_snapshot,prepare,ROOT

SHA="fbaa400fd9613b7abf2d32cab09c0bdafe8cb8ce"
LOCK="a"*64
FIXTURE="b"*64
TIME="2026-10-11T23:00:00Z"

def fixture(platform="macos"):
    return blank_record(platform,SHA,LOCK,FIXTURE)

def mark(doc,index,status,*,defect=None):
    row=doc["caseRecords"][index]
    row.update(status=status,observed="Observed behavior recorded by a real operator",
               observedAtUtc=TIME,evidenceRefs=["private/screenshots/G20-01.png"],defectRef=defect)
    doc.update(operatorAlias="tester",osVersion="observed OS",
               obsidianVersion="observed Obsidian",observedWorkbenchVersion="0.1.18",
               observedBootstrapVersion="0.3.0",sessionStartUtc=TIME)
    return doc

class Step21EvidenceTests(unittest.TestCase):
    def test_16_canonical_ids(self):
        self.assertEqual(len(CASES),16)
        self.assertEqual(CASES[0],"G20-01")
        self.assertEqual(CASES[-1],"G20-16")

    def test_default_macos_never_executed(self):
        doc=fixture()
        s=evaluate(doc)
        self.assertEqual(s["count"]["NOT RUN"],16)
        self.assertFalse(s["operatorEvidenceComplete"])
        self.assertFalse(s["externalPromotionGatesCleared"])

    def test_default_windows_never_executed(self):
        self.assertEqual(evaluate(fixture("windows"))["count"]["PASS"],0)

    def test_pair_default_same_source_not_reviewed(self):
        s=check_pair(fixture(),fixture("windows"))
        self.assertTrue(s["matchedSource"])
        self.assertFalse(s["bothGuiEvidenceReviewed"])
        self.assertFalse(s["publicMainPromotionAllowed"])

    def test_missing_evidence_reference_rejected(self):
        d=mark(fixture(),0,"PASS")
        d["caseRecords"][0]["evidenceRefs"]=[]
        with self.assertRaises(ValueError):evaluate(d)

    def test_empty_actual_observation_rejected(self):
        d=mark(fixture(),0,"PASS")
        d["caseRecords"][0]["observed"]=""
        with self.assertRaises(ValueError):evaluate(d)

    def test_timestamp_must_be_utc(self):
        d=mark(fixture(),0,"PASS")
        d["caseRecords"][0]["observedAtUtc"]="October 11"
        with self.assertRaises(ValueError):evaluate(d)

    def test_missing_operator_metadata_rejected(self):
        d=mark(fixture(),0,"PASS")
        d["obsidianVersion"]=None
        with self.assertRaises(ValueError):evaluate(d)

    def test_fail_requires_defect(self):
        d=mark(fixture(),0,"FAIL")
        with self.assertRaises(ValueError):evaluate(d)

    def test_fail_with_defect_is_recorded_not_approved(self):
        d=mark(fixture(),0,"FAIL",defect="private/defects/123")
        x=evaluate(d)
        self.assertEqual(x["count"]["FAIL"],1)
        self.assertFalse(x["operatorEvidenceComplete"])

    def test_blocked_requires_observation(self):
        d=mark(fixture(),0,"BLOCKED")
        d["caseRecords"][0]["observed"]=None
        with self.assertRaises(ValueError):evaluate(d)

    def test_unsupported_pass_spelling_rejected(self):
        d=fixture()
        d["caseRecords"][0]["status"]="Passed"
        with self.assertRaises(ValueError):evaluate(d)

    def test_not_run_cannot_claim_screenshot(self):
        d=fixture()
        d["caseRecords"][0]["evidenceRefs"]=["artifact"]
        with self.assertRaises(ValueError):evaluate(d)

    def test_duplicate_or_missing_id_rejected(self):
        d=fixture()
        d["caseRecords"][1]["id"]=d["caseRecords"][0]["id"]
        with self.assertRaises(ValueError):evaluate(d)

    def test_unknown_platform_rejected(self):
        d=fixture()
        d["platform"]="linux"
        with self.assertRaises(ValueError):evaluate(d)

    def test_bad_git_sha_rejected(self):
        d=fixture()
        d["sourceCommit"]="not-sha"
        with self.assertRaises(ValueError):evaluate(d)

    def test_bad_lock_sha_rejected(self):
        d=fixture()
        d["pluginLockSha256"]="a"*30
        with self.assertRaises(ValueError):evaluate(d)

    def test_wrong_target_platform_rejected(self):
        with self.assertRaises(ValueError):evaluate(fixture("macos"),expected_platform="windows")

    def test_other_platform_case_cannot_pass_on_mac(self):
        d=mark(fixture("macos"),15,"PASS")
        with self.assertRaises(ValueError):evaluate(d)

    def test_other_platform_case_cannot_pass_on_windows(self):
        d=mark(fixture("windows"),14,"PASS")
        with self.assertRaises(ValueError):evaluate(d)

    def test_premature_review_approval_rejected(self):
        d=fixture()
        d["guiApproval"]="REVIEWED"
        with self.assertRaises(ValueError):evaluate(d)

    def test_complete_synthetic_record_does_not_allow_main_merge(self):
        d=fixture()
        for i in range(14):mark(d,i,"PASS")
        mark(d,14,"PASS")
        d["reviewerAlias"]="private-reviewer"
        d["guiApproval"]="REVIEWED"
        result=evaluate(d)
        self.assertTrue(result["operatorEvidenceComplete"])
        self.assertFalse(result["externalPromotionGatesCleared"])
        self.assertFalse(result["releaseIssued"])

    def test_matched_both_syntactic_passes_still_no_archive_permission(self):
        a=fixture()
        b=fixture("windows")
        for i in range(14):
            mark(a,i,"PASS")
            mark(b,i,"PASS")
        mark(a,14,"PASS")
        mark(b,15,"PASS")
        a["reviewerAlias"]=b["reviewerAlias"]="private-reviewer"
        a["guiApproval"]=b["guiApproval"]="REVIEWED"
        result=check_pair(a,b)
        self.assertTrue(result["bothGuiEvidenceReviewed"])
        self.assertFalse(result["standaloneArchiveAllowed"])
        self.assertFalse(result["publicMainPromotionAllowed"])

    def test_different_commit_blocks_platform_pair(self):
        b=fixture("windows")
        b["sourceCommit"]="0"*40
        with self.assertRaises(ValueError):check_pair(fixture(),b)

    def test_different_plugin_lock_blocks_platform_pair(self):
        b=fixture("windows")
        b["pluginLockSha256"]="0"*64
        with self.assertRaises(ValueError):check_pair(fixture(),b)

    def test_different_fixture_blocks_platform_pair(self):
        b=fixture("windows")
        b["fixtureSnapshotSha256"]="0"*64
        with self.assertRaises(ValueError):check_pair(fixture(),b)

    def test_out_of_repository_constraint(self):
        # An existing checkout would be immediately rejected; no writes occur.
        with self.assertRaises(ValueError):prepare(ROOT/"66_Testing"/"new-private-evidence","macos")

    def test_existing_private_session_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):prepare(d,"windows")

    def test_evidence_json_roundtrip_is_pending(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"record.json"
            p.write_text(json.dumps(fixture()))
            self.assertEqual(evaluate(json.loads(p.read_text()))["count"]["NOT RUN"],16)

if __name__=="__main__":
    unittest.main()
