import csv,hashlib,json,pathlib,tempfile,unittest,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from verify_phase8_local_evidence_bundle import verify,digest
class EvidenceTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  root=pathlib.Path(self.tmp.name)
  self.q=root/"source.qeax";self.q.write_bytes(b"synthetic-qeax")
  self.reg=root/"registry.json";self.reg.write_text("{}")
  self.ledger=root/"ledger.csv"
  self.ledger.write_text("source_pk,source_guid,raw_from,raw_to,normalized_from,normalized_to,status,diagnostics\n1,synthetic-guid,10,11,10,11,deferred_review,REVIEW\n")
  self.att=root/"attestation.json"
  self.att.write_text(json.dumps({"schema":"mdse-phase8-input-attestation/1","source_sha256":digest(self.q),"registry_sha256":digest(self.reg),"native_certified":0}))
 def check(self):return verify(self.q,self.ledger,self.reg,self.att)
 def test_synthetic_valid_bundle(self):
  r=self.check();self.assertTrue(r["verified"]);self.assertEqual(r["connector_count"],1);self.assertEqual(r["native_certified"],0)
 def test_modified_qeax_rejected(self):
  self.q.write_bytes(b"modified");self.assertIn("QEAX_HASH_MISMATCH",self.check()["errors"])
 def test_modified_registry_rejected(self):
  self.reg.write_text("changed");self.assertIn("REGISTRY_HASH_MISMATCH",self.check()["errors"])
 def test_duplicate_source_key_rejected(self):
  with self.ledger.open("a") as f:f.write("1,g2,20,21,20,21,deferred_review,REVIEW\n")
  self.assertIn("DUPLICATE_OR_EMPTY_CONNECTOR_KEY",self.check()["errors"])
 def test_missing_required_column_rejected(self):
  self.ledger.write_text("source_pk\n1\n")
  self.assertIn("LEDGER_SCHEMA_MISMATCH",self.check()["errors"])
 def test_certification_forbidden(self):
  v=json.loads(self.att.read_text());v["native_certified"]=1;self.att.write_text(json.dumps(v))
  self.assertIn("NATIVE_CERTIFICATION_FORBIDDEN",self.check()["errors"])
if __name__=="__main__":unittest.main()
