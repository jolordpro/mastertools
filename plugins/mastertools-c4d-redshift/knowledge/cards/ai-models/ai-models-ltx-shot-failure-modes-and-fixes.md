---
id: ai-models-ltx-shot-failure-modes-and-fixes
title: AI shot fixes: add a second control frame when one fails, name the hand in the prompt, patch gibberish text in Photoshop, and turn on previews to stop bad runs
domain: ai-models
tags: [ai render, ltx, failure modes, control frame, prompting, previews, text, mickmumpitz, deep-read]
applies_to: LTX 2.3 (2026)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=7J7hi-Hxpac, src:yt-transcripts]
feeds: []
conflicts: none
---
Mickmumpitz [18:29-21:44]. (1) A shot with a camera move, a second character and a side switch fell apart on one guide frame; adding a second control frame at the start helped, and the troublesome frame took about half an hour of prompting. (2) A character reached with the wrong hand despite precise control; the prompt had to say which hand and what she reached for. (3) A newspaper far from the guide frame came out as gibberish; extract the frame, paint correct text in Photoshop and feed it back as an extra start frame. (4) Start and end frames made separately in the same style differed in small details, which caused warping and noise; merging them by hand in Photoshop gave steadier motion. (5) Turn on ComfyUI previews: stop the run in the first steps if it looks wrong.

**Use it:** AI shot QC notes: check hands, text and surface details first; most fixes are an extra anchor frame or a more specific prompt.
