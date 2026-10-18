"""Synthetic regression for end-role and port evidence."""
import importlib.util,pathlib,sqlite3,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("evidence",ROOT/"21_Importer/v2_connector_end_evidence.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class EvidenceTest(unittest.TestCase):
 def test_end_evidence(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/"sample.qeax"
   with sqlite3.connect(p) as db:
    db.execute("CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT,Classifier INTEGER,Classifier_guid TEXT,Multiplicity TEXT)")
    db.execute("CREATE TABLE t_connector(Connector_ID INTEGER,Connector_Type TEXT,Stereotype TEXT,Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER,SourceRole TEXT,DestRole TEXT,SourceCard TEXT,DestCard TEXT,SourceContainment TEXT,DestContainment TEXT,SourceIsAggregate INTEGER,DestIsAggregate INTEGER,SourceRoleType TEXT,DestRoleType TEXT)")
    db.executemany("INSERT INTO t_object VALUES(?,?,?,?,?,?)",[(1,"Class","block",0,None,None),(2,"Port",None,42,None,"0..1")])
    db.executemany("INSERT INTO t_connector VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",[
     (1,"Aggregation","","Source -> Destination",1,2,None,"part","1","0..*","Unspecified","Unspecified",0,2,None,None),
     (2,"Association","",None,1,99,None,None,None,None,None,None,0,0,None,None)])
   before=p.read_bytes();result=m.audit(p)
   self.assertEqual(result["selected_connectors"],2)
   for key in ("missing_endpoint","destination_aggregation_indicator_present","port_classifier_reference_present","port_stereotype_missing"):
    self.assertEqual(result["evidence_counts"][key],1)
   self.assertEqual(result["native_relationships_emitted"],0)
   self.assertEqual(before,p.read_bytes())
   with self.assertRaisesRegex(ValueError,"INVALID_LIMIT"):m.audit(p,0)
if __name__=="__main__":unittest.main()
