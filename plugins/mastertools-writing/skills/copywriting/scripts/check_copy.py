#!/usr/bin/env python3
"""Mechanical copy checker for the copywriting skill.

Flags banned words, AI-sounding patterns, ad-speak, passive voice, weak rhythm
and reading level. It cannot judge whether copy is good; it catches what good
copy never contains.

Usage:
  python check_copy.py draft.md                # human-readable report
  python check_copy.py draft.md --mode brand   # brand work: no reading-grade limit
  cat draft.md | python check_copy.py -        # read from stdin
  python check_copy.py draft.md --json         # machine-readable
  python check_copy.py hours.md --allow-days   # weekdays that are real schedule facts
  python check_copy.py ui.md --allow-address   # microcopy / transactional email may address the reader

Exit code 1 if any FAIL, else 0.
"""
import argparse
import json
import re
import statistics
import sys

# ---- word lists -------------------------------------------------------------
HYPE = [
    "world-class", "best-in-class", "cutting-edge", "state-of-the-art",
    "industry-leading", "revolutionary", "game-changing", "game changer",
    "next-generation", "next-gen", "unparalleled", "unmatched", "second to none",
    "best-of-breed", "innovative", "disruptive",
]
CORPORATE = [
    "solutions", "synergy", "synergies", "leverage", "leveraging", "seamless",
    "seamlessly", "robust", "holistic", "empower", "empowering", "empowers",
    "streamline", "streamlined", "utilize", "utilise", "facilitate",
    "best practices", "value-add", "one-stop shop", "turnkey",
]
AI_VOCAB = [
    "delve", "delves", "delving", "tapestry", "testament", "pivotal",
    "underscore", "underscores", "foster", "fosters", "vibrant", "intricate",
    "showcase", "showcases", "elevate", "elevates", "elevated", "unlock",
    "unlocks", "unleash", "unleashes", "embark", "realm", "landscape",
    "navigate the", "boasts", "meticulous", "meticulously", "transformative",
    "ever-evolving", "ever-changing", "in the heart of", "nestled",
    "a symphony of", "harness", "harnessing", "resonate", "resonates",
]
AD_SPEAK = [
    "look no further", "we've got you covered", "we have you covered",
    "take it to the next level", "to the next level", "like never before",
    "quality you can trust", "peace of mind", "one-stop", "introducing the all-new",
    "in today's fast-paced world", "in today's world", "imagine a world",
    "we're excited to announce", "we are excited to announce",
    "we're thrilled", "we are thrilled", "we're passionate about",
    "we are passionate about", "at the end of the day", "it's no secret",
    "whether you're", "your journey", "the perfect blend",
]
CHATBOT = [
    "certainly!", "i hope this helps", "let me know if", "great question",
    "as an ai", "here's a", "here is a", "in summary", "in conclusion",
    "ultimately,", "overall,",
]
WEEKDAYS = r"\b(?:mon|tues|wednes|thurs|fri|satur|sun)days?\b"
# Named events and proper nouns are not the cliche.
WEEKDAY_EVENTS = r"\b(?:black|good|cyber|super|giving|small business|boxing|easter|palm|ash|holy)\s+(?:mon|tues|wednes|thurs|fri|satur|sun)day\b"
WEAK_CTA = [r"\bsubmit\b", r"\bclick here\b", r"\blearn more\b"]

# ---- helpers ----------------------------------------------------------------
VOWELS = "aeiouy"


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    count, prev = 0, False
    for ch in w:
        v = ch in VOWELS
        if v and not prev:
            count += 1
        prev = v
    if w.endswith("e") and count > 1 and not w.endswith("le"):
        count -= 1
    return max(count, 1)


def strip_markup(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"^#+\s.*$", " ", text, flags=re.M)          # headings
    text = re.sub(r"^\s*(RECOMMENDED|ALTERNATES|ASSUMPTIONS.*|Why:.*)$", " ",
                  text, flags=re.M | re.I)
    text = re.sub(r"[*_`>|]", " ", text)
    return text


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if len(re.findall(r"[A-Za-z']+", p)) >= 2]


def find_terms(text_lower, terms):
    hits = []
    for t in terms:
        pat = r"(?<![a-z])" + re.escape(t) + r"(?![a-z])"
        n = len(re.findall(pat, text_lower))
        if n:
            hits.append(f"{t} x{n}" if n > 1 else t)
    return hits


