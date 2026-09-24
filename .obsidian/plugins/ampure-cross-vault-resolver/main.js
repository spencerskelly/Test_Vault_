const { Plugin, Notice, FuzzySuggestModal, EditorSuggest } = require("obsidian");
const fs = require("fs");
const path = require("path");

function parseVaultYaml(text) {
  const out = {};
  for (const line of String(text || "").split(/\r?\n/)) {
    const m = line.match(/^([A-Za-z0-9_]+):\s*(.*?)\s*$/);
    if (m) out[m[1]] = m[2].replace(/^["']|["']$/g, "");
  }
  return out;
}

function uidFromMarkdown(text) {
  const head = String(text || "").slice(0, 12000);
  const fm = head.match(/^---\s*\n([\s\S]*?)\n---/);
  if (!fm) return null;
  const m = fm[1].match(/^uid:\s*([0-9A-Za-z-]{30})\s*$/m);
  return m ? m[1] : null;
}

function titleForFile(filePath) {
  return path.basename(filePath, path.extname(filePath));
}

class CrossVaultModal extends FuzzySuggestModal {
  constructor(app, plugin, editor) {
    super(app);
    this.plugin = plugin;
    this.editor = editor;
    this.setPlaceholder("Search accessible cross-vault notes...");
  }
  getItems() {
    return this.plugin.externalNotes;
  }
  getItemText(item) {
    return `${item.title} — ${item.vaultName} — ${item.relPath}`;
  }
  onChooseItem(item) {
    this.editor.replaceSelection(`[${item.title}](uid:${item.uid})`);
  }
}

class CrossVaultSuggest extends EditorSuggest {
  constructor(app, plugin) {
    super(app);
    this.plugin = plugin;
  }
  onTrigger(cursor, editor) {
    const line = editor.getLine(cursor.line).slice(0, cursor.ch);
    const m = line.match(/\[\[([^\]]*)$/);
    if (!m) return null;
    return {
      start: { line: cursor.line, ch: cursor.ch - m[0].length },
      end: cursor,
      query: m[1]
    };
  }
  getSuggestions(context) {
    const q = String(context.query || "").trim().toLowerCase();
    const items = this.plugin.externalNotes;
    if (!q) return items.slice(0, 25);
    return items
      .filter(x =>
        x.title.toLowerCase().includes(q) ||
        x.vaultName.toLowerCase().includes(q) ||
        x.relPath.toLowerCase().includes(q))
      .slice(0, 25);
  }
  renderSuggestion(item, el) {
    el.createDiv({ text: item.title, cls: "suggestion-title" });
    el.createDiv({ text: `${item.vaultName} · ${item.relPath}`, cls: "suggestion-note" });
  }
  selectSuggestion(item) {
    const ctx = this.context;
    if (!ctx) return;
    ctx.editor.replaceRange(
      `[${item.title}](uid:${item.uid})`,
      ctx.start,
      ctx.end
    );
  }
}

module.exports = class AmpureCrossVaultResolver extends Plugin {
  async onload() {
    this.index = new Map();
    this.externalNotes = [];
    this.basePath = this.getBasePath();

    this.addCommand({
      id: "rebuild-cross-vault-index",
      name: "Rebuild cross-vault index",
      callback: async () => {
        const count = await this.rebuildIndex();
        new Notice(`Cross-vault resolver indexed ${count} accessible notes.`);
      }
    });

    this.addCommand({
      id: "insert-cross-vault-link",
      name: "Insert cross-vault link",
      editorCallback: (editor) => new CrossVaultModal(this.app, this, editor).open()
    });

    this.registerEditorSuggest(new CrossVaultSuggest(this.app, this));
    this.registerDomEvent(document, "click", (evt) => this.handleUidClick(evt), true);

    this.app.workspace.onLayoutReady(() => {
      void this.rebuildIndex();
      this.registerInterval(window.setInterval(() => void this.rebuildIndex(), 60000));
    });
  }

  getBasePath() {
    const adapter = this.app.vault.adapter;
    if (typeof adapter.getBasePath === "function") return adapter.getBasePath();
    return null;
  }

  async rebuildIndex() {
    if (!this.basePath) return 0;
    const parent = path.dirname(this.basePath);
    let entries = [];
    try {
      entries = await fs.promises.readdir(parent, { withFileTypes: true });
    } catch (e) {
      console.warn("Cross-vault resolver: cannot read sibling vault directory", e);
      return 0;
    }

    const next = new Map();
    for (const entry of entries) {
      if (!entry.isDirectory()) continue;
      const vaultPath = path.join(parent, entry.name);
      const identityPath = path.join(vaultPath, ".vault.yaml");
      let identityText;
      try {
        identityText = await fs.promises.readFile(identityPath, "utf8");
      } catch (_) {
        continue;
      }

      const identity = parseVaultYaml(identityText);
      if (!identity.vault_uid) continue;
      const vaultName = identity.name || entry.name;
      const files = await this.walkMarkdown(vaultPath);
      for (const absPath of files) {
        let text;
        try {
          text = await fs.promises.readFile(absPath, "utf8");
        } catch (_) {
          continue;
        }
        const uid = uidFromMarkdown(text);
        if (!uid) continue;
        const relPath = path.relative(vaultPath, absPath).split(path.sep).join("/");
        next.set(uid, {
          uid,
          title: titleForFile(absPath),
          vaultUid: identity.vault_uid,
          vaultName,
          vaultFolder: entry.name,
          vaultPath,
          relPath
        });
      }
    }

    this.index = next;
    this.externalNotes = Array.from(next.values())
      .filter(x => path.resolve(x.vaultPath) !== path.resolve(this.basePath))
      .sort((a, b) => a.title.localeCompare(b.title) || a.vaultName.localeCompare(b.vaultName));
    return next.size;
  }

  async walkMarkdown(root) {
    const out = [];
    const skip = new Set([".git", ".obsidian", ".trash", "node_modules"]);
    const walk = async (dir) => {
      let entries;
      try {
        entries = await fs.promises.readdir(dir, { withFileTypes: true });
      } catch (_) {
        return;
      }
      for (const entry of entries) {
        if (skip.has(entry.name)) continue;
        const abs = path.join(dir, entry.name);
        if (entry.isDirectory()) await walk(abs);
        else if (entry.isFile() && entry.name.toLowerCase().endsWith(".md")) out.push(abs);
      }
    };
    await walk(root);
    return out;
  }

  async handleUidClick(evt) {
    const anchor = evt.target && evt.target.closest ? evt.target.closest("a") : null;
    if (!anchor) return;
    const raw = anchor.getAttribute("href") || anchor.getAttribute("data-href") || "";
    if (!raw.startsWith("uid:")) return;

    evt.preventDefault();
    evt.stopPropagation();

    const ref = raw.slice(4);
    const hashAt = ref.indexOf("#");
    const uid = hashAt >= 0 ? ref.slice(0, hashAt) : ref;
    const fragment = hashAt >= 0 ? ref.slice(hashAt + 1) : "";
    const target = this.index.get(uid);

    if (!target) {
      new Notice("Referenced note unavailable.");
      return;
    }

    if (path.resolve(target.vaultPath) === path.resolve(this.basePath)) {
      const link = target.relPath + (fragment ? "#" + fragment : "");
      await this.app.workspace.openLinkText(link, "", false);
      return;
    }

    const file = target.relPath + (fragment ? "#" + fragment : "");
    const uri = `obsidian://open?vault=${encodeURIComponent(target.vaultFolder)}&file=${encodeURIComponent(file)}`;
    try {
      const electron = require("electron");
      if (electron?.shell?.openExternal) {
        await electron.shell.openExternal(uri);
        return;
      }
    } catch (_) {}
    window.open(uri);
  }
};
