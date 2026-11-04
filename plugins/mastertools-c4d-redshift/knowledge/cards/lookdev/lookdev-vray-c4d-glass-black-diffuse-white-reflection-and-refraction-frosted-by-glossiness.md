---
id: lookdev-vray-c4d-glass-black-diffuse-white-reflection-and-refraction-frosted-by-glossiness
title: V-Ray for C4D glass: diffuse black, reflection white, refraction white; lower refraction glossiness to frost it, tint with the fog colour and set strength with depth
domain: lookdev
tags: [v-ray, chaos, glass, refraction, glossiness, fog colour, translucency, cinema 4d, deep-read]
applies_to: V-Ray for Cinema 4D (node material)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=i6zQmQD_auA, src:yt-transcripts]
feeds: [lookdev]
conflicts: none
---
Chaos V-Ray tutorial [01:15-02:59]. Diffuse can be pure black for glass, unless refraction is pure white (100 percent) [01:51]. Set reflection colour to white so reflections show fully, then raise refraction colour to white: the surface gets more transparent as it rises [01:51-02:26]. Frosted look: lower the glossiness value so it blurs [02:26]. Tint: change the fog colour in the translucency rollout; the depth value raises or lowers colour intensity [02:26-02:59]. These are V-Ray's controls and scales, not Redshift's.

**Use it:** V-Ray baseline. Redshift glass is built differently (transmission, IOR, absorption).
