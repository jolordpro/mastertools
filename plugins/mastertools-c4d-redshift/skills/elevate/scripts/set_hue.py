#!/usr/bin/env python3
"""set_hue.py: does a set of frames share one hero colour? (CLR-13, DRAFT 2026-10-23)

    python3 set_hue.py --ref REF.png F1.png F2.png ... [--bar 3] [--min-v 0.35] [--min-s 0.5]
    python3 set_hue.py --selftest

For each frame: the median hue (degrees, 0-360) of its bright, saturated pixels (value >= min-v, saturation >= min-s), the
share of the frame they cover, and the difference from the reference frame. PASS within --bar degrees (default 3).
Why these pixels: glow and dim edges drift hue under a tone-mapped view (ACES pushes dim gold orange), so the full-strength
pixels are the honest colour of the hero. Report the halo separately if it matters.
Origin: an abstract-light project (one frame read +6.1 deg off the set, fixed to -0.4; a full colour solve overshot to -12.3).
"""
import argparse, sys
import numpy as np
import cv2


def hero_hue(img_bgr, min_v=0.35, min_s=0.5):
    hsv = cv2.cvtColor(img_bgr.astype(np.float32) / 255.0, cv2.COLOR_BGR2HSV)       # H 0-360, S 0-1, V 0-1
    m = (hsv[..., 2] >= min_v) & (hsv[..., 1] >= min_s)
    if m.sum() < 200: return None, float(m.mean())
    h = hsv[..., 0][m]
    a = np.deg2rad(h); mean = np.rad2deg(np.arctan2(np.sin(a).mean(), np.cos(a).mean())) % 360   # circular, so reds near 0/360 work
    d = (h - mean + 180) % 360 - 180
    return float((mean + np.median(d)) % 360), float(m.mean())


def diff(a, b): return (a - b + 180) % 360 - 180


def run(ref, frames, bar, min_v, min_s):
    r, _ = hero_hue(cv2.imread(ref), min_v, min_s)
    if r is None: sys.exit("reference has no bright saturated pixels: lower --min-v / --min-s")
    print("reference %s: hue %.1f" % (ref, r)); ok_all = True
    for f in frames:
        h, share = hero_hue(cv2.imread(f), min_v, min_s)
        if h is None: print("%-40s  no bright saturated pixels (can't judge)" % f); continue
        d = diff(h, r); ok = abs(d) <= bar; ok_all &= ok
        print("%-40s  hue %5.1f  diff %+5.1f  (%.1f%% of frame)  %s" % (f, h, d, 100 * share, "PASS" if ok else "FAIL"))
    return ok_all


def selftest():
    rng = np.random.default_rng(0)
    def swatch(hue):
        hsv = np.zeros((120, 200, 3), np.float32); hsv[..., 0] = hue; hsv[..., 1] = 0.85; hsv[..., 2] = 0.0
        hsv[40:80, :, 2] = 0.9                                                       # one bright band on black
        hsv[..., 0] += rng.normal(0, 0.8, hsv.shape[:2])
        return (cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) * 255).astype(np.uint8)
    ref, same, off, red = swatch(41), swatch(42), swatch(48), swatch(359)
    checks = [("same gold within 3 deg", abs(diff(hero_hue(same)[0], hero_hue(ref)[0])) <= 3, True),
              ("known miss: 7 deg off must fail", abs(diff(hero_hue(off)[0], hero_hue(ref)[0])) <= 3, False),
              ("red near 0/360 measured as ~359, not ~180", abs(diff(hero_hue(red)[0], 359)) <= 2, True),
              ("black frame: can't judge (None)", hero_hue(np.zeros((50, 50, 3), np.uint8))[0] is None, True)]
    good = True
    for name, got, want in checks:
        print("%-45s %s" % (name, "ok" if got == want else "WRONG")); good &= got == want
    print("selftest", "PASS" if good else "FAIL"); return good


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("frames", nargs="*"); ap.add_argument("--ref"); ap.add_argument("--bar", type=float, default=3.0)
    ap.add_argument("--min-v", type=float, default=0.35); ap.add_argument("--min-s", type=float, default=0.5)
    ap.add_argument("--selftest", action="store_true"); a = ap.parse_args()
    if a.selftest: sys.exit(0 if selftest() else 1)
    if not a.ref or not a.frames: ap.error("give --ref and at least one frame")
    sys.exit(0 if run(a.ref, a.frames, a.bar, a.min_v, a.min_s) else 1)
