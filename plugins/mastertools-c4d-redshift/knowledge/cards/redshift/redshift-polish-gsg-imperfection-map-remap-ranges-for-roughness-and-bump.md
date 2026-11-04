---
id: redshift-polish-gsg-imperfection-map-remap-ranges-for-roughness-and-bump
title: Remap imperfection maps with a ramp before use: roughness about 20-50 percent, bump around the 50 percent "water level", not raw 0-1
domain: redshift
tags: [chad-ashley, greyscalegorilla, surface-imperfection, ramp, roughness, bump, deep-read, polish]
applies_to: Redshift in Cinema 4D
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=yFCUHeTf0mQ, src:yt-transcripts, src:polish-roster, https://www.youtube.com/watch?v=Qml8EakEAQ4, https://www.youtube.com/watch?v=pLPOcdxezgE, https://www.youtube.com/watch?v=TonSU8Ljm5c]
feeds: [lookdev, elevate]
conflicts: none
---
Chad (Greyscalegorilla, presenter named only by first name in captions) feeds black-and-white tileable imperfection maps through a ramp (visual) or Change Range (numeric), keeping the texture gamma linear as his habit [01:04-03:09]. Roughness: raw 0-1 is far too rough at white (1.0) and perfectly clean at black, so he squeezes it to roughly 20 percent at the clean end and 30 to 50 percent at the rough end, with a little clamp for contrast [04:12-05:15]. Bump: treat 50 percent grey as the surface level; remap white down to about 20 percent (to 50 range) for a pitted look, then pull the grey down for fine specks [05:15-06:15]. Change Range works the same with in/out labels (old = in, new = out) [03:09].
**Use it:** In scene checks and coach tips, flag unremapped grunge in roughness (reads too rough/clean) and suggest a ramp with a raised floor and a lowered ceiling. Check against the Redshift ledger before publishing.
Transcript support: Maxon trainer lifts the roughness floor to about 15-20 percent and sets the ramp to linear. (https://www.youtube.com/watch?v=TonSU8Ljm5c [51:55-54:29])
