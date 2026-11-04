/**
 * probe-project.jsx — one-round-trip reconnaissance for an open AE project.
 *
 * Answers "what am I actually working with" BEFORE you write a line of tool code:
 * comps, grouped layer geometry, audio/lock/solo flags, footage sources, render-queue
 * state and the template lists that actually exist on THIS machine.
 *
 * It aggregates in-script. A 63-layer comp reports as ~12 lines, not 63 — so the
 * answer arrives in one read instead of a dump you then have to parse.
 *
 * Run it from a shell and read the file it writes:
 *
 *   osascript -e 'tell application id "com.adobe.AfterEffects.application" \
 *     to DoScriptFile POSIX file "/abs/path/probe-project.jsx"'
 *   cat /tmp/ae_probe.txt
 *
 * Bundle-id note: it is com.adobe.AfterEffects.application, NOT com.adobe.AfterEffects.
 *
 * Read-only except for one deliberate, fully-reversed mutation: reading the live
 * render-settings / output-module template lists requires parking a throwaway render
 * queue item, which is removed in a finally. Set CFG.readTemplates = false to skip it.
 *
 * Everything is wrapped so a broken project produces a REPORT, never a modal — an
 * error dialog in AE blocks the next `do javascript` and looks exactly like a hang.
 */

(function () {

    var CFG = {
        out:           "/tmp/ae_probe.txt",  /* where to write the report             */

        /* Comps are INDEXED (one line each) by default and DETAILED only on request.
         * A 77-comp project would otherwise bury the answer in 17 KB of layer dumps. */
        comps:         [],                   /* names to show in full detail          */
        autoDetailUnder: 5,                  /* <= this many comps total: detail all  */
        maxIndex:      60,                   /* cap on the one-line comp index        */

        sampleNames:   6,                    /* names shown per geometry group        */
        maxFolders:    12,                   /* source folders listed, by count desc  */
        namePattern:   "",                   /* e.g. "^[A-Z]{2,3}_[A-Z]{2,3}\\.mov$"  */
        readTemplates: true                  /* parks + removes one RQ item           */
    };

    /* Long repeated paths are most of the noise in a real project. */
    var SHORT = [];
    function shorten(s) {
        var i;
        s = String(s);
        for (i = 0; i < SHORT.length; i++) {
            if (s.indexOf(SHORT[i][0]) === 0) { return SHORT[i][1] + s.substring(SHORT[i][0].length); }
        }
        return s;
    }

    var L = [];
    function p(s) { L.push(String(s)); }
    function pad(s, n) { s = String(s); while (s.length < n) { s += " "; } return s; }
    function rpad(s, n) { s = String(s); while (s.length < n) { s = " " + s; } return s; }

    /* seconds -> frames, which is the unit that actually matters */
    function fr(t, fps) {
        if (t === undefined || t === null || fps === undefined || !fps) { return "?"; }
        return Math.round(t * fps) + "f";
    }
    function resName(rf) {
        if (!rf) { return "?"; }
        if (rf[0] === 1 && rf[1] === 1) { return "Full"; }
        if (rf[0] === 2 && rf[1] === 2) { return "Half"; }
        if (rf[0] === 3 && rf[1] === 3) { return "Third"; }
        if (rf[0] === 4 && rf[1] === 4) { return "Quarter"; }
        return rf[0] + "," + rf[1];
    }
    function statusName(s) {
        try {
            if (s === RQItemStatus.DONE)         { return "DONE"; }
            if (s === RQItemStatus.QUEUED)       { return "QUEUED"; }
            if (s === RQItemStatus.UNQUEUED)     { return "UNQUEUED"; }
            if (s === RQItemStatus.NEEDS_OUTPUT) { return "NEEDS_OUTPUT"; }
            if (s === RQItemStatus.USER_STOPPED) { return "USER_STOPPED"; }
            if (s === RQItemStatus.ERR_STOPPED)  { return "ERR_STOPPED"; }
            if (s === RQItemStatus.RENDERING)    { return "RENDERING"; }
        } catch (e) {}
        return "status_" + s;
    }
    /* `instanceof CompItem` has been seen to misreport depending on evaluation
     * context. Duck-typing is the reliable test. */
    function isComp(it) { return it && it.numLayers !== undefined && it.duration !== undefined; }

    try {
        var pr = app.project;
        if (!pr) { p("NO PROJECT OPEN"); throw new Error("no project"); }

        /* ---------------- project ---------------- */
        p("### PROJECT");
        p("  ae        " + app.version + "  build " + app.buildName);
        if (pr.file) {
            SHORT.push([pr.file.parent.fsName + "/", "<proj>/"]);
            try { SHORT.push([Folder.myDocuments.parent.fsName + "/", "~/"]); } catch (eH) {}
        }
        p("  file      " + (pr.file ? pr.file.fsName : "(never saved)"));
        p("  items     " + pr.numItems + "   bpc=" + pr.bitsPerChannel + "   dirty=" + pr.dirty);
        try {
            p("  scripting write-files pref = " +
              (app.preferences.getPrefAsLong("Main Pref Section", "Pref_SCRIPTING_FILE_NETWORK_SECURITY") === 1
                ? "ON" : "OFF  <-- file output will fail"));
        } catch (ePref) { p("  scripting write-files pref = (key not readable on this version)"); }

        /* ---------------- render queue ---------------- */
        var rq = pr.renderQueue, i, enabledRQ = 0;
        p("");
        p("### RENDER QUEUE  (" + rq.numItems + " item" + (rq.numItems === 1 ? "" : "s") + ")");
        for (i = 1; i <= rq.numItems; i++) {
            var ri = rq.item(i), omN = "?", outF = "?", cn = "?";
            try { cn = ri.comp.name; } catch (e1) {}
            try { omN = ri.outputModule(1).name; } catch (e2) {}
            try { outF = ri.outputModule(1).file.fsName; } catch (e3) {}
            if (ri.render) { enabledRQ++; }
            p("  [" + i + "] " + cn + "   " + statusName(ri.status) +
              "   render=" + (ri.render ? "ON" : "off") + "   om=\"" + omN + "\"");
            p("      -> " + shorten(outF));
        }
        if (enabledRQ > 0) {
            p("  !! " + enabledRQ + " item(s) enabled - renderQueue.render() renders ALL of them.");
            p("     Park them and restore in a finally before batch rendering.");
        }

        /* ---------------- templates (live, machine-local) ---------------- */
        if (CFG.readTemplates) {
            p("");
            p("### TEMPLATES  (what exists on THIS machine)");
            var probeComp = null;
            for (i = 1; i <= pr.numItems; i++) { if (isComp(pr.item(i))) { probeComp = pr.item(i); break; } }
            if (probeComp === null) {
                p("  (no comp to query with)");
            } else {
                var tmpItem = null;
                try {
                    tmpItem = rq.items.add(probeComp);
                    tmpItem.render = false;
                    p("  RS  " + tmpItem.templates.join(" | "));
                    p("  OM  " + tmpItem.outputModule(1).templates.join(" | "));
                } catch (eT) {
                    p("  ERROR reading templates: " + eT);
                } finally {
                    if (tmpItem !== null) { try { tmpItem.remove(); } catch (eT2) {} }
                }
            }
        }

        /* ---------------- footage ---------------- */
        var missing = [], folders = {}, fCount = 0, key;
        for (i = 1; i <= pr.numItems; i++) {
            var it = pr.item(i);
            if (isComp(it) || it.numItems !== undefined) { continue; }   /* comp or folder */
            fCount++;
            try { if (it.footageMissing) { missing.push(it.name); } } catch (eM) {}
            var dir = "(no file - solid/placeholder)";
            try { if (it.mainSource && it.mainSource.file) { dir = it.mainSource.file.parent.fsName; } } catch (eF) {}
            folders[dir] = (folders[dir] || 0) + 1;
        }
        p("");
        p("### FOOTAGE  (" + fCount + " items)");
        p("  missing   " + missing.length + (missing.length ? ("  -> " + missing.join(", ")) : ""));
        var fList = [], fRest = 0;
        for (key in folders) { if (folders.hasOwnProperty(key)) { fList.push({ k: key, n: folders[key] }); } }
        fList.sort(function (a, b) { return b.n - a.n; });
        p("  sources   (" + fList.length + " distinct folders, busiest first)");
        for (i = 0; i < fList.length; i++) {
            if (i >= CFG.maxFolders) { fRest += fList[i].n; continue; }
            p("    " + rpad(fList[i].n, 5) + "  " + shorten(fList[i].k));
        }
        if (fRest > 0) {
            p("    " + rpad(fRest, 5) + "  ... across " + (fList.length - CFG.maxFolders) + " more folders");
        }

        /* ---------------- comps ---------------- */
        var allComps = [], c;
        for (i = 1; i <= pr.numItems; i++) {
            c = pr.item(i);
            if (isComp(c)) { allComps.push(c); }
        }

        /* Small project: detail everything, no config needed.
         * Big project: index everything, detail only what was asked for. */
        var detailAll = (CFG.comps.length === 0 && allComps.length <= CFG.autoDetailUnder);
        var wanted = [], ci, w, keep;
        for (ci = 0; ci < allComps.length; ci++) {
            c = allComps[ci];
            keep = detailAll;
            for (w = 0; w < CFG.comps.length; w++) { if (CFG.comps[w] === c.name) { keep = true; } }
            if (keep) { wanted.push(c); }
        }

        p("");
        p("### COMPS  (" + allComps.length + " in project, " + wanted.length + " detailed below)");
        for (ci = 0; ci < allComps.length && ci < CFG.maxIndex; ci++) {
            c = allComps[ci];
            p("  " + pad(c.name, 38) + " " + rpad(c.width + "x" + c.height, 10) +
              " " + rpad(c.frameRate.toFixed(2), 6) + "fps " +
              rpad(fr(c.duration, c.frameRate), 7) + " " + rpad(c.numLayers, 4) + " layers");
        }
        if (allComps.length > CFG.maxIndex) {
            p("  ... " + (allComps.length - CFG.maxIndex) + " more (CFG.maxIndex=" + CFG.maxIndex + ")");
        }
        if (wanted.length === 0) {
            p("");
            p("  No comps detailed. Set CFG.comps = [\"name\", ...] for full layer analysis,");
            p("  or raise CFG.autoDetailUnder (currently " + CFG.autoDetailUnder + ").");
        }

        for (ci = 0; ci < wanted.length; ci++) {
            c = wanted[ci];
            var fps = c.frameRate;

            p("");
            p("## " + c.name);
            p("   " + c.width + "x" + c.height + "  par=" + c.pixelAspect.toFixed(3) +
              "  " + fps.toFixed(2) + "fps  dur=" + c.duration.toFixed(4) + "s = " + fr(c.duration, fps) +
              "  res=" + resName(c.resolutionFactor) + "  motionBlur=" + (c.motionBlur ? "ON" : "off"));
            p("   workArea " + fr(c.workAreaStart, fps) + " -> " +
              fr(c.workAreaStart + c.workAreaDuration, fps) + "  (" + fr(c.workAreaDuration, fps) + ")");
            p("   layers   " + c.numLayers);

            /* --- group layers by geometry so the output stays readable --- */
            var groups = {}, order = [], k, ly, g;
            var locked = [], solo = [], shy = [], guide = [], adj = [], threeD = [],
                audio = [], fx = [], remap = [], outliers = [], enabledNames = [];
            var re = null;
            if (CFG.namePattern !== "") { try { re = new RegExp(CFG.namePattern); } catch (eRe) { re = null; } }

            for (k = 1; k <= c.numLayers; k++) {
                ly = c.layer(k);
                var srcDur = "-", srcName = "-", srcKind = "-";
                try {
                    if (ly.source) {
                        srcName = ly.source.name;
                        srcKind = isComp(ly.source) ? "comp" : "footage";
                        if (ly.source.duration !== undefined) { srcDur = fr(ly.source.duration, fps); }
                    }
                } catch (eS) {}

                var sig = "in=" + fr(ly.inPoint, fps) + " out=" + fr(ly.outPoint, fps) +
                          " start=" + fr(ly.startTime, fps) + " stretch=" + ly.stretch + "%" +
                          " src=" + srcDur + " (" + srcKind + ")";
                if (!groups[sig]) { groups[sig] = { n: 0, on: 0, names: [] }; order.push(sig); }
                g = groups[sig];
                g.n++;
                if (ly.enabled) { g.on++; }
                if (g.names.length < CFG.sampleNames) { g.names.push(ly.name); }

                if (ly.enabled) { enabledNames.push(ly.name); }
                try { if (ly.locked) { locked.push(ly.name); } } catch (e4) {}
                try { if (ly.solo) { solo.push(ly.name); } } catch (e5) {}
                try { if (ly.shy) { shy.push(ly.name); } } catch (e6) {}
                try { if (ly.guideLayer) { guide.push(ly.name); } } catch (e7) {}
                try { if (ly.adjustmentLayer) { adj.push(ly.name); } } catch (e8) {}
                try { if (ly.threeDLayer) { threeD.push(ly.name); } } catch (e9) {}
                try { if (ly.hasAudio) {
                    audio.push(ly.name + "{audioEnabled=" + ly.audioEnabled +
                               " video=" + (ly.enabled ? "ON" : "off") +
                               " audioActive=" + ly.audioActive + "}");
                } } catch (e10) {}
                try { if (ly.property("ADBE Effect Parade").numProperties > 0) {
                    fx.push(ly.name + "(" + ly.property("ADBE Effect Parade").numProperties + ")");
                } } catch (e11) {}
                try { if (ly.timeRemapEnabled) { remap.push(ly.name); } } catch (e12) {}
                if (re !== null && !re.test(ly.name)) { outliers.push(ly.name); }
            }

            p("   geometry (grouped):");
            var oi;
            for (oi = 0; oi < order.length; oi++) {
                g = groups[order[oi]];
                p("     " + rpad(g.n + "x", 5) + " " + pad(order[oi], 62) +
                  " enabled=" + g.on + "/" + g.n);
                p("           " + g.names.join(", ") + (g.n > g.names.length ? ", ..." : ""));
            }

            p("   enabled  " + (enabledNames.length === 0 ? "NONE"
                : (enabledNames.length + ": " + enabledNames.slice(0, CFG.sampleNames).join(", "))));
            p("   audio    " + (audio.length ? audio.join("  ") : "none"));
            if (audio.length) {
                p("            (a layer with video=off but audioActive=true still renders its sound)");
            }
            p("   flags    locked:" + (locked.length ? locked.join(",") : "none") +
              "  solo:" + (solo.length ? solo.join(",") : "none") +
              "  shy:" + (shy.length ? shy.join(",") : "none"));
            p("            guide:" + (guide.length ? guide.join(",") : "none") +
              "  adjustment:" + (adj.length ? adj.join(",") : "none") +
              "  3D:" + threeD.length);
            p("   effects  " + (fx.length ? fx.join(", ") : "none") +
              "   timeRemap: " + (remap.length ? remap.join(", ") : "none"));
            if (re !== null) {
                p("   names    " + (c.numLayers - outliers.length) + "/" + c.numLayers +
                  " match " + CFG.namePattern);
                if (outliers.length) { p("            outliers: " + outliers.join(", ")); }
            }
        }

        p("");
        p("OK");

    } catch (e) {
        p("");
        p("FATAL  " + e.toString() + (e.line ? ("  @line " + e.line) : ""));
    }

    var f = new File(CFG.out);
    f.open("w");
    f.encoding = "UTF-8";
    f.write(L.join("\n"));
    f.close();

})();
