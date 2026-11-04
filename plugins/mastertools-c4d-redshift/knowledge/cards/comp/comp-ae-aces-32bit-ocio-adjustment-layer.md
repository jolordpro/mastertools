---
id: comp-ae-aces-32bit-ocio-adjustment-layer
title: After Effects ACES recipe (2020): 32 bpc, sRGB working space, Preserve RGB, OCIO effect on an adjustment layer
domain: comp
tags: [after effects, aces, ocio, 32 bit, preserve rgb, adjustment layer, fnord]
applies_to: After Effects with fnord OCIO plugin (2020 video)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=vEoIXTbyz6o, src:yt-transcripts]
feeds: [comp-fix planner, coach]
conflicts: comp-aces-after-effects-setup
---
[13:38] Project depth must be 32 bits per channel, no exceptions; 16 bpc clips. Working space sRGB.
[14:09] Interpret footage (Ctrl+Alt+G) > Color Management > Preserve RGB so the EXR is read untouched.
[14:41] Adjustment layer with the OpenColorIO effect, custom config, input ACEScg, output sRGB; compare against the baked render to check.
Differs from the existing ACEScg working-space checklist; both are community recipes.

**Use it:** present as one tested option stamped with its version, not as the rule.
