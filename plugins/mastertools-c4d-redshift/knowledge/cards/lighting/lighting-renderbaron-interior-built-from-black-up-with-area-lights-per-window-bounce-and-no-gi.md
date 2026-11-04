---
id: lighting-renderbaron-interior-built-from-black-up-with-area-lights-per-window-bounce-and-no-gi
title: "Renderbaron: an interior lit from pitch black upward with separate lights for sun, haze-sun, bounce, window and caustics, and a hand-placed bounce instead of GI"
domain: lighting
tags: [renderbaron, interior-lighting, cinema-4d, redshift, no-gi, manual-bounce, deep-read]
applies_to: C4D + Redshift
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=UWfmun5rxE8, src:yt-transcripts]
feeds: [redshift, elevate]
conflicts: none
---
Order of build: scene starts black; self-luminous background gives faint beige specular; add the dome sky for blue reflections; two area lights for windows (one visible, one off-camera); a directional sun with slight yellow tint; a second bluer sun with shadow softness 20 for atmospheric scatter [01:56-02:57].
Bounce is placed by hand: yellowish area light from the sunlit wall, wall-coloured large area light for indirect sun on the left, disc light over a white chair, a large wall-coloured area light behind the camera for diffuse fill [02:57-03:29].
Caustics from separate lights with small size and many photons for glass and candle; the wall caustic is a spotlight with a painted alpha texture [03:29-03:59].
Two cheap tricks: slight emission on the wall material to lift shadows, camera tone mapping. He uses no GI for his free works because it is a good lighting exercise and, with comp, looks photoreal [03:59-04:32].
Redshift ledger not checked: values quoted as stated; neutral.

**Use it:** Interior lighting checklist: separate light per physical source and per bounce colour, tinted sun pair, fill lights colour-matched to walls.
