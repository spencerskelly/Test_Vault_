"""Synthetic preflight tests: no source model data."""
import sys
import pathlib
import unittest
from tempfile import TemporaryDirectory
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from gate_v2_qeax_reconciliation import assess, ensure_private_output

def observed():
    return {"schema":"mdse-ea-local-profile-evidence/1","fileSha256":"test",
      "expected":{"tables":{"t_object":2,"t_connector":3,"t_package":1,"t_diagram":1},
      "elementTypes":{"Class":2},"connectorTypes":{"Dependency":3},"diagramTypes":{"Logical":1}}}

class GateTests(unittest.TestCase):
    def test_both_gates_pass(self):
        result=assess(observed(),observed(),{"status":"PASS"})
        self.assertEqual(result["status"],"PASS")
        self.assertEqual(result["connectorCount"],3)
        self.assertEqual(result["nextStage"],"CONNECTOR_RECONCILIATION_NOT_EXECUTED")
    def test_wrong_profile_blocks(self):
        selected=observed()
        selected["expected"]["tables"]["t_connector"]=99
        self.assertEqual(assess(observed(),selected,{"status":"PASS"})["status"],"BLOCKED")
    def test_table_disposition_blocks(self):
        self.assertEqual(assess(observed(),observed(),{"status":"BLOCKED"})["status"],"BLOCKED")
    def test_private_report_enforced(self):
        with TemporaryDirectory() as d:
            root=pathlib.Path(d)
            with self.assertRaises(ValueError):
                ensure_private_output(root/"private.json",root)
            ensure_private_output(None,root)
    def test_profile_hash_mismatch_blocks(self):
        selected=observed()
        selected["fileSha256"]="wrong"
        self.assertEqual(assess(observed(),selected,{"status":"PASS"})["status"],"BLOCKED")

if __name__=="__main__": unittest.main()
