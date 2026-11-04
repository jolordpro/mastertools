---
id: pipeline-fmx-standard-render-elements-and-non-destructive-lighting-scene-assembly
title: "FMX 2014 TD (Tim Wagner): one-button standard render elements for every lighter, and lighting scenes assembled from per-task assets that artists edit locally"
domain: pipeline
tags: [fmx, tim-wagner, pipeline, aov, render-elements, vray, student, deep-read]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=8tW77BsgtPY, src:yt-transcripts]
feeds: [redshift, pipeline design]
conflicts: none
---
Tim Wagner (pipeline/lighting/shading TD) designed the Rugby Bucks pipeline so each department only sees what it needs and interfaces stay clean [39:18-40:32].
Each asset (animation Alembic cache, hair, shading) was a separate task; the lighting scene assembled them by script as a local edit, so each artist could iterate until the interface changed [40:32-41:04].
Render deconstruction/reconstruction was standardised: scripts set a linear workflow and the right V-Ray render elements at the push of a button for any lighter, so comp always got the same output and could grade on the light element alone [41:04-42:05].

**Use it:** AOV/light-group template: one preset applied to every shot so comp can rebuild with a fixed recipe.
