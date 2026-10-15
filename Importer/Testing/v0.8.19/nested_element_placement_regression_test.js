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

const code = [
  "function sanitizeName(v){ return String(v); }",
  extractFunction("elementParentChain"),
  extractFunction("pathPlanForEntity"),
  "return { elementParentChain, pathPlanForEntity };"
].join("\n");
const api = new Function(code)();

function entity(key, fileName, parentEntityKey) {
  return {
    key,
    fileName,
    parentEntityKey: parentEntityKey || "",
    vaultPath: "02 Product Context > System"
  };
}

const root = entity("root", "Parent", "");
const child = entity("child", "Child", "root");
const grandchild = entity("grandchild", "Grandchild", "child");
const sibling = entity("sibling", "Sibling", "root");

const entities = new Map([
  [root.key, root],
  [child.key, child],
  [grandchild.key, grandchild],
  [sibling.key, sibling]
]);

const folderMap = new Map([
  ["02 Product Context > System", "02 Product Context/System"]
]);

function expect(actual, expected, label) {
  if (actual !== expected) {
    throw new Error(label + ": expected '" + expected + "', got '" + actual + "'");
  }
}

expect(
  api.pathPlanForEntity(root, folderMap, entities).path,
  "02 Product Context/System/Parent/Parent.md",
  "root parent note lives inside its own folder"
);

expect(
  api.pathPlanForEntity(child, folderMap, entities).path,
  "02 Product Context/System/Parent/Child/Child.md",
  "nested parent note lives inside recursive child folder"
);

expect(
  api.pathPlanForEntity(grandchild, folderMap, entities).path,
  "02 Product Context/System/Parent/Child/Grandchild.md",
  "leaf grandchild lives under complete parent chain"
);

expect(
  api.pathPlanForEntity(sibling, folderMap, entities).path,
  "02 Product Context/System/Parent/Sibling.md",
  "leaf sibling remains beside nested parent folder"
);

const chain = api.elementParentChain(grandchild, entities).map(x => x.key).join(">");
expect(chain, "root>child", "parent chain ordering");

if (!src.includes("Parent/Parent.md beside Parent/Child.md")) {
  throw new Error("Nested placement contract comment missing from importer");
}

console.log("v0.8.19 nested element placement regression: PASS");
