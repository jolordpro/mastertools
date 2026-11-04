---
id: c4d-geometry-solver-with-the-scene-nodes-memory-node-init-solve-store-loop
title: C4D geometry solver (like a Houdini SOP solver) - a Nodes Mesh with a Memory node keeps last frame's geometry so deformers can accumulate
domain: c4d
tags: [scene-nodes, geometry-solver, memory-node, simulation, dominik-ruckli, cinema-4d-2025, deep-read]
applies_to: Cinema 4D 2025 scene nodes (video 2025-09-17)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=Iy2FAJbbyrY, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Dominik Ruckli, uploaded 2025-09-17. Only a tiny amount of nodes; everything else is normal C4D.
- Idea: frame 0 reads an initial state, a solve step changes it, the result is stored, and each later frame reads the stored result and solves again [00:33-02:07].
- Build: two Connect objects (weld off) named init state and solved state; a Nodes Mesh holds the store. In nodes add two Object Link inputs (init, solved) and a Memory node switched from vector to geometry object. Init goes into the memory's initial slot, the solved geometry into next, and the previous-state output is the node output [02:39-06:27].
- Frame 0 has no previous state, so it outputs the initial one; frame 1 outputs frame 0's result, which is fed to the solved state through an Instance set to plain Instance (not render instance or multi-instance) [05:54-06:58].
- Hide init and solve objects so you see only the stored result; for finals show the first solved step or frame 0 is the initial geometry [07:32-08:34].
- Any deformer in the solve step now accumulates: displacer, collision deformer with a sphere, jiggle for delay, and a Surface deformer set to initialize with about 2 percent strength pulling back to the initial shape (a fake soft body) [10:38-13:18].

**Use it:** Proof of concept for procedural growth and sticky sims; solver chains are playhead-dependent, so cache before farm rendering.
