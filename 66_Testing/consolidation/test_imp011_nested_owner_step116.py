"""IMP-011 v2 tests with nested owner paths and duplicate note basenames."""
import csv
import tempfile
import unittest
from pathlib import Path

from imp011_topology_acceptance_v2 import check

A = "ep-20261014130000001skellyspencer"
B = "ep-20261014130000002skellyspencer"
START = "<!-- MDSE:LOCAL-MODEL START schema=0.5 -->"
END = "<!-- MDSE:LOCAL-MODEL END -->"


class NestedOwnerPathTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.vault = Path(self.tmp.name)
        self.first = self.vault / "01_A" / "Assembly.md"
        self.second = self.vault / "02_B" / "Assembly.md"
        for p in (self.first, self.second):
            p.parent.mkdir(parents=True)
        self.first.write_text(f"""{START}
### Interfaces
#### Boundary
- equals: [[#^{B}]]
^{A}
#### Internal
- equals: [[#^{A}]]
^{B}
{END}
""", encoding="utf-8")
        self.second.write_text(f"""{START}
### Interfaces
#### Other
^ep-20261014130000007skellyspencer
{END}
""", encoding="utf-8")
        self.review = self.vault / "99_System/11_Import/Review - Equals Direction.csv"
        self.review.parent.mkdir(parents=True)
        self.row = {"ea_guid":"example", "actual_relation":"Interface.equals",
                    "owner_note":"01_A/Assembly", "start_local":A, "end_local":B}
        self.write_review()

    def write_review(self):
        with self.review.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(self.row))
            writer.writeheader()
            writer.writerow(self.row)

    def test_exact_nested_owner_passes(self):
        self.assertEqual([], check(self.vault))

    def test_other_identically_named_note_cannot_satisfy_owner(self):
        self.row["owner_note"] = "02_B/Assembly"
        self.write_review()
        self.assertTrue(any("owner mismatch" in e for e in check(self.vault)))

    def test_unqualified_duplicate_basename_fails_closed(self):
        self.row["owner_note"] = "Assembly"
        self.write_review()
        self.assertTrue(any("pathTarget not found" in e for e in check(self.vault)))


if __name__ == "__main__":
    unittest.main()
