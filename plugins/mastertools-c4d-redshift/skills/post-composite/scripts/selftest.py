#!/usr/bin/env python3
"""selftest.py: prove analyze_plate.py's detectors on synthetic plates with known answers.

Usage: python3 selftest.py [--keep DIR]

Builds two 1280x720 ProRes 422 HQ 10-bit Rec.709 plates (36 frames, 23.976):
  A  locked camera, no distortion
  B  same scene with 1.2 x 0.8 px drift and barrel distortion
Each has a one-point corridor (VP at 700,300), a clipped window, an unclipped practical with a
halo and a floor reflection streak under it, a dark panel lifted by haze toward the VP, a dark
subject moving 4 px/frame with 180-degree motion blur, lens blur and per-channel noise.
Then runs analyze_plate.py on both and checks each measurement against the truth.
Exit code 0 only if every check passes.
"""
import json, math, os, subprocess, sys, tempfile, argparse
import numpy as np
import cv2

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, N = 1280, 720, 36
VP = (700.0, 300.0)
SIG = (0.004, 0.003, 0.008)          # R'G'B' noise sigma
SUBJ_SPEED = 4.0                     # px/frame
SHUTTER = 0.5                        # 180 degrees


def base_scene(rng):
    img = np.zeros((H, W, 3), np.float32)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    # walls / floor / ceiling tones
    img[:] = (0.50, 0.52, 0.50)
    floor = yy > VP[1] + (np.abs(xx - VP[0]) * 0.55)
    ceil = yy < VP[1] - (np.abs(xx - VP[0]) * 0.45)
    img[floor] = (0.58, 0.58, 0.55)
    img[ceil] = (0.66, 0.68, 0.68)
    # texture so there is something to track
    tex = cv2.GaussianBlur(rng.standard_normal((H, W)).astype(np.float32), (0, 0), 2.0) * 0.06
    img += tex[..., None]
    # lines into the VP
    for ang in np.linspace(-150, -30, 9).tolist() + np.linspace(20, 160, 9).tolist():
        a = math.radians(ang)
        p2 = (int(VP[0] + 2000 * math.cos(a)), int(VP[1] + 2000 * math.sin(a)))
        cv2.line(img, (int(VP[0] + 60 * math.cos(a)), int(VP[1] + 60 * math.sin(a))), p2, (0.30, 0.30, 0.30), 2, cv2.LINE_AA)
    # true verticals (door edges) near the frame edges, horizontals
    for x in (60, 140, 1150, 1230):
        cv2.line(img, (x, 40), (x, 690), (0.22, 0.22, 0.22), 3, cv2.LINE_AA)
    for y in (90, 640):
        cv2.line(img, (240, y), (1040, y), (0.25, 0.25, 0.25), 2, cv2.LINE_AA)
    # dark panel on the right wall running into depth, lifted toward the VP (haze)
    poly = np.array([[760, 250], [1100, 60], [1100, 600], [760, 345]], np.int32)
    pm = np.zeros((H, W), np.uint8)
    cv2.fillPoly(pm, [poly], 1)
    lift = np.clip(1 - (xx - 760) / 340, 0, 1)            # 1 at the far end, 0 near
    dark = 0.03 + 0.05 * lift
    for c in range(3):
        img[..., c] = np.where(pm > 0, dark + tex * 0.05, img[..., c])
    # clipped window at the VP
    img[255:345, 655:745] = 1.0
    # static dark post beside the subject's path: the lens-softness reference for the shutter estimate
    img[420:620, 625:660] = (0.10, 0.10, 0.11)
    # unclipped practical with a halo
    halo = np.zeros((H, W), np.float32)
    halo[76:86, 270:330] = 1
    halo = cv2.GaussianBlur(halo, (0, 0), 6) * 0.25
    img += halo[..., None]
    img[76:86, 270:330] = (0.82, 0.80, 0.74)
    # its floor reflection streak, straight below
    st = np.zeros((H, W), np.float32)
    st[470:660, 297:303] = 1
    st = cv2.GaussianBlur(st, (0, 0), 1.2) * 0.25
    img += st[..., None]
    return img


def subject_alpha(t):
    a = np.zeros((H, W), np.float32)
    cols = np.arange(W, dtype=np.float32)
    subs = 16
    for s in range(subs):
        x0 = 380 + SUBJ_SPEED * (t + SHUTTER * (s + 0.5) / subs)
        cov = np.clip(np.minimum(cols + 1, x0 + 70) - np.maximum(cols, x0), 0, 1)
        a[400:640] += cov[None, :]
    return a / subs


def barrel_maps(k1=0.035):
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    cx, cy = W / 2, H / 2
    rn = math.hypot(cx, cy)
    dx, dy = (xx - cx) / rn, (yy - cy) / rn
    f = 1 + k1 * (dx * dx + dy * dy)
    return (cx + dx * f * rn).astype(np.float32), (cy + dy * f * rn).astype(np.float32)


