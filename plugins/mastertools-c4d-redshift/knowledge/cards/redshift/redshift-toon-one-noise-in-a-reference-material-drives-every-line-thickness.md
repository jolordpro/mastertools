---
id: redshift-toon-one-noise-in-a-reference-material-drives-every-line-thickness
title: Redshift Toon: a Maxon Noise stored in a reference material can drive every toon material's line thickness, but needs a refresh after edits
domain: redshift
tags: [redshift toon, reference node, line thickness, noise, hand-drawn, c4d, school-of-motion, deep-read]
applies_to: Cinema 4D + first Redshift Toon release (video April 2024)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=i3YczHKxtbo, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Varying line width gives the anime or hand-drawn feel: plug a Maxon Noise (large scale, about 90 in his demo; low clip and brightness tune it) into both the internal and external thickness-modifier inputs [19:12-21:17]. With many materials, copy the noise into its own material, plug it into that material's surface, and in every toon material read it with a Reference node (material, then surface input). One node then controls all of them [23:22-25:58].
Quirks he reports: after editing the source noise nothing updates until the viewport is refreshed; pasting the reference into another material means reconnecting the ports; and the Reference node could not carry a global contour thickness at that time [24:55-26:29].
Same trick for a dotted outline: a Tile shader set to black and white (tiles via a triplanar so mapping is even), plugged into both contour opacity inputs, gives dashed lines; store it in a reference material the same way [33:16-36:25].
Related existing card: `redshift-reference-node-brand-colour` uses the same reference-node idea for colour.

**Use it:** for a multi-material toon scene, set up one reference material for line noise early; remember to refresh the render view after editing it.
