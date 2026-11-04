#!/usr/bin/env python3
"""harmonize.py: make a placed layer belong in a plate (Harmonize v1, references/11-harmonize.md).

Usage:
    python3 harmonize.py PLATE LAYER --kind painted|object|projected|emitting|floating [--at SEC] [--out DIR]
        [--wall-albedo 0.6] [--black-reflectance 0.03] [--white-paint 0.85]
        [--project-stops 1.0] [--emit-gain 1.0] [--shadow-box x0,y0,x1,y1 --lit-box x0,y0,x1,y1]

PLATE is a movie or a still, decoded exactly as analyze_plate.py does. LAYER is an RGBA image (straight alpha)
already placed at plate size. --kind is what the layer is in the world; ask, never guess.

Writes into DIR (default ./harmonize_<layer name>/):
    harmonized.png         16-bit composite
    layer_harmonized.png   16-bit RGBA, the layer alone (premultiplied with black)
    before_after.jpg       paste vs harmonized, crop and full frame
    squint.jpg             brightness, each channel, heavy blur, edges at 200%: paste (top) vs harmonized (bottom)
    black_reference.jpg    what was taken as black for the glare floor (magenta), search area (yellow)
    cast.cube              the color cast (Bradford) as a 65-point LUT on display code values
    harmonize.json         every measured value and dial
    plan.md                the After Effects stack (then Photoshop), in priority order, with these values

Needs ffmpeg/ffprobe and Python 3 with numpy + opencv-python.
"""
import argparse, json, math, os, re, sys
import numpy as np
import cv2

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analyze_plate import probe, decode
from harmonize_core import (LUMA, lin, enc, blur, window, neutral, bradford, paste, light_match, black_floor,
                            edge_sigma, grain_model, camera_traits)

VERSION = "1.0.0 (2026-10-27)"
KINDS = ("painted", "object", "projected", "emitting", "floating")
LIT = ("painted", "object")


def read_plate(path, at):
    info = probe(path)
    dur = 1.5 / info["fps"] if info.get("fps") else None    # one frame; ffmpeg stops itself
    for _, rgb in decode(info, at, dur):
        return rgb.astype(np.float64), info
    sys.exit("no frame decoded from %s" % path)


def read_layer(path, h, w):
    im = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if im is None or im.ndim != 3 or im.shape[2] != 4:
        sys.exit("LAYER must be an RGBA image (straight alpha): %s" % path)
    if im.shape[:2] != (h, w):
        sys.exit("LAYER is %dx%d but the plate is %dx%d; place it at plate size first" % (im.shape[1], im.shape[0], w, h))
    scale = 65535.0 if im.dtype == np.uint16 else 255.0
    rgba = cv2.cvtColor(im, cv2.COLOR_BGRA2RGBA).astype(np.float64) / scale
    return rgba


def save16(path, rgb, alpha=None):
    x = np.clip(rgb, 0, 1)
    if alpha is not None:
        x = np.dstack([x, np.clip(alpha, 0, 1)])
        cv2.imwrite(path, cv2.cvtColor((x * 65535 + 0.5).astype(np.uint16), cv2.COLOR_RGBA2BGRA))
    else:
        cv2.imwrite(path, cv2.cvtColor((x * 65535 + 0.5).astype(np.uint16), cv2.COLOR_RGB2BGR))


def to8(x):
    return (np.clip(x, 0, 1) * 255 + 0.5).astype(np.uint8)


def write_cube(path, T, n=65):
    g = np.linspace(0, 1, n)
    with open(path, "w") as f:
        f.write('TITLE "harmonize cast (Bradford)"\nLUT_3D_SIZE %d\nDOMAIN_MIN 0 0 0\nDOMAIN_MAX 1 1 1\n' % n)
        for b in g:
            for gg in g:
                for r in g:
                    o = np.clip(enc(T @ lin(np.array([r, gg, b]))), 0, 1)
                    f.write("%.6f %.6f %.6f\n" % tuple(o))


