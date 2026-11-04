---
id: comp-nuke-volumetric-foreground-fog-from-depth-cards
title: Fake foreground volumetric fog by placing a noise card in a depth point cloud and holding it out in deep
domain: comp
tags: [alex, levelup plus vfx, nuke, deep, volumetric fog, point cloud, nuke survival toolkit, deep-read]
applies_to: Nuke Survival Toolkit, Nuke X
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ETV1VTV0vNg, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Why: fog from a world-position pass is densest at infinity and fades toward the camera; a card lets fog be densest at a chosen spot and thin toward camera [28:03-28:35].
Steps [24:56-33:19]: import the Blender camera (USD), build deep from the depth pass, recolour, convert to points to see a point cloud, place a noise card at the chosen depth, scanline-render the card, deep-merge with hold-out, then a deep blur node controls forward and backward spread.
Colour it with ColorCorrect + big blur multiplied in; raise contrast so it is denser where the lights are; roto and grade-up the shop light so fog seems emitted by it [33:19-36:57].
Cleanup: contrast creates new hard edges, so a roughly 1.5 px blur hides them [36:57]. Crop first, or bounding boxes from glows cause stripe artifacts [27:31].

**Use it:** an option when a fog AOV or Redshift volume is too slow; needs the Nuke Survival Toolkit nodes (free).
