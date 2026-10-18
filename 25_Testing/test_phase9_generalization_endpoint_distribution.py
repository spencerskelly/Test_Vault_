import pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_generalization_endpoint_distribution import distribution
class DistributionTests(unittest.TestCase):
 def setUp(self):
  d=tempfile.TemporaryDirectory();self.addCleanup(d.cleanup);self.path=pathlib.Path(d.name)/"synthetic.qeax"
  with sqlite3.connect(self.path) as db:
   db.execute("CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT)")
   db.executemany("INSERT INTO t_object VALUES(?,?,?)",[(1,"Class","block"),(2,"Class","block"),(3,"Class","Hardware Component"),(4,"Class","Hardware Component"),(5,"Activity",""),(6,"Activity","")])
   db.execute("CREATE TABLE t_connector(Connector_Type TEXT,Stereotype TEXT,Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER)")
   db.executemany("INSERT INTO t_connector VALUES(?,?,?,?,?)",[("Generalization","","Source -> Destination",1,2),("Generalization","","Source -> Destination",3,4),("Generalization","","Source -> Destination",5,6),("Generalization","","Source -> Destination",3,4)])
 def test_only_review_rows(self):
  r=distribution(self.path);self.assertEqual(r["review_count"],2)
  self.assertEqual(r["type_pairs"][0]["count"],2)
  self.assertEqual(r["native_certified"],0)
 def test_no_identity_leak(self):
  r=distribution(self.path);self.assertNotIn("Object_ID",str(r));self.assertNotIn("connector_id",str(r).lower())
 def test_directed_counts(self):
  self.assertEqual(distribution(self.path)["directions"],{"Source -> Destination":2})
if __name__=="__main__":unittest.main()
