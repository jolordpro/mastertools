#!/usr/bin/env python3
"""selftest_harmonize.py: prove harmonize.py on a synthetic painted wall with a known answer.

Usage: python3 selftest_harmonize.py [--keep DIR]

Builds a 1280x720 wall (albedo 0.5) under a warm light that falls off left to right (light tints in ACEScg,
as Redshift renders), with a black patch
(reflectance 0.03), 3% veiling glare, lens blur sigma 1.5 px and grain. The truth has a painted logo on that
wall under the same light. harmonize.py sees only the plate and the flat logo. Checks:
  composite vs truth on the ground-truth bar, glare floor read off the black patch, no floor without it,
  edge blur measured near the logo, the cast LUT vs its matrix, and every --kind runs.
Exit code 0 only if every check passes. The real-render version of this test lives in
post-composite-workspace/harmonize-build/ (C4D/Redshift truth, 2026-10-27).
"""
import argparse, json, os, subprocess, sys, tempfile
import numpy as np
import cv2

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from harmonize_core import LUMA, M709, lin, enc, blur, bradford
from harmonize import apply_cube

W, H = 1280, 720
RHO, PAINT, BLACK, VEIL, LENS = 0.5, 0.85, 0.03, 0.03 * 0.35, 1.5
LIGHT = np.array([1.0, 0.86, 0.68])          # warm, linear Rec.709, luminance-normalised below
AP1_TO_709 = np.linalg.inv(np.array([[0.6130974, 0.3395232, 0.0473795],
                                     [0.0701942, 0.9163539, 0.0134519],
                                     [0.0206156, 0.1095698, 0.8698146]]))
# The light tints surfaces channel by channel in ACEScg, as Redshift does. HARMONIZE_TINT_SPACE=rec709 tints in
# Rec.709 instead: it also passes, with a larger median error (0.09 vs 0.03 stop; measured 2026-10-27).
TINT_SPACE = os.environ.get("HARMONIZE_TINT_SPACE", "acescg")
DESIGN = {"navy": (20, 33, 61), "white": (255, 255, 255), "red": (208, 32, 46)}
BAR = {"lum_med": 0.15, "lum_p90": 0.35, "de_med": 3.0, "de_p90": 6.0, "duv": 0.004}


def scene(with_logo, with_black, rng):
    yy, xx = np.mgrid[0:H, 0:W].astype(float)
    E = 0.7 * (1.15 - 0.6 * xx / W) * (1 - 0.25 * ((yy - 360) / 720) ** 2)
    light = LIGHT / (LIGHT @ LUMA)
    refl = np.full((H, W, 3), RHO)
    if with_black:
        refl[230:272, 560:640] = BLACK         # just above the logo: inside the edge and black search areas
    if with_logo:
        refl = refl * (1 - logo_alpha[..., None]) + logo_refl * logo_alpha[..., None]
    if TINT_SPACE == "acescg":
        to_ap1 = np.linalg.inv(AP1_TO_709)
        lit = (refl @ to_ap1.T) * (to_ap1 @ light)
        img = VEIL + (lit @ AP1_TO_709.T) * E[..., None]
    else:
        img = VEIL + refl * E[..., None] * light
    img = enc(blur(img, LENS))
    img = img + rng.normal(0, 1, img.shape) * np.array([0.004, 0.003, 0.006])
    return np.clip(img, 0, 1)


def make_logo():
    ss = 4
    cx, cy = 640 * ss, 360 * ss
    lab = np.zeros((H * ss, W * ss), np.uint8)
    cv2.ellipse(lab, (cx, cy), (110 * ss, 70 * ss), 0, 0, 360, 3, -1)
    cv2.ellipse(lab, (cx, cy), (95 * ss, 58 * ss), 0, 0, 360, 2, -1)
    cv2.ellipse(lab, (cx, cy), (80 * ss, 47 * ss), 0, 0, 360, 1, -1)
    cv2.rectangle(lab, (cx - 45 * ss, cy - 9 * ss), (cx + 45 * ss, cy + 9 * ss), 2, -1)
    cols = {1: "red", 2: "white", 3: "navy"}
    rgb = np.zeros((H * ss, W * ss, 3))
    for k, n in cols.items():
        rgb[lab == k] = np.array(DESIGN[n]) / 255
    alpha = cv2.resize((lab > 0).astype(np.float32), (W, H), interpolation=cv2.INTER_AREA)
    prem = cv2.resize(rgb.astype(np.float32) * (lab > 0)[..., None], (W, H), interpolation=cv2.INTER_AREA)
    straight = prem / np.maximum(alpha[..., None], 1e-6)
    refl = lin(straight) * PAINT
    labs = cv2.resize(lab, (W, H), interpolation=cv2.INTER_NEAREST)
    return straight.astype(float), alpha.astype(float), refl.astype(float), labs


