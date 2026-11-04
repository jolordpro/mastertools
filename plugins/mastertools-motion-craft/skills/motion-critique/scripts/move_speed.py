#!/usr/bin/env python3
"""Judder check for a straight move: is its speed safe at this frame rate?

Usage: move_speed.py distance_px frames fps [frame_width_px] [pattern_px]
       move_speed.py --selftest
Prints pixels per frame and, for a fractional speed, its two symptoms: the
sub-pixel phase cycle (rendered normally, a thin stroke pulses in brightness)
and the step pattern if positions snap to whole pixels (an uneven cadence).
Then the seven-second rule (a full frame width in no less
than 7 s; RED states it for 24 fps with a 180-degree shutter), and, with a
pattern period, the apparent motion of a repeating texture (stripes, grids,
halftone, LED walls): near 0 it freezes, past half a period it runs backwards.
Linear speed only: for an eased move, pass the distance and frames of its
fastest stretch. A negative distance (a leftward crawl, a credit roll typed as
-1440) is judged by its size. Stdlib only.
"""
import math
import sys

def analyse(dist, frames, fps, width=1920.0, period=None):
    v = abs(dist) / frames                     # direction doesn't change judder
    snap = lambda x: math.floor(x + 0.5)       # half-up, as a renderer snaps
    steps = [snap(v * (i + 1)) - snap(v * i) for i in range(min(frames, 12))]
    frac = lambda x: x - math.floor(x + 1e-9)
    cycle = next((n for n in range(1, 61) if frac(v * n) < 1e-6 or frac(v * n) > 1 - 1e-6), None)
    phases = [frac(v * i) for i in range(min(cycle or 6, 6))]
    out = {"v": v, "steps": steps, "even": len(set(steps)) == 1,
           "whole": abs(v - round(v)) < 1e-6,
           "cycle": cycle, "phases": phases,
           "peaks": [max(p, 1 - p) for p in phases],   # peak coverage of a 1 px stroke
           "cross_s": width / (v * fps) if v else float("inf")}
    if period:
        r = v % period
        ap = r - period if r > period / 2 else r
        if abs(ap - v) < 1e-6:
            note = "reads correctly"
        elif ap < 0:
            note = "reads as moving backwards (wagon wheel)"
        elif ap < 0.1 * period:
            note = "reads as frozen or crawling"
        else:
            note = "reads slower than it moves"
        out["apparent"], out["pattern_note"] = ap, note
    return out

def report(dist, frames, fps, width=1920.0, period=None):
    a = analyse(dist, frames, fps, width, period)
    print(f"{dist:g} px over {frames} frames at {fps:g} fps: {a['v']:.3f} px/frame"
          + (" (negative direction)" if dist < 0 else ""))
    if not a["whole"]:
        rep = f"repeats every {a['cycle']} frames, {fps / a['cycle']:.1f} Hz" if a["cycle"] else "no short repeat"
        print(f"  sub-pixel phase: {' '.join(f'{p:.2f}' for p in a['phases'])} ({rep}); a 1 px stroke peaks at "
              f"{' '.join(f'{q:.0%}' for q in a['peaks'])}: brightness flicker")
        print(f"  if snapped to whole pixels: steps {' '.join(map(str, a['steps']))}: uneven cadence (stutter)")
        options = sorted({max(1, math.floor(a["v"])), math.floor(a["v"]) + 1})
        print("  fix both with a whole-pixel speed: "
              + " or ".join(f"{o} px/frame ({max(1, round(abs(dist) / o))} frames)" for o in options))
    else:
        print(f"  whole-pixel speed: every frame steps {a['steps'][0]} px; no sub-pixel flicker")
    rule = "" if a["cross_s"] >= 7 else "  (faster than the seven-second rule: judders on detailed images, more at 24p)"
    print(f"  crosses a {width:g} px frame in {a['cross_s']:.1f} s{rule}")
    if period:
        print(f"  {period:g} px pattern: apparent {a['apparent']:+.2f} px/frame, {a['pattern_note']}")
    return a

def selftest():
    a = analyse(48, 48, 24)                     # 1 px/frame: whole and even
    assert a["whole"] and a["even"], a
    b = analyse(64, 48, 24)                     # 1.333 px/frame: the classic vanishing line
    assert not b["whole"] and not b["even"] and b["steps"][:3] == [1, 2, 1], b
    assert b["cycle"] == 3 and [round(q, 3) for q in b["peaks"]] == [1.0, 0.667, 0.667], b
    c = analyse(1920, 48, 24)                   # 2 s across the frame: fails 7 s
    assert c["cross_s"] < 7, c
    d = analyse(1920, 168, 24)                  # exactly 7 s at 24 fps: passes
    assert abs(d["cross_s"] - 7) < 1e-9, d
    e = analyse(110, 10, 30, period=12)         # 11 px/frame on a 12 px pattern: backwards
    assert e["apparent"] < 0 and "backwards" in e["pattern_note"], e
    f = analyse(120, 10, 30, period=12)         # 12 px/frame: one full period, frozen
    assert abs(f["apparent"]) < 1e-9 and "frozen" in f["pattern_note"], f
    g = analyse(10, 10, 30, period=12)          # 1 px/frame on a 12 px pattern: slow, not aliased
    assert g["pattern_note"] == "reads correctly", g
    h = analyse(80, 10, 30, period=12)          # 8 px/frame: aliases to -4, backwards
    assert abs(h["apparent"] + 4) < 1e-9, h
    i = analyse(-1440, 1080, 23.976)            # leftward 60 s crawl: same as +1440, passes 7 s
    assert i["cross_s"] > 7 and i["steps"] == analyse(1440, 1080, 23.976)["steps"], i
    print("selftest: PASS (9 cases)")
    return 0

def main(argv):
    if argv[:1] == ["--selftest"]:
        return selftest()
    if len(argv) < 3:
        print(__doc__); return 2
    try:
        dist, frames, fps = float(argv[0]), int(argv[1]), float(argv[2])
        width = float(argv[3]) if len(argv) > 3 else 1920.0
        period = float(argv[4]) if len(argv) > 4 and float(argv[4]) > 0 else None
    except ValueError:
        print("distance, fps, width and pattern are numbers; frames is a whole number\n" + __doc__); return 2
    if frames < 1 or fps <= 0:
        print("frames must be >= 1 and fps > 0"); return 2
    report(dist, frames, fps, width, period)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
