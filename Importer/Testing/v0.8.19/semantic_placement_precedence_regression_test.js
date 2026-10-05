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
  const brace = src.indexOf("{", start);
  if (brace < 0) throw new Error("Missing function body: " + name);

  let depth = 0, quote = null, escape = false;
  for (let i = brace; i < src.length; i++) {
    const ch = src[i];
    if (quote) {
      if (escape) escape = false;
      else if (ch === "\\") escape = true;
      else if (ch === quote) quote = null;
      continue;
    }
    if (ch === "'" || ch === '"' || ch === "`") { quote = ch; continue; }
    if (ch === "{") depth++;
    else if (ch === "}") {
      depth--;
      if (depth === 0) return src.slice(start, i + 1);
    }
  }
  throw new Error("Unterminated function: " + name);
}

const helperNames = ["str", "trim2", "containsPath", "requirementSubtype"];
const helperSource = helperNames.map(extractFunction).join("\n");
const requirementSubtype = new Function(
  helperSource + "\nreturn requirementSubtype;"
)();

function pkg(names) {
  return { vaultNames() { return names.slice(); } };
}

function expect(actual, expected, label) {
  if (actual !== expected) {
    throw new Error(label + ": expected " + expected + ", got " + actual);
  }
}

// Explicit stereotypes must beat conflicting folder context.
expect(
  requirementSubtype(
    { Stereotype: "functionalRequirement", Package_ID: 1 },
    pkg(["03 Product Requirement", "Engineering Requirements"])
  ),
  "functional",
  "functionalRequirement overrides Engineering Requirements folder"
);

expect(
  requirementSubtype(
    { Stereotype: "designConstraint", Package_ID: 2 },
    pkg(["03 Product Requirement", "Engineering Requirements"])
  ),
  "design",
  "designConstraint overrides Engineering Requirements folder"
);

// Folder context remains a valid fallback when no explicit semantic stereotype exists.
expect(
  requirementSubtype(
    { Stereotype: "", Package_ID: 3 },
    pkg(["03 Product Requirement", "Engineering Requirements"])
  ),
  "engineering",
  "Engineering Requirements folder fallback"
);

expect(
  requirementSubtype(
    { Stereotype: "", Package_ID: 4 },
    pkg(["03 Product Requirement", "Regulatory Requirements"])
  ),
  "standard",
  "Regulatory Requirements folder fallback"
);

if (!src.includes('// Explicit EA semantics take precedence over package/folder context.')) {
  throw new Error("Semantic precedence guard comment missing");
}

console.log("v0.8.19 semantic placement precedence regression: PASS");
