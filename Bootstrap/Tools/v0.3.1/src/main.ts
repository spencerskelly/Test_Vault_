import { App, Modal, Notice, Plugin, Setting, TFile, TFolder, apiVersion, normalizePath, parseYaml } from "obsidian";
import {
  Finding, InstalledPlugin, PersonRecord, ReleaseState, activationPlan, checkCode, deriveCode, evaluate, hex, isValidCode, parseLock, summarize,
} from "./core";

const CODE_FILE = ".obsidian/author-code.txt";        // same literal as Snippet - uid
const PEOPLE = "99_System/04_People";
const PERSON_TEMPLATE = "99_System/05_Templates/Person.md";
const AUTHORS = "99_System/03_Schemas/authors.yaml";
const START_DELAY_MS = 4000;

interface PluginsApi {
  manifests: Record<string, { version: string; dir?: string }>;
  enabledPlugins: Set<string>;
  plugins: Record<string, unknown>;
  enablePlugin?(id: string): Promise<void> | void;
}

interface InternalPluginsApi {
  getPluginById(id: string): { enabled: boolean } | null;
  enablePlugin?(id: string): Promise<void> | void;
  disablePlugin?(id: string): Promise<void> | void;
}

export default class MdseBootstrap extends Plugin {
  private status: HTMLElement | null = null;
  private last: Finding[] = [];

  async onload(): Promise<void> {
    this.status = this.addStatusBarItem();
    this.status.setText("MDSE: checking…");
    this.status.addClass("mod-clickable");
    this.registerDomEvent(this.status, "click", () => new CheckModal(this.app, this.last, async () => {
      await this.repairActivation();
      return this.runCheck(true);
    }).open());

    this.addCommand({ id: "show-release-check", name: "Show release check", callback: async () => {
      await this.repairActivation();
      await this.runCheck(false);
      new CheckModal(this.app, this.last, () => this.runCheck(true)).open();
    } });
    this.addCommand({ id: "register-author", name: "Register author code", callback: () => this.openRegistration(true) });

    this.app.workspace.onLayoutReady(() => {
      window.setTimeout(async () => {
        await this.repairActivation();
        await this.runCheck(true);
        if (!(await this.readCode())) this.openRegistration(false);
      }, START_DELAY_MS);
    });
  }

  private plugins(): PluginsApi {
    return (this.app as unknown as { plugins: PluginsApi }).plugins;
  }

  private internalPlugins(): InternalPluginsApi {
    return (this.app as unknown as { internalPlugins: InternalPluginsApi }).internalPlugins;
  }

  private async scanInstalled(lock: ReturnType<typeof parseLock>): Promise<Record<string, InstalledPlugin>> {
    const a = this.app.vault.adapter;
    const cfg = this.app.vault.configDir;
    const installed: Record<string, InstalledPlugin> = {};
    for (const [id, p] of Object.entries(lock.plugins)) {
      const dir = normalizePath(`${cfg}/plugins/${id}`);
      let version: string | null = null;
      try { version = String(JSON.parse(await a.read(`${dir}/manifest.json`)).version); } catch { version = null; }
      const sha256: Record<string, string | null> = {};
      for (const file of Object.keys(p.sha256)) {
        try { sha256[file] = hex(await crypto.subtle.digest("SHA-256", await a.readBinary(`${dir}/${file}`))); }
        catch { sha256[file] = null; }
      }
      installed[id] = { version, sha256 };
    }
    return installed;
  }

  private async repairActivation(): Promise<void> {
    try {
      const a = this.app.vault.adapter;
      const cfg = this.app.vault.configDir;
      const lock = parseLock(parseYaml(await a.read(normalizePath(`${cfg}/plugin-lock.yaml`))));
      const internal = this.internalPlugins();
      const coreEnabled: Record<string, boolean> = {};
      for (const id of [...lock.requiredCorePlugins, ...lock.disabledCorePlugins]) coreEnabled[id] = !!internal.getPluginById(id)?.enabled;
      const installed = await this.scanInstalled(lock);
      const plan = activationPlan(lock, new Set(this.plugins().enabledPlugins), coreEnabled, installed);

      for (const id of plan.enableCommunity) {
        if (typeof this.plugins().enablePlugin === "function") await this.plugins().enablePlugin!(id);
      }
      for (const id of plan.enableCore) {
        if (typeof internal.enablePlugin === "function") await internal.enablePlugin(id);
      }
      for (const id of plan.disableCore) {
        if (typeof internal.disablePlugin === "function") await internal.disablePlugin(id);
      }
    } catch {
      // runCheck reports malformed/missing lock and any activation state that remains wrong.
    }
  }

