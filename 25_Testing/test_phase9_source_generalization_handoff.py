import pathlib,sqlite3,sys,tempfile,unittest
from unittest.mock import patch
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_source_generalization_handoff import audit
class HandoffTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup)
  self.q=pathlib.Path(t.name)/"synthetic.qeax"
  with sqlite3.connect(self.q) as db:
   db.execute("CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT)")
   db.executemany("INSERT INTO t_object VALUES(?,?,?)",[(1,"Class","Hardware Component"),(2,"Class","Hardware Component")])
   db.execute("CREATE TABLE t_connector(Connector_Type TEXT,Stereotype TEXT,Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER)")
   db.execute("INSERT INTO t_connector VALUES('Generalization','','Source -> Destination',1,2)")
 def test_replay_failure_blocks_review(self):
  with patch("phase9_source_generalization_handoff.replay_check",return_value={"valid":False,"source_count":1,"ledger_count":1,"error_counts":{"MISMATCH":1}}):
   r=audit(self.q,"unused","unused")
  self.assertFalse(r["eligible_for_review"]);self.assertEqual(r["native_certified"],0)
 def test_matched_replay_is_still_not_semantic_certification(self):
  with patch("phase9_source_generalization_handoff.replay_check",return_value={"valid":True,"source_count":1,"ledger_count":1,"error_counts":{}}):
   r=audit(self.q,"unused","unused")
  self.assertTrue(r["eligible_for_review"]);self.assertFalse(r["semantic_authorization"])
  self.assertEqual(r["counts"]["same_ea_kind_and_stereotype_review"],1)
  self.assertEqual(r["exported_source_rows"],0)
 def test_count_discrepancy_blocks_review(self):
  with patch("phase9_source_generalization_handoff.replay_check",return_value={"valid":True,"source_count":2,"ledger_count":1,"error_counts":{}}):
   self.assertFalse(audit(self.q,"unused","unused")["eligible_for_review"])
if __name__=="__main__":unittest.main()
