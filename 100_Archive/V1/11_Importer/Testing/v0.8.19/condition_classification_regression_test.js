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

const helperNames = ["str", "trim2", "isProductDesign", "conditionSubtype"];
const helperSource = helperNames.map(extractFunction).join("\n");
const conditionSubtype = new Function(
  helperSource + "\nreturn conditionSubtype;"
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

// An EA State in Product Design is a design condition.
expect(
  conditionSubtype(
    { Stereotype: "", Package_ID: 1 },
    pkg(["05 Product Design", "Power Stage"])
  ),
  "design",
  "State inside Product Design"
);

// An EA State elsewhere remains a state.
expect(
  conditionSubtype(
    { Stereotype: "", Package_ID: 2 },
    pkg(["02 Product Context"])
  ),
  "state",
  "ordinary State"
);

// Folder context must not silently turn a State into a Mode.
expect(
  conditionSubtype(
    { Stereotype: "mode", Package_ID: 3 },
    pkg(["02 Product Context"])
  ),
  "state",
  "State with mode-like stereotype"
);

// Integration guards for the explicit EA source element types.
if (!src.includes('} else if(t==="State"){\n      p.outcome="note";p.mdseType="Condition";p.subtype=conditionSubtype(raw,pkg);p.rule="W-384";')) {
  throw new Error("State -> Condition/state-or-design mapping missing");
}
if (!src.includes('} else if(t==="StateMachine"){\n      p.outcome="note";p.mdseType="Condition";p.subtype="state machine";p.rule="W-384";')) {
  throw new Error("StateMachine -> Condition/state machine mapping missing");
}
if (!src.includes('} else if(t==="Mode"){\n      p.outcome="note";p.mdseType="Condition";p.subtype="mode";p.rule="W-384";')) {
  throw new Error("Mode -> Condition/mode mapping missing");
}
if (src.includes('if(stereotypeIncludes(raw,"mode"))return "mode";')) {
  throw new Error("State stereotype must not silently become Mode");
}

console.log("v0.8.19 Condition classification regression: PASS");
