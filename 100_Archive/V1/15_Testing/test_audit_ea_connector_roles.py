"""Synthetic connector source role evidence tests."""
import pathlib, sqlite3, sys, tempfile, unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from audit_ea_connector_roles import audit

class ConnectorRoles(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db=pathlib.Path(self.tmp.name)/"synthetic.sqlite"
        c=sqlite3.connect(self.db)
        c.execute("""CREATE TABLE t_connector (Connector_ID INTEGER,Connector_Type TEXT,
          Direction TEXT,Start_Object_ID INTEGER,End_Object_ID INTEGER,
          SourceIsAggregate INTEGER,DestIsAggregate INTEGER,
          SourceRole TEXT,DestRole TEXT,SourceCard TEXT,DestCard TEXT)""")
        c.execute("INSERT INTO t_connector VALUES (1,'Aggregation','Source -> Destination',1,2,0,2,'','',NULL,NULL)")
        c.execute("INSERT INTO t_connector VALUES (2,'Generalization','Unspecified',2,2,0,0,NULL,NULL,NULL,NULL)")
        c.commit();c.close()

    def test_composite_end_and_direction(self):
        result=audit(self.db)
        self.assertEqual(result["diagnostics"]["aggregation_composite_dest"],1)
        self.assertEqual(result["diagnostics"]["generalization_direction_unattested"],1)

    def test_missing_roles_not_inferred(self):
        result=audit(self.db)
        self.assertEqual(result["diagnostics"]["aggregation_no_explicit_roles"],1)
        self.assertEqual(result["diagnostics"]["aggregation_no_explicit_cardinality"],1)

    def test_self_reference_cannot_certify_native(self):
        result=audit(self.db)
        self.assertEqual(result["diagnostics"]["self_endpoint"],1)
        self.assertEqual(result["nativeCertified"],0)

    def test_no_source_keys_exposed(self):
        result=audit(self.db)
        self.assertEqual(result["connectors"],2)
        self.assertNotIn("Connector_ID",str(result))

if __name__=="__main__":
    unittest.main()
