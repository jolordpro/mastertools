---
id: motion-maxon-studio-transition-capsule-marker-sets-cut-point-and-more-blur-iterations-fix-stutter
title: Maxon Studio transition capsules carry a layer marker where the frame is fully covered: cut there, and raise blur iterations if the blur steps
domain: motion
tags: [maxon studio, transition, layer marker, fast box blur, iterations, after effects, stutter, render time, chad perkins, deep-read]
applies_to: After Effects with Maxon Studio (2024)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=-7-foJ3thiU, src:yt-transcripts]
feeds: [motion-critique]
conflicts: none
---
Transition capsules need no start and end keyframes. A layer marker named "transition" sits where the frame is entirely covered; put the footage edit exactly there. Holding Shift while dragging snaps to that marker [18:28-19:37].
Perkins noticed a stuttering, choppy look in the default transition blur and fixed it by opening the transition, finding Fast Box Blur and raising its iterations (default was low, he guessed three to seven). More iterations render slower but animate much smoother [20:10-21:11].
Effects capsules apply two ways: as an adjustment layer over footage, or by replacing a placeholder in a nested comp (drop footage in, turn the lower layers off) [16:17-17:55].

**Use it:** blur banding or stepping in a fast move is an iterations or quality setting before it is a timing problem; check it before re-timing.
