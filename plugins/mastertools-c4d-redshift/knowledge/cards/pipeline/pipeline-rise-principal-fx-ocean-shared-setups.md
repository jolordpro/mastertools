---
id: pipeline-rise-principal-fx-ocean-shared-setups
title: Set up all ocean looks and sims once in a shared FX scene, push to shots, and tweak single shots with switches
domain: pipeline
tags: [rise, ocean, principal fx, whitewater, hdri rotation, fx handoff, shot switch, deep-read]
applies_to: Houdini
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jpbMbafS9FY, src:yt-transcripts]
feeds: [pipeline plan, lighting]
conflicts: none
---
For about 40 oceans, Rise set up every ocean spectrum in one principal FX scene, a big time saver because setups differ only by spectrum files [41:37-42:09]. A few degrees of environment light rotation could decide whether an ocean read as realistic, so FX passed a dedicated HDRI light onward [42:09-42:41].
One ocean and whitewater sim for a whole sequence was pushed to all shots; a shot switch added extra whitewater to one approved-shot without touching others [43:46-44:19].
FX layers replace the static asset layer, so lighting needs no change if the sails were already in a collection [48:00]. FX layers were 1 GB+ per frame each [45:54].

**Use it:** Lead lighting setups: environment rotation is a sensitive parameter on water.
