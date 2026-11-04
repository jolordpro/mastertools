---
id: redshift-attenuation-leaves-sun-sky-and-dome-light-alone-so-add-an-area-light
title: Redshift volume attenuation does not dim the sun, sky or dome light, only light travelling inside the volume, so use an area or point light to see it
domain: redshift
tags: [attenuation, sun and sky, dome light, volumetric lighting, area light, phase, bold and break, c4d, deep-read]
applies_to: C4D + Redshift, Bold&Break upload 2021
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=A-stHqCya4s, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Brian McCarthy (Bold&Break): scattering sets how strong the volumetric light is; attenuation combines strength with how much light the medium eats; phase spreads what is left [02:44-04:17]. Redshift does not attenuate dome or physical sky light, so attenuation changes do little in a sun and sky scene [05:18-05:50].
Attenuation only dims light that is inside the volume, not the scene lighting behind it [06:52]. To show it, add an area or point light; a spot-like area light with spread 0.5 lost strength gradually with attenuation, and phase then diffused what remained [07:33-09:06].
He treats volumes like a glass in the scene: many light types give different looks. His warm scene ended near scattering plus 3 and attenuation 0.2 [10:09].

**Use it:** when a sun-only shot ignores attenuation, add a local light before touching the number. The coach warns that sky and dome light are never attenuated.