# ---- checks -----------------------------------------------------------------
def check(text, mode="conversion", allow_days=False, allow_address=False):
    results = []  # (level, name, detail)
    raw_lower = text.lower()
    clean = strip_markup(text)
    low = clean.lower()

    for name, terms in [("Hype words", HYPE), ("Corporate filler", CORPORATE),
                        ("AI vocabulary", AI_VOCAB), ("Ad-speak", AD_SPEAK)]:
        hits = find_terms(low, terms)
        if hits:
            results.append(("FAIL", name, ", ".join(hits)))

    if not allow_days:
        day_text = re.sub(WEEKDAY_EVENTS, " ", low)
        days = re.findall(WEEKDAYS, day_text)
        if days:
            results.append(("FAIL", "Day of the week",
                            ", ".join(sorted(set(days))) + " - banned as color; use the real detail "
                            "(rerun with --allow-days only if it is a schedule fact like opening hours)"))

    hits = find_terms(raw_lower, CHATBOT)
    if hits:
        results.append(("FAIL", "Chatbot residue", ", ".join(hits)))

    neg = re.findall(r"\b(?:it'?s|is|isn'?t|aren'?t|not)\s+(?:just|only|merely)\b[^.!?\n]{0,60}[.,;:-]+\s*(?:it'?s|they'?re|this is|but)\b",
                     low)
    if neg:
        results.append(("WARN", "'Not just X, it's Y' construction",
                        f"{len(neg)} found - use only if it IS the idea"))

    triads = re.findall(r"\b([a-z]+), ([a-z]+),? and ([a-z]+)\b", low)
    adj_like = [t for t in triads if all(len(w) > 3 for w in t)]
    if len(adj_like) >= 2:
        results.append(("WARN", "Reflexive threes",
                        f"{len(adj_like)} lists of three, e.g. '{', '.join(adj_like[0])}'"))

    words = re.findall(r"[A-Za-z']+", clean)
    nwords = max(len(words), 1)
    dashes = clean.count("—") + len(re.findall(r"\s--\s", clean))
    if dashes and dashes / nwords * 100 > 1.0:
        results.append(("WARN", "Em-dash density", f"{dashes} in {nwords} words"))

    excl = clean.count("!")
    if excl > 1:
        results.append(("WARN", "Exclamation marks", f"{excl} - energy should come from the words"))

    passive = re.findall(r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?\w+ed\b(?:\s+by\b)?", low)
    passive_by = [p for p in passive if p.endswith(" by")]
    if passive_by:
        results.append(("WARN", "Passive voice", f"{len(passive_by)} 'was X-ed by' constructions"))

    for pat in WEAK_CTA:
        if re.search(pat, low):
            results.append(("WARN", "Weak CTA", f"'{pat.strip(chr(92) + 'b')}' - name the outcome instead"))

    if not allow_address:
        # House style: no first person singular, no second person. Quoted speech is skipped (proof, not voice).
        unquoted = re.sub(r'"[^"\n]*"|\u201c[^\u201d\n]*\u201d', " ", clean)
        first = re.findall(r"\b(?:I|I'm|I've|I'll|I'd|me|my|mine|myself)\b", unquoted)
        second = re.findall(r"\b(?:you|your|you're|you've|you'll|you'd|yours|yourself|yourselves)\b", unquoted, re.I)
        if first:
            results.append(("FAIL", "First person", ", ".join(sorted(set(first))) +
                            " - house style: no I/me/my in ad copy"))
        if second:
            results.append(("FAIL", "Direct address", ", ".join(sorted(set(w.lower() for w in second))) +
                            " - house style: evoke, don't call the viewer out "
                            "(rerun with --allow-address for microcopy or transactional email)"))

    sents = sentences(clean)
    lens = [len(re.findall(r"[A-Za-z']+", s)) for s in sents]
    if len(lens) >= 6:
        sd = statistics.pstdev(lens)
        if sd < 3.0:
            results.append(("WARN", "Monotone rhythm",
                            f"sentence lengths barely vary (sd {sd:.1f}); mix short and long"))
        long_ones = [l for l in lens if l > 30]
        if long_ones:
            results.append(("WARN", "Very long sentences", f"{len(long_ones)} over 30 words"))

    grade = None
    if sents and nwords >= 40:
        syl = sum(syllables(w) for w in words)
        grade = 0.39 * (nwords / len(sents)) + 11.8 * (syl / nwords) - 15.59
        if mode == "conversion" and grade > 9:
            results.append(("WARN", "Reading level",
                            f"grade {grade:.1f}; conversion copy aims for about 5-7"))

    return {
        "words": nwords,
        "sentences": len(sents),
        "reading_grade": round(grade, 1) if grade is not None else None,
        "fails": sum(1 for r in results if r[0] == "FAIL"),
        "warns": sum(1 for r in results if r[0] == "WARN"),
        "results": [{"level": a, "check": b, "detail": c} for a, b, c in results],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("path", help="file to check, or - for stdin")
    ap.add_argument("--mode", choices=["conversion", "brand", "ux"], default="conversion")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--allow-address", action="store_true",
                    help="permit I/you in UX microcopy, transactional emails and instructions")
    ap.add_argument("--allow-days", action="store_true",
                    help="permit weekday names that are real schedule facts (opening hours, delivery days)")
    a = ap.parse_args()
    text = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    rep = check(text, a.mode, a.allow_days, a.allow_address)
    if a.json:
        print(json.dumps(rep, indent=2))
    else:
        g = rep["reading_grade"]
        print(f"{rep['words']} words, {rep['sentences']} sentences"
              + (f", reading grade {g}" if g is not None else ""))
        if not rep["results"]:
            print("PASS: no mechanical problems found. Now judge it by the rubric.")
        for r in rep["results"]:
            print(f"{r['level']:4}  {r['check']}: {r['detail']}")
    sys.exit(1 if rep["fails"] else 0)


if __name__ == "__main__":
    main()
