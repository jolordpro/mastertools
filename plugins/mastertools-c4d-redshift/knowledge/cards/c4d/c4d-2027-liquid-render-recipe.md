---
id: c4d-2027-liquid-render-recipe
title: Liquid FX render recipe: mesh the main group, shape foam and bubbles separately, use motion blur on foam spheres and more refraction trace depth
domain: c4d
tags: [liquid, redshift, foam, bubbles, motion blur, refraction, trace depth, cloner]
applies_to: Cinema 4D 2027.0, Redshift 2027.0
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=FmaKhqSITFQ, src:yt-transcripts]
feeds: [lookdev, coach]
conflicts: none
---
Mesh the main particle group alone, smooth or tessellate later [30:46-31:49]. Spray, foam and bubbles come as spheres by default; the RS Object tag changes their size [31:49-32:52].
Foam: leave as tiny spheres and let motion blur hide them, or mesh with volume builder and measure, give it SSS and a Maxon noise [33:23-33:57]. Bubbles: clone three sphere sizes onto the cache in multi-instance for varied sizes, and give them their own refraction material [34:31-35:33].
Liquids inside liquids need a high refraction trace depth to avoid dark patches [36:03-36:34].

**Use it:** the coach gives this recipe; the estimator should expect higher trace steps and motion blur cost.
