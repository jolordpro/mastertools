---
id: lookdev-mpc-one-shader-for-a-path-tracer
title: MPC moved to a single shader model on a path tracer, since a light-transport renderer wants fewer variables
domain: lookdev
tags: [mpc, renderman, ris, shader, path tracing, lookdev, polish, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.fxguide.com/?p=185599, src:polish-roster]
feeds: [polish coach]
conflicts: none
---
Valdez says the biggest job in the switch to ray tracing was replacing the whole shader set: separate skin, hair and hard-surface shaders became one model. His reasoning: when the tracer already transports light, extra shader variables only get in the way. Also, the more accurate the light model, the more robust assets, lighting setups and lookdev must be. [§7]

**Use it:** When a render looks off under physical light, suspect the asset or shader before adding lighting hacks.
