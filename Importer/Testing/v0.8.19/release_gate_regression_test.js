#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const cp = require("child_process");

const here = __dirname;
const importer = path.resolve(here, "../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const src = fs.readFileSync(importer, "utf8");

const focused = [
  "taxonomy_local_model_04_static_test.js",
  "behavior_classification_regression_test.js",
  "condition_classification_regression_test.js",
  "semantic_placement_precedence_regression_test.js",
  "nested_element_placement_regression_test.js",
  "path_planning_scalability_regression_test.js",
  "filename_normalization_regression_test.js",
  "canonical_markdown_line_endings_regression_test.js",
  "port_contextual_only_regression_test.js",
  "local_model_parts_interfaces_regression_test.js",
  "folded_part_relationship_regression_test.js",
  "interface_flowproperty_carrier_regression_test.js",
  "contextual_connections_regression_test.js",
  "exposes_regression_test.js",
  "conveyed_flow_allocation_regression_test.js",
  "common_context_connection_ownership_regression_test.js",
  "part_terminated_flow_review_regression_test.js",
  "definitionless_interface_accounting_regression_test.js",
  "canonical_relationship_boundary_regression_test.js",
  "source_fingerprint_regression_test.js",
  "source_profile_regression_test.js",
  "table_disposition_regression_test.js",
  "transaction_failure_regression_test.js"
];

for (const name of focused) {
  const file = path.join(here, name);
  if (!fs.existsSync(file)) throw new Error("Missing v0.8.19 release-gate test: " + name);
  cp.execFileSync(process.execPath, [file], { stdio: "inherit" });
}

function need(text, label) {
  if (!src.includes(text)) throw new Error(label + ": missing " + text);
}

// Source row loss is release-blocking at planner time.
need('severity:"fail",code:"ELEMENT_RULE_COVERAGE"', "unmapped element failure");
need('severity:"fail",code:"CONNECTOR_RULE_COVERAGE"', "unmapped connector failure");
need('severity:"fail",code:"ELEMENT_ROW_COVERAGE"', "element row reconciliation failure");
need('severity:"fail",code:"CONNECTOR_ROW_COVERAGE"', "connector row reconciliation failure");

// Conveyed-flow loss is release-blocking before any model write.
need("if(localModel.stats.unresolvedConveyedXrefs){", "unresolved conveyed-flow gate");
need("flow reconciliation is incomplete.", "conveyed-flow failure message");

// Deterministic local identities and duplicate checks remain part of the write gate.
need('errors.push("global identity token collision: "+m[2]);', "global local-identity collision check");
need('errors.push("duplicate local ID under "+owner+": "+id);', "local duplicate identity check");

const s1 = src.indexOf("<script>"), s2 = src.lastIndexOf("</script>");
if (s1 < 0 || s2 < 0) throw new Error("embedded script missing");
new Function(src.slice(s1 + 8, s2));

console.log("v0.8.19 aggregate release gate: PASS");
