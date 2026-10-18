"""Candidate projection semantics and fail-closed native emission tests."""
import importlib.util,json,pathlib,sqlite3,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("v2_projection",ROOT/"21_Importer/project_v2_element_candidates.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class CandidateProjectionTest(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.q=pathlib.Path(self.tmp.name)/"fixture.qeax"
  with sqlite3.connect(self.q) as db:
   db.execute("CREATE TABLE t_object(Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT)")
   db.executemany("INSERT INTO t_object VALUES(?,?,?)",[(2,"Class","block"),(3,"Port","proxy"),(4,"Port","full"),(5,"Unknown","")])
  self.registry=pathlib.Path(self.tmp.name)/"rules.json"
  self.registry.write_text(json.dumps({"schema":"mdse-v2-semantic-rules/0.2","automaticNativeEmission":False,"elementRules":[
   {"eaType":"Class","stereotype":"block","target":"PartDefinition","emission":"deferred_pending_parser"},
   {"eaType":"Port","stereotype":"proxy","target":"PortUsage","emission":"deferred_pending_parser"},
   {"eaType":"Port","stereotype":"full","target":"PartUsage","emission":"deferred_pending_parser"}]}))
 def test_distinctions_and_deferred(self):
  result=m.project(self.q,4,self.registry)
  self.assertEqual(result["candidate_targets"],{"review:PartDefinition":1,"review:PartUsage":1,"review:PortUsage":1,"review:UNMATCHED":1})
  self.assertEqual(result["native_declarations_emitted"],0)
 def test_unsafe_registry_rejected(self):
  raw=json.loads(self.registry.read_text());raw["automaticNativeEmission"]=True
  self.registry.write_text(json.dumps(raw))
  with self.assertRaisesRegex(ValueError,"INVALID_OR_UNSAFE_REGISTRY"):m.project(self.q,4,self.registry)
 def test_invalid_limit(self):
  with self.assertRaisesRegex(ValueError,"INVALID_LIMIT"):m.project(self.q,0,self.registry)
if __name__=="__main__":unittest.main()
