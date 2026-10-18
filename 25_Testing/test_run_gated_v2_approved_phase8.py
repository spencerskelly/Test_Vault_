"""Synthetic STEP-02D gated QEAX acceptance. Never commit proprietary source rows."""
import csv
import importlib.util
import json
import pathlib
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "25_Testing/run_gated_v2_approved_phase8.py"
spec = importlib.util.spec_from_file_location("v2_gate", SCRIPT)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


class CurrentV2GateTests(unittest.TestCase):
    def setUp(self):
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        self.home = pathlib.Path(td.name)
        self.qeax = self.home / "synthetic.qeax"
        self.dest = self.home / "approved_ledger"
        with sqlite3.connect(self.qeax) as db:
            db.execute("CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT)")
            db.executemany("INSERT INTO t_object VALUES (?,?,?)", [
                (1,"Class","block"),(2,"Class","Hardware Component"),
                (3,"InformationItem",""),(4,"Part","")
            ])
            db.execute("CREATE TABLE t_package(Package_ID INTEGER)")
            db.execute("INSERT INTO t_package VALUES (1)")
            db.execute("""CREATE TABLE t_connector(
                Connector_ID INTEGER,ea_guid TEXT,Connector_Type TEXT,Stereotype TEXT,
                Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER,
                SourceIsAggregate INTEGER,DestIsAggregate INTEGER,
                SourceRole TEXT,DestRole TEXT,SourceCard TEXT,DestCard TEXT)""")
            db.executemany("INSERT INTO t_connector VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",[
                (10,"synthetic-generalization","Generalization","","Source -> Destination",
                 1,2,0,0,"","","",""),
                (11,"synthetic-shared","Aggregation","","Source -> Destination",
                 1,4,1,0,"owner","feature","1","0..*"),
                (12,"synthetic-nonnative","Dependency","","Unspecified",
                 1,3,0,0,"","","",""),
                (13,"synthetic-unknown","Undeclared","","Source -> Destination",
                 1,2,0,0,"","","",""),
            ])
        self.profile={"elements":4,"connectors":4,"packages":1}

    def invoke(self, out=None, **kwargs):
        return gate.execute(self.qeax, out or self.dest, expected_counts=self.profile, **kwargs)

    def test_full_gate_and_private_ledger(self):
        result=self.invoke()
        self.assertEqual(result["status"],"RECONCILED_EVIDENCE_ONLY")
        self.assertTrue(result["ledgerWritten"])
        self.assertEqual(result["verified_connector_rows"],4)
        self.assertEqual(result["aggregate"]["unmatched_connector_rows"],1)
        self.assertEqual(result["nativeCertified"],0)
        with (self.dest/"local_only_phase8_ledger.csv").open(newline="") as f:
            rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),4)
        self.assertEqual(len(rows[0]),len(gate.REQUIRED_FIELDS))
        self.assertEqual(rows[1]["source_role"],"owner")
        self.assertEqual(rows[1]["source_cardinality"],"1")
        self.assertEqual(rows[1]["target_cardinality"],"0..*")
        self.assertEqual(rows[1]["source_aggregation_flag"],"1")
        self.assertEqual(rows[1]["raw_from"],rows[1]["normalized_from"])
        self.assertEqual(rows[1]["raw_to"],rows[1]["normalized_to"])
        self.assertEqual(json.loads((self.dest/"gate.local.json").read_text())["verified"],True)
        self.assertFalse(list(self.home.glob(".v2-approved-stage-*")))
        with self.assertRaisesRegex(ValueError,"OUTPUT_ALREADY_EXISTS"):
            self.invoke()

    def test_profile_drift_blocks_without_ledger_or_stage(self):
        result=gate.execute(self.qeax,self.dest,expected_counts={
            "elements":4,"connectors":999,"packages":1})
        self.assertEqual(result["status"],"BLOCKED")
        self.assertFalse(result["ledgerWritten"])
        self.assertFalse(self.dest.exists())
        self.assertFalse(list(self.home.glob(".v2-approved-stage-*")))

    def test_missing_identity_or_tampering_rolls_back(self):
        real_module=gate.load_module
        def mocked(name,path):
            module=real_module(name,path)
            if name=="v2_phase8_normalizer":
                original=module.reconcile
                def changed(*args):
                    summary=original(*args)
                    csv_path=pathlib.Path(args[2])/"local_only_phase8_ledger.csv"
                    text=csv_path.read_text(encoding="utf-8")
                    csv_path.write_text(text.replace("synthetic-shared","tampered-guid"))
                    return summary
                module.reconcile=changed
            return module
        with patch.object(gate,"load_module",side_effect=mocked):
            with self.assertRaisesRegex(ValueError,"SOURCE_EVIDENCE_MISMATCH"):
                self.invoke()
        self.assertFalse(self.dest.exists())
        self.assertFalse(list(self.home.glob(".v2-approved-stage-*")))

    def test_invalid_registry_and_private_path(self):
        bad=self.home/"candidate.json"
        bad.write_text(json.dumps({"families":[]}))
        with self.assertRaises(ValueError):
            self.invoke(registry=bad)
        with self.assertRaisesRegex(ValueError,"PRIVATE_LEDGER_MUST_BE_OUTSIDE_REPOSITORY"):
            self.invoke(out=ROOT/"do-not-write-here")
        self.assertFalse(self.dest.exists())

    def test_diagram_agnostic(self):
        original=self.invoke(self.home/"without_diagrams")
        with sqlite3.connect(self.qeax) as db:
            db.execute("CREATE TABLE t_diagram(Diagram_ID INTEGER)")
            db.execute("INSERT INTO t_diagram VALUES (99)")
        compared=self.invoke(self.home/"with_diagrams")
        self.assertEqual(compared["aggregate"],original["aggregate"])
        self.assertEqual(compared["eaDiagramsProcessed"],0)

if __name__ == "__main__":
    unittest.main()
