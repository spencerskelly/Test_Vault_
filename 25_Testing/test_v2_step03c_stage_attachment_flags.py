"""STEP-03C synthetic regression tests: no private QEAX data."""
import json
import tempfile
import unittest
from pathlib import Path
from v2_step03c_stage_attachment_flags import patch

class AttachmentFlagTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.nodes, self.flags, self.out = [root / s for s in ("nodes.jsonl", "flags.jsonl", "out.jsonl")]
        self.write(self.nodes, [{"id":"a","source":"preserved"},{"id":"b","flagNote":["old"]}])
    def write(self, path, records):
        path.write_text("".join(json.dumps(r)+"\n" for r in records),encoding="utf-8")
    def test_complete_and_idempotent(self):
        self.write(self.flags,[{"node_id":"a","flagNote":["review"]}])
        self.assertEqual(patch(self.nodes,self.flags,self.out)["matched"],1)
        first=self.out.read_bytes()
        self.assertEqual(json.loads(first.splitlines()[0])["source"],"preserved")
        second=self.out.with_name("second.jsonl")
        patch(self.out,self.flags,second)
        self.assertEqual(first,second.read_bytes())
    def test_missing_identity_rejected(self):
        self.write(self.flags,[{"node_id":"missing","flagNote":["review"]}])
        with self.assertRaisesRegex(ValueError,"Unmatched"): patch(self.nodes,self.flags,self.out)
        self.assertFalse(self.out.exists())
    def test_duplicate_flags_rejected(self):
        self.write(self.flags,[{"node_id":"a","flagNote":["1"]},{"node_id":"a","flagNote":["2"]}])
        with self.assertRaisesRegex(ValueError,"duplicate"): patch(self.nodes,self.flags,self.out)
    def test_conflict_rejected(self):
        self.write(self.flags,[{"node_id":"b","flagNote":["new"]}])
        with self.assertRaisesRegex(ValueError,"Conflicting"): patch(self.nodes,self.flags,self.out)
    def test_duplicate_nodes_rejected(self):
        self.write(self.nodes,[{"id":"a"},{"id":"a"}])
        self.write(self.flags,[{"node_id":"a","flagNote":["review"]}])
        with self.assertRaisesRegex(ValueError,"duplicate"): patch(self.nodes,self.flags,self.out)

if __name__=="__main__": unittest.main()
