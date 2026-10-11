#!/usr/bin/env node
"use strict";
// Candidate consolidation scanner. Does not alter the existing release checker.
// Lists paths only; Git tracked files, no remote fetch or model-content output.
const { spawnSync } = require("node:child_process");
const fs = require("node:fs");
const path = require("node:path");
const LEGACY = ["spencerskelly", "MDSE_Workbench"].join("/");
const CURRENT_DOCS = new Set([
  "README.md", "AGENTS.md", "55_Workbench/README.md",
  "00_Workspace/00 - Current State.md",
  "00_Workspace/MDSE Tool Definitions and Boundaries.md",
  "Base Vault/Definition/mdse-release.yaml",
  "66_Testing/migration-path-plan.json",
]);
const AUDIT_SELF = new Set([
  "66_Testing/check_release_alignment.py",
  "66_Testing/consolidation/audit_workbench_authority.cjs",
  "66_Testing/consolidation/test_workbench_authority.cjs",
]);
const HISTORICAL_PREFIXES = [
  "00_Workspace/History/", "Importer/History/", "55_Workbench/docs/Reference/ARCHIVE_",
  "55_Workbench/docs/bom/a01-a14/", "55_Workbench/docs/bom/History/",
  "00_Workspace/GitHub Consolidation Step ", "00_Workspace/Consolidation Step ",
];
function classify(relativePath) {
  const p = relativePath.replace(/\\/g, "/").replace(/^\.\//, "");
  // Exact current docs and root CI take precedence over history exemptions.
  if (CURRENT_DOCS.has(p) || p.startsWith(".github/workflows/")) return "blocking";
  if (AUDIT_SELF.has(p)) return "detector";
  if (HISTORICAL_PREFIXES.some(prefix => p.startsWith(prefix))) return "historical";
  if (/\.(?:cjs|mjs|js|jsx|ts|tsx|py|sh|ps1|ya?ml|json|toml|ini)$/i.test(p)) return "blocking";
  return "needs_review";
}
function classifyPaths(paths) {
  const classified = { blocking: [], needs_review: [], historical: [], detector: [] };
  for (const p of [...new Set(paths)].sort()) classified[classify(p)].push(p);
  return classified;
}
function gitTrackedMatches(root, term = LEGACY) {
  const out = spawnSync("git", ["-C", root, "grep", "-I", "-l", "-z", "-F", "-e", term, "--", "."], {encoding:"buffer",maxBuffer:32*1024*1024});
  if (out.error) throw out.error;
  if (out.status === 1) return [];
  if (out.status !== 0) throw new Error("git grep failed: " + (out.stderr || Buffer.alloc(0)).toString("utf8").slice(0,300));
  return out.stdout.toString("utf8").split("\0").filter(Boolean).map(p => p.replace(/^\.\//, ""));
}
function audit(root) {
  const paths = gitTrackedMatches(root);
  const categories = classifyPaths(paths);
  return {schema:"mdse-workbench-authority-reference-audit/1",term:LEGACY,root:".",
    counts:Object.fromEntries(Object.entries(categories).map(([k,v])=>[k,v.length])),
    categories, strictReady:categories.blocking.length === 0 && categories.needs_review.length === 0,
    note:"Detector self-references and explicitly historical citations are informational only. Strict mode does not waive active paths."};
}
function main(args) {
  let root=".", output=null, strict=false;
  for(let i=0;i<args.length;i++) {
    if(args[i]==="--root" && args[i+1]) root=args[++i];
    else if(args[i]==="--output" && args[i+1]) output=args[++i];
    else if(args[i]==="--strict") strict=true;
    else throw new Error("Usage: node audit_workbench_authority.cjs [--root DIRECTORY] [--output JSON] [--strict]");
  }
  const doc=audit(path.resolve(root)); const s=JSON.stringify(doc,null,2)+"\n";
  if(output) fs.writeFileSync(output,s,"utf8");
  else process.stdout.write(s);
  return strict&&!doc.strictReady ? 2 : 0;
}
if(require.main===module) {try{process.exitCode=main(process.argv.slice(2));}catch(e){console.error(e.message);process.exitCode=3;}}
module.exports={LEGACY,classify,classifyPaths,gitTrackedMatches,audit,main};
