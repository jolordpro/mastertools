---
id: redshift-greyscalegorilla-sponge-displacement-color-layer-recipe
title: Sponge recipe: displace through a Color Layer of patterns, centre the displacement range so it goes in as far as out, use Screen to add bumps and Multiply to cut holes
domain: redshift
tags: [greyscalegorilla, nick, sponge, displacement, color layer, ramp, subsurface, object tag, screen space adaptive, multiply, screen, deep-read]
applies_to: Redshift for Cinema 4D (2024 video)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Bzt7uYwsT9g, src:yt-transcripts, https://www.youtube.com/watch?v=MuVzbVhMUvI, https://help.maxon.net/r3d/cinema/en-us/Content/html/Displacement.html]
feeds: [[redshift, lookdev]]
conflicts: [maxon-docs]
---
Nick (Greyscalegorilla, 2024). Pass the model to a new scene as its own mesh ("current state to object"). Light: bright rim for subsurface, back cyc, gobo on the face for shadow detail, HDRI for overall brightness [02:06-02:37]. Material [03:08-03:38]: subsurface colour buttery yellow, weight cranked to full, radius a slightly brighter yellow, scale turned down so light "barely comes through". Displacement node into the material output; if nothing happens, the object needs a Redshift Object tag (tags > render tags), Geometry set to override enabled, screen-space adaptive turned off, max displacement raised and scale tuned [04:08-05:10]. Control: combine maps through a Color Layer node [05:10-05:40]; put a Ramp between texture and layer to make the effect subtler; 50% grey is the surface, white goes out, black goes in, so set the displacement range to centre on 0.5 (he says 0.5 to 0.5; likely means a symmetric range, number unsure) so it goes in as much as out [06:43-07:14]. Layer same pattern at different scales (10x10 fine, 4x4 larger) to break repetition. Dots pattern: Screen blend adds white (bumps), so invert the dots with a Ramp and use Multiply to cut holes; scale layer 3 higher for more holes [08:49-11:27].

**Use it:** Starter for organic porous looks; exact displacement range and tag values must be confirmed against the redshift ledger at the gate.
Transcript support: Tessellation recipe from Chad: override geometry, tessellation on, Screen Space Adaptive off, minimum edge length 0 for uniform subdivision; a subdivision of 1 enough, 2 safe, 6 too much on faceted low-poly toys; out-of-frustum tessellation factor exists (2017, Redshift 2.x). (https://www.youtube.com/watch?v=MuVzbVhMUvI [29:17-31:20])
Maxon check (2026-10-31): CORRECTION: since Redshift 3.6.04 C4D has Automatic Displacement: a material with a Displacement shader and texture displaces with no Redshift Object tag (height maps get automatic max displacement; vector maps still need it set). The docs place the switch under Render Settings > Advanced > System > Legacy. Tag settings win when present. (https://help.maxon.net/r3d/cinema/en-us/Content/html/Displacement.html)
