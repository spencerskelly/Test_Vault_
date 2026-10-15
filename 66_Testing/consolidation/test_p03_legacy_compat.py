"""P03.4 synthetic legacy-note triage tests (stdlib only; no edits to models).

Run: python3 -m unittest discover -s 66_Testing/consolidation -p 'test_p03_legacy_compat.py' -v
This is a review-only compatibility classifier, NOT the EA importer or a YAML parser.
"""
import hashlib
import re
import unittest

LEGACY_TYPES = {
    "Design": ("Condition", "design"),
    "Function": ("Behavior", "function"),
    "Step": ("Behavior", "step"),
    "State Machine": ("Condition", "state machine"),
    "State": ("Condition", "state"),
}
AMBIGUOUS_TYPES = {"Port"}
AMBIGUOUS_LINKS = {
    "equals", "exposes", "interfaces", "hasClassifier", "hasFlow",
    "hasPort", "transmits", "receives", "exchanges",
}
FIELD = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*?)\s*$")


def triage_legacy_note(raw: bytes) -> dict:
    """Return proposed classification only. Never modify or normalize input bytes."""
    before = hashlib.sha256(raw).hexdigest()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return {"status": "REVIEW_ONLY", "reason": "non-UTF8 source",
                "source_sha256": before}
    lines = text.splitlines()
    if len(lines) < 3 or lines[0] != "---":
        return {"status": "REVIEW_ONLY", "reason": "missing frontmatter",
                "source_sha256": before}
    try:
        last = lines.index("---", 1)
    except ValueError:
        return {"status": "REVIEW_ONLY", "reason": "unclosed frontmatter",
                "source_sha256": before}
    pairs = []
    for line in lines[1:last]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = FIELD.fullmatch(line)
        if not m:
            return {"status": "REVIEW_ONLY", "reason": "unsupported YAML shape",
                    "source_sha256": before}
        key, value = m.group(1), m.group(2).strip()
        # Conservative guard: this is not a YAML parser. Do not attempt
        # semantic interpretation of collections, aliases, tags or block scalars.
        if (not value or value.startswith(("-", "[", "{", "&", "*", "!", "|", ">"))
                or re.search(r"(?<![A-Za-z0-9])(?:&|[*]|!!)[A-Za-z_]", value)):
            return {"status": "REVIEW_ONLY", "reason": "unsupported YAML shape",
                    "source_sha256": before}
        pairs.append((key, value.strip(chr(34) + chr(39))))
    keys = [k for k, _ in pairs]
    if len(keys) != len(set(keys)):
        return {"status": "REVIEW_ONLY", "reason": "duplicate frontmatter key",
                "source_sha256": before}
    data = dict(pairs)
    note_type = data.get("type", "")
    risky = sorted(AMBIGUOUS_LINKS.intersection(data))
    proposed = LEGACY_TYPES.get(note_type)
    if note_type in AMBIGUOUS_TYPES:
        status, reason = "REVIEW_ONLY", "Port definition versus occurrence requires context"
    elif risky:
        status, reason = "REVIEW_ONLY", "legacy relationships need explicit mapping"
    elif proposed:
        status, reason = "PROPOSED_ONLY", "schema-aligned type mapping, not migration"
    else:
        status, reason = "REVIEW_ONLY", "unknown or non-legacy type"
    return {"status": status, "reason": reason, "old_type": note_type,
            "proposed_type": proposed, "legacy_fields": risky,
            "uid": data.get("uid"), "id": data.get("id"),
            "source_sha256": before}


def note(note_type, more=""):
    return ("---\ntype: " + note_type +
            "\nuid: 20260930133525659skellyspencer\nid: LEG-0001\n" +
            more + "---\n# Legacy title\n\nOriginal narrative preserved.\n").encode()


