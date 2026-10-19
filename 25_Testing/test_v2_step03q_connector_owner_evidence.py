import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

PATH=Path(__file__).with_name("v2_step03q_connector_owner_evidence.py")
spec=importlib.util.spec_from_file_location("step03q",PATH)
tool=importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)
ROOT=PATH.parents[1]

class ConnectorEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.src=Path(self.temp.name)/"in.jsonl"
        self.out=Path(self.temp.name)/"out.jsonl"
    def write(self,items):
        self.src.write_text("".join(json.dumps(i)+"\n" for i in items),encoding="utf-8")
    def test_approved_family_stays_uncertified(self):
        self.write([{"artifact_object_id":1,"artifact_guid":"{A}","status":"connector_review",
                     "evidence":{"connectors":[{"connector_id":9,"connector_type":"Dependency",
                                                "stereotype":"","other_object_id":2,"source_end":"start"}]}}])
        result=tool.inspect(self.src,self.out,ROOT)
        record=json.loads(self.out.read_text().strip())
        self.assertEqual(result["categories"]["connector_owner_unconfirmed"],1)
        self.assertIsNone(record["owner_object_id"])
        self.assertEqual(record["connector_evidence"][0]["family"],"Dependency")
        self.assertFalse(record["ownership_confirmed"])
        self.assertFalse(record["connector_evidence"][0]["approved_family_review"]["emission_authorized"])
    def test_parent_and_unassigned_stay_distinct(self):
        self.write([{"artifact_object_id":1,"status":"parent_owner_candidate","owner_object_id":5,"evidence":{}},
                    {"artifact_object_id":2,"status":"unassigned_review","evidence":{}}])
        result=tool.inspect(self.src,self.out,ROOT)
        self.assertEqual(result["categories"],{"parent_owner_candidate":1,"unassigned_review":1})
    def test_duplicate_source_identity_rejected(self):
        self.write([{"artifact_object_id":1,"status":"unassigned_review"},
                    {"artifact_object_id":1,"status":"unassigned_review"}])
        with self.assertRaisesRegex(ValueError,"duplicate"):
            tool.inspect(self.src,self.out,ROOT)
    def test_refuse_overwrite(self):
        self.write([{"artifact_object_id":1,"status":"unassigned_review"}])
        self.out.write_text("sentinel")
        with self.assertRaisesRegex(ValueError,"new"):
            tool.inspect(self.src,self.out,ROOT)
        self.assertEqual(self.out.read_text(),"sentinel")

if __name__=="__main__":
    unittest.main()
