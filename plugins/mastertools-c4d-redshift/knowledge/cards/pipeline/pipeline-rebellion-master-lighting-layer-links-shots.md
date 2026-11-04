---
id: pipeline-rebellion-master-lighting-layer-links-shots
title: A master lighting layer linked to every shot lets one artist apply a director's note across a whole sequence
domain: pipeline
tags: [rebellion vfx, evil genius 2, usd, master lighting, overrides, notes, sequence, deep-read]
applies_to: Houdini Solaris, USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=NNUtKYRmcjY, src:yt-transcripts]
feeds: [coach, pipeline]
conflicts: none
---
Lighting for an asset or scene exports as a USD layer that is imported by shots; a shot artist can override one parameter (move the key light) while all other settings stay linked [19:46].
The link stays dynamic: update the master and every parameter not overridden in a shot updates [20:18]. One artist can change a whole sequence at once, which makes implementing notes quick.
On the trailer itself no environment was used twice, so they used this more on later projects [19:15].

**Use it:** for recurring sports packages, keep a master light rig with per-shot overrides rather than copies.
