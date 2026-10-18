"""Regression tests for Phase 8 transactional output."""
import json
import csv
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch, MagicMock
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from run_gated_phase8 import execute

class AtomicOutputs(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        d=pathlib.Path(self.temp.name)
        self.q=d/"fake.qeax"
        self.q.write_bytes(b"synthetic")
        self.p=d/"profile.json";self.p.write_text("{}")
        self.policy=d/"policy.json";self.policy.write_text("{}")
        self.registry=d/"registry.json";self.registry.write_text("{}")
        self.out=d/"final"
    def invoke(self,producer):
        fake=MagicMock()
        fake.reconcile.side_effect=producer
        with patch("run_gated_phase8.profile",return_value={}),patch("run_gated_phase8.reconcile",return_value={"status":"PASS"}),patch("run_gated_phase8.assess",return_value={"status":"PASS","connectorCount":2}),patch("run_gated_phase8.importlib.util.spec_from_file_location",return_value=MagicMock()),patch("run_gated_phase8.importlib.util.module_from_spec",return_value=fake),patch("run_gated_phase8.importlib.util.spec.loader.exec_module"):
            return execute(self.q,self.p,self.policy,self.registry,self.out)
    def emit(self,d,ids=(1,2),total=2):
        keys=["source_pk","source_guid","raw_from","raw_to","family","rule","role","status","normalized_from","normalized_to","source_kind","target_kind","diagnostics"]
        with (d/"local_only_phase8_ledger.csv").open("w",newline="") as f:
            w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
            for n in ids:w.writerow({"source_pk":n,"status":"deferred_review"})
        summary={"total":total,"native_certified":0}
        (d/"aggregate_only.json").write_text(json.dumps(summary))
        return summary
    def test_success(self):
        r=self.invoke(lambda q,p,d:self.emit(d))
        self.assertTrue(r["ledgerWritten"])
        self.assertTrue((self.out/"aggregate_only.json").exists())
        self.assertFalse(list(self.out.parent.glob(".phase8-staging-*")))
    def test_duplicate_fails_clean(self):
        with self.assertRaises(RuntimeError):self.invoke(lambda q,p,d:self.emit(d,(1,1)))
        self.assertFalse(self.out.exists())
    def test_short_ledger_fails_clean(self):
        with self.assertRaises(RuntimeError):self.invoke(lambda q,p,d:self.emit(d,(1,)))
        self.assertFalse(self.out.exists())
    def test_missing_files_fails_clean(self):
        with self.assertRaises(RuntimeError):self.invoke(lambda q,p,d:{"total":2,"native_certified":0})
        self.assertFalse(self.out.exists())
    def test_existing_destination_refused(self):
        self.out.mkdir()
        with self.assertRaises(ValueError):self.invoke(lambda q,p,d:self.emit(d))
        self.assertEqual(list(self.out.iterdir()),[])
    def test_exception_rolls_back(self):
        def fail(q,p,d):
            (d/"partial").write_text("x")
            raise RuntimeError("synthetic failure")
        with self.assertRaises(RuntimeError):self.invoke(fail)
        self.assertFalse(self.out.exists())
        self.assertFalse(list(self.out.parent.glob(".phase8-staging-*")))
if __name__=="__main__":unittest.main()
