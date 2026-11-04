---
id: comp-vfx-compositor-shot-day-order-and-finishing-effects
title: A film compositor builds a shot in this order: references, gathered elements, plate prep, keying, passes, 3D bits, then lens-style finishing
domain: comp
tags: [compositing, nuke, plates, clean plate, cryptomatte, deep compositing, halation, grain, crafthive, deep-read]
applies_to: Nuke-style film VFX
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=d5uP3wjc3Tc, src:yt-transcripts]
feeds: [post-composite]
conflicts: none
---
Crafthive's account of a film comp artist's flow [01:40-05:15]: find references (real photography or other films) for a look-dev or key shot, or match the look a key artist set; gather elements (roto'd or painted plate, a clean plate of the same move without actors or props, CG passes from lighting, stock elements such as dust or fire); prep (reformat, retime, reposition, denoise the plate so the CG can match it, then add one uniform film grain at the end); key; block in a rough version; handle the render passes (AOVs, Cryptomatte IDs for masks made on the fly, deep passes instead of mattes and holdouts at high-end studios); project paintings or skies on cards and spheres, and track 2D screens in; finish with bloom or exponential glow, diffusion of hot spots, halation, chromatic aberration, lens dirt, animated grain, and depth of field or motion blur (more often rendered in the CG now) [04:45]. Then render for dailies and decode supervisor notes. Ladder: roto/paint, junior-mid-senior comp, lead, supervisor, head of 2D, VFX supervisor [06:58].

**Use it:** Broadcast comps follow the same order: ground the plate, matte and passes, then lens effects last, one grain over everything. Nuke-based tool list: NukePedia, Pixel Fudger, ActionVFX, ShotDeck [09:53].
