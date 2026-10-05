#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

const importer = path.resolve(
  __dirname,
  "../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html"
);
const src = fs.readFileSync(importer, "utf8");

function need(text, label) {
  if (!src.includes(text)) throw new Error(label + ": missing " + text);
}
function forbid(text, label) {
  if (src.includes(text)) throw new Error(label + ": forbidden " + text);
}

// EA Port classification must remain contextual only.
need(
  'else{p.outcome="local endpoint";p.mdseType="";p.subtype="";p.rule="W-384";p.targetKey=q.resolvedKey||"";}',
  "EA Port contextual classification"
);
need(
  'return {key:"localendpoint:"+id,type:"Local Interface",sourceId:id,plan:p,contextualOnly:true};',
  "Port endpoint resolution"
);
need(
  "EA Ports are contextual Local Model Interfaces and never enter the note entity set.",
  "Port note exclusion comment"
);

// No first-class Port note semantics may reappear.
forbid('p.mdseType="Port"', "Port note classification");
forbid('mdseType==="Port"', "Port entity type");
forbid('hasPort', "hasPort relationship");
forbid('field="interfaces"', "legacy note-level Port interfaces");
forbid('"transmits"', "legacy note-level Port transmit relationship");
forbid('"receives"', "legacy note-level Port receive relationship");
forbid('"exchanges"', "legacy note-level Port exchange relationship");

// First-class reusable interface definitions remain valid Object/interface notes.
need(
  'if(INTERFACE_CLASS_STEREOTYPES.has(st)){p.subtype="interface";p.rule="W-384";}',
  "reusable Object/interface definition"
);

// Local Model must still render boundary/contextual interfaces.
need('lines.push("### Interfaces","");', "Local Model Interfaces section");

// Syntax check the embedded script.
const s1 = src.indexOf("<script>");
const s2 = src.lastIndexOf("</script>");
if (s1 < 0 || s2 < 0) throw new Error("embedded script missing");
new Function(src.slice(s1 + 8, s2));

console.log("v0.8.19 Port contextual-only regression: PASS");
