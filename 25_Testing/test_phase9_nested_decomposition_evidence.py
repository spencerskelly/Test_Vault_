import pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_nested_decomposition_evidence import audit
class NestedDecompositionTests(unittest.TestCase):
 def test_parent_generalization_not_aggregation(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);p=pathlib.Path(t.name)/"fixture.qeax"
  with sqlite3.connect(p) as db:
   db.execute("CREATE TABLE t_object(Object_ID INTEGER,ParentID INTEGER,Object_Type TEXT,Stereotype TEXT,Classifier INTEGER)")
   db.executemany("INSERT INTO t_object VALUES(?,?,?,?,?)",[(1,2,"Class","Hardware Component",0),(2,0,"Class","Hardware Component",0),(3,0,"Class","Hardware Component",0)])
   db.execute("CREATE TABLE t_connector(Connector_Type TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER)")
   db.executemany("INSERT INTO t_connector VALUES(?,?,?)",[("Generalization",1,2),("Generalization",1,3),("Abstraction",3,1)])
  r=audit(p);c=r["counts"]
  self.assertEqual(c["nested_elements"],1)
  self.assertEqual(c["generalization_to_parent"],1)
  self.assertEqual(c["generalization_other"],1)
  self.assertEqual(c.get("incident_aggregation",0),0)
  self.assertEqual(c.get("nested_with_children",0),0)
  self.assertEqual(r["native_certified"],0)
if __name__=="__main__":unittest.main()
