#!/usr/bin/env python3
"""Tests for fix.py. Synthetic images made here. Prints PASS/FAIL per test, exits 1 on any fail."""
import json
import math
import os
import subprocess
import sys
import tempfile

import cv2
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(HERE)
sys.path.insert(0, SCRIPTS)
import fix  # noqa: E402

RNG = np.random.RandomState(7)
RESULTS = []


def record(name, ok, detail):
    RESULTS.append(ok)
    print("%s  %s  (%s)" % ("PASS" if ok else "FAIL", name, detail))


def f32(u8img):
    return u8img.astype(np.float32) / 255.0


def horizon_image(tilt_deg, w=900, h=600):
    """Sky above, ground below; the boundary slopes down to the right by tilt_deg. Posts + noise as distractors."""
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    line = h / 2 + math.tan(math.radians(tilt_deg)) * (xx - w / 2)
    img = np.zeros((h, w, 3), np.float32)
    sky = np.array([235, 190, 120], np.float32)  # BGR
    gnd = np.array([40, 70, 50], np.float32)
    mask = (yy < line)[..., None]
    img[:] = np.where(mask, sky, gnd)
    img = img.astype(np.uint8)
    for x in (120, 380, 700):  # vertical posts
        cv2.rectangle(img, (x, 120), (x + 14, 300), (30, 30, 30), -1)
    img = np.clip(img.astype(np.float32) + RNG.normal(0, 3, img.shape), 0, 255).astype(np.uint8)
    return img


def measure_tilt(img_u8):
    """Independent measure: standard Hough, near-horizontal lines, vote-weighted angle. Degrees, + = down to the right."""
    g = cv2.GaussianBlur(cv2.cvtColor(img_u8, cv2.COLOR_BGR2GRAY), (0, 0), 1.5)
    e = cv2.Canny(g, 40, 120)
    lines = cv2.HoughLines(e, 1, np.pi / 3600, int(0.45 * img_u8.shape[1]))
    assert lines is not None, "no lines found by measure"
    vals = []
    for rho, theta in lines[:8, 0]:
        a = math.degrees(theta) - 90.0
        if abs(a) < 10:
            vals.append(a)
    assert vals, "no near-horizontal line found by measure"
    return float(np.median(vals))


def test_rotate_level():
    img = horizon_image(2.0)
    before = measure_tilt(img)
    for label, p in (("explicit", {"op": "rotate_level", "deg": 2.0}), ("auto", {"op": "rotate_level", "deg": "auto"})):
        out, rep = fix.apply_ops(f32(img), [p])
        after = measure_tilt(fix.u8(out))
        ok = abs(before - 2.0) < 0.4 and abs(after) < 0.3 and rep[0]["applied"] and out.shape == f32(img).shape
        record("rotate_level %s" % label, ok, "tilt before %.2f deg, after %.2f deg" % (before, after))


def lstar_mean(img, cx, cy, r):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)[..., 0]
    h, w = lab.shape
    yy, xx = np.mgrid[0:h, 0:w]
    m = (xx - cx) ** 2 + (yy - cy) ** 2 <= r * r
    return float(lab[m].mean())


def test_burn_region():
    h, w = 600, 800
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    base = np.full((h, w), 0.35, np.float32)
    glow = np.exp(-((xx ** 2 + yy ** 2) / (2 * 170.0 ** 2)))  # glow at top-left corner
    g = np.clip(base + 0.6 * glow, 0, 1)
    img = np.dstack([g, g, g])
    out, rep = fix.apply_ops(img, [{"op": "burn_region", "cx": 0.0, "cy": 0.0, "r": 0.45, "stops": 2.0}])
    d_corner = lstar_mean(img, 0, 0, 120) - lstar_mean(out, 0, 0, 120)
    d_centre = abs(lstar_mean(img, w / 2, h / 2, 60) - lstar_mean(out, w / 2, h / 2, 60))
    record("burn_region corner glow", d_corner >= 10 and d_centre < 2 and rep[0]["applied"],
           "corner L* drop %.1f (need >=10), centre change %.2f (need <2)" % (d_corner, d_centre))


