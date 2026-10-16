/**
 * MDSE Bootstrap core (W-322). Pure functions only: no Obsidian imports, so they run under node:test.
 *
 * The runtime authority is the vault's `.obsidian/plugin-lock.yaml` (schema 2). Bootstrap never downloads,
 * replaces, or updates plugin code or governed settings; the controlled release ships those files. It may safely
 * repair activation state by enabling locked community plugins, enabling required core plugins, and disabling
 * explicitly prohibited core plugins, then reports remaining drift and registers the author code (W-330).
 */

export type Level = "ok" | "warn" | "error";

export interface Finding {
  level: Level;
  area: "release" | "obsidian" | "plugin" | "core" | "git" | "author";
  subject: string;
  message: string;
}

export interface LockedPlugin {
  version: string;
  source?: string;
  settings?: "governed" | "default";
  sha256: Record<string, string>;
}

export interface PluginLock {
  schema: number;
  obsidianMinVersion?: string;
  requiredCorePlugins: string[];
  disabledCorePlugins: string[];
  plugins: Record<string, LockedPlugin>;
}

export interface InstalledPlugin {
  /** Version in the plugin's manifest.json on disk, or null when the folder or manifest is missing. */
  version: string | null;
  /** SHA-256 per locked file name; null when the file is missing. */
  sha256: Record<string, string | null>;
}

export interface ActivationPlan {
  enableCommunity: string[];
  enableCore: string[];
  disableCore: string[];
}

/** W-330: repair activation only. Never add/remove plugin files and never rewrite governed settings. */
export function installedMatchesLock(plugin: LockedPlugin, installed: InstalledPlugin | undefined): boolean {
  if (!installed || installed.version !== plugin.version) return false;
  for (const [file, want] of Object.entries(plugin.sha256)) {
    const got = installed.sha256[file];
    if (!got || got.toLowerCase() !== want.toLowerCase()) return false;
  }
  return true;
}

export function activationPlan(
  lock: PluginLock,
  enabled: Set<string>,
  coreEnabled: Record<string, boolean>,
  installed: Record<string, InstalledPlugin>,
): ActivationPlan {
  return {
    enableCommunity: Object.entries(lock.plugins)
      .filter(([id, plugin]) => !enabled.has(id) && installedMatchesLock(plugin, installed[id]))
      .map(([id]) => id)
      .sort(),
    enableCore: lock.requiredCorePlugins.filter((id) => !coreEnabled[id]).sort(),
    disableCore: lock.disabledCorePlugins.filter((id) => !!coreEnabled[id]).sort(),
  };
}

export interface ReleaseState {
  lock: PluginLock;
  installed: Record<string, InstalledPlugin>;
  enabled: Set<string>;
  /** Community plugin ids present on disk (manifests Obsidian knows about). */
  present: Set<string>;
  appVersion: string;
  coreEnabled: Record<string, boolean>;
  mdseRelease: string | null;
  vaultInitialized: boolean;
  isGitRepo: boolean;
}

const CODE_RE = /^[a-z-]{13}$/;

