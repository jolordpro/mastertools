---
id: redshift-store-color-to-aov-makes-custom-masks-aov-input-0-to-7
title: Store Color To AOV turns any texture or alpha into a custom mask AOV, with eight AOV inputs (0-7) per node
domain: redshift
tags: [store color to aov, custom aov, mask, logo, label, product, deep-read]
applies_to: Redshift in C4D
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=iqrISqFY3bQ, src:yt-transcripts]
feeds: [redshift, comp]
conflicts: none
---
Add a Store Color To AOV node (Shift+C). Plug the final material (a material blender in the example) into its Beauty input, and the node's output to the surface [06:46-07:18].
Drop the mask texture onto AOV input 0, open the AOV 0 tab, Add New Custom AOV, name it (for example logo) [07:18-07:50]. It then appears in the render view and the AOV manager. Denoising it is unnecessary for a black-and-white mask [07:50].
The speaker counts inputs 0 to 7, so eight custom AOVs per node (he says 'I believe') [08:20].
Why: he masked the pack logo and the label text so levels and colour could be changed per variant in post, with no re-render [06:14, 08:52]. Ross (channel name not given), product job for a tea brand.

**Use it:** Variants for broadcast cut-downs: put the swappable element on its own mask AOV instead of rendering each version.
