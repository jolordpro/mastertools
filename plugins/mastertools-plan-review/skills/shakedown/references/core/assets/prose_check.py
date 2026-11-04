#!/usr/bin/env python3
"""Prose check for review reports (core/report.md, "Prose check").

Checks a Markdown report against a rules file: banned words, em dashes per
paragraph, and Markdown table width. Code blocks and inline code are skipped,
because quoted code is evidence, not prose.

usage:
  prose_check.py REPORT.md [--rules FILE]   exit 1 and list each problem if any rule fails
  prose_check.py --selftest

Rules file: --rules, else ~/.config/mastertools/prose-rules.txt, else prose-rules.txt beside this script.
"""
import os, re, sys
from pathlib import Path


def load_rules(path=None):
    for p in (path, os.path.expanduser("~/.config/mastertools/prose-rules.txt"), Path(__file__).with_name("prose-rules.txt")):
        if p and Path(p).exists():
            rules = {"words": [], "dashes": None, "cols": None}
            for ln in Path(p).read_text().splitlines():
                ln = ln.strip()
                if not ln or ln.startswith("#"):
                    continue
                k, _, v = ln.partition(":")
                v = v.strip()
                if k == "word":
                    rules["words"].append(v)
                elif k == "max-dashes-per-paragraph":
                    rules["dashes"] = int(v)
                elif k == "max-table-columns":
                    rules["cols"] = int(v)
            return rules
    raise SystemExit("prose_check: no rules file found - blocked.")


def check(text, rules):
    problems, in_code, para, para_start = [], False, [], 1
    lines = text.splitlines()

    def close_para(end):
        if rules["dashes"] is not None and para:
            n = sum(l.count("—") for l in para)
            if n > rules["dashes"]:
                problems.append(f"line {para_start}: {n} em dashes in one paragraph (max {rules['dashes']})")

    for i, raw in enumerate(lines, 1):
        if raw.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        ln = re.sub(r"`[^`]*`", "", raw)
        if not ln.strip():
            close_para(i); para = []; para_start = i + 1
            continue
        if not para:
            para_start = i
        para.append(ln)
        for w in rules["words"]:
            if re.search(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", ln, re.I):
                problems.append(f"line {i}: banned word \"{w}\"")
        if rules["cols"] is not None and ln.strip().startswith("|") and not re.match(r"^\s*\|[\s:|-]+\|\s*$", ln):
            cols = len([c for c in ln.strip().strip("|").split("|")])
            if cols > rules["cols"]:
                problems.append(f"line {i}: table with {cols} columns (max {rules['cols']})")
    close_para(len(lines))
    return problems


def selftest():
    rules = {"words": ["really", "leverage"], "dashes": 1, "cols": 2}
    bad = "This is really bad — and worse — today.\n\n| a | b | c |\n|---|---|---|\n\nWe leverage it."
    good = "This is bad. It is worse today.\n\n| a | b |\n|---|---|\n\n```\nreally — — code is skipped\n```\nThe `leverage` flag is code."
    pb, pg = check(bad, rules), check(good, rules)
    ok = len(pb) == 4 and pg == []
    print("bad:", pb); print("good:", pg)
    print("prose_check self-test:", "PASSED" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    a = sys.argv[1:]
    if "--selftest" in a:
        sys.exit(selftest())
    rules = load_rules(a[a.index("--rules") + 1] if "--rules" in a else None)
    probs = check(Path(a[0]).read_text(), rules)
    print("\n".join(probs) if probs else "prose check: passed")
    sys.exit(1 if probs else 0)
