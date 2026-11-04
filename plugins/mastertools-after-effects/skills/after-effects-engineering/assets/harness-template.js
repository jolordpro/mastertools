/* =====================================================================
 * Headless test harness template for After Effects ExtendScript
 * =====================================================================
 *
 * Runs AE script logic without opening After Effects, by stubbing the AE
 * object model and (optionally) ScriptUI. Run it with the JavaScriptCore
 * helper that ships with macOS:
 *
 *   JSC=/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc
 *   "$JSC" -e "var ARG_SRC='/abs/path/tool.jsx'; $(cat harness.js)"
 *
 * Two modes, pick per test file:
 *
 * Sections: §1 AE object model · §1b render-path stubs (callSystem, scheduleTask,
 * output-module settings, importFile verification, ScriptUI registry) · §2 ScriptUI ·
 * §3 loading · §4 assertions · §5 your tests.
 *
 *   SLICED      cut the ScriptUI panel off and test pure logic. No UI stubs
 *               needed. Best for preflight, name resolution, maths, naming.
 *   WHOLE-FILE  load everything against the ScriptUI stubs and drive the
 *               tool through its real buttons. The only way to test panel
 *               state machines and multi-item run loops.
 *
 * Search for TODO to find the parts that are project-specific.
 * ================================================================= */

var SRC = readFile(ARG_SRC);

/* =====================================================================
 * §1  AE OBJECT MODEL STUBS
 * ================================================================= */

var CALLS = [];        /* lifecycle trace: close / purge / open / save / undo */

function CompItem(name, w, h, layers, opts) {
    opts = opts || {};
    this.name = name;
    this.width = w || 1920;
    this.height = h || 1080;
    this.frameRate = opts.frameRate || 59.94;
    this.frameDuration = 1001 / 60000;                  /* TODO match your comp */
    this.duration = (opts.duration === undefined) ? 10 : opts.duration;
    this._layers = layers || [];
    this.numLayers = this._layers.length;
}
CompItem.prototype.layer = function (i) { return this._layers[i - 1]; };

function FootageItem(name, missing) {
    this.name = name;
    this.footageMissing = !!missing;
}

var PropertyValueType = {
    NO_VALUE: 0, ThreeD_SPATIAL: 1, ThreeD: 2, TwoD_SPATIAL: 3, TwoD: 4,
    OneD: 5, COLOR: 6, CUSTOM_VALUE: 7, MARKER: 8, LAYER_INDEX: 9,
    MASK_INDEX: 10, SHAPE: 11, TEXT_DOCUMENT: 12
};
var RQItemStatus = {
    WILL_CONTINUE: 0, NEEDS_OUTPUT: 1, UNQUEUED: 2, QUEUED: 3,
    RENDERING: 4, USER_STOPPED: 5, ERR_STOPPED: 6, DONE: 7
};
var CloseOptions = { DO_NOT_SAVE_CHANGES: 0, PROMPT_TO_SAVE_CHANGES: 1, SAVE_CHANGES: 2 };
var PurgeTarget  = { ALL_CACHES: 0, UNDO_CACHES: 1, SNAPSHOT_CACHES: 2,
                     IMAGE_CACHES: 3, ALL_MEMORY_CACHES: 4 };

function Prop(name, matchName, vt, value, opts) {
    opts = opts || {};
    this.name = name;
    this.matchName = matchName;
    this.propertyValueType = vt;
    this.value = value;
    this.canSetExpression = (opts.canSetExpression !== false);
    this.expressionEnabled = !!opts.expressionEnabled;
    this.numProperties = 0;
}
Prop.prototype.setValue = function (v) { this.value = v; };

function Effect(name, matchName, props, enabled) {
    this.name = name;
    this.matchName = matchName;
    this._props = props || [];
    this.numProperties = this._props.length;
    this.enabled = (enabled !== false);
}
Effect.prototype.property = function (i) { return this._props[i - 1]; };

function Parade(fx) { this._fx = fx || []; this.numProperties = this._fx.length; }
Parade.prototype.property = function (i) { return this._fx[i - 1]; };

