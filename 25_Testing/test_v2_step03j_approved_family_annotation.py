import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT=Path(__file__).with_name("v2_step03j_approved_family_annotation.py")
spec=importlib.util.spec_from_file_location("annotation_under_test",SCRIPT)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
ROOT=SCRIPT.parents[1]

class FamilyAnnotationTests(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup)
        self.root=Path(self.t.name);self.nodes=self.root/"nodes.jsonl";self.edges=self.root/"edges.jsonl"
        self.out=self.root/"out"
        self.node={"id":"1","eaGUID":"{a}","source":{"table":"t_object","row":{"Object_Type":"UnrecognizedSyntheticType","Stereotype":"","Notes":"retain"}}}
        self.edge={"id":"2","source":"1","target":"1","sourceData":{"table":"t_connector","row":{"Connector_Type":"UnrecognizedSyntheticLink","Stereotype":"","Notes":"retain link"}}}
    def write(self,nodes=None,edges=None):
        self.nodes.write_text("".join(json.dumps(x)+"\n" for x in (nodes if nodes is not None else [self.node])))
        self.edges.write_text("".join(json.dumps(x)+"\n" for x in (edges if edges is not None else [self.edge])))
    def test_outliers_flagged_and_payload_retained(self):
        self.write()
        counts=module.annotate(self.nodes,self.edges,self.out,ROOT)
        self.assertEqual((counts["nodes"],counts["edges"],counts["flagNote"],counts["flagLink"]),(1,1,1,1))
        n=json.loads((self.out/"nodes.jsonl").read_text().strip())
        e=json.loads((self.out/"edges.jsonl").read_text().strip())
        self.assertEqual(n["source"]["row"]["Notes"],"retain")
        self.assertEqual(e["sourceData"]["row"]["Notes"],"retain link")
        self.assertFalse(n["approvedFamilyReview"]["emission_authorized"])
        self.assertFalse(e["approvedFamilyReview"]["emission_authorized"])
    def test_output_not_overwritten(self):
        self.write();self.out.mkdir();(self.out/"keep").write_text("safe")
        with self.assertRaisesRegex(ValueError,"not empty"):module.annotate(self.nodes,self.edges,self.out,ROOT)
    def test_no_diagram_input_or_native_text(self):
        self.write()
        module.annotate(self.nodes,self.edges,self.out,ROOT)
        self.assertFalse(any(p.name.endswith(".sysml") for p in self.out.iterdir()))
        self.assertEqual(set(p.name for p in self.out.iterdir()),{"nodes.jsonl","edges.jsonl","annotation_summary.json"})

if __name__=="__main__":unittest.main()
