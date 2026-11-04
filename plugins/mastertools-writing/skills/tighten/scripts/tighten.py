#!/usr/bin/env python3
"""tighten.py -- objective clarity metrics + ledger logging for the `tighten` skill.

Two small jobs, kept deliberately narrow:

  metrics   compute countable clarity metrics on a piece of text
  log       append one row to the tighten-passes ledger (append-only, injection-safe)

Why this exists: the `tighten` skill scores every run against a rubric. Half that
rubric is countable (word count, sentence length, hedges, filler, em dashes,
banned words, reading grade). Those numbers must come from arithmetic, not the
model's gut, or re-runs drift instead of converge. This script does the counting.

What it does NOT do: judge whether an analogy lands, whether a line is quotable,
whether the voice survived. Those are human calls. The script only measures what
can be measured honestly. Anything approximate (passive voice, reading grade) is
labelled approximate in the output so nobody mistakes a heuristic for a fact.

Stdlib only. Python 3.8+.

Usage:
  python3 tighten.py metrics --file draft.txt            # JSON to stdout
  python3 tighten.py metrics --file draft.txt --pretty    # readable table
  cat draft.txt | python3 tighten.py metrics --stdin
  python3 tighten.py metrics --file draft.txt --banned banned.txt --max-sentence 30

  python3 tighten.py log --piece "welcome email" --pass-no 1 --profile email \
     --intensity medium --words-before 240 --words-after 150 \
     --grade-before 11.2 --grade-after 7.1 --score-before 4 --score-after 9 \
     --notes "first pass" [--ledger PATH]
"""

import argparse
import csv
import io
import os
import re
import statistics
import sys
from datetime import date

SCHEMA_VERSION = "tighten-1"

# --- Word lists -------------------------------------------------------------
# Conservative on purpose. Better to miss a soft hedge than to flag a word that
# was doing real work. The skill's Sharpen pass catches the rest by reading.

HEDGES = {
    "arguably", "perhaps", "possibly", "probably", "generally", "usually",
    "often", "sometimes", "somewhat", "fairly", "relatively", "essentially",
    "virtually", "roughly", "approximately", "seemingly", "presumably",
    "conceivably", "supposedly", "ostensibly", "mostly", "largely",
}
HEDGE_PHRASES = [
    r"\bi think\b", r"\bi believe\b", r"\bi feel like\b", r"\bin my opinion\b",
    r"\bin general\b", r"\bfor the most part\b", r"\bin many cases\b",
    r"\bto some extent\b", r"\bmore or less\b", r"\bkind of\b", r"\bsort of\b",
    r"\ba bit\b", r"\bit seems\b", r"\bit appears\b", r"\bmight be\b",
    r"\bcould be\b", r"\bmay be\b",
]
FILLERS = {
    "really", "very", "just", "actually", "basically", "literally", "simply",
    "totally", "absolutely", "definitely", "truly", "honestly", "obviously",
    "certainly", "quite", "rather", "somehow", "pretty",
}
FILLER_PHRASES = [r"\bin order to\b", r"\bthe fact that\b", r"\bneedless to say\b"]

BE_FORMS = {"is", "are", "was", "were", "be", "been", "being", "am"}
IRREGULAR_PP = {
    "done", "made", "seen", "known", "given", "taken", "written", "built",
    "held", "kept", "told", "shown", "found", "sent", "brought", "bought",
    "chosen", "driven", "broken", "spoken", "gotten", "run", "won", "left",
    "set", "put", "cut", "led", "read", "met", "paid", "said", "lost",
}


def _tokens(text):
    return re.findall(r"[A-Za-z']+", text.lower())


def _sentences(text):
    # Split on . ! ? followed by whitespace/end. Good enough for prose scoring;
    # abbreviations may over-split slightly and that is fine for a length metric.
    parts = re.split(r"(?<=[.!?])[\"')\]]?\s+", text.strip())
    return [p for p in (s.strip() for s in parts) if p]


def _paragraphs(text):
    parts = re.split(r"\n\s*\n", text.strip())
    return [p for p in (s.strip() for s in parts) if p]


def _syllables(word):
    word = re.sub(r"[^a-z]", "", word.lower())
    if not word:
        return 0
    groups = re.findall(r"[aeiouy]+", word)
    count = len(groups)
    if word.endswith("e") and not word.endswith(("le", "ie", "ee", "ye")):
        count -= 1
    return max(1, count)


