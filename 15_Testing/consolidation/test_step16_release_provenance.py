"""W-341/W-342 source-vs-runtime provenance regression tests.

These read text source + released plugin metadata only. They do not inspect QEAX,
promote source, alter any runtime file, or certify an Obsidian GUI session.
"""
from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = "Base Vault/Definition/mdse-release.yaml"
WORKBENCH_GUIDE = "55_Workbench/docs/User Guide/MDSE Workbench User Guide.md"
BASE_GUIDE = "Base Vault/Definition/MDSE Workbench User Guide.md"
WORKBENCH_PACKAGE = "55_Workbench/package.json"
WORKBENCH_MANIFEST = "55_Workbench/manifest.json"
LOCK_PATH = ".obsidian/plugin-lock.yaml"
W_LOG = "00_Workspace/Workspace Decision Log.md"
NATIVE_CHECK = "Base Vault/Testing/check-release.py"

def raw(p):
    return (ROOT / p).read_bytes()

def git_blob_sha(data):
    return hashlib.sha1(("blob " + str(len(data)) + "\0").encode() + data).hexdigest()

def parse_yaml(p):
    return yaml.safe_load(raw(p))

def metadata():
    manifest = parse_yaml(MANIFEST)
    lock = parse_yaml(LOCK_PATH)
    pkg = json.loads(raw(WORKBENCH_PACKAGE))
    plugin = json.loads(raw(WORKBENCH_MANIFEST))
    return manifest, lock, pkg, plugin

def candidate_acceptance(release_status, pin, candidate, plugin_lock, package, manifest):
    """Mirrors W-342 pre-release guard without changing production checker."""
    if plugin_lock != pin and not (release_status != "release" and candidate and plugin_lock == candidate):
        return False
    if not (package == manifest == pin or (
        release_status != "release" and candidate and package == manifest == candidate
    )):
        return False
    return True

