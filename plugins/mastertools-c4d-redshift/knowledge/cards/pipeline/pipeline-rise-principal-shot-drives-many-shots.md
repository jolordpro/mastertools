---
id: pipeline-rise-principal-shot-drives-many-shots
title: A 'principal shot' is a never-rendered scene that edits many linked shots at once, with a shot-switch node for per-shot overrides
domain: pipeline
tags: [rise, principal shot, shot switch, usd, sequence lighting, context options, layout, deep-read]
applies_to: Houdini Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jpbMbafS9FY, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
Rise's shot machine (2017) rendered dozens of shots from one hip file [04:54]. In USD this became the principal shot: never rendered, but any shot linked to it in the database shows up in a shot menu (a context option) [25:58-26:29].
One artist can export layers for many shots at once, for layout, FX and lighting, not just lighting [26:29]. A shot-switch node confines an edit (extra barrels in one shot) to that shot only [25:27]. The harbor lighting scene covered 50+ shots with one base setup, and the right colour-config LUT switched per shot [33:14-34:17].
The connection is per department (effects, light, layout), and can be removed so a shot leaves the principal scene [59:31].

**Use it:** Same idea for a sports package: one master scene for a template, per-episode overrides behind a switch.
