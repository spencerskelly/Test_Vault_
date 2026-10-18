"""Synthetic Phase 8/9 approved-policy integration, zero proprietary rows in Git."""
import csv, importlib.util, json, pathlib, sqlite3, sys, tempfile, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
PHASE8=ROOT/"24_Workbench/registry/runtime/normalize_qeax_phase8.py"
APPROVED=ROOT/"24_Workbench/registry/sysml_v2_approved_family_resolver.v0.1.json"
spec=importlib.util.spec_from_file_location("phase8_approved_integration",PHASE8)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
sys.path.insert(0,str(ROOT/"25_Testing"))
from phase9_source_direction_bridge import audit

class ApprovedPhase8Integration(unittest.TestCase):
 def setUp(self):
  tmp=tempfile.TemporaryDirectory();self.addCleanup(tmp.cleanup)
  self.root=pathlib.Path(tmp.name);self.qeax=self.root/"source.qeax"
  with sqlite3.connect(self.qeax) as db:
   db.execute("CREATE TABLE t_object (Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT)")
   db.executemany("INSERT INTO t_object VALUES(?,?,?)",[
    (1,"Class","block"),(2,"Class","Hardware Component"),(3,"Object",""),
    (4,"InformationItem",""),(5,"Part",""),(6,"Class","new-unapproved"),
    (7,"Requirement","")])
   db.execute("""CREATE TABLE t_connector (
    Connector_ID INTEGER,ea_guid TEXT,Connector_Type TEXT,Stereotype TEXT,
    Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER,
    SourceIsAggregate INTEGER,DestIsAggregate INTEGER,SourceRole TEXT,
    DestRole TEXT,SourceCard TEXT,DestCard TEXT)""")
   db.executemany("INSERT INTO t_connector VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",[
    (11,"gen","Generalization","","Source -> Destination",1,2,0,0,"","","",""),
    (12,"shared","Aggregation","","Source -> Destination",2,5,1,0,"whole","part","1","0..*"),
    (13,"info","Dependency","","Source -> Destination",3,4,0,0,"","","",""),
    (14,"note","NoteLink","","Unspecified",3,4,0,0,"","","",""),
    (15,"derive","Realisation","deriveReqt","Source -> Destination",7,7,0,0,"","","",""),
    (16,"seq","Sequence","","Source -> Destination",1,2,0,0,"","","",""),
    (17,"unknown","Mystery","","Source -> Destination",1,2,0,0,"","","",""),
    (18,"endpoint","Dependency","","Source -> Destination",6,2,0,0,"","","","")])
 def test_row_level_policy_and_raw_evidence(self):
  out=self.root/"results"
  summary=mod.reconcile_atomic(self.qeax,APPROVED,out)
  self.assertEqual(summary["total"],8)
  self.assertEqual(summary["policy_mode"],"approved_exact_groups")
  self.assertEqual(summary["approved_family_count"],26)
  self.assertEqual(summary["unmatched_connector_rows"],1)
  self.assertEqual(summary["unmatched_endpoint_rows"],1)
  self.assertEqual(summary["native_certified"],0)
  self.assertFalse(summary["native_emission_authorized"])
  self.assertEqual(summary["ea_diagrams_processed"],0)
  with (out/"local_only_phase8_ledger.csv").open(newline="") as f:
   rows={r["source_pk"]:r for r in csv.DictReader(f)}
  self.assertEqual(len(rows),8)
  self.assertEqual(rows["11"]["source_kind"],"PartDefinition")
  self.assertEqual(rows["12"]["source_kind"],"PartDefinition")
  self.assertEqual(rows["12"]["target_kind"],"PartUsage")
  self.assertNotIn("SHARED_NOT_COMPOSITE",rows["12"]["diagnostics"])
  self.assertIn("AGGREGATION_OWNERSHIP_AND_USAGE_REVIEW",rows["12"]["diagnostics"])
  self.assertEqual(rows["12"]["source_aggregation_flag"],"1")
  self.assertEqual(rows["12"]["source_role"],"whole")
  self.assertEqual(rows["12"]["target_cardinality"],"0..*")
  self.assertEqual(rows["13"]["source_kind"],"PartDefinition")
  self.assertEqual(rows["13"]["target_kind"],"")
  self.assertIn("TARGET_NON_NATIVE_MODEL_ELEMENT",rows["13"]["diagnostics"])
  self.assertEqual(rows["14"]["status"],"evidence_only")
  self.assertEqual(rows["15"]["rule"],"RequirementDerivation")
  self.assertEqual(rows["16"]["status"],"evidence_only")
  self.assertIn("EA_DIAGRAMS_OUT_OF_SCOPE",rows["16"]["diagnostics"])
  self.assertIn("CONNECTOR_FAMILY_OUTLIER",rows["17"]["diagnostics"])
  self.assertIn("SOURCE_FAMILY_OUTLIER",rows["18"]["diagnostics"])
  p9=audit(self.qeax,out/"local_only_phase8_ledger.csv")
  self.assertTrue(p9["valid"],p9["errors"])
  self.assertEqual(p9["categories"]["approved_group_orientation_review"],1)
  self.assertFalse(p9["may_emit_native"])
  with self.assertRaisesRegex(ValueError,"OUTPUT_ALREADY_EXISTS"):
   mod.reconcile_atomic(self.qeax,APPROVED,out)
 def test_no_diagram_dependency(self):
  baseline=mod.reconcile(self.qeax,APPROVED,self.root/"clean")
  with sqlite3.connect(self.qeax) as db:
   db.execute("CREATE TABLE t_diagram (Diagram_ID INTEGER)")
   db.execute("CREATE TABLE t_diagramobjects (Diagram_ID INTEGER)")
   db.execute("INSERT INTO t_diagram VALUES (555)")
  again=mod.reconcile(self.qeax,APPROVED,self.root/"with_diag")
  self.assertEqual(again,baseline)
 def test_unknown_registry_rejected_and_legacy_fixture_unchanged(self):
  broken=self.root/"bad.json";broken.write_text('{"schema":"unsupported"}')
  with self.assertRaisesRegex(ValueError,"UNSUPPORTED_PHASE8_REGISTRY_SCHEMA"):
   mod.reconcile(self.qeax,broken,self.root/"bad_output")
  old=self.root/"historical.json";old.write_text(json.dumps({"families":[]}))
  old_result=mod.reconcile(self.qeax,old,self.root/"historical")
  self.assertEqual(old_result["total"],8)
  self.assertNotIn("policy_mode",old_result)

if __name__=="__main__":unittest.main()
