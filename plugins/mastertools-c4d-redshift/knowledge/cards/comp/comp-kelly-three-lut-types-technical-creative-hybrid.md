---
id: comp-kelly-three-lut-types-technical-creative-hybrid
title: "Cullen Kelly sorts LUTs into technical, creative and hybrid, and prefers creative LUTs that stay in the working space"
domain: comp
tags: [cullen-kelly, lut, technical lut, creative lut, hybrid lut, double transform, polish, deep-read]
applies_to: DaVinci Resolve, any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=dSYTWErq0Vw, src:yt-transcripts, src:polish-roster]
feeds: [comp, coach]
conflicts: none
---
Technical LUT: moves colour space A to B with no look (Resolve's VFX IO folder, Cineon log to linear) [22:26]. Creative LUT: stays in the same space and adds character only; his DaVinci Wide Gamut 2383 LUT sits between DWG Intermediate on both sides so the pipeline is untouched [23:00-24:31]. Hybrid LUT: does both, for example the film looks in Resolve's film library that give a print look and also move film-negative log to Rec.709 [24:31-25:33]. With a hybrid LUT, leaving the output transform on double-transforms to 709 and looks wonky. His 2022 advice: use creative LUTs; hybrids tie you to one space, and colour space transforms beat technical LUTs.

**Use it:** Before dropping a LUT into a comp or grade, label it technical, creative or hybrid; a hybrid means switching off the downstream output transform. Same discipline for any look LUT applied to C4D/Redshift renders.
