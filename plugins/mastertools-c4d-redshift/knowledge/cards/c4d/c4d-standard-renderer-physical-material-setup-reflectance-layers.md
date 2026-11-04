---
id: c4d-standard-renderer-physical-material-setup-reflectance-layers
title: For the C4D Physical renderer: delete default Specular, add a Reflectance layer (Beckmann plastics, GGX metals, Ward rubber and skin), switch Fresnel on, put Diffuse under it
domain: c4d
tags: [maxon training, cinema 4d, standard material, physical renderer, reflectance, beckmann, ggx, ward, fresnel, dielectric, conductor, bump, deep-read]
applies_to: Cinema 4D S22-era Standard/Physical renderer (not Redshift)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=171zAg2Wx60, src:yt-transcripts, https://www.youtube.com/watch?v=thZ7TRegehk]
feeds: [[lookdev]]
conflicts: none
---
Maxon Training Team trainer (2021, native C4D renderers only; Redshift uses a different material model). Setup order [08:48-14:32]: new Standard material, turn off the Color channel (colour is the light a surface does not absorb), delete the Specular layer, add a reflectance layer; type choice: Beckmann for plastics and most things, GGX for metals, Ward for rubber and skin [11:55]; Fresnel is off by default and must be turned on, set to Dielectric for non-metals or Conductor for metals [12:26-14:00]; then add a Lambert diffuse layer and drag it below the reflection layer, since the diffuse holds the colour; the two controls most used are roughness and strength [14:32-15:02]. A PBR material already comes set this way. Bump does not change the silhouette (the sphere edge stays perfect), displacement does; alpha removes information (net, gauze) rather than making it see-through [04:39-06:45].

**Use it:** Teaching reference when explaining why a native C4D material looks plasticky; keep Redshift settings sourced from the redshift ledger, not this card.
Transcript support: Greyscalegorilla 2017 adds a number: Lambertian in Reflectance instead of the Color channel took a still from 40 s to 14 s (GI off) (https://www.youtube.com/watch?v=thZ7TRegehk [03:42])
