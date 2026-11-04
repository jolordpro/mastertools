---
id: comp-nuke-beauty-rebuild-from-diffuse-gloss-passes-and-premult-trap
title: Beauty rebuild order: (diffuse direct + indirect) x diffuse colour, plus the same for gloss, plus emission; verify with a difference node; the unpremult handling is where it breaks
domain: comp
tags: [vfx showdown, nuke, beauty rebuild, diffuse direct indirect, glossy, emission, unpremult, premult, difference check, blender, deep-read]
applies_to: Nuke, Blender Cycles passes (2025)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ir1x8Si9A8k, src:yt-transcripts]
feeds: [[comp, shakedown]]
conflicts: none
---
VFX Showdown (single creator, low). Build [01:33-03:14]: plus diffuse direct and indirect, multiply by diffuse colour; same for glossy; plus emission with no in-between step; premult at the end; compare to the beauty. Failure: the rebuild does not match the beauty on a render with transparent glass, with extra edges and transparency errors [03:46-05:19]. What he found with Blender passes: unpremult only the direct and indirect passes (or only the colour passes, tested both ways) rather than "unpremult all", and turn off alpha on the merge nodes so original alpha passes through; with other renderers (Houdini, Maya) a plain unpremult works [05:19-07:54, 12:07-12:37, 15:15-16:17]. Residual mismatch was traced with a difference (minus) merge, which showed splotchy denoise differences because the passes were denoised and the beauty was not [07:23]. Then build a separate light rebuild (light groups added) and combine by dividing the shader rebuild out and multiplying the light rebuild in, check alpha is identical [08:20-10:00]. Benefit: relight, regrade the diffuse colour only, boost environment light, and the shadow-catcher pass carries colour so grading keeps coloured shadow [16:28-17:19].

**Use it:** QC gate for any comp rebuild: difference against the beauty must be near zero before grading; mismatch first suspects premult state and denoised-vs-raw passes. Complements the existing light-group rebuild cards.
