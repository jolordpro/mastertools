---
id: comp-cheap-tricks-depth-generator-ai-depth-pass-from-any-footage-export-full-range-then-isolate-later
title: Red Giant Depth Generator makes an AI depth pass for any footage in After Effects; export the full range and isolate in the comp
domain: comp
tags: [depth pass, depth generator, red giant, after effects, depth anything, z depth, maxon, deep-read]
applies_to: Maxon Red Giant Depth Generator (Dec 2025), After Effects
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=-32g9bYyZuc, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
The Cheap Tricks host (Action Movie Dad, Maxon Red Giant, Dec 2025) shows Depth Generator, which estimates a depth pass for real footage on a solid inside the comp [02:09-02:42]. Controls: resolution low/medium/high, normalised so near is bright and far dark, and two curve modes: Multiply dampens areas, Replace sets the mapping for every depth value so you can push a middle band to 100 percent white and clamp the rest to black [03:13-03:44]. It also offers a curve offset (follow a subject moving through space), a loop over seconds for animated mattes, deflicker and smoothing against banding [04:16]. It uses Depth Anything version 2, a single local model file that sends nothing out [04:46]. The host prefers to export the full-spectrum pass and shape it afterwards rather than bake the isolation in [05:19-05:51].
Transfers: the estimated pass is a stand-in for a rendered Z-depth AOV; a rendered one from Redshift is exact and does not need estimating.

**Use it:** Use an estimated pass only for live-action plates; for C4D/Redshift shots render the real depth AOV.
