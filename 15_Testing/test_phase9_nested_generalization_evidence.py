import pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_nested_generalization_evidence import audit
class NestedTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);self.db=pathlib.Path(t.name)/"synthetic.qeax"
  with sqlite3.connect(self.db) as db:
   db.execute("CREATE TABLE t_object(Object_ID INTEGER,ea_guid TEXT,Object_Type TEXT,Stereotype TEXT,ParentID INTEGER,Classifier INTEGER,Classifier_guid TEXT)")
   db.executemany("INSERT INTO t_object VALUES(?,?,?,?,?,?,?)",[(1,"a","Class","Hardware Component",3,0,""),(2,"b","Class","Hardware Component",0,0,""),(3,"c","Class","Module",0,0,"")])
   db.execute("CREATE TABLE t_connector(Connector_Type TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER)")
   db.executemany("INSERT INTO t_connector VALUES(?,?,?)",[("Generalization",1,2),("Generalization",1,2)])
   db.execute("CREATE TABLE t_xref(Client TEXT,Type TEXT,Name TEXT)")
 def test_apparances_vs_distinct(self):
  c=audit(self.db)["counts"]
  self.assertEqual(c["source_nested_appearances"],2)
  self.assertEqual(c["unique_nested_endpoint_elements"],1)
 def test_parent_type_aggregate(self):
  v=audit(self.db)
  self.assertEqual(v["parent_type_stereotype_counts"][0]["parent_stereotype"],"Module")
 def test_no_certification(self):self.assertEqual(audit(self.db)["native_certified"],0)
if __name__=="__main__":unittest.main()
