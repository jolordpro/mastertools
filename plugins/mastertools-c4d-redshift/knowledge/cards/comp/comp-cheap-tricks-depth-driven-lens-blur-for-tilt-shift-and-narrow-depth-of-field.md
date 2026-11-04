---
id: comp-cheap-tricks-depth-driven-lens-blur-for-tilt-shift-and-narrow-depth-of-field
title: After Effects Camera Lens Blur can take the depth pass as its blur map for a tilt-shift miniature or a narrow depth of field
domain: comp
tags: [lens blur, tilt shift, miniature, depth of field, bokeh, universe bokeh, deep-read]
applies_to: After Effects
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=-32g9bYyZuc, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Apply Camera Lens Blur to the footage with the depth pass as blur map layer, raise the radius and move the focal distance: city shots read as miniatures [11:03-11:34]. Universe Bokeh does the same with selectable blur shapes (hexagon) and a camera-focus mode that reads the depth pass; a forest shot becomes a bee's eye view with a very narrow depth of field [12:06-12:37]. The host also uses it for foreground sparks: Universe Bokeh with a hexagon and highlight boost on the near particle layer [47:47].
Transfers: with a rendered Z-depth the same blur can replace in-render DOF; see existing ZDefocus cards for the clamping and focus-plane rules.

**Use it:** Option for a post DOF pass in AE when ZDefocus is not available.
