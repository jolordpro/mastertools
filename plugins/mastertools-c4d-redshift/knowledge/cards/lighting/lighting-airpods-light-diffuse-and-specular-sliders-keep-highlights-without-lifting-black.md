---
id: lighting-airpods-light-diffuse-and-specular-sliders-keep-highlights-without-lifting-black
title: "HTArchviz beginner: use the light's own diffuse and specular multipliers to rebalance a dark product instead of just raising intensity"
domain: lighting
tags: [airpods, lighting, specular, diffuse, vray, beginner, deep-read]
applies_to: 3ds Max V-Ray
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=nUk3Zs91kZU, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
After lowering a top-light specular the picture went dark; instead of exposure he raised the light's diffuse multiplier (to about 1.5) so the base colour came back while reflections stayed [22:29-23:33]. Turning the light's reflection effect off made the material look too matte, turn it on and set specular about 0.8 and diffuse about 2 as the final feel [23:33-24:34].
Specular multiplier 2.5 down to 1.5 removed an over-hot highlight [26:44-27:14].
Redshift lights have separate diffuse and specular multipliers too; ledger not checked, neutral.

**Use it:** Tune diffuse and specular contribution per light to fix hot highlights without changing key brightness.
