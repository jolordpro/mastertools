#!/bin/bash
# Shared helpers for the compaction hooks. Sourced, never run directly.
# Every function fails quietly (prints nothing) so a hook never breaks a session.

# Tokens in the current context: input + cache read + cache write from the newest usage record in the transcript.
# Transcript usage records aren't a documented interface, so a missing or changed format yields nothing.
context_tokens() {
  local t="$1"
  [ -f "$t" ] || return 0
  tail -c 3000000 "$t" 2>/dev/null | grep '"cache_read_input_tokens"' | tail -n 1 |
    jq -r 'try (.message.usage | (.input_tokens // 0) + (.cache_read_input_tokens // 0) + (.cache_creation_input_tokens // 0)) catch empty' 2>/dev/null
}

# The auto-compaction threshold: env var first, then ~/.claude/settings.json. Prints nothing when unset.
compact_window() {
  if [ -n "${CLAUDE_CODE_AUTO_COMPACT_WINDOW:-}" ]; then echo "$CLAUDE_CODE_AUTO_COMPACT_WINDOW"; return; fi
  jq -r '.autoCompactWindow // empty' "$HOME/.claude/settings.json" 2>/dev/null
}

# File age in seconds (macOS stat, then GNU stat).
file_age() {
  local m
  m=$(stat -f %m "$1" 2>/dev/null || stat -c %Y "$1" 2>/dev/null) || return 0
  [ -n "$m" ] && echo $(( $(date +%s) - m ))
}

# "no" when PROGRESS.md in the given folder says "Safe to compact: no"; otherwise nothing.
checkpoint_busy() {
  local p="$1/PROGRESS.md"
  [ -f "$p" ] && grep -i -q -E '^[^A-Za-z]*safe to compact:[*_ ]*no\b' "$p" && echo no
}

state_file() { echo "${TMPDIR:-/tmp}/mastertools-compact-${1:-unknown}"; }
