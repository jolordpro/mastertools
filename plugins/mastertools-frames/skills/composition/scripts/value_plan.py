#!/usr/bin/env python3
"""value_plan.py: dark field, light event and title room, per frame. DRAFT 2026-10-23.

    python3 value_plan.py IMG [IMG ...] [--json]
    python3 value_plan.py --selftest

Per frame (L* = CIELAB lightness 0-100):
  dark_share     share of pixels with L* < 8 (the black field)
  L_p95, L_max   how bright the brightest 5% and the peak are
  bright_share   share of pixels with L* > 50
  light_event    True when at least 0.3% of the frame is clearly bright (bright_share >= 0.003) [Infer]. False = the "dark and dim"
                 failure: a dark field only works with a clear source. (A first rule on L_p95 called a single thin streak "no
                 event": a light event can be small, so it is measured by bright area, not by percentiles.)
  title_zone     largest empty rectangle on a 16x9 grid of calm cells (cell mean L* < 6 and almost no edges), as a share of
                 the frame, with its cells. Where a title or bug could sit without fighting the picture.
Origin: Between Words 3D rounds, where these numbers decided every keep/drop (they were computed by hand from look.py's
tone and edge_density). Thresholds are starting points to calibrate on graded frames.
"""
import json, sys
import numpy as np
import cv2


def measure(img_bgr, gx=16, gy=9):
    L = cv2.cvtColor(img_bgr.astype(np.float32) / 255.0, cv2.COLOR_BGR2Lab)[..., 0]
    edges = cv2.Canny(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY), 30, 90) > 0
    H, W = L.shape; calm = np.zeros((gy, gx), bool)
    for j in range(gy):
        for i in range(gx):
            sl = (slice(j * H // gy, (j + 1) * H // gy), slice(i * W // gx, (i + 1) * W // gx))
            calm[j, i] = L[sl].mean() < 6 and edges[sl].mean() < 0.002
    best, box = 0, None                                   # largest all-calm rectangle (brute force on a 16x9 grid is cheap)
    for y0 in range(gy):
        for y1 in range(y0, gy):
            rows = calm[y0:y1 + 1].all(0)
            run = 0
            for x in range(gx):
                run = run + 1 if rows[x] else 0
                area = run * (y1 - y0 + 1)
                if area > best: best, box = area, (x - run + 1, y0, x, y1)
    ds, p95, bs = float((L < 8).mean()), float(np.percentile(L, 95)), float((L > 50).mean())
    return dict(dark_share=round(ds, 3), L_p95=round(p95, 1), L_max=round(float(L.max()), 1),
                bright_share=round(bs, 4), light_event=bs >= 0.003, title_zone=round(best / (gx * gy), 3),
                title_zone_cells=dict(x0=box[0], y0=box[1], x1=box[2], y1=box[3], grid=[gx, gy]) if box else None)


def selftest():
    dim = np.zeros((360, 640, 3), np.uint8); cv2.circle(dim, (320, 180), 40, (20, 20, 20), -1)            # dark and dim
    event = np.zeros((360, 640, 3), np.uint8); cv2.line(event, (0, 250), (640, 250), (40, 180, 255), 6)   # one bright streak
    full = np.full((360, 640, 3), 120, np.uint8)                                                            # mid-grey wall to wall
    half = np.zeros((360, 640, 3), np.uint8); half[:, 320:] = 150
    a, b, c, d = measure(dim), measure(event), measure(full), measure(half)
    checks = [("dark + dim flags no light event", a["light_event"] is False), ("one bright streak = light event", b["light_event"] is True),
              ("grey wall has no title zone", c["title_zone"] == 0), ("half-filled frame: zone about half", 0.4 <= d["title_zone"] <= 0.5),
              ("streak frame keeps a big zone above it", b["title_zone"] >= 0.5)]
    ok = all(v for _, v in checks)
    for n, v in checks: print("%-40s %s" % (n, "ok" if v else "WRONG"))
    print("selftest", "PASS" if ok else "FAIL"); return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv: sys.exit(0 if selftest() else 1)
    out = {p: measure(cv2.imread(p)) for p in sys.argv[1:] if not p.startswith("--")}
    if "--json" in sys.argv: print(json.dumps(out, indent=1))
    else:
        for p, m in out.items():
            print("%-44s dark %4.0f%%  bright %5.2f%%  light event %-5s  title zone %4.0f%%" % (p[-44:], 100 * m["dark_share"], 100 * m["bright_share"], m["light_event"], 100 * m["title_zone"]))
