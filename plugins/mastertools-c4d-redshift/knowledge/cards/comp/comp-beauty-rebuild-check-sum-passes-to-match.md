---
id: comp-beauty-rebuild-check-sum-passes-to-match
title: Verify a pass set by adding it back up: material AOVs and light groups should each match the beauty
domain: comp
tags: [beauty rebuild, qc, aov, light groups, a/b, nuke, deep-read]
applies_to: Nuke, Redshift/Arnold/Octane passes
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=UCUXhXKDnWQ, src:yt-transcripts, https://www.youtube.com/watch?v=evwUXSqbysQ]
feeds: []
conflicts: none
---
Tony Lyons (CompositingMentor). In his scene the material passes plus emission rebuilt the beauty almost identically when A/B'd, and adding light groups one by one (plus the emitting lamp as its own group) did the same [13:06-14:12]. Small differences remain. If a rebuild is off, a missing pass or light is the usual suspect. The emissive lamp counts as a light group because it lights the scene [04:43-05:15].

**Use it:** Make rebuild-vs-beauty an automatic QC step before comp starts.
