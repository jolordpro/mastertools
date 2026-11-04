#!/usr/bin/env python3
"""fix.py - render "show the fix" variants of an image so the user sees a better version.

Usage:  python3 fix.py image.jpg plan.json --out dir

plan.json:
  {"variants": [{"name": "level + tighter", "ops": [ {"op": "rotate_level", "deg": "auto"}, ... ]}],
   "notes":    [ {"cell": "B3", "label": "highlight pulls the eye"}, ... ]}

Output in --out:
  NN_<name>.jpg     one image per variant (native size of the result)
  annotated.jpg     the original with numbered notes (only if notes exist)
  board.jpg         ORIGINAL | NOTES | variants, long edge <= 2576 px
  fix_report.json   every op applied, with the numbers it used

COORDINATES. All positions are fractions 0-1 of the CURRENT frame (x to the right, y down).
Ops run in order, so put geometry ops (rotate_level, reframe, crop_box) first; every later op
then speaks in the coordinates of the already-cropped frame.

OPS
  rotate_level  {deg}                 deg = degrees counter-clockwise (cv2 convention), or "auto"
                                      (finds the dominant near-horizontal line). Crops to fill, no borders.
  reframe       {ratio, cx, cy, zoom, lead, lead_share, sy}
                                      ratio "16:9" | "4:5" | number (w/h). (cx,cy) = subject point.
                                      zoom >= 1 tightens. lead "left"|"right"|"none": the subject faces/moves
                                      that way, so lead_share (default 0.62) of the crop width is left free
                                      ahead of it. sy = subject height in crop (default 0.5).
  crop_box      {x0,y0,x1,y1}
  burn_region   {cx,cy,r,stops}       soft radial darkening. r = fraction of the short side, stops default 1.
  dodge_region  {cx,cy,r,stops}       soft radial lightening.
  value_curve   {black,white,gamma,s_curve}
                                      levels in display values 0-1; gamma > 1 brightens; s_curve 0-1.
  local_contrast {mask, amount, radius}
                                      mask "ellipse:cx,cy,rx,ry" | "rect:x0,y0,x1,y1" | "png:path"; omit = whole frame.
  desaturate_outside {mask, amount}   keeps color inside the mask, mutes it outside.
  vignette      {amount, softness}
  plate_behind_text {box, color, opacity, text, feather}
                                      scrim behind text. text "auto" (default) keeps the text strokes at their
                                      own color and plates only the background; "none" plates everything.
  move_box      {box, dx, dy}         shift a region (fractions of the frame), fill the hole by OpenCV inpaint.
                                      For flat graphics and layout mocks.

NOTES (drawn on a copy of the original). Each is one of:
  {"cell": "B3"}  or {"cells": ["B3","C3"]}   columns A-D left to right, rows 1-4 top to bottom
  {"box": [x0,y0,x1,y1]}   {"at": [x,y]}   {"from": "A1"|[x,y], "to": "C3"|[x,y]}  (arrow)
  plus "label": "short text". Plain strings are kept in the report only.

Python 3.9, numpy, OpenCV, Pillow only.
"""
import argparse
import json
import math
import os
import re
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

MAX_BOARD = 2576


