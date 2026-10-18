"""Regression tests for bounded V2 relationship candidate review."""
import importlib.util
import json
import pathlib
import sqlite3
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "relationship_candidates", ROOT / "21_Importer/project_v2_relationship_candidates.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class RelationshipProjectionTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        base = pathlib.Path(self.temp.name)
        self.db = base / "synthetic.qeax"
        with sqlite3.connect(self.db) as con:
            con.execute("CREATE TABLE t_connector("
                        "Connector_ID INTEGER, Connector_Type TEXT, Stereotype TEXT)")
            con.executemany("INSERT INTO t_connector VALUES(?,?,?)", [
                (4, "Generalization", ""),
                (5, "Dependency", "verify"),
                (6, "Dependency", "unapproved"),
                (7, "NoteLink", ""),
            ])
        self.rules = base / "rules.json"
        self.registry = {
            "schema": "mdse-v2-semantic-rules/0.2",
            "automaticNativeEmission": False,
            "relationshipRules": [
                {"family": "Generalization:", "nativeCandidate": "Specialization",
                 "gate": "needs_typed_endpoints_and_direction",
                 "sourceDisposition": "existing_rule",
                 "emission": "deferred_pending_evidence_and_parser"},
                {"family": "Dependency:verify", "nativeCandidate": "VerifyRequirementUsage",
                 "gate": "needs_verification_case_objective",
                 "sourceDisposition": "review",
                 "emission": "deferred_pending_evidence_and_parser"},
                {"family": "NoteLink:", "nativeCandidate": "None",
                 "gate": "evidence_only", "sourceDisposition": "evidence_only",
                 "emission": "deferred_pending_evidence_and_parser"},
            ],
        }
        self.save()

    def save(self):
        self.rules.write_text(json.dumps(self.registry), encoding="utf-8")

    def test_candidates_and_unmatched_are_review_only(self):
        result = module.project(self.db, 4, self.rules)
        self.assertEqual(result["source_connectors"], 4)
        self.assertEqual(result["candidate_targets"], {
            "None": 1, "Specialization": 1, "UNMATCHED_REVIEW": 1,
            "VerifyRequirementUsage": 1,
        })
        self.assertEqual(result["native_relationships_emitted"], 0)
        self.assertFalse(result["source_data_modified"])
        self.assertEqual(result["deferred_rows"], 4)

    def test_bounded(self):
        result = module.project(self.db, 2, self.rules)
        self.assertEqual(result["source_connectors"], 2)
        with self.assertRaisesRegex(ValueError, "INVALID_LIMIT"):
            module.project(self.db, 0, self.rules)

    def test_unsafe_emission_rejected(self):
        self.registry["automaticNativeEmission"] = True
        self.save()
        with self.assertRaisesRegex(ValueError, "INVALID_OR_UNSAFE_REGISTRY"):
            module.project(self.db, 4, self.rules)

    def test_duplicate_rules_rejected(self):
        self.registry["relationshipRules"].append(
            dict(self.registry["relationshipRules"][0]))
        self.save()
        with self.assertRaisesRegex(ValueError, "AMBIGUOUS_RELATIONSHIP_RULES"):
            module.project(self.db, 4, self.rules)

    def test_source_not_modified(self):
        before = self.db.read_bytes()
        module.project(self.db, 4, self.rules)
        self.assertEqual(self.db.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
