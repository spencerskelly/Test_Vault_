"""Synthetic private ledger fidelity audit tests."""
import csv,pathlib,sqlite3,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from verify_phase8_private_ledger import audit
class Fidelity(unittest.TestCase):
 def setUp(self):
  temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup)
  root=pathlib.Path(temp.name);self.db=root/"fixture.sqlite";self.csv=root/"ledger.csv"
  c=sqlite3.connect(self.db)
  c.execute("CREATE TABLE t_object (Object_ID INTEGER,Object_Type TEXT,Stereotype TEXT)")
  c.execute("""CREATE TABLE t_connector (Connector_ID INTEGER,ea_guid TEXT,
   Start_Object_ID INTEGER,End_Object_ID INTEGER,Direction TEXT,
   SourceRole TEXT,DestRole TEXT,SourceCard TEXT,DestCard TEXT,
   SourceIsAggregate INTEGER,DestIsAggregate INTEGER)""")
  c.executemany("INSERT INTO t_object VALUES (?,?,?)",[(1,"Class","block"),(2,"Class","Module")])
  c.execute("INSERT INTO t_connector VALUES (3,'fake-guid',1,2,'Source -> Destination',NULL,NULL,'1','*',0,2)")
  c.commit();c.close()
  self.row=dict(source_pk="3",source_guid="fake-guid",raw_from="1",raw_to="2",
    source_direction="Source -> Destination",source_role="",target_role="",
    source_cardinality="1",target_cardinality="*",source_aggregation_flag="0",
    target_aggregation_flag="2",raw_source_type="Class",
    raw_source_stereotype="block",raw_target_type="Class",
    raw_target_stereotype="Module",status="owner_endpoint_identified")
 def write(self,rows):
  with self.csv.open("w",newline="") as f:
   writer=csv.DictWriter(f,fieldnames=self.row);writer.writeheader();writer.writerows(rows)
 def test_exact_rows(self):
  self.write([self.row]);self.assertEqual(audit(self.db,self.csv)["status"],"PASS")
 def test_changed_direction_fails(self):
  self.row["source_direction"]="Unspecified";self.write([self.row])
  self.assertEqual(audit(self.db,self.csv)["rawMismatches"],1)
 def test_duplicate_fails(self):
  self.write([self.row,self.row])
  self.assertEqual(audit(self.db,self.csv)["duplicateIds"],1)
 def test_missing_fails(self):
  self.write([]);self.assertEqual(audit(self.db,self.csv)["missingIds"],1)
if __name__=="__main__":unittest.main()
