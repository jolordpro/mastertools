---
id: pipeline-siggraph-2026-gaussian-splat-speed-papers-and-simulation-speedup-claims
title: SIGGRAPH 2026 pitches on splats and sims: 3DGS densification in 50 s, 8K tiling 2.5x faster, 97% fewer Gaussians, half-billion real-time, fluid and cloth speedups
domain: pipeline
tags: [pipeline, siggraph, papers, gaussian splatting, simulation, speed, research-radar, deep-read]
applies_to: research papers (July 2026)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=u6xhzA40Af0, src:yt-transcripts]
feeds: []
conflicts: none
---
Claims as pitched (auto captions, unverified). 3DGS: a densification method converging on Mip-NeRF 360 in 50 seconds [24:06-24:37]; rendering half a billion Gaussians in real time with unbiased sampling and GPU atomics [24:37-25:18]; 8K tiling dedup giving 2.5x [25:18-25:57]; a mobile pipeline that renders fewer pixels [25:57]; 97% fewer Gaussians [2:19:14]; a fixer that cleans off-trajectory artifacts using a video model [1:35:27]; real-time 4K light-field rendering by reusing work across views [18:41]. Simulation: fluid solver "100 times faster" for thin structures [41:00]; spatial-temporal FLIP with time steps 10x larger and multi-billion particles [56:34]; collision-free (IPC-style) simulation 100x faster than GPU IPC, and 3x adaptive [2:05:06-2:06:18]; MPM-light up to 16x faster [2:15:58]; 12x faster fluid/sand coupling with zero volume loss [57:09-57:41]; BS-cloth twice as fast as linear FEM [1:32:11-1:32:45]. Terrain erosion with momentum transport [58:12]; a 6M-DOF articulated solver at interactive rates [1:30:39-1:31:10].

**Use it:** Not shipped; use as a map of where speedups are expected, and verify figures before quoting them.