function Layer(name, effects, enabled) {
    this.name = name;
    this.enabled = (enabled !== false);
    this._parade = effects ? new Parade(effects) : null;   /* null = camera/light */
    this.locked = false;
}
Layer.prototype.property = function (key) {
    return (key === "ADBE Effect Parade") ? this._parade : null;
};

/* Note displayName: real projects rename effects on layers, so a Fill may
   show as "COLOR". Exercise that — code must match on matchName. */
function fillEffect(opts) {
    opts = opts || {};
    return new Effect(opts.displayName || "Fill", "ADBE Fill", [
        new Prop("Fill Mask", "ADBE Fill-0001", PropertyValueType.MASK_INDEX, 0),
        new Prop("All Masks", "ADBE Fill-0007", PropertyValueType.OneD, 0),
        new Prop("Color", "ADBE Fill-0002", PropertyValueType.COLOR, [1, 1, 1, 1],
                 { expressionEnabled: !!opts.expr }),
        new Prop("Opacity", "ADBE Fill-0005", PropertyValueType.OneD, 100),
        /* property groups report an undefined value type — keeps `===` honest */
        new Prop("Compositing Options", "ADBE Effect Built In Params", undefined, null)
    ], opts.fxEnabled !== false);
}

/* ---- virtual filesystem ---- */

/* path -> true (2 KB stub) | "empty" (zero bytes) | {size, text} (real content).
 * All three shapes are honoured, so tests written against the older boolean
 * form keep working while newer ones can assert on written text and size. */
var FS = {};
var FOLDERS = {};   /* path -> true | "ro" (exists but unwritable) */

function Folder(p) { this.fsName = String(p); this.name = String(p).split("/").pop(); }
Folder.prototype.__defineGetter__("exists", function () { return !!FOLDERS[this.fsName]; });
Folder.prototype.getFiles = function () {
    var out = [], self = this;
    for (var k in FS) {
        if (!FS.hasOwnProperty(k)) { continue; }
        if (k.substring(0, k.lastIndexOf("/")) === self.fsName) { out.push(new File(k)); }
    }
    return out;
};
Folder.temp = new Folder("/tmp");
Folder.selectDialog = function () { return null; };
FOLDERS["/tmp"] = true;

function File(p) {
    this.fsName = String(p);
    this.name = String(p).split("/").pop();
    this.encoding = "";
}
File.prototype.__defineGetter__("exists", function () { return !!FS[this.fsName]; });
File.prototype.__defineGetter__("length", function () {
    var e = FS[this.fsName];
    if (e === undefined || e === "empty") { return 0; }
    if (e === true) { return 2048; }
    return e.size;
});
File.prototype.__defineGetter__("parent", function () {
    return new Folder(this.fsName.substring(0, this.fsName.lastIndexOf("/")));
});
File.prototype.open = function (mode) {
    var d = this.fsName.substring(0, this.fsName.lastIndexOf("/"));
    if (!FOLDERS[d] || FOLDERS[d] === "ro") { return false; }   /* returns false, does NOT throw */
    if (mode === undefined || String(mode).charAt(0) === "w") { FS[this.fsName] = { size: 0, text: "" }; }
    this._open = true;
    return true;
};
File.prototype.write = function (s) {
    if (!this._open) { return false; }          /* a script that ignores open()'s return gets caught */
    s = String(s);
    var e = FS[this.fsName];
    var txt = (e && e.text !== undefined) ? e.text : "";
    var sz  = (e && e.size !== undefined) ? e.size : 0;
    FS[this.fsName] = { size: sz + s.length, text: txt + s };
    WRITES.push(s);
    return true;
};
File.prototype.read = function () {
    var e = FS[this.fsName];
    if (e === undefined || e === true || e === "empty") { return ""; }
    return e.text;
};
File.prototype.close = function () { this._open = false; return true; };
File.prototype.remove = function () { delete FS[this.fsName]; return true; };
File.prototype.copy = function (dest) {                 /* copy does NOT overwrite */
    var t = (dest instanceof File) ? dest.fsName : String(dest);
    if (FS[t]) { return false; }
    FS[t] = true;
    return true;
};
var WRITES = [];    /* everything written through File.write, for log assertions */

