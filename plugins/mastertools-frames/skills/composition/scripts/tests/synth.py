"""Synthetic frames with known answers for selftest.py. Pure numpy/OpenCV/Pillow."""
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def horizon(angle_deg, w=1280, h=720):
    """Sky above, textured ground below, split by a line tilted angle_deg (positive = clockwise on screen)."""
    rs = np.random.RandomState(1)
    img = np.zeros((h, w, 3), np.uint8)
    img[:] = (200, 170, 120)
    ground = np.full((h, w, 3), (40, 90, 60), np.uint8)
    noise = rs.randint(-12, 12, (h, w, 1)).astype(np.int16)
    ground = np.clip(ground.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    yy, xx = np.mgrid[0:h, 0:w]
    slope = np.tan(np.radians(angle_deg))
    below = yy > (h * 0.55 + (xx - w / 2) * slope)
    img[below] = ground[below]
    return img


def corner_highlight(w=1280, h=720):
    img = np.full((h, w, 3), 90, np.uint8)
    cv2.circle(img, (int(w * 0.88), int(h * 0.16)), 70, (255, 255, 255), -1)
    return cv2.GaussianBlur(img, (0, 0), 3)


def flat_scene(w=1280, h=720):
    return np.full((h, w, 3), 90, np.uint8)


def value_range(full, w=640, h=360):
    """Gradient plus blobs. full=True spans ~black to white, False is squeezed into L ~ 45-60."""
    rs = np.random.RandomState(2)
    base = np.tile(np.linspace(0, 255, w, dtype=np.float32), (h, 1))
    base += rs.randn(h, w).astype(np.float32) * 10
    if not full:
        base = 110 + base * 0.12
    g = np.clip(base, 0, 255).astype(np.uint8)
    return cv2.cvtColor(g, cv2.COLOR_GRAY2BGR)


def text_frame(fg, bg, text="MATCH DAY", w=1280, h=720, size=150, xy=(0.15, 0.38)):
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    try:
        font = ImageFont.load_default(size=size)
    except TypeError:
        font = ImageFont.load_default()
    d.text((int(xy[0] * w), int(xy[1] * h)), text, fill=fg, font=font)
    x0, y0, x1, y1 = d.textbbox((int(xy[0] * w), int(xy[1] * h)), text, font=font)
    box = {"x": x0 / w, "y": y0 / h, "w": (x1 - x0) / w, "h": (y1 - y0) / h}
    return np.asarray(im)[..., ::-1].copy(), box


def subject_mask(cx, cy, bw, bh, w=640, h=360):
    m = np.zeros((h, w), bool)
    x0, y0 = int((cx - bw / 2) * w), int((cy - bh / 2) * h)
    m[max(0, y0):int((cy + bh / 2) * h), max(0, x0):int((cx + bw / 2) * w)] = True
    return m
