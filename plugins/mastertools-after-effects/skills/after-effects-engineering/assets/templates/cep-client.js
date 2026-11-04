/* ----------------------------------------------------------------------------
 * CEP Client Template — client/index.js — MODERN JS (CEF/Chromium), not ES3.
 * Renders the UI, polls host state, calls the ES3 host by name and JSON.parses
 * the result. The client's ceiling is Chromium's, not ES3's (references/06 §5)
 * — when ExtendScript can't do something, ask whether the client can, fed by
 * what the host extracts. The hard boundary: the Adobe DOM is reachable ONLY
 * via evalScript into the host.
 * -------------------------------------------------------------------------- */
(function () {
  "use strict";
  const cs = new CSInterface();

  // host bridge: evalScript -> parsed JSON, or null on a genuine no-response.
  // (Redact any secret token shapes from logs; never put secrets in a call string.)
  function host(call) {
    return new Promise((resolve) => {
      cs.evalScript(call, (res) => {
        if (!res || res === "EvalScript error.") { resolve(null); return; }
        try { resolve(JSON.parse(res)); } catch (e) { resolve(null); }
      });
    });
  }

  // Match AE's panel theme so the panel doesn't look bolted on.
  function applyTheme() {
    try {
      const c = cs.getHostEnvironment().appSkinInfo.panelBackgroundColor.color;
      const dark = (c.red + c.green + c.blue) / 3 < 128;
      const root = document.documentElement.style;
      root.setProperty("--bg", `rgb(${Math.round(c.red)},${Math.round(c.green)},${Math.round(c.blue)})`);
      root.setProperty("--fg", dark ? "#e8e1d3" : "#1a1a1a");
    } catch (e) { /* keep CSS defaults */ }
  }

  // Density: WIDTH-primary only. Never measure height — opening a drawer/popover
  // must not be able to downgrade the tier and hide a control (references/06 §6).
  function applyDensity() {
    const w = document.documentElement.clientWidth;
    document.body.className = w < 200 ? "t-mini" : (w < 260 ? "t-compact" : "t-full");
  }

  let refs = {};

  async function peek() {
    const p = await host("aexPeek()");
    if (!p) { refs.status.textContent = "Connecting…"; refs.apply.disabled = true; return; }
    refs.apply.disabled = !p.hasComp;
    refs.scope.textContent = p.hasComp
      ? (p.sel > 0 ? `Rename: ${p.sel} selected` : `Rename: all ${p.layers} layers`)
      : "Open a comp to begin";
    refs.status.textContent = p.hasComp ? `comp: ${p.comp}` : "";
  }

  // Post-action feedback: momentary color that fades to calm (~7s).
  let fadeT = 0;
  function showResult(kind, msg) {
    refs.result.textContent = msg;
    refs.result.className = "result " + kind;
    clearTimeout(fadeT);
    fadeT = setTimeout(() => { refs.result.className = "result"; }, 7000);
  }

  async function doApply() {
    refs.apply.disabled = true;
    const base = (refs.name.value || "Layer").replace(/^\s+|\s+$/g, "");
    // aexApply takes a JSON-string arg -> stringify twice (object -> JSON -> JS string literal).
    const arg = JSON.stringify(JSON.stringify({ base }));
    const r = await host(`aexApply(${arg})`);
    if (!r) { showResult("bad", "After Effects didn't respond — try again."); return; }
    if (!r.ok) { showResult("bad", r.msg || "Failed."); return; }
    let m = `✓ Renamed ${r.done} layer${r.done === 1 ? "" : "s"}`;
    if (r.skipped) { m += ` (${r.skipped} locked, skipped)`; }
    showResult("ok", m + " — ⌘Z to undo");
  }

  function init() {
    refs = {
      status: document.getElementById("status"),
      scope:  document.getElementById("scope"),
      name:   document.getElementById("nameField"),
      apply:  document.getElementById("applyBtn"),
      result: document.getElementById("result")
    };
    applyTheme();
    applyDensity();
    window.addEventListener("resize", applyDensity);
    refs.apply.addEventListener("click", doApply);
    // Enter = primary action (skip when typing in a textarea); Esc reserved for closing overlays.
    document.addEventListener("keydown", (e) => {
      if (e.key === "Enter" && e.target.tagName !== "TEXTAREA") { doApply(); }
    });
    peek();
    setInterval(peek, 1000);   // poll host state ~1s — cheap; the CEF process polls even while the host blocks
  }

  document.addEventListener("DOMContentLoaded", init);
})();
