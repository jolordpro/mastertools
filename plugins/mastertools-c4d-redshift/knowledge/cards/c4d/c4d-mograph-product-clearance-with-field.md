---
id: c4d-mograph-product-clearance-with-field
title: Keep scattered clones out of a product with a Push Apart effector and a field-limited scale-down that follows the product
domain: c4d
tags: [mograph, cloner, push apart, plane effector, cylinder field, intersections, multi instance, product]
applies_to: Cinema 4D 2026
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=t9hy0YCq0I8, src:yt-transcripts, https://www.youtube.com/watch?v=Iy2FAJbbyrY]
feeds: [coach]
conflicts: none
---
Random effector gives intersections; add Push Apart (radius) to separate clones [10:44-12:16, 13:50]. For clones inside the product, a Plane effector scales them -100% inside a Cylinder field (no falloff), field made child of the product group so it follows animation [16:31-20:37].
Scale -1 is safer than visibility, which sometimes needs a refresh [28:25]. Seed in the Random effector iterates compositions [14:23]. Use Multi-Instance mode for high-res identical clones [06:09].

**Use it:** a template step in the product-viz flow; the scene check could notice cloners without any clearance around the product.
Transcript support: Push Apart radius must exceed half the point spacing (3.5 cm at 6 cm spacing; 3 cm did nothing); a random field on strength limits where it pushes (https://www.youtube.com/watch?v=Iy2FAJbbyrY [17:00])
