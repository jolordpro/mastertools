# Harmonize core: the light match, black-reference glare floor and camera traits used by harmonize.py.
# Tested against C4D/Redshift ground truth (post-composite-workspace/harmonize-gt/, 2026-10-27) and the Jack spike.
# Images are float RGB code values (display, 2.4 power) unless named _lin. Sizes are given at 1920 wide and scaled.
import numpy as np
import cv2

GAMMA = 2.4
LUMA = np.array([0.2126, 0.7152, 0.0722])
M709 = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
MBFD = np.array([[0.8951, 0.2664, -0.1614], [-0.7502, 1.7135, 0.0367], [0.0389, -0.0685, 1.0296]])


def lin(v):
    return np.clip(v, 0, None) ** GAMMA


def enc(l):
    return np.clip(l, 0, None) ** (1 / GAMMA)


def blur(img, s):
    return img if s <= 0 else cv2.GaussianBlur(img, (0, 0), s)


def window(shape, cx, cy, r):
    m = np.zeros(shape[:2], bool)
    m[max(0, cy - r):cy + r, max(0, cx - r):cx + r] = True
    return m


def neutral(plate, mask, sat_max=0.15):
    """Median linear RGB of low-saturation, unclipped, mid-bright pixels, scaled to luminance 1.
    Same as the spike; returns (rgb, n_pixels)."""
    v = plate[mask]
    mx, mn = v.max(1), v.min(1)
    y = v @ LUMA
    ok = (mx < 0.95) & (y > 0.12) & ((mx - mn) / np.maximum(mx, 1e-6) < sat_max)
    if ok.sum() == 0:
        return None, 0
    c = np.median(lin(v[ok]), 0)
    return c / (c @ LUMA), int(ok.sum())


def bradford(c):
    ws, wt = M709 @ np.ones(3), M709 @ c
    A = np.linalg.inv(MBFD) @ np.diag((MBFD @ wt) / (MBFD @ ws)) @ MBFD
    return np.linalg.inv(M709) @ A @ M709


def paste(plate, layer):
    """layer: straight RGB code + alpha (H, W, 4)."""
    a = layer[..., 3:]
    return layer[..., :3] * a + (1 - a) * plate


def stats_match(plate, layer, surround):
    a = layer[..., 3]
    inner = a > 0.5
    straight = np.clip(layer[..., :3], 0, 1).astype(np.float32)
    lab_l = cv2.cvtColor(straight, cv2.COLOR_RGB2Lab)
    lab_p = cv2.cvtColor(np.clip(plate, 0, 1).astype(np.float32), cv2.COLOR_RGB2Lab)
    ml, sl = lab_l[inner].mean(0), lab_l[inner].std(0)
    mp, sp = lab_p[surround].mean(0), lab_p[surround].std(0)
    out = cv2.cvtColor(((lab_l - ml) * (sp / np.maximum(sl, 1e-6)) + mp).astype(np.float32), cv2.COLOR_Lab2RGB)
    return paste(plate, np.dstack([np.clip(out.astype(np.float64), 0, None), a]))


def light_match(plate, layer, spot, rho, white_paint=0.85, glare=None):
    """The spike's painted-layer light match. spot = (cx, cy) of the layer. rho = wall albedo.
    glare: None = the spike's local estimate (P0.5 of a 200 px window); a number overrides it (diagnostic).
    Returns (composite code, info)."""
    h, w = plate.shape[:2]
    k = w / 1920.0
    cx, cy = spot
    c_local, n_loc = neutral(plate, window(plate.shape, cx, cy, int(400 * k)))
    if c_local is None:
        c_local = np.ones(3)
    g = np.percentile(lin(plate[window(plate.shape, cx, cy, int(200 * k))]) @ LUMA, 0.5) if glare is None else float(glare)
    a = layer[..., 3:]
    albedo = lin(layer[..., :3]) * white_paint
    shade = blur(lin(plate) @ LUMA, 3.0 * k) - g
    light = np.clip(g + (albedo @ bradford(c_local).T) * (shade[..., None] / rho), 0, None)
    comp = enc(light) * a + (1 - a) * plate
    return comp, {"neutral_rgb": [round(float(x), 4) for x in c_local], "neutral_pixels": n_loc, "glare_floor": float(g)}


