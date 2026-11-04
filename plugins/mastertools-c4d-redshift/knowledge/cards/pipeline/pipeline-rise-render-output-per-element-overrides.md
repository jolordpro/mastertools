---
id: pipeline-rise-render-output-per-element-overrides
title: Set render settings once, then override samples per render output so only the hard element pays for them
domain: pipeline
tags: [rise, karma, render outputs, overrides, pixel samples, depth of field, aov, collections, deep-read]
applies_to: Karma / Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jpbMbafS9FY, src:yt-transcripts]
feeds: [estimator, redshift]
conflicts: none
---
Rise's render step needs two nodes: a render output (defines the sequence, phantom matte and light selection, default render vars including light exports and cryptomattes) and a submit node [35:18-35:49]. Default products are beauty, preview and utility, with deep optional [35:49].
A separate output per element lets an override apply to one only. Example: depth of field on for one shot, then pixel samples raised from 9 to 20 on the front 'table' output only [38:27-38:58].
Matte and light selections are ignored upstream and applied at the preview/submit node so they stay editable [37:23-37:54]. Submit nodes pick outputs per shot from collections, otherwise every output goes for every shot [38:58-39:30].

**Use it:** Redshift: split a heavy foreground into its own pass with its own sample count.
