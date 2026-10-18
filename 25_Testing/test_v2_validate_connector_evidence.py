import importlib.util,pathlib,sqlite3,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("validity",ROOT/"21_Importer/v2_validate_connector_evidence.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class EvidenceValidityTests(unittest.TestCase):
 def test_multiplicity(self):
  for x in ("1","0..*","1..3","*"):self.assertEqual(m.multiplicity(x),"valid")
  for x in ("2..1","-1","1..x","01","2.."):self.assertEqual(m.multiplicity(x),"invalid")
  self.assertEqual(m.multiplicity(None),"absent")
 def test_fixture(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/"sample.qeax"
   with sqlite3.connect(p) as db:
    db.execute("CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT,Classifier INTEGER,Classifier_guid TEXT)")
    db.execute("CREATE TABLE t_connector(Connector_ID INTEGER,Connector_Type TEXT,SourceCard TEXT,DestCard TEXT,SourceIsAggregate INTEGER,DestIsAggregate INTEGER,Start_Object_ID INTEGER,End_Object_ID INTEGER)")
    db.executemany("INSERT INTO t_object VALUES(?,?,?,?,?)",[(1,"Class","block",0,None),(2,"Port",None,0,None)])
    db.execute("INSERT INTO t_connector VALUES(1,'Aggregation','2..1','1..*',0,2,1,2)")
   before=p.read_bytes();r=m.audit(p)
   self.assertEqual(r["counts"]["multiplicity_source_invalid"],1)
   self.assertEqual(r["counts"]["aggregation_single_end_flag_2"],1)
   self.assertEqual(r["counts"]["port_classifier_absent"],1)
   self.assertEqual(before,p.read_bytes())
if __name__=="__main__":unittest.main()
