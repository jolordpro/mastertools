---
id: comp-blender-cg-over-footage-checklist-fps-levels-readout-blur-grain
title: Dropping a Blender render onto footage in After Effects: match frame rate first, match black and shadow values with Levels and the info readout, add a tiny blur (0.1-0.2) and light grain
domain: comp
tags: [max-novak, blender, after effects, interpret footage, levels, fast box blur, grain, cg comp, deep-read]
applies_to: Blender 4.x, After Effects
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=QlbZDu2tZfE, src:yt-transcripts]
feeds: [composition, CHECKS]
conflicts: none
---
Render a PNG sequence with transparency and import it as footage [08:50]. The track looked wrong because the footage was 24 fps and the sequence imported at 30; Interpret Footage, assume 24, fixed it [09:21]. Then Levels on the CG while reading the RGB values in the info panel from a shadow area (about 48-50 in his example) to match the plate [09:53-10:23]. Blender renders very sharp, so add a Fast Box Blur at about 0.1-0.2 and, if you like, a tiny bit of grain; do not overdo it [10:23-10:54]. His own verdict: shadows still a bit too rough, so the match is not perfect.

**Use it:** Frame-rate mismatch is the first QC check on any image sequence in a comp. Extend with the blur and grain finish.
