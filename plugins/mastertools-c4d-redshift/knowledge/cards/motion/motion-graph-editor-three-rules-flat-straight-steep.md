---
id: motion-graph-editor-three-rules-flat-straight-steep
title: Three rules for reading any value curve: flat is still, straight is constant speed, steeper is faster
domain: motion
tags: [graph editor, value curve, velocity, slope, ease, f-curve, diagnosing timing, deep-read]
applies_to: any graph editor
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=RQ31vjgJM2c, src:yt-transcripts]
feeds: [motion-critique, coach]
conflicts: none
---
Rule 1: a flat curve means no motion [10:17]. Rule 2: a straight sloped line is constant velocity, no acceleration [10:47]. Rule 3: the nearer to vertical the faster; the nearer to horizontal the slower, and a fully vertical line is a step (teleport) [11:48]. Curves between these mean the speed is changing.
To slow a too-fast move, spread its keys apart so the slope moves toward horizontal; to snap it, bring keys closer [13:21-14:55]. The same reading works for rotation and scale; steeper rotate curve = faster spin [15:25].
Caveat: only in the ball-bounce case does the curve look like the on-screen path; do not expect this in general [02:05].

**Use it:** the coach can teach this as the first thing to check when a move feels slow or swimmy: open the curve, find the slope, then move keys.
