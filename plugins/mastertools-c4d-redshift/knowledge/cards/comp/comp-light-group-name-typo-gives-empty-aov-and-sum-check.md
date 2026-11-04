---
id: comp-light-group-name-typo-gives-empty-aov-and-sum-check
title: A light group AOV is only filled if the AOV name matches the group name exactly; a typo gives an empty pass that still renders; check each pass, then plus them and compare to beauty
domain: comp
tags: [sarkamari, reza, arnold, maya, light groups, lpe, aov, naming, typo, half float, nuke, plus merge, deep-read]
applies_to: Arnold in Maya, Nuke (2022); principle applies to Redshift light groups
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=_jGC7_fRlfw, src:yt-transcripts]
feeds: [[shakedown, CHECKS, comp]]
conflicts: none
---
Reza (Sarkamari, Arnold tutorial, low). Name lights by role (key, rim, env) and put the same name in the light's AOV light-group attribute [01:34-05:07]. The custom AOV is the prefix plus the group name and must match exactly; his deliberate typo produced an AOV that rendered without error but was empty, so every pass was opened in the viewer to confirm [06:20-07:55]. Settings he used for the render: 8 camera (AA) samples, diffuse 2, specular 2, diffuse ray depth 2; merge AOVs into one multichannel EXR; use a render-pass token in the file name; half precision (16-bit) when loss is not visible, 32-bit when needed [08:27-09:29]. In Nuke: merge with plus (key + rim, then plus environment) and flip between the composite and beauty (they looked identical) [11:04-13:39]. Reason for light AOVs: a client asks for stronger, greener or warmer light and a grade multiply per light does it without re-rendering [11:35-13:08]. Final grade shared between composite and beauty with a clone node (Alt-K) so one edit updates both [14:10-14:42].

**Use it:** Add a pre-render check that every light group name has a matching AOV, and a post-render check that the passes are non-black and sum to beauty.
