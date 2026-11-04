---
id: pipeline-nineb-non-destructive-material-edit-stores-only-overrides
title: Edit a delivered material non-destructively: USD stores only the changed parameters and references the original, and bypassing the edit restores it
domain: pipeline
tags: [nine between, houdini, solaris, usd, material edit, override, non-destructive, preview surface, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [CHECKS, coach]
conflicts: none
---
Load the asset's material into an edit node; its parameters are greyed until you activate one, and only activated parameters are written, so the file does not duplicate the whole shader [1:58:33-2:00:36]. He changed base colour and switched off subsurface to make a vanilla cake from a chocolate one, and re-pointed subsurface colour to make red velvet [2:00:36-2:01:37]. Bypassing the node returns the original.
Shaders also carry a USD preview surface as fallback for apps that do not read MaterialX; it can drive the viewport for complex shaders [2:02:08-2:02:39].

**Use it:** Ask vendors for assets whose materials can be overridden by layer, so client colour changes never touch the source asset.
