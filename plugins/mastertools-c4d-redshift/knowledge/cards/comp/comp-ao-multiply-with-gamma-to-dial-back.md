---
id: comp-ao-multiply-with-gamma-to-dial-back
title: Ambient occlusion goes in with multiply, then a color correct gamma of about 3.5-4 dials it back to the brief
domain: comp
tags: [sarkamari, reza, nuke, arnold, merged aov, ambient occlusion, multiply, gamma, color correct, deep-read]
applies_to: Nuke
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=xwD_UPqbmCU, src:yt-transcripts]
feeds: [comp, CHECKS]
conflicts: none
---
Reza [17:27-19:00]: lights add (plus), AO multiplies. It darkens too much; avoid the mix slider and throw in a Color Correct with gamma around 3.5-4 to weaken AO to what the brief wants. Note: in Redshift cards the AO AOV is flagged as a trap; check redshift-ao-aov-is-a-trap.

**Use it:** comp checks: AO is multiplied (not added) and has a gamma control for strength.
