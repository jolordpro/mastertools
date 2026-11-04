---
id: lookdev-rebellion-approve-assets-in-the-final-environment
title: Failure story - gold assets approved in a neutral setting looked like a blast furnace once gold reflected gold in the set
domain: lookdev
tags: [rebellion vfx, evil genius 2, gold, materials, approval, environment, solaris, deep-read]
applies_to: Houdini Solaris, Redshift
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=NNUtKYRmcjY, src:yt-transcripts]
feeds: [shakedown, lookdev]
conflicts: none
---
The client cared about the game's gold look and approved assets early in a neutral environment. When dozens of gold objects went into gold walls and floors, reflections multiplied gold on gold and the shot looked burnt; he calls it the blast furnace look and never sent it [14:34-15:36].
Each asset had its own textured gold, so one material swap would not do. Marco built a tool: one editable material node pushes changes to all selected materials live, and branches of the node tree hold versions to show the client [16:06-17:10]. In his estimation doing this by takes would be slower and harder to track [17:10].
His own hindsight: approving assets before the environment existed was a poor choice, but the schedule forced it [15:05].

**Use it:** QC rule - review reflective materials in the final environment, not on a grey stage; keep a global tweak path for materials.
