---
id: pipeline-realtime-path-tracing-not-yet-covered-areas
title: What real-time path tracing still does not cover - mirror reflections, translucency, hair, water, volumetrics, post effects
domain: pipeline
tags: [richard cowgill, nvidia, unreal fest, path tracing limits, mirror reflection, translucency, volumetric fog, deep-read]
applies_to: Unreal Engine 5, NvRTX branch
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=zD9kS1nOuyU, src:yt-transcripts]
feeds: []
conflicts: none
---
Not path traced as of this 2024 talk: mirror-like reflections (use Lumen or ray tracing and blend to path tracing on rougher surfaces), translucency (still ray traced), hair and single-layer water (custom render paths), volumetric fog (rasterised but compatible), depth of field, bloom and motion blur (rasterised) [27:33-30:12].
Other items: Shader Execution Reordering speeds RTX 40 series, opacity micromaps cut alpha-mask cost for foliage, path-traced decals added [30:42-31:46]. He says it needs no RTX-only hardware [10:36].

**Use it:** check list for any claim that an engine render equals offline - which features are fallback.
