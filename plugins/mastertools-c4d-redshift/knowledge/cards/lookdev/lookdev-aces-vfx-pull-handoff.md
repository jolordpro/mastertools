---
id: lookdev-aces-vfx-pull-handoff
title: VFX pull and hand-off practice: 16-bit EXR in ACES2065-1, grades off, a reference frame, gamut compression in VFX or DI but not both
domain: lookdev
tags: [lookdev, aces, vfx pull, exr, di, hand-off, gamut compression, netflix, aces2065-1, netflix vfx, colour handoff, 16-bit, reference frame]
applies_to: any
status: V2
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://mixinglight.com/color-tutorial/advanced-aces-grading-collaboration/, https://backlothelp.netflix.com/hc/en-us/articles/360000611467-VFX-Best-Practices, src:research-vfx-pipelines, https://backlothelp.netflix.com/hc/en-us/articles/360034536253-Titles-Graphics-Requirements-Best-Practices, https://www.youtube.com/watch?v=fuq85rDI01Q]
feeds: [delivery profile]
conflicts: none
---
Search summaries only. Colourists pre-grade pulls so VFX and DI share one look, with one combined shot LUT for VFX.
Netflix: share the colour pipeline with every vendor; graphics as 16-bit EXR or TIFF, log EXR not accepted; working resolution at or above delivery.
Merged from `pipeline-vfx-pull-colour-handoff`: One combined shot LUT for VFX; gamut compression happens in VFX or DI, not both; pre-grade pulls so both share a look. Netflix: colour pipeline shared with every vendor, working resolution at or above delivery. Comp tutorials add: AOVs sum back to beauty, test one frame before the sequence, half float for data passes and float for lighting.

**Use it:** use as a hand-off checklist when work leaves C4D for a post house.
Transcript support: Resolve ACES setup: input transform for camera (S-Log3 example), output Rec.709 or HDR. (https://www.youtube.com/watch?v=fuq85rDI01Q [01:06-02:38])
