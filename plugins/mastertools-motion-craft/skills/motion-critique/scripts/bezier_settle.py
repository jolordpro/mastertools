#!/usr/bin/env python3
"""Perceived timing of a CSS cubic-bezier: when does it *look* finished?

Usage: bezier_settle.py x1 y1 x2 y2 [duration_ms] [distance_px] [fps]
Prints the time-fraction (and ms, if a duration is given) at which progress
reaches 50/90/95/99%, peak velocity position, overshoot, and, if a distance is
given, when the element is within 1px of rest. With a duration it also prints
how much travel lands in the first frame (fps defaults to 60; pass 0 for no
distance). Over 40% in frame 1 reads as a cut. Stdlib only.
"""
import sys

def bez(a, b, t):
    return 3 * (1 - t) ** 2 * t * a + 3 * (1 - t) * t * t * b + t ** 3

def t_for_x(x1, x2, x):
    lo, hi = 0.0, 1.0
    for _ in range(60):
        m = (lo + hi) / 2
        lo, hi = (m, hi) if bez(x1, x2, m) < x else (lo, m)
    return lo

def main(argv):
    if len(argv) < 4:
        print(__doc__); return 2
    x1, y1, x2, y2 = map(float, argv[:4])
    dur = float(argv[4]) if len(argv) > 4 else None
    dist = float(argv[5]) if len(argv) > 5 and float(argv[5]) > 0 else None
    fps = float(argv[6]) if len(argv) > 6 else 60.0
    if not (0 <= x1 <= 1 and 0 <= x2 <= 1):
        print("x1 and x2 must be in [0,1]"); return 2
    N = 4000
    samples = [(bez(x1, x2, i / N), bez(y1, y2, i / N)) for i in range(N + 1)]
    def first_time(p):
        for x, y in samples:
            if y >= p:
                return x
        return 1.0
    fmt = lambda f: f"{f:.3f}" + (f"  ({f * dur:.0f} ms)" if dur else "")
    print(f"cubic-bezier({x1},{y1},{x2},{y2})" + (f", {dur:.0f} ms" if dur else ""))
    for p in (0.5, 0.9, 0.95, 0.99):
        print(f"  {int(p * 100):>2}% of travel at time {fmt(first_time(p))}")
    best = max(range(N), key=lambda i: (samples[i + 1][1] - samples[i][1]) / max(samples[i + 1][0] - samples[i][0], 1e-9))
    print(f"  peak velocity at time {fmt(samples[best][0])}")
    over = max(y for _, y in samples) - 1
    print(f"  overshoot: {over * 100:.1f}%" if over > 1e-6 else "  overshoot: none")
    if dur:
        tx = min(1.0, (1000.0 / fps) / dur)
        f1 = bez(y1, y2, t_for_x(x1, x2, tx))
        note = "  (over 40%: reads as a cut; lengthen or soften)" if f1 > 0.4 else ""
        print(f"  frame 1 at {fps:g}fps ({1000.0 / fps:.1f} ms): {f1 * 100:.1f}% of travel{note}")
    if dist:
        within = 1 - 1 / dist
        print(f"  within 1px of rest ({dist:.0f}px move) at time {fmt(first_time(within))}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
