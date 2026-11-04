---
id: comp-nuke-depth-fog-black-white-point-and-blur-recipe
title: Depth fog recipe - depth as mask, black point at the nearest object, white point at the farthest, fog colour from a big blur
domain: comp
tags: [alex, levelup plus vfx, nuke, depth fog, atmosphere, blur, mask, deep-read]
applies_to: Nuke
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=ETV1VTV0vNg, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Shuffle depth into RGBA and grade it so the black point is the closest object and the white point the farthest (control-click to sample; his values were in the tens of scene units, captions garbled) [20:44-22:49].
Fog colour: ColorCorrect then a large Blur (about 300) on the image; kill highlights first because they dominate the blur; bigger blur = flatter single mist colour, smaller = glow-like [21:47, 23:21-24:24].
Merge the fog through the depth mask with plus (not over) to add it [22:18]. Lowering the black point brings fog closer to camera; raising the white point moves it away [22:49]. The same mask, reversed, darkens the background (gain about 0.5-0.7) [23:21].

**Use it:** a ready recipe for a fog check in Nuke or an AE equivalent; numbers depend on the depth range of the scene.
