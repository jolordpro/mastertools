---
id: comp-valentic-keep-the-look-parametric-and-scene-referred-and-balance-underneath
title: "Valentic keeps a look as live parameters, not a baked LUT, working scene-referred with a display transform last, and designs the look before balancing shots"
domain: comp
tags: [polish, dado-valentic, look-designer, parametric, scene referred, lut, cdl, workflow, colour management, resolve, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bpZ3Zuhop5s, src:yt-transcripts, src:polish-roster]
feeds: [polish-coach]
conflicts: none
---
Exported looks keep every control so they can be refined later, and he does not treat the look as a locked LUT [34:24-36:29]. Because the pipeline is scene-referred he sets the look output to Log C and puts the display transform at the end of the timeline [36:29-37:31]. He designs the look first and then corrects exposure and white balance underneath [58:19-58:49]. Balancing is quicker in ColourLab: push shots to Resolve with a CDL, then replace the show LUT node with the parametric look [58:49-1:00:23]. He also builds a halation effect but says nodes do it as well and in real time, so he would add a plugin only if it beat them [56:45-57:47].

**Use it:** Store a house look as parameters plus a documented output transform, and let each shot's balance sit before it.
