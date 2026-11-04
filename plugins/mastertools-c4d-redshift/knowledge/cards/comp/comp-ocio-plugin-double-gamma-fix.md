---
id: comp-ocio-plugin-double-gamma-fix
title: Using the OCIO plugin to sRGB with After Effects display management on applies two sRGB curves; fix with a Colour Profile Converter layer
domain: comp
tags: [ocio plugin, after effects, gamma, srgb, color profile converter, washed out, aces]
applies_to: After Effects with OpenColorIO plugin (2021), Redshift
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=7uY4-bPvRKs, src:yt-transcripts]
feeds: [coach, comp-fix planner]
conflicts: none
---
The plugin's ACEScg to sRGB already applies the sRGB curve, and After Effects adds another: the result looks washed out [22:36-24:09].
Fix on a top layer: Color Profile Converter, input and output sRGB, Linearize Output Profile ticked, which removes one curve [24:39-25:44].
Zak's null test: the result differed from the standard Preserve RGB export by nothing in Difference mode [42:08-43:10]. This is a different method from the Preserve RGB checklist.

**Use it:** offer this as the alternative when the user cannot manage the project colour settings, and tell them to confirm with a Difference check.
