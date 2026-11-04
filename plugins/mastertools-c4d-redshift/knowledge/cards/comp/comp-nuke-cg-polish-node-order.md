---
id: comp-nuke-cg-polish-node-order
title: Alex's Nuke polish order for a CG render - rebuild, glows, grade, far fog, near fog, sharpen, defocus, flares, aberration, dirt, grain, output transform
domain: comp
tags: [alex, levelup plus vfx, nuke, comp order, cg polish, node order, lens fx, deep-read]
applies_to: Nuke, Blender passes
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ETV1VTV0vNg, src:yt-transcripts]
feeds: [comp, elevate]
conflicts: none
---
Final-comp order as he walks it [03:04-05:06]: shader rebuild from passes, glows on lights, main grade, deep background fog, foreground volumetric fog, sharpen, Z-defocus on the subject, lens flares, a little chromatic aberration, vignette and dust, grain, then the final colour-space conversion.
The reason for rebuilding from passes: tune lights separately (he pulled down window lights and distracting highlights, and used depth to darken the background) so attention goes to the character [02:03-02:33, 05:38].
He says his comp's final look is much darker than the working view, so keep the foreground readable at the dark end [15:03].

**Use it:** a ready checklist order for the coach's comp step and for review of a CG still: look for each stage and ask which one is missing.
