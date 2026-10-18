import pathlib,sqlite3,tempfile,unittest
from phase9_nested_relationship_context import analyze
class NestedContextTests(unittest.TestCase):
 def build(self,nested):
  temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup)
  path=pathlib.Path(temp.name)/'synthetic.qeax'
  with sqlite3.connect(path) as db:
   db.execute('CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT,ParentID INTEGER)')
   db.executemany('INSERT INTO t_object VALUES(?,?,?,?)',[(1,'Class','Hardware Component',2 if nested else 0),(2,'Class','Hardware Component',0),(3,'Class','Hardware Component',0)])
   db.execute('CREATE TABLE t_connector(Connector_Type TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER)')
   db.executemany('INSERT INTO t_connector VALUES(?,?,?)',[('Generalization',1,2),('Generalization',1,3),('Abstraction',3,1)])
  return analyze(path)
 def test_nesting_does_not_consume_generalization(self):
  r=self.build(True)
  self.assertEqual(r['counts']['unique_nested_elements'],1)
  self.assertEqual(r['counts']['incident_connector_appearances'],3)
  counts={(e['type'],e['relationship_to_parent']):e['count'] for e in r['connector_categories']}
  self.assertEqual(counts['Generalization','nested_to_parent'],1)
  self.assertEqual(counts['Generalization','other'],1)
  self.assertEqual(r['native_certified'],0)
 def test_no_nested_endpoint(self):
  r=self.build(False)
  self.assertEqual(r['counts']['unique_nested_elements'],0)
  self.assertEqual(r['connector_categories'],[])
if __name__=='__main__':unittest.main()
