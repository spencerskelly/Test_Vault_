import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

path = Path(__file__).with_name("v2_step03b_graph_flag_gate.py")
spec = importlib.util.spec_from_file_location("graph_gate", path)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

class ExplicitFlagParityTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.nodes = self.root / "nodes.jsonl"
        self.edges = self.root / "edges.jsonl"
        self.nodes.write_text(json.dumps({"id":"1","flagNote":[{"reason":"a"}]})+"\n")
    def write_edges(self, records):
        self.edges.write_text("".join(json.dumps(x)+"\n" for x in records))
    def test_explicit_flaglink_list(self):
        self.write_edges([{"id":"2","source":"1","target":"1","flagLink":[{"reason":"first"},{"reason":"second"}]}])
        self.assertEqual(gate.audit(self.nodes,self.edges,1,2)["flagLinks"],2)
    def test_legacy_flaglink(self):
        self.write_edges([{"id":"2","source":"1","target":"1","disposition":"review"}])
        self.assertEqual(gate.audit(self.nodes,self.edges,1,1)["flagLinks"],1)
    def test_explicit_and_legacy_not_double_counted(self):
        self.write_edges([{"id":"2","source":"1","target":"1","flagLink":[{"reason":"a"}],"disposition":"review"}])
        self.assertEqual(gate.audit(self.nodes,self.edges,1,1)["flagLinks"],1)
    def test_missing_expected_link_fails(self):
        self.write_edges([{"id":"2","source":"1","target":"1"}])
        with self.assertRaisesRegex(ValueError,"flagLink export loss"):
            gate.audit(self.nodes,self.edges,1,1)
    def test_broken_endpoint_fails(self):
        self.write_edges([{"id":"2","source":"1","target":"99","flagLink":[{"reason":"a"}]}])
        with self.assertRaisesRegex(ValueError,"Broken endpoint"):
            gate.audit(self.nodes,self.edges,1,1)

if __name__ == "__main__":
    unittest.main()
