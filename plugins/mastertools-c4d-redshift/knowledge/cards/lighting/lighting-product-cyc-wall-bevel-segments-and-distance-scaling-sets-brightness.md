---
id: lighting-product-cyc-wall-bevel-segments-and-distance-scaling-sets-brightness
title: A cyc wall for product lighting is a plane extruded up and beveled with about 10 segments at fraction 0.25 to 0.3; scaling the room larger darkens it
domain: lighting
tags: [cyc wall, product lighting, bevel, exposure, intensity, aim constraint, area light, kurt b, deep-read]
applies_to: Maya Arnold
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=k5ArlhNwGFU, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Kurt B's product set [4:41-8:50]: with no light the render is black; add three area lights (key near the render camera, fill roughly perpendicular to it, rim behind the product) [2:35-3:39]. Intensity and exposure multiply, so leave intensity at 1 and use exposure for small numbers, instead of typing 10,000 [1:02]. He raised the key to about 14 to 16 exposure [3:39]. Rim light is what cuts the product out of the background [4:11]. For the backdrop, extrude a plane's edge into a hollow box, bevel the corner edges with 10 segments and a fraction about 0.25 to 0.3 for a rounded cyc [5:43-6:15]; raise the rim for a more gradual fall-off [6:45]. Scale the cyc larger to darken it, because it moves away from the lights [8:50]. An aim constraint from each light to a locator (aim vector 0,0,-1, not the default) keeps every light pointed at the product while you move them [7:16-8:18]. Create your own render camera; if Arnold shows the wrong camera, toggle the panel [1:33].

**Use it:** Same set in C4D: Target tag or Null aim on each light, a beveled floor-wall cyc, and darken the background by distance not by turning down every light.
