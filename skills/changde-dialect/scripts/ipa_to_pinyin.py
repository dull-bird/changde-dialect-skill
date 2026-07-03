#!/usr/bin/env python3
"""Approximate-pinyin romanizer for the 语保工程 IPA + Chao-tone-value
transcriptions used in hanshou-ipa-vocab.md.

This is a readability aid, not a phonemic authority. It:
  - rewrites IPA segmental symbols as familiar pinyin-style letters
  - replaces Zhao Yuanren's five-level tone values (55/24/13/...) with a
    single-digit "tone-class" number, assigned by frequency in this word
    list -- NOT the same thing as Mandarin's tone 1-4, just a similarly
    shaped convention so it reads like pinyin-with-tone-numbers.

For the real pronunciation, always defer to hanshou-ipa-vocab.md (IPA + Chao
tone value). This module never modifies that file; it only derives a second,
friendlier column from it.
"""
from __future__ import annotations

import re

# Tone-class index, assigned by descending frequency across the 1200-word
# Hanshou list (13:421, 21:368, 55:326, 24:262, 33:196, 22:25, 14:1).
# 0 (neutral/light syllable) stays "0", same meaning as pinyin's toneless
# syllables (e.g. the "de" in "hao de").
TONE_MAP = {
    "13": "1",
    "21": "2",
    "55": "3",
    "24": "4",
    "33": "5",
    "22": "6",
    "14": "7",
    "0": "0",
}

# Zero-initial (Ǿ) + final -> pinyin y-/w-/plain spelling.
# Longest match first so e.g. "Ǿiɛn" is caught before the bare "Ǿi" rule.
_ZERO_INITIAL_RULES = [
    ("Ǿyan", "yuan"),
    ("Ǿye", "yue"),
    ("Ǿyn", "yun"),
    ("Ǿya", "yua"),
    ("Ǿy", "yu"),
    ("Ǿiɛn", "yan"),
    ("Ǿiaŋ", "yang"),
    ("Ǿiau", "yao"),
    ("Ǿiou", "you"),
    ("Ǿioŋ", "yong"),
    ("Ǿin", "yin"),
    ("Ǿie", "ye"),
    ("Ǿia", "ya"),
    ("Ǿio", "yo"),
    ("Ǿiɚ", "yer"),
    ("Ǿi", "yi"),
    ("Ǿuaŋ", "wang"),
    ("Ǿuai", "wai"),
    ("Ǿuan", "wan"),
    ("Ǿuei", "wei"),
    ("Ǿuən", "wen"),
    ("Ǿua", "wa"),
    ("Ǿuo", "wo"),
    ("Ǿu", "wu"),
    ("Ǿɚ", "er"),
    ("Ǿm", "m"),
    ("Ǿn", "n"),
]

# Onset consonant clusters, longest match first. "H" is a placeholder for
# aspiration so we don't collide with the later ɕ->X->h rewrite.
_ASPIRATED_RULES = [
    ("tɕh", "q"),
    ("tɕ", "j"),
    ("ʦh", "c"),
    ("ʦ", "z"),
    ("tsh", "c"),
    ("ts", "z"),
    ("th", "t*"),  # t* = placeholder for plain "t" (aspirated th -> unmarked t)
    ("kh", "k*"),
    ("ph", "p*"),
]
_BARE_STOP_RULES = [
    ("t", "d"),
    ("k", "g"),
    ("p", "b"),
]


def _convert_syllable(letters: str) -> str:
    s = letters

    for pat, rep in _ZERO_INITIAL_RULES:
        if s.startswith(pat):
            s = rep + s[len(pat) :]
            break
    else:
        if s.startswith("Ǿ"):
            s = s[1:]
        elif s.startswith("ƞ"):
            s = "ng" + s[1:]

    for pat, rep in _ASPIRATED_RULES:
        if s.startswith(pat):
            s = rep + s[len(pat) :]
            break
    else:
        for pat, rep in _BARE_STOP_RULES:
            if s.startswith(pat):
                s = rep + s[len(pat) :]
                break
    s = s.replace("t*", "t").replace("k*", "k").replace("p*", "p")

    # vowel / rime fixes, safe to apply anywhere in the remainder
    s = s.replace("iɛn", "ian")
    s = s.replace("ɛn", "en")
    s = s.replace("ɛ", "e")
    s = s.replace("ɚ", "er")
    s = s.replace("ə", "e")
    s = s.replace("ɿ", "i")
    s = s.replace("au", "ao")  # IPA /au/ diphthong -> pinyin spelling "ao"

    # ɕ (alveolo-palatal fricative, pinyin x) vs plain IPA x (velar fricative,
    # pinyin h) collide on the letter "x" -- convert ɕ via a placeholder first.
    s = s.replace("ɕ", "\0")
    s = s.replace("x", "h")
    s = s.replace("\0", "x")

    # ü spelled "u" after j/q/x per pinyin orthography (juan not jyan, etc.)
    for cons in ("j", "q", "x"):
        s = s.replace(cons + "y", cons + "u")

    s = s.replace("ŋ", "ng").replace("ƞ", "ng")

    return s


_SYLLABLE_RE = re.compile(r"([^\d\s]+)(\d+)")


def convert_reading(reading: str) -> str:
    """Convert one IPA+Chao-tone reading (possibly several space-separated
    alternatives, as stored in hanshou-ipa-vocab.md) to approximate pinyin.

    >>> convert_reading("thai24Ǿiaŋ0")
    'tai4yang0'
    """

    def repl(m: re.Match) -> str:
        letters, tone = m.group(1), m.group(2)
        pinyin_letters = _convert_syllable(letters)
        tone_class = TONE_MAP.get(tone, tone)
        return pinyin_letters + tone_class

    return _SYLLABLE_RE.sub(repl, reading)


if __name__ == "__main__":
    import sys

    for line in sys.stdin:
        line = line.rstrip("\n")
        if line:
            print(convert_reading(line))
