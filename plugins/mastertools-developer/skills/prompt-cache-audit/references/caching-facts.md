# Prompt caching facts

Last checked: 2026-09-30. Prices, minimums and model lists change with every model release. Before quoting one to a user, re-check it against the official page, and say so if you couldn't:

- Prompt caching: `https://platform.claude.com/docs/en/build-with-claude/prompt-caching.md`
- Pricing: `https://platform.claude.com/docs/en/about-claude/pricing.md`

If the `claude-api` skill is available, its `shared/prompt-caching.md` is the fuller reference and wins over this file where they differ.

## The field

```json
"cache_control": {"type": "ephemeral"}               // kept 5 minutes
"cache_control": {"type": "ephemeral", "ttl": "1h"}  // kept 1 hour
```

- On a content block (a system text block, a tool definition, a message block) it is an explicit marker. At most 4 per request.
- At the top level of the request it turns on automatic caching: the API marks the last block and moves the marker forward as the conversation grows. It uses one of the 4 slots.
- If both limits are used in one request, the 1-hour markers must come before the 5-minute ones.

## What it costs

| | Price, relative to normal input |
|---|---|
| Reading a cached part | about 0.1x (lower on some models; check the pricing page) |
| Saving with the 5-minute limit | 1.25x |
| Saving with the 1-hour limit | 2x |

Break-even: with the 5-minute limit, the second request already comes out ahead (1.25 + 0.1 against 2.0). With the 1-hour limit it takes three requests (2.0 + 0.2 against 3.0).

Every read restarts the timer at no charge. The timer runs from the start of the request, so a reply that takes four minutes to generate leaves one minute of a 5-minute entry.

## Choosing the time limit

| Gap between starts of requests that share the opening | Use |
|---|---|
| Under 5 minutes | 5-minute limit |
| 5 to 60 minutes | 1-hour limit, if there are at least three requests |
| Over an hour | Don't cache |

## Minimum length

A marker on a shorter opening is ignored without an error: `cache_creation_input_tokens` comes back 0.

| Model | Minimum tokens |
|---|---:|
| Claude Opus 5.5, Opus 5, Fable 5, Fable 5.1 | 512 |
| Opus 4.8, Sonnet 5, Sonnet 4.6, Sonnet 4.5 | 1024 |
| Opus 4.7 | 2048 |
| Opus 4.6, Opus 4.5, Haiku 4.5 | 4096 |

The minimum does not simply fall with newer models, so look the model up rather than guessing.

## What discards a cached part

The match is on exact bytes, in the order tools, system, messages. A change invalidates its own section and everything after it.

| Change between two requests | What is lost |
|---|---|
| Different model | Everything (each model has its own cache) |
| Tool definitions added, removed or reordered | Everything |
| System text changed | System and messages |
| Thinking or effort setting changed | Messages always; on some models system and tools too |
| `tool_choice` changed, images added | Messages only |
| An earlier message edited or removed | Messages from that point |

Caches are also separate per workspace (per organization on some cloud platforms), so the same prompt sent from two workspaces never shares.

## Reading the result

| `usage` field | Meaning |
|---|---|
| `cache_creation_input_tokens` | Saved on this request, at the higher price |
| `cache_read_input_tokens` | Read on this request, at the low price |
| `input_tokens` | The rest, at the normal price. Not the whole prompt. |

Whole prompt = the three added together.

A healthy conversation: reads grow each turn, writes stay small (roughly the last reply plus the new message). Writes near the full conversation size on every turn mean the opening is changing somewhere.

To find where: log two consecutive request bodies, remove the `cache_control` markers, and compare. The first difference inside the part they should share is the cause.

## Warming up ahead of time

A request with `max_tokens: 0` saves the cache and returns at once with no output billed. Worth it only when the first reply's delay is visible to a person, the opening is large, and there is a natural moment to send it (startup, deploy). It is rejected together with streaming, structured output, or forced tool choice.
