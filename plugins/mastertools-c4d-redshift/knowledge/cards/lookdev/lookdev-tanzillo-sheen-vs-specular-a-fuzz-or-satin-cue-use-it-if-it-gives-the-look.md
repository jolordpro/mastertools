---
id: lookdev-tanzillo-sheen-vs-specular-a-fuzz-or-satin-cue-use-it-if-it-gives-the-look
title: Sheen is a lobe for peach fuzz, satin and oily dark skin; Tanzillo says if it makes the still look right, keep it
domain: lookdev
tags: [ledger-check, mike-tanzillo, sheen, specular, material, arnold, students, deep-read]
applies_to: Arnold-style standard surface (renderer not named)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=cP3AELeZf6o, src:yt-transcripts]
feeds: [lookdev]
conflicts: none
---
A student found that a sheen slider gave muscle definition in white light without rim lights [34:56-36:59]. Student answers: sheen for oily dark skin, satin cloth, peach fuzz on a nose; coat is a layer on top that ignores the bump. Tanzillo: the usual use is fuzz on skin; if it gives the look, especially in a still, do it ("I'll make something look rusty that isn't metal"). Low confidence because it is student talk and the renderer is not named; do not map this to Redshift sheen or coat values.

**Use it:** `ledger-check` before using it in a Redshift material; treat as an idea only.
