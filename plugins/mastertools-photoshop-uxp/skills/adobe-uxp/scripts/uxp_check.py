#!/usr/bin/env python3
"""Static check for a UXP plugin: catches the failures that install fine and then misbehave inside the app.

  uxp_check.py <project-dir>     (with uxp.config.json + src/)  or  uxp_check.py <src-dir-with-manifest.json>

ERROR = will break (missing permission for code that needs it, write(""), bad manifest/version/host).
WARN  = renders or behaves wrongly in UXP (native <button>, <header>/<footer>, sticky, dblclick, ...).
Exit code 1 if any ERROR. Every rule comes from something measured on PS/ID/PR in Oct 2026 (see references/).
"""
import json, os, re, sys

HOST_IDS = {"PS", "ID", "indesign", "premierepro", "aftereffects", "AI", "XD"}
BUILD_KEYS = {"PS": "PS", "ID": "ID", "PR": "premierepro", "AE": "aftereffects", "AI": "AI"}
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")

HTML_RULES = [
    (r"<button\b", "WARN", "native <button> ignores sizing in UXP and overflows narrow panels; use <div class=\"btn\">"),
    (r"<(header|footer)\b", "WARN", "<header>/<footer> mis-lay out in UXP; use plain <div class=\"header\">"),
    (r"type\s*=\s*[\"']search[\"']", "WARN", "type=\"search\" styling is ignored; use type=\"text\""),
]
CSS_RULES = [
    (r"position\s*:\s*sticky", "WARN", "position: sticky is unsupported in UXP"),
    (r"display\s*:\s*grid", "WARN", "CSS grid is unsupported in UXP; use flexbox"),
    (r"::?(before|after)\s*\{[^}]*content", "WARN", "::before/::after content doesn't render in UXP; use a real <span>"),
]
JS_RULES = [
    (r"\.write\(\s*(\"\"|''|``)\s*[,)]", "ERROR", "write(\"\") throws 'writeToFile: data cannot be null'; write a placeholder"),
    (r"dblclick", "WARN", "dblclick is unreliable across UXP hosts; detect double-clicks from click timestamps"),
    (r"classList\.toggle\([^,()]+,", "WARN", "classList.toggle(cls, force) isn't guaranteed in UXP; use add/remove"),
    (r"\.dataset\b", "WARN", "dataset isn't guaranteed in UXP; use getAttribute('data-…')"),
    (r"\.scrollIntoView\(", "WARN", "scrollIntoView may not exist; guard scrollIntoViewIfNeeded"),
    (r"file:/tmp\b", "WARN", "use file:/private/tmp (/tmp is a symlink)"),
    (r"addEventListener\(\s*[\"']focus[\"']", "INFO", "window focus rarely fires in UXP panels; also re-scan on mouseenter or a refresh button"),
    (r"\balert\(", "WARN", "alert() isn't available in UXP panels; report in the panel's status line"),
]


def strip_comments(text, ext):
    """Blank out comments (keeping newlines so line numbers stay right) so advice in comments isn't flagged."""
    keep = lambda m: re.sub(r"[^\n]", " ", m.group(0))
    if ext in (".html", ".htm"):
        return re.sub(r"<!--.*?-->", keep, text, flags=re.S)
    text = re.sub(r"/\*.*?\*/", keep, text, flags=re.S)
    if ext == ".js":
        text = re.sub(r"(?m)(^|[^:\\\"'`])//[^\n]*", lambda m: m.group(1) + " " * (len(m.group(0)) - len(m.group(1))), text)
    return text


