---
id: pipeline-bepic-solaris-asset-layers-per-department-and-shot-hda-for-animation-caches
title: bEpic asset set-up in Solaris: separate layers for model, look dev and groom, a shot-side HDA that swaps in animation-cache positions and bounds
domain: pipeline
tags: [pipeline, bepic, solaris, usd, layers, hda, animation cache, deep-read]
applies_to: Solaris with the "Iron" pipeline (as the captions give it)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=4D9GDZsCzy0, src:yt-transcripts]
feeds: []
conflicts: none
---
They use an existing USD-based pipeline (captions say Ion/Iron; name uncertain) in Solaris, which is close to the Component Builder workflow [12:31-13:02, 20:00-20:30]. Each asset has layers per department: model separate from look dev, groom with its deformation set-up. In a shot it is just a reference node [20:30-21:02]. A custom HDA loads animation caches and replaces positions, transforms and bounding box, which was all they needed; a simple sub-modify HDA to deform feathers before sims turned out unnecessary [21:02-21:36]. Feather sims would use Vellum [21:02].

**Use it:** Keep the shot-side loader tiny: caches in, positions and bounds out, everything else from the layers.
