---
id: redshift-sss-radius-colour-and-scale
title: Subsurface: radius colour is what gets absorbed, radius scale (scene units) sets depth, and black radius shows no scattering
domain: redshift
tags: [subsurface scattering, sss, radius, scale, gummy, candy, weight, absorption]
applies_to: Redshift 2026 standard material
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=t9hy0YCq0I8, src:yt-transcripts, https://www.youtube.com/watch?v=Bzt7uYwsT9g, https://www.youtube.com/watch?v=a9gxWJIFsc0, https://www.youtube.com/watch?v=ZcZa-42w8QE, https://www.youtube.com/watch?v=P75L5fo0Xf0]
feeds: [redshift, elevate, coach]
conflicts: none
---
Switch off base colour and reflection roughness, raise subsurface weight above 0 (1 is full), pick a surface colour, then radius colour is what the light absorbs inside [1:08:42-1:09:46]. Scale is in scene units (cm), so object size matters [1:10:18].
Scale 0.1 reads waxy and solid; 50 reads glassy and desaturated in thin areas [1:10:50-1:11:20]. A near-black radius shows no absorption even at scale 20 [1:11:53].

**Use it:** the coach asks for object size in scene units before suggesting an SSS scale; scene check flags near-black SSS radius.
Transcript support: Radius scale 10 reads as 10 cm; lower radius = more solid colour (speaker's claim, ledger-check) (https://www.youtube.com/watch?v=a9gxWJIFsc0 [05:14-06:48])
Transcript support: black radius removes scattering even with a tint; noise in radius gives patchy SSS; scale about 0.2 reads soapy. (https://www.youtube.com/watch?v=ZcZa-42w8QE [06:48-07:20])
Transcript support: Chad Ashley: set C4D colour range to 0-1; scale in cm multiplies the radius RGB so red travels farthest. (https://www.youtube.com/watch?v=P75L5fo0Xf0 [03:12-04:45])