# ----------------------------------------------------------------------------- helpers
def smoothstep(e0, e1, x):
    t = np.clip((x - e0) / max(e1 - e0, 1e-9), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def to_lin(x):
    return np.where(x <= 0.04045, x / 12.92, ((x + 0.055) / 1.055) ** 2.4).astype(np.float32)


def to_srgb(x):
    x = np.clip(x, 0.0, None)
    return np.where(x <= 0.0031308, x * 12.92, 1.055 * np.power(x, 1 / 2.4) - 0.055).astype(np.float32)


def u8(img):
    return np.clip(img * 255.0 + 0.5, 0, 255).astype(np.uint8)


def parse_color(c):
    """Return BGR float 0-1."""
    names = {"black": (0, 0, 0), "white": (255, 255, 255), "gray": (128, 128, 128), "grey": (128, 128, 128)}
    if c is None:
        rgb = (0, 0, 0)
    elif isinstance(c, str):
        if c.lower() in names:
            rgb = names[c.lower()]
        else:
            m = re.fullmatch(r"#?([0-9a-fA-F]{6})", c.strip())
            if not m:
                raise ValueError("bad color %r" % (c,))
            h = m.group(1)
            rgb = tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    else:
        rgb = tuple(float(v) for v in c[:3])
        if max(rgb) <= 1.0:
            rgb = tuple(v * 255 for v in rgb)
    return np.array([rgb[2], rgb[1], rgb[0]], np.float32) / 255.0


def grid(h, w):
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    return xx + 0.5, yy + 0.5


def parse_mask(spec, h, w, feather=0.25):
    """Float mask 0-1 (h,w). None -> all ones."""
    if spec is None:
        return np.ones((h, w), np.float32)
    kind, _, rest = str(spec).partition(":")
    kind = kind.strip().lower()
    if kind == "ellipse":
        cx, cy, rx, ry = [float(v) for v in rest.split(",")]
        xx, yy = grid(h, w)
        d = np.sqrt(((xx / w - cx) / max(rx, 1e-6)) ** 2 + ((yy / h - cy) / max(ry, 1e-6)) ** 2)
        return (1.0 - smoothstep(1.0 - feather, 1.0 + feather, d)).astype(np.float32)
    if kind == "rect":
        x0, y0, x1, y1 = [float(v) for v in rest.split(",")]
        m = np.zeros((h, w), np.float32)
        m[int(y0 * h):int(math.ceil(y1 * h)), int(x0 * w):int(math.ceil(x1 * w))] = 1.0
        sigma = max(feather * min(h, w) * 0.1, 0.5)
        return cv2.GaussianBlur(m, (0, 0), sigma)
    if kind == "png":
        m = cv2.imread(rest.strip(), cv2.IMREAD_GRAYSCALE)
        if m is None:
            raise ValueError("cannot read mask png %r" % rest)
        return cv2.resize(m, (w, h), interpolation=cv2.INTER_LINEAR).astype(np.float32) / 255.0
    raise ValueError("bad mask %r" % (spec,))


def box_px(box, h, w):
    x0, y0, x1, y1 = [float(v) for v in box]
    X0 = int(np.clip(round(x0 * w), 0, w - 1))
    Y0 = int(np.clip(round(y0 * h), 0, h - 1))
    X1 = int(np.clip(round(x1 * w), X0 + 1, w))
    Y1 = int(np.clip(round(y1 * h), Y0 + 1, h))
    return X0, Y0, X1, Y1


def parse_ratio(r, default):
    if r is None:
        return default
    if isinstance(r, (int, float)):
        return float(r)
    a, _, b = str(r).replace("x", ":").partition(":")
    return float(a) / float(b) if b else float(a)


# ----------------------------------------------------------------------------- ops
def detect_tilt(img):
    """Degrees (image coords, + = line slopes down to the right) of the dominant near-horizontal line."""
    g = cv2.cvtColor(u8(img), cv2.COLOR_BGR2GRAY)
    h, w = g.shape
    s = 1200.0 / max(h, w)
    if s < 1.0:
        g = cv2.resize(g, (int(w * s), int(h * s)), interpolation=cv2.INTER_AREA)
        h, w = g.shape
    g = cv2.GaussianBlur(g, (0, 0), 1.2)
    edges = cv2.Canny(g, 40, 120)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 720, threshold=max(30, int(0.12 * w)),
                            minLineLength=int(0.25 * w), maxLineGap=max(4, int(0.03 * w)))
    if lines is None:
        return None
    angs, wts = [], []
    for x1, y1, x2, y2 in lines[:, 0]:
        a = math.degrees(math.atan2(y2 - y1, x2 - x1))
        if a > 90:
            a -= 180
        if a < -90:
            a += 180
        if abs(a) <= 15:
            angs.append(a)
            wts.append(math.hypot(x2 - x1, y2 - y1))
    if not angs:
        return None
    order = np.argsort(angs)
    angs = np.array(angs)[order]
    wts = np.array(wts)[order]
    cum = np.cumsum(wts)
    return float(angs[np.searchsorted(cum, cum[-1] / 2.0)])


