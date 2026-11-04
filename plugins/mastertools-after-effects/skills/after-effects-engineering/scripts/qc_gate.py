#!/usr/bin/env python3
"""
QC gate for After Effects ExtendScript (.jsx) files.

Catches the failures that kill AE scripts at load time — the ones a normal
syntax check misses. Run this before every delivery.

    python3 qc_gate.py path/to/tool.jsx [more.jsx ...]

Exit status is 0 when everything passes, 1 otherwise, so it drops into a
pre-commit hook or CI step unchanged.

Why JavaScriptCore and not `node --check`: jsc ships with macOS so there is
nothing to install, and parsing via the Function constructor parses without
executing. That matters because an AE script references `app`, `File` and
ScriptUI at load and would throw instantly under plain evaluation. A clean
parse also proves brace/paren/bracket balance, so that check comes free.
"""

import re
import subprocess
import sys
import os

JSC = ("/System/Library/Frameworks/JavaScriptCore.framework/"
       "Versions/A/Helpers/jsc")

RESERVED = (
    "in|for|if|else|do|while|with|new|delete|typeof|instanceof|void|return|throw|"
    "try|catch|finally|switch|case|default|break|continue|function|this|var|class|"
    "const|enum|export|extends|import|super|implements|interface|let|package|"
    "private|protected|public|static|yield|abstract|boolean|byte|char|double|final|"
    "float|goto|int|long|native|short|synchronized|throws|transient|volatile|"
    "debugger|null|true|false"
)

# The subset of RESERVED that looks like an ordinary identifier. Used for the
# positional check, where `null`, `true`, `false` and `this` are perfectly legal
# and matching them produces nothing but false alarms - `f(0, false)` is fine.
IDENTLIKE = (
    "abstract|boolean|byte|char|class|const|double|enum|export|extends|final|"
    "float|goto|implements|import|int|interface|let|long|native|package|private|"
    "protected|public|short|static|super|synchronized|throws|transient|volatile|yield"
)

# Lines carrying a regex literal that starts with '=' — populated by strip_noncode(),
# which is the only place that reliably knows a regex literal is starting.
BAD_REGEX_LINES: list = []

# (label, pattern, why it matters)
CHECKS = [
    ("ES5 let/const", r"\b(let|const)\s+[A-Za-z_$]",
     "ExtendScript is ES3; these are a syntax error at load"),
    ("arrow function", r"=>",
     "ES6 syntax, fails at load"),
    ("template literal", r"`",
     "ES6 syntax, fails at load"),
    ("for...of", r"for\s*\([^;)]*\bof\b",
     "ES6 syntax, fails at load"),
    ("async/await/yield", r"\b(async|await|yield)\b",
     "not supported by the ExtendScript engine"),
    ("JSON.*", r"\bJSON\.",
     "no JSON object in ES3; ship a parser or avoid"),
    ("Object.* ES5", r"\bObject\.(keys|values|entries|assign|create|freeze)",
     "ES5 statics, undefined at runtime"),
    ("Date.now", r"\bDate\.now",
     "ES5; use new Date().getTime()"),
    ("toISOString", r"\.toISOString",
     "ES5 Date method"),
    ("Array ES5 methods", r"\.(forEach|map|filter|reduce|reduceRight|some|every|find|findIndex|includes|fill|flat|flatMap)\s*\(",
     "nothing past indexOf exists; use an indexed for loop"),
    ("String ES5 methods", r"\.(trim|trimStart|trimEnd|startsWith|endsWith|repeat|padStart|padEnd|codePointAt|normalize)\s*\(",
     "ES5/ES6 String methods"),
    ("reserved word as a VARIABLE name", r"\bvar\s+(" + RESERVED + r")\b",
     "ExtendScript rejects this at PARSE time, so the whole file fails to run and "
     "After Effects shows a blocking modal instead of your report. `short`, `int`, "
     "`final`, `native`, `char`, `byte`, `double`, `float`, `long`, `package` and "
     "`enum` all look like ordinary variable names and are not."),
    ("reserved word as a LATER declarator or parameter",
     r"[,(]\s*(" + IDENTLIKE + r")\s*(?:=[^=]|[,;)])",
     "Same parse-time death as `var short`, but in a position the simpler rule "
     "misses: `var i, short = []` or `function f(a, char)`. This gap let a script "
     "through on 2026-08-25 that then died silently in After Effects — no report, "
     "no modal, just nothing."),
    ("reserved word as bare key", r"[{,]\s*(" + RESERVED + r")\s*:",
     "FATAL at load and invisible to syntax checkers — quote the key"),
    ("reserved word as member access", r"\.(" + RESERVED + r")\b",
     "FATAL at load and invisible to syntax checkers — use bracket access"),
    ("trailing comma in literal", r",\s*[\]}]",
     "rejected by strict ES3 parsers"),
]

