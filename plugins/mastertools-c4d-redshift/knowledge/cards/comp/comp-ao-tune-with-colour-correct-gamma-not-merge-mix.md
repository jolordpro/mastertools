---
id: comp-ao-tune-with-colour-correct-gamma-not-merge-mix
title: Set AO strength with a ColorCorrect gamma (about 3.5 here) after a multiply merge, not the merge's mix slider
domain: comp
tags: [ambient occlusion, multiply, colour correct, gamma, merge mix, nuke, sarkamari, deep-read]
applies_to: Nuke 12.3
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=4A9kbUZpqIU, src:yt-transcripts]
feeds: []
conflicts: none
---
AO on a Merge set to Plus does nothing useful; Multiply works but was too dark and killed details and the glow [22:29-23:30]. He avoids using the mix attribute on merges and drops a ColorCorrect labelled AO, raising master gamma to about 3.5 [23:30-24:34]. Reason: more efficient, better practice.

**Use it:** Use a separate grade node for AO strength so the merge stays readable and adjustable.