/* Seed a file with a real size (and optionally content) from a test. */
function setFile(path, size, text) {
    FS[String(path)] = { size: (size === undefined ? 2048 : size), text: (text === undefined ? "" : text) };
}

/* ---- render queue with a simulated renderer ---- */

var SIM = {
    mode: "ok",              /* ok | failStatus | noFile | zeroByte | multiFile        */
    numbered: false,         /* AE appended its frame counter to the filename          */
    failFirst: 0,            /* fail this many attempts, then succeed (transient errs) */
    attempt: 0,
    outputBytes: 165000000,  /* size a successful render writes                        */
    rejectOMSettings: false, /* setSettings silently does nothing                      */
    rejectOMTemplate: false, /* applyTemplate throws (template absent on this machine) */
    ignoreOMFile: false      /* om.file set, but the name template wins                */
};
var OM_TEMPLATES = ["Lossless", "High Quality", "PNG - Not Trans"];   /* TODO */
var RS_TEMPLATES = ["Best Settings", "Draft Settings"];               /* TODO */

function RenderQueue(preExistingCount) {
    this._items = [];
    for (var i = 0; i < (preExistingCount || 0); i++) {
        /* the user's own queued work — must never render, must never be lost */
        this._items.push({ render: true, status: RQItemStatus.QUEUED, _pre: true });
    }
    this.numItems = this._items.length;
    var self = this;
    this.items = {
        add: function (comp) {
            var it = {
                render: false,
                status: RQItemStatus.QUEUED,
                templates: RS_TEMPLATES,
                timeSpanStart: 0,
                timeSpanDuration: comp.duration,
                _comp: comp,
                _om: (function () {
                    /* Models the two things that silently go wrong on a real output
                     * module: a setting that refuses to change, and a file path that
                     * loses to the module's own [compName].[fileExtension] template. */
                    var om = {
                        templates: OM_TEMPLATES,
                        name: "",
                        _file: new File("/tmp/probe.mov"),
                        _settings: {
                            "Output Audio": "Auto",
                            "Channels": "RGB + Alpha",
                            "Format": "QuickTime",
                            "Output File Info": {
                                "Full Flat Path": "/tmp/probe.mov",
                                "File Name": "probe.mov",
                                "File Template": "[compName].[fileExtension]"
                            }
                        },
                        applyTemplate: function (n) {
                            if (SIM.rejectOMTemplate) { throw new Error("no output module template " + n); }
                            this._tpl = n; this.name = n;
                        },
                        getSettings: function () { return this._settings; },
                        setSettings: function (o) {
                            if (SIM.rejectOMSettings) { return; }   /* silently refuses */
                            for (var k in o) { if (o.hasOwnProperty(k)) { this._settings[k] = o[k]; } }
                        }
                    };
                    om.__defineGetter__("file", function () { return om._file; });
                    om.__defineSetter__("file", function (f) {
                        om._file = f;
                        if (SIM.ignoreOMFile) { return; }           /* template wins instead */
                        om._settings["Output File Info"]["Full Flat Path"] = f.fsName;
                        om._settings["Output File Info"]["File Name"] = f.name;
                    });
                    return om;
                }()),
                getSettings: function () {
                    return {
                        "Resolution": "Full", "Quality": "Best",
                        "Time Span": "Custom",
                        "Time Span Duration": String(this.timeSpanDuration)
                    };
                },
                applyTemplate: function (n) {
                    this._rs = n;
                    /* real applyTemplate may reset the span — model the worst case */
                    this.timeSpanStart = 0;
                    this.timeSpanDuration = this._comp.duration;
                },
                outputModule: function () { return this._om; },
                remove: function () {
                    for (var k = 0; k < self._items.length; k++) {
                        if (self._items[k] === it) { self._items.splice(k, 1); break; }
                    }
                    self.numItems = self._items.length;
                }
            };
            /* the reported float-precision range error at exactly frameDuration */
            if (SIM.precisionThrow) {
                var _d = comp.duration;
                it.__defineSetter__("timeSpanDuration", function (v) {
                    if (v <= comp.frameDuration) {
                        throw new Error("Value 0.03 out of range 0.03 to 71654440");
                    }
                    _d = v;
                });
                it.__defineGetter__("timeSpanDuration", function () { return _d; });
            }
            if (SIM.rejectSpan) {   /* span silently refuses to narrow */
                it.__defineSetter__("timeSpanDuration", function () {});
                it.__defineGetter__("timeSpanDuration", function () { return comp.duration; });
            }
            self._items.push(it);
            self.numItems = self._items.length;
            return it;
        }
    };
}
RenderQueue.prototype.item = function (i) { return this._items[i - 1]; };
RenderQueue.prototype.render = function () {
    for (var i = 0; i < this._items.length; i++) {
        var it = this._items[i];
        if (!it.render || it._pre) { continue; }     /* _pre rendering = test failure */
        SIM.attempt++;
        if (SIM.failFirst >= SIM.attempt) { it.status = RQItemStatus.ERR_STOPPED; continue; }
        if (SIM.mode === "failStatus") { it.status = RQItemStatus.ERR_STOPPED; continue; }

        it.status = RQItemStatus.DONE;
        var nm = it._om.file.fsName;
        if (SIM.mode === "noFile") { continue; }
        if (SIM.mode === "zeroByte") { FS[nm] = "empty"; continue; }
        if (SIM.mode === "multiFile") {              /* a sprayed sequence */
            var dot = nm.lastIndexOf(".");
            for (var n = 1; n <= 3; n++) {
                FS[nm.substring(0, dot) + "_0000" + n + nm.substring(dot)] = true;
            }
            continue;
        }
        if (SIM.numbered) {                          /* AE appended _#####  */
            var d2 = nm.lastIndexOf(".");
            setFile(nm.substring(0, d2) + "_00111" + nm.substring(d2), SIM.outputBytes);
            continue;
        }
        setFile(nm, SIM.outputBytes);
    }
};

