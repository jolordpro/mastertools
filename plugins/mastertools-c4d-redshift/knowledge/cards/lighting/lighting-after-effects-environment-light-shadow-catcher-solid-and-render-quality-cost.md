---
id: lighting-after-effects-environment-light-shadow-catcher-solid-and-render-quality-cost
title: In After Effects 24.6.2 Advanced 3D, an Environment Light with an HDRI casts shadows onto a 3D solid set to accept shadows only, and render quality 10 versus 20 took 2 versus 6 minutes a frame
domain: lighting
tags: [after effects, environment light, hdri, shadow catcher, accepts shadows only, render quality, poly haven, deep-read]
applies_to: After Effects 24.6.2 Advanced 3D
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=B0fmI6BW7PI, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Tutos [0:34-7:04]: add a light of type Environment (needs 24.6 or newer and the Advanced 3D engine); the default HDR is used until you import your own (Poly Haven, 2K EXR chosen because 4K/8K crashed AE for him), set it as the light's source, and the HDR layer hides itself [3:50-5:00]. For a shadow catcher, add a solid, make it 3D, rotate X to -90, and under material options set Accepts Shadows to Only, so a transparent export holds model plus shadow [2:10-3:18]. To clear grain, open Render Options: quality 10 and smoothness 10 took 2 minutes for one frame; quality 20 took 6 minutes and removed almost all grain on his M1 Max MacBook Pro [5:59-7:04]. The scene was already slow to move around [1:40]. Single-machine, single-scene timings.

**Use it:** Budget about 3x time for doubling AE Advanced 3D render quality, and use the accept-shadows-only solid for a quick contact shadow in motion comps.
