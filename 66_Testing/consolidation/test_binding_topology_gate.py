import unittest
from binding_topology_gate import validate_binding


class BindingTopologyNegativeTests(unittest.TestCase):
    def setUp(self):
        self.owners = {"boundary": "assembly", "inside": "assembly", "other": "other-assembly"}
        self.connections = {"conn": {"owner": "assembly", "endpoints": ("inside", "peer")}}
        self.exposure = dict(ea_guid="fixture-1", actual_relation="Connection.exposes",
                             category="resolved Connection.exposes", owner_note="assembly",
                             start_local="inside", end_local="boundary", candidate_connection_count="1",
                             connection_local="conn", exposes_local="boundary",
                             boundary_ids=("boundary",))
        self.equals = dict(ea_guid="fixture-2", actual_relation="Interface.equals",
                           category="canonical local equals - same-owner nested internal binding",
                           owner_note="assembly", start_local="inside", end_local="boundary",
                           explicit_binding=True, symmetric=True)

    def test_valid_exposure(self):
        self.assertEqual([], validate_binding(self.exposure, self.owners, self.connections))

    def test_ambiguous_exposure_rejected(self):
        for count in ("0", "2"):
            with self.subTest(count=count):
                row = dict(self.exposure, candidate_connection_count=count)
                self.assertTrue(validate_binding(row, self.owners, self.connections))

    def test_wrong_owner_rejected(self):
        owners = dict(self.owners, boundary="other-assembly")
        self.assertTrue(validate_binding(self.exposure, owners, self.connections))

    def test_nonboundary_rejected(self):
        row = dict(self.exposure, boundary_ids=())
        self.assertTrue(validate_binding(row, self.owners, self.connections))

    def test_missing_connection_rejected(self):
        self.assertTrue(validate_binding(dict(self.exposure, connection_local="missing"), self.owners, self.connections))

    def test_duplicate_disposition_rejected(self):
        self.assertTrue(validate_binding(dict(self.exposure, also_equals=True), self.owners, self.connections))
        self.assertTrue(validate_binding(dict(self.equals, also_exposes=True), self.owners, self.connections))

    def test_valid_equals(self):
        self.assertEqual([], validate_binding(self.equals, self.owners, self.connections))

    def test_cross_owner_equals_rejected(self):
        self.assertTrue(validate_binding(dict(self.equals, end_local="other"), self.owners, self.connections))

    def test_equals_without_evidence_rejected(self):
        self.assertTrue(validate_binding(dict(self.equals, explicit_binding=False), self.owners, self.connections))

    def test_asymmetric_equals_rejected(self):
        self.assertTrue(validate_binding(dict(self.equals, symmetric=False), self.owners, self.connections))

    def test_wrong_category_rejected(self):
        self.assertTrue(validate_binding(dict(self.exposure, category="cross-owner binding"), self.owners, self.connections))

    def test_unresolved_persistence_rejected(self):
        row = dict(ea_guid="fixture-3", actual_relation="", category="cross-owner binding", also_equals=True)
        self.assertTrue(validate_binding(row, self.owners, self.connections))


if __name__ == "__main__":
    unittest.main()
