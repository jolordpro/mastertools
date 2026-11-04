---
id: redshift-houdini-cloud-volume-shader-scatter-60-absorption-30-and-desaturated-rim
title: Redshift in Houdini: a cloud needs an RS Volume in an RS material builder; scatter 60 and absorption 30 plus a desaturated tint stopped the rim light blowing out
domain: redshift
tags: [houdini, volume shader, rs material builder, scatter coefficient, rim light, mark fancher, redshift for houdini, deep-read]
applies_to: Houdini + Redshift (2022 upload, Mark Fancher)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=8kvcoBUVYeo, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Houdini host: a volume has no default shader and renders faint, so build an RS material builder in the material context, delete the standard material, add an RS Volume node and wire it to the volume input, then assign it on the volume object [01:02-02:06]. The density field of the VDB feeds scatter by default; other fields such as temperature can feed emission [02:06-02:38].
Values: scatter coefficient 10 first, then 60 with absorption 30 gave a thicker cloud with a lit rim [02:38-03:08]. He tinted it toward orange and desaturated it a little [03:08].
Tip: a fully saturated red or orange in the lightning mesh light made the volume go out of control; pulling the light colour back toward yellow and desaturating fixed it [07:16-08:00]. Narrow the rim light spread so it acts like a spot [05:12], and use bucket mode with 32 min and 64 max samples to check [06:16-06:45].

**Use it:** do not crank saturation on lights that feed volumes. Numbers are scene-specific, not defaults.
