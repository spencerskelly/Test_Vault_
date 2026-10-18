"""Synthetic profile-selection contract tests; no enterprise model data."""
import importlib.util
import pathlib
import unittest

SOURCE=pathlib.Path(__file__).resolve().parent/"check_qeax_source_profile.py"
spec=importlib.util.spec_from_file_location("profile_gate",SOURCE)
# profile_qeax_local is imported from the same directory by the command-line tool.
import sys
sys.path.insert(0,str(SOURCE.parent))
gate=importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

def fixture():
    return {"schema":"mdse-ea-local-profile-evidence/1","profileId":"fixture-reduced",
            "fileSha256":"fixture-sha","expected":{
             "tables":{"t_object":3,"t_connector":2,"t_package":1,"t_diagram":1},
             "elementTypes":{"Class":2,"Requirement":1},
             "connectorTypes":{"Dependency":2},"diagramTypes":{"Logical":1}}}

class SourceProfileSelection(unittest.TestCase):
    def test_matching_source(self):
        p=fixture()
        self.assertEqual(gate.compare(p,p)["status"],"PASS")
    def test_wrong_full_profile_fails(self):
        p=fixture()
        full=fixture()
        full["expected"]["tables"]["t_object"]=999
        self.assertEqual(gate.compare(p,full)["status"],"BLOCKED")
    def test_new_source_kind_fails(self):
        p=fixture()
        p["expected"]["elementTypes"]["NewThing"]=1
        self.assertIn("UNEXPECTED_SOURCE_KIND",[i["category"] for i in gate.compare(p,fixture())["issues"]])
    def test_hash_drift_fails(self):
        p=fixture()
        p["fileSha256"]="changed"
        self.assertIn("SOURCE_FILE_HASH_MISMATCH",[i["category"] for i in gate.compare(p,fixture())["issues"]])
    def test_missing_section_fails(self):
        p=fixture()
        del p["expected"]["connectorTypes"]
        self.assertIn("PROFILE_SECTION_MISSING",[i["category"] for i in gate.compare(fixture(),p)["issues"]])

if __name__=="__main__":
    unittest.main()
