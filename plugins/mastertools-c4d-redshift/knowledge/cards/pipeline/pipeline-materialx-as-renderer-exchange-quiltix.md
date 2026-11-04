---
id: pipeline-materialx-as-renderer-exchange-quiltix
title: MaterialX is the exchange format that lets a material move between renderers; QuiltiX is a free node editor for it
domain: pipeline
tags: [materialx, quiltix, hydra, exchange, redshift, arnold, usd, look development, deep-read]
applies_to: Prism 2 (private beta mid-2023), QuiltiX early dev
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=GE6Af6hjYfI, src:yt-transcripts]
feeds: []
conflicts: none
---
Manuel Köster (Remedy) [30:48-31:20]: if materials are authored in MaterialX they survive moving between renderers (his example: Arnold years ago, then redshift for GPU), instead of recreating them. QuiltiX is open source, standalone, uses a Hydra viewport (Storm by default; Arnold or Redshift can be plugged in) and shows a USD stage plus MaterialX nodes only [31:20-33:54, 34:24-35:26].
Features: live preview as sliders move; load custom geometry and assign materials to a part [36:35-37:07]; hover/drag shows the type an input needs; tab menu lists only nodes that can plug in; a convert node keeps its types in a dropdown instead of 15 menu entries [37:39-38:43]; the graph is viewable as text [39:17]. Colour workflow was not done yet; the shipped USD includes OCIO [47:28]. Still part-time, beta testers sought; planned on PyPI [40:51-41:22]. Prism lets you open a material from the library in QuiltiX, save new versions and switch layers back [42:26-43:58]. Beta planned July 2023 [44:29].

**Use it:** Note as a lead for look-dev handoff; C4D Redshift materials are not MaterialX yet, so check support before promising portability.