def rel_lum(bgr):
    c = np.array([bgr[2], bgr[1], bgr[0]], np.float64) / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def wcag(a, b):
    la, lb = rel_lum(a), rel_lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def test_plate_behind_text():
    h, w = 400, 800
    img = np.full((h, w, 3), 205, np.uint8)
    img = np.clip(img + RNG.normal(0, 2, img.shape), 0, 255).astype(np.uint8)
    cv2.putText(img, "GAME 7", (110, 230), cv2.FONT_HERSHEY_DUPLEX, 3.0, (255, 255, 255), 8, cv2.LINE_AA)
    # text core = pixels at pure white (before blending)
    core = (img.min(axis=2) >= 252)
    box = [0.08, 0.3, 0.92, 0.7]
    x0, y0, x1, y1 = int(box[0] * w), int(box[1] * h), int(box[2] * w), int(box[3] * h)
    inbox = np.zeros((h, w), bool)
    inbox[y0:y1, x0:x1] = True
    core &= inbox

    def contrast(im):
        text = np.median(im[core].reshape(-1, 3), axis=0)
        bgm = inbox & ~cv2.dilate(core.astype(np.uint8), np.ones((15, 15), np.uint8)).astype(bool)
        bg = np.median(im[bgm].reshape(-1, 3), axis=0)
        return wcag(text, bg)

    c0 = contrast(img)
    out, rep = fix.apply_ops(f32(img), [{"op": "plate_behind_text", "box": box, "color": "black", "opacity": 0.8}])
    c1 = contrast(fix.u8(out))
    record("plate_behind_text contrast", c0 < 2 and c1 >= 4.5 and rep[0]["applied"],
           "WCAG before %.2f (need <2), after %.2f (need >=4.5)" % (c0, c1))


def test_reframe_lead():
    h, w = 600, 1200
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    g = 0.15 + 0.05 * RNG.rand(h, w).astype(np.float32)
    blob = np.exp(-(((xx - 600) ** 2 + (yy - 300) ** 2) / (2 * 40.0 ** 2)))
    g = np.clip(g + 0.8 * blob, 0, 1)
    img = np.dstack([g, g, g])

    def centroid_frac(im):
        gg = im[..., 1]
        m = (gg > 0.6).astype(np.float32)
        ys, xs = np.nonzero(m)
        return float(xs.mean() / im.shape[1])

    base, _ = fix.apply_ops(img, [{"op": "reframe", "ratio": "1:1", "cx": 0.5, "cy": 0.5}])
    out, rep = fix.apply_ops(img, [{"op": "reframe", "ratio": "1:1", "cx": 0.5, "cy": 0.5, "lead": "right", "lead_share": 0.65}])
    cb, co = centroid_frac(base), centroid_frac(out)
    record("reframe lead=right", cb > 0.45 and co <= 0.4 and rep[0]["applied"],
           "centroid x: no lead %.3f, lead right %.3f (need <=0.40, i.e. >=0.10 left of centre)" % (cb, co))


def textured(h=480, w=720):
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    g = 0.35 + 0.25 * np.sin(xx / 53.0) * np.cos(yy / 41.0) + 0.1 * RNG.rand(h, w)
    img = np.dstack([g * 0.9, g, g * 1.1]).astype(np.float32)
    img = np.clip(img, 0.12, 0.95)
    cv2.rectangle(img, (60, 80), (200, 220), (0.8, 0.3, 0.2), -1)
    cv2.circle(img, (500, 300), 70, (0.2, 0.7, 0.9), -1)
    return img


def edges_ok(img):
    u = fix.u8(img)
    g = cv2.cvtColor(u, cv2.COLOR_BGR2GRAY).astype(np.float32)
    sides = {"top": g[0, :], "bottom": g[-1, :], "left": g[:, 0], "right": g[:, -1]}
    bad = []
    for k, v in sides.items():
        if v.std() < 0.5 or v.mean() < 15:
            bad.append("%s(std %.1f mean %.1f)" % (k, v.std(), v.mean()))
    ring = np.concatenate([g[:2].ravel(), g[-2:].ravel(), g[:, :2].ravel(), g[:, -2:].ravel()])
    if (ring < 8).mean() > 0.005:
        bad.append("black ring pixels %.1f%%" % (100 * (ring < 8).mean()))
    return bad


