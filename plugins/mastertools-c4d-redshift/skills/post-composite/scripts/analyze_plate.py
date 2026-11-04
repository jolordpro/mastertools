#!/usr/bin/env python3
"""analyze_plate.py: measure a live-action plate for CG integration.

Usage:
    python3 analyze_plate.py PLATE [--out DIR] [--max-frames 240] [--start SEC] [--dur SEC]

Writes into DIR (default: ./plate_analysis_<name>/):
    plate_analysis.json   every measurement, with method, confidence and the threshold used
    contact_sheet.jpg     9 frames across the shot, frame numbers burned in
    overlay.jpg           clean frame with VP/lines, clipped areas, practicals, streaks,
                          dark panels, subject track, CA tiles and distortion lines drawn on
    maps.jpg              motion coverage, sharpness heat map, haze curve, bloom curves
and prints a compact summary to stdout.

Needs ffmpeg/ffprobe on PATH and Python 3 with numpy + opencv-python.
Designed for display-referred plates (Rec.709 / sRGB / Rec.2020 video, ProRes, H.264/5,
DNx, integer image sequences). Scene-linear EXR plates are out of scope for the
energy numbers (they would need no transfer-function decode).

Every threshold lives in TH below. Values tagged [rule] are starting points that were
calibrated on two real plates (2026-10-23: a ProRes 422 HQ 1080p hallway and an
H.264 UHD low-key hallway) plus the synthetic self-test (selftest.py); tune them per show.
"""
import argparse, json, math, os, re, subprocess, sys, time
import numpy as np
import cv2

VERSION = "1.0.0 (2026-10-23)"

TH = {
    # camera
    "locked_px": 0.25,          # [rule] max drift below this = locked
    "drift2d_max_px": 4.0,      # [rule] up to this with no parallax = 2D planar drift
    "parallax_px": 0.5,         # [rule] homography residual p90 above this (with motion) = parallax
    # clipping / practicals
    "clip_band": 0.008,         # on the temporal-median frame, a pixel within this of the clip ceiling counts as clipped
    "clip_plateau_frac": 2e-5,  # pixels in the ceiling hump (+-6 thousandths) needed to call it a clip (~40 px at 1080p)
    "clip_prominence": 1.5,     # hump height vs the lowest density in the 0.03 below it (a smooth tail has no hump)
    "clip_min_level": 0.85,     # plateau must sit at or above this R'G'B' level
    "practical_min": 0.55,      # practical candidate: max(R'G'B') at least this
    "practical_contrast": 0.10, # and this much brighter than its 25 px neighbourhood
    # gloss
    "streak_aspect": 3.0,       # [rule] length:width to count as a reflection streak
    "streak_min_len": 0.03,     # of frame height
    # haze
    "haze_lift": 0.025,         # [rule] far-minus-near dark level (R'G'B' units) to call haze
    # DOF
    "far_soft_ratio": 0.80,     # [rule] far/near sharpness below this = far region soft
    # CA
    "ca_px": 0.5,               # [rule] lateral CA at the corner, native px
    # distortion
    "distortion_px": 0.75,      # [rule] bow of a full-height vertical at the frame edge implied by the fitted k1 (native px)
    # flicker
    "flicker_pct": 1.0,         # [rule] frame-to-frame wobble (std around a 7-frame average) above this % = flicker
}

ANALYSIS_W = 1920   # geometry, motion and maps run at <= this width; grain and CA at native


# ---------------------------------------------------------------- probe / decode
def probe(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-print_format", "json",
                                   "-show_streams", "-show_format", path])
    j = json.loads(out)
    v = next(s for s in j["streams"] if s.get("codec_type") == "video")
    pf = v.get("pix_fmt", "")
    m = re.search(r"(\d+)(le|be)$", pf)
    bd = int(m.group(1)) if m else int(v.get("bits_per_raw_sample") or 8)
    if pf.startswith(("rgb48", "bgr48", "rgba64", "bgra64")):
        bd = 16
    is_rgb = pf.startswith(("rgb", "bgr", "gbr", "argb", "abgr", "rgba", "bgra"))
    num, den = (v.get("r_frame_rate") or "0/1").split("/")
    fps = float(num) / float(den) if float(den) else 0.0
    dur = float(v.get("duration") or j["format"].get("duration") or 0)
    nb = int(v["nb_frames"]) if str(v.get("nb_frames", "")).isdigit() else int(round(dur * fps))
    chroma = "4:4:4" if ("444" in pf or is_rgb) else "4:2:2" if "422" in pf else "4:2:0" if "420" in pf else "?"
    tags = {k: v.get(k, "unknown") for k in ("color_primaries", "color_transfer", "color_space", "color_range")}
    tc = None
    for s in j["streams"]:
        tc = tc or (s.get("tags") or {}).get("timecode")
    tc = tc or (j["format"].get("tags") or {}).get("timecode")
    return {
        "path": os.path.abspath(path), "codec": v.get("codec_name"), "profile": v.get("profile"),
        "width": int(v["width"]), "height": int(v["height"]), "fps": round(fps, 4),
        "r_frame_rate": v.get("r_frame_rate"), "pix_fmt": pf, "bit_depth": bd, "chroma": chroma,
        "is_rgb": is_rgb, "duration_s": round(dur, 4), "frames": nb, "timecode": tc,
        "bit_rate": v.get("bit_rate") or j["format"].get("bit_rate"), **tags,
    }


def matrix_coeffs(space):
    if space in ("bt2020nc", "bt2020c", "bt2020"):
        return 0.2627, 0.0593
    if space in ("smpte170m", "bt470bg", "bt601"):
        return 0.299, 0.114
    return 0.2126, 0.0722   # bt709 and unknown HD


def decode(info, start=None, dur=None):
    """Yield (ycode, rgb) per frame. ycode = luma in source code values (None for RGB
    sources); rgb = float32 R'G'B' normalised so legal black = 0 and legal white = 1
    (super-whites stay above 1)."""
    w, h, bd = info["width"], info["height"], info["bit_depth"]
    pixfmt = "rgb48le" if info["is_rgb"] else "yuv444p16le"
    cmd = ["ffmpeg", "-v", "error", "-nostdin"]
    if start:
        cmd += ["-ss", str(start)]
    cmd += ["-i", info["path"]]
    if dur:
        cmd += ["-t", str(dur)]
    cmd += ["-map", "0:v:0", "-f", "rawvideo", "-pix_fmt", pixfmt,
            "-sws_flags", "accurate_rnd+full_chroma_int+bitexact", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    n = w * h * 3 * 2
    full = info["color_range"] == "pc"
    kr, kb = matrix_coeffs(info["color_space"])
    maxc = (1 << bd) - 1
    s = 2 ** (bd - 8)
    try:
        while True:
            buf = p.stdout.read(n)
            if len(buf) < n:
                break
            a = np.frombuffer(buf, np.uint16)
            if info["is_rgb"]:
                rgb = a.reshape(h, w, 3).astype(np.float32) / 65535.0
                yield None, rgb
                continue
            a = a.reshape(3, h, w).astype(np.float32) * (maxc / 65535.0)
            Y, Cb, Cr = a[0], a[1], a[2]
            if full:
                y, cb, cr = Y / maxc, (Cb - 128 * s) / maxc, (Cr - 128 * s) / maxc
            else:
                y, cb, cr = (Y - 16 * s) / (219 * s), (Cb - 128 * s) / (224 * s), (Cr - 128 * s) / (224 * s)
            r = y + 2 * (1 - kr) * cr
            b = y + 2 * (1 - kb) * cb
            g = (y - kr * r - kb * b) / (1 - kr - kb)
            yield Y, np.dstack([r, g, b]).astype(np.float32)
    finally:
        p.stdout.close()
        p.wait()


def luma(rgb, kr=0.2126, kb=0.0722):
    return kr * rgb[..., 0] + (1 - kr - kb) * rgb[..., 1] + kb * rgb[..., 2]


def to_lin(x):
    """Display-linear (Strategy A, BT.1886 with Lw=1, Lb=0)."""
    return np.power(np.clip(x, 0, None), 2.4)


def hexcol(rgb):
    c = np.clip(np.asarray(rgb, float), 0, 1)
    return "#%02x%02x%02x" % tuple(int(round(v * 255)) for v in c)


def hue_name(rgb):
    hsv = cv2.cvtColor(np.clip(np.float32([[rgb]]), 0, 1), cv2.COLOR_RGB2HSV)[0, 0]
    hdeg, sat = float(hsv[0]), float(hsv[1])
    if sat < 0.10:
        return "neutral", hdeg, sat
    names = [(15, "red"), (45, "orange"), (70, "yellow"), (150, "green"), (200, "cyan/teal"),
             (250, "blue"), (290, "violet"), (335, "magenta"), (360, "red")]
    for lim, nm in names:
        if hdeg < lim:
            return nm, hdeg, sat
    return "red", hdeg, sat


# ---------------------------------------------------------------- camera
LK = dict(winSize=(21, 21), maxLevel=3,
          criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 60, 0.001))


def _track_pair(g0, g1, pts0):
    p1, st, _ = cv2.calcOpticalFlowPyrLK(g0, g1, pts0, None, **LK)
    p0r, st2, _ = cv2.calcOpticalFlowPyrLK(g1, g0, p1, None, **LK)
    fb = np.linalg.norm((pts0 - p0r).reshape(-1, 2), axis=1)
    good = (st.ravel() == 1) & (st2.ravel() == 1) & (fb < 0.25)
    return p1.reshape(-1, 2), good


def _homog_resid(a, b):
    if len(a) < 12:
        return None, None
    H, inl = cv2.findHomography(a, b, cv2.RANSAC, 1.0)
    if H is None:
        return None, None
    pa = cv2.perspectiveTransform(a.reshape(-1, 1, 2), H).reshape(-1, 2)
    r = np.linalg.norm(pa - b, axis=1)
    return H, r


