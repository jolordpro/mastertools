#!/usr/bin/env python3
"""look.py: measure a frame and write views, a labelled board and report.json.

Usage:
  python3 look.py IMAGE [--format 16:9|9:16|1:1|4:5|auto] [--out DIR] [--no-vision]

Writes to DIR (default ./look_out/<image name>):
  views/*.jpg   grayscale, notan3, notan4, thumb10, blur, saliency, lines, grid, safe,
                crop_16x9/1x1/4x5/9x16, cvd_deuteranopia, cvd_protanopia
  board.jpg     original + key views, long edge <= 2576 px, one picture for a model
  report.json   metrics from references/systems/metric-recipes.md
  vision.json   raw Apple Vision output (when Vision ran)

Grid convention (shared with elevate/frame_prep.py): columns A-D left to right, rows 1-4 top to bottom.
Coordinates in the report are 0-1 from the top-left. Thresholds marked [Infer] are starting points.
Without Apple Vision (--no-vision, or swiftc/Vision failing) the script falls back to an OpenCV/numpy
saliency approximation and nulls every Vision-only metric with reason "no-vision".
"""
import argparse
import json
import math
import os
import subprocess
import sys
import tempfile
import time

try:
    import cv2
    import numpy as np
except ImportError as _exc:
    sys.stderr.write("look.py needs OpenCV and numpy: pip install opencv-python-headless numpy pillow "
                     "(missing: %s)\n" % _exc.name)
    sys.exit(2)
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.stderr.write("look.py needs Pillow: pip install pillow\n")
    sys.exit(2)

HERE = os.path.dirname(os.path.abspath(__file__))
SWIFT_SRC = os.path.join(HERE, "vision.swift")
SWIFT_BIN = os.path.join(HERE, "vision")
WORK_EDGE = 1800          # analysis long edge (never upscaled)
BOARD_EDGE = 2576
FORMATS = {"16:9": 16 / 9, "1:1": 1.0, "4:5": 4 / 5, "9:16": 9 / 16}
NO_VISION = "no-vision"


# ----------------------------------------------------------------------------- small helpers
def r(v, n=4):
    if v is None:
        return None
    v = float(v)
    if math.isnan(v) or math.isinf(v):
        return None
    return round(v, n)


def metric(value=None, confidence=None, reason=None, **extra):
    """A metric is a dict. confidence is a number or None; None always comes with a reason."""
    d = {"confidence": r(confidence, 2) if confidence is not None else None}
    if reason is not None:
        d["reason"] = reason
    d.update(extra)
    if value is not None:
        d["value"] = value
    if d["confidence"] is None and "reason" not in d:
        d["reason"] = "confidence not defined for this metric"
    return d


def null_metric(reason, **extra):
    return metric(None, None, reason, **extra)


def cell_of(x, y, cols=4, rows=4):
    cx = min(cols - 1, max(0, int(x * cols)))
    cy = min(rows - 1, max(0, int(y * rows)))
    return "%s%d" % (chr(65 + cx), cy + 1)


# ----------------------------------------------------------------------------- Vision runner
def build_vision(log):
    """Compile vision.swift once; rebuild when the source is newer. Returns binary path or None."""
    if not os.path.exists(SWIFT_SRC):
        log.append("vision.swift missing")
        return None
    fresh = os.path.exists(SWIFT_BIN) and os.path.getmtime(SWIFT_BIN) >= os.path.getmtime(SWIFT_SRC)
    if fresh:
        return SWIFT_BIN
    try:
        p = subprocess.run(["swiftc", "-O", "-swift-version", "5", SWIFT_SRC, "-o", SWIFT_BIN],
                           capture_output=True, text=True, timeout=240)
    except (OSError, subprocess.SubprocessError) as exc:
        log.append("swiftc unavailable: %s" % exc)
        return None
    if p.returncode != 0:
        log.append("swiftc failed: %s" % p.stderr.strip()[-300:])
        return None
    return SWIFT_BIN


def run_vision(img_path, mask_dir, log, saliency_only=False, timeout=90):
    binp = build_vision(log)
    if not binp:
        return None
    cmd = [binp, img_path]
    if mask_dir:
        cmd += ["--mask-dir", mask_dir]
    if saliency_only:
        cmd += ["--saliency-only"]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except (OSError, subprocess.SubprocessError) as exc:
        log.append("vision run failed: %s" % exc)
        return None
    # Some hosts (sandboxes, OS log noise) add lines to stdout; keep the JSON object, log the rest.
    data, extra = None, []
    for line in p.stdout.splitlines():
        try:
            obj = json.loads(line)
        except ValueError:
            obj = None
        if isinstance(obj, dict) and "ok" in obj and data is None:
            data = obj
        elif line.strip():
            extra.append(line.strip()[:200])
    if extra:
        log.append("vision stdout extra: %s" % " | ".join(extra[:3]))
    if data is None:
        log.append("vision run failed: no JSON result (stderr: %s)" % p.stderr.strip()[-200:])
        return None
    if not data.get("ok"):
        log.append("vision error: %s" % data.get("error"))
        return None
    return data


# ----------------------------------------------------------------------------- fallback saliency
def spectral_residual(gray, out=68):
    """Hou & Zhang spectral residual in numpy; returns an out x out float map (sum not normalised)."""
    h, w = gray.shape
    s = 64.0 / max(h, w)
    small = cv2.resize(gray, (max(8, int(round(w * s))), max(8, int(round(h * s)))), interpolation=cv2.INTER_AREA)
    f = np.fft.fft2(small.astype(np.float64))
    amp, phase = np.abs(f), np.angle(f)
    logamp = np.log(amp + 1e-8)
    resid = logamp - cv2.blur(logamp, (3, 3))
    sal = np.abs(np.fft.ifft2(np.exp(resid + 1j * phase))) ** 2
    sal = cv2.GaussianBlur(sal.astype(np.float32), (0, 0), 2.5)
    sal = cv2.resize(sal, (out, out), interpolation=cv2.INTER_CUBIC)
    sal = np.maximum(sal, 0)
    return sal / (sal.max() + 1e-12)


def grid_peaks(g, count=3, min_dist=0.12):
    """Local maxima of a 2-D map (3x3 smooth), min separation, strength relative to the map max."""
    g = np.asarray(g, dtype=np.float32)
    mx = float(g.max())
    if mx <= 0:
        return []
    sm = cv2.blur(g, (3, 3))
    h, w = sm.shape
    pad = np.pad(sm, 1, mode="constant", constant_values=-1)
    is_max = np.ones_like(sm, dtype=bool)
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx or dy:
                is_max &= sm >= pad[1 + dy:1 + dy + h, 1 + dx:1 + dx + w]
    ys, xs = np.nonzero(is_max & (sm > 0))
    order = np.argsort(-sm[ys, xs])
    chosen = []
    for i in order:
        x, y = (xs[i] + 0.5) / w, (ys[i] + 0.5) / h
        if all(math.hypot(x - c["x"], y - c["y"]) >= min_dist for c in chosen):
            chosen.append({"x": r(x), "y": r(y), "strength": r(sm[ys[i], xs[i]] / mx), "raw": r(sm[ys[i], xs[i]])})
        if len(chosen) >= count:
            break
    return chosen


