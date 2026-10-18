import pathlib,sqlite3,tempfile,unittest,sys
from unittest.mock import patch
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import phase9_local_specialization_evidence_gate as gate
class LocalGateTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);p=pathlib.Path(t.name)
  self.db=p/"synthetic.qeax";self.ledger=p/"ledger.csv";self.reg=p/"registry.json";self.reg.write_text("{}")
  with sqlite3.connect(self.db) as d:
   d.execute("CREATE TABLE t_connector(Connector_ID INTEGER,Connector_Type TEXT,Stereotype TEXT,Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER)")
   d.executemany("INSERT INTO t_connector VALUES(?,?,?,?,?,?)",[(1,"Generalization","","Source -> Destination",10,20),(2,"Generalization","","Unspecified",10,20)])
   d.execute("CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT)")
   d.executemany("INSERT INTO t_object VALUES(?,?,?)",[(10,"Class","Hardware Component"),(20,"Class","Hardware Component")])
  self.ledger.write_text("source_pk,normalized_from,normalized_to\n1,10,20\n2,10,20\n")
 def run_gate(self,ids,valid=True):
  with patch.object(gate,"replay",return_value={"valid":valid,"source_count":2,"ledger_count":2}):
   return gate.qualify(self.db,self.ledger,self.reg,ids)
 def test_source_direction_candidate_not_certified(self):
  r=self.run_gate(["1"]);self.assertEqual(r["qualified"],1);self.assertFalse(r["semantic_approved"]);self.assertEqual(r["native_certified"],0)
 def test_unverified_direction_fails(self):
  self.assertIn("DIRECTION_NOT_EXPLICIT",self.run_gate(["2"])["errors"])
 def test_missing_id_fails(self):
  self.assertIn("MISSING_SOURCE_CONNECTOR",self.run_gate(["3"])["errors"])
 def test_duplicate_request_fails_closed(self):
  self.assertEqual(self.run_gate(["1","1"])["qualified"],0)
 def test_failed_replay_fails_closed(self):
  self.assertIn("FULL_REPLAY_FAILED",self.run_gate(["1"],False)["errors"])
 def test_changed_ledger_direction(self):
  self.ledger.write_text("source_pk,normalized_from,normalized_to\n1,20,10\n")
  self.assertIn("LEDGER_DIRECTION_MISMATCH",self.run_gate(["1"])["errors"])
if __name__=="__main__":unittest.main()
