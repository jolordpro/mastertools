/* Self-test for harness-template.js — proves the stubs behave before you trust
 * them with a tool's test suite. Run it after editing the template:
 *
 *   JSC=/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc
 *   T=harness-template.js
 *   "$JSC" -e "var ARG_SRC='$T'; $(cat $T) $(cat harness-selftest.js)"
 *
 * ARG_SRC points at the template itself only because the template reads a file at
 * load; the contents are unused here.
 */

var T = 0, BAD = [];
function t(cond, name, extra) { T++; if (!cond) { BAD.push(name + (extra ? ("  << " + extra) : "")); } }

/* ---------- virtual filesystem ---------- */
resetWorld();
FOLDERS["/out"] = true;
FOLDERS["/ro"] = "ro";

var f = new File("/out/a.txt");
t(f.open("w") === true, "open w on a writable folder succeeds");
t(f.write("hello") === true, "write returns true when open");
f.close();
t(f.exists === true, "file exists after write");
t(f.length === 5, "length reflects bytes written", f.length);
t(f.read() === "hello", "read returns content", f.read());

f.open("a"); f.write(" there"); f.close();
t(new File("/out/a.txt").read() === "hello there", "append mode appends");
f.open("w"); f.close();
t(new File("/out/a.txt").length === 0, "open w truncates");

var ro = new File("/ro/x.txt");
t(ro.open("w") === false, "open on an unwritable folder returns false (does not throw)");
t(ro.write("x") === false, "write refuses when open failed");
t(ro.exists === false, "nothing created in an unwritable folder");

setFile("/out/big.mov", 165000000);
t(new File("/out/big.mov").length === 165000000, "setFile seeds a real size");
FS["/out/legacy"] = true;
t(new File("/out/legacy").length === 2048, "legacy boolean FS entry still reports 2048");
FS["/out/zero"] = "empty";
t(new File("/out/zero").length === 0, "legacy 'empty' entry still reports 0");

/* ---------- system.callSystem ---------- */
resetWorld(); FOLDERS["/out"] = true; FOLDERS["/tmp"] = true;
setFile("/tmp/src.mov", 1234, "payload");
system.callSystem("/bin/mv -f '/tmp/src.mov' '/out/dst.mov'");
t(new File("/tmp/src.mov").exists === false, "mv removes the source");
t(new File("/out/dst.mov").length === 1234, "mv preserves size");
system.callSystem("/bin/cp -c '/out/dst.mov' '/out/clone.mov'");
t(new File("/out/clone.mov").read() === "payload", "cp -c clones content");
t(new File("/out/dst.mov").exists === true, "cp leaves the source");
FREE_KB = 1000;
var dfOut = system.callSystem("/bin/df -k '/out'");
t(dfOut.split("\n")[1].replace(/\s+/g, " ").split(" ")[3] === "1000", "df reports FREE_KB in column 4");
t(SYS_CALLS.length === 3, "every shell call is recorded", SYS_CALLS.length);

/* ---------- scheduleTask / pump ---------- */
resetWorld();
$.global.__n = 0;
$.global.__step = function () {
    $.global.__n++;
    if ($.global.__n < 50) { app.scheduleTask("$.global.__step()", 10, false); }
};
app.scheduleTask("$.global.__step()", 10, false);
var ticks = pump();
t($.global.__n === 50, "an async loop runs to completion", $.global.__n);
t(ticks === 50, "pump reports the tick count", ticks);
t(SCHEDULED === null, "nothing left scheduled at the end");
app.scheduleTask("$.global.__step()", 10, false);
app.cancelTask();
t(SCHEDULED === null, "cancelTask clears the pending task");

/* ---------- output module ---------- */
resetWorld();
var rq = app.project.renderQueue;
var pre = rq.numItems;
var item = rq.items.add(app.project.item(1));
var om = item.outputModule(1);
t(om.getSettings()["Output Audio"] === "Auto", "output module ships as Audio=Auto");
om.setSettings({ "Output Audio": "On" });
t(om.getSettings()["Output Audio"] === "On", "setSettings changes it");

SIM.rejectOMSettings = true;
om.setSettings({ "Output Audio": "Off" });
t(om.getSettings()["Output Audio"] === "On", "a refusing setSettings is modelled (value unchanged)");
SIM.rejectOMSettings = false;

