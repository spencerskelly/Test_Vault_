import importlib.util,json,tempfile,unittest
from pathlib import Path
p=Path(__file__).with_name("v2_step03p_attachment_owner_candidates.py")
spec=importlib.util.spec_from_file_location("owner_candidate_tool",p)
tool=importlib.util.module_from_spec(spec);spec.loader.exec_module(tool)

class CandidateTests(unittest.TestCase):
    def setUp(self):
        tmp=tempfile.TemporaryDirectory();self.addCleanup(tmp.cleanup)
        self.root=Path(tmp.name);self.source=self.root/"source.jsonl";self.out=self.root/"out.jsonl"
    def write(self,items):
        self.source.write_text("".join(json.dumps(i)+"\n" for i in items))
    def test_parent_and_review_classification(self):
        self.write([
            {"artifact_object_id":1,"artifact_guid":"a","parent_object_id":5,"connector_evidence":[]},
            {"artifact_object_id":2,"artifact_guid":"b","parent_object_id":None,"connector_evidence":[{"connector_id":7}]},
            {"artifact_object_id":3,"artifact_guid":"c","parent_object_id":None,"connector_evidence":[]}])
        result=tool.resolve(self.source,self.out)
        self.assertEqual(result["categories"],{"parent_owner_candidate":1,"connector_review":1,"unassigned_review":1})
        rows=[json.loads(x) for x in self.out.read_text().splitlines()]
        self.assertEqual(rows[0]["owner_object_id"],5)
        self.assertIsNone(rows[1]["owner_object_id"])
        self.assertEqual(result["flags_emitted"],0)
    def test_duplicates_rejected(self):
        self.write([{"artifact_object_id":1},{"artifact_object_id":1}])
        with self.assertRaisesRegex(ValueError,"duplicate"):tool.resolve(self.source,self.out)
    def test_refuses_existing_output(self):
        self.write([{"artifact_object_id":1}]);self.out.write_text("safe")
        with self.assertRaisesRegex(ValueError,"new"):tool.resolve(self.source,self.out)
        self.assertEqual(self.out.read_text(),"safe")
if __name__=="__main__":unittest.main()
