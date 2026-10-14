import test from "node:test";
import assert from "node:assert/strict";
import { ModelIndex, type NoteRecord } from "../src/core/model";
import { validateVariantOf } from "../src/core/variantof";
import { variantOfFormatError, variantOfMetadataFinding } from "../src/core/variantof-format";
import { fixtureSchema } from "./helpers";

function record(path: string, type: string, targets: string[] = []): NoteRecord {
  return {
    path, name: path.replace(/\.md$/, ""), type,
    uid: "20261003170000004skellyspencer",
    fields: new Map(targets.length ? [["variantOf", targets]] : []),
    unresolved: 0,
  };
}

test("variantOf frontmatter accepts one note-level link and rejects unsafe shapes", () => {
  assert.equal(variantOfFormatError("[[Product Type]]"), null);
  assert.equal(variantOfFormatError("[[Product Type|Alias]]"), null);
  for (const invalid of ["[[#^block]]", "[[Part]] [[Other]]", "[[Part#Section]]", ["[[Part]]"], 42]) {
    assert.ok(variantOfFormatError(invalid), JSON.stringify(invalid));
  }
  assert.equal(variantOfMetadataFinding({ variantOf: ["[[Part]]"] })?.includes("single wikilink"), true);
});

test("variantOf review diagnoses cycles and invalid Object endpoints without rewriting data", () => {
  const index = new ModelIndex(fixtureSchema());
  index.upsert(record("A.md", "Object", ["B.md"]));
  index.upsert(record("B.md", "Object", ["A.md"]));
  index.upsert(record("C.md", "Function", ["A.md"]));
  const before = index.notes.get("A.md")?.fields.get("variantOf")?.slice();
  const findings = validateVariantOf(index);
  assert.equal(findings.filter(f => f.code === "variant.cycle").length, 2);
  assert.ok(findings.some(f => f.code === "variant.endpoint-invalid" && f.path === "C.md"));
  assert.deepEqual(index.notes.get("A.md")?.fields.get("variantOf"), before);
});
