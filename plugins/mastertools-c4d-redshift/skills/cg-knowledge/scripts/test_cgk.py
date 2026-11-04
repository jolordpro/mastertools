#!/usr/bin/env python3
"""Self-test for cgk.py against a throwaway knowledge base. Run: python3 -I test_cgk.py"""
import os
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
CGK = HERE / "cgk.py"

CARD = """---
id: {id}
title: test card {id}
domain: lighting
status: {status}
confidence: {conf}
decay: slow
read: 2026-01-01
recheck_by: {due}
sources: [test]
conflicts: {conflicts}
feeds: [{feeds}]
---
Body of {id}.
"""

CASES = [
    ("good", "V", "medium", "2099-01-01", "none", "EVIDENCE"),
    ("high", "V", "high", "2099-01-01", "none (ledger checked)", "EVIDENCE"),
    ("summary", "V2", "medium", "2099-01-01", "none", "TO-VERIFY"),
    ("lowconf", "V", "low", "2099-01-01", "none", "TO-VERIFY"),
    ("ours", "U", "medium", "2099-01-01", "none", "TO-VERIFY"),
    ("stale", "V", "medium", "2000-01-01", "none", "TO-VERIFY"),
    ("fights", "V", "high", "2099-01-01", "ledger", "TO-VERIFY"),
]


def run(args, kb):
    env = dict(os.environ, CG_KNOWLEDGE_DIR=str(kb))
    p = subprocess.run([sys.executable, "-I", str(CGK), *args], env=env, capture_output=True, text=True)
    return p.returncode, p.stdout


def main():
    fails = 0

    def check(name, ok):
        nonlocal fails
        print(("ok   " if ok else "FAIL ") + name)
        fails += 0 if ok else 1

    with tempfile.TemporaryDirectory() as tmp:
        kb = pathlib.Path(tmp)
        (kb / "scripts").mkdir()
        (kb / "scripts" / "kb.py").write_text("import sys; print('kb.py find', *sys.argv[2:])\n")
        (kb / "cards" / "lighting").mkdir(parents=True)
        for cid, st, conf, due, conflicts, _ in CASES:
            (kb / "cards" / "lighting" / f"{cid}.md").write_text(
                CARD.format(id=cid, status=st, conf=conf, due=due, conflicts=conflicts,
                            feeds="redshift, polish coach" if cid == "good" else "polish-coach"))

        code, out = run(["where"], kb)
        check("where counts 7 cards", code == 0 and "7 cards" in out and "1 U" in out and "1 V2" in out)

        for cid, *_, want in CASES:
            code, out = run(["grade", cid], kb)
            check(f"grade {cid} -> {want}", out.startswith(want))

        code, out = run(["grade", "nope"], kb)
        check("grade missing card -> MISSING, exit 0", out.startswith("MISSING") and code == 0)
        code, out = run(["grade", "\n".join(["good-card-id-" + str(i) for i in range(40)])], kb)
        check("pasted multi-line id -> MISSING, no crash", out.startswith("MISSING") and code == 0)
        code, out = run(["grade", "*"], kb)
        check("glob as id -> MISSING", out.startswith("MISSING"))
        code, _ = run(["grade", "--strict", "good", "high"], kb)
        check("strict passes when all are evidence", code == 0)
        code, _ = run(["grade", "--strict", "good", "summary"], kb)
        check("strict fails on one V2", code == 1)

        code, out = run(["show", "good"], kb)
        check("show prints the card", code == 0 and "Body of good." in out)
        code, _ = run(["show", "nope"], kb)
        check("show missing card exits 1", code == 1)

        code, out = run(["find", "glass", "ior"], kb)
        check("find hands off to kb.py", code == 0 and "kb.py find glass ior" in out)

        code, out = run(["feeds"], kb)
        check("feeds lists names with counts, spelling merged", code == 0 and "7  polish-coach" in out and "1  redshift" in out)
        code, out = run(["feeds", "redshift", "--all"], kb)
        check("feeds redshift finds only the card that lists it", code == 0 and "1 cards feed 'redshift'" in out and "good  [V·medium]" in out and "summary" not in out)
        code, out = run(["feeds", "Polish", "Coach"], kb)
        check("feeds matches across spaces and case", code == 0 and "7 cards feed 'polish-coach'" in out)
        code, _ = run(["feeds", "nothing-feeds-this"], kb)
        check("feeds with no match exits 1", code == 1)

    code, out = run(["where"], pathlib.Path(tmp) / "gone")
    check("unreachable base exits 3", code == 3 and "not reachable" in out)

    print(f"\n{fails} failed" if fails else "\nall passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
