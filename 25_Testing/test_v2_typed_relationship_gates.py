import importlib.util,json,pathlib,sqlite3,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("gates",ROOT/"21_Importer/v2_typed_relationship_gates.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class GatesTest(unittest.TestCase):
 def test_evidence(self):
  with tempfile.TemporaryDirectory() as d:
   root=pathlib.Path(d);dbpath=root/"test.qeax";reg=root/"rules.json"
   reg.write_text(json.dumps({"automaticNativeEmission":False,"relationshipRules":[
    {"family":x,"emission":"deferred_pending_evidence_and_parser"} for x in
    ("Generalization:","Aggregation:","Dependency:verify","Dependency:deriveReqt","Dependency:satisfy")]}))
   with sqlite3.connect(dbpath) as db:
    db.execute("CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT)")
    db.execute("CREATE TABLE t_connector(Connector_ID INTEGER,Connector_Type TEXT,Stereotype TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER)")
    db.executemany("INSERT INTO t_object VALUES(?,?,?)",[(1,"Requirement",""),(2,"Activity","testCase")])
    db.executemany("INSERT INTO t_connector VALUES(?,?,?,?,?)",[(1,"Dependency","verify",2,1),(2,"Dependency","deriveReqt",2,1),(3,"Generalization","",2,1),(4,"Aggregation","",1,2),(5,"Dependency","other",1,2),(6,"Dependency","satisfy",1,99)])
   before=dbpath.read_bytes();out=m.assess(dbpath,reg)
   self.assertEqual(out["reviewed"],6)
   self.assertEqual(out["gates"]["verify_roles_unverified"],1)
   self.assertEqual(out["gates"]["invalid_derivation_endpoints"],1)
   self.assertEqual(out["gates"]["direction_unverified"],1)
   self.assertEqual(out["gates"]["ownership_and_multiplicity_unverified"],1)
   self.assertEqual(out["gates"]["unmatched_family"],1)
   self.assertEqual(out["gates"]["missing_endpoint"],1)
   self.assertEqual(out["native_emission"],0)
   self.assertEqual(dbpath.read_bytes(),before)
   with self.assertRaisesRegex(ValueError,"INVALID_LIMIT"):m.assess(dbpath,reg,0)
if __name__=="__main__":unittest.main()
