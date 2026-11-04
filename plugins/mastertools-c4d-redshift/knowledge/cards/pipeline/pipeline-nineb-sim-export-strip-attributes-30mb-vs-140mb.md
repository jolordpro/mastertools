---
id: pipeline-nineb-sim-export-strip-attributes-30mb-vs-140mb
title: Delete unneeded attributes before writing a sim to USD: his rain cache fell from 140 MB to 30 MB; keep pscale and velocity
domain: pipeline
tags: [nine between, houdini, solaris, usd, simulation, file size, attributes, pscale, velocity, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [CHECKS, estimator]
conflicts: none
---
A sim point cloud carries many attributes. Keeping only pscale (size) and v (velocity) cut his rain USD from about 140 MB to 30 MB, nearly five times smaller; with flip sims at gigabytes this matters more [2:10:24-2:11:26]. Particles need a pscale; if missing, each defaults to size 1 and renders as huge spheres [2:06:47].
Motion blur reads the velocity primvar (named velocities in USD), and velocity blur must be switched on in render settings [2:07:17-2:08:49]. Assign a transmissive material to get water-like drops [2:05:15].

**Use it:** For FX caches, make a size and attribute check part of publish: needed attributes only, sensible particle scale.