class LegacyTriageTests(unittest.TestCase):
    def test_five_type_families_only_propose(self):
        for old, new in LEGACY_TYPES.items():
            with self.subTest(old=old):
                r = triage_legacy_note(note(old))
                self.assertEqual(r["status"], "PROPOSED_ONLY")
                self.assertEqual(r["proposed_type"], new)

    def test_port_is_review_only(self):
        self.assertEqual(triage_legacy_note(note("Port"))["status"], "REVIEW_ONLY")

    def test_exposes_is_not_reinterpreted(self):
        r = triage_legacy_note(note("Port", "exposes: '[[inner Port]]'\n"))
        self.assertIn("exposes", r["legacy_fields"])
        self.assertEqual(r["status"], "REVIEW_ONLY")

    def test_equals_is_not_reinterpreted(self):
        r = triage_legacy_note(note("Port", "equals: '[[other Port]]'\n"))
        self.assertIn("equals", r["legacy_fields"])
        self.assertEqual(r["status"], "REVIEW_ONLY")

    def test_flow_direction_not_inferred(self):
        for key in ("transmits", "receives", "exchanges", "hasFlow"):
            with self.subTest(key=key):
                r = triage_legacy_note(note("Port", key + ": '[[flow]]'\n"))
                self.assertIn(key, r["legacy_fields"])

    def test_relationships_block_automatic_type_conversion(self):
        r = triage_legacy_note(note("Step", "interfaces: []\n"))
        self.assertEqual(r["status"], "REVIEW_ONLY")

    def test_duplicate_fields_fail_closed(self):
        self.assertEqual(triage_legacy_note(note("Design", "uid: duplicate\n"))["reason"],
                         "duplicate frontmatter key")

    def test_malformed_frontmatter_fails_closed(self):
        self.assertEqual(triage_legacy_note(b"---\ntype: Port\n")["status"],
                         "REVIEW_ONLY")

    def test_byte_preservation_and_determinism(self):
        raw = note("State", "unrecognized_field: keep-me\n")
        digest = hashlib.sha256(raw).hexdigest()
        self.assertEqual(triage_legacy_note(raw), triage_legacy_note(raw))
        self.assertEqual(hashlib.sha256(raw).hexdigest(), digest)
        self.assertEqual(triage_legacy_note(raw)["source_sha256"], digest)

    def test_unsupported_yaml_shape_fails_closed(self):
        raw = note("Function", "nested:\n  value: uncertain\n")
        self.assertEqual(triage_legacy_note(raw)["status"], "REVIEW_ONLY")


    def test_realistic_multiline_yaml_is_review_only(self):
        raw = note("Design", "satisfies:\n  - '[[REQ-01]]'\n  - '[[REQ-02]]'\n")
        result = triage_legacy_note(raw)
        self.assertEqual(result["status"], "REVIEW_ONLY")
        self.assertEqual(result["reason"], "unsupported YAML shape")

    def test_realistic_legacy_port_links_retained_as_review(self):
        raw = note("Port", "interfaces: '[[Assembly/Port-A|Port A]]'\n"
                   "exposes: '[[InnerPort#Interface]]'\n")
        result = triage_legacy_note(raw)
        self.assertEqual(result["status"], "REVIEW_ONLY")
        self.assertEqual(result["legacy_fields"], ["exposes", "interfaces"])
        self.assertEqual(result["source_sha256"], hashlib.sha256(raw).hexdigest())

    def test_unknown_property_never_deleted_or_converted(self):
        raw = note("Function", "customSupplierId: A:B-12\n")
        result = triage_legacy_note(raw)
        self.assertEqual(result["status"], "PROPOSED_ONLY")
        self.assertEqual(result["source_sha256"], hashlib.sha256(raw).hexdigest())

    def test_unsupported_yaml_alias_or_list_fails_closed(self):
        for raw in (
            note("State", "tags: &labels [legacy]\nnotes: *labels\n"),
            note("State", "hasState:\n  - '[[Substate]]'\n"),
        ):
            with self.subTest(sample=raw):
                result = triage_legacy_note(raw)
                self.assertEqual(result["status"], "REVIEW_ONLY")
                self.assertEqual(result["source_sha256"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(triage_legacy_note(
            note("State", "hasState:\n  - '[[Substate]]'\n"))["status"], "REVIEW_ONLY")

    def test_invalid_utf8_fails_closed(self):
        self.assertEqual(triage_legacy_note(b"---\ntype: Design\n---\n\xff")["reason"],
                         "non-UTF8 source")


    def test_yaml_alias_never_proposed(self):
        for extra in ("tags: &labels [legacy]\\nnotes: *labels\\n",
                      "related: *source\\n", "related: !unsafe value\\n",
                      "related: {key: value}\\n", "related: |\\n  text\\n"):
            with self.subTest(extra=extra):
                self.assertEqual(triage_legacy_note(note("State", extra))["status"],
                                 "REVIEW_ONLY")

    def test_empty_and_inline_collections_review_only(self):
        for extra in ("satisfies: []\\n", "satisfies: [REQ-1]\\n",
                      "satisfies:\\n  - REQ-1\\n"):
            with self.subTest(extra=extra):
                self.assertEqual(triage_legacy_note(note("Function", extra))["status"],
                                 "REVIEW_ONLY")


if __name__ == "__main__":
    unittest.main()
