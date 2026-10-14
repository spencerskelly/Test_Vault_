import test from "node:test";
import assert from "node:assert/strict";
import { parseLocalModel, READABLE_VERSIONS, WRITABLE_VERSION } from "../src/core/localmodel";

const END = "<!-- MDSE:LOCAL-MODEL END -->";
const ID = "20261003133512742skellyspencer";
const part = (version: string, extras: string[]) => [
  "## Local Model",
  "<!-- MDSE:LOCAL-MODEL START schema=" + version + " -->",
  "### Parts",
  "#### Cable",
  ...extras,
  "^" + ID,
  END,
].join("\n");

test("schema 0.6 reads quantity and unitOfMeasure without enabling 0.6 writes", () => {
  assert.ok(READABLE_VERSIONS.includes("0.6"));
  assert.equal(WRITABLE_VERSION, "0.5");
  const parsed = parseLocalModel(part("0.6", [
    "- multiplicity: 2",
    "- quantity: 3.5",
    "- unitOfMeasure: m",
  ]));
  assert.ok(parsed);
  const record = parsed.records.find(r => r.localId === ID);
  assert.ok(record);
  assert.equal(record.quantity, "3.5");
  assert.equal(record.unitOfMeasure, "m");
  assert.equal(record.multiplicity, "2");
  assert.ok(!parsed.findings.some(f => f.code === "field.unknown"));
});

test("quantity and unitOfMeasure are not silently accepted under schema 0.5", () => {
  const parsed = parseLocalModel(part("0.5", [
    "- quantity: 4",
    "- unitOfMeasure: kg",
  ]));
  assert.ok(parsed);
  assert.ok(parsed.findings.length > 0, "earlier writable schema must report unsupported fields");
});
