---
id: redshift-standard-material-transmission-depth-and-scatter-color-fake-sss
title: Redshift 3.5 Standard material transmission Depth and Scatter Colour work like a backlight/SSS hybrid, replacing extinction and absorption tweaks
domain: redshift
tags: [transmission depth, scatter color, scatter anisotropy, plastic, backlit, redshift standard material, deep-read]
applies_to: Redshift 3.5 / C4D R26 Standard material (2022)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=DmeiTnrqp3I, src:yt-transcripts, https://www.youtube.com/watch?v=a5BDzPkwlUM]
feeds: [lookdev]
conflicts: none
---
Derek Kirk [05:20-11:37, 13:43-15:49]. Depth 0 = light spreads evenly. Raising it (0.1 first) lets light fill only thin corners while thick middles stay dark; more depth reveals more of the Transmission colour and less of the Scatter colour; values go past 10, and 50 floods the object with light so the scatter colour is overridden [06:54-07:54, 11:07-11:37]. Scatter colour multiplies the light that gets inside: white gives milky plastic, yellow over red transmission gives a gradient. Combine with Extra Roughness for a stronger gradient. Scatter anisotropy: below 0 hugs the surface edges, above 1 pushes colour toward the back. He prefers these to extinction and absorption [10:06-10:36]. Scatter colour does nothing at depth 0. Free presets were offered by the speaker.

**Use it:** A fast route to waxy, candy-coloured plastics; adjust Depth first, then scatter colour.
Transcript support: transmission scatter colour and depth are single scattering; near-zero depth is almost opaque; combine with subsurface at about 50 percent transmission for juice. (https://www.youtube.com/watch?v=a5BDzPkwlUM [01:20-02:48])
