/* __NAME__ (UXP). config.js is written per app by uxp_build.py: window.UXP_CFG = { key, id, name, version }.
   Logs to /private/tmp/<id>.log: without developer mode that log is the only debugger (references/testing.md). */
(function () {
  "use strict";

  const uxp = require("uxp");
  const lfs = uxp.storage.localFileSystem;
  const CFG = window.UXP_CFG || { key: "??", id: "uxp.plugin", name: "__NAME__", version: "0.0.0" };
  const $ = (id) => document.getElementById(id);

  // ---------- log + receipts (best-effort: a logging failure must never break the panel)
  const logLines = [];
  async function writeTmp(name, text) {
    const tmp = await lfs.getEntryWithUrl("file:/private/tmp");
    const f = await tmp.createFile(name, { overwrite: true });
    await f.write(text || "-");                       // write("") throws "data cannot be null"
  }
  async function log(line) {
    try {
      logLines.push(new Date().toISOString() + " " + line);
      if (logLines.length > 200) { logLines.shift(); }
      await writeTmp(CFG.id + ".log", logLines.join("\n") + "\n");
    } catch (e) { /* ignore */ }
  }
  function status(msg, kind) {
    const el = $("status");
    el.textContent = msg;
    el.className = "status" + (kind ? " " + kind : "");
    log("status: " + msg);
  }

  // ---------- host helpers
  // Photoshop: anything that changes a document must run inside executeAsModal.
  async function modal(name, fn) {
    if (CFG.key === "PS") { return require("photoshop").core.executeAsModal(fn, { commandName: name }); }
    return fn();
  }

  // ---------- actions
  async function test() {
    status("Testing…", "busy");
    try {
      await modal("Test", async () => {
        await writeTmp(CFG.id + ".receipt.txt", new Date().toString() + " | " + uxp.host.name + " " + uxp.host.version + "\n");
      });
      status("Wrote /private/tmp/" + CFG.id + ".receipt.txt", "good");
    } catch (e) {
      status("Test failed: " + (e && e.message ? e.message : String(e)), "bad");
    }
  }

  // ---------- lifecycle: setup must run in the first synchronous tick
  try {
    uxp.entrypoints.setup({ panels: { main: { show() { log("panel shown"); } } } });
  } catch (e) { /* optional */ }

  (async function start() {
    $("app").textContent = CFG.key;
    $("test").addEventListener("click", test);
    await log("start: " + CFG.key + " " + CFG.version + " host=" + (uxp.host && uxp.host.name) + " " +
      (uxp.host && uxp.host.version) + " uxp=" + (uxp.versions && uxp.versions.uxp));
    status("Ready in " + (uxp.host && uxp.host.name));
  })();
})();