def op_rotate_level(img, p):
    h, w = img.shape[:2]
    deg = p.get("deg", "auto")
    info = {}
    if isinstance(deg, str):
        det = detect_tilt(img)
        if det is None:
            info["note"] = "no near-horizontal line found; left unrotated"
            return img, info
        info["detected_tilt"] = round(det, 3)
        deg = det
    deg = float(deg)
    info["deg_applied"] = round(deg, 3)
    if abs(deg) < 0.01:
        return img, info
    t = math.radians(abs(deg))
    c, s = math.cos(t), math.sin(t)
    fit = min(w / (w * c + h * s), h / (w * s + h * c))
    zoom = 1.0 / fit * 1.006  # small margin against interpolation edge
    M = cv2.getRotationMatrix2D((w / 2.0, h / 2.0), deg, zoom)
    out = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
    info["zoom"] = round(zoom, 4)
    return np.clip(out, 0, 1), info


def op_reframe(img, p):
    h, w = img.shape[:2]
    ratio = parse_ratio(p.get("ratio"), w / float(h))
    cx, cy = float(p.get("cx", 0.5)), float(p.get("cy", 0.5))
    zoom = max(float(p.get("zoom", 1.0)), 1.0)
    lead = str(p.get("lead", "none")).lower()
    share = float(p.get("lead_share", 0.62))
    sy = float(p.get("sy", 0.5))
    if ratio >= w / float(h):
        cw, ch = float(w), w / ratio
    else:
        ch, cw = float(h), h * ratio
    cw, ch = cw / zoom, ch / zoom
    sx = {"right": 1.0 - share, "left": share}.get(lead, 0.5)
    x0 = cx * w - sx * cw
    y0 = cy * h - sy * ch
    x0 = float(np.clip(x0, 0, w - cw))
    y0 = float(np.clip(y0, 0, h - ch))
    X0, Y0 = int(round(x0)), int(round(y0))
    CW, CH = int(round(cw)), int(round(ch))
    CW, CH = min(CW, w - X0), min(CH, h - Y0)
    out = img[Y0:Y0 + CH, X0:X0 + CW]
    info = {"crop_px": [X0, Y0, X0 + CW, Y0 + CH], "size": [CW, CH],
            "subject_pos_in_crop": [round((cx * w - X0) / CW, 3), round((cy * h - Y0) / CH, 3)]}
    return out, info


def op_crop_box(img, p):
    h, w = img.shape[:2]
    X0, Y0, X1, Y1 = box_px([p["x0"], p["y0"], p["x1"], p["y1"]], h, w)
    return img[Y0:Y1, X0:X1], {"crop_px": [X0, Y0, X1, Y1]}


def _radial(img, p, sign):
    h, w = img.shape[:2]
    cx, cy = float(p.get("cx", 0.5)), float(p.get("cy", 0.5))
    r = max(float(p.get("r", 0.25)), 1e-3) * min(h, w)
    stops = abs(float(p.get("stops", 1.0)))
    xx, yy = grid(h, w)
    d = np.sqrt((xx - cx * w) ** 2 + (yy - cy * h) ** 2) / r
    m = 1.0 - smoothstep(0.0, 1.0, d)
    gain = np.power(2.0, sign * stops * m)[..., None]
    out = to_srgb(np.clip(to_lin(img) * gain, 0, 1))
    return out, {"stops": sign * stops, "radius_px": round(r, 1)}


def op_burn_region(img, p):
    return _radial(img, p, -1.0)


def op_dodge_region(img, p):
    return _radial(img, p, +1.0)


def op_value_curve(img, p):
    b, wh = float(p.get("black", 0.0)), float(p.get("white", 1.0))
    gamma = float(p.get("gamma", 1.0))
    s = float(p.get("s_curve", 0.0))
    x = np.clip((img - b) / max(wh - b, 1e-6), 0, 1)
    if gamma != 1.0:
        x = np.power(x, 1.0 / gamma)
    if s:
        x = x + s * (x * x * (3 - 2 * x) - x)
    return np.clip(x, 0, 1).astype(np.float32), {"black": b, "white": wh, "gamma": gamma, "s_curve": s}


def op_local_contrast(img, p):
    h, w = img.shape[:2]
    amount = float(p.get("amount", 0.5))
    radius = float(p.get("radius", 0.04)) * min(h, w)
    m = parse_mask(p.get("mask"), h, w, float(p.get("feather", 0.25)))
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
    L = lab[..., 0]
    blur = cv2.GaussianBlur(L, (0, 0), max(radius, 1.0))
    L2 = np.clip(L + amount * (L - blur) * m, 0, 100)
    lab[..., 0] = L2
    out = cv2.cvtColor(lab, cv2.COLOR_Lab2BGR)
    return np.clip(out, 0, 1), {"amount": amount, "radius_px": round(radius, 1)}


