"""Synthetic integration gate tests; no proprietary QEAX or source GUIDs."""
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from run_gated_phase8 import execute

def obs():
    return {"fileSha256":"dummy","expected":{"tables":{"t_object":1,"t_connector":2},
        "elementTypes":{"Class":1},"connectorTypes":{"Dependency":2},
        "diagramTypes":{"Logical":1}}}

class GatedRunnerTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root=pathlib.Path(self.tmp.name)
        self.qeax=root/"dummy.qeax"
        self.qeax.write_bytes(b"synthetic")
        self.profile=root/"selected.json"
        self.policy=root/"policy.json"
        self.registry=root/"registry.json"
        self.profile.write_text("{}")
        self.policy.write_text("{}")
        self.registry.write_text("{}")
        self.out=root/"ledger"

    def test_profile_failure_writes_no_ledger(self):
        with patch("run_gated_phase8.profile",return_value=obs()),\
             patch("run_gated_phase8.reconcile",return_value={"status":"PASS"}),\
             patch("run_gated_phase8.assess",return_value={"status":"BLOCKED"}):
            result=execute(self.qeax,self.profile,self.policy,self.registry,self.out)
        self.assertEqual(result["status"],"BLOCKED")
        self.assertFalse(self.out.exists())
        self.assertFalse(result["ledgerWritten"])

    def test_table_policy_failure_writes_no_ledger(self):
        with patch("run_gated_phase8.profile",return_value=obs()),\
             patch("run_gated_phase8.reconcile",return_value={"status":"BLOCKED"}),\
             patch("run_gated_phase8.assess",return_value={"status":"BLOCKED"}):
            result=execute(self.qeax,self.profile,self.policy,self.registry,self.out)
        self.assertFalse(result["ledgerWritten"])
        self.assertFalse(self.out.exists())

    def test_missing_registry_fails_before_side_effects(self):
        self.registry.unlink()
        with self.assertRaises(ValueError):
            execute(self.qeax,self.profile,self.policy,self.registry,self.out)
        self.assertFalse(self.out.exists())

    def test_output_rejected_in_repository_checkout(self):
        with self.assertRaises(ValueError):
            execute(self.qeax,self.profile,self.policy,self.registry,
                    pathlib.Path(__file__).resolve().parent/"private-ledger")

if __name__=="__main__":
    unittest.main()