  async runCheck(notify: boolean): Promise<Finding[]> {
    const a = this.app.vault.adapter;
    const cfg = this.app.vault.configDir;
    let findings: Finding[];
    try {
      const lock = parseLock(parseYaml(await a.read(normalizePath(`${cfg}/plugin-lock.yaml`))));
      const installed = await this.scanInstalled(lock);
      let vaultText = "";
      try { vaultText = await a.read(".vault.yaml"); } catch { /* reported below */ }
      const rel = /^mdse_release:\s*["']?([^"'#\r\n]+)/m.exec(vaultText);
      const internal = this.internalPlugins();
      const coreEnabled: Record<string, boolean> = {};
      for (const id of [...lock.requiredCorePlugins, ...lock.disabledCorePlugins]) coreEnabled[id] = !!internal.getPluginById(id)?.enabled;
      const state: ReleaseState = {
        lock, installed,
        enabled: new Set(this.plugins().enabledPlugins),
        present: new Set(Object.keys(this.plugins().manifests)),
        appVersion: apiVersion,
        coreEnabled,
        mdseRelease: rel ? rel[1].trim() : null,
        vaultInitialized: !!vaultText && !/vault_uid:\s*UNINITIALIZED/.test(vaultText),
        isGitRepo: await a.exists(".git"),
      };
      findings = evaluate(state);
      const code = await this.readCode();
      findings.push(code
        ? { level: "ok", area: "author", subject: "Author code", message: code }
        : { level: "warn", area: "author", subject: "Author code", message: "not registered on this computer; run “MDSE Bootstrap: Register author code”" });
    } catch (e) {
      findings = [{ level: "error", area: "release", subject: "plugin-lock.yaml", message: (e as Error).message }];
    }
    this.last = findings;
    const { errors, warnings } = summarize(findings);
    this.status?.setText(errors ? `MDSE: ${errors} problem${errors > 1 ? "s" : ""}` : warnings ? `MDSE: ${warnings} warning${warnings > 1 ? "s" : ""}` : "MDSE: release OK");
    if (notify && errors) new Notice(`MDSE Bootstrap: ${errors} release problem${errors > 1 ? "s" : ""}. Click “MDSE” in the status bar for details.`, 10000);
    return findings;
  }

  async readCode(): Promise<string | null> {
    try {
      const c = (await this.app.vault.adapter.read(CODE_FILE)).trim();
      return isValidCode(c) ? c : null;
    } catch { return null; }
  }

  people(): PersonRecord[] {
    const out: PersonRecord[] = [];
    for (const f of this.app.vault.getMarkdownFiles()) {
      if (!f.path.startsWith(PEOPLE + "/")) continue;
      const fm = this.app.metadataCache.getFileCache(f)?.frontmatter ?? {};
      const prev = Array.isArray(fm.previousCodes) ? fm.previousCodes.map(String) : [];
      out.push({ path: f.path, name: String(fm.name ?? f.basename), code: String(fm.code ?? ""), previousCodes: prev });
    }
    return out;
  }

  async reserved(): Promise<string[]> {
    try {
      const y = parseYaml(await this.app.vault.adapter.read(AUTHORS)) as { ai_authors?: { code?: string }[]; unmapped?: { code?: string } };
      return [...(y.ai_authors ?? []).map((x) => String(x.code ?? "")), String(y.unmapped?.code ?? "")].filter(Boolean);
    } catch { return []; }
  }

  async openRegistration(manual: boolean): Promise<void> {
    const existing = await this.readCode();
    if (existing && !manual) return;
    new RegisterModal(this.app, this, existing).open();
  }

  /** Spec steps 5 to 7. */
  async registerAuthor(first: string, last: string, code: string): Promise<string> {
    await this.app.vault.adapter.write(CODE_FILE, code);
    const fullName = `${first.trim()} ${last.trim()}`.replace(/\s+/g, " ");
    const already = this.people().find((p) => p.code === code || p.name.toLowerCase() === fullName.toLowerCase());
    if (already) {
      await this.runCheck(false);
      return `Author code ${code} saved on this computer. Your person note already exists (${already.path}).`;
    }
    const tp = this.plugins().plugins["templater-obsidian"] as
      | { templater?: { create_new_note_from_template(t: TFile, f: TFolder, name: string, open: boolean): Promise<TFile | undefined> } }
      | undefined;
    const template = this.app.vault.getAbstractFileByPath(PERSON_TEMPLATE);
    const folder = this.app.vault.getAbstractFileByPath(PEOPLE);
    if (!tp?.templater || !(template instanceof TFile) || !(folder instanceof TFolder)) {
      await this.runCheck(false);
      return `Author code ${code} saved, but the person note could not be created (Templater or the Person template is missing). Run the release check.`;
    }
    const note = await tp.templater.create_new_note_from_template(template, folder, fullName, false);
    if (!note) return `Author code ${code} saved, but Templater did not create the person note.`;
    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || "";
    await this.app.fileManager.processFrontMatter(note, (fm: Record<string, unknown>) => {
      fm.code = code;
      fm.name = fullName;
      fm.timezone = tz;
    });
    await this.runCheck(false);
    return `Registered ${fullName} as ${code} and created ${note.path}. Commit and sync with Git so others and AI tools see your code.`;
  }
}

class CheckModal extends Modal {
  constructor(app: App, private findings: Finding[], private rerun: () => Promise<Finding[]>) { super(app); }
  onOpen(): void { this.render(); }
  private render(): void {
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
      tr.createEl("td", { text: f.level === "ok" ? "✓" : f.level === "warn" ? "!" : "✗", cls: `mdse-${f.level}` });
      tr.createEl("td", { text: f.area });
      tr.createEl("td", { text: f.subject });
      tr.createEl("td", { text: f.message });
    }
    new Setting(contentEl).addButton((b) => b.setButtonText("Check again").setCta().onClick(async () => {
      this.findings = await this.rerun();
      this.render();
    }));
  }
  onClose(): void { this.contentEl.empty(); }
}

