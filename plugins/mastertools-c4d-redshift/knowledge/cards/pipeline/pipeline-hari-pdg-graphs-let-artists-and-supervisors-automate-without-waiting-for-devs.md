---
id: pipeline-hari-pdg-graphs-let-artists-and-supervisors-automate-without-waiting-for-devs
title: Hari uses PDG as the bridge between artists who know what to automate and devs who know how: shot, asset and farm jobs chained as graphs, e.g. 150 snow shots rendered overnight
domain: pipeline
tags: [flavien-rojon, hari, houdini, pdg, topnet, automation, deadline, shotgrid, deep-read]
applies_to: Houdini PDG, Solaris, Karma (Paris HUG 2026)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=Dd1eYWpgpkw, src:yt-transcripts]
feeds: [coach, CHECKS]
conflicts: none
---
Flavien Rojon (deputy head of CG, Hari studio, TV series). Problem: artists click 500 shots by hand; devs cannot build every tool; PDG lets artists compose graphs from dev-written job nodes [09:57-11:02]. Get-entity nodes make one work item per asset or shot with its attributes; get-file nodes find published files; a play-in-RV node opens them [11:33-12:38]. Procedural selection: from a forest set, 117 cast assets found; from an episode, all shots then assets, split props from characters, remove doubles [12:38-13:41]. The dev tools are Python jobs that run as command lines with the environment loaded, local or on Deadline [14:15]. Chain AnimToRender then a Karma render and an auto-comp Nuke job; an FX artist wrote one HDA to add snow, plugged it between the two, and 150 shots were ready next day instead of two days [15:21-17:28]. A supervisor can chain re-export of an animation fix plus all FX caches, send it to the farm and leave [17:59]. Queries can start from ShotGrid statuses or tags [17:28]. Quality, not money, was the gain: artists light instead of copy-pasting [29:22]. Whisper transcript with French speech; details may be mis-heard.

**Use it:** Model for a render-platform job-graph feature: entity query, publish lookup, tool nodes, farm submit. Related: pipeline-union-publish-from-maya-via-farm-houdini-sessions.
