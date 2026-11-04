---
id: comp-cheap-tricks-3d-tracker-fails-on-big-subjects-so-block-them-with-a-black-solid-first
title: When the 3D camera tracker fails because subjects fill the frame, cover them with a black solid, pre-comp and track again
domain: comp
tags: [3d camera tracker, tracking trick, black solid, 2d null, toComp, ground plane, deep-read]
applies_to: After Effects
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=-32g9bYyZuc, src:yt-transcripts]
feeds: [comp, pipeline]
conflicts: none
---
The bikers clip tracked badly because the subjects took up most of the frame; adding a black solid scaled over them but leaving the two edges visible, then pre-composing and tracking again gave a working solve [24:20-25:22]. Select 3 or 4 ground-plane points mid-shot, set ground plane and origin, create a solid and camera; then hide the black solid again from the original comp. For FX parenting: make a null named '2D track' with a position expression using the pick whip onto the tracker solid plus .toComp(), then parent effect layers to that null instead of making every layer 3D [25:52-26:54]. Save that comp as a starter and duplicate per variation (tornado, underwater, fire) [26:23].
Transfers: the null trick is a quick way to stick 2D elements on a tracked plate without full 3D.

**Use it:** Suggest as first aid for failed tracks and for quick 2D-to-3D parenting.
