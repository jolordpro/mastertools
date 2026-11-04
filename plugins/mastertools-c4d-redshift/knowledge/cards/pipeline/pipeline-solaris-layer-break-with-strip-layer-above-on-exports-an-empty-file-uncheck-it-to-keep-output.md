---
id: pipeline-solaris-layer-break-with-strip-layer-above-on-exports-an-empty-file-uncheck-it-to-keep-output
title: Solaris: a USD ROP set to strip layers above a layer break writes an empty file; uncheck it, or use a break plus a ROP to export one light temporarily
domain: pipeline
tags: [houdini, solaris, usd rop, layer break, strip layer above layer breaks, empty usda, export one light, deep-read]
applies_to: Houdini Solaris (Sept 2026 video)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=XUsleR7wJhk, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
A Layer Break node has no parameters; it ends one layer and starts another without writing a path [12:32-13:03]. Replacing Start New Layer nodes with breaks produced an output file with nothing in it, because the ROP option that strips everything above a layer break was on [13:33-14:03]. Unchecking "strip layer above layer breaks" and saving again wrote all the content [14:03].
Use: put a break before and after a branch, attach a separate ROP, and save only that part, such as one light, without restructuring a complex network; one ROP per branch saves them all [14:03-15:36]. He does not recommend it for normal use; one Start New Layer per layer is the default practice [15:36].

**Use it:** if a USD export comes out empty, check the strip-above-break option before debugging the network. Supports pipeline-usd-hda-layer-break-and-merge-order.