class RegisterModal extends Modal {
  private first = "";
  private last = "";
  private code = "";
  private codeEdited = false;
  constructor(app: App, private plugin: MdseBootstrap, private existing: string | null) { super(app); }

  onOpen(): void {
    const { contentEl } = this;
    contentEl.addClass("mdse-bootstrap-register");
    contentEl.createEl("h2", { text: "Register your author code" });
    contentEl.createEl("p", { text: this.existing
      ? `This computer already uses ${this.existing}. Registering again replaces it on this computer only; to change your code everywhere, follow Definitions/Changing Your Author Code.`
      : "Every note you create carries your author code in its uid. It is asked once per computer." });
    let codeInput: { setValue(v: string): unknown } | null = null;
    const refresh = () => { if (!this.codeEdited) { this.code = deriveCode(this.first, this.last); codeInput?.setValue(this.code); } };
    new Setting(contentEl).setName("First name").addText((t) => t.onChange((v) => { this.first = v; refresh(); }));
    new Setting(contentEl).setName("Last name").addText((t) => t.onChange((v) => { this.last = v; refresh(); }));
    new Setting(contentEl).setName("Author code").setDesc("Last name then first name, 13 characters, padded with '-'. Accept it unless it is taken.")
      .addText((t) => { codeInput = t; t.onChange((v) => { this.code = v.trim(); this.codeEdited = true; }); });
    const err = contentEl.createDiv({ cls: "mdse-error" });
    new Setting(contentEl)
      .addButton((b) => b.setButtonText("Later").onClick(() => this.close()))
      .addButton((b) => b.setButtonText("Register").setCta().onClick(async () => {
        err.setText("");
        if (!this.first.trim() || !this.last.trim()) { err.setText("First and last name are both needed."); return; }
        const fullName = `${this.first.trim()} ${this.last.trim()}`;
        const check = checkCode(this.code, fullName, this.plugin.people(), await this.plugin.reserved());
        if (!check.ok) { err.setText(check.reason); return; }
        b.setDisabled(true);
        try {
          const msg = await this.plugin.registerAuthor(this.first, this.last, this.code);
          new Notice(msg, 12000);
          this.close();
        } catch (e) {
          err.setText(`Registration failed: ${(e as Error).message}`);
          b.setDisabled(false);
        }
      }));
  }
  onClose(): void { this.contentEl.empty(); }
}
