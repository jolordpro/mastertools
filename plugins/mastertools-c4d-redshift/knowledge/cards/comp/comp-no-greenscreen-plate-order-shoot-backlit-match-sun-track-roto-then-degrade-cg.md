---
id: comp-no-greenscreen-plate-order-shoot-backlit-match-sun-track-roto-then-degrade-cg
title: Greenscreen-free composite order: shoot against clean contrast, roto with AI, track the real camera, match the sun in 3D, add lens flaws and grain last
domain: comp
tags: [[rotoscoping, camera-tracking, magic-mask, relighting, lens-imperfection, grain, unreal, fusion], deep-read]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=lVJEzuydOcU, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Kevin Vandermarliere (YouTube creator, sells a course): for a backlit-sun shot without a screen he lists [02:40-07:49]: even background, enough light and good contrast so AI roto works [03:11-03:41]; Resolve Magic Mask applied in parts for a clean cut [03:41]; consider AI relighting (SwitchLight) which wants flat light on the subject to make passes [04:14]; track the real camera with a 3D camera tracker, fine-tune alignment and scale, so perspective shifts are right and not a 2D card in 3D [05:15-05:45]; put a human-size reference at the actor position and place a digital sun in roughly the real sun's position [06:48-07:19]; render in Unreal with Lumen; then in Fusion colour-match, add vignette, chromatic aberration and grain so CG blends [07:49-08:14].

**Use it:** Order for a plate-plus-CG test; the last step (degrade CG to the lens) is the one worth keeping on any composite.
