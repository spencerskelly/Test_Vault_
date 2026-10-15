"""Step18 exact registry application candidate, without promotion authority."""
import copy
import json
import unittest
from pathlib import Path
from step18_registry_candidate import MANIFEST,INVENTORY,BASE,CANDIDATE,ANCHOR,audit,baseline,rows,sha
from step17_registry_review import existing_rows,tracked_md,SCAN_FOLDERS

class Step18RegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=MANIFEST.read_text()
        cls.p=json.loads(INVENTORY.read_text())
    def test_exact_candidate_blob(self):
        self.assertEqual(sha(MANIFEST.read_bytes()),CANDIDATE)
    def test_exact_prior_blob(self):
        self.assertEqual(sha(baseline(self.m,self.p).encode()),BASE)
    def test_exact_32_rows(self):
        self.assertEqual(rows(self.p).count("\n"),32)
    def test_count_29_reference(self):
        self.assertEqual(sum(x["proposedStatus"]=="reference" for x in self.p["entries"]),29)
    def test_count_3_proposal(self):
        self.assertEqual(sum(x["proposedStatus"]=="proposal" for x in self.p["entries"]),3)
    def test_insertion_immediately_after_documents(self):
        self.assertIn(ANCHOR+rows(self.p),self.m)
    def test_roundtrip_restores_every_original_byte(self):
        original=baseline(self.m,self.p)
        self.assertEqual(original.replace(ANCHOR,ANCHOR+rows(self.p),1),self.m)
    def test_exact_registry_no_missing(self):
        self.assertEqual(audit(self.m,self.p)["missing"],0)
    def test_sourced_hashes_match_exact(self):
        self.assertEqual(audit(self.m,self.p)["inserted"],32)
    def test_original_registered_entries_retained(self):
        a=existing_rows(baseline(self.m,self.p));b=existing_rows(self.m)
        self.assertEqual(len(b-a),32)
        self.assertFalse(a-b)
    def test_no_new_current_entries(self):
        self.assertNotIn("status: current",rows(self.p))
    def test_no_premature_approved_proposal(self):
        self.assertTrue(all(x["reviewDecision"]=="PENDING_DOCUMENT_CONTROL_APPROVAL" for x in self.p["entries"]))
    def test_governance_old_handoffs_still_current(self):
        for p in ("00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md","00_Workspace/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md"):
            self.assertIn('path: "'+p+'", status: current',self.m)
    def test_step13_successor_still_proposal(self):
        self.assertIn('MDSE v0.8 Unified Development Continuation Contract - PROPOSAL 2026-10-10.md", status: proposal',self.m)
    def test_schema_and_release_pins_unchanged(self):
        for pin in ('releaseStatus: pre-release','relationships: "1.36"','elementTypes: "1.18"','localModel: "0.5"','version: "0.1.18"'):
            self.assertIn(pin,self.m)
    def test_mutated_manifest_rejected(self):
        with self.assertRaises(ValueError): audit(self.m.replace("pre-release","release",1),self.p)
    def test_missing_proposal_row_rejected(self):
        with self.assertRaises(ValueError): baseline(self.m.replace(rows(self.p).splitlines(True)[0],"",1),self.p)
    def test_duplicate_proposal_row_rejected(self):
        x=copy.deepcopy(self.p);x["entries"][1]["path"]=x["entries"][0]["path"]
        with self.assertRaises(ValueError): rows(x)
    def test_status_promoted_rejected(self):
        x=copy.deepcopy(self.p);x["entries"][0]["proposedStatus"]="current"
        with self.assertRaises(ValueError): rows(x)
    def test_bad_source_hash_rejected(self):
        x=copy.deepcopy(self.p);x["entries"][0]["sha"]="0"*40
        with self.assertRaises(ValueError): audit(self.m,x)
    def test_unexpected_new_unregistered_file_rejected(self):
        a=set().union(*(tracked_md(d) for d in SCAN_FOLDERS))
        self.assertFalse(a-existing_rows(self.m))
    def test_no_source_model_archive_in_registry(self):
        self.assertFalse(any(".qeax" in e["path"].lower() for e in self.p["entries"]))
    def test_manifest_file_not_written_by_helper(self):
        before=MANIFEST.read_bytes();audit(self.m,self.p)
        self.assertEqual(before,MANIFEST.read_bytes())

if __name__=="__main__":unittest.main()