def lab_of(rgb_lin):
    xyz = rgb_lin @ M709.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > (6 / 29) ** 3, np.cbrt(np.clip(xyz, 0, None)), xyz / (3 * (6 / 29) ** 2) + 4 / 29)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def de76(a, b):
    return np.linalg.norm(lab_of(a) - lab_of(b), axis=-1)


def uv(rgb):
    X, Y, Z = M709 @ rgb
    d = X + 15 * Y + 3 * Z
    return np.array([4 * X / d, 6 * Y / d])


def w16(path, x):
    code = cv2.COLOR_RGBA2BGRA if x.shape[2] == 4 else cv2.COLOR_RGB2BGR
    cv2.imwrite(path, cv2.cvtColor((np.clip(x, 0, 1) * 65535 + 0.5).astype(np.uint16), code))


def r16(path):
    return cv2.cvtColor(cv2.imread(path, -1), cv2.COLOR_BGR2RGB).astype(np.float64) / 65535


def harm(plate, layer, out, kind="painted"):
    r = subprocess.run([sys.executable, os.path.join(HERE, "harmonize.py"), plate, layer, "--kind", kind,
                        "--wall-albedo", str(RHO), "--out", out], capture_output=True, text=True)
    return r.returncode == 0, r.stderr[-400:]


logo_straight, logo_alpha, logo_refl, logo_lab = make_logo()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep")
    a = ap.parse_args()
    d = a.keep or tempfile.mkdtemp(prefix="harmonize_selftest_")
    os.makedirs(d, exist_ok=True)
    rng = np.random.default_rng(7)
    plate, truth = scene(False, True, rng), scene(True, True, np.random.default_rng(8))
    plate_nb = scene(False, False, np.random.default_rng(9))
    w16(os.path.join(d, "plate.png"), plate)
    w16(os.path.join(d, "plate_noblack.png"), plate_nb)
    w16(os.path.join(d, "layer.png"), np.dstack([logo_straight, logo_alpha]))
    checks = []

    ok, err = harm(os.path.join(d, "plate.png"), os.path.join(d, "layer.png"), os.path.join(d, "painted"))
    checks.append(("painted run", ok, err))
    if ok:
        comp, info = r16(os.path.join(d, "painted", "harmonized.png")), json.load(open(os.path.join(d, "painted", "harmonize.json")))
        inner = cv2.erode((logo_alpha >= 0.98).astype(np.uint8), np.ones((7, 7))) > 0
        white = inner & (logo_lab == 2)
        cl, tl = lin(blur(comp, 2.0)), lin(blur(truth, 2.0))          # compare light, not grain
        yl = np.log2(np.maximum(cl[inner] @ LUMA, 1e-6) / np.maximum(tl[inner] @ LUMA, 1e-6))
        de = de76(cl[inner], tl[inner])
        s = {"lum_med": float(np.median(np.abs(yl))), "lum_p90": float(np.percentile(np.abs(yl), 90)),
             "de_med": float(np.median(de)), "de_p90": float(np.percentile(de, 90)),
             "duv": float(np.hypot(*(uv(cl[white].mean(0)) - uv(tl[white].mean(0)))))}
        checks.append(("composite vs truth on the bar", all(s[m] <= BAR[m] for m in BAR), {k: round(v, 4) for k, v in s.items()}))
        f = info["glare_floor"]["floor"]
        checks.append(("glare floor within 30%% of %.4f" % VEIL, abs(f - VEIL) <= 0.3 * VEIL, round(f, 5)))
        ps = info["softness"]["plate_edge_sigma_px"]
        checks.append(("plate edge blur within 0.3 px of %.1f" % LENS, ps is not None and abs(ps - LENS) <= 0.3, ps))
        T = np.array(info["cast_matrix_linear"])
        cols = logo_straight[inner]
        dl = float(np.abs(apply_cube(os.path.join(d, "painted", "cast.cube"), cols) - np.clip(enc(lin(cols) @ T.T), 0, 1)).max())
        checks.append(("cast LUT vs matrix within 1/255", dl <= 1 / 255, round(dl, 5)))
    ok, err = harm(os.path.join(d, "plate_noblack.png"), os.path.join(d, "layer.png"), os.path.join(d, "noblack"))
    if ok:
        f = json.load(open(os.path.join(d, "noblack", "harmonize.json")))["glare_floor"]["floor"]
        checks.append(("no black object: floor 0", f == 0.0, f))
    else:
        checks.append(("no black object: run", False, err))
    for kind in ("object", "projected", "emitting", "floating"):
        ok, err = harm(os.path.join(d, "plate.png"), os.path.join(d, "layer.png"), os.path.join(d, kind), kind)
        checks.append(("kind %s runs" % kind, ok, err if not ok else ""))

    w = max(len(c[0]) for c in checks)
    for n, ok, got in checks:
        print(("PASS  " if ok else "FAIL  ") + n.ljust(w) + "  " + str(got))
    passed = sum(1 for c in checks if c[1])
    print("%d/%d checks pass · files in %s" % (passed, len(checks), d))
    sys.exit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()
