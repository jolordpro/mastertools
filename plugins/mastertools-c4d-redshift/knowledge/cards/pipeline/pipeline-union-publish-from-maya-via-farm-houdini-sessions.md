---
id: pipeline-union-publish-from-maya-via-farm-houdini-sessions
title: Union publishes from Maya through persistent headless Houdini sessions on the farm so all DCCs get the same outputs
domain: pipeline
tags: [union vfx, houdini engine, hapi, persistent session, pdg, deadline, shotgrid publisher, maya usd, deep-read]
applies_to: Houdini, Maya, Deadline
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=nUXfEdZ-7Xs, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
Artists use the normal ShotGrid publisher and loader in every app [16:36]. Maya's publish writes a temporary USD (with Arnold shading), then the Houdini Engine API passes it to one of about 10 persistent headless Houdini sessions on the farm behind a load-balancing proxy; the session runs the same asset-publisher HDA as a Houdini user would [19:43-20:13, 21:47].
The HDA holds a Solaris graph (model, animation, crowd branches) and a PDG graph (ShotGrid calls, three output formats, LOD generation, turntable preview) [27:01-28:34]. Lighters can switch between Maya and Houdini mid-sequence with identical results [30:40].

**Use it:** Design idea: one publish brain, thin clients.