def apply_cube(path, rgb):
    """Trilinear lookup, for the self-test."""
    vals = [l.split() for l in open(path) if l[:1].isdigit() or l[:1] == "-"]
    n = round(len(vals) ** (1 / 3))
    lut = np.array(vals, float).reshape(n, n, n, 3)   # [b][g][r]
    p = np.clip(rgb, 0, 1) * (n - 1)
    i0 = np.minimum(np.floor(p).astype(int), n - 2)
    f = p - i0
    out = 0
    for db in (0, 1):
        for dg in (0, 1):
            for dr in (0, 1):
                wgt = ((f[..., 2] if db else 1 - f[..., 2]) * (f[..., 1] if dg else 1 - f[..., 1]) *
                       (f[..., 0] if dr else 1 - f[..., 0]))
                out = out + wgt[..., None] * lut[i0[..., 2] + db, i0[..., 1] + dg, i0[..., 0] + dr]
    return out


def parse_box(s):
    if not s:
        return None
    v = [int(float(t)) for t in s.split(",")]
    if len(v) != 4:
        sys.exit("boxes are x0,y0,x1,y1 in plate pixels")
    return v


def label(img, text):
    bar = np.full((28, img.shape[1], 3), 20, np.uint8)
    cv2.putText(bar, text, (6, 19), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (235, 235, 235), 1, cv2.LINE_AA)
    return np.vstack([bar, img])


