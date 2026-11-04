---
id: redshift-quick-gold-copper-metalness-roughness-ramp-and-bump-blender
title: Redshift quick metal: Fresnel type metalness at 1, roughness map through a Scalar Ramp (easy-ease, brights to about 0.4), tiny bump, bump blender for noise
domain: redshift
tags: [[metal, gold, copper, redshift-material, scalar-ramp, bump-blender, mographplus], deep-read]
applies_to: Redshift in Cinema 4D (RS Material with Fresnel Type setting; check against the redshift ledger)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=pLPOcdxezgE, src:yt-transcripts, https://help.maxon.net/r3d/cinema/en-us/Content/html/Standard_Material.html]
feeds: [coach]
conflicts: none
---
MographPlus steps [00:39-02:51]: new Redshift material; set Fresnel type to Metalness and metalness to 1; diffuse a pale yellow with a lighter, less saturated reflectivity colour of the same hue for gold; roughness map into a Scalar Ramp, both points easy-ease, brightest ramp value lowered to about 0.4, texture UV scale 20; bump map with height around 0.006 from the same texture; combine with a noise bump via the Bump Blender (first bump to base input). Copper is a duplicate with a light brown-orange diffuse and brighter, less saturated reflectivity [03:29]. Changing only the shared texture changes the whole feel [02:51]. "Reflection roughness is the key to everything" [04:11].
Unsure if the 2021 UI names match current Redshift materials.

**Use it:** Cross-check any numeric claim against the redshift skill's ledger before the coach repeats it.
Maxon check (2026-10-31): Maxon docs: this is the legacy RS Material route (Fresnel Type: Metalness). The current Standard Material has a Metalness slider and no Fresnel Type menu. (https://help.maxon.net/r3d/cinema/en-us/Content/html/Standard_Material.html)
