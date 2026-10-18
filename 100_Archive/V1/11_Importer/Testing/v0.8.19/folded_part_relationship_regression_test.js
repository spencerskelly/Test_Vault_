#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

const importer = path.resolve(__dirname, "../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const src = fs.readFileSync(importer, "utf8");

function extractFunction(name) {
  const start = src.indexOf("function " + name + "(");
  if (start < 0) throw new Error("Missing function: " + name);
  const next = src.indexOf("\nfunction ", start + 10);
  if (next < 0) throw new Error("Missing function boundary after: " + name);
  return src.slice(start, next).trim();
}

const expectedCall =
  'addForwardRel(graph,owner.key,ownerField(owner.type,child.type,owner.plan&&owner.plan.subtype,child.plan&&child.plan.subtype),child.key,false);';
const staleCall =
  'addForwardRel(graph,owner.key,ownerField(owner.type,child.type,child.plan&&child.plan.subtype),child.key,false);';

if (!src.includes(expectedCall)) {
  throw new Error("folded Part relationship graph does not pass both ownerSubtype and childSubtype");
}
if (src.includes(staleCall)) {
  throw new Error("stale folded Part ownerField argument order remains");
}

const api = new Function(extractFunction("ownerField") + "\nreturn { ownerField };")();

function expect(actual, expected, label) {
  if (actual !== expected) {
    throw new Error(label + ": expected " + expected + ", got " + actual);
  }
}

expect(api.ownerField("Object", "Condition", "", "design"), "hasDesign",
  "Object -> design Condition");
expect(api.ownerField("Object", "Condition", "", "state"), "hasState",
  "Object -> state Condition");
expect(api.ownerField("Behavior", "Behavior", "function", "function"), "hasChild",
  "Behavior hierarchy");
expect(api.ownerField("Condition", "Condition", "state", "state"), "hasChild",
  "Condition hierarchy");

console.log("v0.8.19 folded Part relationship ownership regression: PASS");
