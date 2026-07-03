#!/usr/bin/env python3
"""Dictionary-based lookup for the Hanshou 1200-word IPA vocabulary
(hanshou-ipa-vocab.md).

This exists because "read the reference file and use good judgment" is not
a deterministic guarantee that a dialect response actually uses verified
words -- this script gives a small, checkable substitute: given a piece of
Mandarin text, segment it against the *actual* recorded vocabulary (forward
maximum matching, no external NLP dependency so it stays runnable in any
agent sandbox) and report which spans have a known Hanshou form.

Not a general-purpose segmenter -- only recognizes words that exist in the
table. Anything else is left as single characters, which is fine for our
purpose (checking specific words, not full linguistic parsing).
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

_TABLE_ROW_RE = re.compile(
    r"^\|\s*(\d{4})\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|$"
)


@dataclass(frozen=True)
class VocabEntry:
    num: str
    headword: str  # 词条: the Mandarin gloss used as the lookup key
    note: str  # 注例
    reading: str  # 读音: IPA + Chao tone value
    dialect_form: str  # 说法: what's actually said in Hanshou


def load_vocab(path: Path) -> dict[str, list[VocabEntry]]:
    """Parse hanshou-ipa-vocab.md's table into a {headword: [VocabEntry, ...]}
    dict. 45 of the 1200 headwords are genuinely polysemous (e.g. "叫" has
    separate entries for a dog barking / a rooster crowing / calling someone
    -- three different readings) -- keeping a list per headword instead of
    overwriting means none of those senses get silently dropped.
    """
    entries: dict[str, list[VocabEntry]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = _TABLE_ROW_RE.match(line.strip())
        if not m:
            continue
        num, headword, note, reading, dialect_form = m.groups()
        if not headword or headword == "词条":
            continue
        entries.setdefault(headword, []).append(
            VocabEntry(num, headword, note, reading, dialect_form)
        )
    return entries


@dataclass(frozen=True)
class Match:
    start: int
    end: int  # exclusive
    entries: tuple[VocabEntry, ...]  # >1 when the headword is polysemous


def segment(text: str, vocab: dict[str, list[VocabEntry]]) -> list[Match]:
    """Forward maximum matching: at each position, try the longest known
    headword first, then shorter ones, then advance by one character if
    nothing matches."""
    if not vocab:
        return []
    max_len = max(len(k) for k in vocab)
    matches: list[Match] = []
    i = 0
    n = len(text)
    while i < n:
        matched = False
        for length in range(min(max_len, n - i), 0, -1):
            candidate = text[i : i + length]
            candidate_entries = vocab.get(candidate)
            if candidate_entries is not None:
                matches.append(Match(i, i + length, tuple(candidate_entries)))
                i += length
                matched = True
                break
        if not matched:
            i += 1
    return matches


def annotate(text: str, vocab: dict[str, list[VocabEntry]]) -> str:
    """Human-readable report: which spans of `text` have a verified Hanshou
    form, and what it is (all senses, if the headword is polysemous)."""
    matches = segment(text, vocab)
    if not matches:
        return f"(没有在词表里查到任何词条: {text!r})"
    lines = [f"输入: {text}"]
    saw_loan_marker = False
    for m in matches:
        for e in m.entries:
            note = f"（{e.note}）" if e.note else ""
            if "=" in e.dialect_form:
                saw_loan_marker = True
            lines.append(
                f"  [{m.start}:{m.end}] {text[m.start:m.end]!r}{note} "
                f"-> 汉寿话说法「{e.dialect_form}」 读音 {e.reading} (编号{e.num})"
            )
    if saw_loan_marker:
        lines.append(
            "  注意：说法里带\"=\"的字是借音字标注，实际说话/打字时去掉\"=\"，"
            "只取汉字本身（例如「顽=」实际写作「顽」）。"
        )
    return "\n".join(lines)


def default_vocab_path() -> Path:
    return Path(__file__).resolve().parent.parent / "references" / "hanshou-ipa-vocab.md"


if __name__ == "__main__":
    vocab = load_vocab(default_vocab_path())
    args = sys.argv[1:]
    texts: Iterable[str] = args if args else [line.rstrip("\n") for line in sys.stdin]
    for text in texts:
        if text:
            print(annotate(text, vocab))