def op_desaturate_outside(img, p):
    h, w = img.shape[:2]
    amount = float(p.get("amount", 0.5))
    if p.get("mask") is None:
        raise ValueError("desaturate_outside needs a mask")
    m = parse_mask(p["mask"], h, w, float(p.get("feather", 0.25)))[..., None]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)[..., None]
    muted = img * (1 - amount) + gray * amount
    return (img * m + muted * (1 - m)).astype(np.float32), {"amount": amount}


def op_vignette(img, p):
    h, w = img.shape[:2]
    amount = float(p.get("amount", 0.3))
    soft = float(p.get("softness", 0.6))
    xx, yy = grid(h, w)
    d = np.sqrt(((xx / w) - 0.5) ** 2 + ((yy / h) - 0.5) ** 2) / math.sqrt(0.5)
    wgt = smoothstep(max(0.0, 1.0 - soft), 1.0, d)
    return np.clip(img * (1 - amount * wgt)[..., None], 0, 1).astype(np.float32), {"amount": amount, "softness": soft}


def op_plate_behind_text(img, p):
    h, w = img.shape[:2]
    X0, Y0, X1, Y1 = box_px(p["box"], h, w)
    col = parse_color(p.get("color", "black"))
    opacity = float(p.get("opacity", 0.7))
    roi = img[Y0:Y1, X0:X1].copy()
    alpha = np.full(roi.shape[:2], opacity, np.float32)
    info = {"box_px": [X0, Y0, X1, Y1], "opacity": opacity}
    feather = float(p.get("feather", 0.0))
    if feather > 0:
        pad = np.pad(alpha, 1, constant_values=0.0)
        k = max(feather * min(h, w), 1.0)
        alpha = cv2.GaussianBlur(pad, (0, 0), k)[1:-1, 1:-1] * 1.0
        alpha = np.minimum(alpha / max(alpha.max(), 1e-6) * opacity, opacity)
    if str(p.get("text", "auto")).lower() == "auto":
        lab = cv2.cvtColor(roi, cv2.COLOR_BGR2Lab)
        bg = np.median(lab.reshape(-1, 3), axis=0)
        dist = np.linalg.norm(lab - bg, axis=2)
        tm = np.clip((dist - 5.0) / 10.0, 0, 1)
        tm = cv2.dilate(tm, np.ones((3, 3), np.uint8))
        alpha = alpha * (1 - tm)
        info["text_kept_fraction"] = round(float((tm > 0.5).mean()), 4)
    out = img.copy()
    out[Y0:Y1, X0:X1] = roi * (1 - alpha[..., None]) + col * alpha[..., None]
    return out, info


def op_move_box(img, p):
    h, w = img.shape[:2]
    X0, Y0, X1, Y1 = box_px(p["box"], h, w)
    dx = int(round(float(p.get("dx", 0)) * w))
    dy = int(round(float(p.get("dy", 0)) * h))
    region = img[Y0:Y1, X0:X1].copy()
    mask = np.zeros((h, w), np.uint8)
    mask[Y0:Y1, X0:X1] = 255
    mask = cv2.dilate(mask, np.ones((5, 5), np.uint8))
    filled = cv2.inpaint(u8(img), mask, 3, cv2.INPAINT_TELEA).astype(np.float32) / 255.0
    # destination, clipped to the frame
    nx0, ny0 = X0 + dx, Y0 + dy
    sx0, sy0 = max(0, -nx0), max(0, -ny0)
    nx0c, ny0c = max(0, nx0), max(0, ny0)
    nx1c, ny1c = min(w, nx0 + (X1 - X0)), min(h, ny0 + (Y1 - Y0))
    if nx1c > nx0c and ny1c > ny0c:
        filled[ny0c:ny1c, nx0c:nx1c] = region[sy0:sy0 + (ny1c - ny0c), sx0:sx0 + (nx1c - nx0c)]
    return filled, {"box_px": [X0, Y0, X1, Y1], "shift_px": [dx, dy]}


