---
id: broadcast-aximmetry-set-from-another-machine-reports-unreal-project-not-found-relink-it
title: A downloaded Aximmetry set fails with 'cannot find the Unreal project' because the developer's file path differs; relink it in the flow view
domain: broadcast
tags: [aximmetry, unreal project path, relink, flow view, cook content, failure point, camera paths, 2021, deep-read]
applies_to: Aximmetry DE, 2021
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=rhcwOVyKDlI, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
After cooking in Unreal, the Aximmetry project reported it could not find the Unreal project, because the set's author had stored it on a different path [05:56-06:31]. Fix: open the flow layout, select the set's node, and redirect its input source to the local Unreal project [06:31-07:04].
The same demo notes limits useful for set-up: up to three camera views, 16 paths per camera, each path a move from point A to B with its own speed (he sets 5 to speed it up), loop, ping-pong, linear or S-curve [07:38-08:43, 13:38].
Cook time grows with reflections and screens; a simple set cooked almost at once, bigger ones can take a minute or two [04:19-04:50].

**Use it:** When a virtual-set pipeline moves between machines, check the project path first and re-cook after any engine version update.
