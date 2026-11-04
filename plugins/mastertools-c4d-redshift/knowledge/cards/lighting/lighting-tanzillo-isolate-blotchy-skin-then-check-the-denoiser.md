---
id: lighting-tanzillo-isolate-blotchy-skin-then-check-the-denoiser
title: Blotchy skin in one pose: isolate the light, kill spec, bump and SSS in turn, swap to a default shader, then turn the denoiser off
domain: lighting
tags: [mike-tanzillo, critique, sss, denoiser, aov, skin, troubleshooting, deep-read, lighting-critique]
applies_to: Arnold, Blender
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=sjiuEeAp-JE, src:yt-transcripts]
feeds: [shakedown, coach]
conflicts: none
---
Mike Tanzillo [10:25-17:10], order of checks: find which light causes it, go through each AOV, turn off spec, then bump, then subsurface. Next put a plain default shader on to see whether it is geometry or UVs. A student then spotted the likely cause and he agreed [16:39-17:10]: noisy SSS plus a denoiser gives splotches. Turn the denoiser off, or add samples so it has less to do.
If only a few frames show it, he would blur that AOV under a bezier mask in comp [16:06]. Moving the light slightly also works when the pose is brief and the hit angle is the trigger [11:27].

**Use it:** Add the denoiser-off test to any skin blotch triage before changing shaders. Pairs with the denoiser flicker card.
