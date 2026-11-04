---
id: comp-kelly-viewing-lut-for-vfx-is-the-full-pipeline-and-look
title: Kelly gives VFX vendors a viewing LUT made from the whole colour pipeline plus the look, and asks for the same colour space back
domain: comp
tags: [cullen kelly, vfx, viewing lut, handoff, color management, look, exr, round trip, polish, cullen-kelly, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=upUAulx7sGI, src:yt-transcripts, src:polish-roster]
feeds: [shakedown, CHECKS, redshift]
conflicts: none
---
Kelly [49:20-53:30]: VFX is almost never finished when colour starts, so he sets up the pipeline and a look with the creative team first (macro beats micro: a fix that works across all shots beats shot-level fixes). He then bakes pipeline plus look into a LUT that takes the vendor's working space to Rec 709 (or another display standard) so they judge their work as it will look in the grade, avoiding seams that only show later. He accepts whatever space the vendor wants (e.g. Aces linear) with one condition: they must return what he sent, same space, so the original camera asset can be swapped for the VFX version and the grade holds.
EXR that "grades worse than camera raw" [54:03-55:37]: his two checks are that the vendor kept the colour space intact and that the linear EXR is input mapped back into a log-style grading space; a mismatch is a bug in the chain, not a property of EXR.

**Use it:** the render handoff note for comp: ship a preview LUT with the look baked in, and require the return in the same colour space as sent.
