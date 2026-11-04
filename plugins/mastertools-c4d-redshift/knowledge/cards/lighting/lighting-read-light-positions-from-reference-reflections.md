---
id: lighting-read-light-positions-from-reference-reflections
title: Rebuild a reference's lighting by reading where its reflections and highlights sit, one targeted area light per highlight
domain: lighting
tags: [[product, reference, chrome, octane, area-light, learnplasticity], deep-read]
applies_to: Cinema 4D + Octane (principle any)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=HtDz9bOJT_E, src:yt-transcripts]
feeds: [coach, elevate]
conflicts: none
---
Nikita Kapustin (LearnPlasticity): put the reference beside the render and look at where reflections and highlights fall; a light lives there. Sky power goes to 0, HDRI black, and each highlight (front-right, top edge, sharp bottom line, left) gets its own targeted area light [07:26-08:26]. Lights are first built rough, then balanced against each other at the end [11:33]. If a side is dark, duplicate a light to the other side, change the gradient direction, add roughness to the glossy material to soften a hard edge [12:06-13:09].
Camera: about 150 mm focal length for a flat, undistorted product look [03:11].

**Use it:** For a product hero still, annotate the reference with highlight positions first, then place lights to match before touching values.