OPS = {
    "rotate_level": op_rotate_level,
    "reframe": op_reframe,
    "crop_box": op_crop_box,
    "burn_region": op_burn_region,
    "dodge_region": op_dodge_region,
    "value_curve": op_value_curve,
    "local_contrast": op_local_contrast,
    "desaturate_outside": op_desaturate_outside,
    "vignette": op_vignette,
    "plate_behind_text": op_plate_behind_text,
    "move_box": op_move_box,
}


def apply_ops(img, ops):
    """img float32 BGR 0-1. Returns (img, report list)."""
    report = []
    for op in ops:
        name = op.get("op")
        params = {k: v for k, v in op.items() if k != "op"}
        entry = {"op": name, "params": params}
        fn = OPS.get(name)
        if fn is None:
            entry.update(applied=False, error="unknown op")
        else:
            try:
                img, info = fn(img, params)
                img = np.ascontiguousarray(img, dtype=np.float32)
                entry.update(applied=True, info=info, size=[img.shape[1], img.shape[0]])
            except Exception as e:  # keep going; the report says what failed
                entry.update(applied=False, error="%s: %s" % (type(e).__name__, e))
        report.append(entry)
    return img, report


# ----------------------------------------------------------------------------- annotations
_FONT_PATHS = ["/System/Library/Fonts/Helvetica.ttc", "/System/Library/Fonts/Supplemental/Arial.ttf",
               "/Library/Fonts/Arial.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]


def get_font(size, bold=False):
    for path in _FONT_PATHS:
        if os.path.exists(path):
            try:
                idx = 1 if (bold and path.endswith(".ttc")) else 0
                return ImageFont.truetype(path, size, index=idx)
            except Exception:
                try:
                    return ImageFont.truetype(path, size)
                except Exception:
                    pass
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def cell_box(cell):
    m = re.fullmatch(r"\s*([A-Da-d])\s*([1-4])\s*", str(cell))
    if not m:
        raise ValueError("bad grid cell %r (use A-D and 1-4, e.g. B3)" % (cell,))
    c = "ABCD".index(m.group(1).upper())
    r = int(m.group(2)) - 1
    return [c / 4.0, r / 4.0, (c + 1) / 4.0, (r + 1) / 4.0]


def _pt(v, w, h):
    if isinstance(v, str):
        b = cell_box(v)
        return ((b[0] + b[2]) / 2 * w, (b[1] + b[3]) / 2 * h)
    x, y = float(v[0]), float(v[1])
    if max(abs(x), abs(y)) <= 1.0:
        return (x * w, y * h)
    return (x, y)


def _box(v, w, h):
    vals = [float(a) for a in v]
    if max(vals) <= 1.0:
        return [vals[0] * w, vals[1] * h, vals[2] * w, vals[3] * h]
    return vals


def resolve_note(n, w, h):
    if "cells" in n:
        boxes = [cell_box(c) for c in n["cells"]]
        b = [min(x[0] for x in boxes), min(x[1] for x in boxes), max(x[2] for x in boxes), max(x[3] for x in boxes)]
        return ("box", [b[0] * w, b[1] * h, b[2] * w, b[3] * h])
    if "cell" in n:
        b = cell_box(n["cell"])
        return ("box", [b[0] * w, b[1] * h, b[2] * w, b[3] * h])
    if "box" in n:
        return ("box", _box(n["box"], w, h))
    if "from" in n and "to" in n:
        return ("arrow", list(_pt(n["from"], w, h)) + list(_pt(n["to"], w, h)))
    if "at" in n:
        return ("pin", list(_pt(n["at"], w, h)))
    raise ValueError("note has no location: %r" % (n,))


def annotate(img_u8, notes):
    """img_u8 BGR uint8 -> BGR uint8 copy with numbered notes."""
    h, w = img_u8.shape[:2]
    pil = Image.fromarray(cv2.cvtColor(img_u8, cv2.COLOR_BGR2RGB)).convert("RGBA")
    ov = Image.new("RGBA", pil.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    short = min(w, h)
    lw = max(2, int(round(short / 280)))
    rad = max(13, int(round(short / 42)))
    font = get_font(max(14, int(round(short / 36))), bold=True)
    nfont = get_font(max(12, int(rad * 1.15)), bold=True)
    gold, dark = (255, 200, 0, 255), (0, 0, 0, 255)
    drawn = []
    num = 0
    for n in notes:
        if not isinstance(n, dict):
            continue
        num += 1
        kind, g = resolve_note(n, w, h)
        label = str(n.get("label", ""))
        if kind == "box":
            x0, y0, x1, y1 = g
            d.rectangle([x0, y0, x1, y1], outline=dark, width=lw + 2)
            d.rectangle([x0, y0, x1, y1], outline=gold, width=lw)
            bx, by = x0 + rad + 2, y0 + rad + 2
        elif kind == "arrow":
            x0, y0, x1, y1 = g
            d.line([x0, y0, x1, y1], fill=dark, width=lw + 3)
            d.line([x0, y0, x1, y1], fill=gold, width=lw)
            ang = math.atan2(y1 - y0, x1 - x0)
            hl = rad * 1.3
            tri = [(x1, y1)] + [(x1 - hl * math.cos(ang + s * 0.45), y1 - hl * math.sin(ang + s * 0.45)) for s in (-1, 1)]
            d.polygon(tri, fill=dark)
            inner = [(x1, y1)] + [(x1 - (hl - 3) * math.cos(ang + s * 0.45), y1 - (hl - 3) * math.sin(ang + s * 0.45)) for s in (-1, 1)]
            d.polygon(inner, fill=gold)
            bx, by = x0, y0
        else:
            bx, by = g
            d.ellipse([bx - rad - 4, by - rad - 4, bx + rad + 4, by + rad + 4], outline=gold, width=lw)
        bx = float(np.clip(bx, rad + 1, w - rad - 1))
        by = float(np.clip(by, rad + 1, h - rad - 1))
        d.ellipse([bx - rad - 1, by - rad - 1, bx + rad + 1, by + rad + 1], fill=dark)
        d.ellipse([bx - rad + 1, by - rad + 1, bx + rad - 1, by + rad - 1], fill=gold)
        d.text((bx, by), str(num), font=nfont, fill=dark, anchor="mm")
        if label:
            tb = d.textbbox((0, 0), label, font=font)
            tw, th = tb[2] - tb[0], tb[3] - tb[1]
            px = bx + rad + 6
            py = by - th / 2 - 5
            if px + tw + 14 > w:
                px = max(2, bx - rad - 6 - tw - 14)
            py = float(np.clip(py, 2, h - th - 12))
            d.rounded_rectangle([px, py, px + tw + 14, py + th + 12], radius=6, fill=(0, 0, 0, 205))
            d.text((px + 7, py + 5 - tb[1]), label, font=font, fill=(255, 255, 255, 255))
        drawn.append({"n": num, "kind": kind, "label": label, "geometry_px": [round(v, 1) for v in g]})
    out = Image.alpha_composite(pil, ov).convert("RGB")
    return cv2.cvtColor(np.array(out), cv2.COLOR_RGB2BGR), drawn


# ----------------------------------------------------------------------------- board
BG = (24, 24, 24)
MARGIN, GAP, STRIP = 16, 16, 34


def _row_height(panels, max_w, cap):
    aspects = [p[1].shape[1] / float(p[1].shape[0]) for p in panels]
    avail = max_w - GAP * (len(panels) - 1)
    return min(cap, avail / sum(aspects))


def _build_row(panels, h):
    """panels: [(title, bgr_u8)] -> PIL image of one row at image height h."""
    font = get_font(20, bold=True)
    tiles = []
    for title, im in panels:
        ih, iw = im.shape[:2]
        tw_ = max(1, int(round(h * iw / float(ih))))
        small = cv2.resize(im, (tw_, int(round(h))), interpolation=cv2.INTER_AREA)
        tile = Image.new("RGB", (tw_, int(round(h)) + STRIP), BG)
        tile.paste(Image.fromarray(cv2.cvtColor(small, cv2.COLOR_BGR2RGB)), (0, STRIP))
        dr = ImageDraw.Draw(tile)
        t = title if len(title) < 60 else title[:57] + "..."
        dr.text((2, STRIP // 2), t, font=font, fill=(235, 235, 235), anchor="lm")
        tiles.append(tile)
    row = Image.new("RGB", (sum(t.width for t in tiles) + GAP * (len(tiles) - 1), tiles[0].height), BG)
    x = 0
    for t in tiles:
        row.paste(t, (x, 0))
        x += t.width + GAP
    return row


def make_board(orig_u8, annotated_u8, variants):
    """variants: [(name, bgr_u8)] -> PIL board, long edge <= MAX_BOARD."""
    first = [("ORIGINAL", orig_u8)]
    if annotated_u8 is not None:
        first.append(("NOTES", annotated_u8))
    allp = first + [(n, im) for n, im in variants]
    inner = MAX_BOARD - 2 * MARGIN
    rows = []
    h_one = _row_height(allp, inner, 1000)
    if h_one >= 700 or not variants:
        rows.append(_build_row(allp, h_one))
    else:
        rows.append(_build_row(first, _row_height(first, inner, 800)))
        # variants may need to wrap onto more rows
        chunk = []
        for v in variants:
            trial = chunk + [v]
            if chunk and _row_height(trial, inner, 800) < 420:
                rows.append(_build_row(chunk, _row_height(chunk, inner, 800)))
                chunk = [v]
            else:
                chunk = trial
        if chunk:
            rows.append(_build_row(chunk, _row_height(chunk, inner, 800)))
    W = max(r.width for r in rows) + 2 * MARGIN
    H = sum(r.height for r in rows) + GAP * (len(rows) - 1) + 2 * MARGIN
    board = Image.new("RGB", (W, H), BG)
    y = MARGIN
    for r in rows:
        board.paste(r, ((W - r.width) // 2, y))
        y += r.height + GAP
    if max(W, H) > MAX_BOARD:
        s = MAX_BOARD / float(max(W, H))
        board = board.resize((int(W * s), int(H * s)), Image.LANCZOS)
    return board


# ----------------------------------------------------------------------------- main
def slug(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", str(s)).strip("-").lower()
    return s[:40] or "variant"


def run(image_path, plan, out_dir, quality=92):
    os.makedirs(out_dir, exist_ok=True)
    bgr = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if bgr is None:
        raise SystemExit("cannot read image %s" % image_path)
    src = bgr.astype(np.float32) / 255.0
    h, w = bgr.shape[:2]
    report = {"source": os.path.abspath(image_path), "size": [w, h], "variants": [], "notes": []}
    outs = []
    failed = False
    for i, v in enumerate(plan.get("variants", []), 1):
        name = v.get("name") or "variant %d" % i
        img, ops_rep = apply_ops(src.copy(), v.get("ops", []))
        fname = "%02d_%s.jpg" % (i, slug(name))
        cv2.imwrite(os.path.join(out_dir, fname), u8(img), [cv2.IMWRITE_JPEG_QUALITY, quality])
        failed = failed or any(not o["applied"] for o in ops_rep)
        report["variants"].append({"name": name, "file": fname, "size": [img.shape[1], img.shape[0]], "ops": ops_rep})
        outs.append((name, u8(img)))
    notes = plan.get("notes", [])
    annotated = None
    if any(isinstance(n, dict) for n in notes):
        annotated, drawn = annotate(bgr, notes)
        cv2.imwrite(os.path.join(out_dir, "annotated.jpg"), annotated, [cv2.IMWRITE_JPEG_QUALITY, quality])
        report["notes"] = drawn + [{"text": n} for n in notes if isinstance(n, str)]
    else:
        report["notes"] = [{"text": n} for n in notes if isinstance(n, str)]
    board = make_board(bgr, annotated, outs)
    board.save(os.path.join(out_dir, "board.jpg"), quality=quality)
    report["board"] = {"file": "board.jpg", "size": list(board.size)}
    with open(os.path.join(out_dir, "fix_report.json"), "w") as f:
        json.dump(report, f, indent=2)
    return report, failed


def main(argv=None):
    ap = argparse.ArgumentParser(description="Render 'show the fix' variants.")
    ap.add_argument("image")
    ap.add_argument("plan")
    ap.add_argument("--out", required=True)
    ap.add_argument("--quality", type=int, default=92)
    a = ap.parse_args(argv)
    with open(a.plan) as f:
        plan = json.load(f)
    report, failed = run(a.image, plan, a.out, a.quality)
    for v in report["variants"]:
        for o in v["ops"]:
            if not o["applied"]:
                print("WARN %s: %s failed: %s" % (v["name"], o["op"], o.get("error")), file=sys.stderr)
    print("board: %s  (%dx%d)" % (os.path.join(a.out, "board.jpg"), *report["board"]["size"]))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
