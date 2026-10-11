"""Regression coverage for Workbench legacy repository reference disposition."""
from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from workbench_reference_policy import (
    LEGACY_REPO, PROVENANCE_BLOBS, analyze, classify, git_blob_sha,
)

ROOT = Path(__file__).resolve().parents[2]


class RepositoryReferenceTests(unittest.TestCase):
    def test_legacy_repo_constant(self):
        self.assertEqual(LEGACY_REPO, "spencerskelly/" + "MDSE_Workbench")

    def test_three_frozen_provenance_files_match(self):
        for path, expected in PROVENANCE_BLOBS.items():
            with self.subTest(path=path):
                self.assertEqual(git_blob_sha((ROOT / path).read_bytes()), expected)
                self.assertEqual(classify(ROOT, path), "verified_provenance")

    def test_provenance_tampering_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            p = ".obsidian/plugin-lock.yaml"
            path = Path(d) / p
            path.parent.mkdir(parents=True)
            path.write_bytes((ROOT / p).read_bytes() + b"\n# tampered\n")
            self.assertEqual(classify(Path(d), p), "blocking")

    def test_generator_tampering_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            p = "Base Vault/Tools/v0.8.0-r2/update-plugin-lock.py"
            file = Path(d) / p
            file.parent.mkdir(parents=True)
            shutil.copy2(ROOT / p, file)
            self.assertEqual(classify(Path(d), p), "verified_provenance")
            file.write_bytes(file.read_bytes().replace(b"default", b"unsafe", 1))
            self.assertEqual(classify(Path(d), p), "blocking")

    def test_missing_provenance_source_is_blocking(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(classify(Path(d), ".obsidian/plugin-lock.yaml"), "blocking")

    def test_active_workflow_checkouts_are_blocking(self):
        self.assertEqual(classify(ROOT, ".github/workflows/wb129-rehearsal.yml"), "blocking")

    def test_altered_active_workflow_is_not_exempted(self):
        self.assertEqual(classify(ROOT, ".github/workflows/old-frozen-history.yml"), "blocking")

    def test_current_manifest_is_blocking(self):
        self.assertEqual(classify(ROOT, "Base Vault/Definition/mdse-release.yaml"), "blocking")

    def test_current_owned_docs_block(self):
        for p in ("README.md", "00_Workspace/README.md",
                  "55_Workbench/docs/Definition/04 - Architecture and Model Boundary.md"):
            with self.subTest(p=p):
                self.assertEqual(classify(ROOT, p), "blocking")

    def test_history_frozen_citations_nonblocking(self):
        paths = ["00_Workspace/Workspace Decision Log.md",
                 "55_Workbench/docs/bom/A01-A14_RECOVERY_STATUS_2026-10-09.md",
                 "00_Workspace/Consolidation Step 08 - Actual Workbench Reference Audit 2026-10-10.md",
                 "55_Workbench/docs/Reference/ARCHIVE_WB106_RUNTIME_BUILD.yml"]
        for p in paths:
            with self.subTest(p=p):
                self.assertEqual(classify(ROOT, p), "historical")

    def test_current_unknown_doc_needs_review(self):
        self.assertEqual(classify(ROOT, "55_Workbench/docs/Definition/03 - Build Outline and Roadmap.md"), "needs_review")

    def test_unexpected_executable_blocks(self):
        self.assertEqual(classify(ROOT, "Importer/Tools/v0.8.19/new.py"), "blocking")

    def test_unknown_plain_text_needs_review(self):
        self.assertEqual(classify(ROOT, "00_Workspace/New Owner Policy.md"), "needs_review")

    def test_invalid_unsafe_paths_are_not_trusted(self):
        for p in ("../README.md", "/etc/passwd", "", "docs\\..\\README.md"):
            with self.subTest(p=p):
                self.assertEqual(classify(ROOT, p), "needs_review")

    def test_active_plus_history_rejects_strict(self):
        res = analyze(ROOT, [".github/workflows/wb129-rehearsal.yml",
                             "00_Workspace/Workspace Decision Log.md"])
        self.assertFalse(res["strictReady"])
        self.assertEqual(res["counts"]["blocking"], 1)
        self.assertEqual(res["counts"]["historical"], 1)

    def test_provenance_and_history_only_are_informational(self):
        res = analyze(ROOT, [".obsidian/plugin-lock.yaml",
                             "Base Vault/Tools/v0.8.0-r2/update-plugin-lock.py",
                             "00_Workspace/Workspace Decision Log.md"])
        self.assertTrue(res["strictReady"])
        self.assertEqual(res["counts"]["verified_provenance"], 2)
        self.assertEqual(res["counts"]["historical"], 1)

    def test_needs_review_fails_strict(self):
        res = analyze(ROOT, ["00_Workspace/Unknown.md"])
        self.assertFalse(res["strictReady"])
        self.assertEqual(res["counts"]["needs_review"], 1)

    def test_deduplicate_paths_and_counts(self):
        res = analyze(ROOT, ["00_Workspace/History/old.md",
                             "00_Workspace/History/old.md",
                             "00_Workspace/Unexpected.md"])
        self.assertEqual(res["counts"]["historical"], 1)
        self.assertEqual(res["counts"]["needs_review"], 1)

    def test_no_file_contents_in_output(self):
        res = analyze(ROOT, [".obsidian/plugin-lock.yaml"])
        self.assertNotIn("artifact b0c4e2c6", str(res))
        self.assertNotIn(LEGACY_REPO, str(res))

    def test_known_historical_registry_is_not_executable(self):
        self.assertEqual(classify(ROOT, "66_Testing/consolidation/STEP08_REFERENCE_DISPOSITIONS.json"), "historical")

    def test_no_frozen_workflow_exemption(self):
        all_paths = [".github/workflows/wb128-gate5-release-alignment.yml",
                     "00_Workspace/History/wb128.md"]
        res = analyze(ROOT, all_paths)
        self.assertFalse(res["strictReady"])
        self.assertEqual(res["counts"]["blocking"], 1)


if __name__ == "__main__":
    unittest.main()
