---
id: redshift-roberts-light-group-aovs-to-exr-and-rebuild-with-add-then-rebalance-by-percent-and-match-camera-exposure
title: Redshift light-group AOVs to a multi-layer EXR, rebuilt with Add, then rebalanced by percent; camera exposure is not baked into the passes
domain: redshift
tags: [phil-roberts, light groups, aov, multilayer exr, linear dodge add, camera exposure, ledger-check, after effects, deep-read]
applies_to: Redshift in Cinema 4D and After Effects (NAB 2024)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=oANXbk9OUbI, src:yt-transcripts]
feeds: [redshift, comp, CHECKS]
conflicts: none
---
Set up [30:23-32:04]: on each light's Details tab add a Light Group (dome, key, rim, backlight, etc.), then in render settings Advanced > AOV enable the multi-layer EXR so each light goes in its own pass. Beauty, Reflections and Specular are the three AOVs he usually takes, and he says a crypto map can isolate a part, like a watch lit by a too-strong reflection [32:34-33:38].
Gotcha he reports (ledger-check): if the camera has an exposure offset (his minus 0.5), the AOV EXR does not keep it, so match it with an exposure adjustment on the comp [33:38-35:14].
Rebuild: dome at the bottom, then each light with the Add mode (Linear Dodge), RGB equals the beauty, then rebalance [34:44-35:47]. His sci-fi short Insection numbers: dome source 75 percent, backlight about 30, fill about 30, key about 20, under source about 20, gunfire 100, volumetric passes up to 100 [39:35-41:49]. Per-light saturation or curves tweak a single light [35:47].

**Use it:** Supports existing light-group cards; check that exposure and sum match before rebalancing.