def _load_banned(path):
    """Return (single_words, phrases). Single words match on token; phrases
    (anything with a space or hyphen) match on substring, which safely catches
    'game-changer', 'cutting-edge', 'dive deep', 'at the end of the day'."""
    words, phrases = set(), []
    if not path or not os.path.exists(path):
        return words, phrases
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip().lower()
            if not line or line.startswith("#"):
                continue
            if " " in line or "-" in line:
                phrases.append(line)
            else:
                words.add(line)
    return words, phrases


def compute_metrics(text, banned=None, max_sentence=30):
    banned_words, banned_phrases = banned if banned else (set(), [])
    toks = _tokens(text)
    sents = _sentences(text)
    paras = _paragraphs(text)
    low = text.lower()

    n_words = len(toks)
    n_sents = max(1, len(sents))
    sent_lens = [len(_tokens(s)) for s in sents] or [0]

    total_syl = sum(_syllables(w) for w in toks) or 1
    # Flesch-Kincaid grade level (approximate; heuristic syllable count).
    fk_grade = 0.39 * (n_words / n_sents) + 11.8 * (total_syl / max(1, n_words)) - 15.59

    hedge_hits = [t for t in toks if t in HEDGES]
    for pat in HEDGE_PHRASES:
        hedge_hits += re.findall(pat, low)
    filler_hits = [t for t in toks if t in FILLERS]
    for pat in FILLER_PHRASES:
        filler_hits += re.findall(pat, low)

    # Passive heuristic (APPROXIMATE): a be-form within 3 tokens of an -ed word
    # or a known irregular past participle.
    passive = 0
    for i, t in enumerate(toks):
        if t in BE_FORMS:
            window = toks[i + 1:i + 4]
            if any(w.endswith("ed") or w in IRREGULAR_PP for w in window):
                passive += 1

    em_total = text.count("\u2014")
    em_per_para = [p.count("\u2014") for p in paras] or [0]

    banned_hits = {t for t in toks if t in banned_words}
    for ph in banned_phrases:
        if ph in low:
            banned_hits.add(ph)
    banned_hits = sorted(banned_hits)

    return {
        "words": n_words,
        "sentences": len(sents),
        "paragraphs": len(paras),
        "avg_sentence_len": round(statistics.mean(sent_lens), 1),
        "max_sentence_len": max(sent_lens),
        "sentence_len_stdev": round(statistics.pstdev(sent_lens), 1) if len(sent_lens) > 1 else 0.0,
        "long_sentences_over_%d" % max_sentence: sum(1 for L in sent_lens if L > max_sentence),
        "reading_grade_fk_approx": round(fk_grade, 1),
        "hedges": len(hedge_hits),
        "hedge_hits": sorted(set(hedge_hits)),
        "fillers": len(filler_hits),
        "filler_hits": sorted(set(filler_hits)),
        "passive_approx": passive,
        "em_dashes_total": em_total,
        "em_dashes_max_per_paragraph": max(em_per_para),
        "banned_hits": banned_hits,
        "banned_count": len(banned_hits),
    }


def _pretty(m):
    order = [
        ("words", "words"),
        ("sentences", "sentences"),
        ("paragraphs", "paragraphs"),
        ("avg_sentence_len", "avg sentence length (words)"),
        ("max_sentence_len", "longest sentence (words)"),
        ("sentence_len_stdev", "sentence-length variance (higher = more rhythm)"),
        ("reading_grade_fk_approx", "reading grade  [approx]"),
        ("hedges", "hedges"),
        ("fillers", "filler words"),
        ("passive_approx", "passive constructions  [approx]"),
        ("em_dashes_total", "em dashes (total)"),
        ("em_dashes_max_per_paragraph", "em dashes (worst paragraph)"),
        ("banned_count", "banned-word hits"),
    ]
    lines = ["clarity metrics", "-" * 44]
    for key, label in order:
        val = m.get(key)
        lines.append("  %-42s %s" % (label, val))
    if m.get("hedge_hits"):
        lines.append("  hedges found: " + ", ".join(m["hedge_hits"]))
    if m.get("filler_hits"):
        lines.append("  filler found: " + ", ".join(m["filler_hits"]))
    if m.get("banned_hits"):
        lines.append("  banned found: " + ", ".join(m["banned_hits"]))
    return "\n".join(lines)


