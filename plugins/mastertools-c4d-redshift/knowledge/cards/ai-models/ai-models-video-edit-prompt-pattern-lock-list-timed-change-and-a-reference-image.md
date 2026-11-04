---
id: ai-models-video-edit-prompt-pattern-lock-list-timed-change-and-a-reference-image
title: Prompt pattern for AI edits of real footage: have an LLM read the clip and write a prompt listing everything that must stay fixed plus the exact seconds to change; give a reference image instead of describing a creature
domain: ai-models
tags: [higgsfield, seedance 2.0, ai vfx, prompt, lock list, reference image, handheld, deep-read]
applies_to: Seedance 2.0 via Higgsfield (June 2026)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=Yte-UGhYkPQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Promo video from the vendor. Workflow: drop the clip into Claude, which reads it as frames; add one sentence of change; the prompt it writes lists what stays exactly as shot (face, walk, rings, the handheld camera move; for the car shot the seatbelt and rig framing) and the exact time of the change [02:18-02:49, 03:52]. When you know the creature, make a reference image with an image model and attach it [06:30]. Locked-off shots are easy; handheld is the hard case, as the effect has to track parallax and shake [07:32]. His claims of no masking and relit faces are unverified; judge by results.

**Use it:** A prompt checklist for AI edit tests: lock list, timed change, reference image, camera note.
