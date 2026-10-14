"""IMP-011 v2 regression suite: each test invokes the v2 check, never v1."""
import unittest
from test_imp011_topology_synthetic import Imp011TopologySynthetic, A, B, C
from imp011_topology_acceptance_v2 import check

class Step115V2(unittest.TestCase):
    def setUp(self):
        # Reuse only fixtures; never inherit v1 test methods.
        self.addCleanup(lambda: self.fixture.doCleanups())
        self.fixture = Imp011TopologySynthetic(methodName="test_valid_equals")
        self.fixture.setUp()
        self.root = self.fixture.root
        self.rows = self.fixture.rows
        self.csv_write = self.fixture.write_csv
        self.rows[0]["owner_note"]="Assembly"
        self.csv_write()

    def test_valid_equals(self):
        self.assertEqual([],check(self.root))

    def test_invalid_owner_path(self):
        self.rows[0]["owner_note"]="Wrong/Assembly"
        self.csv_write()
        self.assertTrue(any("pathTarget not found" in e for e in check(self.root)))

    def test_missing_symmetry(self):
        p=self.root/"Assembly.md"
        p.write_text(p.read_text().replace(f"- equals: [[#^{A}]]","- identifier: only"))
        self.assertTrue(any("symmetric" in e for e in check(self.root)))

    def test_flow_safe_exposure(self):
        self.rows[:]=[dict(ea_guid="binding-exposure",actual_relation="Connection.exposes",
            owner_note="Assembly",start_local=A,end_local=B,
            connection_local=C,exposes_local=A,candidate_connection_count="1")]
        self.csv_write()
        p=self.root/"Assembly.md"
        text="\n".join(line for line in p.read_text().splitlines() if not line.startswith("- equals:"))
        text=text.replace("<!-- MDSE:LOCAL-MODEL END -->",
            "##### Flow\n- endpointA: transmit\n- endpointB: receive\n^flow-20261014130000006skellyspencer\n<!-- MDSE:LOCAL-MODEL END -->")
        p.write_text(text)
        self.assertEqual([],check(self.root))

    def test_ambiguous_exposure_rejected(self):
        self.rows[:]=[dict(ea_guid="binding-exposure",actual_relation="Connection.exposes",
            owner_note="Assembly",start_local=A,end_local=B,
            connection_local=C,exposes_local=A,candidate_connection_count="2")]
        self.csv_write()
        self.assertTrue(any("ambiguous" in e for e in check(self.root)))

if __name__=="__main__":
    unittest.main()
