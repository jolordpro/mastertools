---
id: motion-curve-metrics-from-keys
title: Motion metrics from keyframes: velocity, acceleration, jerk, overshoot and pops, since no open curve-quality tool exists
domain: motion
tags: [motion, curves, velocity, acceleration, jerk, overshoot, pop, strobing, bezier]
applies_to: any
status: U
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [src:research-verticals, src:research-vfx-pipelines]
feeds: [bezier_settle.py, PLAN Phase 1]
conflicts: none
---
No open animation-curve analysis tool was found; the research proposes NumPy on the keys.
Department list for animation: arcs, pops, overshoot, contact holds, strobing at the frame rate.

**Use it:** extend bezier_settle.py with these per-channel metrics.
