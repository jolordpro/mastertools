#!/usr/bin/env python3
"""frame_prep.py: prepare frames for /elevate.

For each input frame (F1, F2, ... in argument order):
  - resize so the long edge is <= --long-edge (default 2576; never upscales)
  - save an unmarked copy (F1.png) and a gridded copy (F1_grid.png)
    with cells labelled A1..D4 (columns A.., rows 1..)
Crops are cut 1:1 from the ORIGINAL pixels (no scaling), so fine detail survives.
Writes manifest.json describing frames, grid and crops.

Usage:
  python3 frame_prep.py F1.png F2.png --out prep
  python3 frame_prep.py F1.png --out prep --grid 4x4 --long-edge 2576 \
      --crop "K1=F1:1200,400,600,400" --crop "K2=F1:0,900,800,300"
Crop format: ID=FRAME:x,y,w,h in the original pixel coordinates of that frame.

Requires Pillow (pip install pillow). EXR is not supported: export PNG or TIFF first.
"""
import argparse
import json
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    if sys.flags.isolated:
        sys.stderr.write("frame_prep can't see Pillow because Python runs isolated (-I), which hides "
                         "user-installed packages. Run it without -I, or with "
                         "`uv run --with pillow python frame_prep.py ...`.\n")
    else:
        sys.stderr.write("frame_prep needs Pillow: run `pip install pillow` (add --break-system-packages "
                         "on managed Pythons), or skip it and cite an imagined 4x4 grid (A-D, 1-4).\n")
    sys.exit(2)


def load_font(size):
    try:
        return ImageFont.load_default(size=size)  # Pillow >= 10.1
    except TypeError:
        return ImageFont.load_default()


def col_label(i):
    label, i = "", i + 1
    while i:
        i, r = divmod(i - 1, 26)
        label = chr(65 + r) + label
    return label


def draw_grid(img, cols, rows):
    im = img.convert("RGB")
    d = ImageDraw.Draw(im)
    w, h = im.size
    lw = max(1, round(min(w, h) / 540))
    font = load_font(max(12, round(min(w, h) / 36)))
    for c in range(1, cols):
        x = round(c * w / cols)
        d.line([(x, 0), (x, h)], fill=(255, 255, 255), width=lw + 2)
        d.line([(x, 0), (x, h)], fill=(0, 0, 0), width=lw)
    for r in range(1, rows):
        y = round(r * h / rows)
        d.line([(0, y), (w, y)], fill=(255, 255, 255), width=lw + 2)
        d.line([(0, y), (w, y)], fill=(0, 0, 0), width=lw)
    for c in range(cols):
        for r in range(rows):
            x = round(c * w / cols) + 3 * lw + 4
            y = round(r * h / rows) + 3 * lw + 2
            d.text((x, y), f"{col_label(c)}{r + 1}", font=font, fill=(255, 255, 255),
                   stroke_width=max(2, lw + 1), stroke_fill=(0, 0, 0))
    return im


def parse_grid(text):
    try:
        cols, rows = (int(v) for v in text.lower().split("x"))
        if cols < 1 or rows < 1 or cols > 26:
            raise ValueError
        return cols, rows
    except ValueError:
        sys.exit(f"--grid must look like 4x4 (columns 1-26), got {text!r}")


def parse_crop(text):
    try:
        cid, rest = text.split("=", 1)
        frame, box = rest.split(":", 1)
        x, y, w, h = (int(v) for v in box.split(","))
        if w <= 0 or h <= 0:
            raise ValueError
        return cid.strip(), frame.strip(), (x, y, w, h)
    except ValueError:
        sys.exit(f"--crop must look like K1=F1:x,y,w,h, got {text!r}")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Prepare frames for /elevate.")
    ap.add_argument("frames", nargs="+", help="frame images, in order F1, F2, ...")
    ap.add_argument("--out", required=True, help="output folder")
    ap.add_argument("--long-edge", type=int, default=2576)
    ap.add_argument("--grid", default="4x4", help="columns x rows, e.g. 4x4")
    ap.add_argument("--crop", action="append", default=[], help="ID=FRAME:x,y,w,h (original pixels)")
    args = ap.parse_args(argv)

    cols, rows = parse_grid(args.grid)
    os.makedirs(args.out, exist_ok=True)
    manifest = {"tool": "elevate frame_prep", "version": "1.0", "long_edge": args.long_edge,
                "grid": {"cols": cols, "rows": rows,
                         "labels": f"A1..{col_label(cols - 1)}{rows}"},
                "frames": [], "crops": [], "warnings": []}
    originals = {}

    for n, path in enumerate(args.frames, 1):
        fid = f"F{n}"
        try:
            img = Image.open(path)
            img.load()
        except Exception as exc:  # unreadable or unsupported (e.g. EXR)
            sys.exit(f"{fid}: cannot read {path}: {exc}")
        originals[fid] = img
        w, h = img.size
        scale = min(1.0, args.long_edge / max(w, h))
        size = (max(1, round(w * scale)), max(1, round(h * scale)))
        prepared = img.convert("RGB")
        if scale < 1.0:
            prepared = prepared.resize(size, Image.LANCZOS)
        plain = os.path.join(args.out, f"{fid}.png")
        grid = os.path.join(args.out, f"{fid}_grid.png")
        prepared.save(plain)
        draw_grid(prepared, cols, rows).save(grid)
        if img.mode not in ("RGB", "RGBA", "L"):
            manifest["warnings"].append(f"{fid}: source mode {img.mode} converted to 8-bit RGB; "
                                        "judge banding and grain from the delivered file, not these PNGs")
        manifest["frames"].append({"id": fid, "source": os.path.abspath(path),
                                   "original_size": [w, h], "prepared_size": list(size),
                                   "scale": round(scale, 6),
                                   "files": {"plain": plain, "grid": grid}})

    for text in args.crop:
        cid, frame, (x, y, w, h) = parse_crop(text)
        if frame not in originals:
            sys.exit(f"{cid}: unknown frame {frame}; frames are F1..F{len(originals)}")
        src = originals[frame]
        sw, sh = src.size
        x0, y0, x1, y1 = max(0, x), max(0, y), min(sw, x + w), min(sh, y + h)
        if x1 <= x0 or y1 <= y0:
            sys.exit(f"{cid}: box {x},{y},{w},{h} is outside {frame} ({sw}x{sh})")
        if (x0, y0, x1, y1) != (x, y, x + w, y + h):
            manifest["warnings"].append(f"{cid}: box clipped to the frame edge")
        out = os.path.join(args.out, f"{cid}.png")
        src.crop((x0, y0, x1, y1)).convert("RGB").save(out)
        manifest["crops"].append({"id": cid, "frame": frame,
                                  "box_original_px": [x0, y0, x1 - x0, y1 - y0], "file": out})

    mpath = os.path.join(args.out, "manifest.json")
    with open(mpath, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)
    print(f"prepared {len(manifest['frames'])} frame(s), {len(manifest['crops'])} crop(s) -> {mpath}")
    for warning in manifest["warnings"]:
        print("warning:", warning)
    return 0


if __name__ == "__main__":
    sys.exit(main())