def approx_attention(gray):
    g = spectral_residual(gray)
    return {"width": 68, "height": 68, "max": r(g.max()), "sum": r(g.sum()),
            "values": [r(v) for v in g.ravel()], "peaks": grid_peaks(g), "approx": "spectral-residual"}


# ----------------------------------------------------------------------------- colour
def to_lab(bgr):
    """float32 Lab (L 0-100) from a BGR uint8 image."""
    return cv2.cvtColor(bgr.astype(np.float32) / 255.0, cv2.COLOR_BGR2Lab)


def srgb_to_lin(c):
    c = np.asarray(c, dtype=np.float64)
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def rel_lum_rgb(rgb01):
    lin = srgb_to_lin(rgb01)
    return lin[..., 0] * 0.2126 + lin[..., 1] * 0.7152 + lin[..., 2] * 0.0722


def contrast_ratio(l1, l2):
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def kmeans(samples, k, seed=0):
    cv2.setRNGSeed(seed)
    crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.5)
    _, labels, centers = cv2.kmeans(samples.astype(np.float32), k, None, crit, 3, cv2.KMEANS_PP_CENTERS)
    return labels.ravel(), centers


def subsample(arr2d, n=60000):
    flat = arr2d.reshape(-1, arr2d.shape[-1]) if arr2d.ndim == 3 else arr2d.reshape(-1, 1)
    if len(flat) > n:
        idx = np.random.RandomState(0).choice(len(flat), n, replace=False)
        flat = flat[idx]
    return flat


# ----------------------------------------------------------------------------- metric pieces
def tone_metrics(L):
    p5, p50, p95 = np.percentile(L, [5, 50, 95])
    spread = p95 - p5
    return {
        "L_p5": r(p5, 2), "L_median": r(p50, 2), "L_p95": r(p95, 2),
        "L_spread_p5_p95": r(spread, 2),
        "rms_contrast": r(np.std(L) / 100.0),
        "flat_flag": bool(spread < 35),   # [Infer] spread under 35 L* reads flat
        "confidence": 1.0,
        "confidence_basis": "pixel measurement",
    }


def notan(L, k):
    flat = subsample(L)
    _, centers = kmeans(flat, k)
    order = np.argsort(centers.ravel())
    cs = centers.ravel()[order]
    idx = np.argmin(np.abs(L.reshape(-1, 1) - cs.reshape(1, -1)), axis=1).reshape(L.shape)
    shares = [float((idx == i).mean()) for i in range(k)]
    cents = []
    for i in range(k):
        ys, xs = np.nonzero(idx == i)
        cents.append({"x": r(xs.mean() / L.shape[1]), "y": r(ys.mean() / L.shape[0])} if len(xs) else None)
    return idx, {"k": k, "centers_L": [r(c, 1) for c in cs], "area_share": [r(s) for s in shares],
                 "centroid": cents, "confidence": 1.0, "confidence_basis": "pixel measurement"}


def notan_image(idx, k):
    lv = np.linspace(0, 255, k).astype(np.uint8)
    return lv[idx]


def subject_dL(Lab, mask):
    if mask is None:
        return None
    m = mask.astype(np.uint8)
    h, w = m.shape
    rad = max(3, int(round(0.05 * min(h, w))))
    ring = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * rad + 1, 2 * rad + 1))) - m
    if ring.sum() < 20 or m.sum() < 20:
        return None
    inside = Lab[m > 0].mean(axis=0)
    outside = Lab[ring > 0].mean(axis=0)
    dL = abs(float(inside[0] - outside[0]))
    dE = float(np.linalg.norm(inside - outside))
    return {"delta_L": r(dL, 2), "delta_E": r(dE, 2), "ring_px": int(rad),
            "low_contrast_flag": bool(dL < 20),                         # [Infer]
            "equiluminance_flag": bool(dL < 5 and dE > 25)}              # [Infer]


def mass_in_mask(sal68, mask):
    if mask is None:
        return None
    m = cv2.resize(mask.astype(np.float32), (sal68.shape[1], sal68.shape[0]), interpolation=cv2.INTER_AREA)
    tot = float(sal68.sum())
    return float((sal68 * m).sum() / tot) if tot > 0 else None


def edge_distances(mask):
    ys, xs = np.nonzero(mask)
    h, w = mask.shape
    d = {"left": xs.min() / w, "right": 1 - (xs.max() + 1) / w, "top": ys.min() / h, "bottom": 1 - (ys.max() + 1) / h}
    px = {"left": 1.0 / w, "right": 1.0 / w, "top": 1.0 / h, "bottom": 1.0 / h}
    touching = [s for s in d if d[s] <= px[s] * 1.5]
    tangent = [s for s in d if px[s] * 1.5 < d[s] <= 0.01]            # within 1% of an edge, not crossing
    return {"per_side": {k: r(v) for k, v in d.items()}, "min_edge_distance": r(min(d.values())),
            "min_side": min(d, key=d.get), "tangent_flag": bool(tangent), "tangent_sides": tangent,
            "touches_edge_sides": touching}


def facing_from_face(face):
    """Horizontal facing from nose offset against the eye midpoint (sign-convention free).
    Returns (dx, strength, confidence) with dx>0 facing image-right; None when landmarks are missing."""
    le, re_, nose = face.get("left_eye"), face.get("right_eye"), face.get("nose")
    if not (isinstance(le, dict) and isinstance(re_, dict) and isinstance(nose, dict)):
        return None
    mid = (le["x"] + re_["x"]) / 2.0
    inter = abs(le["x"] - re_["x"])
    if inter < 1e-4:
        return None
    ratio = (nose["x"] - mid) / inter
    return ratio, face.get("confidence", 0.5)


def facing_from_pose(pose):
    j = pose.get("joints", {})
    nose = j.get("nose_joint")
    ears = [j[k] for k in ("left_ear_joint", "right_ear_joint") if k in j and j[k]["confidence"] > 0.2]
    if not nose or nose["confidence"] < 0.2 or not ears:
        return None
    ex = sum(e["x"] for e in ears) / len(ears)
    ls, rs = j.get("left_shoulder_1_joint"), j.get("right_shoulder_1_joint")
    scale = abs(ls["x"] - rs["x"]) / 2.0 if ls and rs else 0.05
    scale = max(scale, 0.03)
    conf = min([nose["confidence"]] + [e["confidence"] for e in ears])
    return (nose["x"] - ex) / scale, conf


def facing_metrics(subject_bbox, centroid, face_dx, source):
    """Inward score and space ratio from a horizontal facing ratio (>0 = facing image-right)."""
    if face_dx is None or abs(face_dx[0]) < 0.2:
        why = "no face/pose landmarks" if face_dx is None else "subject faces the camera (nose offset %.2f)" % face_dx[0]
        return null_metric(why, source=source)
    d = 1.0 if face_dx[0] > 0 else -1.0
    towards_center = 0.5 - centroid[0]
    inward = 0.0 if abs(towards_center) < 0.02 else (1.0 if d * towards_center > 0 else -1.0)
    x0, x1 = subject_bbox[0], subject_bbox[0] + subject_bbox[2]
    ahead = (1 - x1) if d > 0 else x0
    behind = x0 if d > 0 else (1 - x1)
    ratio = ahead / max(behind, 0.005)
    return metric({
        "direction": "right" if d > 0 else "left", "vector": [d, 0.0], "inward_score": inward,
        "space_ahead": r(ahead), "space_behind": r(behind), "space_ratio_front_back": r(min(ratio, 99.0), 3),
        "outward_near_edge_flag": bool(inward < 0 and ahead < 0.15),    # [Infer] outward within 0.15 of an edge
        "nose_offset_ratio": r(face_dx[0], 3), "source": source},
        confidence=max(0.05, min(1.0, float(face_dx[1]) * min(1.0, abs(face_dx[0]) / 0.5))))


