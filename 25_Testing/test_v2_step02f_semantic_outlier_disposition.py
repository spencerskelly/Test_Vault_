"""Synthetic STEP-02F review classifier tests. No real-model source rows."""
import csv
import importlib.util
import json
import pathlib
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).with_name("v2_step02f_semantic_outlier_disposition.py")
spec = importlib.util.spec_from_file_location("step02f", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class Step02FTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = pathlib.Path(temp.name)
        self.gated = self.root/"gated"
        self.gated.mkdir()
        self.out = self.root/"private-result"
        self.rows = []
        self.append("10", "NoteLink", "Note", "", "Class", "Module", "evidence_only")
        self.append("11", "Aggregation", "Change", "", "Change", "", "deferred_review")
        self.append("12", "Abstraction:allocate", "Trigger", "", "Requirement", "requirement",
                    "deferred_review", direction="Destination -> Source")
        self.write_fixture()

    def append(self, ident, family, source_type, source_stereo, target_type,
               target_stereo, status, direction="Source -> Destination"):
        row = dict.fromkeys(mod.FIELDS, "")
        row.update(source_pk=ident, source_guid="synthetic-guid-"+ident,
                   raw_from=ident, raw_to=str(int(ident)+100), family=family,
                   role="approved-group-review",status=status,
                   normalized_from=ident, normalized_to=str(int(ident)+100),
                   raw_source_type=source_type, raw_source_stereotype=source_stereo,
                   raw_target_type=target_type, raw_target_stereotype=target_stereo,
                   source_direction=direction)
        self.rows.append(row)

    def write_fixture(self):
        with (self.gated/"local_only_phase8_ledger.csv").open("w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=mod.FIELDS);w.writeheader();w.writerows(self.rows)
        count=len(self.rows)
        (self.gated/"gate.local.json").write_text(json.dumps({
            "verified":True,"native_certified":0,"ea_diagrams_processed":0,
            "verified_connector_rows":count,"selected_counts":{"connectors":count}}))
        (self.gated/"aggregate_only.json").write_text(json.dumps({
            "policy_mode":"approved_exact_groups","native_certified":0,
            "native_emission_authorized":False,"ea_diagrams_processed":0,
            "total":count}))
        (self.gated/"input_attestation.local.json").write_text(json.dumps({
            "native_certified":0,"source_sha256":"a"*64}))

    def test_three_exclusive_groups_and_no_native_certification(self):
        output=mod.reconcile(self.gated,self.out)
        self.assertEqual(output["source_connectors"],3)
        self.assertEqual(output["exclusive_dispositions"],
            {"flaglink_candidate":1,"mdse_hierarchy":1,"reference_only":1})
        self.assertEqual(output["native_certified"],0)

    def test_duplicate_source_guid_fails_closed(self):
        self.rows[1]["source_guid"]=self.rows[0]["source_guid"]
        self.write_fixture()
        with self.assertRaisesRegex(ValueError,"DUPLICATE_SOURCE_IDENTITY"):
            mod.reconcile(self.gated,self.out)
        self.assertFalse(self.out.exists())

    def test_unverified_gate_fails_closed(self):
        gate=json.loads((self.gated/"gate.local.json").read_text())
        gate["verified"]=False
        (self.gated/"gate.local.json").write_text(json.dumps(gate))
        with self.assertRaisesRegex(ValueError,"VERIFIED_APPROVED_PHASE8_GATE_REQUIRED"):
            mod.reconcile(self.gated,self.out)
        self.assertFalse(self.out.exists())

    def test_existing_output_and_missing_rows(self):
        self.rows.pop()
        self.write_fixture()
        summary=json.loads((self.gated/"aggregate_only.json").read_text())
        summary["total"]=3
        (self.gated/"aggregate_only.json").write_text(json.dumps(summary))
        with self.assertRaisesRegex(ValueError,"GATED_COUNTS_DISAGREE"):
            mod.reconcile(self.gated,self.out)
        self.assertFalse(self.out.exists())

    def test_flagged_boundary_trace_stays_reference(self):
        row=self.rows[2].copy()
        row.update(family="Dependency:trace",raw_source_type="Boundary",
                   raw_target_type="Class",raw_target_stereotype="Module")
        decision,reason=mod.classify(row)
        self.assertEqual(decision,"boundary_reference")

if __name__=="__main__":unittest.main()
