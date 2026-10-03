import { test } from "node:test";
import assert from "node:assert/strict";
import { activationPlan, checkCode, compareVersions, deriveCode, evaluate, parseLock, summarize, type ReleaseState } from "../src/core";

test("author codes match the Author Registration Spec test cases", () => {
  const cases: [string, string, string][] = [
    ["Spencer", "Skelly", "skellyspencer"],
    ["Jesse", "Rivera", "riverajesse--"],
    ["Florian", "Koerfer", "koerferfloria"],
    ["Ray", "Virzi", "virziray-----"],
    ["Jürgen", "Müller", "mullerjurgen-"],
    ["Anna", "Weiß", "weissanna----"],
  ];
  for (const [f, l, c] of cases) assert.equal(deriveCode(f, l), c);
});

test("code uniqueness: reserved, taken, previous codes, and returning person", () => {
  const people = [
    { path: "99_System/04_People/Spencer Skelly.md", name: "Spencer Skelly", code: "skellyspencer", previousCodes: [] },
    { path: "99_System/04_People/Ray Virzi.md", name: "Ray Virzi", code: "virziray-----", previousCodes: ["virzir-------"] },
  ];
  const reserved = ["claudeai-----", "sparxeaauthor"];
  assert.equal(checkCode("BAD", "X Y", people, reserved).ok, false);
  assert.equal(checkCode("claudeai-----", "X Y", people, reserved).ok, false);
  assert.equal(checkCode("skellyspencer", "Sam Skelly", people, reserved).ok, false);
  assert.equal(checkCode("virzir-------", "Someone Else", people, reserved).ok, false);
  const back = checkCode("skellyspencer", "spencer  skelly", people, reserved);
  assert.ok(back.ok && back.existing?.path.endsWith("Spencer Skelly.md"));
  assert.deepEqual(checkCode("riverajesse--", "Jesse Rivera", people, reserved), { ok: true });
});

test("version comparison", () => {
  assert.equal(compareVersions("1.12.7", "1.12.7"), 0);
  assert.equal(compareVersions("1.12.10", "1.12.7"), 1);
  assert.equal(compareVersions("1.9", "1.12.7"), -1);
});

const LOCK = parseLock({
  schema: 2,
  obsidianMinVersion: "1.12.7",
  requiredCorePlugins: ["bases", "canvas"],
  disabledCorePlugins: ["templates"],
  plugins: {
    dataview: { version: "0.5.68", settings: "governed", sha256: { "main.js": "AA", "manifest.json": "bb", "data.json": "ee" } },
    "mdse-bootstrap": { version: "0.3.0", sha256: { "main.js": "cc", "manifest.json": "dd" } },
  },
});

function state(over: Partial<ReleaseState> = {}): ReleaseState {
  return {
    lock: LOCK,
    installed: {
      dataview: { version: "0.5.68", sha256: { "main.js": "aa", "manifest.json": "bb", "data.json": "ee" } },
      "mdse-bootstrap": { version: "0.3.0", sha256: { "main.js": "cc", "manifest.json": "dd" } },
    },
    enabled: new Set(["dataview", "mdse-bootstrap"]),
    present: new Set(["dataview", "mdse-bootstrap"]),
    appVersion: "1.12.7",
    coreEnabled: { bases: true, canvas: true, templates: false },
    mdseRelease: "0.8.0",
    vaultInitialized: true,
    isGitRepo: true,
    ...over,
  };
}

test("a vault that matches the lock has no problems", () => {
  const s = summarize(evaluate(state()));
  assert.deepEqual(s, { errors: 0, warnings: 0 });
});

test("drift is reported: changed file, wrong version, disabled, missing, extra plugin, old Obsidian, core plugins", () => {
  const f = evaluate(state({
    installed: {
      dataview: { version: "0.5.70", sha256: { "main.js": "ff", "manifest.json": "bb", "data.json": "00" } },
      "mdse-bootstrap": { version: null, sha256: { "main.js": null, "manifest.json": null } },
    },
    enabled: new Set(["dataview", "calendar"]),
    present: new Set(["dataview", "calendar", "kanban"]),
    appVersion: "1.11.0",
    coreEnabled: { bases: false, canvas: true, templates: true },
    mdseRelease: null,
    vaultInitialized: false,
    isGitRepo: false,
  }));
  const msg = (subject: string) => f.filter((x) => x.subject === subject).map((x) => `${x.level}:${x.message}`).join(" | ");
  assert.match(msg("dataview"), /^error:version 0\.5\.70, release pins 0\.5\.68; main\.js differs/);
  assert.match(msg("mdse-bootstrap"), /^error:missing/);
  assert.match(msg("calendar"), /warn:enabled but not part/);
  assert.match(msg("kanban"), /warn:installed but not part/);
  assert.match(msg("Obsidian"), /^error:1\.11\.0 is older/);
  assert.match(msg("bases"), /^error/);
  assert.match(msg("templates"), /^warn/);
  assert.match(msg("MDSE release"), /^error/);
  assert.match(msg("Vault identity"), /^warn/);
  assert.match(msg("Git"), /^warn/);
});

test("lock validation", () => {
  assert.throws(() => parseLock({ schema: 1, plugins: {} }), /schema 1/);
  assert.throws(() => parseLock({ schema: 2, plugins: { x: { version: "1", sha256: { "main.js": "a" } } } }), /must lock main\.js and manifest\.json/);
});


test("W-330 activation repair plans only enable locked/required and disable explicitly prohibited plugins", () => {
  const p = activationPlan(
    LOCK,
    new Set(["mdse-bootstrap", "calendar"]),
    { bases: false, canvas: true, templates: true },
  );
  assert.deepEqual(p, {
    enableCommunity: ["dataview"],
    enableCore: ["bases"],
    disableCore: ["templates"],
  });
});


test("governed settings hash drift is reported", () => {
  const f = evaluate(state({
    installed: {
      dataview: { version: "0.5.68", sha256: { "main.js": "aa", "manifest.json": "bb", "data.json": "ff" } },
      "mdse-bootstrap": { version: "0.3.0", sha256: { "main.js": "cc", "manifest.json": "dd" } },
    },
  }));
  assert.match(f.find((x) => x.subject === "dataview")?.message ?? "", /data\.json differs from the release/);
});