/* ---- app ---- */

var PREFS = {};
var app = {
    version: "26.3x87",
    onError: null,
    beginSuppressDialogs: function () {},
    endSuppressDialogs: function () {},
    beginUndoGroup: function () { CALLS.push("undoOpen"); },
    endUndoGroup: function () { CALLS.push("undoClose"); },
    purge: function (t) {
        var n = ["ALL", "UNDO", "SNAP", "IMG", "ALLMEM"];
        CALLS.push("purge:" + n[t]);
    },
    findMenuCommandId: function (s) { return s === "All Memory & Disk Cache" ? 2372 : 0; },
    scheduleTask: function (str) { SCHEDULED = str; return 1; },
    cancelTask: function () { SCHEDULED = null; },
    preferences: {
        getPrefAsLong: function (sec, k) { return PREFS[k] === undefined ? 1 : PREFS[k]; },
        savePrefAsLong: function (sec, k, v) { PREFS[k] = v; }
    },
    executeCommand: function () { CALLS.push("purge:disk"); },
    open: function (f) {
        CALLS.push("open:" + f.name);
        app.project = makeProject({ file: f });
        return app.project;
    },
    settings: {
        haveSetting: function (sec, k) { return PREFS.hasOwnProperty(k); },
        getSetting: function (sec, k) { return PREFS[k]; },
        saveSetting: function (sec, k, v) { PREFS[k] = v; }
    },
    project: null
};
var $ = { sleep: function () {}, global: {} };
function alert() { CALLS.push("ALERT"); }     /* assert this stays at 0 */

/* =====================================================================
 * §1b  RENDER-PATH STUBS
 * =====================================================================
 * The pieces a batch-render tool actually touches, which the plain object
 * model above does not reach: shelling out, the async task loop, and
 * verifying an output by re-importing it.
 */

/* ---- system.callSystem, backed by the virtual filesystem ---- */

var SYS_CALLS = [];         /* every shell command, for assertions */
var FREE_KB = 800000000;    /* what `df -k` reports as available   */

