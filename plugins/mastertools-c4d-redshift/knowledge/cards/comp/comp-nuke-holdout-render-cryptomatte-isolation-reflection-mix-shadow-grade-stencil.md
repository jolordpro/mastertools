---
id: comp-nuke-holdout-render-cryptomatte-isolation-reflection-mix-shadow-grade-stencil
title: Nuke comp of a Redshift shadow-catcher render: isolate object, reflection and shadow with Cryptomatte, mix the reflection down, multiply the shadow with a graded alpha, blur it, and stencil out occluders
domain: comp
tags: [nuke, cryptomatte, shadow catcher, comp, premult, merge, stencil, redshift, avfx, deep-read]
applies_to: Nuke + Redshift EXRs from Maya (video April 2020)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=aplU2CXwXLY, src:yt-transcripts]
feeds: [comp, redshift]
conflicts: none
---
AVFX [11:00-19:38]. Three inputs: plate, render, Cryptomatte. (1) Isolate the CG object by selecting it in Cryptomatte, copying its alpha onto the render, premult, merge over the plate [12:12-12:44]. (2) Isolate the reflection layer the same way (he masks with a roto shape because the shadow and reflection share one object; better to split them in Maya) and merge on top with the merge mix reduced until it matches the plate's glass transparency [13:17-15:29]. (3) Shadow: Cryptomatte or mask to isolate, then a Grade on the plate using that alpha as the mask and the multiply pulled down; if the alpha is weak, a Grade on the alpha channel boosts it; blur the alpha for a softer shadow [15:29-18:05]. (4) To remove a bit of shadow that falls on a foreground object (couch), roto a shape and use a Stencil merge instead of Over [18:36-19:38]. His own note: using Cryptomatte for this is overkill for a still, shown to explain the animated case.

**Use it:** use as the checklist for comp of a shadow-catcher plate: three separate masks, three separate strengths.
