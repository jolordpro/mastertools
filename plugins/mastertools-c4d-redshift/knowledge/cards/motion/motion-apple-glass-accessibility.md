---
id: motion-apple-glass-accessibility
title: Liquid Glass accessibility modifiers: reduced motion lowers effect intensity and switches off elastic properties
domain: motion
tags: [motion-tokens, product, liquid-glass, accessibility, reduced-motion]
applies_to: any
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-04-30
sources: [https://developer.apple.com/videos/play/wwdc2025/219/, https://www.youtube.com/watch?v=IrGYUq1mklk, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
Said by Bruno (not Chan) in WWDC25 session 219. Reduced Transparency makes glass frostier; Increased Contrast goes mostly black or white with a border; Reduced Motion softens some effects and disables elastic behavior. All apply across the board whenever the system setting is on, with no per-app work.

**Use it:** Define reduced-motion as a mode that changes named properties (here: elasticity), not a global off switch.
