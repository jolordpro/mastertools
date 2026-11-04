---
id: pipeline-moonray-aswf-integration-points-hydra-materialx-opencue
title: MoonRay as an ASWF integration point: Hydra delegate for viewport scale tests, MaterialX for material transfer, and Rez plus OpenCue for deployment at scale
domain: pipeline
tags: [[moonray, aswf, hydra delegate, materialx, openvdb, ocio, openexr, openimageio, rez, opencue, snap installer, bill ballew], deep-read]
applies_to: MoonRay, ASWF projects
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=fQUnq6drevw, src:yt-transcripts, https://www.youtube.com/watch?v=GE6Af6hjYfI, https://www.youtube.com/watch?v=0gXT3sntiFg, https://www.youtube.com/watch?v=fnbRcTeKirw]
feeds: [[]]
conflicts: none
---
Ballew's pitch for MoonRay in the foundation [16:13-18:59]: its native OpenUSD Hydra delegate pressure-tests asset scale in a viewport; MaterialX support can be a baseline for moving material definitions between platforms; it exercises OpenVDB, OpenColorIO, OpenEXR and OpenImageIO for performance; and deployment through Rez with OpenCue helps harden scale-out tooling.
Early wins within a couple of months: tied into the CI working group's build infrastructure, a snap installer for several Linux versions, monthly steering meetings, 119 channel members, Hydra delegate talks with Foundry, patches for Houdini 21 and Hydra 2.0, a Microsoft effort for Windows, and a Blender Foundation test framework comparing OpenPBR implementations [17:28-18:59].

**Use it:** supports a USD, MaterialX, OCIO and EXR base for the platform, and OpenCue as a farm option.
Transcript support: OpenCue as an Academy Software Foundation project: opened Jan 2019, Postgres and gRPC replaced Oracle and ICE, Linux only, Windows and in-memory scheduler on the roadmap (https://www.youtube.com/watch?v=0gXT3sntiFg [03:07-10:43])
Transcript support: OpenCue is Imageworks' internal Q3 scheduler, running Oracle then Postgres; gives scale numbers (https://www.youtube.com/watch?v=fnbRcTeKirw [09:19])
