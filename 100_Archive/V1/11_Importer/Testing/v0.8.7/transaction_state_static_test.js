#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");

const importer = path.resolve(__dirname, "../../Tools/v0.8.7/EA_to_MDSE_Native_Importer_v0.8.7.html");
const src = fs.readFileSync(importer, "utf8");

function mustContain(text, label) {
  if (!src.includes(text)) throw new Error("missing: " + label);
}
function order(a, b, label) {
  const ia = src.indexOf(a), ib = src.indexOf(b);
  if (ia < 0 || ib < 0 || ia >= ib) throw new Error("bad ordering: " + label);
}

mustContain('version: "0.8.7"', "v0.8.7 build");
mustContain('const IMPORT_STATE_PATH="99_System/11_Import/Import State.json"', "state path");
mustContain('await fileExists(outputDirHandle,IMPORT_STATE_PATH)', "dirty destination rejection");
mustContain('writeImportState(outputDirHandle,"IMPORT_IN_PROGRESS"', "transaction start");
mustContain('writeImportState(outputDirHandle,"IMPORT_FAILED"', "failure state");
mustContain('writeImportState(outputDirHandle,"IMPORT_COMPLETE"', "completion state");
mustContain('if(p!==RUN_MANIFEST_PATH)', "manifest excluded from early evidence loop");

order('writeImportState(outputDirHandle,"IMPORT_IN_PROGRESS"', 'el("sliceStatus").textContent="Writing "+fmt(files.length)+" notes"', "state before first model write");
order('for(const [p,t] of Object.entries(evidence))if(p!==RUN_MANIFEST_PATH)', 'await writeTextPath(outputDirHandle,RUN_MANIFEST_PATH,manifest)', "ordinary evidence before manifest");
order('await writeTextPath(outputDirHandle,RUN_MANIFEST_PATH,manifest)', 'writeImportState(outputDirHandle,"IMPORT_COMPLETE"', "manifest before completion");
order('writeImportState(outputDirHandle,"IMPORT_IN_PROGRESS"', 'writeImportState(outputDirHandle,"IMPORT_COMPLETE"', "start before complete");

console.log("v0.8.7 transaction-state static checks: PASS");
