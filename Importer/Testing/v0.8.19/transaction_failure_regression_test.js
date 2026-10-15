#!/usr/bin/env node
"use strict";

const fs = require("fs");
const path = require("path");
const vm = require("vm");

const importer = path.resolve(__dirname, "../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const src = fs.readFileSync(importer, "utf8");

function extractFunction(name) {
  const markers = [`async function ${name}(`, `function ${name}(`];
  let start = -1;
  for (const marker of markers) {
    start = src.indexOf(marker);
    if (start >= 0) break;
  }
  if (start < 0) throw new Error("Missing production function: " + name);
  const brace = src.indexOf("{", start);
  if (brace < 0) throw new Error("Malformed production function: " + name);
  let depth = 0, quote = null, esc = false;
  for (let i = brace; i < src.length; i++) {
    const ch = src[i];
    if (quote) {
      if (esc) { esc = false; continue; }
      if (ch === "\\") { esc = true; continue; }
      if (ch === quote) quote = null;
      continue;
    }
    if (ch === '"' || ch === "'" || ch === "`") { quote = ch; continue; }
    if (ch === "{") depth++;
    else if (ch === "}") {
      depth--;
      if (depth === 0) return src.slice(start, i + 1);
    }
  }
  throw new Error("Unterminated production function: " + name);
}

const names = [
  "dirFor",
  "transientFsStateError",
  "fsRetryPause",
  "fsWrappedError",
  "fileExists",
  "writeTextPath",
  "readTextPath",
  "importStateText",
  "writeImportState",
  "assertFreshImportDestination",
  "runImportTransaction",
];

const context = {
  console,
  setTimeout,
  BUILD: { name: "EA to MDSE Native Importer", version: "0.8.19" },
  MDSE_RELEASE: "0.8.0",
  IMPORT_STATE_PATH: "99_System/11_Import/Import State.json",
};
vm.createContext(context);
vm.runInContext(
  names.map(extractFunction).join("\n") +
  "\nthis.__api={fileExists,writeTextPath,readTextPath,assertFreshImportDestination,runImportTransaction};",
  context,
  { filename: "v0.8.19-transaction-production-functions.js" }
);
const api = context.__api;

function notFound(message) {
  const e = new Error(message || "not found");
  e.name = "NotFoundError";
  return e;
}

class FakeFileHandle {
  constructor(root, path, node) {
    this.kind = "file";
    this.root = root;
    this.path = path;
    this.node = node;
  }
  async getFile() {
    const node = this.node;
    return { text: async () => String(node.content ?? "") };
  }
  async createWritable() {
    const root = this.root, node = this.node, path = this.path;
    let pending = ""; // createWritable() defaults to keepExistingData: false
    return {
      async write(data) {
        if (root.failPredicate && root.failPredicate(path, data)) {
          const e = new Error("injected write failure: " + path);
          e.name = "InjectedWriteError";
          throw e;
        }
        pending = data;
      },
      async close() { node.content = pending; },
      async abort() {},
    };
  }
}

class FakeDirHandle {
  constructor(root, path = "") {
    this.kind = "directory";
    this.root = root;
    this.path = path;
    this.children = new Map();
  }
  childPath(name) { return this.path ? this.path + "/" + name : name; }
  async getDirectoryHandle(name, opts = {}) {
    const existing = this.children.get(name);
    if (existing) {
      if (existing.kind !== "directory") throw new Error("not a directory: " + name);
      return existing;
    }
    if (!opts.create) throw notFound("directory: " + name);
    const d = new FakeDirHandle(this.root, this.childPath(name));
    this.children.set(name, d);
    return d;
  }
  async getFileHandle(name, opts = {}) {
    const existing = this.children.get(name);
    if (existing) {
      if (existing.kind !== "file") throw new Error("not a file: " + name);
      return new FakeFileHandle(this.root, this.childPath(name), existing);
    }
    if (!opts.create) throw notFound("file: " + name);
    const node = { kind: "file", content: "" };
    this.children.set(name, node);
    return new FakeFileHandle(this.root, this.childPath(name), node);
  }
}

function makeRoot() {
  const state = { failPredicate: null };
  const root = new FakeDirHandle(state, "");
  state.root = root;
  return { root, state };
}

async function readState(root) {
  return JSON.parse(await api.readTextPath(root, context.IMPORT_STATE_PATH));
}

function assertStatusSeparation(state, expectedWrite, label) {
  if (state.runStatus.source !== "SOURCE_PASS") throw new Error(label + ": source status changed");
  if (state.runStatus.plan !== "PLAN_PASS") throw new Error(label + ": plan status changed");
  if (state.runStatus.write !== expectedWrite) throw new Error(label + ": unexpected write status " + state.runStatus.write);
  if (state.runStatus.semantic !== "SEMANTIC_REVIEW_REQUIRED") throw new Error(label + ": semantic review status was conflated with write state");
  if (state.runStatus.acceptance !== "ACCEPTANCE_PENDING") throw new Error(label + ": acceptance status was conflated with write state");
}

const meta = {
  source: { name: "fixture.qeax", size: 123, sha256: "a".repeat(64) },
  scope: "WHOLE MODEL",
  startedAt: "2026-10-05T00:00:00.000Z",
  planned: { notes: 2, attachmentFiles: 0, evidenceFiles: 1 },
  runStatus: {
    source: "SOURCE_PASS",
    plan: "PLAN_PASS",
    semantic: "SEMANTIC_REVIEW_REQUIRED",
    acceptance: "ACCEPTANCE_PENDING",
  },
};

(async () => {
  // Successful transaction establishes the positive control.
  {
    const { root } = makeRoot();
    await api.assertFreshImportDestination(root);
    await api.runImportTransaction(root, meta, async () => {
      await api.writeTextPath(root, "Model/One.md", "one");
    });
    const state = await readState(root);
    if (state.status !== "IMPORT_COMPLETE") throw new Error("success path did not finalize IMPORT_COMPLETE");
    assertStatusSeparation(state, "WRITE_PASS", "success path");
  }

  // Inject a model-write failure after IN_PROGRESS. Production helper must persist FAILED.
  {
    const { root } = makeRoot();
    let thrown = null;
    try {
      await api.runImportTransaction(root, meta, async () => {
        await api.writeTextPath(root, "Model/One.md", "one");
        throw new Error("injected note/evidence write failure");
      });
    } catch (e) { thrown = e; }
    if (!thrown) throw new Error("injected transaction failure did not propagate");
    const state = await readState(root);
    if (state.status !== "IMPORT_FAILED") throw new Error("failed transaction did not persist IMPORT_FAILED");
    assertStatusSeparation(state, "WRITE_FAIL", "failed path");
    if (!state.failure || !/injected note\/evidence write failure/.test(state.failure.message || "")) {
      throw new Error("failed transaction did not preserve failure reason");
    }
    let rerunBlocked = false;
    try { await api.assertFreshImportDestination(root); } catch (e) { rerunBlocked = /already contains an import transaction state/.test(e.message); }
    if (!rerunBlocked) throw new Error("dirty failed destination was not refused on rerun");
  }

  // If persisting IMPORT_FAILED also fails, prior IN_PROGRESS must remain authoritative.
  {
    const { root, state: fsState } = makeRoot();
    fsState.failPredicate = (p, data) =>
      p === context.IMPORT_STATE_PATH &&
      typeof data === "string" &&
      data.includes('"status": "IMPORT_FAILED"');
    let thrown = null;
    try {
      await api.runImportTransaction(root, meta, async () => {
        throw new Error("injected body failure with failed state persistence");
      });
    } catch (e) { thrown = e; }
    if (!thrown) throw new Error("double-failure transaction did not propagate");
    if (!thrown.importStateWriteError) throw new Error("IMPORT_FAILED persistence error was not retained");
    const state = await readState(root);
    if (state.status !== "IMPORT_IN_PROGRESS") {
      throw new Error("failed failure-state write did not leave IMPORT_IN_PROGRESS authoritative");
    }
    assertStatusSeparation(state, "WRITE_IN_PROGRESS", "in-progress fallback");
    let rerunBlocked = false;
    try { await api.assertFreshImportDestination(root); } catch (e) { rerunBlocked = /already contains an import transaction state/.test(e.message); }
    if (!rerunBlocked) throw new Error("dirty in-progress destination was not refused on rerun");
  }

  console.log("IMP-001 transaction failure injection: PASS");
})().catch((e) => {
  console.error(e && e.stack ? e.stack : e);
  process.exit(1);
});
