"""Approved-group lookup tests: no QEAX model data or parser claims."""
import importlib.util
import json
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "approved_rules", ROOT / "21_Importer/v2_approved_family_resolver.py")
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


class ApprovedResolverTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = mod.load_registry()

    def test_all_60_plus_26_groups_are_exactly_addressable(self):
        self.assertEqual(len(self.rules["elements"]), 60)
        self.assertEqual(len(self.rules["relationships"]), 26)
        for family, rule in self.rules["elements"].items():
            a, sep, b = family.partition(":")
            result = mod.resolve_element(a, b if sep else "", registry=self.rules)
            self.assertEqual(result["status"], "approved_group", family)
            self.assertEqual(result["disposition"], rule["disposition"])
            self.assertFalse(result["emission_authorized"])
        for family, rule in self.rules["relationships"].items():
            a, sep, b = family.partition(":")
            result = mod.resolve_connector(a, b if sep else "", registry=self.rules)
            self.assertEqual(result["status"], "approved_group", family)
            self.assertEqual(result["native_operation"], rule["native_operation"])
            self.assertFalse(result["emission_authorized"])
        self.assertEqual(sum(x["source_count"] for x in self.rules["relationships"].values()), 14688)

    def test_known_approved_exceptions_not_overridden_by_generic_family(self):
        expectations = {
            "InformationItem": ("mdse_note", None),
            "Object": ("native_candidate", "PartDefinition"),
            "Class:Generic Physical Interface": ("native_candidate", "PortDefinition"),
            "Class:Physical Context": ("native_candidate", "PartDefinition"),
            "Signal:Software Parameter": ("native_candidate", "AttributeDefinition"),
            "Activity:testCase": ("native_candidate", "VerificationCaseDefinition"),
            "Event": ("native_candidate", "OccurrenceDefinition"),
            "Part:FlowProperty": ("native_candidate", "ItemUsage"),
            "Boundary": ("aggregate_boundary_note", None),
            "Package": ("folder_only", None),
            "Sequence": ("reference_only", None),
            "ProxyConnector": ("reference_only", None)
        }
        for family, expected in expectations.items():
            a, sep, b = family.partition(":")
            result = mod.resolve_element(a, b if sep else "", registry=self.rules)
            self.assertEqual((result["disposition"], result["native_kind"]), expected)
        for family, operation in {
            "Realisation:deriveReqt": "RequirementDerivation",
            "UseCase:include": "RequiredUseCaseUsage",
            "UseCase:extend": "ConditionalUseCaseUsage",
            "Generalization": "Specialization",
            "Aggregation": "TypedOwnedUsage",
            "Sequence": None, "NoteLink": None
        }.items():
            a, sep, b = family.partition(":")
            self.assertEqual(
                mod.resolve_connector(a, b if sep else "", registry=self.rules)["native_operation"],
                operation)

    def test_untyped_families_are_allowed_with_review_not_conjured_typing(self):
        for family, kind in [("Part", "PartUsage"), ("Port", "PortUsage"), ("Action", "ActionUsage")]:
            result = mod.resolve_element(family, registry=self.rules)
            self.assertEqual(result["native_kind"], kind)
            self.assertIn("UNTYPED_ALLOWED_REVIEW_FLAG", result["review_notes"])
            self.assertTrue(result["requires_row_validation"])

    def test_unknowns_are_outliers_not_wildcard_coercion(self):
        self.assertEqual(mod.resolve_element("Class", "unapproved", registry=self.rules)["reason"],
                         mod.OUTLIER)
        self.assertEqual(mod.resolve_element("InformationItem", "unapproved", registry=self.rules)["reason"],
                         mod.OUTLIER)
        self.assertEqual(mod.resolve_connector("Realisation", "new-mystery", registry=self.rules)["reason"],
                         mod.OUTLIER)
        self.assertEqual(mod.resolve_connector("Aggregation", registry=self.rules)["status"],
                         "approved_group")
        for args in [(" Class", ""), ("Class", " new "), (None, "")]:
            with self.assertRaises(ValueError):
                mod.family_key(*args)

    def test_registry_rejects_unsafe_emission_diagrams_or_loss_of_families(self):
        original = json.loads(mod.DEFAULT_REGISTRY.read_text(encoding="utf-8"))
        scenarios = [
            ("ea_diagrams_enabled", True),
            ("automatic_native_emission", True),
            ("source_data_tables", ["t_object", "t_connector", "t_package", "t_diagram"])
        ]
        with tempfile.TemporaryDirectory() as d:
            dest = pathlib.Path(d)/"rules.json"
            for key, changed in scenarios:
                invalid = dict(original)
                invalid[key] = changed
                dest.write_text(json.dumps(invalid))
                with self.assertRaises(ValueError, msg=key):
                    mod.load_registry(dest)
            invalid = dict(original)
            invalid["elements"] = invalid["elements"][:-1]
            dest.write_text(json.dumps(invalid))
            with self.assertRaisesRegex(ValueError, "COVERAGE_INCOMPLETE"):
                mod.load_registry(dest)
            invalid = dict(original)
            invalid["relationships"] = invalid["relationships"][:-1] + [invalid["relationships"][0]]
            dest.write_text(json.dumps(invalid))
            with self.assertRaisesRegex(ValueError, "DUPLICATE_EXACT_FAMILY"):
                mod.load_registry(dest)


if __name__ == "__main__":
    unittest.main()
