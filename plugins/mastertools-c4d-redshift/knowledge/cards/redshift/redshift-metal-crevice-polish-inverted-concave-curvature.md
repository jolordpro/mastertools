---
id: redshift-metal-crevice-polish-inverted-concave-curvature
title: Reduce roughness and scratches in crevices with an inverted concave curvature mask, a stand-in for ambient occlusion
domain: redshift
tags: [polygon division, redshift, metal, crevices, curvature, occlusion, polish, multiply, deep-read]
applies_to: Cinema 4D 2024, Redshift
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=-lpj38Cql4c, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Areas that hands and tools rarely reach (grooves, creases) should stay cleaner and shinier. Use concave curvature, invert it, and set the layer to Multiply (which keeps darks and drops whites); widen the effect with the radius or min remap [33:54-36:33].
Apply the same mask to the scratch layers so crevices lose scratches too; as the last layer it overrides those below [36:33-37:03].
It reads like ambient occlusion without using the AO node [35:31].

**Use it:** an authored-wear trick that avoids an AO node and its bucket-mode limits (see the AO card).
