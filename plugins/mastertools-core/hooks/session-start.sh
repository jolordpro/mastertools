#!/bin/sh
# The always-on and model-routing rules print from their own commands (scripts/render_rules.py --part N):
# Claude Code keeps only 10,000 characters of each hook command's output, so this script must stay under that too.
# After a compaction it also prints the project's checkpoint (the "## Now" section of PROGRESS.md), so the work resumes exactly.
# In a folder with an open sequence build (buildplan/), it prints "Use Skill(sequence) to resume it" and the checkpoint on every start
# plus a line for a gate card left open in buildplan/GATE.md. A done or parked build prints nothing.
# Never fails the session: missing files or tools print nothing.
# Hard cap on everything this script prints, whatever its parts add up to: it reruns itself through head.
if [ -z "${OSKIT_START_INNER:-}" ]; then
  OSKIT_START_INNER=1 sh "$0" | head -c 9000
  exit 0
fi
ROOT="${CLAUDE_PLUGIN_ROOT:-$(dirname "$0")/..}"
INPUT=$(cat 2>/dev/null || true)

# Print a "## Now" checkpoint. When it is long, keep its first lines (phase, next step) and its newest lines,
# so two checkpoints in one start still stay under the cap. $1 = the section, $2 = the PROGRESS.md it came from.
print_now() {
  if [ "$(printf '%s' "$1" | wc -c)" -le 3000 ]; then printf '%s\n' "$1"; return; fi
  echo "(This checkpoint is long, so only its first and newest lines are below. Read the whole \"## Now\" section of $2 before acting.)"
  printf '%s\n' "$1" | awk '{l[NR]=substr($0,1,1000)} END{
    h=0; t=0; for(i=1;i<=NR;i++){t+=length(l[i])+1; if(t>1000) break; h=i}
    s=NR+1; t=0; for(i=NR;i>h;i--){t+=length(l[i])+1; if(t>1800) break; s=i}
    if(h==0 && s>NR) s=NR
    for(i=1;i<=h;i++) print l[i]
    if(s>h+1) print "..."
    for(i=s;i<=NR;i++) print l[i]}'
}
command -v jq >/dev/null 2>&1 || exit 0
SOURCE=$(printf '%s' "$INPUT" | jq -r '.source // empty' 2>/dev/null)
CWD=$(printf '%s' "$INPUT" | jq -r '.cwd // empty' 2>/dev/null)
MODEL=$(printf '%s' "$INPUT" | jq -r '.model // empty' 2>/dev/null)

# The model field is optional; only speak up when it's present and isn't Opus.
case "$MODEL" in
  ""|*opus*|*Opus*) ;;
  *) echo "Routing note: this session's main model is \"$MODEL\". The routing rules expect Opus for the main thread. If this is substantive work, mention it to the user once.";;
esac

# A sequence build in this folder or one above it. Its status lives in buildplan/: the "status:"
# field on the first "Sequence:" line of BRIEF.md (Full) or CARD.md (Lite). Only an open status
# (planned, building) prints; done, parked or no status prints nothing. After a compaction in the
# build's own folder the compaction block below prints the checkpoint, so only the resume line prints here.
D="${CWD:-}"
while [ -n "$D" ] && [ "$D" != "/" ] && [ "$D" != "$HOME" ]; do
  if [ -f "$D/buildplan/BRIEF.md" ] || [ -f "$D/buildplan/CARD.md" ]; then
    F="$D/buildplan/CARD.md"
    [ -f "$D/buildplan/BRIEF.md" ] && F="$D/buildplan/BRIEF.md"
    LINE=$(grep -m1 '^Sequence: ' "$F" 2>/dev/null)
    STATUS=$(printf '%s' "$LINE" | sed -n 's/.*[Ss]tatus: *\([A-Za-z]*\).*/\1/p' | tr A-Z a-z)
    case "$STATUS" in
      planned|building)
        NOW=""
        [ -f "$D/PROGRESS.md" ] && NOW=$(awk '/^## Now/{f=1; print; next} f && /^## /{exit} f{print}' "$D/PROGRESS.md" 2>/dev/null)
        echo "A build is in progress here. Use Skill(sequence) to resume it."
        if [ "$SOURCE" = "compact" ] && [ "$D" = "$CWD" ]; then :
        elif [ "$F" = "$D/buildplan/CARD.md" ]; then
          echo "Lite sequence build open at $D. Read buildplan/CARD.md before acting: $LINE"
        elif printf '%s\n' "$NOW" | grep -q '^Sequence:'; then
          echo "Sequence build in progress at $D. Resume from this checkpoint; re-ask nothing a gate approved:"
          print_now "$NOW" "$D/PROGRESS.md"
        else
          echo "Sequence build open at $D ($LINE), with no \"Sequence:\" line in PROGRESS.md's \"## Now\". Read buildplan/ before acting."
        fi
        GATE=$(grep -i -m1 '^Gate .* status: *open' "$D/buildplan/GATE.md" 2>/dev/null)
        # A gate card left for the user while they were away: name it on every start, so it never waits unseen.
        [ -n "$GATE" ] && echo "A gate card is waiting for the user at $D/buildplan/GATE.md: $GATE. Show it to them before other build work."
        ;;
    esac
    break
  fi
  D=$(dirname "$D")
done

if [ "$SOURCE" = "compact" ]; then
  P="${CWD:-.}/PROGRESS.md"
  echo "Context was just compacted. Resume from the checkpoint below and re-check the live state before changing anything."
  if [ -f "$P" ]; then
    NOW=$(awk '/^## Now/{f=1; print; next} f && /^## /{exit} f{print}' "$P" 2>/dev/null)
    if [ -n "$NOW" ]; then echo "Checkpoint from $P:"; print_now "$NOW" "$P"
    else echo "$P has no \"## Now\" section; read the whole file before continuing."; fi
  else
    echo "No PROGRESS.md in $CWD. Rebuild the current step from the compaction summary, then write a checkpoint before going on."
  fi
fi
exit 0
