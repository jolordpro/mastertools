---
id: lookdev-shoot-your-own-surface-textures-cloudy-stitch-seam-invert-for-spec
title: Make a texture from photos: shoot on an overcast day for flat light, step sideways between shots, stitch with perspective, flip a copy to seam, and invert the bump for specular
domain: lookdev
tags: [texture, photography, photomerge, seamless, specular, displacement, andrey lebrov, deep-read]
applies_to: Photoshop plus any renderer (2018)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=a8d6p-E4KSE, src:yt-transcripts]
feeds: []
conflicts: none
---
Andrey Lebrov [04:56-09:13]. Shoot surfaces on a cloudy day so shadows are flat; take several overlapping photos, stepping one step left or right, to get more resolution. In Photoshop use File > Automate > Photomerge with Perspective, then transform to correct the distortion, crop, and spot-heal litter. Duplicate the layer and flip horizontally, then erase to blend, as a quick seam. Make the diffuse folder; duplicate it, apply a black-and-white filter for the bump; duplicate that for specular and invert it so the reflective areas sit below the stones (water pools in the low spots). For the displacement map even out the tonal distribution and darken so deformation does not blow out. His advice: a custom texture for the project beats a premade one, and the material should 'feel' right (wet asphalt, heavy painted steel).

**Use it:** A recipe for custom surfaces: one source photo drives the diffuse, bump, specular and displacement; do the seam and levelling steps before use.
