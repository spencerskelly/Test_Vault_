"""Run exact Phase 8 normalizer on synthetic SQLite and check raw evidence."""
import csv,importlib.util,json,pathlib,sqlite3,tempfile,unittest
TARGET=pathlib.Path(__file__).resolve().parents[1]/"14_Workbench/registry/runtime/normalize_qeax_phase8.py"
SPEC=importlib.util.spec_from_file_location("normalize_qeax_phase8",TARGET)
MOD=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(MOD)

class E2E(unittest.TestCase):
 def test_original_values_retained(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);db=root/"synthetic.sqlite"
   c=sqlite3.connect(db)
   c.execute("CREATE TABLE t_object (Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT)")
   c.execute("""CREATE TABLE t_connector (
    Connector_ID INTEGER,ea_guid TEXT,Connector_Type TEXT,Stereotype TEXT,
    Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER,
    SourceIsAggregate INTEGER,DestIsAggregate INTEGER,
    SourceRole TEXT,DestRole TEXT,SourceCard TEXT,DestCard TEXT)""")
   c.executemany("INSERT INTO t_object VALUES (?,?,?)",
       [(1,"Class","block"),(2,"Class","Hardware Component")])
   c.execute("INSERT INTO t_connector VALUES (5,'fixture-guid','Aggregation','','Source -> Destination',1,2,0,2,'original-source-role','original-dest-role','1','0..*')")
   c.commit();c.close()
   registry=root/"registry.json";registry.write_text(json.dumps({"families":[]}))
   out=root/"out";result=MOD.reconcile(db,registry,out)
   self.assertEqual(result["total"],1)
   self.assertEqual(result["native_certified"],0)
   with (out/"local_only_phase8_ledger.csv").open(newline="") as fd:
    rows=list(csv.DictReader(fd))
   self.assertEqual(len(rows),1)
   row=rows[0]
   self.assertEqual(row["source_role"],"original-source-role")
   self.assertEqual(row["target_role"],"original-dest-role")
   self.assertEqual(row["source_cardinality"],"1")
   self.assertEqual(row["target_cardinality"],"0..*")
   self.assertEqual(row["source_direction"],"Source -> Destination")
   self.assertEqual(row["raw_target_stereotype"],"Hardware Component")
   self.assertEqual(row["source_aggregation_flag"],"0")
   self.assertEqual(row["target_aggregation_flag"],"2")
   self.assertEqual(row["raw_from"],"1")
   self.assertEqual(row["raw_to"],"2")
if __name__=="__main__":unittest.main()