# --- Ledger -----------------------------------------------------------------

LEDGER_HEADER = [
    "date", "user", "piece", "pass_no", "profile", "intensity",
    "words_before", "words_after", "grade_before", "grade_after",
    "score_before", "score_after", "frozen", "needs", "notes", "schema_version",
]


def _sanitize(value):
    # Stop a CSV cell from executing as a formula in Excel/Sheets.
    s = "" if value is None else str(value)
    if s and s[0] in ("=", "+", "-", "@"):
        return "'" + s
    return s


def ledger_path(cli_path):
    return cli_path or os.environ.get("TIGHTEN_LEDGER") or os.path.join(".ledger", "tighten-passes.csv")


def log_row(args):
    path = ledger_path(args.ledger)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    exists = os.path.exists(path)
    row = {
        "date": date.today().isoformat(),
        "user": _sanitize(args.user),
        "piece": _sanitize(args.piece),
        "pass_no": args.pass_no,
        "profile": _sanitize(args.profile),
        "intensity": _sanitize(args.intensity),
        "words_before": args.words_before if args.words_before is not None else "",
        "words_after": args.words_after if args.words_after is not None else "",
        "grade_before": args.grade_before if args.grade_before is not None else "",
        "grade_after": args.grade_after if args.grade_after is not None else "",
        "score_before": args.score_before if args.score_before is not None else "",
        "score_after": args.score_after if args.score_after is not None else "",
        "frozen": _sanitize(args.frozen),
        "needs": _sanitize(args.needs),
        "notes": _sanitize(args.notes),
        "schema_version": SCHEMA_VERSION,
    }
    with open(path, "a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=LEDGER_HEADER)
        if not exists:
            writer.writeheader()
        writer.writerow(row)
    print("[tighten] logged pass %s of '%s' -> %s" % (args.pass_no, args.piece, path))


def init_ledger(args):
    path = ledger_path(args.ledger)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    if os.path.exists(path):
        print("[tighten] ledger already exists: %s" % path)
        return
    with open(path, "w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerow(LEDGER_HEADER)
    print("[tighten] created ledger: %s" % path)


# --- CLI --------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="Objective clarity metrics + ledger for the tighten skill.")
    sub = p.add_subparsers(dest="cmd", required=True)

    m = sub.add_parser("metrics", help="compute clarity metrics on text")
    src = m.add_mutually_exclusive_group(required=True)
    src.add_argument("--file", help="path to a text file")
    src.add_argument("--stdin", action="store_true", help="read text from stdin")
    m.add_argument("--banned", help="path to a banned-words file (one per line)")
    m.add_argument("--max-sentence", type=int, default=30, help="long-sentence threshold in words")
    m.add_argument("--pretty", action="store_true", help="readable table instead of JSON")

    lg = sub.add_parser("log", help="append a row to the tighten-passes ledger")
    lg.add_argument("--ledger", help="ledger path (default .ledger/tighten-passes.csv or $TIGHTEN_LEDGER)")
    lg.add_argument("--user", default="")
    lg.add_argument("--piece", required=True)
    lg.add_argument("--pass-no", required=True)
    lg.add_argument("--profile", default="")
    lg.add_argument("--intensity", default="")
    lg.add_argument("--words-before", type=int)
    lg.add_argument("--words-after", type=int)
    lg.add_argument("--grade-before", type=float)
    lg.add_argument("--grade-after", type=float)
    lg.add_argument("--score-before", type=int)
    lg.add_argument("--score-after", type=int)
    lg.add_argument("--frozen", default="")
    lg.add_argument("--needs", default="")
    lg.add_argument("--notes", default="")

    it = sub.add_parser("init", help="create an empty ledger with header")
    it.add_argument("--ledger", help="ledger path")

    args = p.parse_args()

    if args.cmd == "metrics":
        if args.stdin:
            text = sys.stdin.read()
        else:
            with open(args.file, "r", encoding="utf-8") as fh:
                text = fh.read()
        banned = _load_banned(args.banned)
        m = compute_metrics(text, banned=banned, max_sentence=args.max_sentence)
        if args.pretty:
            print(_pretty(m))
        else:
            import json
            print(json.dumps(m, indent=2))
    elif args.cmd == "log":
        log_row(args)
    elif args.cmd == "init":
        init_ledger(args)


if __name__ == "__main__":
    main()