var system = {
    callSystem: function (cmd) {
        cmd = String(cmd);
        SYS_CALLS.push(cmd);
        var m;
        if (/\bdf\b/.test(cmd)) {
            return "Filesystem 1024-blocks Used Available Capacity\n" +
                   "/dev/disk1s5 3900000000 100000000 " + FREE_KB + " 79%\n";
        }
        if ((m = cmd.match(/\bmv\b(?:\s+-\w+)*\s+'([^']+)'\s+'([^']+)'/))) {
            if (FS[m[1]] === undefined) { return ""; }
            FS[m[2]] = FS[m[1]];
            delete FS[m[1]];
            return "";
        }
        if ((m = cmd.match(/\bcp\b(?:\s+-\w+)*\s+'([^']+)'\s+'([^']+)'/))) {
            if (FS[m[1]] === undefined) { return ""; }
            var e = FS[m[1]];
            FS[m[2]] = (e && e.size !== undefined) ? { size: e.size, text: e.text } : e;
            return "";
        }
        return "";
    }
};

/* ---- app.scheduleTask: an async run loop, pumped by the test ---- *
 * A long batch should yield between items so Stop stays live and the UI
 * repaints. Driving it from the test also keeps the stack flat, so a
 * 122-item run does not blow the recursion limit.
 */
var SCHEDULED = null;
function pump(maxTicks) {
    var n = 0, s;
    while (SCHEDULED !== null && n < (maxTicks || 5000)) {
        s = SCHEDULED;
        SCHEDULED = null;
        eval(s);
        n++;
    }
    return n;                /* ticks executed */
}

/* ---- importing a rendered file back to verify it ---- *
 * The only check that catches a silently audio-less or truncated render.
 */
var VERIFY = { duration: 2.002002002002, hasAudio: true, hasVideo: true, throwOnImport: false };
function ImportOptions(f) { this.file = f; this.importAs = 0; }

/* ---- flat ScriptUI registry, so tests can find a control by its label ---- */
var ALLCTRL = [];
function findW(type, frag) {
    for (var i = 0; i < ALLCTRL.length; i++) {
        if (ALLCTRL[i].type === type && String(ALLCTRL[i].text).indexOf(frag) >= 0) { return ALLCTRL[i]; }
    }
    return null;
}
function findAllW(type) {
    var out = [], i;
    for (i = 0; i < ALLCTRL.length; i++) { if (ALLCTRL[i].type === type) { out.push(ALLCTRL[i]); } }
    return out;
}

/* TODO — build the project your script expects. Include the ugly parts of
   the real one: junk layers, duplicate names, renamed effects, a populated
   render queue. A harness that only models the happy project proves little. */
function makeProject(opt) {
    opt = opt || {};
    var items = [
        new CompItem("MY_COMP", 1920, 1080, [
            new Layer("TARGET LAYER", [fillEffect({})], true),
            new Layer("GUIDE", null, true)
        ]),
        new CompItem("*RENDER", 1920, 1080, [new Layer("x", null, true)]),
        new FootageItem("plate.png", !!opt.missingFootage)
    ];
    var proj = {
        numItems: items.length,
        item: function (n) { return items[n - 1]; },
        file: opt.unsaved ? null : (opt.file || new File("/proj/master.aep")),
        renderQueue: new RenderQueue(opt.queueCount === undefined ? 52 : opt.queueCount),
        importFile: function (io) {
            CALLS.push("import:" + io.file.name);
            if (VERIFY.throwOnImport) { throw new Error("Unsupported filetype or damaged file"); }
            return {
                name: io.file.name,
                duration: VERIFY.duration,
                hasAudio: VERIFY.hasAudio,
                hasVideo: VERIFY.hasVideo,
                remove: function () { CALLS.push("importRemoved"); }
            };
        },
        close: function () { CALLS.push("close"); return true; },
        save: function (f) { CALLS.push("save:" + f.name); FS[f.fsName] = true; proj.file = f; return true; }
    };
    return proj;
}

/* =====================================================================
 * §2  SCRIPTUI STUBS   (whole-file mode only — delete for sliced mode)
 * ================================================================= */

function Panel() { initCtrl(this); this.type = "panel"; this.text = ""; ALLCTRL.push(this); }
function Window(kind, title) {
    initCtrl(this);
    this.type = "window"; this.text = title === undefined ? "" : title;
    this._title = title;
    ALLCTRL.push(this);
}
Window.prototype.close = function () {};
Window.prototype.center = function () {};
Window.prototype.show = function () {};

function Ctrl(type, text, opts) {
    initCtrl(this);
    this.type = type;
    this.text = (text === undefined) ? "" : text;
    this._opts = opts || {};
}

