---
id: pipeline-spring-storage-split-svn-repo-and-render-share
title: Spring split storage in two: a versioned repository for source files and a big shared /render volume for caches and frames
domain: pipeline
tags: [pipeline, storage, svn, subversion, shared storage, render farm, folder structure, blender studio, spring, deep-read]
applies_to: Blender 2.8 (Spring, 2019)
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=aR3yNNGK_sc, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
Andy Goralczyk (director of Blender's film Spring) says artists have two places to worry about [07:32]. The production repository on local disks, managed with Subversion because it handles binary diffs well, holds libraries (characters, props, environments, sets, maps), the edit, shots and scenes, tools and notes [07:32] [08:34] [09:39].
The shared storage ("/render") holds caches and final frames: a frames folder for raw farm output, a shots folder where renders are cleaned up, plates for reusable background renders, and an export folder with the latest film cut [10:09] [10:41].
A new export was rendered each Friday [10:41].

**Use it:** Template for platform folder layout: keep light source files in a versioned tree, put heavy caches and frames on a separate shared volume with raw, cleaned and export stages.
