---
id: lighting-product-studio-hdri-fill-plus-targeted-area-lights
title: Product lighting recipe: a studio HDRI as invisible fill, targeted area lights for the shaping, a gradient backdrop
domain: lighting
tags: [product lighting, hdri fill, area light, target tag, hidden hdri, gradient backdrop, deep-read]
applies_to: Cinema 4D + Octane
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=siNE2SEgD7E, src:yt-transcripts]
feeds: [redshift, elevate]
conflicts: none
---
Setup order [02:10-05:21]: black texture environment for the visible background, studio HDRI as a separate environment that lights but is hidden from camera ("visible environment" kept on the black one), camera at 150 mm focal length pulled back to frame, area lights with a Target tag on the product and camera/shadow visibility off. The HDRI fills in so the lights only add accents and some randomness stays in the lighting [04:19-04:49].
A dark-to-light gradient backdrop is made with a 2D gradient texture and its black slider and angle [05:21, 07:29]. When a look needs a colour, turn the HDRI power down first to get deep shadows, then restore it to fill what the lights miss rather than adding another light [11:44-13:15].

**Use it:** the same structure carries to Redshift (dome with camera visibility off for fill, rect lights with a target aim for accents); verify names against the Redshift ledger before use.
