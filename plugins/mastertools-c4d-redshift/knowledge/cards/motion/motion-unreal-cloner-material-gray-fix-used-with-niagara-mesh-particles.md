---
id: motion-unreal-cloner-material-gray-fix-used-with-niagara-mesh-particles
title: In Unreal's Cloner, a mesh whose materials show grey needs 'Used with Niagara Mesh Particles' ticked on the master material
domain: motion
tags: [unreal engine, cloner, material, niagara mesh particles, gray material, fix, school of motion, deep-read]
applies_to: Unreal Engine 5.4 preview (2024)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=DOgfmp_ot9E, src:yt-transcripts]
feeds: []
conflicts: none
---
School of Motion [06:47-08:21]. After assigning materials to the hex inside the Cloner nothing showed until the hex was pulled out and put back (the author is unsure if this is a bug). Separately, materials on cloned meshes can show as plain grey: open the material, go to its parent master material in the hierarchy, scroll down and tick 'Used with Niagara Mesh Particles', save, and re-insert the mesh into the Cloner if needed.

**Use it:** Add to a real-time troubleshooting list: grey clones means a missing usage flag on the master material, not a missing texture.
