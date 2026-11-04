---
id: c4d-2023-1-freeze-grow-on-a-vertex-map-needs-a-multiplied-random-field-to-look-organic
title: Organic growth in a vertex map: put a Random field above Freeze/Grow, multiply it against the original selection, and enlarge the noise scale
domain: c4d
tags: [mitch scott, behind the button, freeze, grow, vertex map, random field, multiply, decay, cinema 4d 2023.1, cloth, deep-read]
applies_to: Cinema 4D 2023.1 (video uploaded 2023-03)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=tQbqZzk7Kc0, src:yt-transcripts]
feeds: [motion-critique]
conflicts: none
---
Why a vertex map: a dense plane (width/height segments) gives fine resolution, where a cloner would need huge clone counts [06:17-06:49]. Setup: vertex map tag with a box field for the seed selection, Freeze in Grow mode on top [06:49-07:19].
Radius matters again, tied to point spacing: 40 grew slowly and looked dull and mechanical (he says he meant 300 after) [07:19-07:51].
A plain Random field on top gets pushed to full by Grow, so nothing is gained. Set the Random field's blend to Multiply so it restricts the growth to the original selection; the radius still sets speed [07:51-08:53]. Because it applies later, it does not push other values up; stacking another random field or another Freeze can help [08:23-08:53].
Other blends: Subtract looked different at first; Screen/Clip came back close to the no-random look [08:53-09:56]. Multiply was best here.
To read more natural: switch noise type to turbulence, and raise the noise scale (large patterns changed the look a lot) [09:56-10:29]. A Decay on top keeps bright values longer [10:29-11:00]. Because it lives in a vertex map, it can drive deformers or dynamics, for example cloth that transitions [11:00].

**Use it:** for a spreading mask on a mesh (dissolve, burn, infection), build vertex map + Grow + multiplied turbulence field, and animate the noise rather than keying the mask.
