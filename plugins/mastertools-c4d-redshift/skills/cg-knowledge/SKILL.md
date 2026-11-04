---
name: cg-knowledge
description: Front door to the local CG knowledge base, a few thousand checked, dated, sourced cards on Cinema 4D, Redshift, rendering, lighting, look development, compositing, motion design, render farms and GPU cloud, broadcast delivery, pipelines, AI for 3D, and how top studios work. Use it BEFORE a web search or an answer from memory on any of those topics, before giving a render setting, number, version fact or price, and whenever someone says "what does the knowledge base say", "check the cards", "search Knowledge", "is there a card for", or cites a card id. Also use it when a skill edit, plan or brief needs evidence from the cards, since it says which cards count as evidence. Works beside the redshift skill (its ledger outranks every card), elevate, composition, motion-critique and shakedown. Not for web or app UI, code unrelated to CG, or general questions with no CG fact in them.
---

# CG knowledge

A local knowledge base of cards. Each card holds one fact or rule, with its numbers,
the versions it applies to, its source, when it was read, and how sure we are.
It exists so sessions answer from checked notes instead of searching the web again.

## 1. Find it

```
python3 -I <this skill>/scripts/cgk.py where
```

The location comes from `$CG_KNOWLEDGE_DIR`, else the first line of
`~/.config/cg-knowledge/dir`, else the cards bundled with this plugin at
`${CLAUDE_PLUGIN_ROOT}/knowledge/`. It is set once per machine and never kept in this skill.

- **Exit 3 (not reachable):** say once that the knowledge base isn't on this machine,
  then work as usual. Don't search the disk for it.
- **Found:** read the base's own `README.md` once per session. It is the authority on
  its rules, folders and how cards get added. This skill only covers using it.

## 2. When to search

Search first, then decide whether the web is needed:

- Before any web search on the topics in this skill's description.
- Before stating a setting, a number, a default, a version fact, a price or a speed.
- When a plan, brief or critique leans on "how pros do it".
- When a card id appears anywhere (`lighting-...`, `redshift-...`): open it, don't guess.

Skip it for quick talk with no fact at stake.

## 3. How to search

```
python3 -I <this skill>/scripts/cgk.py find <words>
python3 -I <this skill>/scripts/cgk.py show <card-id>
```

- Use separate plain words. Try two or three phrasings, including trade synonyms
  (the base's `glossary.md` lists them): "fireflies clamp", then "noise hot pixels".
- Results rank by how many of your words matched. When nothing fits, you still get
  near matches. Read the titles and judge them. A `(1/4 words)` hit is usually noise.
- Open a card with `show` before you use it. The one-line preview drops the
  version, the source and the conditions.
- Look at `applies_to`. A rule for another renderer or version is a hint, not a fact.

### Cards for one skill

Every card's `feeds:` names the skills, checks and plan steps it serves.
`cgk.py feeds` lists those names; `cgk.py feeds <skill> [--all]` lists that skill's cards.
When working for a skill, search these folders first:

| Skill | Card folders |
|---|---|
| redshift | `redshift` (its ledger still wins), then `lighting`, `lookdev` |
| elevate | `lighting`, `lookdev`, `comp`, `c4d`, `redshift`, plus the base's `polish-profiles.md` |
| composition, post-composite | `comp`, `lighting`, `motion`, `broadcast` |
| motion-critique | `motion`, `broadcast` |
| motion-system-architect | `motion`, `agencies` |
| shakedown | `broadcast` (delivery and QC) |
| render cost and farms | `gpu-cloud`, `pipeline` |
| C4D scene work | `c4d`, `redshift` |

## 4. How much weight a card carries

Every card has a **status** and a **confidence**. Read both.

| Card | Use it as |
|---|---|
| `V` · high | Fact. A primary vendor doc or standard with exact values. Cite it. |
| `V` · medium | A working pro stating specifics. Use it, cite it, name whose practice it is. |
| `V` · low | One creator, rough captions or hearsay. A lead. Say it's low confidence. |
| `V2` | Built from a page summary, not the page. A lead only: check the source first. |
| `U` | Our own inference or maths. Never evidence. |

**Why V2 is only a lead:** when 210 cards built from web-fetch summaries were checked
against the full pages, 83 needed corrections and 11 weren't on the page at all.
Summaries pad, misattribute and drop numbers.

Also check:
- **`recheck_by` in the past:** the card may be stale. For fast fields (prices, versions,
  cloud offers, AI models) check the live source before relying on it.
- **`conflicts:`** `ledger` means the redshift ledger disagrees and wins.
  A card id means two cards disagree: read both and say so.

`cgk.py grade <ids>` prints the verdict per card: **EVIDENCE** (V, medium or high,
in date, no open conflict), **TO-VERIFY** with the reason, or **MISSING**.

## 5. What outranks a card

1. **The redshift skill's ledger**, for every Redshift fact it covers. Load the redshift
   skill (the Skill tool, `c4d-redshift:redshift`) for any Redshift value, and never quote a Redshift
   setting from a card alone. A value only a card carries is "card-backed, not in the
   ledger": say so next to it.
   A card that disagrees with the ledger is a proposed ledger update, not an answer.
2. **Any skill on its own turf.** A skill's measured rules beat a card's general one.
3. **A newer primary source** (vendor docs, release notes) beats an older card.
   Say which card it overturns so it can be fixed.

## 6. Cite what you use

- Name the card id in backticks with its grade: `redshift-bucket-quality-presets-set-threshold` (V·medium).
- Put it in your own words. At most one quote under 15 words.
- Say where the base ends: "no card on this; from the web" or "no card; from memory, unverified".

## 7. Using cards as evidence for a skill, plan or brief

When cards justify a change to a skill, a checklist or a plan:

- Only **EVIDENCE** cards count. Run `cgk.py grade --strict <ids>` and list the ids.
- V2, U and low-confidence cards can be named only as "to verify", never as the reason.
- Redshift facts go through the ledger, never straight into another skill.
- Skills cite cards in our own words. No transcript or page passages.

## 8. When the base has nothing

1. Say so plainly, with the words you searched.
2. Search the web. Prefer full reads of primary sources.
3. If the finding is worth keeping, follow the base's `README.md` and `RESEARCH-SYSTEM.md`
   for adding it. Don't edit existing cards or `staging/`. A card you think is wrong
   gets a line in `proposals/contradictions.md` (card id, what disagrees, source),
   so the base's checks still run.

## Stand down

- No fact at stake, or a topic outside CG: don't load the base.
- The user wants a fresh look, not what the cards say: answer, then offer the cards.
- A measured result in this session beats any card. Log the disagreement as a proposal.
