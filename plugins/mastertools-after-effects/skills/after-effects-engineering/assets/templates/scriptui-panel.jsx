/**********************************************************************
 * ScriptUI Panel Template  —  v1.0.0
 * AE compatibility: 2022+ (uses Layer.id where persistence matters)
 * What it does: dockable panel skeleton following the §0–§12 architecture
 *               (references/05 §5). Replace the ACTION ENGINE with your op.
 * Author / site / support: you / yoursite.com
 * Settings section: "ToolName_v1"   (migrates older sections on load)
 * CHANGELOG:
 *   1.0.0 — template.
 *
 * Strict ES3 (references/00 §4). Guarded polyfills below. No alert() for
 * expected conditions — errors go inline. One undo group, closed in finally.
 **********************************************************************/

(function (thisObj) {

    // ----- §1  DESIGN SYSTEM CONSTANTS -----
    var DS = {
        accent: [0.25, 0.56, 0.85], success: [0.30, 0.72, 0.45],
        warning: [0.85, 0.68, 0.25], error: [0.82, 0.30, 0.30],
        dimText: [0.55, 0.55, 0.55], ok: "✓", arrow: "→", dash: "—",
        warn: "(!)", fail: "X", minW: 250
    };

    // ----- §2  POLYFILLS (assume native absent — Adobe panels inject them; references/00 §4) -----
    if (!Array.prototype.indexOf) {
        Array.prototype.indexOf = function (x) {
            var i; for (i = 0; i < this.length; i++) { if (this[i] === x) { return i; } } return -1;
        };
    }
    if (typeof JSON === "undefined" || !JSON) {
        JSON = {};
        JSON.stringify = function (v) { return _enc(v); };
        JSON.parse = function (s) { return eval("(" + s + ")"); };
        function _enc(v) {
            if (v === null) { return "null"; }
            var t = typeof v, i, out;
            if (t === "number" || t === "boolean") { return String(v); }
            if (t === "string") { return '"' + v.replace(/\\/g, "\\\\").replace(/"/g, '\\"') + '"'; }
            if (v instanceof Array) {
                out = []; for (i = 0; i < v.length; i++) { out.push(_enc(v[i])); } return "[" + out.join(",") + "]";
            }
            out = []; for (i in v) { if (v.hasOwnProperty(i)) { out.push(_enc(String(i)) + ":" + _enc(v[i])); } }
            return "{" + out.join(",") + "}";
        }
    }
    function trimStr(s) { return String(s).replace(/^\s+/, "").replace(/\s+$/, ""); }

    // ----- §3  SETTINGS PERSISTENCE (also stores the AE version written under) -----
    var SECTION = "ToolName_v1";
    var Settings = {
        get: function (k, d) {
            try { if (app.settings.haveSetting(SECTION, k)) { return app.settings.getSetting(SECTION, k); } } catch (e) {}
            return d;
        },
        set: function (k, v) { try { app.settings.saveSetting(SECTION, k, String(v)); } catch (e) {} }
    };

    // ----- §4  UTILITY FUNCTIONS -----
    function setColor(ctrl, arr) {
        try { ctrl.graphics.foregroundColor = ctrl.graphics.newPen(ctrl.graphics.PenType.SOLID_COLOR, arr, 1); } catch (e) {}
    }

    // ----- §6  STATE -----
    var _busy = false, _cache = [];

    // ----- §7  EMPTY STATE MAP -----
    function emptyStateMsg() {
        if (!(app.project)) { return "Open a project to begin"; }
        var comp = app.project.activeItem;
        if (!(comp instanceof CompItem)) { return "Select a comp in the Project panel"; }
        if (comp.numLayers === 0) { return "Add layers to the comp first"; }
        if (getSelLayers(comp).length === 0) { return "Select layers in the timeline"; }
        return "";
    }

    // ----- §8  DATA LAYER (snapshot the DOM once; preview/decisions use the cache) -----
    function getSelLayers(comp) {
        var out = [], sel, i;
        try { sel = comp.selectedLayers; } catch (e) { sel = null; }
        if (sel) { for (i = 0; i < sel.length; i++) { out.push(sel[i]); } }
        return out;
    }
    function refreshCache() {
        _cache = [];
        var comp = app.project.activeItem;
        if (!(comp instanceof CompItem)) { return; }
        var layers = getSelLayers(comp), i;
        for (i = 0; i < layers.length; i++) {
            _cache.push({ id: layers[i].id, name: layers[i].name, locked: layers[i].locked });
        }
    }

    // ----- §9  PREVIEW / DISPLAY (reads the cache, never the DOM) -----
    function refreshPreview() {
        var msg = emptyStateMsg();
        if (msg) { ui.preview.text = msg; setColor(ui.preview, DS.dimText); ui.apply.enabled = false; return; }
        refreshCache();
        var base = trimStr(ui.name.text) || "Layer";
        var first = base + "_01", last = base + "_" + pad(_cache.length);
        ui.preview.text = _cache.length === 1 ? (_cache[0].name + "  " + DS.arrow + "  " + first)
                                              : (first + "  " + DS.dash + "  " + last);
        setColor(ui.preview, DS.dimText);
        ui.apply.enabled = true;
    }
    function pad(n) { var s = "" + n; return s.length < 2 ? ("0" + s) : s; }

    // ----- §10  ACTION ENGINE (one undo group, closed in finally; locked skipped) -----
    function doApply() {
        if (_busy) { return; }
        var comp = app.project.activeItem;
        if (!(comp instanceof CompItem)) { return showStatus(DS.warn + "  Open a composition first", DS.warning); }
        _busy = true; ui.apply.enabled = false;
        app.beginUndoGroup("Rename layers");
        try {
            var base = trimStr(ui.name.text) || "Layer", done = 0, skipped = 0, n = 1, i, lyr;
            for (i = 0; i < _cache.length; i++) {
                lyr = byId(comp, _cache[i].id);                  // re-validate ref just-in-time (Cmd+Z is invisible)
                if (!lyr) { continue; }
                if (lyr.locked) { skipped++; continue; }
                lyr.name = base + "_" + pad(n); n++; done++;
            }
            var m = DS.ok + "  Renamed " + done + " layer" + (done === 1 ? "" : "s");
            if (skipped > 0) { m += " (" + skipped + " locked, skipped)"; }
            showStatus(m + " " + DS.dash + " Cmd+Z to undo", DS.success);
            Settings.set("base", base); Settings.set("aeVer", parseFloat(app.version));
        } catch (e) {
            showStatus(DS.fail + "  " + e.toString(), DS.error);
        } finally {
            app.endUndoGroup(); _busy = false; refreshPreview();
        }
    }
    function byId(comp, id) {
        try { var l = app.project.layerByID(id); return (l && l.containingComp === comp) ? l : null; } catch (e) { return null; }
    }

    function showStatus(msg, arr) { ui.status.text = msg; setColor(ui.status, arr || DS.dimText); }

    // ----- §5  BUILD UI -----
    var ui = {};
    function buildUI(parent) {
        var win = (parent instanceof Panel) ? parent : new Window("palette", "Tool Name", undefined, { resizeable: true });
        win.alignChildren = ["fill", "top"]; win.spacing = 6; win.margins = 10;

        var row = win.add("group"); row.alignment = ["fill", "top"]; row.spacing = 6;
        row.add("statictext", undefined, "Name");
        ui.name = row.add("edittext", undefined, Settings.get("base", "Layer"));
        ui.name.alignment = ["fill", "center"]; ui.name.helpTip = "Base name — e.g. 'BG' makes BG_01, BG_02 …";

        ui.preview = win.add("statictext", undefined, "", { truncate: "middle" });
        ui.preview.alignment = ["fill", "top"];

        ui.apply = win.add("button", undefined, "Rename");
        ui.apply.helpTip = "Rename the selected layers in sequence (Enter)";

        ui.status = win.add("statictext", undefined, "");
        ui.status.alignment = ["fill", "top"];

        // ----- §11  EVENT WIRING -----
        ui.name.onChanging = refreshPreview;                 // reads the cache only, never the DOM
        ui.name.onActivate = function () { refreshPreview(); };   // catches "selected then clicked in"
        ui.apply.onClick = doApply;
        ui.name.addEventListener("keydown", function (k) {
            if (k.keyName === "Enter" || k.keyName === "Return") { doApply(); }
        });
        win.onResizing = win.onResize = function () { try { this.layout.resize(); } catch (e) {} };

        if (win instanceof Window) { win.minimumSize = [DS.minW, 0]; }
        return win;
    }

    // ----- §12  INIT -----
    var panel = buildUI(thisObj);
    refreshPreview();
    if (panel instanceof Window) { panel.center(); panel.show(); }
    else { panel.layout.layout(true); }

})(this);
