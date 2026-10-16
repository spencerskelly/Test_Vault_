import unittest
from imp011_owner_reference_v1 import resolve_owner


class OwnerReferenceTests(unittest.TestCase):
    def setUp(self):
        self.paths = {"01_A/Assembly.md", "02_B/Assembly.md"}

    def test_exact_relative_path(self):
        self.assertEqual("01_A/Assembly.md", resolve_owner("01_A/Assembly.md", self.paths))

    def test_explicit_unique_alias(self):
        self.assertEqual("01_A/Assembly.md", resolve_owner(
            "Assembly A", self.paths, {"Assembly A": "01_A/Assembly.md"}))

    def test_basename_collision_rejected(self):
        with self.assertRaises(ValueError):
            resolve_owner("Assembly.md", self.paths)

    def test_unmapped_alias_rejected(self):
        with self.assertRaises(ValueError):
            resolve_owner("Assembly A", self.paths)

    def test_parent_escape_rejected(self):
        with self.assertRaises(ValueError):
            resolve_owner("../01_A/Assembly.md", self.paths)


if __name__ == "__main__":
    unittest.main()
