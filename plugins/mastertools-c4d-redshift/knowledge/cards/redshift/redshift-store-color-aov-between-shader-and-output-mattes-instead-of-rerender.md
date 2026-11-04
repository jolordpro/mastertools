---
id: redshift-store-color-aov-between-shader-and-output-mattes-instead-of-rerender
title: Chad Ashley's rule: render matte AOVs with Store Color To AOV so a client colour note becomes a comp tweak, not a re-render
domain: redshift
tags: [chad-ashley, greyscalegorilla, custom aov, store color to aov, matte, re-render, deep-read]
applies_to: Redshift 2.x for C4D (2018)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ARykOD6lG3c, src:yt-transcripts]
feeds: [comp, coach, estimator]
conflicts: none
---
Chad (Greyscalegorilla, Jan 2018) renders a beauty plus a pile of matte AOVs "as insurance": sticker, orange centre of the sticker, stripes and edge wear all came out of one EXR, so a note like "change that colour" or "brighten the stripes" is a colour-correct in comp [05:18-07:52]. His line: avoid costly re-renders.
Build: put a Store Color To AOV node between the shader and the surface output; one node takes about eight inputs and nodes can be daisy-chained for more [19:48-20:19]. Create the custom AOV in the AOV manager, then link the input to it or type a new name to make one [16:41-17:12, 21:21-21:51]. Refresh the IPR if it does not appear, and look in bucket mode [10:40-11:00].
Limits: a custom AOV takes colour, integer or float only, never a whole shader; Arnold is the same [16:10]. Feeds can be a PNG alpha pulled out with a colour splitter, a curvature mask with noise for edge wear, a triplanar dust map [22:54-25:30]. He also floats a facing-ratio or fresnel texture sent to an AOV to control light wrap or back light in comp [41:54].
Grade the matte before the lighting passes are added, so the change sits on the diffuse (see the diffuse-before-reflection card).
Transfer: for sports logo and team-colour variants, a matte per colour area lets one render serve many colourways.

**Use it:** Before a render, ask which areas a client could change (logo, label, accent stripe) and give each a Store Color AOV. Chad says he is lazy and usually does beauty plus mattes.