def analyze_camera(stack, scale):
    """stack: list of uint8 grey frames at analysis res. scale: native px per analysis px."""
    n = len(stack)
    h, w = stack[0].shape
    cx, cy = w / 2, h / 2
    pts0 = cv2.goodFeaturesToTrack(stack[0], maxCorners=1000, qualityLevel=0.005,
                                   minDistance=10, blockSize=7)
    res = {"method": "LK optical flow on Shi-Tomasi features vs frame 0 (direct) with forward-backward "
                     "check; RANSAC affine for drift; homography residuals over a k-frame baseline for parallax"}
    if pts0 is None or len(pts0) < 20:
        res.update(classification="unknown", confidence="low", note="too few trackable features")
        return res
    pts0 = pts0.astype(np.float32)
    direct = []
    direct_ok = True
    for t in range(n):
        p1, good = _track_pair(stack[0], stack[t], pts0)
        if good.sum() < max(20, 0.2 * len(pts0)):
            direct_ok = False
            break
        a, b = pts0.reshape(-1, 2)[good], p1[good]
        A, inl = cv2.estimateAffinePartial2D(a, b, method=cv2.RANSAC, ransacReprojThreshold=1.0)
        if A is None:
            direct_ok = False
            break
        c = A @ np.array([cx, cy, 1.0]) - np.array([cx, cy])
        rot = math.degrees(math.atan2(A[1, 0], A[0, 0]))
        sc = math.hypot(A[0, 0], A[1, 0])
        d = (b - a)[inl.ravel() == 1]
        direct.append(dict(t=t, dx=float(c[0] * scale), dy=float(c[1] * scale), rot_deg=rot,
                           scale=sc, n=int(good.sum()), spread=float(np.std(d, axis=0).mean() * scale)))
    # chained tracking (works for moving cameras too)
    path = [(0.0, 0.0)]
    chain_n = []
    for t in range(1, n):
        p = cv2.goodFeaturesToTrack(stack[t - 1], maxCorners=800, qualityLevel=0.005,
                                    minDistance=10, blockSize=7)
        if p is None:
            path.append(path[-1]); continue
        p = p.astype(np.float32)
        p1, good = _track_pair(stack[t - 1], stack[t], p)
        a, b = p.reshape(-1, 2)[good], p1[good]
        chain_n.append(int(good.sum()))
        A, inl = (cv2.estimateAffinePartial2D(a, b, method=cv2.RANSAC, ransacReprojThreshold=1.0)
                  if len(a) >= 6 else (None, None))
        if A is None:
            path.append(path[-1]); continue
        c = A @ np.array([cx, cy, 1.0]) - np.array([cx, cy])
        path.append((path[-1][0] + c[0] * scale, path[-1][1] + c[1] * scale))
    path = np.array(path)
    step = np.diff(path, axis=0) if n > 1 else np.zeros((1, 2))
    # parallax over a k-frame baseline
    k = max(1, min(12, n // 4))
    par = []
    for t0 in range(0, n - k, max(1, k // 2)):
        p = cv2.goodFeaturesToTrack(stack[t0], maxCorners=800, qualityLevel=0.005, minDistance=10, blockSize=7)
        if p is None:
            continue
        p = p.astype(np.float32)
        p1, good = _track_pair(stack[t0], stack[t0 + k], p)
        a, b = p.reshape(-1, 2)[good], p1[good]
        H, r = _homog_resid(a, b)
        if r is None:
            continue
        mv = float(np.median(np.linalg.norm(b - a, axis=1)) * scale)
        # p90 of residuals among the 80% best-fitting tracks (moving subjects are the worst 20%)
        rr = np.sort(r)[: max(5, int(0.8 * len(r)))]
        par.append(dict(t0=t0, k=k, motion_px=mv, resid_p90_px=float(np.percentile(rr, 90) * scale),
                        resid_med_px=float(np.median(r) * scale)))
    par_p90 = float(np.median([p["resid_p90_px"] for p in par])) if par else None
    par_mv = float(np.median([p["motion_px"] for p in par])) if par else None
    if direct_ok and direct:
        dx = np.array([d["dx"] for d in direct]); dy = np.array([d["dy"] for d in direct])
        mag = np.hypot(dx, dy)
        res["direct"] = dict(max_drift_px=float(mag.max()), final_dx=float(dx[-1]), final_dy=float(dy[-1]),
                             max_rot_deg=float(max(abs(d["rot_deg"]) for d in direct)),
                             max_scale_change=float(max(abs(d["scale"] - 1) for d in direct)),
                             jitter_px=float(np.std(np.diff(mag))) if len(mag) > 2 else 0.0,
                             track_spread_px=float(np.median([d["spread"] for d in direct[1:]])) if len(direct) > 1 else 0.0,
                             features=int(len(pts0)), per_frame=[[d["t"], round(d["dx"], 3), round(d["dy"], 3)] for d in direct])
        max_drift = float(mag.max())
    else:
        max_drift = float(np.max(np.linalg.norm(path, axis=1)))
    res["chained"] = dict(path_len_px=float(np.linalg.norm(step, axis=1).sum()),
                          end_offset_px=[float(path[-1][0]), float(path[-1][1])],
                          mean_step_px=float(np.linalg.norm(step, axis=1).mean()) if len(step) else 0.0)
    res["parallax"] = dict(baseline_frames=k, median_motion_px=par_mv, resid_p90_px=par_p90, samples=par[:12],
                           note="homography residual p90 (best 80% of tracks); pure pan/tilt/zoom/drift leaves "
                                "it near the tracking noise floor, depth-dependent motion raises it")
    res["max_drift_px"] = max_drift
    has_par = par_p90 is not None and par_p90 > TH["parallax_px"] and (par_mv or 0) > TH["parallax_px"]
    if direct_ok and max_drift < TH["locked_px"]:
        cls = "locked"
    elif direct_ok and max_drift <= TH["drift2d_max_px"] and not has_par:
        cls = "2d_drift"
    elif has_par:
        cls = "moving_parallax"
    else:
        cls = "moving_no_parallax"
    res["classification"] = cls
    res["confidence"] = "high" if direct_ok else "medium"
    return res


# ---------------------------------------------------------------- perspective
def _seg_arrays(segs):
    x1, y1, x2, y2 = segs.T
    d = np.stack([x2 - x1, y2 - y1], 1)
    L = np.linalg.norm(d, axis=1)
    d = d / L[:, None]
    mid = np.stack([(x1 + x2) / 2, (y1 + y2) / 2], 1)
    hl = np.cross(np.stack([x1, y1, np.ones_like(x1)], 1), np.stack([x2, y2, np.ones_like(x2)], 1))
    return d, L, mid, hl


def _vp_ransac(segs, rng, tol_deg=1.5, iters=4000):
    if len(segs) < 4:
        return None
    d, L, mid, hl = _seg_arrays(segs)
    prob = L / L.sum()
    cos_t = math.cos(math.radians(tol_deg))
    best, best_s = None, 0
    for _ in range(iters):
        i, j = rng.choice(len(segs), 2, replace=False, p=prob)
        p = np.cross(hl[i], hl[j])
        if abs(p[2]) < 1e-9:
            continue
        p = p[:2] / p[2]
        v = p - mid
        nv = np.linalg.norm(v, axis=1) + 1e-9
        inl = np.abs((v * d).sum(1) / nv) > cos_t
        s = L[inl].sum()
        if s > best_s:
            best_s, best = s, inl
    if best is None:
        return None
    # least-squares refinement on inliers
    nrm = np.stack([-d[best, 1], d[best, 0]], 1)
    c = (nrm * mid[best]).sum(1)
    W = L[best]
    A = nrm * W[:, None]
    p, *_ = np.linalg.lstsq(A, c * W, rcond=None)
    return dict(point=p, inliers=best, score=float(best_s))


def analyze_perspective(gray_f, rng):
    h, w = gray_f.shape
    lsd = cv2.createLineSegmentDetector(cv2.LSD_REFINE_STD)
    segs = lsd.detect((np.clip(gray_f, 0, 1) * 255).astype(np.uint8))[0]
    out = {"method": "LSD segments; RANSAC vanishing point on oblique segments (1.5 deg tolerance), "
                     "least-squares refine; verticals/horizontals checked separately"}
    if segs is None:
        out.update(vp_count=0, confidence="low"); return out, None, []
    segs = segs.reshape(-1, 4)
    d, L, mid, _ = _seg_arrays(segs)
    keep = L > 0.03 * math.hypot(w, h)
    segs, d, L, mid = segs[keep], d[keep], L[keep], mid[keep]
    ang = (np.degrees(np.arctan2(d[:, 1], d[:, 0])) + 180) % 180
    vert = np.abs(ang - 90) < 6
    horz = (ang < 4) | (ang > 176)
    obl = ~(vert | horz)
    out["segments"] = dict(total=int(len(segs)), vertical=int(vert.sum()), horizontal=int(horz.sum()),
                           oblique=int(obl.sum()))
    vps = []
    rest = segs[obl]
    total = L[obl].sum() + 1e-9
    for _ in range(2):
        r = _vp_ransac(rest, rng)
        if r is None:
            break
        frac = r["score"] / total
        if frac < 0.15 or (vps and r["score"] < 0.25 * vps[0]["score"]):
            break
        p = r["point"]
        vps.append(dict(x=float(p[0]), y=float(p[1]), nx=float(p[0] / w), ny=float(p[1] / h),
                        inside_frame=bool(0 <= p[0] <= w and 0 <= p[1] <= h), score=r["score"],
                        inlier_len_frac=float(frac), inliers=int(r["inliers"].sum()),
                        segs=rest[r["inliers"]].tolist()))
        rest = rest[~r["inliers"]]
    # verticals: roll + keystone
    if vert.sum() >= 3:
        va = ang[vert] - 90
        vx = (mid[vert, 0] - w / 2) / w
        slope = float(np.polyfit(vx, va, 1, w=L[vert])[0]) if vert.sum() >= 5 else 0.0
        out["verticals"] = dict(median_tilt_deg=float(np.median(va)), keystone_deg_per_framewidth=slope,
                                converging=bool(abs(slope) > 1.0))
        if abs(slope) > 0.3 and vert.sum() >= 5:
            vs = segs[vert]; dv, Lv, mv, _ = _seg_arrays(vs)
            nrm = np.stack([-dv[:, 1], dv[:, 0]], 1)
            A = nrm * Lv[:, None]
            pz, *_ = np.linalg.lstsq(A, (nrm * mv).sum(1) * Lv, rcond=None)
            out["verticals"]["vertical_vp"] = [float(pz[0]), float(pz[1])]
    if horz.sum() >= 2:
        ha = ang[horz]
        ha = np.where(ha > 90, ha - 180, ha)
        out["horizontals"] = dict(median_tilt_deg=float(np.median(ha)))
    nvp = len(vps) + (1 if out.get("verticals", {}).get("converging") else 0)
    out["vp_count"] = nvp
    out["vanishing_points"] = [{k: v for k, v in vp.items() if k != "segs"} for vp in vps]
    if vps:
        vp = vps[0]
        out["horizon_y"] = vp["y"]
        out["vp_offset_from_center_px"] = [vp["x"] - w / 2, vp["y"] - h / 2]
        # pitch hint for common focal lengths on a Super 35 sensor (assumption, labelled)
        hints = {}
        for f in (18, 24, 35, 50, 85):
            fpx = f / 24.89 * w
            hints[f"{f}mm_S35"] = round(math.degrees(math.atan((h / 2 - vp["y"]) / fpx)), 2)
        out["pitch_deg_if_focal"] = hints
        if len(vps) >= 2:
            a = np.array([vps[0]["x"] - w / 2, vps[0]["y"] - h / 2])
            b = np.array([vps[1]["x"] - w / 2, vps[1]["y"] - h / 2])
            f2 = -float(a @ b)
            out["focal_px_from_2vp"] = math.sqrt(f2) if f2 > 0 else None
        vv = out.get("verticals", {}).get("vertical_vp")
        if vv is not None:
            a = np.array([vp["x"] - w / 2, vp["y"] - h / 2]); b = np.array([vv[0] - w / 2, vv[1] - h / 2])
            f2 = -float(a @ b)
            if f2 > 0:
                fpx = math.sqrt(f2)
                out["focal_from_depth_and_vertical_vp"] = dict(
                    focal_px=round(fpx, 1), hfov_deg=round(math.degrees(2 * math.atan(w / 2 / fpx)), 1),
                    focal_mm_if_S35=round(fpx / w * 24.89, 1), focal_mm_if_FF=round(fpx / w * 36.0, 1),
                    pitch_deg=round(math.degrees(math.atan((h / 2 - vp["y"]) / fpx)), 2),
                    confidence="low" if abs(out["verticals"]["keystone_deg_per_framewidth"]) < 2 else "medium",
                    note="orthogonal VPs (depth + converging verticals) give focal length; weak keystone makes it "
                         "unstable. Prefer the camera report.")
    vv = out.get("verticals", {}).get("vertical_vp")
    if vv is not None and abs(vv[1] - h / 2) > h:
        # with keystone, the true vertical is the line from the principal point to the vertical VP
        out["roll_deg_estimate"] = round(math.degrees(math.atan2(vv[0] - w / 2, vv[1] - h / 2)), 3) * (1 if vv[1] > 0 else -1)
    else:
        out["roll_deg_estimate"] = out.get("verticals", {}).get("median_tilt_deg",
                                                                out.get("horizontals", {}).get("median_tilt_deg"))
    out["confidence"] = "high" if vps and vps[0]["inlier_len_frac"] > 0.4 else "medium" if vps else "low"
    return out, (vps[0] if vps else None), vps


def _peak_offsets(gx, gy, P, nvec, centre, half=5.0):
    offs = np.arange(-half, half + 0.01, 0.5)
    X = (P[:, 0:1] + (centre[:, None] + offs[None, :]) * nvec[0]).astype(np.float32)
    Yv = (P[:, 1:2] + (centre[:, None] + offs[None, :]) * nvec[1]).astype(np.float32)
    mag = np.abs(cv2.remap(gx, X, Yv, cv2.INTER_LINEAR) * nvec[0] + cv2.remap(gy, X, Yv, cv2.INTER_LINEAR) * nvec[1])
    k = mag.argmax(1)
    pk = mag[np.arange(len(k)), k]
    inner = (k > 0) & (k < len(offs) - 1)
    kk = np.clip(k, 1, len(offs) - 2)
    a_, b_, c_ = mag[np.arange(len(k)), kk - 1], mag[np.arange(len(k)), kk], mag[np.arange(len(k)), kk + 1]
    den = a_ - 2 * b_ + c_
    with np.errstate(divide="ignore", invalid="ignore"):
        sub = np.where(np.abs(den) > 1e-9, 0.5 * (a_ - c_) / den, 0)
    return centre + offs[k] + sub * 0.5, pk, inner


def _trace_edge(gx, gy, origin, dvec, nvec, L0, w, h, step=2.0):
    S = np.arange(0.04 * L0, 0.96 * L0, step)
    P = origin + np.outer(S, dvec)
    off, pk, inner = _peak_offsets(gx, gy, P, nvec, np.zeros(len(S)))
    ref = np.median(pk)
    ok = inner & (pk > 0.35 * ref)
    if ok.sum() < 15:
        return None, None
    S, O = list(S[ok]), list(off[ok])
    for direction in (1, -1):
        miss = 0
        s_ = (max(S) if direction > 0 else min(S))
        while miss < 4:
            s_ += direction * step
            span = max(S) - min(S)
            deg = 2 if span > 120 else 1
            pred = float(np.polyval(np.polyfit(S, O, deg), s_))
            q = origin + s_ * dvec + pred * nvec
            if not (3 <= q[0] < w - 3 and 3 <= q[1] < h - 3):
                break
            o, p_, inn = _peak_offsets(gx, gy, (origin + s_ * dvec)[None, :], nvec, np.array([pred]), half=2.5)
            if inn[0] and p_[0] > 0.35 * ref:
                S.append(s_); O.append(float(o[0])); miss = 0
            else:
                miss += 1
    order = np.argsort(S)
    return np.array(S)[order], np.array(O)[order]


def analyze_distortion(gray_f, scale):
    """Bow of long straight edges far from centre, traced to sub-pixel along their normal."""
    h, w = gray_f.shape
    lo_, hi_ = np.percentile(gray_f, 1), np.percentile(gray_f, 99)
    g8 = (np.clip((gray_f - lo_) / max(0.05, hi_ - lo_), 0, 1) * 255).astype(np.uint8)
    edges = cv2.Canny(cv2.GaussianBlur(g8, (5, 5), 1.2), 20, 60)
    minlen = int(0.22 * min(w, h))
    lines = cv2.HoughLinesP(edges, 2, np.pi / 720, threshold=60, minLineLength=minlen, maxLineGap=20)
    gf = cv2.GaussianBlur(((gray_f - lo_) / max(0.05, hi_ - lo_)).astype(np.float32), (0, 0), 0.8)
    gx = cv2.Sobel(gf, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(gf, cv2.CV_32F, 0, 1, ksize=3)
    cx, cy = w / 2, h / 2
    rmax = math.hypot(cx, cy)
    found = []
    if lines is not None:
        for x1, y1, x2, y2 in lines.reshape(-1, 4).astype(float):
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            if math.hypot(mx - cx, my - cy) < 0.35 * rmax:
                continue
            L0 = math.hypot(x2 - x1, y2 - y1)
            dvec = np.array([x2 - x1, y2 - y1]) / L0
            nvec = np.array([-dvec[1], dvec[0]])
            if nvec @ np.array([mx - cx, my - cy]) < 0:
                nvec = -nvec            # normal points away from the image centre
            # Hough splits a bent edge into short chords, so follow the edge beyond the seed's
            # ends (predicting its path from the points found so far) before fitting the bow
            S, O = _trace_edge(gx, gy, np.array([x1, y1]), dvec, nvec, L0, w, h)
            if S is None:
                continue
            p0 = np.array([x1, y1]) + S[0] * dvec + O[0] * nvec
            p1 = np.array([x1, y1]) + S[-1] * dvec + O[-1] * nvec
            if any(np.linalg.norm(p0 - np.array(f["p0"])) + np.linalg.norm(p1 - np.array(f["p1"])) < 12 or
                   np.linalg.norm(p0 - np.array(f["p1"])) + np.linalg.norm(p1 - np.array(f["p0"])) < 12 for f in found):
                continue        # same physical edge traced from another seed
            L = float(S[-1] - S[0])
            t = (S - S[0]) / L * 2 - 1
            off = O
            coef = np.polyfit(t, off, 2)
            fit = np.polyval(coef, t)
            rms = float(np.sqrt(np.mean((off - fit) ** 2)))
            if rms > 0.6:
                continue
            x1, y1, x2, y2 = float(p0[0]), float(p0[1]), float(p1[0]), float(p1[1])
            bow_out = float(-coef[0])    # >0: middle of the line bulges away from centre (barrel)
            # radial distortion bends a line in proportion to its distance from the centre and the
            # square of its length; lines through the centre stay straight. Convert to k1.
            dperp = abs(nvec @ np.array([x1 - cx, y1 - cy]))
            gain = rmax * rmax / (dperp * (L / 2) ** 2) if dperp > 0.25 * rmax else None
            k1 = bow_out * gain if gain else None
            k1_sigma = max(0.15, rms) * gain if gain else None   # tracing noise floor ~0.15 px
            found.append(dict(x1=x1, y1=y1, x2=x2, y2=y2, len_px=L * scale, bow_out_px=bow_out * scale,
                              fit_rms_px=rms * scale, r_norm=math.hypot(mx - cx, my - cy) / rmax,
                              d_perp_norm=dperp / rmax, k1=k1, k1_sigma=k1_sigma, p0=p0.tolist(), p1=p1.tolist()))
    # most informative first: lines far from the centre (small k1_sigma); radial lines carry no signal
    found.sort(key=lambda f: (f["k1_sigma"] is None, f["k1_sigma"] or 0, -f["len_px"]))
    found = found[:16]
    out = {"method": "Hough seeds >=22% of frame, centre >=35% of half-diagonal out; each edge followed "
                     "beyond the seed and traced sub-pixel along the normal; quadratic bow signed outward = barrel; each bow converted to a "
                     "radial k1 (bow * R^2 / (d_perp * (L/2)^2)), lines passing near the centre ignored",
           "lines": [{k: (round(v, 3) if isinstance(v, float) else v) for k, v in f.items() if k not in ("p0", "p1")}
                     for f in found]}
    use = [f for f in found if f["k1"] is not None]
    if len(use) >= 2:
        ks = np.array([f["k1"] for f in use]); sg = np.array([f["k1_sigma"] for f in use])
        wts = 1 / sg ** 2
        k = float((wts * ks).sum() / wts.sum())
        ksig = float(1 / math.sqrt(wts.sum()))
        agree = float(np.mean(np.sign(ks) == np.sign(k)))
        # bow of a full-height vertical at the left/right frame edge, native px
        fb = cx * cy * cy / (rmax * rmax) * scale
        edge_bow, edge_sig = k * fb, ksig * fb
        signif = abs(k) / ksig
        dom = float(wts.max() / wts.sum())
        out.update(k1_estimate=round(k, 5), k1_sigma=round(ksig, 5), edge_bow_px=round(edge_bow, 3),
                   edge_bow_sigma_px=round(edge_sig, 3), significance_sigma=round(signif, 2), lines_used=len(use),
                   dominant_line_weight=round(dom, 2),
                   note=("one line carries %d%% of the weight: confirm on a second straight edge or a lens grid" % round(100 * dom))
                   if dom > 0.7 else None,
                   median_bow_px=float(np.median([f["bow_out_px"] for f in found])), sign_agreement=agree,
                   type="barrel" if k > 0 else "pincushion",
                   distortion_likely=bool(abs(edge_bow) > TH["distortion_px"] and signif >= 2.5),
                   confidence=("low" if len(use) < 3 or edge_sig >= 1.0 else
                               "medium" if dom > 0.7 else "high"),
                   magnitude_note="self-test (2026-10-23): k1 0.0339 read for a true 0.035 (edge-traced lines). "
                                  "Good enough to decide; still set the final undistort with a lens tool or grid")
    else:
        out.update(distortion_likely=None, confidence="low", note="not enough long straight edges near the frame edge")
    return out, found


# ---------------------------------------------------------------- tone, clipping, practicals
def clip_levels(hists, edges):
    """Graded plates rarely clip at exactly legal white: the ceiling sits wherever the grade put the
    sensor clip (super-white, or rolled off below 1.0), and grain smears it into a hump a few
    thousandths wide with a thin noise tail above. So look for the highest hump (pile-up) in the
    top of each channel's histogram, not for the absolute maximum."""
    out = {}
    bw = edges[1] - edges[0]
    k = 5
    for ci, nm in enumerate("RGB"):
        hst = hists[ci].astype(np.float64)
        tot = hst.sum()
        nz = np.nonzero(hst > tot * 2e-6)[0]
        if not len(nz):
            continue
        top = nz[-1]
        sm = np.convolve(hst, np.ones(k) / k, mode="same")
        win = int(0.06 / bw)
        ceiling, share, prom = None, 0.0, 0.0
        for i in range(top, max(k, top - win), -1):
            lo_ = sm[max(0, i - 30):max(1, i - 3)]
            if sm[i] < sm[max(0, i - 3):i].max(initial=0) or sm[i] < sm[i + 1:i + 4].max(initial=0):
                continue
            p_ = sm[i] / max(1e-9, lo_.min()) if lo_.size else 0
            sh = hst[max(0, i - 6):i + 7].sum() / tot
            if p_ >= TH["clip_prominence"] and sh >= TH["clip_plateau_frac"]:
                ceiling, share, prom = float(edges[i] + bw / 2), float(sh), float(p_)
                break
        lvl = float(edges[top + 1])
        out[nm] = dict(max_level=round(lvl, 4), ceiling=(round(ceiling, 4) if ceiling else None),
                       hump_share=share, hump_prominence=round(prom, 2),
                       plateau=bool(ceiling is not None and ceiling >= TH["clip_min_level"]))
    return out


def components(mask, min_area):
    n, lab, st, cen = cv2.connectedComponentsWithStats(mask.astype(np.uint8), 8)
    comps = []
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] >= min_area:
            comps.append(dict(id=i, x=int(st[i, 0]), y=int(st[i, 1]), w=int(st[i, 2]), h=int(st[i, 3]),
                              area=int(st[i, 4]), cx=float(cen[i, 0]), cy=float(cen[i, 1])))
    return comps, lab


def shape_stats(lab, cid):
    ys, xs = np.nonzero(lab == cid)
    pts = np.stack([xs, ys], 1).astype(np.float32)
    (rx, ry), (rw, rh), ra = cv2.minAreaRect(pts)
    length, width = max(rw, rh), max(1.0, min(rw, rh))
    # orientation of the long axis in degrees from horizontal
    ang = ra if rw >= rh else ra + 90
    return length, width, (ang + 180) % 180, ys, xs


def analyze_practicals(rgb, clipmask, horizon_y, scale, ceiling=None):
    h, w, _ = rgb.shape
    mx = rgb.max(2)
    Y = luma(rgb)
    local = cv2.GaussianBlur(mx, (0, 0), 25)
    cand = (mx > TH["practical_min"]) & ((mx - local) > TH["practical_contrast"])
    cand = cv2.morphologyEx(cand.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    comps, lab = components(cand, max(12, int(2e-5 * w * h)))
    lin = to_lin(rgb)
    items = []
    for c in comps:
        L_, W_, ang, ys, xs = shape_stats(lab, c["id"])
        v = mx[ys, xs]
        core = v >= np.percentile(v, 75)
        core_rgb = rgb[ys[core], xs[core]].mean(0)
        clipped = float(clipmask[ys, xs].mean())
        items.append(dict(
            bbox=[c["x"], c["y"], c["w"], c["h"]], centroid=[round(c["cx"], 1), round(c["cy"], 1)],
            area_px=c["area"], length_px=round(L_ * scale, 1), width_px=round(W_ * scale, 1),
            aspect=round(L_ / W_, 2), angle_deg=round(ang, 1),
            peak_max_rgb=round(float(v.max()), 4), core_rgb=[round(float(x), 4) for x in core_rgb],
            core_hex=hexcol(core_rgb), core_linear=[round(float(x), 4) for x in lin[ys[core], xs[core]].mean(0)],
            peak_linear=round(float(to_lin(v.max())), 4), clipped_frac=round(clipped, 3),
            of_ceiling=(round(float(v.max()) / ceiling, 3) if ceiling else None),
            above_horizon=bool(horizon_y is None or c["cy"] < horizon_y),
            local_contrast=round(float((mx - local)[ys, xs].max()), 3)))
    items.sort(key=lambda d: -d["peak_max_rgb"])
    sources = [i for i in items if i["above_horizon"]]
    unclipped = [i for i in sources if i["clipped_frac"] < 0.02]
    return dict(note="candidates include speculars (glass edges, chrome) as well as emitters: decide which are real "
                     "light sources on the overlay before picking the energy reference",
                method="local maxima of max(R'G'B') >= %.2f and >= %.2f above a 25 px blur; clipped share from "
                       "the clip mask; linear = display-linear (value^2.4, Strategy A)" % (TH["practical_min"], TH["practical_contrast"]),
                items=items[:25], brightest_unclipped_source=(unclipped[0] if unclipped else None),
                clipped_sources=[i for i in sources if i["clipped_frac"] >= 0.02][:8]), items


def analyze_streaks(rgb, horizon_y, sources, scale, vp=None, excl=None):
    h, w, _ = rgb.shape
    Y = luma(rgb)
    top = int(horizon_y) if horizon_y is not None and 0 < horizon_y < h else int(0.55 * h)
    floor = np.zeros_like(Y, bool)
    floor[top:, :] = True
    k = max(15, int(0.03 * w) | 1)
    th = cv2.morphologyEx(Y.astype(np.float32), cv2.MORPH_TOPHAT, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k)))
    m = floor & (th > 0.05) & (Y > np.percentile(Y[floor], 60))
    m = cv2.morphologyEx(m.astype(np.uint8), cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 9)))
    comps, lab = components(m, max(40, int(3e-5 * w * h)))
    Ys = cv2.GaussianBlur(Y.astype(np.float32), (0, 0), 1.5)
    streaks = []
    for c in comps:
        L_, W_, ang, ys, xs = shape_stats(lab, c["id"])
        asp = L_ / W_
        if asp < TH["streak_aspect"] or L_ < TH["streak_min_len"] * h:
            continue
        # A floor reflection sits straight below a point source (level camera) or, for a line
        # source running into depth, on a line through the VP. Rails, baseboards and door
        # edges also make long bright lines, so test orientation and side symmetry.
        vert_dev = abs(ang - 90)
        to_vp = None
        if vp is not None:
            dvp = (math.degrees(math.atan2(vp[1] - c["cy"], vp[0] - c["cx"])) + 180) % 180
            to_vp = min(abs(dvp - ang), 180 - abs(dvp - ang))
        oriented = vert_dev < 15 or (to_vp is not None and to_vp < 4)
        a = math.radians(ang)
        nx, ny = -math.sin(a), math.cos(a)
        off = max(3.0, 2.0 * W_)
        sx = np.clip(xs[::3] + nx * off, 0, w - 1).astype(int); sy = np.clip(ys[::3] + ny * off, 0, h - 1).astype(int)
        tx = np.clip(xs[::3] - nx * off, 0, w - 1).astype(int); ty = np.clip(ys[::3] - ny * off, 0, h - 1).astype(int)
        side_a, side_b = float(np.median(Ys[sy, sx])), float(np.median(Ys[ty, tx]))
        excess = float(np.median(Ys[ys, xs])) - 0.5 * (side_a + side_b)
        symmetric = excess > 0 and abs(side_a - side_b) < 0.5 * excess
        peak = float(Y[ys, xs].max())
        src = None
        for s in sources:
            bx, by, bw, bh = s["bbox"]
            if bx - 0.02 * w <= c["cx"] <= bx + bw + 0.02 * w:
                src = s; break
        in_floor = horizon_y is None or c["cy"] > horizon_y + 0.08 * h
        if excl is not None and excl[ys, xs].mean() > 0.3:
            continue      # on the moving subject (gaps between legs, reflections of the person)
        likely = bool(oriented and symmetric and in_floor)
        streaks.append(dict(bbox=[c["x"], c["y"], c["w"], c["h"]], length_px=round(L_ * scale, 1),
                            width_px=round(W_ * scale, 1), aspect=round(asp, 2), angle_deg=round(ang, 1),
                            deg_from_vertical=round(vert_dev, 1), deg_from_vp_line=(round(to_vp, 1) if to_vp is not None else None),
                            side_asymmetry=round(abs(side_a - side_b) / max(1e-4, excess), 2) if excess > 0 else None,
                            likely_reflection=likely, paired_with_source=bool(src),
                            peak_luma=round(peak, 4), peak_linear=round(float(to_lin(peak)), 4),
                            tophat=round(float(th[ys, xs].max()), 3),
                            source_centroid=(src["centroid"] if src else None),
                            refl_ratio_linear=(round(float(to_lin(peak)) / src["peak_linear"], 3)
                                               if src and src["clipped_frac"] < 0.02 and src["peak_linear"] > 0 else None)))
    streaks.sort(key=lambda s: (not s["likely_reflection"], -s["length_px"]))
    good = [s for s in streaks if s["likely_reflection"]]
    paired = [s for s in good if s["paired_with_source"]]
    asp = [s["aspect"] for s in (paired or good)]
    return dict(method="white top-hat (%d px) below the horizon; components with aspect >= %.1f and length >= %.0f%% "
                       "of frame height; 'likely_reflection' = vertical (+-15 deg) or on a VP line (+-4 deg) AND the "
                       "two sides match (rails, baseboards and door edges have different surfaces either side); "
                       "paired with a source above when x overlaps" % (k, TH["streak_aspect"], 100 * TH["streak_min_len"]),
                floor_region_top_y=top, streaks=streaks[:14], count=len(good), candidates_total=len(streaks),
                median_aspect=(float(np.median(asp)) if asp else None),
                longest_reflection=(good[0] if good else None),
                paired_count=len(paired), gloss_present=bool(len(paired) >= 1),
                gloss_possible=bool(not paired and len(good) >= 2),
                confidence="medium" if len(good) >= 2 else "low"), good


def analyze_dark_panels(rgb, black_p1, horizon_y, excl=None):
    h, w, _ = rgb.shape
    Y = luma(rgb)
    thr = max(black_p1 + 0.08, np.percentile(Y, 8))
    m = (Y < thr)
    if excl is not None:
        m &= ~excl
    m = m.astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    comps, lab = components(m, int(0.005 * w * h))
    k = max(9, int(0.012 * w) | 1)
    th = cv2.morphologyEx(Y.astype(np.float32), cv2.MORPH_TOPHAT, cv2.getStructuringElement(cv2.MORPH_RECT, (k, 1)))
    panels = []
    for c in comps:
        x, y, ww, hh = c["x"], c["y"], c["w"], c["h"]
        sub = (lab[y:y + hh, x:x + ww] == c["id"])
        dil = cv2.dilate(sub.astype(np.uint8), np.ones((7, 7), np.uint8)).astype(bool)
        bright_lines = float(((th[y:y + hh, x:x + ww] > 0.04) & dil).mean())
        vals = Y[y:y + hh, x:x + ww][sub]
        panels.append(dict(bbox=[x, y, ww, hh], area_frac=round(c["area"] / (w * h), 4),
                           mean_luma=round(float(vals.mean()), 4), std_luma=round(float(vals.std()), 4),
                           mean_rgb=[round(float(v), 4) for v in rgb[y:y + hh, x:x + ww][sub].mean(0)],
                           tall=bool(hh > 1.5 * ww), thin_highlight_density=round(bright_lines, 4),
                           side=("left" if x + ww / 2 < w / 3 else "right" if x + ww / 2 > 2 * w / 3 else "centre")))
    panels = [p for p in panels if p["area_frac"] < 0.25]
    panels.sort(key=lambda p: -p["area_frac"])
    return dict(low_key=bool(np.median(Y) < 0.18), method="regions darker than max(black P1 + 0.08, P8 luma), >=0.5% of frame; thin horizontal top-hat "
                       "highlights inside suggest mullions or reflections. Candidates only: confirm on the overlay.",
                threshold=round(float(thr), 4), candidates=panels[:6])


def ring_profile(Y, vp, excl, nbins=10, pct=2):
    h, w = Y.shape
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.hypot(xx - vp[0], yy - vp[1])
    rmax = np.percentile(r, 99)
    edges = np.linspace(0.03 * rmax, rmax, nbins + 1)
    prof = []
    for i in range(nbins):
        m = (r >= edges[i]) & (r < edges[i + 1]) & ~excl
        if m.sum() < 200:
            continue
        prof.append(dict(r_norm=round(float((edges[i] + edges[i + 1]) / 2 / rmax), 3),
                         dark_p=round(float(np.percentile(Y[m], pct)), 4),
                         median=round(float(np.median(Y[m])), 4), n=int(m.sum())))
    return prof


def panel_profile(Y, vp, excl, panels, nbins=6):
    """Dark level of ONE dark surface (glass bank, dark wall) sampled along depth. Same material
    near and far, so any lift toward the VP is haze or veiling glare, not a different surface."""
    h, w = Y.shape
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.hypot(xx - vp[0], yy - vp[1])
    best = None
    for p in panels:
        x, y, bw, bh = p["bbox"]
        m = np.zeros((h, w), bool); m[y:y + bh, x:x + bw] = True
        m &= ~excl
        if m.sum() < 2000:
            continue
        rr = r[m]
        lo, hi = np.percentile(rr, 2), np.percentile(rr, 98)
        if hi <= 0 or lo / hi > 0.45:
            continue          # does not run into depth
        span = hi - lo
        if best is None or span > best[0]:
            best = (span, p, m, lo, hi)
    if best is None:
        return None
    _, p, m, lo, hi = best
    edges = np.linspace(lo, hi, nbins + 1)
    prof = []
    for i in range(nbins):
        mm = m & (r >= edges[i]) & (r < edges[i + 1])
        if mm.sum() < 150:
            continue
        prof.append(dict(r_norm=round(float((edges[i] + edges[i + 1]) / 2 / np.percentile(r, 99)), 3),
                         dark_p=round(float(np.percentile(Y[mm], 10)), 4), n=int(mm.sum())))
    return dict(panel_bbox=p["bbox"], profile=prof) if len(prof) >= 3 else None


def analyze_haze(rgb, vp, excl, panels=()):
    if vp is None:
        return dict(measured=False, note="no vanishing point: depth direction unknown")
    Y = luma(rgb)
    pp = panel_profile(Y, (vp["x"], vp["y"]), excl, panels)
    if pp:
        prof = pp["profile"]
        far, near = prof[0]["dark_p"], min(p["dark_p"] for p in prof[len(prof) // 2:])
        h, w = Y.shape
        x, y, bw, bh = pp["panel_bbox"]
        yy, xx = np.mgrid[0:h, 0:w]
        rr = np.hypot(xx - vp["x"], yy - vp["y"])
        m = np.zeros((h, w), bool); m[y:y + bh, x:x + bw] = True
        m &= ~excl & (rr < np.percentile(rr[m], 20))
        sel = m & (Y <= np.percentile(Y[m], 10)) if m.sum() > 100 else None
        tint = [round(float(v), 4) for v in rgb[sel].mean(0)] if sel is not None and sel.any() else None
        lift = float(far - near)
        return dict(measured=True,
                    method="P10 luma of one dark surface (dark-panel candidate %s) binned by distance from the VP; "
                           "same material near and far, so the lift is haze/veiling glare" % pp["panel_bbox"],
                    profile=prof, far_dark=round(float(far), 4), near_dark=round(float(near), 4),
                    lift=round(lift, 4), lift_linear=round(float(to_lin(far) - to_lin(near)), 5),
                    far_dark_rgb=tint, far_dark_hex=(hexcol(tint) if tint else None),
                    haze_present=bool(lift > TH["haze_lift"]), confidence="medium",
                    rings_fallback=ring_profile(Y, (vp["x"], vp["y"]), excl))
    prof = ring_profile(Y, (vp["x"], vp["y"]), excl)
    if len(prof) < 4:
        return dict(measured=False, note="too few samples")
    far = np.mean([p["dark_p"] for p in prof[:2]])
    near = np.min([p["dark_p"] for p in prof[len(prof) // 2:]])
    lift = float(far - near)
    tint = None
    # far haze colour: median colour of the darkest 5% of pixels in the innermost usable rings
    h, w = Y.shape
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.hypot(xx - vp["x"], yy - vp["y"])
    m = (r < 0.2 * np.percentile(r, 99)) & ~excl
    if m.sum() > 200:
        sel = m & (Y <= np.percentile(Y[m], 5))
        tint = [round(float(v), 4) for v in rgb[sel].mean(0)]
    return dict(measured=True,
                method="2nd-percentile luma in rings around the VP (near VP = far depth), clipped and subject "
                       "pixels excluded; lift = far dark level minus the darkest near ring",
                profile=prof, far_dark=round(float(far), 4), near_dark=round(float(near), 4),
                lift=round(lift, 4), lift_linear=round(float(to_lin(far) - to_lin(near)), 5),
                far_dark_rgb=tint, far_dark_hex=(hexcol(tint) if tint else None),
                haze_present=bool(lift > TH["haze_lift"]),
                confidence="low", note="rings mix surfaces: a bright far wall reads as haze. Confirm on the plate.")


def analyze_palette(rgb, excl):
    Y = luma(rgb)
    ch = rgb.max(2) - rgb.min(2)
    bands = {"shadows": (Y >= 0.0) & (Y < 0.2), "mids": (Y >= 0.2) & (Y < 0.6), "highs": (Y >= 0.6) & (Y < 0.95)}
    out = {}
    for nm, m in bands.items():
        m = m & ~excl
        if m.sum() < 500:
            continue
        mean = rgb[m].mean(0)
        hn, hd, sat = hue_name(mean)
        out[nm] = dict(share=round(float(m.mean()), 3), mean_rgb=[round(float(v), 4) for v in mean],
                       hex=hexcol(mean), hue=hn, hue_deg=round(hd, 1), mean_sat=round(sat, 3),
                       chroma_p50=round(float(np.median(ch[m])), 4), chroma_p95=round(float(np.percentile(ch[m], 95)), 4))
    allc = ch[~excl & (Y > 0.03)]
    ceil = float(np.percentile(allc, 99)) if allc.size else None
    sh, hi = out.get("shadows", {}).get("hue"), out.get("highs", {}).get("hue")
    mid = out.get("mids", {}).get("hue")
    teal_orange = bool(sh in ("cyan/teal", "blue", "green") and (hi in ("orange", "yellow") or mid in ("orange", "yellow")))
    cool_cast = bool(all(out.get(b, {}).get("hue") in ("cyan/teal", "blue", "green", "neutral") for b in out)
                     and any(out.get(b, {}).get("hue") in ("cyan/teal", "blue") for b in out))
    med_ch = float(np.median(allc)) if allc.size else 0
    return dict(method="mean R'G'B' and chroma (max-min) per luma band, clipped and subject pixels excluded",
                bands=out, chroma_ceiling_p99=(round(ceil, 4) if ceil is not None else None),
                chroma_median=round(med_ch, 4),
                low_saturation=bool(med_ch < 0.08), teal_orange=teal_orange, overall_cool_cast=cool_cast)


def analyze_sharpness(Yf, vp, excl, tiles=(24, 14)):
    h, w = Yf.shape
    g1 = cv2.GaussianBlur(Yf, (0, 0), 1.0)
    g4 = cv2.GaussianBlur(Yf, (0, 0), 4.0)
    hf, mf = np.abs(Yf - g1), np.abs(g1 - g4)
    tw, th_ = w // tiles[0], h // tiles[1]
    rows = []
    heat = np.full((tiles[1], tiles[0]), np.nan, np.float32)
    for j in range(tiles[1]):
        for i in range(tiles[0]):
            sl = (slice(j * th_, (j + 1) * th_), slice(i * tw, (i + 1) * tw))
            if excl[sl].mean() > 0.3:
                continue
            M = mf[sl].mean()
            rows.append((i, j, M, hf[sl].mean()))
    if not rows:
        return dict(measured=False), heat
    Ms = np.array([r[2] for r in rows])
    thr = np.percentile(Ms, 55)
    pts = []
    for i, j, M, H in rows:
        if M < thr or M < 1e-3:
            continue
        s = H / M
        heat[j, i] = s
        cxp, cyp = (i + 0.5) * tw, (j + 0.5) * th_
        rn = math.hypot(cxp - vp["x"], cyp - vp["y"]) / math.hypot(w, h) if vp else None
        pts.append((s, rn, cxp, cyp))
    out = dict(method="per-tile ratio of fine (sigma<1) to medium (1-4) detail energy on textured tiles; "
                      "independent of contrast, raised by noise, lowered by defocus/motion blur",
               tiles_used=len(pts), global_median=round(float(np.median([p[0] for p in pts])), 4))
    if vp and len(pts) > 10:
        rn = np.array([p[1] for p in pts]); s = np.array([p[0] for p in pts])
        far = s[rn < np.percentile(rn, 25)]; near = s[rn > np.percentile(rn, 75)]
        mid = s[(rn >= np.percentile(rn, 25)) & (rn <= np.percentile(rn, 75))]
        ratio = float(np.median(far) / np.median(near)) if len(far) and len(near) else None
        out.update(far_median=round(float(np.median(far)), 4), mid_median=round(float(np.median(mid)), 4),
                   near_median=round(float(np.median(near)), 4), far_near_ratio=(round(ratio, 3) if ratio else None),
                   far_soft=bool(ratio is not None and ratio < TH["far_soft_ratio"]),
                   focus_band=max((("far", np.median(far)), ("mid", np.median(mid)), ("near", np.median(near))),
                                  key=lambda t: t[1])[0])
    out["confidence"] = "medium"
    return out, heat


# ---------------------------------------------------------------- noise / grain
class NoiseAcc:
    """Temporal noise from consecutive-frame differences, robust to movers (MAD)."""
    bands = {"shadows": (0.02, 0.2), "mids": (0.2, 0.6), "highs": (0.6, 0.9)}

    def __init__(self, max_pairs=24):
        self.prev = None
        self.samples = {b: [[], [], [], []] for b in self.bands}
        self.ac = []
        self.pairs = 0
        self.max_pairs = max_pairs
        self.rng = np.random.default_rng(1)

    def add(self, rgb):
        if self.pairs >= self.max_pairs:
            return
        if self.prev is not None:
            d = rgb - self.prev
            Y = luma(self.prev)
            dY = luma(rgb) - Y
            for b, (lo, hi) in self.bands.items():
                m = (Y >= lo) & (Y < hi)
                idx = np.flatnonzero(m)
                if idx.size < 2000:
                    continue
                idx = self.rng.choice(idx, min(idx.size, 40000), replace=False)
                for c in range(3):
                    self.samples[b][c].append(d[..., c].ravel()[idx])
                self.samples[b][3].append(dY.ravel()[idx])
            # spatial autocorrelation of the temporal difference (grain size), on a centre crop
            hh, ww = dY.shape
            cr = dY[hh // 4: 3 * hh // 4, ww // 4: 3 * ww // 4]
            cr = cr - np.median(cr)
            lim = 4 * 1.4826 * np.median(np.abs(cr))
            cr = np.clip(cr, -lim, lim)
            v = (cr * cr).mean()
            if v > 0:
                self.ac.append(((cr[:, 1:] * cr[:, :-1]).mean() / v, (cr[1:, :] * cr[:-1, :]).mean() / v))
            self.pairs += 1
        self.prev = rgb

    def result(self, bd):
        out = {}
        for b, chans in self.samples.items():
            if not chans[0]:
                continue
            row = {}
            for c, nm in enumerate(["R", "G", "B", "Y"]):
                x = np.concatenate(chans[c])
                sig = 1.4826 * np.median(np.abs(x - np.median(x))) / math.sqrt(2)
                row[nm] = round(float(sig), 5)
            row["Y_codes"] = round(row["Y"] * 219 * 2 ** (bd - 8), 2)
            row["below_one_code"] = bool(row["Y_codes"] < 0.5)
            out[b] = row
        ac = np.array(self.ac) if self.ac else None
        return dict(method="sigma = 1.4826*MAD(frame t+1 - frame t)/sqrt(2) per luma band, R'G'B' units "
                           "(0-1 = legal black-white); Y_codes in source code values",
                    pairs=self.pairs, bands=out,
                    autocorr_lag1_h=(round(float(ac[:, 0].mean()), 3) if ac is not None else None),
                    autocorr_lag1_v=(round(float(ac[:, 1].mean()), 3) if ac is not None else None))


def spatial_noise(rgb, excl_native=None):
    """White-noise-equivalent sigma from flat patches (use when the camera moves)."""
    s = 1.0
    k = cv2.getGaussianKernel(9, s)
    k2 = k @ k.T
    delta = np.zeros_like(k2); delta[4, 4] = 1
    gain = math.sqrt(((delta - k2) ** 2).sum())
    Y = luma(rgb)
    h, w = Y.shape
    T = 32
    gm = cv2.GaussianBlur(Y, (0, 0), 2)
    gmag = np.hypot(cv2.Sobel(gm, cv2.CV_32F, 1, 0), cv2.Sobel(gm, cv2.CV_32F, 0, 1))
    tiles = []
    for y in range(0, h - T, T):
        for x in range(0, w - T, T):
            yt = Y[y:y + T, x:x + T]
            if not (0.03 < yt.mean() < 0.9):
                continue
            tiles.append((gmag[y:y + T, x:x + T].mean(), y, x))
    if len(tiles) < 10:
        return dict(measured=False)
    tiles.sort()
    flat = tiles[: max(10, len(tiles) // 10)]
    out = {}
    for c, nm in enumerate("RGB"):
        ch = rgb[..., c]
        hp = ch - cv2.GaussianBlur(ch, (9, 9), s)
        vals = np.concatenate([hp[y:y + T, x:x + T].ravel() for _, y, x in flat])
        out[nm] = round(float(1.4826 * np.median(np.abs(vals - np.median(vals))) / gain), 5)
    return dict(measured=True, method="flat 32 px tiles (lowest 10% gradient), high-pass (sigma 1) MAD, "
                                      "white-noise equivalent; underestimates clumpy grain", sigma=out,
                tiles=len(flat))


# ---------------------------------------------------------------- subject / motion
def analyze_subject(stack_small, cam_class, sc_small, keyframes_small_idx, shifts=None):
    n = len(stack_small)
    h, w = stack_small[0].shape
    out = {"method": None}
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    people = []
    for t in keyframes_small_idx:
        g = stack_small[t]
        rects, wts = hog.detectMultiScale(g, winStride=(8, 8), padding=(16, 16), scale=1.05)
        for (x, y, rw, rh), wt in zip(rects, np.ravel(wts) if len(rects) else []):
            if wt > 0.5:
                people.append(dict(t=int(t), bbox=[int(x * sc_small), int(y * sc_small), int(rw * sc_small), int(rh * sc_small)],
                                   score=round(float(wt), 2)))
    out["hog_people"] = people[:30]
    coverage = np.zeros((h, w), np.float32)
    track = []
    if cam_class in ("locked", "2d_drift"):
        if shifts is not None:
            # register every frame back onto frame 0 so slow drift does not read as motion
            stack_small = [cv2.warpAffine(g, np.float32([[1, 0, -shifts[t][0]], [0, 1, -shifts[t][1]]]), (w, h),
                                          flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
                           if t < len(shifts) else g for t, g in enumerate(stack_small)]
        samp = np.linspace(0, n - 1, min(n, 41)).astype(int)
        bg = np.median(np.stack([stack_small[i] for i in samp]), axis=0).astype(np.float32)
        diffs = [np.abs(stack_small[i].astype(np.float32) - bg) for i in samp]
        noise = 1.4826 * np.median(np.abs(np.stack(diffs[:5]) - np.median(np.stack(diffs[:5]))))
        thr = max(8.0, 6 * noise)
        speeds = []
        for i, t in enumerate(samp):
            m = (diffs[i] > thr).astype(np.uint8)
            # a slow subject overlaps itself, so the median background keeps a ghost of it; keep only
            # changed pixels that are also moving now
            t2 = t + 1 if t + 1 < n else t - 1
            fl = cv2.calcOpticalFlowFarneback(stack_small[t], stack_small[t2], None, 0.5, 3, 15, 3, 5, 1.2, 0)
            v = np.hypot(fl[..., 0], fl[..., 1])
            moving = cv2.dilate((v > 0.15).astype(np.uint8), np.ones((21, 21), np.uint8))
            if ((m > 0) & (v > 0.15)).sum() > 50:
                speeds.append(float(np.median(v[(m > 0) & (v > 0.15)])) * sc_small)
            m = m & moving
            m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
            m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15)))
            comps, lab = components(m, int(0.0015 * w * h))
            if not comps:
                continue
            # group components that are close (limbs of one person)
            comps.sort(key=lambda c: -c["area"])
            main = comps[0]
            x0, y0, x1, y1 = main["x"], main["y"], main["x"] + main["w"], main["y"] + main["h"]
            for c in comps[1:]:
                if (c["x"] < x1 + 0.03 * w and c["x"] + c["w"] > x0 - 0.03 * w and
                        c["y"] < y1 + 0.05 * h and c["y"] + c["h"] > y0 - 0.05 * h):
                    x0, y0 = min(x0, c["x"]), min(y0, c["y"])
                    x1, y1 = max(x1, c["x"] + c["w"]), max(y1, c["y"] + c["h"])
            coverage[y0:y1, x0:x1] += 1
            track.append(dict(t=int(t), bbox=[int(x0 * sc_small), int(y0 * sc_small), int((x1 - x0) * sc_small),
                                              int((y1 - y0) * sc_small)],
                              changed_area_frac=round(float(m.mean()), 4)))
        out["method"] = ("median background over %d frames; |frame - bg| > %.1f (8-bit stretched) AND moving in "
                         "Farneback flow (drops the ghost a slow, self-overlapping subject leaves in the median); "
                         "grouped components; HOG people detector on key frames as a cross-check" % (len(samp), thr))
    else:
        out["method"] = "camera moves: background subtraction skipped; HOG people detector on key frames only"
    out["track"] = track
    out["drift_compensated"] = shifts is not None
    if track:
        b0, b1 = track[0]["bbox"], track[-1]["bbox"]
        def iou(a, b):
            ax1, ay1, bx1, by1 = a[0] + a[2], a[1] + a[3], b[0] + b[2], b[1] + b[3]
            ix = max(0, min(ax1, bx1) - max(a[0], b[0])); iy = max(0, min(ay1, by1) - max(a[1], b[1]))
            u = a[2] * a[3] + b[2] * b[3] - ix * iy
            return ix * iy / u if u else 0
        dt = max(1, track[-1]["t"] - track[0]["t"])
        cxs = [(t["bbox"][0] + t["bbox"][2] / 2, t["bbox"][1] + t["bbox"][3] / 2) for t in track]
        out.update(present=True, frames_with_subject=len(track),
                   bbox_first=b0, bbox_last=b1, union_bbox=[min(t["bbox"][0] for t in track), min(t["bbox"][1] for t in track),
                                                            max(t["bbox"][0] + t["bbox"][2] for t in track) - min(t["bbox"][0] for t in track),
                                                            max(t["bbox"][1] + t["bbox"][3] for t in track) - min(t["bbox"][1] for t in track)],
                   height_change=round(b1[3] / max(1, b0[3]), 3),
                   direction=("receding" if b1[3] < 0.95 * b0[3] else "approaching" if b1[3] > 1.05 * b0[3] else "lateral/steady"),
                   centroid_speed_px_per_frame=round(float(np.hypot(cxs[-1][0] - cxs[0][0], cxs[-1][1] - cxs[0][1]) / dt), 2),
                   flow_speed_px_per_frame=(round(float(np.median(speeds)), 2) if speeds else None),
                   first_last_iou=round(float(iou(b0, b1)), 3),
                   clean_plate_from_plate=bool(iou(b0, b1) < 0.05))
    else:
        out.update(present=bool(people), frames_with_subject=0)
    return out, coverage


def _rise_width(g, ys, xs, gxn, gyn, k=8.0):
    """10-90% rise distance of the edge profile along its gradient. Returns widths and a mask of
    clean steps (flat both ends, monotonic), so texture and line crossings are dropped."""
    offs = np.arange(-k, k + 0.01, 0.25, dtype=np.float32)
    X = (xs[:, None] + gxn[:, None] * offs[None, :]).astype(np.float32)
    Y = (ys[:, None] + gyn[:, None] * offs[None, :]).astype(np.float32)
    P = cv2.remap(g, X, Y, cv2.INTER_LINEAR)
    lo_, hi_ = P[:, :4].mean(1, keepdims=True), P[:, -4:].mean(1, keepdims=True)
    C = (hi_ - lo_).ravel()
    n = (P - lo_) / np.maximum(1e-3, hi_ - lo_)
    w = (np.argmax(n >= 0.9, axis=1) - np.argmax(n >= 0.1, axis=1)) * 0.25
    flat = (P[:, :6].std(1) < 0.08 * np.abs(C)) & (P[:, -6:].std(1) < 0.08 * np.abs(C))
    mono = (np.diff(n, axis=1) > -0.05).all(1)
    return w, (C > 15) & flat & mono


# extra 10-90 width (in quadrature over the lens) per px of box motion blur, for a Gaussian lens:
# 0.76 across L = 1..6 px (computed numerically, sigma 1); used to turn width into blur length
RISE_PER_BLUR = 0.76


def analyze_shutter(stack, scale, fps, shifts=None):
    """Motion blur = how much wider moving edges are (along their motion) than static edges of
    similar objects nearby. Needs movers whose per-frame motion is at least their edge width."""
    n = len(stack)
    if n < 4:
        return dict(measured=False, assumed_deg=180, note="too few frames")
    if shifts is not None:
        h, w = stack[0].shape
        stack = [cv2.warpAffine(g, np.float32([[1, 0, -shifts[t][0]], [0, 1, -shifts[t][1]]]), (w, h),
                                flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE) if t < len(shifts) else g
                 for t, g in enumerate(stack)]
    bg = np.median(np.stack([stack[i] for i in np.linspace(0, n - 1, min(n, 31)).astype(int)]), 0).astype(np.float32)
    ts = np.linspace(2, n - 3, min(8, n - 4)).astype(int)
    wA, vA, wS = [], [], []
    for t in ts:
        g0 = stack[t]
        fl = 0.5 * (cv2.calcOpticalFlowFarneback(g0, stack[t + 1], None, 0.5, 4, 21, 5, 7, 1.5, 0) +
                    cv2.calcOpticalFlowFarneback(stack[t - 1], g0, None, 0.5, 4, 21, 5, 7, 1.5, 0))
        g = g0.astype(np.float32)
        gs = cv2.GaussianBlur(g, (0, 0), 0.7)
        gx, gy = cv2.Sobel(gs, cv2.CV_32F, 1, 0), cv2.Sobel(gs, cv2.CV_32F, 0, 1)
        gm = np.hypot(gx, gy)
        v = np.hypot(fl[..., 0], fl[..., 1])
        fg = cv2.dilate((np.abs(g - bg) > 20).astype(np.uint8), np.ones((7, 7), np.uint8))
        can = cv2.Canny(g0, 30, 90) > 0
        ys, xs = np.nonzero((v > 1.0) & (fg > 0) & can & (gm > 20))
        if len(ys) >= 20:
            gxn, gyn = gx[ys, xs] / gm[ys, xs], gy[ys, xs] / gm[ys, xs]
            vm = v[ys, xs]
            c = np.abs(gxn * fl[ys, xs, 0] + gyn * fl[ys, xs, 1]) / vm
            wd, ok = _rise_width(g, ys.astype(np.float32), xs.astype(np.float32), gxn, gyn)
            sel = ok & (c > 0.85)
            wA.append(wd[sel]); vA.append(vm[sel])
        # lens reference: clean static edges within ~60 px of the movers (similar depth, same lens)
        ring = (cv2.dilate(fg, np.ones((121, 121), np.uint8)) > 0) & ~(cv2.dilate(fg, np.ones((9, 9), np.uint8)) > 0) & (v < 0.5)
        ys2, xs2 = np.nonzero(ring & can & (gm > 20))
        if len(ys2) >= 20:
            wd2, ok2 = _rise_width(g, ys2.astype(np.float32), xs2.astype(np.float32),
                                   gx[ys2, xs2] / gm[ys2, xs2], gy[ys2, xs2] / gm[ys2, xs2])
            wS.append(wd2[ok2])
    nA = sum(len(x) for x in wA); nS = sum(len(x) for x in wS)
    if nA < 100 or nS < 50:
        return dict(measured=False, assumed_deg=180, moving_edge_samples=nA, static_edge_samples=nS,
                    note="not enough clean moving and static edges to separate motion blur from lens softness; "
                         "assume 180 deg unless the camera report says otherwise")
    WA, V, WS = np.concatenate(wA), np.concatenate(vA), np.concatenate(wS)
    wa, ws, vmed = float(np.median(WA)), float(np.median(WS)), float(np.median(V))
    base = dict(moving_edge_samples=nA, static_edge_samples=nS, median_motion_px_per_frame=round(vmed * scale, 2),
                rise_moving_px=round(wa * scale, 2), rise_static_px=round(ws * scale, 2),
                method="10-90%% rise of clean step edges: moving edges (gradient along the flow) vs static edges within "
                       "60 px of the movers; blur = sqrt(moving^2 - static^2) / %.2f; shutter = blur / motion" % RISE_PER_BLUR)
    if vmed < max(3.0, 0.75 * ws):
        base.update(measured=False, assumed_deg=180,
                    note="movers too slow for their softness (%.1f px/frame vs %.1f px edge rise): blur cannot be "
                         "separated from lens softness. Assume 180 deg unless the camera report says otherwise"
                         % (vmed * scale, ws * scale))
        return base
    blur = math.sqrt(max(0.0, wa * wa - ws * ws)) / RISE_PER_BLUR
    f = blur / vmed
    deg = 360 * f
    ok = 45 <= deg <= 360
    base.update(measured=True, blur_px=round(blur * scale, 2), shutter_fraction=round(f, 3), shutter_deg_estimate=round(deg, 0),
                exposure_s=(round(f / fps, 5) if fps else None), plausible=ok,
                confidence="low" if (not ok or nA < 500) else "medium",
                consistent_with_180=bool(120 <= deg <= 240),
                note="self-test accuracy about +-20% (read 149 for a true 180); treat as a band, not a value",
                recommend_deg=(180 if 120 <= deg <= 240 else int(round(deg / 45.0) * 45) if ok else 180))
    return base


def analyze_ca(rgb_native, excl_native=None):
    h, w, _ = rgb_native.shape
    T = 96
    cx, cy = w / 2, h / 2
    rmax = math.hypot(cx, cy)
    G = rgb_native[..., 1]
    gm = np.hypot(cv2.Sobel(G, cv2.CV_32F, 1, 0), cv2.Sobel(G, cv2.CV_32F, 0, 1))
    win = cv2.createHanningWindow((T, T), cv2.CV_32F)
    rows = []
    for y in range(0, h - T, T // 2):
        for x in range(0, w - T, T // 2):
            if gm[y:y + T, x:x + T].mean() < 0.15:
                continue
            if rgb_native[y:y + T, x:x + T].max() > 1.0:
                continue      # skip clipped tiles: channel clipping fakes misregistration
            tc = (x + T / 2 - cx, y + T / 2 - cy)
            r = math.hypot(*tc)
            u = (tc[0] / (r + 1e-9), tc[1] / (r + 1e-9))
            res = []
            for c in (0, 2):
                ch = rgb_native[y:y + T, x:x + T, c]
                gch = np.hypot(cv2.Sobel(ch, cv2.CV_32F, 1, 0), cv2.Sobel(ch, cv2.CV_32F, 0, 1))
                (dx, dy), resp = cv2.phaseCorrelate(gm[y:y + T, x:x + T].astype(np.float32), gch.astype(np.float32), win)
                res.append((dx, dy, resp))
            if min(res[0][2], res[1][2]) < 0.25:
                continue
            rows.append(dict(x=x, y=y, r=r / rmax, ux=u[0], uy=u[1], R=res[0][:2], B=res[1][:2]))
    if len(rows) < 8:
        return dict(measured=False, note="too few high-contrast tiles"), []
    Rx = np.array([r_["R"][0] for r_ in rows]); Ry = np.array([r_["R"][1] for r_ in rows])
    Bx = np.array([r_["B"][0] for r_ in rows]); By = np.array([r_["B"][1] for r_ in rows])
    ux = np.array([r_["ux"] for r_ in rows]); uy = np.array([r_["uy"] for r_ in rows]); rr = np.array([r_["r"] for r_ in rows])
    # constant offsets (chroma siting / subsampling) removed, then radial component vs radius
    out = {"method": "phase correlation of R and B gradient magnitude against G in 96 px native tiles; "
                     "constant offset (chroma siting) removed; radial shift regressed on radius and reported at the corner"}
    for nm, X, Yv in (("R", Rx, Ry), ("B", Bx, By)):
        X0, Y0 = np.median(X), np.median(Yv)
        rad = (X - X0) * ux + (Yv - Y0) * uy
        k = float(np.sum(rad * rr) / np.sum(rr * rr))
        out[nm] = dict(constant_offset_px=[round(float(X0), 3), round(float(Y0), 3)],
                       radial_at_corner_px=round(k, 3), spread_px=round(float(np.std(rad)), 3))
    out["tiles"] = len(rows)
    out["ca_px_corner"] = round(max(abs(out["R"]["radial_at_corner_px"]), abs(out["B"]["radial_at_corner_px"])), 3)
    out["ca_present"] = bool(out["ca_px_corner"] > TH["ca_px"])
    out["confidence"] = "medium" if len(rows) > 30 else "low"
    return out, rows


def analyze_bloom(rgb, blobs, excl_all):
    """Radial falloff of display-linear luminance around each bright source."""
    Y = to_lin(luma(rgb))
    h, w = Y.shape
    res = []
    for b in blobs[:4]:
        x, y, bw, bh = b["bbox"]
        m = np.zeros((h, w), np.uint8)
        m[y:y + bh, x:x + bw] = 1
        if b.get("mask") is not None:
            m = b["mask"].astype(np.uint8)
        dist = cv2.distanceTransform(1 - m, cv2.DIST_L2, 5)
        other = excl_all & (m == 0) & (dist > 3)
        core = float(np.percentile(Y[m > 0], 90)) if (m > 0).any() else 0
        dists = [2, 4, 8, 16, 32, 64, 128]
        prof = []
        bkg_m = (dist > 160) & (dist < 220) & ~other
        if bkg_m.sum() < 100:
            continue
        bkg = float(np.median(Y[bkg_m]))
        for d in dists:
            ring = (dist > d * 0.75) & (dist <= d * 1.25) & ~other
            if ring.sum() < 20:
                continue
            prof.append((d, float(np.median(Y[ring]) - bkg)))
        if len(prof) < 4 or core <= 0:
            continue
        e0 = prof[0][1]
        r50 = next((d for d, e in prof if e < 0.5 * e0), None)
        r10 = next((d for d, e in prof if e < 0.1 * e0), None)
        res.append(dict(source=b.get("label", "source"), centroid=b["centroid"], core_linear=round(core, 4),
                        background_linear=round(bkg, 4),
                        excess_profile=[[d, round(e / core, 5)] for d, e in prof],
                        near_excess_ratio=round(e0 / core, 4), r50_px=r50, r10_px=r10,
                        blooms=bool(e0 / core > 0.05 and (r50 or 0) >= 4)))
    return dict(method="median display-linear luminance in rings at 2-128 px from each source mask minus the "
                       "160-220 px ring, as a share of the source core. Scene structure leaks in: read with the overlay.",
                sources=res, confidence="low")


def analyze_ghosts(rgb, sources):
    h, w, _ = rgb.shape
    Y = luma(rgb)
    k = 41
    th = cv2.morphologyEx(Y.astype(np.float32), cv2.MORPH_TOPHAT, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k)))
    out = []
    for s in sources[:6]:
        if math.hypot(s["centroid"][0] - w / 2, s["centroid"][1] - h / 2) < 0.3 * math.hypot(w / 2, h / 2):
            continue     # mirror lands near the source or on its floor reflection (symmetric sets)
        mx, my = w - s["centroid"][0], h - s["centroid"][1]
        x0, x1 = int(max(0, mx - 30)), int(min(w, mx + 30)); y0, y1 = int(max(0, my - 30)), int(min(h, my + 30))
        if x1 - x0 < 10 or y1 - y0 < 10:
            continue
        ex = float(th[y0:y1, x0:x1].max())
        out.append(dict(source=s["centroid"], mirror=[round(mx), round(my)], tophat_at_mirror=round(ex, 3),
                        possible_ghost=bool(ex > 0.08)))
    return dict(method="top-hat brightness at the point mirrored through frame centre from each source "
                       "(where lens ghosts land). Weak test: confirm by eye.", checks=out,
                tested=len(out), any_possible=bool(any(o["possible_ghost"] for o in out)))


# ---------------------------------------------------------------- drawing
def draw_overlay(img, persp_vps, clipmask, practicals, streaks, panels, subj, distl, ca_rows, scale_an, w_an):
    o = (np.clip(img, 0, 1) ** 1.0 * 255).astype(np.uint8)[..., ::-1].copy()
    h, w = o.shape[:2]
    red = np.zeros_like(o); red[..., 2] = 255
    cm = clipmask.astype(bool)
    o[cm] = (0.45 * o[cm] + 0.55 * red[cm]).astype(np.uint8)
    for vp in persp_vps[:2]:
        for s in vp["segs"][:200]:
            cv2.line(o, (int(s[0]), int(s[1])), (int(s[2]), int(s[3])), (0, 255, 0), 1, cv2.LINE_AA)
        cv2.drawMarker(o, (int(vp["x"]), int(vp["y"])), (0, 255, 0), cv2.MARKER_CROSS, 40, 3)
        cv2.line(o, (0, int(vp["y"])), (w, int(vp["y"])), (0, 200, 0), 1, cv2.LINE_AA)
    for p in panels:
        x, y, ww, hh = p["bbox"]
        cv2.rectangle(o, (x, y), (x + ww, y + hh), (255, 128, 0), 2)
        cv2.putText(o, "dark %.2f" % p["mean_luma"], (x + 4, y + 22), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 160, 0), 2)
    for i, p in enumerate(practicals[:10]):
        x, y, ww, hh = p["bbox"]
        col = (0, 0, 255) if p["clipped_frac"] >= 0.02 else (0, 255, 255)
        cv2.rectangle(o, (x - 2, y - 2), (x + ww + 2, y + hh + 2), col, 2)
        cv2.putText(o, "P%d %.3f%s" % (i, p["peak_max_rgb"], " CLIP" if p["clipped_frac"] >= 0.02 else ""),
                    (x, max(15, y - 6)), cv2.FONT_HERSHEY_SIMPLEX, 0.55, col, 2)
    for s in streaks[:14]:
        x, y, ww, hh = s["bbox"]
        col = (255, 255, 0) if s["likely_reflection"] else (120, 120, 60)
        cv2.rectangle(o, (x, y), (x + ww, y + hh), col, 2 if s["likely_reflection"] else 1)
        if s["likely_reflection"]:
            cv2.putText(o, "refl %.1f:1" % s["aspect"], (x, y + hh + 18), cv2.FONT_HERSHEY_SIMPLEX, 0.55, col, 2)
    for t in subj.get("track", []):
        x, y, ww, hh = [int(v / scale_an) for v in t["bbox"]]
        cv2.rectangle(o, (x, y), (x + ww, y + hh), (255, 0, 255), 1)
    for d in distl:
        cv2.line(o, (int(d["x1"]), int(d["y1"])), (int(d["x2"]), int(d["y2"])), (0, 140, 255), 2)
    for r in ca_rows:
        x, y = int(r["x"] / scale_an), int(r["y"] / scale_an)
        cv2.circle(o, (x + int(48 / scale_an), y + int(48 / scale_an)), 3, (200, 200, 200), -1)
    cv2.putText(o, "green: VP lines/horizon  red: clipped  yellow: practicals (red box = clipped)  cyan: floor streaks  "
                   "blue: dark panels  magenta: subject  orange: distortion lines  grey dots: CA tiles",
                (10, h - 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    return o


def plot_curve(title, xs, ys, size=(640, 360), xlabel="", ylabel="", hline=None):
    W, H = size
    im = np.full((H, W, 3), 24, np.uint8)
    cv2.putText(im, title, (10, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
    if not xs:
        cv2.putText(im, "no data", (W // 2 - 40, H // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (180, 180, 180), 1)
        return im
    x0, x1 = min(xs), max(xs); y0, y1 = min(ys + ([hline] if hline is not None else [])), max(ys + ([hline] if hline is not None else []))
    if y1 - y0 < 1e-9: y1 = y0 + 1
    if x1 - x0 < 1e-9: x1 = x0 + 1
    def P(x, y):
        return int(50 + (x - x0) / (x1 - x0) * (W - 70)), int(H - 40 - (y - y0) / (y1 - y0) * (H - 80))
    pts = [P(x, y) for x, y in zip(xs, ys)]
    for a, b in zip(pts, pts[1:]):
        cv2.line(im, a, b, (0, 220, 255), 2, cv2.LINE_AA)
    for p in pts:
        cv2.circle(im, p, 3, (0, 220, 255), -1)
    if hline is not None:
        cv2.line(im, P(x0, hline), P(x1, hline), (120, 120, 120), 1)
    cv2.putText(im, "%s  [%.3g .. %.3g]" % (xlabel, x0, x1), (50, H - 12), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (200, 200, 200), 1)
    cv2.putText(im, "%s  [%.3g .. %.3g]" % (ylabel, y0, y1), (10, 46), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (200, 200, 200), 1)
    return im


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("plate")
    ap.add_argument("--out")
    ap.add_argument("--max-frames", type=int, default=240)
    ap.add_argument("--start", type=float)
    ap.add_argument("--dur", type=float)
    a = ap.parse_args()
    t0 = time.time()
    info = probe(a.plate)
    name = os.path.splitext(os.path.basename(a.plate))[0]
    out = a.out or os.path.join(os.getcwd(), "plate_analysis_" + re.sub(r"[^A-Za-z0-9_-]+", "_", name))
    os.makedirs(out, exist_ok=True)
    W, H, bd = info["width"], info["height"], info["bit_depth"]
    scale = max(1.0, W / ANALYSIS_W)
    aw, ah = int(round(W / scale)), int(round(H / scale))
    nfr = info["frames"] or 1
    stride = max(1, math.ceil(nfr / a.max_frames))
    kidx = set(np.linspace(0, max(0, nfr - 1), 9).astype(int).tolist())
    kr, kb = matrix_coeffs(info["color_space"])

    ycode_hist = np.zeros(1 << bd if not info["is_rgb"] else 1, np.int64)
    edges = np.linspace(-0.1, 1.2, 1301)
    rgb_hist = np.zeros((3, 1300), np.int64)
    noise = NoiseAcc()
    stack, keyframes, kf_ids, means = [], [], [], []
    mid_native = None
    lo = hi = None
    i = 0
    for ycode, rgb in decode(info, a.start, a.dur):
        if ycode is not None:
            ycode_hist += np.bincount(np.clip(ycode.round().astype(np.int64), 0, (1 << bd) - 1).ravel(),
                                      minlength=1 << bd)
        for c in range(3):
            rgb_hist[c] += np.histogram(rgb[..., c], bins=edges)[0]
        noise.add(rgb)
        if i == nfr // 2 or (mid_native is None and i >= nfr // 2):
            mid_native = rgb.copy()
        if i % stride == 0:
            small = cv2.resize(rgb, (aw, ah), interpolation=cv2.INTER_AREA) if scale > 1 else rgb
            Yl = luma(small, kr, kb)
            if lo is None:
                lo, hi = np.percentile(Yl, 0.5), np.percentile(Yl, 99.5)
                hi = max(hi, lo + 0.05)
            stack.append(np.clip((Yl - lo) / (hi - lo) * 255, 0, 255).astype(np.uint8))
            means.append(float(Yl.mean()))
        if i in kidx:
            keyframes.append(cv2.resize(rgb, (aw, ah), interpolation=cv2.INTER_AREA) if scale > 1 else rgb.copy())
            kf_ids.append(i)
        i += 1
    nread = i
    if nread == 0:
        sys.exit("no frames decoded")
    if mid_native is None:
        mid_native = rgb
    rng = np.random.default_rng(7)

    # format block
    fmt = dict(info)
    fmt["frames_decoded"] = nread
    fmt["analysis_scale"] = scale
    if ycode_hist.size > 1:
        tot = ycode_hist.sum()
        cum = np.cumsum(ycode_hist) / tot
        s8 = 2 ** (bd - 8)
        fmt["luma_codes"] = dict(min=int(np.nonzero(ycode_hist)[0][0]), max=int(np.nonzero(ycode_hist)[0][-1]),
                                 legal_black=int(16 * s8), legal_white=int(235 * s8),
                                 share_below_black=round(float(cum[16 * s8 - 1]), 6),
                                 share_above_white=round(float(1 - cum[235 * s8]), 6),
                                 p0_1=int(np.searchsorted(cum, 0.001)), p1=int(np.searchsorted(cum, 0.01)),
                                 p99_9=int(np.searchsorted(cum, 0.999)))
    missing = [k for k in ("color_primaries", "color_transfer", "color_space", "color_range") if info[k] in ("unknown", None)]
    fmt["missing_color_tags"] = missing
    fmt["display_referred"] = info["color_transfer"] not in ("linear",)

    # camera
    cam = analyze_camera(stack, scale)

    # clean frame: temporal median of key frames when the camera holds still, else the middle key frame
    if cam["classification"] in ("locked", "2d_drift") and len(keyframes) >= 5:
        clean = np.median(np.stack(keyframes), axis=0).astype(np.float32)
        clean_src = "temporal median of %d key frames" % len(keyframes)
    else:
        clean = keyframes[len(keyframes) // 2]
        clean_src = "middle key frame (camera moves)"
    Yc = luma(clean, kr, kb)

    # clipping
    cl = clip_levels(rgb_hist, edges)
    clipmask = np.zeros(Yc.shape, bool)
    for ci, nm in enumerate("RGB"):
        if cl.get(nm, {}).get("plateau"):
            clipmask |= clean[..., ci] >= cl[nm]["ceiling"] - TH["clip_band"]
    clipmask = cv2.morphologyEx(clipmask.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)).astype(bool)
    comps, lab = components(clipmask, max(12, int(1e-5 * aw * ah)))
    clip_regions = []
    for c in comps:
        reg = lab == c["id"]
        chans = [nm for ci, nm in enumerate("RGB") if cl.get(nm, {}).get("plateau") and
                 (clean[..., ci][reg] >= cl[nm]["ceiling"] - TH["clip_band"]).mean() > 0.5]
        clip_regions.append(dict(bbox=[int(c["x"] * scale), int(c["y"] * scale), int(c["w"] * scale), int(c["h"] * scale)],
                                 area_frac=round(c["area"] / (aw * ah), 5), centroid=[round(c["cx"] * scale, 1), round(c["cy"] * scale, 1)],
                                 channels=chans, label_id=c["id"]))
    clip_regions.sort(key=lambda r: -r["area_frac"])
    clipping = dict(method="per-channel histogram over all frames; a clip plateau is >= %.2f%% of pixels in the top 4 "
                           "bins at a level >= %.2f; regions = connected components on the clean frame" %
                           (100 * TH["clip_plateau_frac"], TH["clip_min_level"]),
                    channels=cl, regions=[{k: v for k, v in r.items() if k != "label_id"} for r in clip_regions[:10]],
                    clipped_area_frac=round(float(clipmask.mean()), 5), any_clipped=bool(clipmask.any()))

    # tone: black floor from all frames
    cum = np.cumsum(rgb_hist.sum(0)) / rgb_hist.sum()
    def lvl(p): return float(edges[np.searchsorted(cum, p)])
    Yhist_floor = None
    if "luma_codes" in fmt:
        s8 = 2 ** (bd - 8)
        lc = fmt["luma_codes"]
        Yhist_floor = dict(p0_1=round((lc["p0_1"] - 16 * s8) / (219 * s8), 4), p1=round((lc["p1"] - 16 * s8) / (219 * s8), 4),
                           p0_1_code=lc["p0_1"], p1_code=lc["p1"])
    dark = Yc <= np.percentile(Yc, 0.5)
    dark_rgb = clean[dark].mean(0)
    nb_m = (Yc > np.percentile(Yc, 1)) & (Yc <= np.percentile(Yc, 5))
    nb_rgb = clean[nb_m].mean(0)
    ys_, xs_ = np.nonzero(dark)
    black = dict(method="luma percentiles over all frames (codes) + mean colour of the darkest 0.5% of the clean frame",
                 luma=Yhist_floor, rgb_all_frames_p0_1=round(lvl(0.001), 4),
                 darkest_rgb=[round(float(v), 4) for v in dark_rgb], darkest_hex=hexcol(dark_rgb),
                 near_black_rgb_p1_p5=[round(float(v), 4) for v in nb_rgb],
                 near_black_hex=hexcol(nb_rgb), near_black_tint=hue_name(nb_rgb)[0],
                 below_legal_black=bool(Yhist_floor and Yhist_floor["p1"] < -0.005),
                 darkest_linear=[round(float(v), 5) for v in to_lin(dark_rgb)],
                 darkest_location=[round(float(xs_.mean() * scale), 0), round(float(ys_.mean() * scale), 0)],
                 tint=hue_name(dark_rgb)[0] if dark_rgb.max() > 0.01 else "neutral")
    black_p1 = Yhist_floor["p1"] if Yhist_floor else float(np.percentile(Yc, 1))

    # perspective + distortion
    persp, vp, vps = analyze_perspective(Yc, rng)
    dist, distl = analyze_distortion(Yc, scale)
    horizon = vp["y"] if vp else None
    if vp:
        vp_native = dict(x=vp["x"] * scale, y=vp["y"] * scale)
        persp["vp_native_px"] = [round(vp_native["x"], 1), round(vp_native["y"], 1)]

    # subject
    small_scale = 2.0
    stack_small = [cv2.resize(g, (aw // 2, ah // 2), interpolation=cv2.INTER_AREA) for g in stack]
    kf_small = [min(len(stack) - 1, k // stride) for k in kf_ids]
    shifts = None
    if "direct" in cam:
        shifts = [(dx / (small_scale * scale), dy / (small_scale * scale)) for _, dx, dy in cam["direct"]["per_frame"]]
    subj, coverage = analyze_subject(stack_small, cam["classification"], small_scale * scale, kf_small, shifts)
    subj_mask = cv2.resize((coverage > 0).astype(np.uint8), (aw, ah), interpolation=cv2.INTER_NEAREST).astype(bool)
    excl = clipmask | subj_mask
    excl_d = cv2.dilate(excl.astype(np.uint8), np.ones((15, 15), np.uint8)).astype(bool)

    # practicals, streaks, panels
    ceiling = max((v["ceiling"] for v in cl.values() if v.get("ceiling")), default=None) or \
        max((v["max_level"] for v in cl.values()), default=None)
    prac, prac_items = analyze_practicals(clean, clipmask, horizon, scale, ceiling)
    sources = [p for p in prac_items if p["above_horizon"]]
    st, streaks = analyze_streaks(clean, horizon, sources, scale, (vp["x"], vp["y"]) if vp else None, subj_mask)
    panels = analyze_dark_panels(clean, black_p1, horizon, subj_mask)

    # haze, palette, sharpness
    haze = analyze_haze(clean, vp, excl_d, panels["candidates"])
    pal = analyze_palette(clean, excl_d)
    sharp, heat = analyze_sharpness(Yc.astype(np.float32), vp, excl_d)

    # grain
    grain = noise.result(bd)
    grain["temporal_valid"] = cam["classification"] in ("locked", "2d_drift")
    gb = grain["bands"]
    if gb and any(v.get("below_one_code") for v in gb.values()):
        grain["temporal_valid"] = False
        grain["note"] = ("frame-to-frame noise is below one code value in some bands (8-bit and/or heavy "
                         "compression smoothed it away): use the spatial estimate and match texture by eye")
    grain["spatial"] = spatial_noise(mid_native)
    gb = grain["bands"]
    if gb:
        mids = gb.get("mids") or next(iter(gb.values()))
        grain["strongest_channel_mids"] = max("RGB", key=lambda c: mids[c])
        if "shadows" in gb and "mids" in gb:
            grain["shadow_to_mid_ratio_Y"] = round(gb["shadows"]["Y"] / max(1e-6, gb["mids"]["Y"]), 2)

    # motion blur / shutter, CA, bloom, ghosts, flicker
    shutter = analyze_shutter(stack, scale, info["fps"] / stride,
                              [(dx / scale, dy / scale) for _, dx, dy in cam["direct"]["per_frame"]] if "direct" in cam else None)
    ca, ca_rows = analyze_ca(mid_native)
    blobs = []
    for r in clip_regions[:2]:
        m = (lab == r["label_id"])
        blobs.append(dict(label="clipped region", bbox=[int(v / scale) for v in r["bbox"]],
                          centroid=r["centroid"], mask=m))
    for p in sources[:3]:
        if p["clipped_frac"] < 0.5:
            blobs.append(dict(label="practical %s" % p["core_hex"], bbox=p["bbox"], centroid=p["centroid"], mask=None))
    allbright = (clean.max(2) > 0.85) | clipmask
    bloom = analyze_bloom(clean, blobs, allbright)
    ghosts = analyze_ghosts(clean, sources + [dict(centroid=[r["centroid"][0] / scale, r["centroid"][1] / scale]) for r in clip_regions[:2]])
    # Global flicker/exposure vs local light change: tile the static pixels, follow each tile's
    # brightness relative to its own average; the median across tiles is the global factor.
    stat = ~cv2.dilate(subj_mask.astype(np.uint8), np.ones((31, 31), np.uint8)).astype(bool) & ~clipmask
    gh, gw = 4, 6
    th_, tw_ = ah // gh, aw // gw
    tiles = []
    for j in range(gh):
        for i in range(gw):
            sl = (slice(j * th_, (j + 1) * th_), slice(i * tw_, (i + 1) * tw_))
            if stat[sl].mean() > 0.6:
                tiles.append((sl, stat[sl]))
    if len(tiles) >= 6:
        lum = np.array([[float((g[sl].astype(np.float32)[m] / 255 * (hi - lo) + lo).mean()) for sl, m in tiles] for g in stack])
        lum = np.maximum(lum, 1e-4)
        rel = lum / lum.mean(0, keepdims=True)
        glob = np.median(rel, 1)
        # flicker = frame-to-frame wobble around a 7-sample moving average; slow light/exposure
        # changes go to the ramp instead (beats slower than ~1 Hz read as a ramp, not flicker)
        k7 = min(7, len(glob) if len(glob) % 2 else len(glob) - 1)
        smooth = np.convolve(np.pad(glob, k7 // 2, mode="edge"), np.ones(k7) / k7, "valid")
        resid = glob - smooth
        e = max(1, len(glob) // 8)
        local = rel / glob[:, None]
        tile_change = local[-e:].mean(0) - local[:e].mean(0)
        lit = lum.mean(0) >= 0.05          # relative change on near-black tiles is noise, skip them
        tile_change = np.where(lit, tile_change, 0)
        flick = dict(method="static pixels in a 6x4 tile grid (subject, its surroundings and clipped areas excluded); "
                            "global factor = median tile brightness relative to its own mean; local = tiles vs global",
                     std_pct=round(float(100 * resid.std()), 3),
                     exposure_ramp_pct=round(float(100 * (smooth[-e:].mean() - smooth[:e].mean())), 2),
                     exposure_swing_pct=round(float(100 * (smooth.max() - smooth.min())), 2),
                     local_change_pct=round(float(100 * np.max(np.abs(tile_change))), 2),
                     local_change_tiles=int(np.sum(np.abs(tile_change) > 0.05)), tiles=len(tiles),
                     changed_tiles=[dict(bbox_native=[round(sl[1].start * scale), round(sl[0].start * scale),
                                                      round(tw_ * scale), round(th_ * scale)],
                                         change_vs_global_pct=round(float(100 * c), 1),
                                         start_luma=round(float(lum[:e, t].mean()), 4), end_luma=round(float(lum[-e:, t].mean()), 4))
                                    for t, ((sl, _), c) in enumerate(zip(tiles, tile_change)) if abs(c) > 0.05])
        flick["local_light_change"] = bool(flick["local_change_pct"] > 5.0)
    else:
        m_arr = np.array(means)
        flick = dict(method="frame-mean luma over the whole frame (no static mask available: movers included)",
                     std_pct=round(float(100 * m_arr.std() / max(1e-6, m_arr.mean())), 3))
    flick["flicker"] = bool(flick["std_pct"] > TH["flicker_pct"])
    flick["exposure_change"] = bool(abs(flick.get("exposure_ramp_pct", 0)) > 3 or flick.get("exposure_swing_pct", 0) > 3)

    # flags (deterministic summary the skill maps to recommendations)
    flags = dict(
        camera=cam["classification"],
        perspective=(("%d-VP" % len(persp.get("vanishing_points", []))) +
                     (" + converging verticals" if persp.get("verticals", {}).get("converging") else "")
                     if persp.get("vanishing_points") else "unknown"),
        distortion_likely=dist.get("distortion_likely"),
        clipped_regions=len(clip_regions), energy_reference=("unclipped practical" if prac["brightest_unclipped_source"] else "none unclipped"),
        gloss_floor=st["gloss_present"], dark_panel_candidates=len(panels["candidates"]),
        haze=haze.get("haze_present"), subject=subj.get("present"),
        clean_plate_from_plate=subj.get("clean_plate_from_plate"),
        far_soft=sharp.get("far_soft"), ca=ca.get("ca_present"),
        practical_bloom=any(s["blooms"] for s in bloom["sources"]) if bloom["sources"] else None,
        possible_ghosts=ghosts["any_possible"], flicker=flick["flicker"], exposure_change=flick.get("exposure_change"),
        local_light_change=flick.get("local_light_change"), low_key=panels.get("low_key"),
        low_saturation=pal["low_saturation"], teal_orange=pal["teal_orange"], cool_cast=pal["overall_cool_cast"],
        shutter_deg=(shutter.get("recommend_deg", 180)),
    )

    result = dict(tool="analyze_plate.py " + VERSION, analysed_at=time.strftime("%Y-%m-%d %H:%M"),
                  thresholds=TH, format=fmt, camera=cam, perspective={k: v for k, v in persp.items()},
                  lens_distortion=dist, clipping=clipping, black_floor=black, practicals=prac,
                  floor_gloss=st, dark_panels=panels, haze=haze, palette=pal, sharpness_dof=sharp,
                  grain=grain, motion_blur=shutter, chromatic_aberration=ca, practical_bloom=bloom,
                  ghosts=ghosts, flicker=flick, subject=subj, clean_frame_source=clean_src,
                  key_frames=kf_ids, flags=flags,
                  coordinate_note="bbox/centroid values in practicals, streaks, dark panels and the overlay are in "
                                  "analysis pixels (scale %.3g); clipping regions, subject boxes, VP 'vp_native_px' "
                                  "and all *_px lengths are native pixels" % scale)
    for vp_ in result["perspective"].get("vanishing_points", []):
        vp_.pop("segs", None)
    with open(os.path.join(out, "plate_analysis.json"), "w") as f:
        json.dump(result, f, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))

    # images
    sheet = []
    for img, fid in zip(keyframes, kf_ids):
        t = cv2.resize((np.clip(img, 0, 1) * 255).astype(np.uint8)[..., ::-1], (640, int(640 * ah / aw)))
        cv2.putText(t, "f%d  %.2fs" % (fid, fid / max(1e-6, info["fps"])), (10, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        sheet.append(t)
    while len(sheet) % 3:
        sheet.append(np.zeros_like(sheet[0]))
    rows = [np.hstack(sheet[r:r + 3]) for r in range(0, len(sheet), 3)]
    cv2.imwrite(os.path.join(out, "contact_sheet.jpg"), np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 88])
    ov = draw_overlay(clean, vps, clipmask, prac["items"], st["streaks"], panels["candidates"], subj, distl, ca_rows, scale, aw)
    cv2.imwrite(os.path.join(out, "overlay.jpg"), ov, [cv2.IMWRITE_JPEG_QUALITY, 90])
    # maps
    cov = cv2.resize(coverage, (640, 360)); cov = (255 * cov / max(1, cov.max())).astype(np.uint8)
    cov = cv2.applyColorMap(cov, cv2.COLORMAP_MAGMA)
    cv2.putText(cov, "subject coverage over time", (10, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    hm = heat.copy(); valid = ~np.isnan(hm)
    hmn = np.zeros_like(hm)
    if valid.any():
        hmn[valid] = (hm[valid] - np.nanmin(hm)) / max(1e-6, np.nanmax(hm) - np.nanmin(hm))
    hmi = cv2.applyColorMap((hmn * 255).astype(np.uint8), cv2.COLORMAP_VIRIDIS)
    hmi[~valid] = 30
    hmi = cv2.resize(hmi, (640, 360), interpolation=cv2.INTER_NEAREST)
    cv2.putText(hmi, "sharpness (yellow = sharp, grey = no texture)", (10, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    hp = haze.get("profile", [])
    hz = plot_curve("haze: dark level vs distance from VP (left = far)", [p["r_norm"] for p in hp],
                    [p["dark_p"] for p in hp], xlabel="r from VP (norm)", ylabel="P2 luma")
    bl = bloom["sources"][:1]
    bc = plot_curve("bloom: excess around %s" % (bl[0]["source"] if bl else "-"),
                    [math.log2(d) for d, _ in bl[0]["excess_profile"]] if bl else [],
                    [e for _, e in bl[0]["excess_profile"]] if bl else [], xlabel="log2 px", ylabel="excess/core", hline=0.0)
    cv2.imwrite(os.path.join(out, "maps.jpg"), np.vstack([np.hstack([cov, hmi]), np.hstack([hz, bc])]),
                [cv2.IMWRITE_JPEG_QUALITY, 88])

    # summary
    L = []
    L.append("PLATE  %s" % os.path.basename(a.plate))
    L.append("format  %dx%d %s %s %s %s-bit %s, %s fps, %d frames (%.2fs), tags %s/%s/%s/%s%s" % (
        W, H, info["codec"], info["profile"] or "", info["pix_fmt"], bd, info["chroma"], info["fps"], nread,
        info["duration_s"], info["color_primaries"], info["color_transfer"], info["color_space"], info["color_range"],
        ("  MISSING " + ",".join(missing)) if missing else ""))
    if "luma_codes" in fmt:
        lc = fmt["luma_codes"]
        L.append("codes   Y min %d max %d (legal %d-%d), below black %.4f%%, above white %.4f%%" % (
            lc["min"], lc["max"], lc["legal_black"], lc["legal_white"], 100 * lc["share_below_black"], 100 * lc["share_above_white"]))
    L.append("camera  %s  max drift %.3f px  parallax resid p90 %s px over %s fr" % (
        cam["classification"], cam.get("max_drift_px", -1),
        "%.3f" % cam["parallax"]["resid_p90_px"] if cam.get("parallax", {}).get("resid_p90_px") is not None else "n/a",
        cam.get("parallax", {}).get("baseline_frames")))
    if vp:
        L.append("persp   %s  VP1 native (%.0f, %.0f)  offset from centre (%.0f, %.0f) analysis px  roll %.2f deg" % (
            flags["perspective"], vp["x"] * scale, vp["y"] * scale, *persp["vp_offset_from_center_px"],
            persp.get("roll_deg_estimate") or 0))
        fv = persp.get("focal_from_depth_and_vertical_vp")
        if fv:
            L.append("focal   from depth VP + vertical VP: %.0f px = hFOV %.1f deg (%.1f mm S35 / %.1f mm FF), pitch %.1f deg down, %s confidence" % (
                fv["focal_px"] * scale, fv["hfov_deg"], fv["focal_mm_if_S35"], fv["focal_mm_if_FF"], fv["pitch_deg"], fv["confidence"]))
    L.append("distort %s  edge bow %s +- %s px (%s sigma) from %s off-centre lines" % (
        dist.get("type", "-") if dist.get("distortion_likely") else "not detected",
        dist.get("edge_bow_px", "n/a"), dist.get("edge_bow_sigma_px", "n/a"), dist.get("significance_sigma", "n/a"),
        dist.get("lines_used", 0)) + ("  confidence %s" % dist["confidence"] if dist.get("confidence") else "")
             + ("  NOTE " + dist["note"] if dist.get("note") else ""))
    L.append("clip    %d region(s), %.2f%% of frame; channels %s" % (
        len(clip_regions), 100 * clipping["clipped_area_frac"],
        {k: (v["ceiling"], v["max_level"], v["plateau"]) for k, v in cl.items()}))
    unc = [p for p in prac["items"] if p["above_horizon"] and p["clipped_frac"] < 0.02][:4]
    L.append("energy  ceiling %s; unclipped source candidates (pick the real emitter on the overlay): %s" % (
        ceiling, "; ".join("%s peak %.3f (%.0f%% of ceiling) at %s aspect %.1f" % (
            p["core_hex"], p["peak_max_rgb"], 100 * (p["of_ceiling"] or 0), p["centroid"], p["aspect"]) for p in unc) or "none"))
    L.append("black   luma P0.1 %s P1 %s (codes %s/%s)%s, darkest rgb %s, near-black %s (%s)" % (
        Yhist_floor["p0_1"] if Yhist_floor else "-", Yhist_floor["p1"] if Yhist_floor else "-",
        Yhist_floor["p0_1_code"] if Yhist_floor else "-", Yhist_floor["p1_code"] if Yhist_floor else "-",
        "  BELOW LEGAL BLACK" if black["below_legal_black"] else "", black["darkest_rgb"], black["near_black_hex"],
        black["near_black_tint"]))
    L.append("palette %s  chroma median %.3f ceiling(p99) %s  teal/orange %s  cool cast %s" % (
        {b: (v["hex"], v["hue"]) for b, v in pal["bands"].items()}, pal["chroma_median"], pal["chroma_ceiling_p99"],
        pal["teal_orange"], pal["overall_cool_cast"]))
    L.append("gloss   %s: %d likely reflection streak(s) (%d paired with a source), median aspect %s; dark panel candidates %d %s" % (
        "GLOSSY" if st["gloss_present"] else "possible" if st["gloss_possible"] else "no gloss found",
        st["count"], st["paired_count"], st["median_aspect"], len(panels["candidates"]),
        [(p["bbox"], p["mean_luma"]) for p in panels["candidates"][:3]]))
    L.append("haze    %s" % (("lift %.3f (far %.3f vs near %.3f), far dark %s -> %s" % (
        haze["lift"], haze["far_dark"], haze["near_dark"], haze["far_dark_hex"], "HAZE" if haze["haze_present"] else "no haze"))
        if haze.get("measured") else haze.get("note")))
    if gb:
        L.append("grain   %s  (temporal %s)  autocorr h/v %s/%s" % (
            {b: (v["R"], v["G"], v["B"], v["Y_codes"]) for b, v in gb.items()},
            "valid" if grain["temporal_valid"] else ("INVALID: below 1 code, compression" if grain.get("note") else "INVALID: camera moves; use spatial"),
            grain["autocorr_lag1_h"], grain["autocorr_lag1_v"]))
    if grain["spatial"].get("measured"):
        L.append("grain2  spatial white-equiv sigma %s" % grain["spatial"]["sigma"])
    L.append("subject %s" % (("%s, %d frames, first %s last %s, height x%.2f, first/last IoU %.2f, HOG hits %d" % (
        subj.get("direction"), subj.get("frames_with_subject"), subj.get("bbox_first"), subj.get("bbox_last"),
        subj.get("height_change", 1), subj.get("first_last_iou", 0), len(subj.get("hog_people", []))))
        if subj.get("track") else "no background-subtraction track; HOG hits %d" % len(subj.get("hog_people", []))))
    L.append("shutter %s" % (("~%.0f deg (blur %.2f px / move %.2f px per frame, %d samples, %s)" % (
        shutter["shutter_deg_estimate"], shutter["blur_px"], shutter["median_motion_px_per_frame"],
        shutter["moving_edge_samples"], shutter["confidence"])) if shutter.get("measured") else shutter.get("note")))
    L.append("dof     %s" % (("far/near sharpness %.2f -> %s, focus band %s" % (
        sharp["far_near_ratio"], "FAR SOFT" if sharp["far_soft"] else "even", sharp.get("focus_band")))
        if sharp.get("far_near_ratio") else "n/a"))
    L.append("ca      %s" % (("corner R %.2f px, B %.2f px -> %s" % (ca["R"]["radial_at_corner_px"], ca["B"]["radial_at_corner_px"],
                                                                     "CA" if ca["ca_present"] else "none")) if ca.get("tiles") else ca.get("note")))
    L.append("bloom   %s" % "; ".join("%s r50=%s r10=%s near=%.3f%s" % (b["source"], b["r50_px"], b["r10_px"], b["near_excess_ratio"],
                                                                         " BLOOMS" if b["blooms"] else "") for b in bloom["sources"]))
    L.append("ghosts  %s   flicker %.2f%% frame-to-frame%s  exposure start->end %s%% (swing %s%%)  local light change %s%% (%s tiles >5%%)" % (
        "possible" if ghosts["any_possible"] else "none found", flick["std_pct"], " FLICKER" if flick["flicker"] else "",
        flick.get("exposure_ramp_pct", "-"), flick.get("exposure_swing_pct", "-"),
        flick.get("local_change_pct", "-"), flick.get("local_change_tiles", "-")))
    L.append("outputs %s  (%.1fs)" % (out, time.time() - t0))
    result["summary"] = L
    with open(os.path.join(out, "plate_analysis.json"), "w") as f:
        json.dump(result, f, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else str(o))
    print("\n".join(L))


if __name__ == "__main__":
    main()
