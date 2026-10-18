import unittest,tempfile,sqlite3,pathlib
from reconcile_qeax import classify,disposition,run
class Tests(unittest.TestCase):
 def test_definition(self):self.assertEqual(classify(('Class','block')),'PartDefinition')
 def test_unknown_type(self):self.assertIsNone(classify(('Mystery','')))
 def test_trace(self):self.assertEqual(disposition(('Dependency','trace','Source -> Destination',0,0,'',''),('Class','block'),('Class','block'))[0],'deferred_review')
 def test_dependency_candidate(self):self.assertEqual(disposition(('Dependency','','Source -> Destination',0,0,'',''),('Class','block'),('Class','block'))[0],'candidate_only')
 def test_reject_unknown_family(self):self.assertEqual(disposition(('Mystery','','Source -> Destination',0,0,'',''),('Class','block'),('Class','block'))[0],'deferred_review')
 def test_synthetic_db(self):
  with tempfile.TemporaryDirectory() as td:
   p=pathlib.Path(td)/'test.qeax';c=sqlite3.connect(p)
   c.executescript('CREATE TABLE t_object(Object_ID integer,Object_Type text,Stereotype text);CREATE TABLE t_connector(Connector_ID integer,ea_guid text,Connector_Type text,Stereotype text,Direction text,Start_Object_ID integer,End_Object_ID integer,SourceIsAggregate integer,DestIsAggregate integer,SourceCard text,DestCard text);')
   c.executemany('insert into t_object values(?,?,?)',[(1,'Class','block'),(2,'Class','block')]);c.execute("insert into t_connector values(1,'synthetic','Dependency','','Source -> Destination',1,2,0,0,'','')");c.commit();c.close()
   result=run(p,pathlib.Path(td)/'out');self.assertEqual(result['connector_count'],1);self.assertEqual(result['dispositions']['candidate_only'],1)
if __name__=='__main__':unittest.main()
