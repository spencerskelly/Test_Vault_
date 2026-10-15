import unittest
from imp011_importer_owner_path_v1 import resolve_importer_owner

class PathTargetMappingTests(unittest.TestCase):
    def setUp(self):
        self.paths={"01_A/Assembly.md","02_B/Assembly.md","Nested/Sub/PCBA.md"}

    def test_nested_path_target(self):
        self.assertEqual("Nested/Sub/PCBA.md",resolve_importer_owner("Nested/Sub/PCBA",self.paths))

    def test_same_basename_distinct_folders(self):
        self.assertEqual("02_B/Assembly.md",resolve_importer_owner("02_B/Assembly",self.paths))

    def test_unqualified_name_rejected(self):
        with self.assertRaises(ValueError):
            resolve_importer_owner("Assembly",self.paths)

    def test_no_suffix_guess(self):
        with self.assertRaises(ValueError):
            resolve_importer_owner("B/Assembly",self.paths)

    def test_parent_escape_rejected(self):
        with self.assertRaises(ValueError):
            resolve_importer_owner("../01_A/Assembly",self.paths)

if __name__=="__main__":
    unittest.main()
