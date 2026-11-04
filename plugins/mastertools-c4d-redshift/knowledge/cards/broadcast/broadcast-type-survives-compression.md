---
id: broadcast-type-survives-compression
title: Proposed type check: downscale and compress a hero frame, run OCR (Tesseract, PaddleOCR); if it cannot read the text, a phone viewer cannot
domain: broadcast
tags: [type legibility, ocr, compression, small screens, tesseract, paddleocr]
applies_to: any
status: U
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [src:research-production-pipelines]
feeds: [type legibility check]
conflicts: none
---
Also measure cap height and thinnest stroke in output pixels, local contrast, bevel spread (must cover a couple of output pixels), and flag steep perspective or motion blur on type. Kerning outliers need a human eye.