def render(path, drift=(0, 0), distort=False, seed=3):
    rng = np.random.default_rng(seed)
    base = base_scene(rng)
    maps = barrel_maps() if distort else None
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb48le", "-s", f"{W}x{H}",
           "-r", "24000/1001", "-i", "-", "-vf", "scale=out_color_matrix=bt709:out_range=tv",
           "-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le",
           "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709", "-color_range", "tv", path]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for t in range(N):
        img = base.copy()
        a = subject_alpha(t)[..., None]
        img = img * (1 - a) + np.float32([0.07, 0.07, 0.08]) * a
        img = cv2.GaussianBlur(img, (0, 0), 1.0)
        if drift != (0, 0):
            f = t / (N - 1)
            M = np.float32([[1, 0, drift[0] * f], [0, 1, drift[1] * f]])
            img = cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
        if maps is not None:
            img = cv2.remap(img, maps[0], maps[1], cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
        img = img + rng.standard_normal(img.shape).astype(np.float32) * np.float32(SIG)
        p.stdin.write((np.clip(img, 0, 1) * 65535 + 0.5).astype("<u2").tobytes())
    p.stdin.close()
    p.wait()


def run(plate, out):
    subprocess.run([sys.executable, os.path.join(HERE, "analyze_plate.py"), plate, "--out", out],
                   check=True, stdout=subprocess.DEVNULL)
    return json.load(open(os.path.join(out, "plate_analysis.json")))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep")
    a = ap.parse_args()
    d = a.keep or tempfile.mkdtemp(prefix="plate_selftest_")
    os.makedirs(d, exist_ok=True)
    pa, pb = os.path.join(d, "A_locked.mov"), os.path.join(d, "B_drift_barrel.mov")
    render(pa)
    render(pb, drift=(1.2, 0.8), distort=True)
    A = run(pa, os.path.join(d, "A"))
    B = run(pb, os.path.join(d, "B"))
    sy = math.sqrt((0.2126 * SIG[0]) ** 2 + (0.7152 * SIG[1]) ** 2 + (0.0722 * SIG[2]) ** 2)
    checks = []

    def chk(name, ok, got):
        checks.append((name, bool(ok), got))

    chk("A camera locked", A["camera"]["classification"] == "locked", A["camera"]["max_drift_px"])
    vp = A["perspective"].get("vanishing_points") or [{}]
    chk("A VP within 15 px of truth", vp[0] and math.hypot(vp[0]["x"] - VP[0], vp[0]["y"] - VP[1]) < 15,
        (vp[0].get("x"), vp[0].get("y")))
    regs = A["clipping"]["regions"]
    chk("A clipped window found", any(655 <= r["centroid"][0] <= 745 and 255 <= r["centroid"][1] <= 345 for r in regs),
        [r["centroid"] for r in regs])
    prac = [p for p in A["practicals"]["items"] if p["clipped_frac"] < 0.02]
    chk("A unclipped practical found", any(270 <= p["centroid"][0] <= 330 and 70 <= p["centroid"][1] <= 92 for p in prac),
        [p["centroid"] for p in prac[:4]])
    sts = [s for s in A["floor_gloss"]["streaks"] if s["likely_reflection"]]
    chk("A floor streak found and paired", any(s["bbox"][0] <= 300 <= s["bbox"][0] + s["bbox"][2] and s["paired_with_source"] for s in sts),
        [(s["bbox"], s["paired_with_source"]) for s in sts])
    chk("A dark panel candidate", any(740 <= p["bbox"][0] <= 800 for p in A["dark_panels"]["candidates"]),
        [p["bbox"] for p in A["dark_panels"]["candidates"]])
    hz = A["haze"]
    chk("A haze detected, lift 0.02-0.07", hz.get("haze_present") and 0.02 <= hz["lift"] <= 0.07, hz.get("lift"))
    g = A["grain"]["bands"]["mids"]
    chk("A luma noise within 30%", abs(g["Y"] - sy) / sy < 0.30, (g["Y"], round(sy, 5)))
    chk("A blue noisiest", g["B"] > g["G"] and g["B"] > g["R"], (g["R"], g["G"], g["B"]))
    sub = A["subject"]
    # flow speed is the measurement; the box/centroid of a slow self-overlapping mover keeps some of the
    # median-background ghost (conservative for holdouts), so only check the box covers the true subject
    last = sub.get("bbox_last") or [0, 0, 0, 0]
    tx0 = 380 + SUBJ_SPEED * (N - 1)
    chk("A subject speed 4 px/frame +-1, box covers it", sub.get("present") and abs((sub.get("flow_speed_px_per_frame") or 0) - 4) <= 1
        and last[0] <= tx0 + 5 and last[0] + last[2] >= tx0 + 65 and last[1] <= 405 and last[1] + last[3] >= 635,
        (sub.get("flow_speed_px_per_frame"), last))
    mb = A["motion_blur"]
    chk("A shutter 90-270 deg", mb.get("measured") and 90 <= mb["shutter_deg_estimate"] <= 270, mb.get("shutter_deg_estimate"))
    chk("A no distortion", not A["lens_distortion"].get("distortion_likely"), A["lens_distortion"].get("edge_bow_px"))
    exp = math.hypot(1.2, 0.8)
    chk("B camera 2d_drift", B["camera"]["classification"] == "2d_drift", B["camera"]["classification"])
    chk("B drift magnitude +-0.3 px", abs(B["camera"]["max_drift_px"] - exp) < 0.3, (B["camera"]["max_drift_px"], round(exp, 3)))
    # truth: k1 0.035 bends a full-height vertical at the frame edge ~5.4 px
    chk("B barrel detected, edge bow 4.0-6.8 px", B["lens_distortion"].get("distortion_likely") and
        B["lens_distortion"].get("type") == "barrel" and 4.0 <= (B["lens_distortion"].get("edge_bow_px") or 0) <= 6.8,
        (B["lens_distortion"].get("edge_bow_px"), B["lens_distortion"].get("type")))
    w = max(len(c[0]) for c in checks)
    for n_, ok, got in checks:
        print(("PASS  " if ok else "FAIL  ") + n_.ljust(w) + "  got " + str(got))
    nf = sum(not c[1] for c in checks)
    print("\n%d/%d passed   (plates and outputs in %s)" % (len(checks) - nf, len(checks), d))
    sys.exit(1 if nf else 0)


if __name__ == "__main__":
    main()
