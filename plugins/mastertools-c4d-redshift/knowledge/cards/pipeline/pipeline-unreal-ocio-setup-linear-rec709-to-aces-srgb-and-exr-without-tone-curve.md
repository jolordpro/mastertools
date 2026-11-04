---
id: pipeline-unreal-ocio-setup-linear-rec709-to-aces-srgb-and-exr-without-tone-curve
title: Unreal 5.7 colour setup: OCIO asset with Linear Rec.709 working space and ACES sRGB view, then MRQ output to 16-bit EXR with the tone curve off
domain: pipeline
tags: [pipeline, unreal, ocio, aces, movie-render-queue, exr, colour-management, tone-mapper, deep-read]
applies_to: Unreal Engine 5.7
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=OMyANHhrahI, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Single creator tutorial (automotive series, Karol), so low confidence. Why: UE's default sRGB with filmic tone mapper pulls intense reds toward orange/yellow (colour drifts to white) and cannot show saturated cyan, deep green, magenta [01:04-02:09]. Steps: enable the OpenColorIO plugin and restart; new OpenColorIO configuration asset (the config path is already correct in 5.7); desired colour space = Linear Rec.709, desired display view = ACES sRGB [04:16-05:19]. In the viewport mode menu pick OCIO Display, set the same pair and tick enable display [05:19-05:51]. In Movie Render Queue add a Color Output node, enable OCIO, choose the asset, and disable tone curve when rendering EXR for comp; export 16-bit OpenEXR; PNG or JPEG throws away the benefit [06:22-06:54]. Without a comp stage, leave tone curve on to get a finished ACES-tonemapped image, at the cost of post flexibility [06:54-07:25]. Also checked: Lumen GI and reflections, virtual shadow maps, DX12, Movie Render Queue with extra passes and Niagara support [03:11-04:16].

**Use it:** Use as a checklist when a Unreal render must match a client colour reference. The EXR route needs the display transform applied later, in comp.
