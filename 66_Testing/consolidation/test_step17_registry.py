"""Fail-closed Step17 document registry proposal tests (no live manifest edits)."""
from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path
from step18_registry_candidate import baseline as _step18_baseline, INVENTORY as _STEP18_INVENTORY

from step17_registry_review import (
    MANIFEST_PATH, PROPOSAL_PATH, ROOT, SCAN_FOLDERS,
    existing_rows, git_blob_sha, render_rows, simulate_manifest,
    tracked_md, validate,
)

def _step18_original_manifest():
    return _step18_baseline((Path(__file__).resolve().parents[2] / "Base Vault/Definition/mdse-release.yaml").read_text(encoding="utf-8"), json.loads(_STEP18_INVENTORY.read_text(encoding="utf-8")))

class Step17DocumentRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = _step18_original_manifest()
        cls.proposal = json.loads(PROPOSAL_PATH.read_text(encoding="utf-8"))

    def mutate(self, key, value):
        changed = copy.deepcopy(self.proposal)
        changed["entries"][0][key] = value
        return changed

    def test_exact_baseline_manifest_sha(self):
        self.assertEqual(git_blob_sha(_step18_original_manifest().encode("utf-8")),
                         "29a05fc71c2f25108f07927870ac5d3d3bdd618b")

    def test_explicit_review_only_state(self):
        self.assertEqual(self.proposal["changeStatus"],
                         "PROPOSAL_ONLY_NO_LIVE_MANIFEST_MODIFICATION")

    def test_no_current_or_approved_registry_rows(self):
        self.assertTrue(all(e["proposedStatus"] in ("reference","proposal") and
                            e["reviewDecision"] == "PENDING_DOCUMENT_CONTROL_APPROVAL"
                            for e in self.proposal["entries"]))

    def test_exactly_thirty_two_paths(self):
        self.assertEqual(len(self.proposal["entries"]), 32)

    def test_29_references_3_unapproved_proposals(self):
        statuses = [e["proposedStatus"] for e in self.proposal["entries"]]
        self.assertEqual(statuses.count("reference"), 29)
        self.assertEqual(statuses.count("proposal"), 3)

    def test_all_missing_entries_live_only_under_workspace(self):
        for e in self.proposal["entries"]:
            self.assertTrue(e["path"].startswith("00_Workspace/"))
            self.assertEqual(e["path"].count("/"), 1)

    def test_every_missing_source_sha_matches_git_blob(self):
        for e in self.proposal["entries"]:
            with self.subTest(e=e["path"]):
                self.assertEqual(git_blob_sha((ROOT / e["path"]).read_bytes()),e["sha"])

    def test_no_empty_titles(self):
        for e in self.proposal["entries"]:
            with self.subTest(e=e["path"]):
                self.assertTrue((ROOT / e["path"]).read_text(encoding="utf-8").startswith("# "))

    def test_only_these_two_top_level_scopes(self):
        self.assertEqual(SCAN_FOLDERS, ("00_Workspace","Importer/Definition"))

    def test_importer_definition_has_zero_missing_entries(self):
        registered = existing_rows(self.manifest)
        self.assertFalse(tracked_md("Importer/Definition")-registered)

    def test_tree_set_matches_exact_unregistered_list(self):
        registered = existing_rows(self.manifest)
        actual = set().union(*(tracked_md(p) for p in SCAN_FOLDERS))
        expected = {x["path"] for x in self.proposal["entries"]}
        self.assertEqual(actual - registered,expected)

    def test_existing_registered_entries_stay_untouched(self):
        after = simulate_manifest(self.manifest,self.proposal)
        self.assertTrue(existing_rows(self.manifest).issubset(existing_rows(after)))

    def test_rehearsal_closes_only_registry_path_gap_in_memory(self):
        after = simulate_manifest(self.manifest,self.proposal)
        actual = set().union(*(tracked_md(p) for p in SCAN_FOLDERS))
        self.assertFalse(actual-existing_rows(after))

    def test_reversal_is_byte_for_byte(self):
        after = simulate_manifest(self.manifest,self.proposal)
        rows = render_rows(self.proposal["entries"])
        self.assertEqual(after.replace("\ndocuments:\n"+rows,
                                       "\ndocuments:\n",1),self.manifest)

    def test_live_manifest_never_written(self):
        before = MANIFEST_PATH.read_bytes()
        simulate_manifest(self.manifest,self.proposal)
        self.assertEqual(MANIFEST_PATH.read_bytes(),before)

    def test_preview_is_exactly_thirty_two_marked_lines(self):
        lines = render_rows(self.proposal["entries"]).splitlines()
        self.assertEqual(len(lines),32)
        for line in lines:
            self.assertTrue(line.startswith('  - {path: "00_Workspace/'))
            self.assertRegex(line,r', status: (reference|proposal)\}$')

    def test_explicit_governance_documents_proposed_only(self):
        selected={e["path"] for e in self.proposal["entries"]
                  if e["proposedStatus"]=="proposal"}
        self.assertEqual(selected,{
          "00_Workspace/Consolidation Step 09 - Proposed W Authority Decision 2026-10-10.md",
          "00_Workspace/Consolidation Step 15 - Exact Registry Redline and Promotion Stops 2026-10-10.md",
          "00_Workspace/Consolidation Step 15 - Proposed W Decision and Authority Signoff 2026-10-10.md",
        })
        for p in selected:
            t=(ROOT/p).read_text(encoding="utf-8").upper()
            self.assertTrue("PROPOSAL" in t or "REVIEW ONLY" in t)

    def test_excludes_qeax_binary(self):
        self.assertFalse(any(e["path"].endswith(".qeax.zip")
                             for e in self.proposal["entries"]))

    def test_baseline_is_not_approved_registry_status(self):
        self.assertEqual(validate(self.manifest,self.proposal)["release_status"],
                         "NOT_APPROVED")

    def test_fails_wrong_manifest_sha(self):
        with self.assertRaises(ValueError):
            validate(self.manifest.replace("pre-release","release",1),
                     self.proposal,check_git=False)

    def test_fails_unexpected_missing_document(self):
        altered=self.mutate("path","00_Workspace/Not-In-Tree.md")
        with self.assertRaises(ValueError):
            validate(self.manifest,altered,check_git=False)

    def test_fails_drifted_document_sha(self):
        with self.assertRaises(ValueError):
            validate(self.manifest,self.mutate("sha","0"*40),check_git=False)

    def test_fails_approval_promotion(self):
        with self.assertRaises(ValueError):
            validate(self.manifest,self.mutate("proposedStatus","current"),check_git=False)

    def test_fails_historical_status_without_banner(self):
        with self.assertRaises(ValueError):
            validate(self.manifest,self.mutate("proposedStatus","historical"),check_git=False)

    def test_fails_unreviewed_decision(self):
        with self.assertRaises(ValueError):
            validate(self.manifest,self.mutate("reviewDecision","APPROVED"),check_git=False)

    def test_fails_duplicated_row(self):
        broken=copy.deepcopy(self.proposal)
        broken["entries"][1]["path"]=broken["entries"][0]["path"]
        with self.assertRaises(ValueError):
            validate(self.manifest,broken,check_git=False)

    def test_fails_unexpected_registry_status(self):
        broken=copy.deepcopy(self.proposal)
        broken["changeStatus"]="APPROVED"
        with self.assertRaises(ValueError):
            validate(self.manifest,broken,check_git=False)

    def test_rejects_duplicate_existing_manifest_path(self):
        row='  - {path: "00_Workspace/00 - Current State.md", status: current}\n'
        with self.assertRaises(ValueError):
            existing_rows(self.manifest+row)

    def test_rejects_missing_proposal_documents_anchor(self):
        with self.assertRaises(ValueError):
            simulate_manifest(self.manifest.replace("\ndocuments:\n","\ndocuments_copy:\n"),
                              self.proposal)

    def test_refuses_duplicate_rows_after_proposal_replay(self):
        proposed = simulate_manifest(self.manifest,self.proposal)
        with self.assertRaises(ValueError):
            validate(proposed,self.proposal,check_git=False)

if __name__ == "__main__":
    unittest.main()
