"use strict";
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// src/main.ts
var main_exports = {};
__export(main_exports, {
  default: () => MdseBootstrap
});
module.exports = __toCommonJS(main_exports);
var import_obsidian = require("obsidian");

// src/core.ts
function installedMatchesLock(plugin, installed) {
  if (!installed || installed.version !== plugin.version) return false;
  for (const [file, want] of Object.entries(plugin.sha256)) {
    const got = installed.sha256[file];
    if (!got || got.toLowerCase() !== want.toLowerCase()) return false;
  }
  return true;
}
function activationPlan(lock, enabled, coreEnabled, installed) {
  return {
    enableCommunity: Object.entries(lock.plugins).filter(([id, plugin]) => !enabled.has(id) && installedMatchesLock(plugin, installed[id])).map(([id]) => id).sort(),
    enableCore: lock.requiredCorePlugins.filter((id) => !coreEnabled[id]).sort(),
    disableCore: lock.disabledCorePlugins.filter((id) => !!coreEnabled[id]).sort()
  };
}
var CODE_RE = /^[a-z-]{13}$/;
function deriveCode(first, last) {
  const letters = (s) => String(s || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ß/g, "ss").toLowerCase().replace(/[^a-z]/g, "");
  return (letters(last) + letters(first)).slice(0, 13).padEnd(13, "-");
}
function isValidCode(code) {
  return CODE_RE.test(code) && code.replace(/-/g, "").length > 0;
}
function compareVersions(a, b) {
  const pa = a.split(".").map((x) => parseInt(x, 10) || 0);
  const pb = b.split(".").map((x) => parseInt(x, 10) || 0);
  for (let i = 0; i < Math.max(pa.length, pb.length); i++) {
    const d = (pa[i] ?? 0) - (pb[i] ?? 0);
    if (d !== 0) return d < 0 ? -1 : 1;
  }
  return 0;
}
function parseLock(raw) {
  const r = raw;
  if (!r || typeof r !== "object") throw new Error("plugin-lock.yaml is empty or not a mapping");
  if (r.schema !== 2) throw new Error(`plugin-lock.yaml schema ${String(r.schema)} is not supported (expected 2)`);
  const plugins = r.plugins;
  if (!plugins || typeof plugins !== "object") throw new Error("plugin-lock.yaml has no plugins");
  const out = {};
  for (const [id, v] of Object.entries(plugins)) {
    const p = v;
    if (!p || typeof p.version !== "string") throw new Error(`plugin-lock.yaml: ${id} has no version`);
    const sha = p.sha256 ?? {};
    const hashes = {};
    for (const [f, h] of Object.entries(sha)) if (typeof h === "string") hashes[f] = h.toLowerCase();
    if (!hashes["main.js"] || !hashes["manifest.json"]) throw new Error(`plugin-lock.yaml: ${id} must lock main.js and manifest.json`);
    out[id] = {
      version: p.version,
      source: typeof p.source === "string" ? p.source : void 0,
      settings: p.settings === "governed" ? "governed" : "default",
      sha256: hashes
    };
  }
  const list = (k) => Array.isArray(r[k]) ? r[k].map(String) : [];
  return {
    schema: 2,
    obsidianMinVersion: typeof r.obsidianMinVersion === "string" ? r.obsidianMinVersion : void 0,
    requiredCorePlugins: list("requiredCorePlugins"),
    disabledCorePlugins: list("disabledCorePlugins"),
    plugins: out
  };
}
function evaluate(s) {
  const f = [];
  const add = (level, area, subject, message) => f.push({ level, area, subject, message });
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
    const problems = [];
    if (inst.version !== p.version) problems.push(`version ${inst.version}, release pins ${p.version}`);
    for (const [file, want] of Object.entries(p.sha256)) {
      const got = inst.sha256[file];
      if (got === null || got === void 0) problems.push(`${file} missing`);
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
function summarize(findings) {
  return {
    errors: findings.filter((x) => x.level === "error").length,
    warnings: findings.filter((x) => x.level === "warn").length
  };
}
function checkCode(code, fullName, people, reserved) {
  if (!isValidCode(code)) return { ok: false, reason: "A code is exactly 13 characters: lowercase a\u2013z and '-'." };
  if (reserved.includes(code)) return { ok: false, reason: `${code} is reserved for an AI tool or the EA import.` };
  const norm = (s) => s.trim().toLowerCase().replace(/\s+/g, " ");
  for (const p of people) {
    const owns = p.code === code || p.previousCodes.includes(code);
    if (!owns) continue;
    if (norm(p.name) === norm(fullName) && p.code === code) return { ok: true, existing: p };
    return { ok: false, reason: `${code} is already used by ${p.name || p.path}. Choose another.` };
  }
  return { ok: true };
}
function hex(buf) {
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

// src/main.ts
var CODE_FILE = ".obsidian/author-code.txt";
var PEOPLE = "99_System/04_People";
var PERSON_TEMPLATE = "99_System/05_Templates/Person.md";
var AUTHORS = "99_System/03_Schemas/authors.yaml";
var START_DELAY_MS = 4e3;
var MdseBootstrap = class extends import_obsidian.Plugin {
  constructor() {
    super(...arguments);
    this.status = null;
    this.last = [];
  }
  async onload() {
    this.status = this.addStatusBarItem();
    this.status.setText("MDSE: checking\u2026");
    this.status.addClass("mod-clickable");
    this.registerDomEvent(this.status, "click", () => new CheckModal(this.app, this.last, async () => {
      await this.repairActivation();
      return this.runCheck(true);
    }).open());
    this.addCommand({ id: "show-release-check", name: "Show release check", callback: async () => {
      await this.repairActivation();
      await this.runCheck(false);
      new CheckModal(this.app, this.last, async () => {
        await this.repairActivation();
        return this.runCheck(true);
      }).open();
    } });
    this.addCommand({ id: "register-author", name: "Register author code", callback: () => this.openRegistration(true) });
    this.app.workspace.onLayoutReady(() => {
      window.setTimeout(async () => {
        await this.repairActivation();
        await this.runCheck(true);
        if (!await this.readCode()) this.openRegistration(false);
      }, START_DELAY_MS);
    });
  }
  plugins() {
    return this.app.plugins;
  }
  internalPlugins() {
    return this.app.internalPlugins;
  }
  async scanInstalled(lock) {
    const a = this.app.vault.adapter;
    const cfg = this.app.vault.configDir;
    const installed = {};
    for (const [id, p] of Object.entries(lock.plugins)) {
      const dir = (0, import_obsidian.normalizePath)(`${cfg}/plugins/${id}`);
      let version = null;
      try {
        version = String(JSON.parse(await a.read(`${dir}/manifest.json`)).version);
      } catch {
        version = null;
      }
      const sha256 = {};
      for (const file of Object.keys(p.sha256)) {
        try {
          sha256[file] = hex(await crypto.subtle.digest("SHA-256", await a.readBinary(`${dir}/${file}`)));
        } catch {
          sha256[file] = null;
        }
      }
      installed[id] = { version, sha256 };
    }
    return installed;
  }
  async repairActivation() {
    try {
      const a = this.app.vault.adapter;
      const cfg = this.app.vault.configDir;
      const lock = parseLock((0, import_obsidian.parseYaml)(await a.read((0, import_obsidian.normalizePath)(`${cfg}/plugin-lock.yaml`))));
      const internal = this.internalPlugins();
      const coreEnabled = {};
      for (const id of [...lock.requiredCorePlugins, ...lock.disabledCorePlugins]) coreEnabled[id] = !!internal.getPluginById(id)?.enabled;
      const installed = await this.scanInstalled(lock);
      const plan = activationPlan(lock, new Set(this.plugins().enabledPlugins), coreEnabled, installed);
      for (const id of plan.enableCommunity) {
        const plugins = this.plugins();
        if (typeof plugins.enablePluginAndSave === "function") await plugins.enablePluginAndSave(id);
        else if (typeof plugins.enablePlugin === "function") await plugins.enablePlugin(id);
      }
      for (const id of plan.enableCore) {
        if (typeof internal.enablePlugin === "function") await internal.enablePlugin(id);
      }
      for (const id of plan.disableCore) {
        if (typeof internal.disablePlugin === "function") await internal.disablePlugin(id);
      }
    } catch {
    }
  }
  async runCheck(notify) {
    const a = this.app.vault.adapter;
    const cfg = this.app.vault.configDir;
    let findings;
    try {
      const lock = parseLock((0, import_obsidian.parseYaml)(await a.read((0, import_obsidian.normalizePath)(`${cfg}/plugin-lock.yaml`))));
      const installed = await this.scanInstalled(lock);
      let vaultText = "";
      try {
        vaultText = await a.read(".vault.yaml");
      } catch {
      }
      const rel = /^mdse_release:\s*["']?([^"'#\r\n]+)/m.exec(vaultText);
      const internal = this.internalPlugins();
      const coreEnabled = {};
      for (const id of [...lock.requiredCorePlugins, ...lock.disabledCorePlugins]) coreEnabled[id] = !!internal.getPluginById(id)?.enabled;
      const state = {
        lock,
        installed,
        enabled: new Set(this.plugins().enabledPlugins),
        present: new Set(Object.keys(this.plugins().manifests)),
        appVersion: import_obsidian.apiVersion,
        coreEnabled,
        mdseRelease: rel ? rel[1].trim() : null,
        vaultInitialized: !!vaultText && !/vault_uid:\s*UNINITIALIZED/.test(vaultText),
        isGitRepo: await a.exists(".git")
      };
      findings = evaluate(state);
      const code = await this.readCode();
      findings.push(code ? { level: "ok", area: "author", subject: "Author code", message: code } : { level: "warn", area: "author", subject: "Author code", message: "not registered on this computer; run \u201CMDSE Bootstrap: Register author code\u201D" });
    } catch (e) {
      findings = [{ level: "error", area: "release", subject: "plugin-lock.yaml", message: e.message }];
    }
    this.last = findings;
    const { errors, warnings } = summarize(findings);
    this.status?.setText(errors ? `MDSE: ${errors} problem${errors > 1 ? "s" : ""}` : warnings ? `MDSE: ${warnings} warning${warnings > 1 ? "s" : ""}` : "MDSE: release OK");
    if (notify && errors) new import_obsidian.Notice(`MDSE Bootstrap: ${errors} release problem${errors > 1 ? "s" : ""}. Click \u201CMDSE\u201D in the status bar for details.`, 1e4);
    return findings;
  }
  async readCode() {
    try {
      const c = (await this.app.vault.adapter.read(CODE_FILE)).trim();
      return isValidCode(c) ? c : null;
    } catch {
      return null;
    }
  }
  people() {
    const out = [];
    for (const f of this.app.vault.getMarkdownFiles()) {
      if (!f.path.startsWith(PEOPLE + "/")) continue;
      const fm = this.app.metadataCache.getFileCache(f)?.frontmatter ?? {};
      const prev = Array.isArray(fm.previousCodes) ? fm.previousCodes.map(String) : [];
      out.push({ path: f.path, name: String(fm.name ?? f.basename), code: String(fm.code ?? ""), previousCodes: prev });
    }
    return out;
  }
  async reserved() {
    try {
      const y = (0, import_obsidian.parseYaml)(await this.app.vault.adapter.read(AUTHORS));
      return [...(y.ai_authors ?? []).map((x) => String(x.code ?? "")), String(y.unmapped?.code ?? "")].filter(Boolean);
    } catch {
      return [];
    }
  }
  async openRegistration(manual) {
    const existing = await this.readCode();
    if (existing && !manual) return;
    new RegisterModal(this.app, this, existing).open();
  }
  /** Spec steps 5 to 7. */
  async registerAuthor(first, last, code) {
    await this.app.vault.adapter.write(CODE_FILE, code);
    const fullName = `${first.trim()} ${last.trim()}`.replace(/\s+/g, " ");
    const already = this.people().find((p) => p.code === code || p.name.toLowerCase() === fullName.toLowerCase());
    if (already) {
      await this.runCheck(false);
      return `Author code ${code} saved on this computer. Your person note already exists (${already.path}).`;
    }
    const tp = this.plugins().plugins["templater-obsidian"];
    const template = this.app.vault.getAbstractFileByPath(PERSON_TEMPLATE);
    const folder = this.app.vault.getAbstractFileByPath(PEOPLE);
    if (!tp?.templater || !(template instanceof import_obsidian.TFile) || !(folder instanceof import_obsidian.TFolder)) {
      await this.runCheck(false);
      return `Author code ${code} saved, but the person note could not be created (Templater or the Person template is missing). Run the release check.`;
    }
    const note = await tp.templater.create_new_note_from_template(template, folder, fullName, false);
    if (!note) return `Author code ${code} saved, but Templater did not create the person note.`;
    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || "";
    await this.app.fileManager.processFrontMatter(note, (fm) => {
      fm.code = code;
      fm.name = fullName;
      fm.timezone = tz;
    });
    await this.runCheck(false);
    return `Registered ${fullName} as ${code} and created ${note.path}. Commit and sync with Git so others and AI tools see your code.`;
  }
};
var CheckModal = class extends import_obsidian.Modal {
  constructor(app, findings, rerun) {
    super(app);
    this.findings = findings;
    this.rerun = rerun;
  }
  onOpen() {
    this.render();
  }
  render() {
    const { contentEl } = this;
    contentEl.empty();
    contentEl.addClass("mdse-bootstrap-check");
    contentEl.createEl("h2", { text: "MDSE release check" });
    const { errors, warnings } = summarize(this.findings);
    contentEl.createEl("p", { text: errors ? `${errors} problem(s), ${warnings} warning(s).` : warnings ? `No problems, ${warnings} warning(s).` : "Everything matches the controlled release." });
    const table = contentEl.createEl("table");
    const head = table.createEl("tr");
    for (const h of ["", "Area", "Item", "Result"]) head.createEl("th", { text: h });
    for (const f of this.findings) {
      const tr = table.createEl("tr");
      tr.createEl("td", { text: f.level === "ok" ? "\u2713" : f.level === "warn" ? "!" : "\u2717", cls: `mdse-${f.level}` });
      tr.createEl("td", { text: f.area });
      tr.createEl("td", { text: f.subject });
      tr.createEl("td", { text: f.message });
    }
    new import_obsidian.Setting(contentEl).addButton((b) => b.setButtonText("Check again").setCta().onClick(async () => {
      this.findings = await this.rerun();
      this.render();
    }));
  }
  onClose() {
    this.contentEl.empty();
  }
};
var RegisterModal = class extends import_obsidian.Modal {
  constructor(app, plugin, existing) {
    super(app);
    this.plugin = plugin;
    this.existing = existing;
    this.first = "";
    this.last = "";
    this.code = "";
    this.codeEdited = false;
  }
  onOpen() {
    const { contentEl } = this;
    contentEl.addClass("mdse-bootstrap-register");
    contentEl.createEl("h2", { text: "Register your author code" });
    contentEl.createEl("p", { text: this.existing ? `This computer already uses ${this.existing}. Registering again replaces it on this computer only; to change your code everywhere, follow Definitions/Changing Your Author Code.` : "Every note you create carries your author code in its uid. It is asked once per computer." });
    let codeInput = null;
    const refresh = () => {
      if (!this.codeEdited) {
        this.code = deriveCode(this.first, this.last);
        codeInput?.setValue(this.code);
      }
    };
    new import_obsidian.Setting(contentEl).setName("First name").addText((t) => t.onChange((v) => {
      this.first = v;
      refresh();
    }));
    new import_obsidian.Setting(contentEl).setName("Last name").addText((t) => t.onChange((v) => {
      this.last = v;
      refresh();
    }));
    new import_obsidian.Setting(contentEl).setName("Author code").setDesc("Last name then first name, 13 characters, padded with '-'. Accept it unless it is taken.").addText((t) => {
      codeInput = t;
      t.onChange((v) => {
        this.code = v.trim();
        this.codeEdited = true;
      });
    });
    const err = contentEl.createDiv({ cls: "mdse-error" });
    new import_obsidian.Setting(contentEl).addButton((b) => b.setButtonText("Later").onClick(() => this.close())).addButton((b) => b.setButtonText("Register").setCta().onClick(async () => {
      err.setText("");
      if (!this.first.trim() || !this.last.trim()) {
        err.setText("First and last name are both needed.");
        return;
      }
      const fullName = `${this.first.trim()} ${this.last.trim()}`;
      const check = checkCode(this.code, fullName, this.plugin.people(), await this.plugin.reserved());
      if (!check.ok) {
        err.setText(check.reason);
        return;
      }
      b.setDisabled(true);
      try {
        const msg = await this.plugin.registerAuthor(this.first, this.last, this.code);
        new import_obsidian.Notice(msg, 12e3);
        this.close();
      } catch (e) {
        err.setText(`Registration failed: ${e.message}`);
        b.setDisabled(false);
      }
    }));
  }
  onClose() {
    this.contentEl.empty();
  }
};