om.file = new File("/out/BOS_TOR.mov");
t(om.getSettings()["Output File Info"]["Full Flat Path"] === "/out/BOS_TOR.mov",
  "om.file updates Full Flat Path");
SIM.ignoreOMFile = true;
om.file = new File("/out/OTHER.mov");
t(om.getSettings()["Output File Info"]["Full Flat Path"] === "/out/BOS_TOR.mov",
  "ignoreOMFile models the name template winning");
SIM.ignoreOMFile = false;

SIM.rejectOMTemplate = true;
var threw = false;
try { om.applyTemplate("High Quality with Alpha"); } catch (e) { threw = true; }
t(threw, "a missing output-module template throws");
SIM.rejectOMTemplate = false;
t(typeof item.getSettings()["Time Span"] === "string", "render settings are readable");

/* ---------- render ---------- */
resetWorld(); FOLDERS["/out"] = true;
rq = app.project.renderQueue;
var preCount = rq.numItems;
t(preCount > 0, "pre-existing queue items exist to be protected", preCount);
var it2 = rq.items.add(app.project.item(1));
it2.outputModule(1).file = new File("/out/r.mov");
it2.render = true;
rq.render();
t(new File("/out/r.mov").length === 165000000, "a successful render writes a sized file",
  new File("/out/r.mov").length);
t(it2.status === RQItemStatus.DONE, "status is DONE");

resetWorld(); FOLDERS["/out"] = true;
rq = app.project.renderQueue;
SIM.failFirst = 2;
var it3 = rq.items.add(app.project.item(1));
it3.outputModule(1).file = new File("/out/r2.mov");
it3.render = true;
rq.render(); t(it3.status === RQItemStatus.ERR_STOPPED, "failFirst fails attempt 1");
rq.render(); t(it3.status === RQItemStatus.ERR_STOPPED, "failFirst fails attempt 2");
rq.render(); t(it3.status === RQItemStatus.DONE, "and succeeds on attempt 3");

resetWorld(); FOLDERS["/out"] = true;
rq = app.project.renderQueue;
SIM.mode = "zeroByte";
var it4 = rq.items.add(app.project.item(1));
it4.outputModule(1).file = new File("/out/r3.mov");
it4.render = true;
rq.render();
t(new File("/out/r3.mov").exists && new File("/out/r3.mov").length === 0,
  "zeroByte mode produces a file that exists but is empty");

/* ---------- import verification ---------- */
resetWorld();
var imported = app.project.importFile(new ImportOptions(new File("/out/x.mov")));
t(Math.abs(imported.duration - 2.002002002002) < 1e-9, "import reports VERIFY.duration");
t(imported.hasAudio === true, "import reports audio by default");
VERIFY.hasAudio = false;
t(app.project.importFile(new ImportOptions(new File("/out/x.mov"))).hasAudio === false,
  "VERIFY.hasAudio models a silent render");
VERIFY.throwOnImport = true;
threw = false;
try { app.project.importFile(new ImportOptions(new File("/out/x.mov"))); } catch (e2) { threw = true; }
t(threw, "VERIFY.throwOnImport models an unreadable file");

/* ---------- ScriptUI registry ---------- */
resetWorld();
var w = new Window("palette", "Tool");
var g = w.add("group");
var btn = g.add("button", undefined, "Preflight");
var cb = g.add("checkbox", undefined, "Skip existing outputs");
cb.value = true;
t(findW("button", "Preflight") === btn, "findW locates a button by label fragment");
t(findW("checkbox", "Skip existing") === cb, "findW locates a checkbox");
t(findW("button", "Nope") === null, "findW returns null when absent");
t(findAllW("checkbox").length === 1, "findAllW collects by type");
t(findW("window", "Tool") === w, "the window itself is registered");

/* ---------- results ---------- */
print("");
if (BAD.length === 0) { print("  harness self-test: ALL " + T + " CHECKS PASSED"); }
else {
    print("  harness self-test: " + (T - BAD.length) + "/" + T + " passed, " + BAD.length + " FAILED:");
    for (var i = 0; i < BAD.length; i++) { print("    - " + BAD[i]); }
}
print("");
