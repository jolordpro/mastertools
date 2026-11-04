//@target aftereffects
/* ae_readout.jsx: read-only comp readout for /elevate (After Effects, strict ES3).

   Run: File > Scripts > Run Script File... with the comp open (or selected in the Project panel).
   Writes <project>_<comp>_elevate_readout.json next to the saved .aep. If the project has
   never been saved, a save dialog asks where to put it. Changes nothing in the project.

   Needs: Preferences > Scripting & Expressions > Allow Scripts to Write Files and Access Network.
   Reports one status message at the end; caps are listed in the JSON "notes". */
(function () {
    var VERSION = "1.0";
    var MAX_KEYS_PER_PROP = 64;
    var MAX_ANIMATED_PROPS = 300;
    var MAX_EFFECT_PARAMS = 24;
    var notes = [];
    var animatedCount = 0;
    var animatedCapped = false;

    function rnd(n, d) {
        var m = Math.pow(10, (d === undefined) ? 3 : d);
        return Math.round(n * m) / m;
    }

    function jsonStr(s) {
        var str = String(s);
        var out = "\"";
        for (var i = 0; i < str.length; i++) {
            var c = str.charAt(i);
            var code = str.charCodeAt(i);
            if (c === "\"" || c === "\\") {
                out += "\\" + c;
            } else if (code < 32) {
                out += "\\u" + ("0000" + code.toString(16)).slice(-4);
            } else {
                out += c;
            }
        }
        return out + "\"";
    }

    function toJSON(v) {
        if (v === null || v === undefined) { return "null"; }
        var t = typeof v;
        if (t === "number") { return isFinite(v) ? String(v) : "null"; }
        if (t === "boolean") { return v ? "true" : "false"; }
        if (t === "string") { return jsonStr(v); }
        var parts = [];
        if (v instanceof Array) {
            for (var i = 0; i < v.length; i++) { parts.push(toJSON(v[i])); }
            return "[" + parts.join(",") + "]";
        }
        for (var k in v) {
            if (v.hasOwnProperty(k)) { parts.push(jsonStr(k) + ":" + toJSON(v[k])); }
        }
        return "{" + parts.join(",") + "}";
    }

    function enumName(enumObj, value) {
        try {
            for (var k in enumObj) {
                if (enumObj[k] === value) { return k; }
            }
        } catch (e) {}
        return value;
    }

    function simpleValue(p) {
        try {
            if (p.propertyType !== PropertyType.PROPERTY) { return undefined; }
            var vt = p.propertyValueType;
            if (vt === PropertyValueType.NO_VALUE || vt === PropertyValueType.CUSTOM_VALUE ||
                    vt === PropertyValueType.MARKER || vt === PropertyValueType.SHAPE ||
                    vt === PropertyValueType.TEXT_DOCUMENT) { return undefined; }
            var v = p.value;
            if (typeof v === "number") { return rnd(v, 4); }
            if (typeof v === "boolean" || typeof v === "string") { return v; }
            if (v instanceof Array) {
                var arr = [];
                for (var i = 0; i < v.length; i++) { arr.push(typeof v[i] === "number" ? rnd(v[i], 4) : null); }
                return arr;
            }
        } catch (e) {}
        return undefined;
    }

    function layerKind(L) {
        if (L instanceof TextLayer) { return "text"; }
        if (L instanceof ShapeLayer) { return "shape"; }
        if (L instanceof CameraLayer) { return "camera"; }
        if (L instanceof LightLayer) { return "light"; }
        if (L instanceof AVLayer) {
            if (L.adjustmentLayer) { return "adjustment"; }
            if (L.nullLayer) { return "null"; }
            if (L.source && L.source instanceof CompItem) { return "precomp"; }
            return "av";
        }
        return "other";
    }

    function readEffects(L) {
        var out = [];
        var parade = null;
        try { parade = L.property("ADBE Effect Parade"); } catch (e) {}
        if (!parade) { return out; }
        for (var i = 1; i <= parade.numProperties; i++) {
            var fx = parade.property(i);
            var e = { name: fx.name, matchName: fx.matchName, params: {} };
            try { e.enabled = fx.enabled; } catch (e1) {}
            var n = 0;
            for (var j = 1; j <= fx.numProperties; j++) {
                if (n >= MAX_EFFECT_PARAMS) { e.paramsCapped = true; break; }
                var v = simpleValue(fx.property(j));
                if (v !== undefined) { e.params[fx.property(j).name] = v; n++; }
            }
            out.push(e);
        }
        return out;
    }

    function readText(L) {
        try {
            var tp = L.property("ADBE Text Properties");
            var td = tp.property("ADBE Text Document").value;
            var t = { text: String(td.text).substring(0, 120), font: td.font,
                      fontSize: rnd(td.fontSize, 2), tracking: td.tracking };
            try { t.autoLeading = td.autoLeading; } catch (e1) {}
            try { if (!td.autoLeading) { t.leading = rnd(td.leading, 2); } } catch (e2) {}
            try { t.allCaps = td.allCaps; } catch (e3) {}
            try { t.animators = tp.property("ADBE Text Animators").numProperties; } catch (e4) {}
            return t;
        } catch (e) {
            return { error: String(e) };
        }
    }

    function readCamera(L) {
        var o = null;
        try { o = L.property("ADBE Camera Options Group"); } catch (e) {}
        function g(mn) {
            try { return rnd(o.property(mn).value, 3); } catch (e2) { return null; }
        }
        return { zoom: g("ADBE Camera Zoom"), depthOfField: g("ADBE Camera Depth of Field"),
                 focusDistance: g("ADBE Camera Focus Distance"), aperture: g("ADBE Camera Aperture"),
                 blurLevel: g("ADBE Camera Blur Level") };
    }

    function readLight(L) {
        var o = null;
        var r = {};
        try { r.lightType = enumName(LightType, L.lightType); } catch (e) {}
        try { o = L.property("ADBE Light Options Group"); } catch (e1) {}
        function g(mn) {
            try { return simpleValue(o.property(mn)); } catch (e2) { return null; }
        }
        r.intensity = g("ADBE Light Intensity");
        r.color = g("ADBE Light Color");
        r.coneAngle = g("ADBE Light Cone Angle");
        r.castsShadows = g("ADBE Light Casts Shadows");
        return r;
    }

    function near(a, b, tol) { return Math.abs(a - b) <= tol; }

    function readKeys(p, label) {
        var r = { property: label, matchName: p.matchName, numKeys: p.numKeys, keys: [],
                  linear: 0, easyEaseDefault: 0, hold: 0, custom: 0 };
        var n = Math.min(p.numKeys, MAX_KEYS_PER_PROP);
        if (p.numKeys > MAX_KEYS_PER_PROP) { r.keysCapped = true; }
        for (var k = 1; k <= n; k++) {
            var kin = p.keyInInterpolationType(k);
            var kout = p.keyOutInterpolationType(k);
            var key = { t: rnd(p.keyTime(k), 4), inType: enumName(KeyframeInterpolationType, kin),
                        outType: enumName(KeyframeInterpolationType, kout) };
            var ie = null;
            var oe = null;
            try { ie = p.keyInTemporalEase(k)[0]; oe = p.keyOutTemporalEase(k)[0]; } catch (e) {}
            if (ie && oe) {
                key.inSpeed = rnd(ie.speed, 3); key.inInfluence = rnd(ie.influence, 2);
                key.outSpeed = rnd(oe.speed, 3); key.outInfluence = rnd(oe.influence, 2);
            }
            if (kin === KeyframeInterpolationType.HOLD || kout === KeyframeInterpolationType.HOLD) {
                r.hold++;
            } else if (kin === KeyframeInterpolationType.LINEAR && kout === KeyframeInterpolationType.LINEAR) {
                r.linear++;
            } else if (ie && oe && near(ie.influence, 33.333, 0.5) && near(oe.influence, 33.333, 0.5) &&
                       near(ie.speed, 0, 0.001) && near(oe.speed, 0, 0.001)) {
                r.easyEaseDefault++;
            } else {
                r.custom++;
            }
            r.keys.push(key);
        }
        return r;
    }

    function walkKeys(group, path, out) {
        for (var i = 1; i <= group.numProperties; i++) {
            var p = null;
            try { p = group.property(i); } catch (e) {}
            if (!p) { continue; }
            if (p.propertyType === PropertyType.PROPERTY) {
                var nk = 0;
                try { nk = p.numKeys; } catch (e2) {}
                if (nk > 0) {
                    if (animatedCount >= MAX_ANIMATED_PROPS) { animatedCapped = true; return; }
                    out.push(readKeys(p, path + p.name));
                    animatedCount++;
                }
            } else {
                walkKeys(p, path + p.name + " > ", out);
            }
        }
    }

    function safeName(s) {
        return String(s).replace(/[^A-Za-z0-9_\-]+/g, "_").substring(0, 60);
    }

    function findComp() {
        if (!app.project) { return null; }
        var item = app.project.activeItem;
        if (item && item instanceof CompItem) { return item; }
        var sel = app.project.selection;
        for (var i = 0; i < sel.length; i++) {
            if (sel[i] instanceof CompItem) { return sel[i]; }
        }
        return null;
    }

    function run() {
        var comp = findComp();
        if (!comp) { return "elevate readout: open or select a comp first. Nothing was written."; }

        var data = { tool: "elevate ae_readout", version: VERSION, notes: notes };
        var proj = {};
        try { proj.bitsPerChannel = app.project.bitsPerChannel; } catch (e1) {}
        try { proj.linearBlending = app.project.linearBlending; } catch (e2) {}
        try { proj.workingSpace = app.project.workingSpace; } catch (e3) {}
        try { proj.file = app.project.file ? app.project.file.name : null; } catch (e4) {}
        data.project = proj;

        var c = { name: comp.name, width: comp.width, height: comp.height,
                  frameRate: rnd(comp.frameRate, 3), duration: rnd(comp.duration, 3), numLayers: comp.numLayers };
        try { c.pixelAspect = comp.pixelAspect; } catch (e5) {}
        try { c.motionBlur = comp.motionBlur; c.shutterAngle = comp.shutterAngle; c.shutterPhase = comp.shutterPhase; } catch (e6) {}
        try { c.renderer = comp.renderer; } catch (e7) {}
        data.comp = c;

        var layers = [];
        for (var i = 1; i <= comp.numLayers; i++) {
            var L = comp.layer(i);
            var kind = layerKind(L);
            var e = { index: i, name: L.name, kind: kind, inPoint: rnd(L.inPoint, 3), outPoint: rnd(L.outPoint, 3) };
            try { e.enabled = L.enabled; } catch (e8) {}
            try { e.threeD = L.threeDLayer; } catch (e9) {}
            try { e.blendingMode = enumName(BlendingMode, L.blendingMode); } catch (e10) {}
            try { e.parent = L.parent ? L.parent.name : null; } catch (e11) {}
            if (kind === "text") { e.text = readText(L); }
            if (kind === "camera") { e.camera = readCamera(L); }
            if (kind === "light") { e.light = readLight(L); }
            e.effects = readEffects(L);
            e.animated = [];
            walkKeys(L, "", e.animated);
            layers.push(e);
        }
        data.layers = layers;

        var totals = { linear: 0, easyEaseDefault: 0, hold: 0, custom: 0, animatedProperties: animatedCount };
        for (var a = 0; a < layers.length; a++) {
            for (var b = 0; b < layers[a].animated.length; b++) {
                var r = layers[a].animated[b];
                totals.linear += r.linear; totals.easyEaseDefault += r.easyEaseDefault;
                totals.hold += r.hold; totals.custom += r.custom;
            }
        }
        data.easeTotals = totals;
        if (animatedCapped) { notes.push("animated properties capped at " + MAX_ANIMATED_PROPS); }
        notes.push("keys capped at " + MAX_KEYS_PER_PROP + " per property; effect params capped at " + MAX_EFFECT_PARAMS);
        notes.push("read-only dump; values are for diagnosis only");

        var target = null;
        if (app.project.file) {
            var base = String(app.project.file.name).replace(/\.aepx?$/i, "");
            target = new File(app.project.file.parent.fsName + "/" + safeName(base) + "_" +
                              safeName(comp.name) + "_elevate_readout.json");
        } else {
            target = File.saveDialog("Save /elevate readout as", "JSON:*.json");
            if (!target) { return "elevate readout: no file chosen. Nothing was written."; }
        }
        target.encoding = "UTF-8";
        if (!target.open("w")) {
            return "elevate readout: could not write " + target.fsName +
                   ". Check Preferences > Scripting & Expressions > Allow Scripts to Write Files and Access Network.";
        }
        target.write(toJSON(data));
        target.close();
        if (!target.exists) { return "elevate readout: write reported success but the file is missing: " + target.fsName; }
        return "elevate readout written:\n" + target.fsName + "\n" + layers.length + " layers, " +
               animatedCount + " animated properties (" + totals.easyEaseDefault + " default Easy Ease keys, " +
               totals.linear + " linear).";
    }

    var status;
    try {
        status = run();
    } catch (err) {
        status = "elevate readout failed: " + err.toString() + (err.line ? " (line " + err.line + ")" : "");
    }
    alert(status);
}());
