#!/usr/bin/env python3
"""ae_dialog_lint.py FILE ... : the dialog lint (dialog-proofing lint). Ships with aerun.py in the
after-effects-engineering skill; it sits beside qc_gate.py and does not replace it. Run it on every .jsx/.sh/.py input
(runners included) before AE is touched. Prints one "FAIL <file>:<line> <rule>: <text>" per finding, then
"LINT PASS <n> files" (exit 0) or "LINT FAIL <k> finding(s) in <n> files" (exit 1). Exit 2: a file is missing.

Skill copy of a QC-frozen project tool, source sha256 44cb7843f131e267 (QC freeze FREEZE_render v2 b941ea8aa0c04258).
Changes from that source: this docstring only (project paths and names removed). The rules below are unchanged.

.jsx (comments and string literals are blanked first, so words in them never count):
  J1 alert(, confirm( or prompt( anywhere.
  J2 an entry point not wrapped in H.run: top-level code other than H.run(...) calls, function declarations and the library
     form "var X = (function () { ... })();". A file of declarations only (a house.jsx library) passes.
  J3 endSuppressDialogs outside a finally block.
  J4 app.quit.
  J5 .save( with no readonly guard: the D7 line "if (<f>.exists && <f>.readonly) throw" within the 6 lines before it.
.sh / .py (shell comments are blanked; Python is read as text, its strings included, since that is where AppleScript lives):
  S1 "open ... -a" without -g (D3).
  S2 "tell application" without "is running" on the same line or within the 3 lines before it (D2).
  S3 chmod to a read-only mode (4xx, -w, a-w, u-w, =r) on a line that names an .aep, or on a target with no extension other
     than .aep (D1: never lock a project file).
"""
import os, re, sys

JS_RULES = ("J1", "J2", "J3", "J4", "J5")


def blank_js(src):
    """src with comments and string/regex literals replaced by spaces (newlines kept, so line numbers hold)."""
    out, i, n = [], 0, len(src)
    prev = ""                                         # last significant character, to tell a regex from a division
    while i < n:
        c = src[i]
        if c == "/" and i + 1 < n and src[i + 1] == "/":
            j = src.find("\n", i); j = n if j < 0 else j
            out.append(" " * (j - i)); i = j; continue
        if c == "/" and i + 1 < n and src[i + 1] == "*":
            j = src.find("*/", i + 2); j = n if j < 0 else j + 2
            out.append(re.sub(r"[^\n]", " ", src[i:j])); i = j; continue
        if c in "\"'":
            j = i + 1
            while j < n and src[j] != c and src[j] != "\n":
                j += 2 if src[j] == "\\" else 1
            out.append(c + " " * (min(j, n) - i - 1) + (c if j < n else "")); i = j + 1; prev = c; continue
        if c == "/" and (prev == "" or prev in "(,=:[!&|?{};+-*%<>~^" or re.search(r"\breturn\s*$", "".join(out[-3:]))):
            j, cls = i + 1, False                     # a regex literal
            while j < n and src[j] != "\n":
                if src[j] == "\\": j += 2; continue
                if src[j] == "[": cls = True
                elif src[j] == "]": cls = False
                elif src[j] == "/" and not cls: break
                j += 1
            if j < n and src[j] == "/":
                j += 1
                while j < n and src[j].isalpha(): j += 1
                out.append(" " * (j - i)); i = j; prev = "/"; continue
        out.append(c)
        if not c.isspace(): prev = c
        i += 1
    return "".join(out)


def line_of(s, pos):
    return s.count("\n", 0, pos) + 1


