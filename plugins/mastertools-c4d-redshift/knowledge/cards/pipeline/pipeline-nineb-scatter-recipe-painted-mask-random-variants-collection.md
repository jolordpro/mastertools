---
id: pipeline-nineb-scatter-recipe-painted-mask-random-variants-collection
title: Scatter recipe: paint a mask, scatter and align points to the surface with a random cone angle, drive scale with pscale, and instance a collection of variants
domain: pipeline
tags: [nine between, houdini, solaris, usd, scatter, instancer, mask, collection, pscale, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Steps [1:27:31-1:33:42]: get the ground grid and unpack it, subdivide, paint a 0-1 attribute mask, scatter points weighted by the mask, and use align to orient to the normal with a random cone angle and random spin. pscale and orient on the points drive each copy's size and rotation [1:29:03-1:30:05].
For random variants: reference the asset, explore its variants as duplicates, gather them in a collection with /* , choose that collection as the instancer's prototype and untick 'only copy specified prototypes'. Then raise density (he went to 5000) since these are instances [1:30:35-1:33:10].

**Use it:** A template for scattering sweets, confetti, turf details or crowd props with cheap instancing and controlled randomness.
