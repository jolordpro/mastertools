#!/usr/bin/env python3
"""ab_sheets.py: blind A/B judging in both orders (Law 5), as one command. DRAFT 2026-10-23.

Make the sheets (each pair twice: original on the left, then on the right) plus a hidden key:
    python3 ab_sheets.py make --pair NAME A.png B.png [--pair NAME2 A2.png B2.png ...] --out DIR [--h 360]
Give the judge `references/critique/judge-prompt.md` and the DIR (never the key). Save its reply as judge.txt, then:
    python3 ab_sheets.py decode DIR judge.txt
which prints, per pair, the winner in each order and whether the two orders agree (only agreeing verdicts count).
    python3 ab_sheets.py --selftest

Judge reply format (one line per sheet):  pair01_order1: A|B|same - reason
Origin: the Between Words rounds, where the both-orders judge agreed 4/4 and 10/10 and drove every keep/drop.
"""
import argparse, json, os, re, sys
import numpy as np
import cv2

F = cv2.FONT_HERSHEY_SIMPLEX


def tile(path, label, h):
    im = cv2.imread(path); im = cv2.resize(im, (int(im.shape[1] * h / im.shape[0]), h), interpolation=cv2.INTER_AREA)
    cv2.rectangle(im, (0, 0), (40, 34), (0, 0, 0), -1); cv2.putText(im, label, (8, 27), F, 0.9, (255, 255, 255), 2, cv2.LINE_AA); return im


def make(pairs, out, h=360):
    os.makedirs(out, exist_ok=True); key = {}
    for k, (name, a, b) in enumerate(pairs, 1):
        gap = np.zeros((h, 6, 3), np.uint8)
        cv2.imwrite(os.path.join(out, "pair%02d_order1.jpg" % k), np.hstack([tile(a, "A", h), gap, tile(b, "B", h)]), [cv2.IMWRITE_JPEG_QUALITY, 90])
        cv2.imwrite(os.path.join(out, "pair%02d_order2.jpg" % k), np.hstack([tile(b, "A", h), gap, tile(a, "B", h)]), [cv2.IMWRITE_JPEG_QUALITY, 90])
        key["%02d" % k] = dict(name=name, original=a, candidate=b)
    json.dump(key, open(os.path.join(out, ".KEY_do_not_show_the_judge.json"), "w"), indent=1)
    return key


def decode(out, reply_text):
    key = json.load(open(os.path.join(out, ".KEY_do_not_show_the_judge.json")))
    got = {(m.group(1), m.group(2)): m.group(3).lower() for m in re.finditer(r"pair(\d+)_order([12])\s*:\s*(A|B|same)\b", reply_text, re.I)}
    res = {}
    for k, v in sorted(key.items()):
        o1, o2 = got.get((k, "1")), got.get((k, "2"))
        w1 = {"a": "original", "b": "candidate", "same": "same"}.get(o1)          # order1: A = original
        w2 = {"a": "candidate", "b": "original", "same": "same"}.get(o2)          # order2: A = candidate
        verdict = w1 if (w1 and w1 == w2) else "disagree" if (w1 and w2) else "missing"
        res[k] = verdict; print("pair%s %-28s order1 %-9s order2 %-9s -> %s" % (k, v["name"], w1, w2, verdict))
    n = sum(1 for v in res.values() if v in ("original", "candidate", "same"))
    print("agreed in both orders: %d of %d" % (n, len(res))); return res


def selftest():
    import tempfile
    d = tempfile.mkdtemp(); ims = []
    for i, c in enumerate([(30, 30, 30), (200, 160, 40), (90, 90, 200)]):
        p = os.path.join(d, "f%d.png" % i); cv2.imwrite(p, np.full((90, 160, 3), c, np.uint8)); ims.append(p)
    make([("p1", ims[0], ims[1]), ("p2", ims[0], ims[2]), ("p3", ims[1], ims[2])], d, h=90)
    reply = "pair01_order1: B - x\npair01_order2: A - x\npair02_order1: A - x\npair02_order2: A - x\npair03_order1: same - x\npair03_order2: same - x"
    r = decode(d, reply)
    ok = r == {"01": "candidate", "02": "disagree", "03": "same"} and os.path.exists(os.path.join(d, "pair02_order2.jpg"))
    print("selftest", "PASS" if ok else "FAIL (order flip not decoded)"); return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv: sys.exit(0 if selftest() else 1)
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0]); sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("make"); m.add_argument("--pair", nargs=3, action="append", metavar=("NAME", "ORIGINAL", "CANDIDATE"), required=True)
    m.add_argument("--out", required=True); m.add_argument("--h", type=int, default=360)
    dd = sub.add_parser("decode"); dd.add_argument("dir"); dd.add_argument("reply")
    a = ap.parse_args()
    if a.cmd == "make": make(a.pair, a.out, a.h); print("sheets in", a.out, "(give the judge the .jpg files only)")
    else: decode(a.dir, open(a.reply).read())
