---
id: pipeline-usd-kind-hierarchy-assembly-group-component
title: USD kinds: assembly > group > component > subcomponent set where a prim sits in the hierarchy
domain: pipeline
tags: [usd, kind, assembly, component, group, hierarchy, deep-read]
applies_to: USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hBYSHFRnFlo, src:yt-transcripts]
feeds: []
conflicts: none
---
Kind is guidance, not a hard rule, on where a prim belongs [31:03-31:36]. Assembly = published asset or reference to one, highest importance. Group = the flexible container (holds components, groups or assemblies). Component = a leaf-ish asset piece that cannot hold groups or assemblies. Subcomponent = an important prim inside a component, such as a door pivot someone might animate [31:36-32:39].
Example: a lady and a dog are assemblies, each with two components (skin, collar); both are grouped under characters, which sits under models next to props [33:11-34:44].
Do not confuse kind with prim type (mesh, light, camera, volume, render settings, point instancer) [29:31-31:03]. A leaf prim just has no children [28:30].

**Use it:** Name asset roots as assemblies and parts as components so selections like all-components pick the right level.
