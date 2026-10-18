import csv,pathlib,sqlite3,sys,tempfile,unittest
from unittest.mock import patch
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import phase9_source_bound_generalization_gate as gate
class SourceBoundTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);d=pathlib.Path(t.name)
  self.db=d/"synthetic.qeax";self.ledger=d/"ledger.csv";self.registry=d/"registry.json"
  self.registry.write_text("{}")
  with sqlite3.connect(self.db) as db:
   db.execute("CREATE TABLE t_connector(Connector_ID INTEGER,Connector_Type TEXT,Stereotype TEXT,Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER)")
   db.execute("INSERT INTO t_connector VALUES(1,'Generalization','','Source -> Destination',11,22)")
  self.row={"source_pk":"1","family":"Generalization","role":"source-subtype-to-destination-supertype","status":"orientation_normalized","normalized_from":"11","normalized_to":"22"}
  self.write()
 def write(self):
  with self.ledger.open("w",newline="") as f:
   w=csv.DictWriter(f,fieldnames=list(self.row));w.writeheader();w.writerow(self.row)
 def run_gate(self,subtype="11",supertype="22"):
  with patch.object(gate,"replay",return_value={"valid":True,"source_count":1,"ledger_count":1}):
   return gate.evaluate(self.db,self.ledger,self.registry,"1",subtype,supertype)
 def test_matching_candidate_review_only(self):
  r=self.run_gate();self.assertTrue(r["eligibleForCanonicalReview"]);self.assertFalse(r["nativeCertified"])
 def test_reversed_ids_rejected(self):
  self.assertIn("SOURCE_ENDPOINT_ORIENTATION_MISMATCH",self.run_gate("22","11")["diagnostics"])
 def test_wrong_role_rejected(self):
  self.row["role"]="unknown";self.write()
  self.assertIn("LEDGER_ROLE_NOT_QUALIFIED",self.run_gate()["diagnostics"])
 def test_unverified_source_direction(self):
  with sqlite3.connect(self.db) as db:db.execute("UPDATE t_connector SET Direction='Unspecified'")
  self.assertIn("SOURCE_DIRECTION_UNVERIFIED",self.run_gate()["diagnostics"])
 def test_full_replay_failure(self):
  with patch.object(gate,"replay",return_value={"valid":False,"source_count":1,"ledger_count":1}):
   self.assertIn("COMPLETE_LEDGER_REPLAY_FAILED",gate.evaluate(self.db,self.ledger,self.registry,"1","11","22")["diagnostics"])
if __name__=="__main__":unittest.main()