def lines_matching(text, pattern):
    for m in re.finditer(pattern, text, flags=re.I | re.S):
        yield text.count("\n", 0, m.start()) + 1


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return 0
    root = os.path.abspath(argv[0])
    findings = []

    def add(level, where, msg):
        findings.append((level, where, msg))

    cfg_path = os.path.join(root, "uxp.config.json")
    if os.path.isfile(cfg_path):
        cfg = json.load(open(cfg_path, encoding="utf-8"))
        src = os.path.join(root, cfg.get("src", "src"))
        perms = cfg.get("permissions", {})
        hosts = [BUILD_KEYS.get(a, a) for a in cfg.get("apps", [])]
        version, entry_ids = cfg.get("version", ""), [cfg.get("entrypoint", {}).get("id", "main")]
        where = "uxp.config.json"
        for a in cfg.get("apps", []):
            if a not in BUILD_KEYS:
                add("ERROR", where, "unknown app key %r (use PS, ID, PR, AE, AI)" % a)
            if a in ("AE", "AI"):
                add("INFO", where, "%s refused homemade UXP plugins as of Oct 2026 (UPIA -411); keep a CEP/ScriptUI version" % a)
    elif os.path.isfile(os.path.join(root, "manifest.json")):
        src, where = root, "manifest.json"
        m = json.load(open(os.path.join(root, "manifest.json"), encoding="utf-8"))
        if m.get("manifestVersion") != 5:
            add("WARN", where, "manifestVersion is %r; these checks assume 5" % m.get("manifestVersion"))
        perms, version = m.get("requiredPermissions", {}), m.get("version", "")
        h = m.get("host", [])
        hosts = [x.get("app") for x in (h if isinstance(h, list) else [h])]
        entry_ids = [e.get("id") for e in m.get("entrypoints", [])]
        for x in hosts:
            if x not in HOST_IDS:
                add("ERROR", where, "unknown host app id %r" % x)
    else:
        sys.exit("No uxp.config.json or manifest.json in %s" % root)

    if not SEMVER.match(str(version)):
        add("ERROR", where, "version %r must be x.y.z" % version)

    js_all = ""
    for dirpath, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "node_modules"]
        for f in files:
            p = os.path.join(dirpath, f)
            rel = os.path.relpath(p, root)
            ext = os.path.splitext(f)[1].lower()
            if ext not in (".html", ".htm", ".css", ".js"):
                continue
            text = strip_comments(open(p, encoding="utf-8", errors="replace").read(), ext)
            rules = HTML_RULES if ext in (".html", ".htm") else CSS_RULES if ext == ".css" else JS_RULES
            for pat, level, msg in rules:
                for ln in lines_matching(text, pat):
                    add(level, "%s:%d" % (rel, ln), msg)
            if ext == ".css":
                for m in re.finditer(r"([^{}]*disabled[^{}]*)\{([^}]*)\}", text):
                    if "opacity" in m.group(2):
                        at = m.start() + m.group(0).find("disabled")
                        add("WARN", "%s:%d" % (rel, text.count("\n", 0, at) + 1),
                            "opacity didn't render on UXP divs; show the disabled state with colour")
            if ext == ".js":
                js_all += "\n" + text
                for m in re.finditer(r"entrypoints\.setup\(\s*\{\s*panels\s*:\s*\{([^}]*)", text):
                    for pid in re.findall(r"([A-Za-z_$][\w$]*)\s*:\s*\{", m.group(1)):
                        if entry_ids and pid not in entry_ids:
                            add("ERROR", "%s:%d" % (rel, text.count("\n", 0, m.start()) + 1),
                                "entrypoints.setup panel %r doesn't match the manifest entrypoint id(s) %s" % (pid, entry_ids))

    # permission <-> code consistency
    if re.search(r"new\s+Function\s*\(|AsyncFunction|\beval\s*\(", js_all) and not perms.get("allowCodeGenerationFromStrings"):
        add("ERROR", where, "code builds functions from strings but allowCodeGenerationFromStrings isn't granted")
    if re.search(r"shell\.(openPath|openExternal)\s*\(", js_all) and not perms.get("launchProcess"):
        add("ERROR", where, "uxp.shell.openPath/openExternal needs a launchProcess permission")
    if re.search(r"getEntryWithUrl\(\s*[\"'`]file:", js_all) and perms.get("localFileSystem") != "fullAccess":
        add("ERROR", where, "getEntryWithUrl('file:…') on arbitrary paths needs localFileSystem: fullAccess")
    if re.search(r"fetch\(|XMLHttpRequest|WebSocket", js_all) and not perms.get("network"):
        add("WARN", where, "network calls need a network permission with the domains listed")
    if "batchPlay" in js_all and "executeAsModal" not in js_all:
        add("WARN", where, "batchPlay that changes state must run inside core.executeAsModal (Photoshop)")
    if "AdobeScriptAutomation Scripts" in js_all and "ERR|" not in js_all and "catch(e)" not in js_all.replace(" ", ""):
        add("WARN", where, "running .jsx via batchPlay without a try/catch wrapper: Photoshop shows its own error modal "
                           "and batchPlay returns only -128 (see references/runtime-gotchas.md)")
    for mod, host in (("photoshop", "PS"), ("indesign", "ID"), ("premierepro", "premierepro")):
        if re.search(r"require\(\s*[\"']%s[\"']\s*\)" % mod, js_all) and host not in hosts and not (host == "ID" and "indesign" in hosts):
            add("INFO", where, "uses require(%r) but the plugin doesn't target that app (fine if guarded by host checks)" % mod)

    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    findings.sort(key=lambda f: (order[f[0]], f[1]))
    for level, w, msg in findings:
        print("%-5s %s  %s" % (level, w, msg))
    n = sum(1 for f in findings if f[0] == "ERROR")
    print("%d error(s), %d warning(s), %d note(s)" % (n, sum(1 for f in findings if f[0] == "WARN"),
                                                       sum(1 for f in findings if f[0] == "INFO")))
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
