---
id: redshift-light-groups-must-sum-to-beauty
title: Light-group passes should add back to the beauty; check the sum on a draft
domain: redshift
tags: [light groups, aov, beauty, sum, comp, compositingmentor, add, rebuild beauty, relight in comp, check sum equals beauty, unassigned lights black, deep-read, tony lines, nuke, rebuild]
applies_to: Redshift 2026
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=q5Pyx7Jb5Xo, src:research-youtube, src:research-vfx-pipelines, https://www.youtube.com/watch?v=IjFXi2axl-8, src:yt-transcripts, https://www.youtube.com/watch?v=ZrOiwMSGmIw, https://www.youtube.com/watch?v=ETV1VTV0vNg, https://www.youtube.com/watch?v=oANXbk9OUbI]
feeds: [CHECKS light-group sum, redshift, shakedown, CHECKS, comp]
conflicts: none
---
The CompositingMentor video (2025-05-27) is cited for two points: rebuilding by subtraction misbehaves, division is steadier, and mixing light groups with material AOVs clashes. Only the video's description supports it.
Merged from `comp-light-groups-sum-with-add-and-verify-against-beauty`: Steps [02:05-07:47]: create a group per light source (sun, lantern, environment); assign each light (and the world light separately); unassigned lights render black in the group passes. Render once, then in comp Add the groups together (chain Add nodes for more groups). The sum should match the beauty output exactly; compare it before changing anything [06:44-07:47]. Then grade each group alone. Examples [07:47-09:22]: switch lantern off with gain 0; environment at saturation 0.5 and gain about 0.4 for a dim room; day to moonlight by desaturating the sun, gain about 0.2, then Multiply by a bluish colour. Keyframes on those values animate lights on or off without re-rendering [09:22]. Compared with grading the whole frame, or masking areas by hand, this keeps changes per light [01:34-02:05].
Merged from `comp-light-groups-rebuild-by-plain-add`: Tony Lines (CompositingMentor): shuffle out every light group and plus them together. No multiply or divide, unlike the material AOV rebuild [01:02-02:36]. The groups and the material AOVs each rebuild the beauty on their own, and they do not add to each other [00:30]. If the sum misses anything, subtract the sum from the original beauty to get the leftovers and plus them back on [02:03]. Transfers: same check applies to Redshift light group AOVs in a C4D comp.

**Use it:** sum the group passes on the draft and report the largest per-region error against the beauty.
Transcript support: his rebuild ends with the sum equalling beauty before he rebalances; also reports camera exposure not baked into the AOV EXR (ledger-check) (https://www.youtube.com/watch?v=oANXbk9OUbI [35:14])
