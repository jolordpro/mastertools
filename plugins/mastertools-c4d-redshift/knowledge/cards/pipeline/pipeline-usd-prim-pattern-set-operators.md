---
id: pipeline-usd-prim-pattern-set-operators
title: USD primitive matching patterns can union, subtract and intersect sets, and take a seeded random fraction
domain: pipeline
tags: [usd, pattern matching, procedural, random, seed, collections, deep-read]
applies_to: Houdini Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hBYSHFRnFlo, src:yt-transcripts]
feeds: []
conflicts: none
---
Patterns select by kind (all components), by reference source (everything that references the pig source asset), and by a keep-random clause: a fractional share of the children of a path, 50 percent in the demo, with a seed value to reroll [55:37-57:41].
Combine with minus (random set without the Tommy references), plus (random set plus all Tommy references) and and (only the Tommies that were inside the random set) [57:41-58:46].
Full syntax is in the Houdini "primitive matching patterns" doc page [55:37].

**Use it:** Use pattern sets instead of hand-picking prims when a scene has many instances of one asset.
