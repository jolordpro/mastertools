---
id: pipeline-edit-file-owns-shot-names-and-lengths-then-pushes-to-tracker
title: Blender Studio keeps shot name and length in the edit; a meta strip pushes them to Kitsu, and a timing change forces animators to pull the new range
domain: pipeline
tags: [nick alberelli, blender studio, kitsu, editorial, meta strip, shot length, frame range, shot naming, insert shot, deep-read]
applies_to: Blender 3.x/4.x, Kitsu
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jiXB5X1S1AI, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Nick Alberelli (TD, Blender Studio) [00:37-02:11, 12:02-15:39]: the storyboard or previs edit sequence is the source. A meta strip per shot holds name, position and length; one button uploads it to Kitsu with default tasks (animation, lighting, effects).
When timing changes, he pushes new metadata to the server; each open shot file then shows a big red stop until the artist pulls the frame range [43:57-46:24].
Naming leaves gaps (shot 10, 20) so a new shot can be inserted by using the extra zero [43:57]. Shot files start at frame 101 for headroom [45:32].

**Use it:** use as a model for an edit-first tracker: the cut owns durations, and files must be told when it changes.
