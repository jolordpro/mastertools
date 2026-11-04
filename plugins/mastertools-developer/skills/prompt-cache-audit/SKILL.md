---
name: prompt-cache-audit
description: Decide, from evidence, where Claude API prompt caching (`cache_control`) will actually save money or time in a codebase, then add it only there and prove it works. Use this whenever someone asks about cache_control, prompt caching, cache hit rate, "why is my cache_read zero", cutting Claude API input cost or latency, or "should we cache this prompt" - and also before adding `cache_control` to any request while writing or reviewing Claude API code, even if nobody asked for an audit. It covers every call site in a project (or several projects), returns a verdict per call site, and treats "don't cache this" as a normal outcome. Not for application-level caching (Redis, HTTP, CDN, memoization) and not for choosing a model or effort level.
---

# Prompt cache audit

Prompt caching is easy to add and easy to get wrong in a way nobody notices: a marker on a prompt that is never re-sent in time costs more than no marker, and nothing errors. So this skill decides from evidence first, and edits second. Most of the value is in the verdicts, including the ones that say "leave it alone".

Read `references/caching-facts.md` before quoting any price, time limit or minimum. Those numbers change with model releases; the file says when it was last checked and where to re-check.

## How caching works, in one paragraph

A request is rendered in the order `tools`, then `system`, then `messages`. A `cache_control` marker saves everything from the start up to that point. A later request that begins with exactly the same bytes, on the same model, within the time limit, pays about a tenth of the normal input price for that part. Saving it costs more than normal (1.25x for the 5-minute limit, 2x for the 1-hour limit). So caching pays only when the same opening text really is sent again in time. Everything below follows from that.

## Step 1: List every place the code calls Claude

Search the project for SDK imports, `api.anthropic.com`, model IDs and existing `cache_control`. For each call site note the model, what goes in `tools`, `system` and `messages`, and whether it is one request or a loop. If the request is about several projects, do this for each one, and check that you are looking at the live copy of each (an archived or frozen copy will mislead you).

List the call sites you found before judging any of them, so nothing is skipped silently.

## Step 2: Name the shape of each call

| Shape | What it looks like | Usual verdict |
|---|---|---|
| One-off | Unique content each time (a new document, a new photo), sent once | Don't cache |
| Fixed opening, changing ending | The same long instructions or reference text, then a different question each time | Cache the fixed part, if requests come close together |
| Conversation | Each request re-sends the earlier turns plus one new one | Cache the growing conversation |
| Tool loop | The code calls the model again seconds later with the same history plus tool results | Cache the growing conversation |
| Fan-out | Many parallel requests over the same context | Cache, but send one first (see Step 5) |

## Step 3: Get the evidence that decides it

Three questions per call site. Answer them from data where data exists, and say so plainly where you are estimating.

1. **How long between two requests that share the same opening?** This is the deciding fact. Look in the app's own records: a spend or usage log, database timestamps, request logs. Compare the start times of consecutive requests with the same opening text. Under 5 minutes: caching pays. Between 5 and 60 minutes: only the 1-hour limit pays, and it needs three or more requests. Over an hour: it doesn't pay. "It probably gets re-run" is not evidence; a re-run a week later reads nothing.
2. **Is the shared opening long enough?** Each model has a minimum length below which a marker is silently ignored (no error, nothing saved). Check the table in the reference file. A short instruction block on a model with a high minimum cannot be cached at all.
3. **Is input cost even the problem?** If the log shows the money going to output (long answers, heavy thinking) or to another provider entirely, caching input can't move the total much. Say how much is at stake before recommending work.

If the app records only total cost and not token counts, say that this is a gap and recommend recording input, output, cache-read and cache-write token counts per call. Without them nobody can tell whether caching is working.

## Step 4: Give a verdict per call site

Use exactly one of these for each call site, with the evidence next to it:

- **Cache it** - the opening repeats within the time limit and is long enough. Say where the marker goes.
- **Already cached, leave it** - markers are in the right place.
- **Already cached, fix it** - markers exist but something breaks them or they sit in the wrong place (see Step 5).
- **Don't cache** - one-off content, gaps too long, opening too short, or too little money at stake. Say which.
- **Can't tell yet** - no records to judge from. Say what to record and for how long.

"Don't cache" is a good result. An audit that recommends caching everywhere has not looked at the gaps.

## Step 5: Add it where it pays

Place the marker where the stable text ends:

- **Fixed opening:** an explicit marker on the last block of the fixed part (usually the last `system` block). Not at the end of the whole prompt, or every request saves a copy nobody reads.
- **Conversation or tool loop:** automatic caching, which is a top-level `cache_control` on the request. The API puts the marker on the last block and moves it forward each turn. Keep an explicit marker on the fixed `system` text as well.
- **One-off jobs sharing a request builder with conversations:** turn automatic caching on per job, not for every request the builder makes. On a one-off job it is a pure surcharge.
- **Fan-out:** send one request, wait for its first streamed token, then send the rest. Parallel requests can't read a cache that is still being written.

Then look for things that quietly break the match. Any of these anywhere before the marker means nothing after it is ever read:

- a date, time, request ID or random value in the system text (move it to the end of the user message)
- a list or object serialized in an order that can change between runs (sort it)
- a tool list that differs per user or per mode, or that changes mid-conversation
- system text assembled from conditional pieces
- a different model, or a changed thinking or effort setting, between the two requests

Make the change in the one place the project builds its requests. If requests are built in several places, say so rather than adding markers to each.

## Step 6: Prove it

Two checks, because they catch different failures.

1. **A test that needs no API call.** Assert that the request carries the marker on the jobs meant to have it and on no others, and that a second request begins with the first request's exact bytes (same model, same system, same settings, earlier messages unchanged). This is what catches a later change that breaks the match.
2. **One real pair of requests.** The response's `usage` reports `cache_creation_input_tokens` (saved this time) and `cache_read_input_tokens` (read this time). The first request should show a write; the second, sent within the time limit, should show a read covering the shared part. A read of zero on the second request means something before the marker differs. Real requests cost money, so ask before sending them.

If you could only do the first check, say so. Don't report caching as working on the strength of a test that never reached the API.

## What to hand back

Lead with the overall answer in a sentence or two: how much this will save and where. Then one entry per call site: the verdict, the evidence (the measured gap, the opening's length against the minimum, the money at stake), and what changes, if anything. Then what you changed and what the tests showed, or that nothing was changed. Use plain words; the reader may not know what a breakpoint or a TTL is. Keep measured numbers and estimates visibly apart.

## If the question is about chat apps or Claude Code rather than API code

`cache_control` is a field in an API request. In Claude's chat apps and in Claude Code there is nothing to set; caching is handled for you. What still applies is the same rule about matching openings: switching model mid-session, or connecting and disconnecting tools mid-session, discards what was cached. Say that, and don't invent a setting.
