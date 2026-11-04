---
id: pipeline-fmx-auto-rig-before-the-models-exist-and-rebuild-the-3d-scene-in-nuke-from-exr-metadata
title: "FMX 2014 TD (Tim Wagner): agree modelling standards so an auto-rigger did about 70% of rigs before models, and rebuild the Nuke 3D scene from EXR metadata"
domain: pipeline
tags: [fmx, tim-wagner, pipeline, rigging, nuke, exr-metadata, student, deep-read]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=8tW77BsgtPY, src:yt-transcripts]
feeds: [pipeline design]
conflicts: none
---
He agreed standards with the modellers so an auto-rigger could produce about 70% of the rigs before the models were final; animators got automated secondary motion such as a rolling deformer that respects radius [43:08-44:45].
On a later spot he stored scene data in EXR metadata so a button click rebuilt the comp in Nuke: Alembic meshes back, lights mapped (Nuke does not know V-Ray lights), so compositors can place cards knowing where things are [50:35-51:38].
Other student projects (OCIO nodes in Houdini COPs, a CUDA cloth server, a C++ wrapper that renames 40,000 Maya nodes in 1.3 s versus 8.6 s) had no process lessons [46:52-50:03].

**Use it:** Standardise modelling rules so rigging and passes can be automated; stash scene info in EXR metadata for comp rebuilds.
