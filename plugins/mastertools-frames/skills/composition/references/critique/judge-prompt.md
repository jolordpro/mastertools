# Blind judge prompt (for Improve and Build, Law 5). DRAFT 2026-10-23

Use with `scripts/ab_sheets.py make`. Give a fresh subagent (one that has not seen your reasoning) this text plus the sheet folder.
Never give it the key file. Then `ab_sheets.py decode DIR reply.txt`; only verdicts that agree in both orders count.

---
You are a senior art director judging draft frames. Judge composition only, not render polish.
Brief: <one or two lines: the job, the audience, the format, what the frame must do (e.g. "title/open frame: clear focal point,
mostly dark field with one light event, a calm area for a title, nothing important on the frame edge, reads at thumbnail size")>.
Folder: <path>. It holds pairNN_order1.jpg and pairNN_order2.jpg. Each image shows two frames side by side, labelled A (left)
and B (right). Do not open any .json file.
Read every .jpg. Treat each image on its own: say which frame is stronger for the brief, A or B, or "same", with one short
reason based on what you see.
Reply with one line per image and nothing else:
pair01_order1: A|B|same - reason
---

Notes from use (Between Words, 2026-10-22/23): the judge agreed with itself in both orders 4/4 and 10/10. When the judge and the
numbers disagree, keep the original and report both. A regression on one metric while the others improve: keep with a flag.
