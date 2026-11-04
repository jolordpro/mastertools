---
id: lookdev-maya-standard-surface-keep-specular-on-rough-concrete-and-transmission-shares-specular-roughness
title: Standard Surface rules from a Maya course: rough concrete still has specular (raise roughness to 1, do not zero the weight), and transmission uses the specular roughness, so frosted glass comes from roughness
domain: lookdev
tags: [vertmode, maya, arnold, standard surface, pbr, roughness, transmission, ior, metalness, deep-read]
applies_to: Maya 2020+, Arnold standard surface
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=HmAzZFJpCI0, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Specular weight zero turns the shader into a Lambert [18:15]. Concrete and asphalt do have specular but diffused, visible at grazing light; set roughness high, not weight low [19:17]. Transmission and specular reflection are linked: raise specular roughness and the transmission goes frosted [23:26]. IOR 1.52 glass, 1.33 water, about 2.5 diamond, 0 removes refraction (his numbers) [22:56]. Metalness is a conductor/insulator switch and partial values suit corroded or impure metal [15:15-18:15]. Diffuse roughness and specular roughness are separate channels (matte colour with smooth reflection) [13:35]. Subsurface cancels base colour when full [24:59]. Steel colours lean blue-grey [30:11]. Spec colour stays white [18:45]. 90% of work is base, specular and some emission [26:35].

**Use it:** Quick material coach. IOR already carded in lookdev-ior-values-and-what-they-do-to-glass (supports).
