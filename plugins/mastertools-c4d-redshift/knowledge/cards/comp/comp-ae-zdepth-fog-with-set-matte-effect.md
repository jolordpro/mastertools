---
id: comp-ae-zdepth-fog-with-set-matte-effect
title: Fake atmospheric fog by driving each pass's alpha with the Z-depth through the Set Matte effect, after crushing the Z-depth with Curves
domain: comp
tags: [after effects, z-depth, set matte, atmospheric perspective, fog, curves, cgstirk, deep-read]
applies_to: After Effects (2019)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=AxviuFLniB8, src:yt-transcripts, https://www.youtube.com/watch?v=DVJOZzRzlGg, https://www.youtube.com/watch?v=-32g9bYyZuc]
feeds: []
conflicts: none
---
CGStirk [04:37-07:12, 21:16-22:19]. Crush the Z-depth layer with Curves, stopping just before it clips: more contrast on Z-depth reads as thicker fog. A track matte per pass would need a Z-depth copy over every pass, so put the Set Matte effect on each pass instead: matte layer = Z-depth, Use For Matte = Luminance, tick 'Effects and Masks' so the Curves counts, and Invert so the far areas fade. Copy the effect to all passes except the Z-depth layer. Trap: this only makes the CG transparent, so anything behind it (trees, sky, buildings) shows through; fix by duplicating a ship alpha layer, filling it a flat sample of the sky, and putting it under the GI as a ship-sky matte. To thin the fog, crush the whites less.

**Use it:** Use for far-away CG that should sit in haze when no depth-based fog was rendered. Check Z-depth showing through the object before sign-off.
Transcript support: the same Set Matte (inverted luma, effects and masks ticked) route with a Fractal Noise fog solid and a depth-masked Compound Blur (https://www.youtube.com/watch?v=-32g9bYyZuc [21:15])
