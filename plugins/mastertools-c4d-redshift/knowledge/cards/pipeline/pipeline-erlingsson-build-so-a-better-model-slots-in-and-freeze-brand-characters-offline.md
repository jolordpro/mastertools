---
id: pipeline-erlingsson-build-so-a-better-model-slots-in-and-freeze-brand-characters-offline
title: "Erlingsson: build client workflows so a new model improves them rather than breaks them, and keep brand-specific characters on a frozen, offline setup"
domain: pipeline
tags: [ingi erlingsson, comfyui, model swap, pipeline, brand character, lora, production window, sora, polish, ingi-erlingsson, deep-read]
applies_to: any
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=4xS4LOn3CTE, src:yt-transcripts, src:polish-roster]
feeds: [CHECKS]
conflicts: none
---
He says time spent tuning to one model is wasted when the next model arrives, like building a wrapper around a chatbot [29:05-30:08]. For client work, build so that a new model is simply better [30:08].
Where a brand character must not change (his example: a trained LoRA around a licensed character on a public platform), you need something offline and not centralised [34:17]. Ad production windows are about three weeks, rarely three months, and a model being pulled mid-project is rare, though Sora went without warning [34:49-35:20].

**Use it:** Version-pin models and weights used on a job; keep the render recipe separate from the model so it can be re-pointed.
