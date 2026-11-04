---
id: pipeline-union-splat-crowd-relight-from-neutral-capture
title: Union VFX relights splat crowds because they are captured under flat neutral light and rendered with the shot's own CG lights
domain: pipeline
tags: [gaussian splat, crowd, relighting, union vfx, karma xpu, david schneider, deep-read]
applies_to: Houdini Karma XPU, 4D Gaussian splats
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Ybln1zAQDVc, src:yt-transcripts]
feeds: [pipeline design]
conflicts: none
---
David Schneider (VFX and technical supervisor, Union VFX; host Mike Seymour, fxguide) says relighting was the make-or-break problem for splat crowds [06:45]. Captures are shot under completely flat, neutral light so no stage highlights or reflections are baked in [20:44]. The splats then sit in the CG stadium and are lit by the same lights, in the same render, with the same production renderer as everything else [07:50]. Splats shadow each other and the environment, and the environment shadows them. About 20 to 30 thousand were scattered in stadium seats in the example [07:50]. Cards (flat photo crowds) fail here because the baked light direction is wrong for the far side of a stadium. Captures made under real set lights could keep view-dependent speculars if no relight is needed [21:15].
Transfers: a crowd that must sit in different light directions around an arena needs neutral-lit sources, not baked lighting.

**Use it:** when judging crowd or stadium plates, check that source elements are neutral-lit and take light from the scene, not from the element.