class W341W342Verification(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.man, cls.lock, cls.pkg, cls.plugin = metadata()
        cls.workbench = cls.man["tools"]["workbench"]
        cls.lock_workbench = cls.lock["plugins"]["mdse-workbench"]

    def test_w341_source_guide_present(self):
        self.assertTrue((ROOT / WORKBENCH_GUIDE).is_file())

    def test_w341_base_guide_present(self):
        self.assertTrue((ROOT / BASE_GUIDE).is_file())

    def test_w341_guide_byte_exact(self):
        self.assertEqual(raw(WORKBENCH_GUIDE), raw(BASE_GUIDE))

    def test_w341_guide_git_blob_identical(self):
        for p in (WORKBENCH_GUIDE,BASE_GUIDE):
            with self.subTest(path=p):
                self.assertEqual(git_blob_sha(raw(p)),
                                 "2a82d21f89a2e80e4df227760f85f1215cd76ec5")

    def test_w341_guide_fails_on_single_byte_drift(self):
        mutated = raw(BASE_GUIDE) + b"\n"
        self.assertNotEqual(raw(WORKBENCH_GUIDE),mutated)

    def test_w341_release_manifest_points_to_base_copy(self):
        self.assertEqual(self.workbench["userGuide"], BASE_GUIDE)

    def test_w341_runtime_copy_has_exact_user_path(self):
        copies = self.man["runtimeBase"]["mappedFiles"]
        self.assertEqual(sum(x.get("source")==BASE_GUIDE and
                             x.get("target")=="99_System/01_Admin/MDSE Workbench User Guide.md"
                             for x in copies), 1)

    def test_w341_missing_guide_mapping_fails_policy(self):
        copies = self.man["runtimeBase"]["mappedFiles"]
        bad=[x for x in copies if x["source"]!=BASE_GUIDE]
        self.assertFalse(any(x["source"]==BASE_GUIDE for x in bad))

    def test_w341_guide_marks_candidate_versus_release(self):
        text=raw(BASE_GUIDE).decode("utf-8")
        self.assertIn("**Candidate**",text)
        self.assertIn("0.1.18",text)
        self.assertIn("pre-release",text)

    def test_w342_release_remains_pre_release(self):
        self.assertEqual(self.man["releaseStatus"],"pre-release")

    def test_w342_explicit_pin_equals_workbench_package(self):
        self.assertEqual(self.workbench["version"],self.pkg["version"])

    def test_w342_explicit_pin_equals_plugin_manifest(self):
        self.assertEqual(self.workbench["version"],self.plugin["version"])

    def test_w342_explicit_pin_equals_plugin_lock(self):
        self.assertEqual(self.workbench["version"],self.lock_workbench["version"])

    def test_w342_no_unapproved_candidate_override(self):
        self.assertIsNone(self.workbench["candidateVersion"])

    def test_w342_wb106_pin_matches_controlled_runtime(self):
        self.assertEqual(self.workbench["wb106Version"],self.workbench["version"])

    def test_w342_plugin_identity(self):
        self.assertEqual(self.plugin["id"],self.workbench["runtimePluginId"])
        self.assertEqual(self.pkg["name"],self.plugin["id"])

    def test_w342_lock_source_stays_historical(self):
        self.assertIn("spencerskelly/MDSE_Workbench 0.1.18 artifact",
                      self.lock_workbench["source"])
        self.assertEqual(git_blob_sha(raw(LOCK_PATH)),
                         "c430670577318457972a154012d08c6d28e6d11b")

    def test_w342_current_configuration_accepted(self):
        wb=self.workbench
        self.assertTrue(candidate_acceptance(self.man["releaseStatus"],
                        wb["version"],wb["candidateVersion"],
                        self.lock_workbench["version"],
                        self.pkg["version"],self.plugin["version"]))

    def test_w342_explicit_pre_release_candidate_can_differ(self):
        self.assertTrue(candidate_acceptance("pre-release","0.1.18","0.1.19",
                                              "0.1.18","0.1.19","0.1.19"))

    def test_w342_unapproved_candidate_rejected(self):
        self.assertFalse(candidate_acceptance("pre-release","0.1.18",None,
                                               "0.1.18","0.1.19","0.1.19"))

    def test_w342_mismatched_candidate_package_manifest_rejected(self):
        self.assertFalse(candidate_acceptance("pre-release","0.1.18","0.1.19",
                                               "0.1.18","0.1.19","0.1.18"))

    def test_w342_issued_release_rejects_candidate_difference(self):
        self.assertFalse(candidate_acceptance("release","0.1.18","0.1.19",
                                               "0.1.18","0.1.19","0.1.19"))

    def test_w342_issued_release_rejects_lock_drift(self):
        self.assertFalse(candidate_acceptance("release","0.1.18","0.1.19",
                                               "0.1.19","0.1.18","0.1.18"))

    def test_w342_unexpected_lock_drift_rejected(self):
        self.assertFalse(candidate_acceptance("pre-release","0.1.18",None,
                                               "0.1.17","0.1.18","0.1.18"))

    def test_w342_release_checker_version_branch_exists(self):
        source=raw(NATIVE_CHECK).decode("utf-8")
        for phrase in (
            'candidate_wb=man["tools"]["workbench"].get("candidateVersion")',
            'man["releaseStatus"]!="release" and candidate_wb',
            'if pv==mv==pinned:',
            '"Workbench user guide equals Base Vault release copy"',
        ):
            self.assertIn(phrase,source)

    def test_w342_original_decisions_unchanged(self):
        self.assertEqual(git_blob_sha(raw(W_LOG)),
                         "49ab9bc513b27ce7e1c2beed6e039aad5c0bebbb")
        txt=raw(W_LOG).decode("utf-8")
        for key in ("**W-341 · 2026-10-03", "**W-342 · 2026-10-03"):
            self.assertIn(key,txt)

    def test_w342_runtime_manifest_lock_payload_mapping(self):
        self.assertEqual(self.man["runtimePlugins"]["lock"],LOCK_PATH)
        self.assertEqual(self.man["runtimePlugins"]["payload"],"Base Vault/Runtime/Plugins")
        self.assertIn("main.js",self.lock_workbench["sha256"])
        self.assertIn("manifest.json",self.lock_workbench["sha256"])

    def test_w342_release_pin_has_no_writer_06_promotion(self):
        self.assertEqual(self.man["schemas"]["localModel"],"0.5")
        self.assertEqual(self.man["mdseRelease"],"0.8.0")

if __name__ == "__main__":
    unittest.main()