def black_floor(plate, spot, rho, a_black=0.03, dark_ratio=0.25, min_area=1e-4, search=600, want_mask=False):
    """Glare floor from a black reference (VEIL-DESIGN.md). Black objects = pixels under dark_ratio of the local mean
    luminance (Gaussian, sigma 40 px at 1920), in connected patches >= min_area of the frame, within `search` px of the
    spot. A smooth falloff stays near its own mean, so it is not picked. B = dark level (P2 of the patches), S = median
    of a ring just outside them. Floor v solves B = v + a_black*E, S = v + rho*E. None found: 0."""
    h, w = plate.shape[:2]
    k = w / 1920.0
    y = lin(plate) @ LUMA
    dark = (y < dark_ratio * blur(y, 40 * k)).astype(np.uint8)
    yy, xx = np.mgrid[:h, :w]
    near = np.hypot(xx - spot[0], yy - spot[1]) <= search * k
    n, lab, stats, _ = cv2.connectedComponentsWithStats(dark, connectivity=8)
    keep = np.zeros((h, w), np.uint8)
    for i in range(1, n):
        if stats[i, cv2.CC_STAT_AREA] >= min_area * h * w:
            keep[lab == i] = 1
    keep &= near.astype(np.uint8)
    if keep.sum() == 0:
        info = {"black_pixels": 0, "floor": 0.0}
        return (0.0, info, keep > 0) if want_mask else (0.0, info)
    r1, r2 = max(2, int(15 * k)), max(4, int(45 * k))
    ring = (cv2.dilate(keep, np.ones((2 * r2 + 1,) * 2)) > 0) & ~(cv2.dilate(keep, np.ones((2 * r1 + 1,) * 2)) > 0)
    B = float(np.percentile(y[keep > 0], 2))
    S = float(np.median(y[ring]))
    v = max(0.0, (B - a_black * S / rho) / (1 - a_black / rho))
    info = {"black_pixels": int(keep.sum()), "dark_level": round(B, 5), "surround": round(S, 5), "floor": round(v, 5)}
    return (v, info, keep > 0) if want_mask else (v, info)


# ---------- camera traits (from the spike, unchanged method) ----------
def edge_sigma(y, mask):
    """Zhuo & Sim gradient-ratio defocus: median blur sigma (px) over strong edges inside mask. (sigma, n_edges)."""
    g = lambda im: np.hypot(cv2.Sobel(im, cv2.CV_64F, 1, 0, ksize=3), cv2.Sobel(im, cv2.CV_64F, 0, 1, ksize=3))
    g1, g2 = g(y), g(blur(y, 1.0))
    if mask.sum() < 50:
        return float("nan"), 0
    e = cv2.Canny((np.clip(y, 0, 1) * 255).astype(np.uint8), 20, 50) > 0
    e &= mask & (g1 > np.percentile(g1[mask], 90))
    R = g1[e] / np.maximum(g2[e], 1e-9)
    R = R[R > 1.02]
    return (float(np.median(1.0 / np.sqrt(R ** 2 - 1))) if R.size > 20 else float("nan")), int(R.size)


def grain_model(plate, nbins=20):
    """The plate's own grain: residual (plate - blur 2) and its per-channel std by brightness band, measured on
    flat areas. Returns (resid, table[nbins,3], bins_measured)."""
    k = plate.shape[1] / 1920.0
    resid = plate - blur(plate, 2.0 * k)
    flat = np.hypot(*np.gradient(blur(plate @ LUMA, 2.0 * k))) < 0.002
    yb = np.clip(((blur(plate, 2.0 * k) @ LUMA) * nbins).astype(int), 0, nbins - 1)
    sig = np.full((nbins, 3), np.nan)
    need = max(200, int(2000 * k * k))
    for b in range(nbins):
        m = flat & (yb == b)
        if m.sum() > need:
            sig[b] = resid[m].std(0)
    good = ~np.isnan(sig[:, 0])
    if good.sum() == 0:
        return resid, np.zeros((nbins, 3)), 0
    for ch in range(3):
        sig[:, ch] = np.interp(np.arange(nbins), np.where(good)[0], sig[good, ch])
    return resid, sig, int(good.sum())


def camera_traits(layer, plate, sigma_add, resid, sig, chroma="4:4:4"):
    """layer: premultiplied RGB + alpha (code). Defocus, then the plate's grain rescaled to the layer's brightness
    band, then chroma softening to the plate's subsampling. Returns composite (code)."""
    nb = sig.shape[0]
    sig_at = lambda y: sig[np.clip((y * nb).astype(int), 0, nb - 1)]
    # Defocus and the over are done in linear light, as a lens and a linear AE project do. Blurring code values
    # darkens bright-to-dark edges (found by selftest_harmonize.py, 2026-10-27).
    a = layer[..., 3:]
    prem_lin = lin(layer[..., :3] / np.maximum(a, 1e-6)) * a
    if sigma_add > 0:
        prem_lin, a = blur(prem_lin, sigma_add), blur(a[..., 0], sigma_add)[..., None]
    straight = enc(prem_lin / np.maximum(a, 1e-6))
    comp = enc(prem_lin + (1 - a) * lin(plate))
    ratio = sig_at(straight @ LUMA) / np.maximum(sig_at(blur(plate, 2.0 * plate.shape[1] / 1920.0) @ LUMA), 1e-6)
    comp = comp + a * resid * ratio
    if chroma in ("4:2:2", "4:2:0"):
        m = cv2.dilate((a[..., 0] > 0.001).astype(np.uint8), np.ones((5, 5))) > 0
        Mfwd = np.array([[0.2126, -0.1146, 0.5], [0.7152, -0.3854, -0.4542], [0.0722, 0.5, -0.0458]])
        ycc = comp @ Mfwd
        kx = np.array([[0.25, 0.5, 0.25]])
        for ch in (1, 2):
            c = cv2.filter2D(ycc[..., ch], -1, kx)
            if chroma == "4:2:0":
                c = cv2.filter2D(c, -1, kx.T)
            ycc[..., ch] = np.where(m, c, ycc[..., ch])
        comp = ycc @ np.linalg.inv(Mfwd)
    return comp
