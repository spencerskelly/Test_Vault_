import test from "node:test";
import assert from "node:assert/strict";
import { ModelIndex } from "../src/core/model";
import { LocalModelIndex, parseLocalModel } from "../src/core/localmodel";
import { serializeSemanticState, restoreSemanticState } from "../src/core/cache";
import { fixtureSchema } from "./helpers";

const schema = fixtureSchema();
const scope = { vaultUid: "20261003190000001skellyspencer" };
const ID = "20261003133512742skellyspencer";

test("semantic cache preserves schema 0.6 part quantities and units after JSON roundtrip", () => {
  const text = [
    "## Local Model", "<!-- MDSE:LOCAL-MODEL START schema=0.6 -->",
    "### Parts", "#### Cable",
    "- multiplicity: 2", "- quantity: 3.5", "- unitOfMeasure: m",
    "^" + ID, "<!-- MDSE:LOCAL-MODEL END -->",
  ].join("\n");
  const parsed = parseLocalModel(text);
  assert.ok(parsed);
  const index = new ModelIndex(schema);
  const local = new LocalModelIndex();
  local.set("Assembly.md", parsed);
  const cache = serializeSemanticState(index, local, new Map(), schema, scope, "0.1.18");
  const restored = restoreSemanticState(JSON.parse(JSON.stringify(cache)), schema, scope);
  const record = restored.local.recordsOf("Assembly.md").find(r => r.localId === ID);
  assert.ok(record);
  assert.equal(record.multiplicity, "2");
  assert.equal(record.quantity, "3.5");
  assert.equal(record.unitOfMeasure, "m");
});