function initCtrl(o) {
    o._children = [];
    o.enabled = true;
    o.visible = true;
    o.preferredSize = { width: 0, height: 0 };
    o.layout = { layout: function () {}, resize: function () {} };
    o.add = ctrlAdd;
    o.update = function () {};
    o.hide = function () {};
    o.show = function () {};
}

function ctrlAdd(type, bounds, text, opts) {
    var c = (type === "listbox") ? new ListBox() : new Ctrl(type, text, opts);
    if (type === "checkbox") { c.value = false; }
    if (type === "progressbar") { c.value = 0; c.minvalue = 0; c.maxvalue = 1; }
    this._children.push(c);
    c._parent = this;
    ALLCTRL.push(c);            /* flat registry — findW(type, labelFragment) */
    return c;
}

function ListBox() {
    initCtrl(this);            /* assigns an own .add — must override it below */
    this.type = "listbox";
    this.items = [];
    this._sel = [];
    var self = this;
    this.add = function (kind, txt) {
        var it = { text: txt, subItems: [{ text: "" }, { text: "" }, { text: "" }, { text: "" }] };
        self.items.push(it);
        return it;
    };
    this.removeAll = function () { self.items = []; self._sel = []; };
    this.__defineGetter__("selection", function () { return self._sel.length ? self._sel : null; });
    this.__defineSetter__("selection", function (v) {
        if (v === null || v === undefined) { self._sel = []; return; }
        var arr = (v instanceof Array) ? v : [v];
        self._sel = [];
        for (var i = 0; i < arr.length; i++) {
            var x = arr[i];
            if (typeof x === "number") { if (self.items[x]) { self._sel.push(self.items[x]); } }
            else { self._sel.push(x); }
        }
        if (typeof self.onChange === "function") { self.onChange(); }
    });
}

function walk(root, out) {
    out = out || [];
    for (var i = 0; i < root._children.length; i++) {
        out.push(root._children[i]);
        walk(root._children[i], out);
    }
    return out;
}
/* Filter on type: a statictext can easily share a prefix with its button. */
function findButton(root, frag) {
    var all = walk(root);
    for (var i = 0; i < all.length; i++) {
        if (all[i].type === "button" && String(all[i].text).indexOf(frag) === 0) { return all[i]; }
    }
    return null;
}
function findLabel(root, frag) {
    var all = walk(root);
    for (var i = 0; i < all.length; i++) {
        if (all[i].type === "statictext" && String(all[i].text).indexOf(frag) === 0) { return all[i]; }
    }
    return null;
}

/* =====================================================================
 * §3  LOADING THE SCRIPT
 * ================================================================= */

/* -- SLICED MODE: cut the panel off, export the internals -------------
 * Pick a marker that reliably precedes the UI (a section comment works).
 */
function sliceBody(src, panelMarker) {
    var open = src.indexOf("(function (thisObj) {");
    if (open < 0) { throw new Error("IIFE opener not found"); }
    var p = src.indexOf(panelMarker);
    if (p < 0) { throw new Error("panel marker not found: " + panelMarker); }
    var cut = src.lastIndexOf("/* =", p);
    return src.substring(open + "(function (thisObj) {".length, cut);
}

function loadSliced(panelMarker, exportList) {
    var body = sliceBody(SRC, panelMarker);
    var ret = "\nreturn {" + exportList + "};\n";
    var f = new Function("app", "PropertyValueType", "RQItemStatus", "CompItem",
                         "FootageItem", "File", "Folder", "$", "CloseOptions",
                         "PurgeTarget", body + ret);
    return f(app, PropertyValueType, RQItemStatus, CompItem, FootageItem,
             File, Folder, $, CloseOptions, PurgeTarget);
}

/* -- WHOLE-FILE MODE: load everything, drive the real buttons ---------
 * `this` inside the loaded function becomes the Panel, so the script's
 * `(function (thisObj) { ... })(this)` receives it and builds into it.
 */
