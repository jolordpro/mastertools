---
id: redshift-environment-tint-scattering-attenuation-phase-and-ray-scales-explained
title: Redshift Environment general tab: tint colours only light scatter, scattering sets strength, attenuation also drives fog, phase biases toward or away from camera, and each ray type has its own contribution scale
domain: redshift
tags: [environment, scattering, attenuation, phase, tint, ray contribution, gi contribution, volume, c4d, deep-read]
applies_to: C4D + Redshift, Maxon Redshift channel upload 2018
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=vnHKQmvKYH8, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Tint is a global colour for volumetric light only, not fog [02:41]. Scattering raises the effect for every light; too high gives a white screen, 0.1 was used [03:11-03:49]. Attenuation weakens the scatter along distance and also strengthens fog; at maximum the light beams vanish and only fog stays [03:49-04:51].
Phase 0 scatters evenly; above 0 pushes light toward the camera, below 0 away from it so beams show only behind objects [04:51-05:53]. Exposure compensation should be on when a photographic exposure or Redshift camera tag is used [06:27].
Ray contribution scales: camera 1 shows the volume to the lens, reflection scale shows it in mirrors, GI scale defaults to 0 and only adds bounce when GI is on (brute force, 128 then 256 rays cut the noise) [09:59-12:21]. Environment-fog scale limits fog to the light shafts when low [13:23].

**Use it:** the coach can name each control in plain words; scene check: GI contribution above 0 with GI off does nothing.