# (open token, close token) that must appear in equal numbers
PAIRS = [
    ("app.beginSuppressDialogs", "app.endSuppressDialogs"),
    ("app.beginUndoGroup", "app.endUndoGroup"),
]


def strip_comments(src: str) -> str:
    """Remove block and line comments, preserving line numbers."""
    out, i, n = [], 0, len(src)
    while i < n:
        if src.startswith("/*", i):
            j = src.find("*/", i + 2)
            seg = src[i:j + 2] if j > 0 else src[i:]
            out.append("\n" * seg.count("\n"))
            i = (j + 2) if j > 0 else n
        elif src.startswith("//", i):
            j = src.find("\n", i)
            i = j if j > 0 else n
        else:
            out.append(src[i])
            i += 1
    return "".join(out)


def strip_noncode(src: str) -> str:
    """Blank comments, string bodies and regex bodies in one left-to-right pass.

    Line numbers, quotes and delimiters survive so reported positions stay
    accurate. This has to be one pass rather than three, because a quote inside
    a comment and a slash inside a string each derail a naive second scan.

    Without this, the ES5+ sweep matches its own vocabulary inside message
    text: a script that prints "=> keep the fallback" is not using an arrow
    function, and flagging it trains you to ignore the gate.
    """
    del BAD_REGEX_LINES[:]          # per-file
    out: list = []
    i, n = 0, len(src)
    prev = ""                       # last significant code character emitted

    while i < n:
        c = src[i]

        if src.startswith("/*", i):                        # block comment
            j = src.find("*/", i + 2)
            seg = src[i:j + 2] if j >= 0 else src[i:]
            out.append("\n" * seg.count("\n"))
            i = (j + 2) if j >= 0 else n
            continue

        if src.startswith("//", i):                        # line comment
            j = src.find("\n", i)
            i = j if j >= 0 else n
            continue

        if c == '"' or c == "'":                           # string literal
            out.append(c)
            i += 1
            while i < n:
                if src[i] == "\\":                         # escape: blank both
                    out.append("\n" if (i + 1 < n and src[i + 1] == "\n") else " ")
                    out.append(" ")
                    i += 2
                    continue
                if src[i] == c:
                    out.append(c)
                    i += 1
                    break
                out.append("\n" if src[i] == "\n" else " ")
                i += 1
            prev = c
            continue

        # Regex literal, but only where a regex can legally start — otherwise
        # this is division. The preceding significant character disambiguates.
        if c == "/" and (prev == "" or prev in "(,=:[!&|?{};+-*%~^<>"):
            # A regex literal whose FIRST character is '=' is fatal in ExtendScript: the
            # parser reads the '/=' as the divide-assign operator and dies at load with
            # "Unable to execute script at line N. /= does not have a value" — and that
            # modal then blocks every later DoScriptFile. Recorded here rather than in
            # CHECKS because CHECKS runs on the stripped source, where the regex body
            # (and therefore the '=') has already been blanked away.
            if i + 1 < n and src[i + 1] == "=":
                BAD_REGEX_LINES.append(src.count("\n", 0, i) + 1)
            j, in_class, closed = i + 1, False, False
            while j < n:
                if src[j] == "\\":
                    j += 2
                    continue
                if src[j] == "\n":
                    break
                if src[j] == "[":
                    in_class = True
                elif src[j] == "]":
                    in_class = False
                elif src[j] == "/" and not in_class:
                    closed = True
                    break
                j += 1
            if closed:
                out.append("/")
                out.append(" " * (j - i - 1))
                out.append("/")
                i = j + 1
                while i < n and src[i].isalpha():           # flags
                    out.append(src[i])
                    i += 1
                prev = "/"
                continue

        out.append(c)
        if not c.isspace():
            prev = c
        i += 1

    return "".join(out)


def strip_directives(src: str) -> str:
    """Blank ExtendScript preprocessor directives, preserving line numbers.

    #target, #include, #includepath, #script, #engine, #targetengine and
    #strict are valid ExtendScript but are not JavaScript — a JS parser reads
    the leading # as a private field and rejects the file. Blanking them keeps
    the parse honest without flagging correct code.
    """
    out = []
    for line in src.split("\n"):
        out.append("" if re.match(r"\s*#\s*[A-Za-z]", line) else line)
    return "\n".join(out)


def parse_check(path: str, cleaned: str):
    """Parse without executing. Returns (ok, message)."""
    if not os.path.exists(JSC):
        return None, "jsc not found — parse check skipped (macOS only)"

    tmp = path + ".qcparse.tmp"
    try:
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(cleaned)
    except OSError as exc:
        return None, "could not stage a temp file: %s" % exc

    prog = (
        'var src = readFile(%s);'
        'try { new Function(src); print("OK"); }'
        'catch (e) { print("FAIL: " + e); }'
    ) % _js_string(tmp)
    try:
        res = subprocess.run([JSC, "-e", prog], capture_output=True,
                             text=True, timeout=60)
    except Exception as exc:                                  # noqa: BLE001
        return None, "could not run jsc: %s" % exc
    finally:
        try:
            os.remove(tmp)
        except OSError:
            pass
    out = (res.stdout or "").strip()
    if out.startswith("OK"):
        return True, "parses (brace/paren/bracket balance implied)"
    return False, out or (res.stderr or "").strip() or "unknown parse failure"


