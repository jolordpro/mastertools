---
id: comp-render-characters-isolated-no-holdout-expanded-depth-and-shading-masks
title: DillonGoo renders characters isolated without holdouts, adds expanded depth and shading masks, and does holdout in After Effects
domain: comp
tags: [cody winchester, dylan goo, dillongoo studios, blender conference 2024, holdout, depth pass, inpaint, shading mask, id matte, fx naming, deep-read]
applies_to: Blender to After Effects
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aDsyNfISVLA, src:yt-transcripts]
feeds: [comp, CHECKS]
conflicts: none
---
Winchester [32:59-35:34]: passes are split into background, effects and each character. Characters have no holdout in 3D; holdout happens in AE using depth. Shading is a black-and-white mask and light/shadow colours separately. The mask is expanded past the alpha with an inpaint node, because blurring white-to-black edges gives a halo.
Depth is exported twice; the second removes pixels with alpha under one and is inpaint-expanded, so feathered depth and distorted characters do not corrupt the holdout.
FX passes use two-letter tags (glow, blur or nothing, under or over) so a script puts them above or below the character and hints what to apply.

**Use it:** for layered character comps, export clean expanded depth and shading mattes and use a naming tag for layer order.
