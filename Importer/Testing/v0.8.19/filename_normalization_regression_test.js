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
  extractFunction("trim2"),
  extractFunction("machineNoiseName"),
  extractFunction("sanitizeName"),
  "return { machineNoiseName, sanitizeName };"
].join("\n");
const api = new Function(code)();

function expect(actual, expected, label) {
  if (actual !== expected) {
    throw new Error(label + ": expected " + expected + ", got " + actual);
  }
}

const noisy = [
  "$inet",
  "$inet query",
  "https://example.com/search?q=charger",
  "www.example.com/path",
  "example.com/path?x=1",
  "search?q=charger",
  "result&query=charger",
  "C:\\Temp\\ea\\file.txt",
  "\\\\server\\share\\file.txt",
  "/Users/example/model/file.txt",
  "/home/example/model/file.txt",
  "/var/tmp/model/file.txt"
];

for (const value of noisy) {
  expect(api.machineNoiseName(value), true, "machine-noise detection for " + value);
}

const human = [
  "Battery charger",
  "CAN communication",
  "R&D Requirements",
  "Connector A to Connector B"
];

for (const value of human) {
  expect(api.machineNoiseName(value), false, "human-readable name retained for " + value);
}

// Filesystem sanitization must remove or replace unsafe filename characters.
expect(
  api.sanitizeName('A/B:C?D*E"F<G>H|I\\J'),
  "A-B -CDE''F(G)H-I-J",
  "unsafe filename characters normalized"
);

// Global uniqueness in the importer must remain case-insensitive.
if (!src.includes("usedFileNames.has(candidate.toLowerCase())")) {
  throw new Error("case-insensitive collision detection missing");
}
if (!src.includes("usedFileNames.add(candidate.toLowerCase())")) {
  throw new Error("case-insensitive collision reservation missing");
}

console.log("v0.8.19 filename normalization regression: PASS");
