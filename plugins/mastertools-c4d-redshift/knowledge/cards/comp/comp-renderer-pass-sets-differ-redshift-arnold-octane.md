---
id: comp-renderer-pass-sets-differ-redshift-arnold-octane
title: Redshift, Arnold and Octane give different default pass sets, so check what a renderer actually wrote
domain: comp
tags: [redshift, arnold, octane, aovs, pass differences, default passes, deep-read]
applies_to: Nuke, Redshift/Arnold/Octane passes
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=UCUXhXKDnWQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Tony Lyons (CompositingMentor). Same scene in three engines [12:35-18:54]: Arnold lacked a shadow pass that others had and had fewer utility passes; Redshift supplied SSS and more utilities; Octane added shadow, light direction and filter passes but only depth, normals, position and UV as utilities. He suspects unticked boxes rather than missing features, and notes subtle light differences between engines on matching scenes. ID passes look alike because he made them himself.

**Use it:** List passes found in the EXR against the intended list, since defaults differ.
