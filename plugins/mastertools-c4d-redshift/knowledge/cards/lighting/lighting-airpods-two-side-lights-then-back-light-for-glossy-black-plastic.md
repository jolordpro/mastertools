---
id: lighting-airpods-two-side-lights-then-back-light-for-glossy-black-plastic
title: "HTArchviz beginner: glossy black earbuds read well with two side lights, a low-diffuse polish on the reflective plastic, and a third light placed behind"
domain: lighting
tags: [airpods, product-lighting, vray, 3ds-max, beginner, black-plastic, deep-read]
applies_to: 3ds Max V-Ray
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=nUk3Zs91kZU, src:yt-transcripts]
feeds: [elevate]
conflicts: none
---
Setup in 3ds Max V-Ray: camera first, safe-frame with a grid to check centring [04:44-05:15]. Two instanced side lights for a straight-on camera, set to equal intensity (he lowered 10x) [08:27-09:58].
Materials: black plastic needs reflection with highlight, silicone has lower glossiness, and a very reflective plastic has full reflection with no gloss spread [17:48-19:55]. Chrome parts no Fresnel, gloss 0.7 [19:55-20:27]; indicator spot as green glass [20:58-21:59].
A top light straight above made a bad blob on the case; angle it behind instead and drop its specular, then make lights invisible to camera [25:06-27:14]. Three lights total, a few minutes of render, output with alpha [28:25-30:29].
Beginner channel, V-Ray, first video; low confidence.

**Use it:** Glossy dark product shots: build from side strip lights, add a rim/back light last, and check reflections in the camera frame, not just the light angle.
