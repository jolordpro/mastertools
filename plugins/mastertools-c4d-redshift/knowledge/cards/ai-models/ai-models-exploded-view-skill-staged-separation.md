---
id: ai-models-exploded-view-skill-staged-separation
title: An exploded-view skill only worked once the agent was told to act like an engineer and puzzle-maker and pull parts apart in stages
domain: ai-models
tags: [[claude skill, exploded view, cad, c4d, push apart, hill climbing, greyscalegorilla, chad ashley], deep-read]
applies_to: Cinema 4D with the C4D MCP, Claude skills
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=ysIL6NORGIo, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Chad Ashley (Greyscalegorilla) built a skill for CAD-style exploded diagrams, where each part slides out along its own path [1:02:20]. The Push Apart effector was not enough because it has no sense of which pieces sit inside others [1:02:51].
It took him about three days of back-and-forth ("hill climbing"). The key instruction was to behave like an engineer who is also a puzzle maker: parts leave in stages, because some pieces are inside others [1:03:22].
He tested on badly named, random machinery models from a CAD download site, and it still came out clean [1:03:22]. The skill also ships a C4D script that drops in a controller null with user data for speed and randomness [1:03:52].
Transfers: a skill earns its keep on jobs with a hidden order of operations (what must move first), not on single-setting tweaks.

**Use it:** when the platform offers a "fix this scene" skill, test it on messy, badly named client files, not only clean demo scenes, and give the agent the ordering rule in plain words.
