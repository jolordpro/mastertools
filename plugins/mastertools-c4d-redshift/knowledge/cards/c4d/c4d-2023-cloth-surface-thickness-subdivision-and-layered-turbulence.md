---
id: c4d-2023-cloth-surface-thickness-subdivision-and-layered-turbulence
title: Finish cloth without simulating the heavy mesh: Cloth Surface adds thickness (about 0.25 cm in the demo), a Subdivision Surface rounds it, and two Turbulence forces at different scales give fine wrinkles
domain: c4d
tags: [cloth, cloth surface, thickness, subdivision surface, turbulence, layered noise, friction force, simulate, deep-read]
applies_to: Cinema 4D 2023 new simulation system, cloth (School of Motion, EJ, Oct 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dHQWVXWbsEM, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
EJ [01:06-07:50; 11:22]. Add the Cloth tag from the new Simulation tags (not the old bullet tags) and a Collider tag on the other object; start with no intersection or things stick [01:36-02:08]. Raise the collider's segments and Phong angle to hide chunky geometry [02:40].
Wrinkles: layer Turbulence forces, one small scale with high strength (looks like rippling water) and one larger scale with lower strength; frequency sets how fast the noise moves [05:16-06:49]. A Friction force object (values like 250 are normal, the particle-force numbers are odd) avoids editing every cloth tag [11:22].
Thickness: with Cmd/Ctrl held add a Cloth Surface as parent, thickness 0.25 cm in the demo, then another Subdivision Surface as parent set to 1/1 to round the edge [06:49-07:50]. Turn these off while simulating and on for the cache or render [09:57; 18:47].

**Use it:** A standard cloth pipeline: light sim mesh, layered forces, cache, then surface and subdivision for the final.
