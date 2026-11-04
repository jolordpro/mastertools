---
id: pipeline-usd-hda-layer-break-and-merge-order
title: Start and end each Houdini USD asset with a new layer; use layer breaks for branches and watch merge order
domain: pipeline
tags: [usd, layer break, configure layer, merge order, hda, houdini, luca scheller, deep-read]
applies_to: Houdini Solaris / OpenUSD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=VSE7ayrRStg, src:yt-transcripts, https://www.youtube.com/watch?v=XUsleR7wJhk]
feeds: []
conflicts: none
---
Houdini keeps a backup of the active layer per node, so editing a layer that holds a huge hierarchy can become very slow; adding a configure-layer node to start a new layer makes edits instant again [49:20]. Recommendation: begin and end every HDA with a new layer so edits are encapsulated [49:51]. Unlike SOPs, merge order matters: two cubes with different transforms give different results if inputs are swapped [50:24, 51:58]. For diamond-shaped networks, put a layer break at the split, or content can load double or triple and get buggy [51:25]. Keep subtrees isolated and merge them in.

**Use it:** If a USD lighting scene gets sluggish, check for edits on a heavy layer; add the break.
Transcript support: layer break has no parameters; USD ROP option to strip layers above a break can produce an empty file (https://www.youtube.com/watch?v=XUsleR7wJhk [12:32])
