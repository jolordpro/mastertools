---
id: motion-ae-stagger-valueattime-index-offset
title: Stagger a stack of layers with valueAtTime(time - offset) pointing at the layer two above by index, then copy the expression everywhere
domain: motion
tags: [stagger, valueAtTime, index, time offset, expression, pick whip, after effects]
applies_to: After Effects
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=M4FLVszXkbk, src:yt-transcripts]
feeds: [motion-critique]
conflicts: none
---
Boxes are parented to team assets and share one set of position keys. Each layer reads the position of the layer index-2 minus a time offset (0.05 s) [F 12:46-15:26]. Replacing a pick-whipped layer name with index-2 means one copy-paste for all [14:22-15:26].
Offset lives in one place so retiming is a single edit [15:56]. A remaining hand step: the effect order for the controller was typed per layer (author notes it could be automated) [22:01].

**Use it:** pattern for any cascading list; note remaining manual indexes as known risks.
