#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

const importer = path.resolve(
  __dirname,
  "../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html"
);
const src = fs.readFileSync(importer, "utf8");

function extractFunction(name) {
  const start = src.indexOf("function " + name + "(");
  if (start < 0) throw new Error("Missing function: " + name);
  const next = src.indexOf("\nfunction ", start + 10);
  if (next < 0) throw new Error("Missing function boundary after: " + name);
  return src.slice(start, next).trim();
}

const code = [
  extractFunction("str"),
  extractFunction("canonicalMarkdownLf"),
  "return { canonicalMarkdownLf };"
].join("\n");
const api = new Function(code)();

function expect(actual, expected, label) {
  if (actual !== expected) {
    throw new Error(label + ": expected " + JSON.stringify(expected) + ", got " + JSON.stringify(actual));
  }
}

expect(api.canonicalMarkdownLf("a\r\nb\rc\nd"), "a\nb\nc\nd", "CRLF and CR normalize to LF");
expect(api.canonicalMarkdownLf("plain\ntext"), "plain\ntext", "existing LF is preserved");
expect(api.canonicalMarkdownLf(null), "", "null is normalized through importer string semantics");

const productionReturn = 'return canonicalMarkdownLf(lines.join("\\n")).replace(/\\n+$/,"")+"\\n";';
if (!src.includes(productionReturn)) {
  throw new Error("renderEntityMarkdown does not canonicalize final Markdown output");
}

// This reproduces the real-QEAX failure shape: generated LF structure with
// an EA narrative block that still carries CRLF internally.
const mixed = [
  "---",
  "type: \"Object\"",
  "---",
  "",
  "# Example",
  "",
  "EA line one\r\nEA line two",
  "",
  "## Local Model",
  "<!-- MDSE:LOCAL-MODEL START schema=0.4 -->",
  "",
  "### Interfaces",
  "",
  "#### P1",
  "- kind: port",
  "^ep-20231101140544000legaspichesca",
  "",
  "<!-- MDSE:LOCAL-MODEL END -->",
  ""
].join("\n");
const normalized = api.canonicalMarkdownLf(mixed).replace(/\n+$/, "") + "\n";
if (normalized.includes("\r")) throw new Error("canonical Markdown still contains carriage returns");
if (!normalized.includes("EA line one\nEA line two")) throw new Error("EA narrative line structure was not preserved");
if (!normalized.includes("<!-- MDSE:LOCAL-MODEL START schema=0.4 -->")) throw new Error("Local Model content changed unexpectedly");

console.log("v0.8.19 canonical Markdown line-ending regression: PASS");