def _js_string(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def check_file(path: str) -> bool:
    print("=" * 62)
    print(path)
    print("=" * 62)

    try:
        raw = open(path, encoding="utf-8").read()
    except OSError as exc:
        print("  cannot read: %s" % exc)
        return False

    ok = True

    directives = len([1 for l in raw.split("\n") if re.match(r"\s*#\s*[A-Za-z]", l)])
    cleaned = strip_directives(raw)

    parsed, msg = parse_check(path, cleaned)
    if parsed is True:
        print("  ok    parse — %s%s" % (
            msg,
            " (%d ExtendScript directive line(s) skipped)" % directives if directives else ""))
    elif parsed is False:
        print("  FAIL  parse — %s" % msg)
        ok = False
    else:
        print("  ----  parse — %s" % msg)

    code = strip_noncode(cleaned)
    lines = code.split("\n")

    for label, pattern, why in CHECKS:
        hits = [(i + 1, l.strip()[:88])
                for i, l in enumerate(lines) if re.search(pattern, l)]
        if hits:
            ok = False
            print("  FAIL  %s  (%d)" % (label, len(hits)))
            print("        %s" % why)
            for ln, text in hits[:8]:
                print("        L%-5d %s" % (ln, text))
            if len(hits) > 8:
                print("        ... and %d more" % (len(hits) - 8))
    if BAD_REGEX_LINES:
        ok = False
        print("  FAIL  regex literal starting with '='  (%d)" % len(BAD_REGEX_LINES))
        print("        ExtendScript reads the leading /= as the divide-assign operator and "
              "dies at load:")
        print("        \"Unable to execute script at line N. /= does not have a value\" — and "
              "that modal")
        print("        then blocks every later DoScriptFile. Use new RegExp(\"==...\") instead.")
        for ln in BAD_REGEX_LINES[:8]:
            print("        L%-5d %s" % (ln, lines[ln - 1].strip()[:88] if ln - 1 < len(lines) else ""))
        if len(BAD_REGEX_LINES) > 8:
            print("        ... and %d more" % (len(BAD_REGEX_LINES) - 8))

    if ok:
        print("  ok    ES3 + reserved-word sweep (%d checks)" % len(CHECKS))

    for a, b in PAIRS:
        ca, cb = code.count(a), code.count(b)
        if ca or cb:
            if ca == cb:
                print("  ok    %s / %s balanced (%d)" % (a, b, ca))
            else:
                ok = False
                print("  FAIL  %s:%d vs %s:%d — unbalanced" % (a, ca, b, cb))

    if "app.onError" in code:
        # Count by subtraction: a negative lookahead after \s* would match the
        # whitespace position and wrongly score "= function" as a restore.
        total = len(re.findall(r"app\.onError\s*=", code))
        handlers = len(re.findall(r"app\.onError\s*=\s*function", code))
        restores = total - handlers
        if handlers and not restores:
            ok = False
            print("  FAIL  app.onError set %d time(s) but never restored" % handlers)
            print("        capture the previous value and put it back in a finally")
        else:
            print("  ok    app.onError set %d, restored %d" % (handlers, restores))

    if "Array.prototype" in code or "String.prototype" in code:
        unguarded = []
        for m in re.finditer(r"(Array|String|Object)\.prototype\.(\w+)\s*=", code):
            before = code[max(0, m.start() - 200):m.start()]
            if ("if (!" + m.group(1) + ".prototype." + m.group(2)) not in before:
                unguarded.append(m.group(1) + ".prototype." + m.group(2))
        if unguarded:
            ok = False
            print("  FAIL  unguarded polyfill(s): %s" % ", ".join(unguarded))
            print("        wrap in if (!X) so a host-provided method is never clobbered")
        else:
            print("  ok    polyfills guarded")

    if "app.open(" in code:
        opens = code.count("app.open(")
        print("  note  app.open( appears %d time(s)%s" % (
            opens,
            " — route every open through one function so close/purge cannot be skipped"
            if opens > 1 else " (single entry point)"))

    print("  ==>   %s" % ("PASS" if ok else "FAIL"))
    print()
    return ok


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not args:
        print(__doc__)
        return 1
    results = [check_file(p) for p in args]
    total, passed = len(results), sum(1 for r in results if r)
    print("%d/%d file(s) passed" % (passed, total))
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
