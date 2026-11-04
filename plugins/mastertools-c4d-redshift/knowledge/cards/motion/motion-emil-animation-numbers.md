---
id: motion-emil-animation-numbers
title: Emil's concrete UI motion numbers: press scale 0.97, enter from scale 0.9+, ease-out, origin-aware
domain: motion
tags: [motion-tokens, product, emil-kowalski, spec, easing]
applies_to: any
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://emilkowal.ski/ui/7-practical-animation-tips]
feeds: [studies/motion-leaders]
conflicts: none
---
Pressed buttons scale to 0.97; never animate in from scale 0, start at 0.9 or higher; ease-out for enter/exit with custom curves; popovers scale from their trigger (transform-origin); under 300 ms; a small blur (about 2px) can hide rough transitions. Personal tips, not a system spec. Fetch summary; undated.

**Use it:** A ready list of starting values to compare against a system's own tokens.
