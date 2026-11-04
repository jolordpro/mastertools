/**********************************************************************
 * CEP Host Template  —  host/index.jsx  —  v1.0.0
 * STRICT ES3 ExtendScript (references/00 §4 + references/06 §2). The ONLY
 * layer that touches the AE DOM. Every entry point is wrapped so it ALWAYS
 * returns a JSON string (the hostFail invariant — references/06 §3): a bare
 * throw becomes CEP's misleading "EvalScript error." Keep the wrapper + the
 * called-vs-defined audit (scripts/qc.sh) on every new entry point.
 *
 * Client calls these by name via CSInterface.evalScript("aexPeek()", cb) and
 * JSON.parse the result. Keep the host<->client contract in one canonical place.
 **********************************************************************/

/* ---- guarded polyfills (Adobe panels inject these; assume absent) ---- */
if (typeof JSON === "undefined" || !JSON) {
    JSON = {};
    JSON.parse = function (s) { return eval("(" + s + ")"); };
    JSON.stringify = function (v) { return _enc(v); };
    function _enc(v) {
        if (v === null || v === undefined) { return "null"; }
        var t = typeof v, i, out;
        if (t === "number" || t === "boolean") { return String(v); }
        if (t === "string") { return '"' + v.replace(/\\/g, "\\\\").replace(/"/g, '\\"').replace(/\n/g, "\\n") + '"'; }
        if (v instanceof Array) { out = []; for (i = 0; i < v.length; i++) { out.push(_enc(v[i])); } return "[" + out.join(",") + "]"; }
        out = []; for (i in v) { if (v.hasOwnProperty(i)) { out.push(_enc(String(i)) + ":" + _enc(v[i])); } }
        return "{" + out.join(",") + "}";
    }
}

/* ---- constants ---- */
var BRIDGE_DIRNAME = "YourApp";
var SECTION = "YourApp";

/* ---- diagnostics + the hostFail invariant ---- */
function logLine(msg) {
    try {
        var dir = new Folder(Folder.userData.fsName + "/" + BRIDGE_DIRNAME);
        if (!dir.exists) { dir.create(); }
        var f = new File(dir.fsName + "/host.log");
        f.encoding = "UTF-8";
        if (f.open("a")) { f.writeln("" + (new Date()).getTime() + "  " + msg); f.close(); }
    } catch (e) {}
}
function hostFail(where, e) {
    logLine("ERR " + where + ": " + e);
    return JSON.stringify({ ok: false, _hostError: true, where: where, msg: String((e && e.message) || e) });
}

/* ---- bridge I/O (temp-then-rename, UTF-8 — a torn read can never happen) ---- */
function writeBridgeFile(name, jsonStr) {
    var dir = new Folder(Folder.userData.fsName + "/" + BRIDGE_DIRNAME);
    if (!dir.exists) { dir.create(); }
    var tmp = new File(dir.fsName + "/" + name + ".tmp");
    var dst = new File(dir.fsName + "/" + name);
    tmp.encoding = "UTF-8";
    if (!tmp.open("w")) { return false; }
    tmp.write(jsonStr); tmp.close();
    if (dst.exists) { dst.remove(); }
    if (!tmp.rename(name)) {
        dst.encoding = "UTF-8";
        if (dst.open("w")) { dst.write(jsonStr); dst.close(); } else { return false; }
    }
    return true;
}

/* ============================================================
 * ENTRY POINTS — each a thin wrapper over a _impl, always returns JSON.
 * ============================================================ */

function aexPeek() { try { return _aexPeek(); } catch (e) { return hostFail("aexPeek", e); } }
function _aexPeek() {
    var hasComp = false, name = "", sel = 0, layers = 0;
    var c = app.project.activeItem;
    if (c && c instanceof CompItem) {
        hasComp = true; name = c.name; layers = c.numLayers;
        var s = c.selectedLayers; sel = s ? s.length : 0;
    }
    return JSON.stringify({ ok: true, hasComp: hasComp, comp: name, sel: sel, layers: layers });
}

function aexApply(argsJson) { try { return _aexApply(argsJson); } catch (e) { return hostFail("aexApply", e); } }
function _aexApply(argsJson) {
    var args = argsJson ? JSON.parse(argsJson) : {};
    var comp = app.project.activeItem;
    if (!comp || !(comp instanceof CompItem)) { return JSON.stringify({ ok: false, msg: "Open a composition first." }); }
    var base = (args && args.base) ? String(args.base) : "Layer";
    var done = 0, skipped = 0, n = 1, i, lyr, sel = comp.selectedLayers;
    app.beginUndoGroup("Rename layers");
    try {
        for (i = 0; i < sel.length; i++) {
            lyr = sel[i];
            if (lyr.locked) { skipped++; continue; }
            lyr.name = base + "_" + (n < 10 ? "0" + n : "" + n); n++; done++;
        }
    } finally {
        app.endUndoGroup();
    }
    logLine("aexApply: renamed " + done + ", skipped " + skipped);
    return JSON.stringify({ ok: true, done: done, skipped: skipped });
}