/** Author code rule (W-10, W-24): last name + first name, accents removed, ß→ss, a–z only, cut to 13, padded with '-'. */
export function deriveCode(first: string, last: string): string {
  const letters = (s: string) =>
    String(s || "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .replace(/ß/g, "ss")
      .toLowerCase()
      .replace(/[^a-z]/g, "");
  return (letters(last) + letters(first)).slice(0, 13).padEnd(13, "-");
}

export function isValidCode(code: string): boolean {
  return CODE_RE.test(code) && code.replace(/-/g, "").length > 0;
}

/** Numeric dotted-version comparison; non-numeric parts compare as 0. */
export function compareVersions(a: string, b: string): number {
  const pa = a.split(".").map((x) => parseInt(x, 10) || 0);
  const pb = b.split(".").map((x) => parseInt(x, 10) || 0);
  for (let i = 0; i < Math.max(pa.length, pb.length); i++) {
    const d = (pa[i] ?? 0) - (pb[i] ?? 0);
    if (d !== 0) return d < 0 ? -1 : 1;
  }
  return 0;
}

/** Validates the parsed YAML of plugin-lock.yaml. Throws with a readable message when it is not schema 2. */
export function parseLock(raw: unknown): PluginLock {
  const r = raw as Record<string, unknown> | null;
  if (!r || typeof r !== "object") throw new Error("plugin-lock.yaml is empty or not a mapping");
  if (r.schema !== 2) throw new Error(`plugin-lock.yaml schema ${String(r.schema)} is not supported (expected 2)`);
  const plugins = r.plugins as Record<string, unknown> | undefined;
  if (!plugins || typeof plugins !== "object") throw new Error("plugin-lock.yaml has no plugins");
  const out: Record<string, LockedPlugin> = {};
  for (const [id, v] of Object.entries(plugins)) {
    const p = v as Record<string, unknown>;
    if (!p || typeof p.version !== "string") throw new Error(`plugin-lock.yaml: ${id} has no version`);
    const sha = (p.sha256 ?? {}) as Record<string, unknown>;
    const hashes: Record<string, string> = {};
    for (const [f, h] of Object.entries(sha)) if (typeof h === "string") hashes[f] = h.toLowerCase();
    if (!hashes["main.js"] || !hashes["manifest.json"]) throw new Error(`plugin-lock.yaml: ${id} must lock main.js and manifest.json`);
    out[id] = {
      version: p.version,
      source: typeof p.source === "string" ? p.source : undefined,
      settings: p.settings === "governed" ? "governed" : "default",
      sha256: hashes,
    };
  }
  const list = (k: string) => (Array.isArray(r[k]) ? (r[k] as unknown[]).map(String) : []);
  return {
    schema: 2,
    obsidianMinVersion: typeof r.obsidianMinVersion === "string" ? r.obsidianMinVersion : undefined,
    requiredCorePlugins: list("requiredCorePlugins"),
    disabledCorePlugins: list("disabledCorePlugins"),
    plugins: out,
  };
}

/** Compares the running vault with the lock. Returns every finding, ok ones included, in display order. */
export function evaluate(s: ReleaseState): Finding[] {
  const f: Finding[] = [];
  const add = (level: Level, area: Finding["area"], subject: string, message: string) => f.push({ level, area, subject, message });

  add(s.mdseRelease ? "ok" : "error", "release", "MDSE release", s.mdseRelease ? `mdse_release ${s.mdseRelease}` : ".vault.yaml has no mdse_release");
  add(s.vaultInitialized ? "ok" : "warn", "release", "Vault identity", s.vaultInitialized ? "vault_uid set" : "vault_uid is UNINITIALIZED; the release owner initializes it once with Initialize-Vault before sharing");

  if (s.lock.obsidianMinVersion) {
    const okApp = compareVersions(s.appVersion, s.lock.obsidianMinVersion) >= 0;
    add(okApp ? "ok" : "error", "obsidian", "Obsidian", okApp ? `${s.appVersion}` : `${s.appVersion} is older than the required ${s.lock.obsidianMinVersion}; update Obsidian`);
  }

  for (const [id, p] of Object.entries(s.lock.plugins)) {
    const inst = s.installed[id];
    if (!inst || inst.version === null) {
      add("error", "plugin", id, "missing from .obsidian/plugins; pull the vault again or restore it from Git");
      continue;
    }
    const problems: string[] = [];
    if (inst.version !== p.version) problems.push(`version ${inst.version}, release pins ${p.version}`);
    for (const [file, want] of Object.entries(p.sha256)) {
      const got = inst.sha256[file];
      if (got === null || got === undefined) problems.push(`${file} missing`);
      else if (got.toLowerCase() !== want) problems.push(`${file} differs from the release`);
    }
    if (!s.enabled.has(id)) problems.push("not enabled");
    if (problems.length) add("error", "plugin", id, problems.join("; ") + ". Do not update plugins yourself; restore the vault's copy with Git.");
    else add("ok", "plugin", id, p.version);
  }
  for (const id of [...s.enabled].sort()) {
    if (!s.lock.plugins[id]) add("warn", "plugin", id, "enabled but not part of the controlled release");
  }
  for (const id of [...s.present].sort()) {
    if (!s.lock.plugins[id] && !s.enabled.has(id)) add("warn", "plugin", id, "installed but not part of the controlled release");
  }

  for (const id of s.lock.requiredCorePlugins) {
    const on = !!s.coreEnabled[id];
    add(on ? "ok" : "error", "core", id, on ? "enabled" : "core plugin must be enabled");
  }
  for (const id of s.lock.disabledCorePlugins) {
    const on = !!s.coreEnabled[id];
    add(on ? "error" : "ok", "core", id, on ? "core plugin must be off (use Templater for templates)" : "off");
  }

  add(s.isGitRepo ? "ok" : "warn", "git", "Git", s.isGitRepo ? "vault is a Git repository" : "vault is not a Git repository; changes cannot be shared");
  return f;
}

export function summarize(findings: Finding[]): { errors: number; warnings: number } {
  return {
    errors: findings.filter((x) => x.level === "error").length,
    warnings: findings.filter((x) => x.level === "warn").length,
  };
}

export interface PersonRecord {
  path: string;
  name: string;
  code: string;
  previousCodes: string[];
}

export type CodeCheck =
  | { ok: true; existing?: PersonRecord }
  | { ok: false; reason: string };

/**
 * Spec step 4: a code must match ^[a-z-]{13}$ and not belong to anyone else (person `code` or `previousCodes`,
 * AI codes, the unmapped-EA code). A person re-registering on a new computer (same name as an existing person
 * note holding this code) is accepted and told their note already exists.
 */
export function checkCode(code: string, fullName: string, people: PersonRecord[], reserved: string[]): CodeCheck {
  if (!isValidCode(code)) return { ok: false, reason: "A code is exactly 13 characters: lowercase a–z and '-'." };
  if (reserved.includes(code)) return { ok: false, reason: `${code} is reserved for an AI tool or the EA import.` };
  const norm = (s: string) => s.trim().toLowerCase().replace(/\s+/g, " ");
  for (const p of people) {
    const owns = p.code === code || p.previousCodes.includes(code);
    if (!owns) continue;
    if (norm(p.name) === norm(fullName) && p.code === code) return { ok: true, existing: p };
    return { ok: false, reason: `${code} is already used by ${p.name || p.path}. Choose another.` };
  }
  return { ok: true };
}

export function hex(buf: ArrayBuffer): string {
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");
}
