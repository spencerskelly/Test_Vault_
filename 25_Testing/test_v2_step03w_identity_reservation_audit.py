import importlib.util,json,tempfile,unittest
from pathlib import Path

P=Path(__file__).resolve().parents[1]/"21_Importer"/"v2_step03w_identity_reservation_audit.py"
spec=importlib.util.spec_from_file_location("reservation_audit",P)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class ReservationAuditTests(unittest.TestCase):
    def setUp(self):
        tmp=tempfile.TemporaryDirectory();self.addCleanup(tmp.cleanup)
        self.root=Path(tmp.name);self.vault=self.root/"vault";self.vault.mkdir()
        self.ledger=self.root/"uid.jsonl";self.cross=self.root/"cross.jsonl";self.output=self.root/"out.jsonl"
        self.uid="20261001123456000skellyspencer"
        self.ledger.write_text(json.dumps({"eaObjectID":1,"eaGUID":"A","uid":self.uid})+"\n")
        self.cross.write_text(json.dumps({"eaObjectID":1,"eaGUID":"A"})+"\n")
    def test_unreserved(self):
        result=m.audit(self.ledger,self.cross,self.vault,self.output)
        self.assertEqual(result["statuses"]["uid_candidate_available"],1)
        self.assertIsNone(json.loads(self.output.read_text())["proposedFilename"])
    def test_existing_note_reserves_uid(self):
        (self.vault/"existing.md").write_text("---\nuid: "+self.uid+"\n---\n")
        result=m.audit(self.ledger,self.cross,self.vault,self.output)
        self.assertEqual(result["statuses"]["uid_collision_review"],1)
    def test_local_model_token_reserves_uid(self):
        (self.vault/"existing.md").write_text("local part-20261001123456000skellyspencer")
        result=m.audit(self.ledger,self.cross,self.vault,self.output)
        self.assertEqual(result["statuses"]["uid_collision_review"],1)
    def test_refuse_overwrite(self):
        self.output.write_text("safe")
        with self.assertRaisesRegex(ValueError,"exists"):
            m.audit(self.ledger,self.cross,self.vault,self.output)
        self.assertEqual(self.output.read_text(),"safe")
if __name__=="__main__":unittest.main()
