---
id: lookdev-octane-kernels-start-direct-then-path-tracing-then-pmc-and-raise-depth-until-the-image-stops-changing
title: Octane kernel ladder: start with Direct Lighting, move to Path Tracing for glass and caustics, then PMC if caustics stay unresolved; raise bounce depth until the render stops changing
domain: lookdev
tags: [octane, unity, kernels, direct lighting, path tracing, pmc, depth, caustic blur, gi clamp, deep-read]
applies_to: OctaneRender for Unity (2017)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=RtFA9RU-Vdo, src:yt-transcripts, https://www.youtube.com/watch?v=8zCqKpeF5Uc]
feeds: [coach]
conflicts: none
---
Eric Keller (Otoy video, 2017). Direct lighting is the fast default but not unbiased; path tracing gives physically right specular and caustics; PMC resolves caustics and tricky light (energy beam in glass tube) better [01:11-04:25]. Try them in that order as the scene demands [04:25]. Max samples is the main setting: start about 500 and raise if noisy [05:28]. Specular, glossy and diffuse depth: set to 1 and raise each until the image stops changing; at specular 1 the glass robot turns black [05:58-07:33]. Path tracing at 1200 samples; caustic blur reduces noise in caustics but softens them; GI clamp lowers render time but removes caustics if too low [07:37-09:07]. PMC example: 2048 samples, caustic blur 0.15 [09:38].

**Use it:** Teaching pattern for Redshift bounce counts: raise until no visible change. Related: lighting-tune-bounce-counts-by-viewing-each-indirect-pass.
Transcript support: Direct lighting is the default; path tracing allows more bounces and a brighter, more realistic image but renders slower. (https://www.youtube.com/watch?v=8zCqKpeF5Uc [02:38-03:43])
