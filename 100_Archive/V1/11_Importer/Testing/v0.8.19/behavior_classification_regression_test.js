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

  let depth = 0;
  let quote = null;
  let escape = false;
  for (let i = brace; i < src.length; i++) {
    const ch = src[i];

    if (quote) {
      if (escape) escape = false;
      else if (ch === "\\") escape = true;
      else if (ch === quote) quote = null;
      continue;
    }

    if (ch === "'" || ch === '"' || ch === "`") {
      quote = ch;
      continue;
    }
    if (ch === "{") depth++;
    else if (ch === "}") {
      depth--;
      if (depth === 0) return src.slice(start, i + 1);
    }
  }
  throw new Error("Unterminated function: " + name);
}

const helperNames = [
  "str",
  "trim2",
  "stereotypeTokens",
  "stereotypeIncludes",
  "behaviorSubtype"
];

const helperSource = helperNames.map(extractFunction).join("\n");
const behaviorSubtype = new Function(
  helperSource + "\nreturn behaviorSubtype;"
)();

function pkg(names) {
  return {
    vaultNames() {
      return names.slice();
    }
  };
}

function expect(actual, expected, label) {
  if (actual !== expected) {
    throw new Error(label + ": expected " + expected + ", got " + actual);
  }
}

// Explicit semantic stereotype wins regardless of package location.
expect(
  behaviorSubtype(
    { Stereotype: "function", Package_ID: 1 },
    pkg(["05 Product Design", "Unrelated Folder"])
  ),
  "function",
  "function stereotype outside Function folder"
);

// Stereotype matching is case-insensitive and works when multiple stereotypes exist.
expect(
  behaviorSubtype(
    { Stereotype: "SysML::FUNCTION;custom", Package_ID: 2 },
    pkg(["02 Product Context"])
  ),
  "function",
  "function stereotype token among multiple stereotypes"
);

// Legacy/location-only Function package still maps Activity to function.
expect(
  behaviorSubtype(
    { Stereotype: "", Package_ID: 3 },
    pkg(["04 Product Function"])
  ),
  "function",
  "Activity inside Function folder"
);

// Ordinary Activity remains Activity.
expect(
  behaviorSubtype(
    { Stereotype: "custom", Package_ID: 4 },
    pkg(["02 Product Context"])
  ),
  "activity",
  "ordinary Activity"
);

// Integration guards: EA Action and Step must remain Behavior subtypes.
if (!src.includes('} else if(t==="Action"){\n      p.outcome="note";p.mdseType="Behavior";p.subtype="action";p.rule="W-384";')) {
  throw new Error("Action -> Behavior/action mapping missing");
}
if (!src.includes('} else if(t==="Step"){\n      p.outcome="note";p.mdseType="Behavior";p.subtype="step";p.rule="W-384";')) {
  throw new Error("Step -> Behavior/step mapping missing");
}
if (!src.includes('else{p.mdseType="Behavior";p.subtype=behaviorSubtype(raw,pkg);p.rule="W-384";}')) {
  throw new Error("Activity -> Behavior classification does not call behaviorSubtype()");
}

console.log("v0.8.19 Behavior classification regression: PASS");
