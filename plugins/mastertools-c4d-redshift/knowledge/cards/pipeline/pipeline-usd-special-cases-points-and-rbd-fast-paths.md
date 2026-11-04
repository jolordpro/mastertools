---
id: pipeline-usd-special-cases-points-and-rbd-fast-paths
title: Write special export paths for points and RBD; piping points directly was about 20 times faster, and skeletons suit millions of RBD pieces
domain: pipeline
tags: [usd, rbd, skeleton, point instancer, performance, export, luca scheller, deep-read]
applies_to: Houdini Solaris / OpenUSD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=VSE7ayrRStg, src:yt-transcripts]
feeds: []
conflicts: none
---
For point instances, skipping copy-to-points and sending points with prototypes straight to USD was about 20 times faster, at the cost of packed-prim access [46:10-46:42]. For RBD with millions of pieces, avoid millions of prims; use skeletons (they store only transforms and deform the mesh) and pre-process in SOPs/VEX, importing only what is needed then layering back [47:13-48:17]. Result was close to real time with many packed transforms [48:17-48:48]. Pipeline should write specific exports per data type [46:10].

**Use it:** For heavy dynamics handoff, ask what type it is first, then use the matching export.
