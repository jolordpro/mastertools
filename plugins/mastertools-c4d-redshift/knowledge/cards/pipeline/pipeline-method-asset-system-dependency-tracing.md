---
id: pipeline-method-asset-system-dependency-tracing
title: An asset system tracks every version's dependencies so a final image can be traced to its sources and old versions freed
domain: pipeline
tags: [andre prado, method studios, asset system, dependencies, versions, metadata, bundle, deep-read]
applies_to: Python, Maya, Houdini
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=HuV0_AbDgYk, src:yt-transcripts]
feeds: [pipeline plan, CHECKS]
conflicts: none
---
Andre Prado (lead core developer, Method Studios): everything artists make is an asset with many versions (hundreds for one character before approval). Metadata tracked: creator, users, what was needed to make it, client approval, location on disk [10:32-11:37].
Example: a character bundle v3 is body geometry v5 plus armour geometry v3, plus a texture asset; exports are Maya file, video, render [11:37-12:08]. With dependencies recorded you can trace a final image to its Maya file and textures [12:42]; once a shot is final, unneeded versions can be deleted. Artists get notified when work uses an out-of-date asset, and cannot delete files others use. Graphs run thousands of levels deep and are traversed constantly [13:13].
Artist UIs are Qt panels that hide this [12:08].

**Use it:** Design: every render records inputs and versions; block deleting inputs still referenced.
