import csv,json,pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_local_ea_generalization_bridge import bridge,digest
class BridgeTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);p=pathlib.Path(t.name)
  self.db=p/"source.qeax";self.ledger=p/"ledger.csv";self.registry=p/"registry.json"
  with sqlite3.connect(self.db) as db:
   db.execute("CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT)")
   db.executemany("INSERT INTO t_object VALUES(?,?,?)",[(1,"Class","block"),(2,"Class","block")])
   db.execute("CREATE TABLE t_connector(Connector_ID INTEGER,ea_guid TEXT,Connector_Type TEXT,Stereotype TEXT,Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER,SourceIsAggregate INTEGER,DestIsAggregate INTEGER,SourceRole TEXT,DestRole TEXT,SourceCard TEXT,DestCard TEXT)")
   db.execute("INSERT INTO t_connector VALUES(1,'synthetic-guid','Generalization','','Source -> Destination',1,2,0,0,'','','','')")
   db.row_factory=sqlite3.Row
   from replay_phase8_local_normalization import mod
   pred=mod.decide(db.execute("SELECT * FROM t_connector").fetchone(),("Class","block"),("Class","block"),set())
  self.registry.write_text('{"families":[]}')
  row={"source_pk":"1","source_guid":"synthetic-guid","raw_from":"1","raw_to":"2","source_direction":"Source -> Destination","source_role":"","target_role":"","source_cardinality":"","target_cardinality":"","source_aggregation_flag":"0","target_aggregation_flag":"0"}
  row.update({k:";".join(v) if isinstance(v,list) else str(v) for k,v in pred.items()})
  with self.ledger.open("w",newline="") as f:
   w=csv.DictWriter(f,fieldnames=list(row));w.writeheader();w.writerow(row)
 def test_complete_synthetic_replay_review_only(self):
  result,rows=bridge(self.db,self.ledger,self.registry)
  self.assertTrue(result["valid"]);self.assertEqual(len(rows),1)
  self.assertEqual(rows[0]["reviewStatus"],"SOURCE_ORIENTATION_ONLY")
  self.assertFalse(rows[0]["nativeCertified"])
 def test_tamper_fails_closed(self):
  s=self.ledger.read_text().replace("synthetic-guid","altered-guid");self.ledger.write_text(s)
  result,rows=bridge(self.db,self.ledger,self.registry)
  self.assertFalse(result["valid"]);self.assertEqual(rows,[])
if __name__=="__main__":unittest.main()