def squint_row(comp, box, edge_box, name):
    x0, y0, x1, y1 = box
    c = comp[y0:y1, x0:x1]
    th = 220
    sc = th / c.shape[0]
    rs = lambda im: cv2.resize(im, (max(1, int(im.shape[1] * sc)), th), interpolation=cv2.INTER_AREA)
    y = c @ LUMA
    tiles = [label(rs(to8(c)), name),
             label(rs(to8(np.dstack([y] * 3))), "brightness"),
             *[label(rs(to8(np.dstack([c[..., i]] * 3))), ch) for i, ch in enumerate(("red", "green", "blue"))],
             label(rs(to8(blur(c, max(2.0, c.shape[0] * 0.04)))), "heavy blur")]
    ex0, ey0, ex1, ey1 = edge_box
    e = cv2.resize(to8(comp[ey0:ey1, ex0:ex1]), None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST)
    tiles.append(label(cv2.resize(e, (int(e.shape[1] * th / e.shape[0]), th), interpolation=cv2.INTER_NEAREST), "edge 200%"))
    gap = np.full((th + 28, 6, 3), 255, np.uint8)
    row = []
    for t in tiles:
        row += [t, gap]
    return np.hstack(row[:-1])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("plate")
    ap.add_argument("layer")
    ap.add_argument("--kind", required=True, choices=KINDS)
    ap.add_argument("--at", type=float, help="seconds into a movie plate")
    ap.add_argument("--out")
    ap.add_argument("--wall-albedo", type=float, default=0.6, help="surface paint vs a white surface (a dial)")
    ap.add_argument("--black-reflectance", type=float, default=0.03, help="reflectance of black objects (a dial)")
    ap.add_argument("--white-paint", type=float, default=0.85, help="the layer's white as reflectance")
    ap.add_argument("--project-stops", type=float, default=1.0, help="projected white, stops above the wall")
    ap.add_argument("--emit-gain", type=float, default=1.0, help="emitter white vs the plate's bright diffuse level")
    ap.add_argument("--shadow-box")
    ap.add_argument("--lit-box")
    a = ap.parse_args()

    plate, info = read_plate(a.plate, a.at)
    H, W = plate.shape[:2]
    k = W / 1920.0
    layer = read_layer(a.layer, H, W)
    alpha = layer[..., 3]
    if (alpha > 0.5).sum() < 20:
        sys.exit("LAYER alpha is empty")
    name = os.path.splitext(os.path.basename(a.layer))[0]
    out = a.out or os.path.join(os.getcwd(), "harmonize_" + re.sub(r"[^A-Za-z0-9_-]+", "_", name))
    os.makedirs(out, exist_ok=True)

    ys, xs = np.where(alpha > 0.5)
    spot = (int(xs.mean()), int(ys.mean()))
    am = (alpha > 0.01).astype(np.uint8)
    near_layer = cv2.dilate(am, np.ones((int(9 * k) | 1,) * 2)) > 0
    ring = (cv2.dilate(am, np.ones((int(81 * k) | 1,) * 2)) > 0) & ~(cv2.dilate(am, np.ones((int(13 * k) | 1,) * 2)) > 0)
    rep = {"version": VERSION, "plate": info.get("path"), "at_s": a.at, "layer": os.path.abspath(a.layer), "kind": a.kind,
           "size": [W, H], "chroma": info.get("chroma"), "spot": spot,
           "dials": {"wall_albedo": a.wall_albedo, "black_reflectance": a.black_reflectance, "white_paint": a.white_paint,
                     "project_stops": a.project_stops, "emit_gain": a.emit_gain}}
    pasted = paste(plate, layer)

    # 1. Blacks and light (per kind)
    g, binfo, bmask = black_floor(plate, spot, a.wall_albedo, a_black=a.black_reflectance, want_mask=True)
    rep["glare_floor"] = binfo
    c_local, n_loc = neutral(plate, window(plate.shape, spot[0], spot[1], int(400 * k)))
    rep["local_neutral"] = {"rgb": None if c_local is None else [round(float(x), 4) for x in c_local], "pixels": n_loc,
                            "fallback": c_local is None}
    T = bradford(c_local if c_local is not None else np.ones(3))
    rep["cast_matrix_linear"] = [[round(float(x), 5) for x in r] for r in T]
    wall_lum = float(np.median(blur(lin(plate) @ LUMA, 3.0 * k)[ring])) if ring.any() else float("nan")
    rep["wall_luminance_lin"] = round(wall_lum, 5)
    A = layer[..., 3:]
    if a.kind in LIT:
        comp_l, li = light_match(plate, layer, spot, a.wall_albedo, white_paint=a.white_paint, glare=g)
        light_layer = comp_l - (1 - A) * plate
    elif a.kind == "projected":
        add = (2 ** a.project_stops - 1) * wall_lum * lin(layer[..., :3])
        light_layer = (enc(lin(plate) + add) - plate) * A + plate * A      # premultiplied
        rep["projected_white_add_lin"] = round((2 ** a.project_stops - 1) * wall_lum, 5)
    elif a.kind == "emitting":
        y = lin(plate) @ LUMA
        diffuse = float(np.percentile(y[np.max(plate, -1) < 0.98], 99))
        level = diffuse * a.emit_gain
        light_layer = enc(g + level * lin(layer[..., :3])) * A
        rep["emitter_white_lin"] = round(level, 5)
    else:
        light_layer = layer[..., :3] * A

    # 2. Softness: plate edge blur near the spot vs the layer's own (measured on the paste)
    pl_mask = window(plate.shape, spot[0], spot[1], int(200 * k)) & ~near_layer
    sig_p, n_p = edge_sigma(plate @ LUMA, pl_mask)
    # Near the layer only: far edges sit at other depths, and soft light boundaries read as blur (GT case D).
    src = "near the layer" if np.isfinite(sig_p) else "not measured: too few edges near the layer, none added; set by eye"
    edge_band = (cv2.dilate(am, np.ones((5, 5))) > 0) & ~(cv2.erode((alpha > 0.99).astype(np.uint8), np.ones((5, 5))) > 0)
    sig_l, n_l = edge_sigma(pasted @ LUMA, cv2.dilate(edge_band.astype(np.uint8), np.ones((5, 5))) > 0)
    if not np.isfinite(sig_l):
        sig_l = 0.5
    sig_add = float(np.sqrt(max((sig_p if np.isfinite(sig_p) else 0) ** 2 - sig_l ** 2, 0)))
    rep["softness"] = {"plate_edge_sigma_px": round(sig_p, 3) if np.isfinite(sig_p) else None, "plate_edges": n_p,
                       "measured": src, "layer_edge_sigma_px": round(sig_l, 3), "layer_edges": n_l, "add_sigma_px": round(sig_add, 3)}

    # 3. Grain and texture: the plate's own residual by brightness band; chroma to the plate's subsampling
    resid, sig, nb = grain_model(plate)
    rep["grain"] = {"bands_measured": nb, "std_code_by_band": {"%.2f" % ((i + 0.5) / sig.shape[0]): [round(float(x), 5) for x in sig[i]]
                                                                for i in range(0, sig.shape[0], 4)}}
    yl = lin(plate) @ LUMA
    band = (blur(yl, 1.5 * k) - blur(yl, 8 * k)) / np.maximum(blur(yl, 8 * k), 1e-6)
    rep["wall_texture_contrast"] = round(float(band[ring].std()), 4) if ring.any() else None
    layer_in = np.dstack([light_layer, alpha])
    comp = camera_traits(layer_in, plate, sig_add, resid, sig, chroma=info.get("chroma") or "4:4:4")
    layer_out = comp - (1 - A) * plate          # premultiplied, includes softness, grain and chroma
    alpha_out = blur(alpha, sig_add) if sig_add > 0 else alpha

    # 4. Color cast LUT (painted/object use it; written for every kind so the file set is constant)
    write_cube(os.path.join(out, "cast.cube"), T)

    # 6. Contact shadow density from the plate's own shadow (object, optional boxes)
    sb, lb = parse_box(a.shadow_box), parse_box(a.lit_box)
    if sb and lb:
        sh = np.median(lin(plate[sb[1]:sb[3], sb[0]:sb[2]]).reshape(-1, 3), 0)
        lt = np.median(lin(plate[lb[1]:lb[3], lb[0]:lb[2]]).reshape(-1, 3), 0)
        r = sh / np.maximum(lt, 1e-6)
        rep["shadow"] = {"density_lin": round(float(r @ LUMA), 4), "density_stops": round(float(np.log2(max(r @ LUMA, 1e-6))), 2),
                         "color_ratio_rgb": [round(float(x / max(r @ LUMA, 1e-6)), 3) for x in r]}

    # Outputs
    save16(os.path.join(out, "harmonized.png"), comp)
    save16(os.path.join(out, "layer_harmonized.png"), layer_out, alpha_out)
    pad = int(40 * k)
    box = (max(0, xs.min() - pad), max(0, ys.min() - pad), min(W, xs.max() + pad), min(H, ys.max() + pad))
    eb = np.argwhere(edge_band)
    ey, ex = eb[len(eb) // 2] if len(eb) else (spot[1], spot[0])
    r_e = int(24 * max(k, 0.5))
    ebox = (max(0, ex - r_e), max(0, ey - r_e), min(W, ex + r_e), min(H, ey + r_e))
    top, bot = squint_row(pasted, box, ebox, "paste"), squint_row(comp, box, ebox, "harmonized")
    sq = np.vstack([top, np.full((6, top.shape[1], 3), 255, np.uint8), bot])
    cv2.imwrite(os.path.join(out, "squint.jpg"), cv2.cvtColor(sq, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 88])
    x0, y0, x1, y1 = box
    crop = lambda im: to8(im[y0:y1, x0:x1])
    ba = np.hstack([label(crop(pasted), "paste"), np.full((y1 - y0 + 28, 6, 3), 255, np.uint8), label(crop(comp), "harmonized")])
    full = cv2.resize(to8(comp), (ba.shape[1], int(H * ba.shape[1] / W)), interpolation=cv2.INTER_AREA)
    cv2.imwrite(os.path.join(out, "before_after.jpg"), cv2.cvtColor(np.vstack([ba, full]), cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 88])
    ov = to8(plate).copy()
    ov[bmask] = (255, 60, 200)
    cv2.circle(ov, spot, int(600 * k), (255, 255, 0), max(1, int(3 * k)))
    cv2.putText(ov, "glare floor %.4f (linear), %d black px" % (binfo["floor"], binfo["black_pixels"]), (int(20 * k), int(50 * k)),
                cv2.FONT_HERSHEY_SIMPLEX, max(0.5, 1.2 * k), (255, 255, 0), max(1, int(2 * k)), cv2.LINE_AA)
    cv2.imwrite(os.path.join(out, "black_reference.jpg"), cv2.cvtColor(ov, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 85])
    json.dump(rep, open(os.path.join(out, "harmonize.json"), "w"), indent=1)
    open(os.path.join(out, "plan.md"), "w").write(plan_md(a, rep))
    print("harmonize %s · kind %s · glare floor %.4f (%d black px) · add blur %.2f px · grain bands %d · out %s" % (
        VERSION, a.kind, binfo["floor"], binfo["black_pixels"], sig_add, nb, out))


def plan_md(a, r):
    s, gf, sh = r["softness"], r["glare_floor"], r.get("shadow")
    stops = math.log2(a.white_paint / a.wall_albedo)
    T = r["cast_matrix_linear"]
    L = ["# Harmonize plan: %s" % os.path.basename(r["layer"]),
         "",
         "Kind: **%s**. Plate: `%s`%s. Every value is a starting point; judge in context on the squint board." % (
             a.kind, os.path.basename(r["plate"] or ""), " at %.2f s" % a.at if a.at is not None else ""),
         "",
         "## Measured",
         "- Glare floor: **%.4f** linear, from %d pixels taken as black (see `black_reference.jpg`; a shadow picked by mistake shows there). Black reflectance assumed %.3f." % (
             gf["floor"], gf["black_pixels"], a.black_reflectance) if gf["black_pixels"] else
         "- Glare floor: **0**. No black object within reach of the layer, so no glare can be read. If the shot has visible glare, this is low.",
         "- Wall light near the layer: %.4f linear. Wall albedo assumed **%.2f** (a dial: ×0.75 or ×1.33 moves brightness 0.4 stop, not color)." % (
             r["wall_luminance_lin"], a.wall_albedo),
         "- Local neutral: %s." % ("none found, cast left neutral" if r["local_neutral"]["fallback"] else
                                    "RGB %s from %d pixels" % (r["local_neutral"]["rgb"], r["local_neutral"]["pixels"])),
         "- Softness: plate edges σ %s px (%s), layer σ %.2f px, so add **σ %.2f px**." % (
             s["plate_edge_sigma_px"], s["measured"], s["layer_edge_sigma_px"], s["add_sigma_px"]),
         "- Grain: %d brightness bands measured on flat areas of the plate. Chroma: %s." % (r["grain"]["bands_measured"], r["chroma"]),
         "- Wall texture contrast near the layer: %s." % r["wall_texture_contrast"],
         ""]
    L += ["## After Effects stack (32 bpc, linear working space per reference 01, Strategy A)",
          "Inside the layer's precomp, top to bottom of the work order:", ""]
    n = 1
    if a.kind in ("painted", "object"):
        L += ["%d. **Color cast.** Channel Mixer on the layer, values from this matrix (rows are output R, G, B):" % n,
              "   `R %.4f %.4f %.4f · G %.4f %.4f %.4f · B %.4f %.4f %.4f`. Exact in a linear project. In a non-linear project or Photoshop, use `cast.cube` (Apply Color LUT; 65 points [verify the app loads that size]); a LUT can miss very dark colors by a few code values." % tuple(T[0] + T[1] + T[2])]
        n += 1
        L += ["%d. **Paint level.** Exposure %+.2f stops (white paint %.2f ÷ wall albedo %.2f)." % (n, stops, a.white_paint, a.wall_albedo)]
        n += 1
        L += ["%d. **Wall light.** Duplicate the plate into the precomp above the layer: Tint to gray, a small blur (removes grain only, about %.0f px),%s blend Multiply, Preserve Underlying Transparency on." % (
            n, max(1, 3 * W_scale(r)), " Exposure offset −%.4f," % gf["floor"] if gf["floor"] > 0 else "")]
        n += 1
        if gf["floor"] > 0:
            L += ["%d. **Glare floor.** A solid at linear %.4f in Add mode, Preserve Underlying Transparency on." % (n, gf["floor"])]
            n += 1
        if a.kind == "painted":
            L += ["%d. **Texture.** Grain from the plate carries the wall's fine surface (step %d below). For bumpy walls, Displacement Map from the plate's luminance, 1–2 px, by eye (texture contrast %s)." % (n, n + 2, r["wall_texture_contrast"])]
            n += 1
    elif a.kind == "projected":
        L += ["%d. **Added light.** Layer in Add mode over the plate. Its white adds linear %.4f (%+.1f stops over the wall). Never darker than the wall; no shadow." % (n, r["projected_white_add_lin"], a.project_stops)]
        n += 1
    elif a.kind == "emitting":
        L += ["%d. **Own light.** Keep the layer's colors. White at linear %.4f (the plate's bright diffuse level × %.2f). Glare floor %.4f added. Add glow and spill by eye (references 04 and 07)." % (n, r["emitter_white_lin"], a.emit_gain, gf["floor"])]
        n += 1
    L += ["%d. **Softness.** Gaussian Blur on the precomp to match σ %.2f px. Compare edges at 200%% on `squint.jpg`." % (n, s["add_sigma_px"])]
    n += 1
    L += ["%d. **Grain**, outside the precomp, last. Per channel, by brightness band, from the plate (numbers in `harmonize.json`). Note: AE Match Grain is 8/16 bpc only (reference 06)." % n]
    n += 1
    if r["chroma"] in ("4:2:2", "4:2:0"):
        L += ["%d. **Chroma.** The plate is %s. Soften the layer's color edges, not its brightness, if they look crisper than the plate's." % (n, r["chroma"])]
        n += 1
    if a.kind == "object":
        if sh:
            L += ["%d. **Contact shadow.** Darken to %.0f%% (%+.2f stops) with color ratio %s, measured from the plate's own shadow." % (
                n, sh["density_lin"] * 100, sh["density_stops"], sh["color_ratio_rgb"])]
        else:
            L += ["%d. **Contact shadow.** Not measured: rerun with `--shadow-box` and `--lit-box` on a shadow and a lit patch of the same surface." % n]
    L += ["", "## Photoshop", "Same order, each adjustment clipped to the layer. Cast: `cast.cube` in a Color Lookup layer. Grain on a merged copy last.", ""]
    L += ["## Files", "- `harmonized.png`, `layer_harmonized.png` (premultiplied), `before_after.jpg`, `squint.jpg`, `black_reference.jpg`, `cast.cube`, `harmonize.json`."]
    if a.kind in ("projected", "emitting"):
        L += ["", "**Untested:** the %s path has no ground-truth test yet (v1). Judge by eye." % a.kind]
    if a.kind == "floating":
        L.insert(L.index("## After Effects stack (32 bpc, linear working space per reference 01, Strategy A)") + 3,
                 "No scene light for a floating graphic: colors stay as designed. Only the camera's traits below.")
    return "\n".join(L) + "\n"


def W_scale(r):
    return r["size"][0] / 1920.0


if __name__ == "__main__":
    main()