def test_no_borders():
    img = textured()
    h, w = img.shape[:2]
    cases = [
        {"op": "rotate_level", "deg": 3.0}, {"op": "rotate_level", "deg": -7.5}, {"op": "rotate_level", "deg": 12},
        {"op": "reframe", "ratio": "16:9", "cx": 0.9, "cy": 0.1, "lead": "right", "zoom": 1.5},
        {"op": "reframe", "ratio": "4:5", "cx": 0.05, "cy": 0.95, "lead": "left"},
        {"op": "crop_box", "x0": 0.1, "y0": 0.1, "x1": 0.7, "y1": 0.8},
        {"op": "burn_region", "cx": 0.0, "cy": 0.0, "r": 0.4, "stops": 1.5},
        {"op": "dodge_region", "cx": 1.0, "cy": 1.0, "r": 0.4, "stops": 1.0},
        {"op": "value_curve", "black": 0.1, "white": 0.9, "gamma": 1.2, "s_curve": 0.5},
        {"op": "local_contrast", "mask": "ellipse:0.5,0.5,0.3,0.3", "amount": 0.8},
        {"op": "desaturate_outside", "mask": "ellipse:0.5,0.5,0.3,0.3", "amount": 0.7},
        {"op": "vignette", "amount": 0.3, "softness": 0.6},
        {"op": "plate_behind_text", "box": [0.1, 0.1, 0.5, 0.3], "opacity": 0.5},
        {"op": "move_box", "box": [0.0, 0.1, 0.25, 0.5], "dx": 0.2, "dy": 0.1},
        {"op": "move_box", "box": [0.7, 0.5, 1.0, 1.0], "dx": -0.1, "dy": -0.2},
    ]
    bad_all = []
    for c in cases:
        out, rep = fix.apply_ops(img.copy(), [c])
        bad = edges_ok(out) if rep[0]["applied"] else ["op failed: %s" % rep[0].get("error")]
        if bad:
            bad_all.append("%s %s" % (c["op"], bad))
    # chained
    out, rep = fix.apply_ops(img.copy(), [cases[0], cases[3], cases[6], cases[11]])
    bad = edges_ok(out)
    if bad:
        bad_all.append("chain %s" % bad)
    record("no op produces borders", not bad_all, "%d cases + chain; %s" % (len(cases), "; ".join(bad_all) or "all edges textured"))


def test_cli_board():
    with tempfile.TemporaryDirectory() as td:
        src = os.path.join(td, "in.jpg")
        cv2.imwrite(src, fix.u8(textured(900, 1600)))
        plan = {"variants": [
            {"name": "level and tighter", "ops": [{"op": "rotate_level", "deg": 2}, {"op": "reframe", "ratio": "16:9", "zoom": 1.2}]},
            {"name": "burn corner", "ops": [{"op": "burn_region", "cx": 0, "cy": 0, "r": 0.4, "stops": 1}]},
            {"name": "bad op", "ops": [{"op": "nonsense"}]}],
            "notes": [{"cell": "B3", "label": "bright patch"}, {"from": "A1", "to": [0.5, 0.5], "label": "line"},
                      {"at": [0.9, 0.9], "label": "pin"}, "plain note"]}
        pj = os.path.join(td, "plan.json")
        json.dump(plan, open(pj, "w"))
        out = os.path.join(td, "out")
        r = subprocess.run([sys.executable, os.path.join(SCRIPTS, "fix.py"), src, pj, "--out", out], capture_output=True, text=True)
        rep = json.load(open(os.path.join(out, "fix_report.json")))
        b = cv2.imread(os.path.join(out, "board.jpg"))
        files = all(os.path.exists(os.path.join(out, v["file"])) for v in rep["variants"])
        ok = (b is not None and max(b.shape[:2]) <= 2576 and files and os.path.exists(os.path.join(out, "annotated.jpg"))
              and rep["variants"][0]["ops"][0]["applied"] and not rep["variants"][2]["ops"][0]["applied"]
              and r.returncode == 1 and "nonsense" in r.stderr + json.dumps(rep))
        record("CLI board + report (bad op reported, exit 1)", ok,
               "board %s, exit %d" % (None if b is None else "%dx%d" % (b.shape[1], b.shape[0]), r.returncode))


if __name__ == "__main__":
    for t in (test_rotate_level, test_burn_region, test_plate_behind_text, test_reframe_lead, test_no_borders, test_cli_board):
        try:
            t()
        except Exception as e:  # a crash is a FAIL
            import traceback
            traceback.print_exc()
            record(t.__name__, False, "exception %s" % e)
    n_fail = RESULTS.count(False)
    print("\n%d passed, %d failed" % (RESULTS.count(True), n_fail))
    sys.exit(1 if n_fail else 0)