def joint_crop(pose, margin=0.02):
    names = {"left_hand_joint": "wrist", "right_hand_joint": "wrist", "left_forearm_joint": "elbow",
             "right_forearm_joint": "elbow", "left_leg_joint": "knee", "right_leg_joint": "knee",
             "left_foot_joint": "ankle", "right_foot_joint": "ankle"}
    hits = []
    for k, kind in names.items():
        j = pose.get("joints", {}).get(k)
        if j and j["confidence"] >= 0.3:
            d = min(j["x"], 1 - j["x"], j["y"], 1 - j["y"])
            if d <= margin:
                hits.append({"joint": k, "kind": kind, "edge_distance": r(d), "confidence": j["confidence"]})
    return hits


# ----------------------------------------------------------------------------- lines
def detect_lines(gray):
    """Returns array of segments (x1,y1,x2,y2) in pixels. LSD where available, else probabilistic Hough."""
    segs = None
    try:
        lsd = cv2.createLineSegmentDetector(cv2.LSD_REFINE_STD)
        lines = lsd.detect(gray)[0]
        if lines is not None:
            segs = lines.reshape(-1, 4)
    except (AttributeError, cv2.error):
        segs = None
    if segs is None:
        edges = cv2.Canny(gray, 60, 160)
        hl = cv2.HoughLinesP(edges, 1, np.pi / 360, 60, minLineLength=gray.shape[1] // 12, maxLineGap=8)
        segs = hl.reshape(-1, 4).astype(np.float32) if hl is not None else np.zeros((0, 4), np.float32)
    return segs


def line_stats(segs, w):
    if len(segs) == 0:
        return None
    dx, dy = segs[:, 2] - segs[:, 0], segs[:, 3] - segs[:, 1]
    length = np.hypot(dx, dy)
    ang = np.degrees(np.arctan2(dy, dx))
    ang = (ang + 90) % 180 - 90          # (-90, 90]; positive = slopes down to the right (clockwise)
    keep = length >= 0.04 * w
    return length, ang, keep


def line_horizon(segs, w):
    st = line_stats(segs, w)
    if st is None:
        return None
    length, ang, keep = st
    sel = keep & (np.abs(ang) <= 20)
    if sel.sum() == 0:
        return None
    a, wt = ang[sel], length[sel]
    order = np.argsort(a)
    cw = np.cumsum(wt[order])
    med = float(a[order][np.searchsorted(cw, cw[-1] / 2.0)])
    near = sel & (np.abs(ang - med) < 3)
    return {"angle_deg": r(med, 2), "n_lines": int(near.sum()), "total_length_px": r(length[near].sum(), 1)}


def orientation_shares(segs, w):
    st = line_stats(segs, w)
    if st is None:
        return None
    length, ang, keep = st
    L, A = length[keep], ang[keep]
    if L.sum() == 0:
        return None
    hz = L[np.abs(A) <= 10].sum()
    vt = L[np.abs(A) >= 80].sum()
    return {"horizontal": r(hz / L.sum()), "vertical": r(vt / L.sum()), "diagonal": r(1 - (hz + vt) / L.sum()),
            "n_segments": int(keep.sum())}


# ----------------------------------------------------------------------------- text contrast
def text_contrast(bgr, box, pad=0.05):
    """WCAG contrast for one text box. box = x,y,w,h normalised (OCR box, kept tight so the plate or
    background right behind the glyphs is what gets measured, not the scene beyond a plate).
    Background = majority cluster; text = minority cluster's core (the glyph pixels furthest from the
    background, so anti-aliased edges do not dilute it); worst case over the background's spread."""
    h, w = bgr.shape[:2]
    x0, y0 = int(max(0, (box["x"] - pad * box["w"]) * w)), int(max(0, (box["y"] - pad * box["h"]) * h))
    x1, y1 = int(min(w, (box["x"] + box["w"] * (1 + pad)) * w)), int(min(h, (box["y"] + box["h"] * (1 + pad)) * h))
    if x1 - x0 < 4 or y1 - y0 < 4:
        return None
    patch = bgr[y0:y1, x0:x1].reshape(-1, 3).astype(np.float32)
    if len(patch) < 16:
        return None
    labels, centers = kmeans(patch, 2)
    n0, n1 = int((labels == 0).sum()), int((labels == 1).sum())
    if min(n0, n1) < 0.03 * len(patch):
        # one flat colour: no text pixels separable -> cannot judge
        return None
    t_id = 0 if n0 < n1 else 1
    bg_lum = rel_lum_rgb(patch[labels != t_id][:, ::-1] / 255.0)
    tx_lum = rel_lum_rgb(patch[labels == t_id][:, ::-1] / 255.0)
    bg_med = float(np.median(bg_lum))
    t_lum = float(np.percentile(tx_lum, 10 if np.median(tx_lum) < bg_med else 90))
    cands = [float(np.percentile(bg_lum, 10)), float(np.percentile(bg_lum, 90)), bg_med]
    worst = min(contrast_ratio(t_lum, b) for b in cands)
    typical = contrast_ratio(t_lum, bg_med)
    return {"contrast_worst": r(worst, 2), "contrast_median_bg": r(typical, 2),
            "pass_4_5": bool(worst >= 4.5), "pass_3_0": bool(worst >= 3.0)}


def safe_rects(fmt):
    """Normalised (x0,y0,x1,y1) for graphics-safe and action-safe, plus optional shaded band."""
    if fmt == "9:16":
        # hard box x120-888, y288-1248 of 1080x1920: union of the largest TikTok/Reels/Shorts
        # ad margins (canon/poster-social-vertical, references/broadcast-motion/reframing) [Practice]
        g = (120 / 1080.0, 288 / 1920.0, 888 / 1080.0, 1248 / 1920.0)
        return {"graphics": g, "action": g, "band": (0.0, 1248 / 1920.0, 1.0, 1.0), "note": "9:16 hard box"}
    return {"graphics": (0.05, 0.05, 0.95, 0.95), "action": (0.035, 0.035, 0.965, 0.965), "band": None,
            "note": "%s EBU/SMPTE-style 90%% graphics, 93%% action" % fmt}


def box_inside(box, rect):
    return (box["x"] >= rect[0] and box["y"] >= rect[1] and box["x"] + box["w"] <= rect[2] and box["y"] + box["h"] <= rect[3])


def pick_format(arg, w, h):
    if arg and arg != "auto":
        return arg
    a = w / float(h)
    return min(FORMATS, key=lambda k: abs(math.log(a / FORMATS[k])))


def crop_for(fmt, w, h, cx, cy):
    """Largest crop of aspect fmt inside w x h, centred on (cx,cy) in pixels, clamped. Returns x0,y0,x1,y1."""
    a = FORMATS[fmt]
    cw, ch = (w, w / a) if w / h <= a else (h * a, h)
    cw, ch = min(cw, w), min(ch, h)
    x0 = min(max(cx - cw / 2, 0), w - cw)
    y0 = min(max(cy - ch / 2, 0), h - ch)
    return int(round(x0)), int(round(y0)), int(round(x0 + cw)), int(round(y0 + ch))


# ----------------------------------------------------------------------------- balance
def balance(L, sal68, faces, texts):
    sm = 160.0 / max(L.shape)
    Ls = cv2.resize(L, (max(8, int(L.shape[1] * sm)), max(8, int(L.shape[0] * sm))), interpolation=cv2.INTER_AREA)
    mu = cv2.blur(Ls, (7, 7))
    c = np.sqrt(np.maximum(cv2.blur(Ls * Ls, (7, 7)) - mu * mu, 0))
    c = c / (c.max() + 1e-6)
    s = cv2.resize(sal68, (Ls.shape[1], Ls.shape[0]), interpolation=cv2.INTER_CUBIC)
    s = np.maximum(s, 0)
    s = s / (s.sum() + 1e-12)
    W = c * (s + 0.1 * s.mean() + 1e-9)
    hh, ww = W.shape
    for f in faces:
        b = f["bbox"]
        W[int(b["y"] * hh):int((b["y"] + b["h"]) * hh) + 1, int(b["x"] * ww):int((b["x"] + b["w"]) * ww) + 1] *= 2.0
    for t in texts:
        b = t["bbox"]
        W[int(b["y"] * hh):int((b["y"] + b["h"]) * hh) + 1, int(b["x"] * ww):int((b["x"] + b["w"]) * ww) + 1] *= 1.5
    tot = W.sum()
    if tot <= 0:
        return None
    ys, xs = np.mgrid[0:hh, 0:ww]
    cx, cy = float((xs + 0.5).__mul__(W).sum() / tot / ww), float((ys + 0.5).__mul__(W).sum() / tot / hh)
    left, right = W[:, : ww // 2].sum(), W[:, ww - ww // 2:].sum()
    top, bot = W[: hh // 2].sum(), W[hh - hh // 2:].sum()
    return {"center_of_mass": {"x": r(cx), "y": r(cy)}, "dcm": r(math.hypot(cx - 0.5, cy - 0.5)),
            "lr_offset": r(cx - 0.5), "tb_offset": r(cy - 0.5),           # + = right-heavy / bottom-heavy
            "lr_halves": r((right - left) / tot), "tb_halves": r((bot - top) / tot),
            "cell": cell_of(cx, cy)}


# ----------------------------------------------------------------------------- CVD
CVD = {
    "protanopia": np.array([[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]]),
    "deuteranopia": np.array([[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]]),
}


def cvd_sim(bgr, mat):
    rgb = bgr[..., ::-1].astype(np.float64) / 255.0
    lin = srgb_to_lin(rgb)
    sim = np.clip(lin @ mat.T, 0, 1)
    enc = np.where(sim <= 0.0031308, sim * 12.92, 1.055 * np.power(sim, 1 / 2.4) - 0.055)
    return (np.clip(enc, 0, 1)[..., ::-1] * 255).astype(np.uint8)


# ----------------------------------------------------------------------------- drawing (PIL)
def load_font(size):
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def to_pil(bgr):
    return Image.fromarray(bgr[..., ::-1].copy())


def from_pil(im):
    return np.asarray(im.convert("RGB"))[..., ::-1].copy()


def draw_grid(bgr, cols=4, rows=4):
    """Same look as elevate/frame_prep.py draw_grid: white+black lines, labels A1..D4 in cell corners."""
    im = to_pil(bgr)
    d = ImageDraw.Draw(im)
    w, h = im.size
    lw = max(1, round(min(w, h) / 540))
    font = load_font(max(12, round(min(w, h) / 36)))
    for c in range(1, cols):
        x = round(c * w / cols)
        d.line([(x, 0), (x, h)], fill=(255, 255, 255), width=lw + 2)
        d.line([(x, 0), (x, h)], fill=(0, 0, 0), width=lw)
    for rr in range(1, rows):
        y = round(rr * h / rows)
        d.line([(0, y), (w, y)], fill=(255, 255, 255), width=lw + 2)
        d.line([(0, y), (w, y)], fill=(0, 0, 0), width=lw)
    for c in range(cols):
        for rr in range(rows):
            d.text((round(c * w / cols) + 3 * lw + 4, round(rr * h / rows) + 3 * lw + 2), "%s%d" % (chr(65 + c), rr + 1),
                   font=font, fill=(255, 255, 255), stroke_width=max(2, lw + 1), stroke_fill=(0, 0, 0))
    return from_pil(im)


def draw_safe(bgr, rects, fmt):
    h, w = bgr.shape[:2]
    out = bgr.copy()
    shade = out.copy()
    g = rects["graphics"]
    gx0, gy0, gx1, gy1 = int(g[0] * w), int(g[1] * h), int(g[2] * w), int(g[3] * h)
    mask = np.ones((h, w), bool)
    mask[gy0:gy1, gx0:gx1] = False
    shade[mask] = (shade[mask] * 0.35 + np.array([0, 0, 160]) * 0.65).astype(np.uint8)
    if rects["band"]:
        b = rects["band"]
        by0 = int(b[1] * h)
        shade[by0:, :] = (shade[by0:, :] * 0.5 + np.array([0, 140, 255]) * 0.5).astype(np.uint8)
    out = shade
    lw = max(2, min(w, h) // 300)
    a = rects["action"]
    cv2.rectangle(out, (int(a[0] * w), int(a[1] * h)), (int(a[2] * w) - 1, int(a[3] * h) - 1), (0, 255, 255), lw)
    cv2.rectangle(out, (gx0, gy0), (gx1 - 1, gy1 - 1), (0, 255, 0), lw)
    im = to_pil(out)
    d = ImageDraw.Draw(im)
    font = load_font(max(12, min(w, h) // 40))
    d.text((gx0 + 6, gy0 + 4), "graphics safe" if fmt != "9:16" else "9:16 safe box", font=font, fill=(0, 255, 0),
           stroke_width=2, stroke_fill=(0, 0, 0))
    if fmt != "9:16":
        d.text((int(a[0] * w) + 6, int(a[1] * h) + 4 + 2 * font.size if hasattr(font, "size") else 24), "action safe",
               font=font, fill=(0, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))
    if rects["band"]:
        d.text((gx0 + 6, int(rects["band"][1] * h) + 4), "caption/UI band", font=font, fill=(255, 255, 255),
               stroke_width=2, stroke_fill=(0, 0, 0))
    return from_pil(im)


def draw_saliency(bgr, att, peaks_xy):
    h, w = bgr.shape[:2]
    g = np.array(att["values"], np.float32).reshape(att["height"], att["width"])
    g = g / (g.max() + 1e-9)
    g = cv2.resize(g, (w, h), interpolation=cv2.INTER_CUBIC)
    heat = cv2.applyColorMap((np.clip(g, 0, 1) * 255).astype(np.uint8), cv2.COLORMAP_JET)
    a = (np.clip(g, 0, 1) * 0.65)[..., None]
    out = (bgr * (1 - a) + heat * a).astype(np.uint8)
    rad = max(8, min(w, h) // 40)
    for i, p in enumerate(peaks_xy):
        c = (int(p["x"] * w), int(p["y"] * h))
        cv2.circle(out, c, rad, (255, 255, 255), max(2, rad // 5))
        cv2.putText(out, str(i + 1), (c[0] - rad // 3, c[1] + rad // 3), cv2.FONT_HERSHEY_SIMPLEX, rad / 22.0,
                    (255, 255, 255), max(2, rad // 8), cv2.LINE_AA)
    return out


def draw_lines(bgr, segs):
    h, w = bgr.shape[:2]
    out = (bgr * 0.45).astype(np.uint8)
    st = line_stats(segs, w)
    if st is None:
        return out
    length, ang, keep = st
    lw = max(1, w // 700)
    for (x1, y1, x2, y2), a, k in zip(segs, ang, keep):
        if not k:
            continue
        col = (80, 220, 80) if abs(a) <= 10 else ((255, 160, 40) if abs(a) >= 80 else (40, 160, 255))
        cv2.line(out, (int(x1), int(y1)), (int(x2), int(y2)), col, lw, cv2.LINE_AA)
    return out


def label_tile(img, text, cell_w, cell_h, font):
    """Fit img (BGR) in a cell_w x cell_h area under a label strip."""
    h, w = img.shape[:2]
    s = min(cell_w / float(w), (cell_h - font.size - 6 if hasattr(font, "size") else cell_h - 24) / float(h))
    tw, th = max(1, int(w * s)), max(1, int(h * s))
    small = cv2.resize(img, (tw, th), interpolation=cv2.INTER_AREA)
    tile = Image.new("RGB", (cell_w, cell_h), (24, 24, 24))
    tile.paste(to_pil(small), ((cell_w - tw) // 2, cell_h - th))
    d = ImageDraw.Draw(tile)
    d.text((6, 2), text, font=font, fill=(240, 240, 240))
    return tile


def make_board(tiles, aspect, path):
    """tiles = [(label, bgr)]. Picks the column count that makes tiles largest while height <= BOARD_EDGE."""
    pad = 6
    n = len(tiles)
    best = None
    for cols in range(2, 9):
        cw = (BOARD_EDGE - pad * (cols + 1)) // cols
        rows = int(math.ceil(n / float(cols)))
        fs = max(14, cw // 26)
        ch = int(cw / aspect) + fs + 10
        H = rows * (ch + pad) + pad
        W = cols * (cw + pad) + pad
        if H <= BOARD_EDGE and W <= BOARD_EDGE and (best is None or cw > best[1]):
            best = (cols, cw, ch, H, W, fs)
    if best is None:                       # extreme aspect: shrink
        cols = 6
        cw = (BOARD_EDGE - pad * 7) // cols
        rows = int(math.ceil(n / float(cols)))
        fs = max(12, cw // 26)
        ch = (BOARD_EDGE - pad * (rows + 1)) // rows
        best = (cols, cw, ch, BOARD_EDGE, BOARD_EDGE, fs)
    cols, cw, ch, H, W, fs = best
    font = load_font(fs)
    sheet = Image.new("RGB", (W, H), (12, 12, 12))
    for i, (label, img) in enumerate(tiles):
        cx, cy = i % cols, i // cols
        sheet.paste(label_tile(img, label, cw, ch, font), (pad + cx * (cw + pad), pad + cy * (ch + pad)))
    sheet.save(path, quality=88)
    return sheet.size


# ----------------------------------------------------------------------------- analysis
def pick_subject(vis, att_peaks, shape, mask_dir):
    """Choose the subject: foreground instance holding the top attention peak (else largest);
    fall back to the largest face box. Returns dict or None."""
    h, w = shape
    fg = (vis or {}).get("foreground")
    if fg and fg.get("instances"):
        best, best_score = None, -1
        top = att_peaks[0] if att_peaks else None
        for inst in fg["instances"]:
            png = inst.get("mask_png")
            if not png or not os.path.exists(png):
                continue
            m = cv2.imread(png, cv2.IMREAD_GRAYSCALE)
            if m is None:
                continue
            m = cv2.resize(m, (w, h), interpolation=cv2.INTER_NEAREST) > 127
            score = inst["area_share"]
            if top is not None and m[min(h - 1, int(top["y"] * h)), min(w - 1, int(top["x"] * w))]:
                score += 10
            if score > best_score:
                best, best_score = (inst, m), score
        if best:
            inst, m = best
            a = inst["area_share"]
            return {"mask": m, "source": "foreground-instance", "bbox": [inst["bbox"][k] for k in ("x", "y", "w", "h")],
                    "centroid": (inst["centroid"]["x"], inst["centroid"]["y"]), "area_share": a,
                    "confidence": 0.7 if 0.01 <= a <= 0.75 else 0.4,
                    "n_instances": fg["count"]}
    faces = (vis or {}).get("faces") or []
    if faces:
        f = max(faces, key=lambda f: f["bbox"]["w"] * f["bbox"]["h"])
        b = f["bbox"]
        m = np.zeros((h, w), bool)
        m[int(b["y"] * h):int((b["y"] + b["h"]) * h), int(b["x"] * w):int((b["x"] + b["w"]) * w)] = True
        return {"mask": m, "source": "face-box (no foreground mask)", "bbox": [b["x"], b["y"], b["w"], b["h"]],
                "centroid": (b["x"] + b["w"] / 2, b["y"] + b["h"] / 2), "area_share": b["w"] * b["h"],
                "confidence": 0.4, "n_instances": 0}
    return None


def analyse(bgr, vis, fmt, mask_dir, workdir, timings, vision_ok, vlog):
    """Compute every metric. Returns (report dict, intermediates for drawing)."""
    h, w = bgr.shape[:2]
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    Lab = to_lab(bgr)
    L = Lab[..., 0]
    rep = {}
    nov = lambda: null_metric(NO_VISION)   # noqa: E731

    # --- saliency source
    t0 = time.time()
    if vis and vis.get("attention"):
        att = vis["attention"]
        att_basis = "apple-vision"
    else:
        att = approx_attention(gray)
        att_basis = "spectral-residual approximation (no-vision)"
    sal68 = np.array(att["values"], np.float32).reshape(att["height"], att["width"])
    peaks = att["peaks"]
    timings["saliency_fallback_s"] = r(time.time() - t0, 2) if att_basis.startswith("spectral") else 0

    subject = pick_subject(vis, peaks, (h, w), mask_dir) if vis else None
    mask = subject["mask"] if subject else None

    # --- tone, notan
    rep["tone"] = tone_metrics(L)
    idx3, n3 = notan(L, 3)
    idx4, n4 = notan(L, 4)
    rep["notan_k3"], rep["notan_k4"] = n3, n4

    # --- subject
    if subject:
        bx = subject["bbox"]
        rep["subject"] = metric({"source": subject["source"], "bbox": {"x": bx[0], "y": bx[1], "w": bx[2], "h": bx[3]},
                                 "area_share": r(subject["area_share"]), "n_foreground_instances": subject["n_instances"],
                                 "centroid": {"x": r(subject["centroid"][0]), "y": r(subject["centroid"][1]),
                                              "cell": cell_of(*subject["centroid"])}},
                                confidence=subject["confidence"],
                                confidence_basis="heuristic: Vision gives no mask score; lowered when the mask is under 1% or over 75% of the frame")
        d = subject_dL(Lab, mask)
        rep["subject_delta_L"] = metric(d, 0.8 * subject["confidence"] / 0.7) if d else null_metric("mask or ring too small")
    else:
        reason = NO_VISION if not vision_ok else "no foreground instance and no face found"
        rep["subject"] = null_metric(reason)
        rep["subject_delta_L"] = null_metric(reason)

    # --- saliency peak ratio, capture
    if float(np.std(L)) < 1.0:
        # measured: Apple's attention map on a flat frame still shows a centre blob (peak ~0.41 at the middle)
        peaks = []
        rep["saliency"] = null_metric("frame has no tonal variation (L* std < 1); any heatmap peak would be the model's centre bias")
    elif len(peaks) >= 1:
        p1 = peaks[0]["raw"]
        p2 = peaks[1]["raw"] if len(peaks) > 1 else 0.0
        ratio = p1 / p2 if p2 > 1e-6 else 99.0
        pk = [{"x": p["x"], "y": p["y"], "strength": p["strength"], "cell": cell_of(p["x"], p["y"])} for p in peaks]
        rep["saliency"] = metric({"basis": att_basis, "peaks": pk, "peak_ratio_p1_p2": r(min(ratio, 99.0), 2),
                                  "single_dominant_peak": bool(ratio > 1.5),                      # [Infer] target > 1.5
                                  "centre_bias_note": "Apple attention has a centre prior; a peak near (0.5,0.4) on a low-contrast frame may be that prior"},
                                 confidence=0.7 if att_basis == "apple-vision" else 0.35,
                                 confidence_basis="Apple attention heatmap peaks" if att_basis == "apple-vision"
                                 else "approximation; treat as a rough guide")
    else:
        rep["saliency"] = null_metric("saliency heatmap is empty (flat or uniform frame)")
    cap = mass_in_mask(sal68, mask)
    rep["subject_capture"] = (metric({"share": r(cap), "meets_0_4": bool(cap >= 0.4)}, 0.6 if att_basis == "apple-vision" else 0.3)
                              if cap is not None else null_metric(NO_VISION if not vision_ok else "no subject mask"))
    obj = (vis or {}).get("objectness")
    rep["objectness"] = (metric({"peaks": obj["peaks"]}, 0.5) if obj and obj.get("peaks")
                         else null_metric(NO_VISION if not vision_ok else "objectness saliency found nothing"))
    if vis and vis.get("aesthetics"):
        rep["aesthetics"] = metric({"overall_score": vis["aesthetics"]["overall_score"],
                                    "is_utility": vis["aesthetics"]["is_utility"]}, 0.5)
    else:
        rep["aesthetics"] = null_metric(NO_VISION if not vision_ok else "needs macOS 15 CalculateImageAestheticsScoresRequest")

    # --- framing
    if subject:
        ed = edge_distances(mask)
        rep["edge_distance"] = metric(ed, subject["confidence"])
        rep["tangent"] = metric({"flag": ed["tangent_flag"], "sides": ed["tangent_sides"],
                                 "touches_edge_sides": ed["touches_edge_sides"]}, subject["confidence"])
        # facing
        faces = vis.get("faces") or []
        poses = vis.get("pose") or []
        fd, src = None, None
        inside = lambda p: mask[min(h - 1, int(p[1] * h)), min(w - 1, int(p[0] * w))]   # noqa: E731
        fcand = [f for f in faces if f.get("nose") and inside((f["nose"]["x"], f["nose"]["y"]))] or faces
        if fcand:
            f = max(fcand, key=lambda f: f["bbox"]["w"] * f["bbox"]["h"])
            fd = facing_from_face(f)
            src = "face landmarks (nose vs eye midpoint)"
        if fd is None and poses:
            pcand = [p for p in poses if p["joints"].get("nose_joint") and inside((p["joints"]["nose_joint"]["x"], p["joints"]["nose_joint"]["y"]))] or poses
            fd = facing_from_pose(pcand[0])
            src = "body pose (nose vs ears)"
        rep["facing"] = facing_metrics(subject["bbox"], subject["centroid"], fd, src)
        if not fd and not faces and not poses:
            rep["facing"] = null_metric("no face or pose found; facing needs a face, pose or manual input")
    else:
        for k in ("edge_distance", "tangent", "facing"):
            rep[k] = null_metric(NO_VISION if not vision_ok else "no subject")

    # --- joint crop
    if vis and vis.get("pose"):
        hits = []
        for p in vis["pose"]:
            hits += joint_crop(p)
        rep["joint_crop"] = metric({"flag": bool(hits), "joints": hits}, float(max(p["confidence"] for p in vis["pose"])))
    else:
        rep["joint_crop"] = null_metric(NO_VISION if not vision_ok else "no body pose found")

    # --- lines and horizon
    t0 = time.time()
    segs = detect_lines(gray)
    timings["lines_s"] = r(time.time() - t0, 2)
    lh = line_horizon(segs, w)
    rep["line_orientation"] = (metric(orientation_shares(segs, w), 0.6) if orientation_shares(segs, w)
                               else null_metric("no long line segments found"))
    apple = (vis or {}).get("horizon")
    apple_deg = apple["angle_deg"] if apple else None
    if apple_deg is not None and lh is not None and abs(apple_deg + lh["angle_deg"]) < abs(apple_deg - lh["angle_deg"]) - 1e-9:
        apple_deg = -apple_deg                      # normalise Apple's sign to ours (positive = clockwise)
    chosen = apple_deg if apple_deg is not None else (lh["angle_deg"] if lh else None)
    if chosen is None:
        rep["horizon"] = null_metric(("no horizon or long near-horizontal lines found" if vision_ok else NO_VISION + ": no long near-horizontal lines found"))
    else:
        agree = (abs(apple_deg - lh["angle_deg"]) <= 1.0) if (apple_deg is not None and lh) else None
        conf = 0.75 if agree else (0.5 if apple_deg is not None or lh else 0.3)
        rep["horizon"] = metric({"tilt_deg": r(chosen, 2), "apple_deg": r(apple_deg, 2) if apple_deg is not None else None,
                                 "lines_deg": lh["angle_deg"] if lh else None, "lines_n": lh["n_lines"] if lh else 0,
                                 "cross_check_agrees": agree, "source": "apple" if apple_deg is not None else "lines",
                                 "accidental_tilt_flag": bool(0.5 <= abs(chosen) <= 3.0 and agree is not False),   # [Infer]
                                 "note": "Apple and line detector disagree; tilt unconfirmed, no flag" if agree is False else None},
                                conf)

    # --- palette
    samp = subsample(Lab)
    k = 6
    lab_lab, centers = kmeans(samp, k)
    d2 = ((Lab.reshape(-1, 1, 3)[:: max(1, (h * w) // 80000)] - centers.reshape(1, k, 3)) ** 2).sum(-1)
    assign = np.argmin(d2, axis=1)
    shares = np.bincount(assign, minlength=k) / float(len(assign))
    pal = []
    for i in np.argsort(-shares):
        L_, a_, b_ = centers[i]
        rgb = cv2.cvtColor(np.array([[[L_, a_, b_]]], np.float32), cv2.COLOR_Lab2RGB)[0, 0]
        pal.append({"hex": "#%02x%02x%02x" % tuple(int(round(np.clip(c, 0, 1) * 255)) for c in rgb),
                    "L": r(L_, 1), "a": r(a_, 1), "b": r(b_, 1), "chroma": r(math.hypot(a_, b_), 1), "share": r(shares[i])})
    big_hc = [p for p in pal if p["chroma"] >= 40 and p["share"] >= 0.08]   # [Infer]
    rep["palette"] = {"k": k, "clusters": pal, "large_high_chroma_count": len(big_hc),
                      "review_flag": bool(len(big_hc) > 2), "confidence": 1.0, "confidence_basis": "pixel measurement"}

    # --- text
    texts = (vis or {}).get("text") or []
    rects = safe_rects(fmt)
    rep["safe_area"] = {"format": fmt, "graphics": [r(v) for v in rects["graphics"]], "action": [r(v) for v in rects["action"]],
                        "note": rects["note"]}
    if not vision_ok:
        rep["text"] = nov()
        rep["text_outside_graphics_safe"] = nov()
    elif not texts:
        rep["text"] = null_metric("Vision found no text")
        rep["text_outside_graphics_safe"] = null_metric("Vision found no text")
    else:
        items, outside = [], []
        for t in sorted(texts, key=lambda t: -t["bbox"]["w"] * t["bbox"]["h"])[:40]:
            tc = text_contrast(bgr, t["bbox"])
            ins = box_inside(t["bbox"], rects["graphics"])
            item = {"text": t["text"], "bbox": t["bbox"], "cell": cell_of(t["bbox"]["x"] + t["bbox"]["w"] / 2, t["bbox"]["y"] + t["bbox"]["h"] / 2),
                    "ocr_confidence": t["confidence"], "inside_graphics_safe": ins}
            item.update(tc if tc else {"contrast_worst": None, "contrast_reason": "text and background not separable in box"})
            items.append(item)
            if not ins:
                outside.append(t["text"])
        rep["text"] = metric({"boxes": items}, float(np.mean([t["confidence"] for t in texts])))
        rep["text_outside_graphics_safe"] = metric({"flag": bool(outside), "strings": outside},
                                                   float(np.mean([t["confidence"] for t in texts])))

    # --- balance
    bal = balance(L, sal68, (vis or {}).get("faces") or [], texts)
    rep["balance"] = (metric(bal, 0.5 if att_basis == "apple-vision" else 0.3,
                             confidence_basis="luminance contrast x saliency; saliency is %s" % att_basis)
                      if bal else null_metric("weight map empty"))

    # --- edge density per grid cell
    edges = cv2.Canny(cv2.GaussianBlur(gray, (0, 0), 1.2), 50, 150) > 0
    dens = {}
    for rr in range(4):
        for cc in range(4):
            sub = edges[rr * h // 4:(rr + 1) * h // 4, cc * w // 4:(cc + 1) * w // 4]
            dens["%s%d" % (chr(65 + cc), rr + 1)] = r(sub.mean())
    hot = max(dens, key=dens.get)
    rep["edge_density"] = {"cells": dens, "overall": r(edges.mean()), "busiest_cell": hot, "quietest_cell": min(dens, key=dens.get),
                           "confidence": 1.0, "confidence_basis": "pixel measurement"}

    inter = dict(gray=gray, Lab=Lab, L=L, idx3=idx3, idx4=idx4, segs=segs, att=att, peaks=peaks, subject=subject,
                 sal68=sal68, att_basis=att_basis, texts=texts)
    return rep, inter


def thumbnail_survival(bgr, rep, inter, vis_on, tmpdir, vlog):
    """Shrink to 10% (blurred slightly), recompute saliency, and see whether the top peak stays on the subject."""
    h, w = bgr.shape[:2]
    s = max(0.1, 48.0 / max(h, w))
    small = cv2.resize(bgr, (max(8, int(w * s)), max(8, int(h * s))), interpolation=cv2.INTER_AREA)
    small = cv2.GaussianBlur(small, (0, 0), 0.8)
    pk = None
    basis = "spectral-residual approximation (no-vision)"
    if vis_on:
        # Vision needs more than ~10 px: upscale the 10% thumbnail back to the working size, as a viewer sees it
        up = cv2.resize(small, (w, h), interpolation=cv2.INTER_LINEAR)
        p = os.path.join(tmpdir, "thumb_up.png")
        cv2.imwrite(p, up)
        v = run_vision(p, None, vlog, saliency_only=True)
        if v and v.get("attention") and v["attention"].get("peaks"):
            pk, basis = v["attention"]["peaks"], "apple-vision"
    if pk is None:
        up = cv2.resize(small, (w, h), interpolation=cv2.INTER_LINEAR)
        g = spectral_residual(cv2.cvtColor(up, cv2.COLOR_BGR2GRAY))
        pk = grid_peaks(g)
    if not pk:
        return null_metric("no saliency peak at 10%"), None
    full = inter["peaks"][0] if inter["peaks"] else None
    dist = math.hypot(pk[0]["x"] - full["x"], pk[0]["y"] - full["y"]) if full else None
    mask = inter["subject"]["mask"] if inter["subject"] else None
    on_subject = None
    if mask is not None:
        on_subject = bool(mask[min(h - 1, int(pk[0]["y"] * h)), min(w - 1, int(pk[0]["x"] * w))])
    res = {"basis": basis, "thumb_peak": {"x": pk[0]["x"], "y": pk[0]["y"], "cell": cell_of(pk[0]["x"], pk[0]["y"])},
           "distance_from_full_res_peak": r(dist) if dist is not None else None,
           "peak_stays_put": bool(dist is not None and dist < 0.15),
           "peak_on_subject": on_subject,
           "survives": (on_subject if on_subject is not None else bool(dist is not None and dist < 0.15))}
    if mask is None:
        res["note"] = "no subject mask; survival judged by the peak not moving more than 0.15"
    return metric(res, 0.6 if basis == "apple-vision" else 0.3), small


def format_survival(rep, inter, shape, vis_on):
    h, w = shape
    subj = inter["subject"]
    if subj:
        cx, cy = subj["centroid"][0] * w, subj["centroid"][1] * h
        anchor = "subject centroid"
    elif inter["peaks"]:
        cx, cy = inter["peaks"][0]["x"] * w, inter["peaks"][0]["y"] * h
        anchor = "top saliency peak"
    else:
        cx, cy, anchor = w / 2, h / 2, "frame centre"
    out, crops = {}, {}
    for fmt in FORMATS:
        x0, y0, x1, y1 = crop_for(fmt, w, h, cx, cy)
        crops[fmt] = (x0, y0, x1, y1)
        e = {"crop_px": [x0, y0, x1, y1]}
        if subj:
            m = subj["mask"]
            tot = m.sum()
            e["subject_share_inside"] = r(m[y0:y1, x0:x1].sum() / float(tot)) if tot else None
        else:
            e["subject_share_inside"] = None
        tx = inter["texts"]
        if tx:
            n_in = sum(1 for t in tx if box_inside(t["bbox"], (x0 / w, y0 / h, x1 / w, y1 / h)))
            e["text_boxes_inside"] = "%d/%d" % (n_in, len(tx))
        else:
            e["text_boxes_inside"] = None
        out[fmt] = e
    reason = None if subj else ("subject mask unavailable (%s)" % (NO_VISION if not vis_on else "none found"))
    m = metric({"anchor": anchor, "formats": out}, 0.6 if subj else 0.3, confidence_basis="share of subject mask pixels kept by a centred crop")
    if reason:
        m["subject_note"] = reason
    return m, crops


def save(path, img, quality=88):
    cv2.imwrite(path, img, [cv2.IMWRITE_JPEG_QUALITY, quality])


def run(image, fmt_arg="auto", out_dir=None, no_vision=False):
    t_all = time.time()
    timings = {}
    bgr0 = cv2.imread(image, cv2.IMREAD_COLOR)           # applies EXIF orientation
    if bgr0 is None:
        sys.stderr.write("look.py: cannot read image %s\n" % image)
        return 2
    H0, W0 = bgr0.shape[:2]
    s = min(1.0, WORK_EDGE / float(max(H0, W0)))
    bgr = cv2.resize(bgr0, (max(1, int(round(W0 * s))), max(1, int(round(H0 * s)))), interpolation=cv2.INTER_AREA) if s < 1 else bgr0
    h, w = bgr.shape[:2]
    name = os.path.splitext(os.path.basename(image))[0]
    out_dir = out_dir or os.path.join("look_out", name)
    vdir = os.path.join(out_dir, "views")
    os.makedirs(vdir, exist_ok=True)
    fmt = pick_format(fmt_arg, w, h)

    vlog = []
    vis = None
    vision_reason = None
    tmp = tempfile.mkdtemp(prefix="look_")
    if no_vision:
        vision_reason = "--no-vision"
    else:
        t0 = time.time()
        wp = os.path.join(tmp, "work.png")
        cv2.imwrite(wp, bgr)
        mask_dir = os.path.join(out_dir, "vision_masks")
        vis = run_vision(wp, mask_dir, vlog)
        timings["vision_s"] = r(time.time() - t0, 2)
        if vis is not None and not vis.get("attention") and vis.get("notes"):
            # The binary ran but its models did not load (seen inside Claude Code's Bash sandbox:
            # "espresso error", "ANE model"). Treat as no Vision so nothing downstream trusts it.
            vlog.append("Apple Vision models did not load (sandboxed shell?): %s" % vis["notes"][0][:160])
            vis = None
        if vis is None:
            vision_reason = "; ".join(vlog) or "vision failed"
    vision_ok = vis is not None
    if vis:
        with open(os.path.join(out_dir, "vision.json"), "w") as fh:
            json.dump(vis, fh)

    t0 = time.time()
    rep, inter = analyse(bgr, vis, fmt, None, tmp, timings, vision_ok, vlog)
    timings["metrics_s"] = r(time.time() - t0, 2)

    t0 = time.time()
    rep["thumbnail_survival"], thumb_small = thumbnail_survival(bgr, rep, inter, vision_ok, tmp, vlog)
    timings["thumbnail_s"] = r(time.time() - t0, 2)
    rep["format_survival"], crops = format_survival(rep, inter, (h, w), vision_ok)

    # --- views
    t0 = time.time()
    views = {}
    gray3 = cv2.cvtColor(inter["gray"], cv2.COLOR_GRAY2BGR)
    views["grayscale"] = gray3
    views["notan_k3"] = cv2.cvtColor(notan_image(inter["idx3"], 3), cv2.COLOR_GRAY2BGR)
    views["notan_k4"] = cv2.cvtColor(notan_image(inter["idx4"], 4), cv2.COLOR_GRAY2BGR)
    views["thumb10_upscaled"] = cv2.resize(thumb_small if thumb_small is not None else bgr, (w, h), interpolation=cv2.INTER_NEAREST)
    views["blur"] = cv2.GaussianBlur(bgr, (0, 0), max(2.0, max(h, w) * 0.012))
    views["saliency"] = draw_saliency(bgr, inter["att"], inter["peaks"])
    views["lines"] = draw_lines(bgr, inter["segs"])
    views["grid"] = draw_grid(bgr)
    views["safe_area"] = draw_safe(bgr, safe_rects(fmt), fmt)
    for f, (x0, y0, x1, y1) in crops.items():
        views["crop_" + f.replace(":", "x")] = bgr[y0:y1, x0:x1]
    for nm, mat in CVD.items():
        views["cvd_" + nm] = cvd_sim(bgr, mat)
    files = {}
    for k, v in views.items():
        p = os.path.join(vdir, k + ".jpg")
        save(p, v)
        files[k] = p
    timings["views_s"] = r(time.time() - t0, 2)

    # --- board
    t0 = time.time()
    order = [("original", bgr), ("grid A-D x 1-4", views["grid"]), ("saliency (peaks 1-3)", views["saliency"]),
             ("grayscale", views["grayscale"]), ("notan k=3", views["notan_k3"]), ("notan k=4", views["notan_k4"]),
             ("10% thumbnail", views["thumb10_upscaled"]), ("blur", views["blur"]), ("lines", views["lines"]),
             ("safe area " + fmt, views["safe_area"]), ("deuteranopia", views["cvd_deuteranopia"]),
             ("protanopia", views["cvd_protanopia"])]
    for f in FORMATS:
        order.append(("crop " + f, views["crop_" + f.replace(":", "x")]))
    bpath = os.path.join(out_dir, "board.jpg")
    bsize = make_board(order, w / float(h), bpath)
    timings["board_s"] = r(time.time() - t0, 2)

    timings["total_s"] = r(time.time() - t_all, 2)
    report = {
        "tool": "composition look.py", "version": "1.0", "image": os.path.abspath(image),
        "size_original": [W0, H0], "size_analysed": [w, h], "format": fmt,
        "grid": {"cols": 4, "rows": 4, "labels": "A1..D4", "columns": "A-D left to right", "rows_order": "1-4 top to bottom"},
        "vision": bool(vision_ok), "vision_reason_off": vision_reason,
        "vision_notes": (vis or {}).get("notes", []),
        "metrics": rep, "files": {"board": bpath, "views": files}, "board_size": list(bsize), "timings": timings,
        "thresholds_note": "Thresholds marked [Infer] in metric-recipes.md are starting points to calibrate.",
    }
    with open(os.path.join(out_dir, "report.json"), "w") as fh:
        json.dump(report, fh, indent=1)
    try:
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)
    except Exception:
        pass
    print("look: %s  vision=%s  total %.1fs  -> %s" % (name, vision_ok, timings["total_s"], out_dir))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Measure a frame; write views, board.jpg and report.json.")
    ap.add_argument("image")
    ap.add_argument("--format", default="auto", choices=["auto", "16:9", "9:16", "1:1", "4:5"])
    ap.add_argument("--out", default=None, help="output folder")
    ap.add_argument("--no-vision", action="store_true", help="skip Apple Vision (OpenCV-only fallback)")
    a = ap.parse_args(argv)
    return run(a.image, a.format, a.out, a.no_vision)


if __name__ == "__main__":
    sys.exit(main())
