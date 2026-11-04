---
id: comp-grain-match-method-and-reintroduce-only-on-new-elements
title: Match grain by comparing grained and denoised areas per channel, then grain only the elements you added
domain: comp
tags: [courtney price, nuke, foundry, grain, denoise, luma key, difference key, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=yl28HkA-qyo, src:yt-transcripts, https://www.youtube.com/watch?v=ETV1VTV0vNg, https://www.youtube.com/watch?v=AxviuFLniB8]
feeds: [shakedown, composition]
conflicts: none
---
Courtney Price's method [33:55-36:32]: she prefers understanding the process over an auto-grain tool, because it helps when a supervisor sends the shot back for the sixth time about grain.
- Make a black-and-white checkerboard, use it as an alpha, key-mix the denoised plate against the grained one, and compare where grain is and is not.
- Match size first, then mid-tone balance in each of R, G, B, then the dark areas, then balance darks against mids.
- Use a luma key to fade the grain in highlights, where it is less visible.
- Check highlights, mids and darks all around the frame. Apply the result over 50% grey with the luma key as a mask, optionally desaturate it, overlay it at maybe 70% rather than 100%.
- Only grain what you changed: take a difference key of the changed elements and key-mix the grained version back, leaving the plate untouched.

**Use it:** Use it as the grain step of the comp checklist; the 'only grain the new elements' rule keeps the original plate untouched.
