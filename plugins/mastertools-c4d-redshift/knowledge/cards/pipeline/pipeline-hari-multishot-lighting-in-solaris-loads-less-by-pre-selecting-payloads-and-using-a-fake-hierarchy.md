---
id: pipeline-hari-multishot-lighting-in-solaris-loads-less-by-pre-selecting-payloads-and-using-a-fake-hierarchy
title: For multi-shot lighting in Solaris, cut load time by choosing what loads (look-dev, grooms, textures) before the stage loads, building USD on the fly from cameras, and using a hollow prim hierarchy for light linking
domain: pipeline
tags: [flavien-rojon, hari, solaris, lighting, multishot, configure stage, mute layers, light linking, shot group, deep-read]
applies_to: Houdini Solaris, USD
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=Dd1eYWpgpkw, src:yt-transcripts]
feeds: []
conflicts: none
---
Multi-shot scenes force loads and unloads of textures, grooms, scatter and FX just to change a light colour or shadow [18:31-19:04]. Configure Stage can take a list of USD paths to mute; PDG builds that list (cast assets minus the ones to keep, such as ground and trees) before loading, so the first load is lighter [19:04-20:36]. A custom USD Builder takes cameras from shot group to shots plus the common set, so artists do not switch manifests per shot [20:48-21:40]. A 'fake hierarchy' recreates only prim paths, with no types, kinds or properties, so 3,000 prims cost nothing and light linking is instant [21:40-22:44]. Scene is split into a shot-group graph (set, cameras, all prims; light edits and light linking published to all shots) and one graph per shot (camera, frame range, animation) [23:16-24:18].

**Use it:** Pattern for scene assembly feeding a lighting step in a render platform.