def lint_js(path, src):
    b, bad = blank_js(src), []
    raw = src.split("\n")
    def add(rule, pos, why):
        ln = line_of(b, pos); bad.append((rule, ln, why + ": " + raw[ln - 1].strip()[:120]))
    for m in re.finditer(r"(?<![\w.$])(alert|confirm|prompt)\s*\(", b): add("J1", m.start(), m.group(1) + "() opens a modal dialog")
    for m in re.finditer(r"\bapp\s*\.\s*quit\b", b): add("J4", m.start(), "app.quit")
    # block structure: a stack of the keyword that opened each brace
    stack, top, i = [], [], 0
    for m in re.finditer(r"[{}]|\bendSuppressDialogs\b", b):
        t = m.group(0)
        if t == "{":
            before = b[:m.start()].rstrip()
            kw = "finally" if re.search(r"\bfinally$", before) else "block"
            stack.append(kw)
        elif t == "}":
            if stack: stack.pop()
        elif "finally" not in stack:
            add("J3", m.start(), "endSuppressDialogs outside a finally block")
    # J2: top-level text (depth 0, comments/strings blanked)
    depth, tl, paren = 0, [], 0
    for k, ch in enumerate(b):
        if ch == "{": depth += 1; tl.append(" "); continue
        if ch == "}": depth -= 1; tl.append(" "); continue
        tl.append(ch if depth == 0 else (" " if ch != "\n" else "\n"))
    top = "".join(tl)
    # remove the allowed forms, then anything left that is not punctuation is unwrapped code
    allowed = top
    allowed = re.sub(r"\bH\s*\.\s*run\s*\([^;]*?\)\s*;?", lambda m: re.sub(r"[^\n]", " ", m.group(0)), allowed, flags=re.S)
    allowed = re.sub(r"\bfunction\s+[\w$]+\s*\([^)]*\)\s*", lambda m: re.sub(r"[^\n]", " ", m.group(0)), allowed)
    allowed = re.sub(r"\bvar\s+[\w$]+\s*=\s*\(\s*function\s*\(\s*\)\s*\)\s*\(\s*\)\s*;?", lambda m: re.sub(r"[^\n]", " ", m.group(0)), allowed)
    for m in re.finditer(r"[\w$]+", allowed):
        add("J2", m.start(), "entry code outside H.run (wrap the entry point in H.run, house.jsx)"); break
    # J5: every .save( needs the D7 guard within the 6 lines before it
    guard = re.compile(r"if\s*\(\s*([\w$.]+)\.exists\s*&&\s*\1\.readonly\s*\)\s*throw")
    bl = b.split("\n")
    for m in re.finditer(r"\.\s*save\s*\(", b):
        ln = line_of(b, m.start())
        if not any(guard.search(bl[k]) for k in range(max(0, ln - 7), ln)):
            add("J5", m.start(), ".save( with no readonly guard (D7: if (dst.exists && dst.readonly) throw ...)")
    return bad


def blank_sh(src):
    """shell: drop comments (a # at a word start outside quotes); keep everything else."""
    out = []
    for line in src.split("\n"):
        q, j, keep = None, 0, len(line)
        while j < len(line):
            c = line[j]
            if c == "\\" and q != "'": j += 2; continue
            if q:
                if c == q: q = None
            elif c in "\"'": q = c
            elif c == "#" and (j == 0 or line[j - 1] in " \t;|&("):
                if not (j > 0 and line[j - 1] == "$"): keep = j; break
            j += 1
        out.append(line[:keep])
    return "\n".join(out)


RO_MODE = re.compile(r"\bchmod\s+(?:-[A-Za-z]+\s+)*(0?4[0-7][0-7]|[ugoa]*-w\b|[ugoa]*=r\b|-w\b)\s+(.*)$")
OPEN_A = re.compile(r"(?<![\w./-])open((?:\s+-[A-Za-z]+)+)")


def lint_text(path, src, is_sh):
    b, bad = (blank_sh(src) if is_sh else src), []
    raw, bl = src.split("\n"), (blank_sh(src) if is_sh else src).split("\n")
    for k, line in enumerate(bl, 1):
        for m in OPEN_A.finditer(line):
            flags = m.group(1).split()
            if any("a" in f[1:] for f in flags) and not any("g" in f[1:] for f in flags):
                bad.append(("S1", k, "open -a without -g (D3: open -g -a): " + raw[k - 1].strip()[:120]))
        if re.search(r"\btell\s+application\b", line):
            ctx = " ".join(bl[max(0, k - 4):k])
            if "is running" not in ctx:
                bad.append(("S2", k, "tell application without an \"is running\" check (D2: it would launch AE): " + raw[k - 1].strip()[:120]))
        m = RO_MODE.search(line)
        if m:
            tgt = m.group(2)
            other = re.search(r"\.(py|sh|jsx|json|txt|log|md|png|jpg|mp4|csv)\b", tgt) and not re.search(r"aep", tgt, re.I)
            if re.search(r"aep", line, re.I) or not other:
                bad.append(("S3", k, "chmod to read-only on a project file (D1: no locked .aep): " + raw[k - 1].strip()[:120]))
    return bad


def lint(path):
    src = open(path, encoding="utf-8", errors="replace").read()
    if path.endswith(".jsx"): return lint_js(path, src)
    return lint_text(path, src, not path.endswith(".py"))


def main(a):
    if not a: print(__doc__); return 2
    n, k = 0, 0
    for p in a:
        if not os.path.isfile(p): print("MISSING " + p); return 2
        n += 1
        for rule, ln, why in lint(p):
            k += 1; print("FAIL %s:%d %s: %s" % (p, ln, rule, why))
    print("LINT PASS %d files" % n if not k else "LINT FAIL %d finding(s) in %d files" % (k, n))
    return 0 if not k else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
