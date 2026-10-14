"""Synthetic validation of strict owner pathTarget and Flow-safe IMP-011 v2."""
import unittest
from test_imp011_topology_synthetic import Imp011TopologySynthetic, A, B, C
from imp011_topology_acceptance_v2 import check

class TopologyV2OwnerAndFlow(Imp011TopologySynthetic):
    def setUp(self):
        super().setUp()
        for row in self.rows:
            row["owner_note"] = "Assembly"
        self.write_csv()

    def test_valid_equals(self):
        self.assertEqual([], check(self.root))

    def test_valid_exposure(self):
        self.rows=[dict(ea_guid="binding-exposure",actual_relation="Connection.exposes",
                        owner_note="Assembly",start_local=A,end_local=B,
                        connection_local=C,exposes_local=A,candidate_connection_count="1")]
        self.write_csv()
        p=self.root/"Assembly.md"
        text="\n".join(x for x in p.read_text().splitlines() if not x.startswith("- equals:"))
        text=text.replace("<!-- MDSE:LOCAL-MODEL END -->",
            "##### Item Flow\n- endpointA: transmit\n- endpointB: receive\n^flow-20261014130000006skellyspencer\n<!-- MDSE:LOCAL-MODEL END -->")
        p.write_text(text)
        self.assertEqual([],check(self.root))

    def test_missing_owner_path_rejected(self):
        self.rows[0]["owner_note"] = "Nonexistent/Assembly"
        self.write_csv()
        self.assertTrue(any("pathTarget not found" in x for x in check(self.root)))

    def test_reject_wrong_owner(self):
        self.rows[0]["owner_note"]="Other"
        self.write_csv()
        self.assertTrue(check(self.root))

if __name__=="__main__":
    unittest.main()
