---
id: pipeline-solaris-render-settings-node-takes-over-the-viewport-settings-and-must-be-wired-in
title: In Solaris a Render Settings node overrides the viewport delegate's own settings once it is active; lights and the settings node only work when wired into the displayed chain
domain: pipeline
tags: [solaris, render settings, display flag, hydra, viewport, integrator, deep-read]
applies_to: Houdini 18.0 Solaris, 2020
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=lidw4rllGV4, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Viewport settings (press D over the viewport, Render tab) are for fast preview, for example Karma at 8-16 pixel samples [04:41-07:46].
For the final image build a Render Settings node: camera, resolution and per-renderer tabs [18:45-19:16]. Connect it under the camera and put the display flag below it; then it appears as a choice in the viewport [19:16-19:48].
Trap: once a Render Settings node is active it takes over, so changing RenderMan's integrator in the viewport seems to do nothing; disable the node or change the setting there [19:48-20:50].
Several Render Settings nodes (low-res preview, final) can be switched [20:50-21:20].
Lights, dome lights and similar nodes are inert if floating; they must be in the network upstream of the display flag [10:24-11:27].

**Use it:** Troubleshooting order for 'my change does nothing' in a USD lighting pipeline.
