---
id: pipeline-solaris-houdini-env-renderman-line-first-append-houdini-path-redshift-needs-pxr-plugin-path
title: Houdini Solaris with several renderers (2020): RenderMan's env lines must come first in houdini.env, HOUDINI_PATH must be appended not overwritten, and Redshift needs its Solaris plugin path
domain: pipeline
tags: [solaris, houdini.env, houdini_path, renderman, arnold, redshift, hydra delegate, environment, deep-read]
applies_to: Houdini 18.0.532 with Karma beta, RenderMan, Arnold, Redshift (video 2020)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=q-vXgQYDUL8, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Per RenderMan's docs, its environment variables must be listed first in houdini.env, because an older bundled RenderMan 21 plugin must be unloaded before the new one loads [03:43-04:45].
HOUDINI_PATH ends with the append token (semicolon and ampersand on Windows; Linux uses colons) [05:16-06:49]. Each renderer's installer may write a plain line that overwrites the earlier ones; append instead so every renderer stays loaded [05:46-06:49].
Redshift needs the PXR_PLUGINPATH_NAME variable pointing at its Solaris folder, not the plain Houdini plugin folder; it follows the Houdini version variable, so it breaks if the version differs [07:20-07:52]. RenderMan and Arnold load their Hydra delegates from the path alone [09:24].
Check: after restart the top menu shows Redshift and RenderMan menus, and the stage context's renderer menu lists RenderMan, Arnold, Redshift [08:23-09:24].

**Use it:** If a renderer vanishes from Solaris, check env order and the append token first.
