---
id: comp-perez-aces-look-in-viewer-not-baked-in
title: Preview the director's look in the viewer with LMTs, CDL or a viewer input process, and only bake it into files when someone asks for a QuickTime
domain: comp
tags: [victor perez, foundry, fmx, aces, look, cdl, viewer, review, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Y2mcVM8c7cA, src:yt-transcripts]
feeds: [coach, motion-critique]
conflicts: none
---
Failure he describes: comp for weeks on ungraded footage, then the colourist goes very dark and the work no longer holds. The look is the intent, so view it while you work and watch the highlights or shadows it will push [33:27-33:58].
Apply the look through OCIO file, CDL or look nodes in the viewer, not in the files, unless asked for a movie for an iPad or review [34:29].
A node named viewer_input becomes the viewer process: it changes what the monitor shows, not the pixel values; sampling with it off shows unchanged values [47:29-49:04]. Several LMTs apply in order [35:30].

**Use it:** For sports packages, keep the broadcast look as a viewer-only layer in comp and render the clean version; bake only the review movie.
