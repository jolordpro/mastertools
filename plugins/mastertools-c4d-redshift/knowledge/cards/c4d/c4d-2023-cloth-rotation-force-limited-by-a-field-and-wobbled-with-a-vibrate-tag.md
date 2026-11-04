---
id: c4d-2023-cloth-rotation-force-limited-by-a-field-and-wobbled-with-a-vibrate-tag
title: A twisting cloth with no keyframes: Rotation force on the Z axis limited by a spherical field with a random field multiplied in, and a Vibrate tag slowly moving the axis
domain: c4d
tags: [cloth, rotation force, spherical field, random field, vibrate tag, smoothing iterations, damping, popping, deep-read]
applies_to: Cinema 4D 2023 new simulation system, cloth (School of Motion, EJ, Oct 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dHQWVXWbsEM, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
EJ [12:51-19:18]. The Rotation force spins around its own Z axis, so turn Z up. Limit it with a spherical field in the force's Fields tab (rotation only inside) and raise angle speed to 150 to 300 [13:02-15:08]. To vary strength, add a Random field to the sphere, blend Multiply, raise scale, sharpen with remap inner offset and animate its speed [15:39-16:43].
Popping fix [14:04-14:36]: Project settings, Simulation: substeps give accuracy, iterations multiply them, smoothing iterations is the one to raise for popping; damping removes energy so it looks underwater and also helps. Collision passes need not rise unless cloth intersects.
Billow look: a Vibrate animation tag on the rotation force (frequency about 0.1) keeps the Z axis moving; offset the spherical field to the side so the twist happens off-centre [17:14-18:47].

**Use it:** Procedural twist and billow on drapes or flags with no keyframes; check popping against smoothing iterations first.
