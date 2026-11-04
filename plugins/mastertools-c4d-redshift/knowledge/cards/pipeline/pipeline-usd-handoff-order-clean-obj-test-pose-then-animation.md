---
id: pipeline-usd-handoff-order-clean-obj-test-pose-then-animation
title: Maya-to-USD hand-off order: clean OBJ to rigging and Painter, USD test-pose export before animation, XGen as render proxy, merge in Katana or Solaris
domain: pipeline
tags: [[usd, maya, handoff, rigging, xgen, lookdevx, textures, katana, solaris], deep-read]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hNzbznG0ywU, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Presenter's pipeline [00:30-05:40]: model in Maya, keep the .ma/.mb on the server, export a separate OBJ (no junk nodes) for Substance Painter and for rigging; textures in lossless TIF, PNG or EXR rather than large TGA [01:01-02:34]; LookdevX material stored in USD [02:34]. Rigging must hand over the Maya file plus a test pose set (bent arm, bent leg) exported as USD; if that exports without issues, go to animation [03:06-03:36]. Animation can swap back to a Maya reference to edit or re-export a USD sequence and replace the layer [04:07]. XGen hair goes out as a render proxy so missing XGen files do not break it [04:38]. Katana (or Solaris) merges textured model, animation, hair and FX, then lighting and comp [05:09-05:40]. Unreal MaterialX must be imported separately as .mtlx at this time [08:18-08:48].

**Use it:** A checklist of publish gates between departments.
