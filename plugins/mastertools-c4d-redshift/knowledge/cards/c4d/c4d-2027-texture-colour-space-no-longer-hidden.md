---
id: c4d-2027-texture-colour-space-no-longer-hidden
title: C4D 2027 shows the real colour space a texture resolves to instead of an invisible 'auto'
domain: c4d
tags: [ocio, color space, texture, auto, srgb, color management, material]
applies_to: C4D 2027.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts]
feeds: [CHECKS 5, lookdev, coach]
conflicts: none
---
[01:07:42] In 2026 a texture dropped into a material said 'auto', hiding what it was converted from. In 2027 the same texture reads sRGB: the conversion is unchanged, only visible.
[01:08:13] The colour-space name is now stored with the index so a changed config follows the name (he says he does not fully understand this point). Dropdowns follow the config file's order, not alphabetical, with common spaces at the top and families collapsed.

**Use it:** a scene check can read the shown space per texture and flag any that does not match the expected map type; tell artists to reorder the config to put their common spaces first.