function loadWhole() {
    var f = new Function("app", "PropertyValueType", "RQItemStatus", "CompItem",
                         "FootageItem", "File", "Folder", "$", "CloseOptions",
                         "PurgeTarget", "Panel", "Window", "alert", SRC);
    var root = new Panel();
    f.call(root, app, PropertyValueType, RQItemStatus, CompItem, FootageItem,
           File, Folder, $, CloseOptions, PurgeTarget, Panel, Window, alert);
    return root;
}

/* =====================================================================
 * §4  ASSERTIONS
 * ================================================================= */

var PASS = 0, FAIL = 0;

function chk(label, got, want) {
    var g = String(got), w = String(want);
    if (g === w) { PASS++; print("  ok   " + label + "  -> " + g); }
    else { FAIL++; print("  FAIL " + label + "\n         got  " + g + "\n         want " + w); }
}

/* Verifies the invariants that are tedious to eyeball and easy to regress:
   every open preceded by a close and a purge, and no save or open while an
   undo group is still open. */
function orderViolations(trace) {
    var closed = false, purged = false, opens = 0, undo = 0, bad = [];
    for (var i = 0; i < trace.length; i++) {
        var c = trace[i];
        if (c === "close") { closed = true; }
        if (c.indexOf("purge:") === 0) { purged = true; }
        if (c === "undoOpen") { undo++; }
        if (c === "undoClose") { undo--; }
        if (c.indexOf("save:") === 0 && undo !== 0) { bad.push("save at undo depth " + undo); }
        if (c.indexOf("open:") === 0) {
            opens++;
            if (undo !== 0) { bad.push("open #" + opens + " at undo depth " + undo); }
            if (!closed) { bad.push("open #" + opens + " without a preceding close"); }
            if (!purged) { bad.push("open #" + opens + " without a preceding purge"); }
            closed = false; purged = false;
        }
    }
    if (undo !== 0) { bad.push("undo depth ended at " + undo); }
    return { opens: opens, bad: bad };
}

function resetWorld() {
    FS = {}; FOLDERS = { "/tmp": true };      /* TODO add your folders */
    Folder.temp = new Folder("/tmp");
    CALLS = []; WRITES = []; PREFS = {}; SYS_CALLS = []; ALLCTRL = [];
    SCHEDULED = null;
    FREE_KB = 800000000;
    SIM = { mode: "ok", numbered: false, failFirst: 0, attempt: 0,
            outputBytes: 165000000, rejectOMSettings: false,
            rejectOMTemplate: false, ignoreOMFile: false };
    VERIFY = { duration: 2.002002002002, hasAudio: true, hasVideo: true, throwOnImport: false };
    app.project = makeProject({});
}

/* =====================================================================
 * §5  TESTS   — TODO write yours
 * =================================================================
 *
 * Coverage worth having, roughly in value order:
 *
 *   Preflight reports and never throws, for each broken project you can
 *   construct: wrong project, comp renamed, comp ambiguous, layer missing,
 *   layer duplicated, effect disabled, expression on a target, unsaved
 *   project, folder missing / read-only, template absent, missing footage.
 *
 *   Apply logic writes the right values and touches nothing outside the
 *   whitelist — assert on the layers that must NOT change, not just the
 *   ones that must.
 *
 *   Render paths: exact output filename, numbered output absorbed, retry
 *   after a transient failure, give up cleanly after N, zero-byte rejected,
 *   scratch cleaned up on the failure path.
 *
 *   The user's pre-existing queue items: never rendered, never lost.
 *
 *   Lifecycle ordering via orderViolations(CALLS).
 *
 *   No alert() for an expected condition.
 */

resetWorld();
print("======================================================");
print(" harness");
print("======================================================");

/* Example — whole-file mode:
 *
 *   FOLDERS["/out"] = true;
 *   FS["/proj/master.aep"] = true;          // openProjectClean checks existence
 *   PREFS = { outFolder: "/out", selection: "A,B" };
 *   var root = loadWhole();
 *   var go = findButton(root, "Build");
 *   chk("button enabled after preflight", go.enabled, "true");
 *   CALLS = [];
 *   go.onClick();
 *   var ord = orderViolations(CALLS);
 *   chk("ordering violations", ord.bad.length === 0 ? "none" : ord.bad.join("; "), "none");
 */

print("");
print("======================================================");
print(" " + PASS + " passed, " + FAIL + " failed");
print("======================================================");
