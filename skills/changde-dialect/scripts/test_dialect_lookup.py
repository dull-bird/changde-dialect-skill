#!/usr/bin/env python3
import tempfile
import unittest
from pathlib import Path

from dialect_lookup import Match, VocabEntry, default_vocab_path, load_vocab, segment


FIXTURE_TABLE = """# fixture

| 编号 | 词条 | 注例 | 读音 | 说法 |
|---|---|---|---|---|
| 0001 | 太阳 | ～下山了 | thai24Ǿiaŋ0 | 太阳 |
| 0002 | 我们 | 不包括听话人 | Ǿuan13 | 顽= |
| 0003 | 你们 |  | niɛn13 | 你安= |
| 0998 | 干净 | 衣服～ | so24ni0 | 索=里= |
"""


class TestLoadVocab(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False, encoding="utf-8"
        )
        self.tmp.write(FIXTURE_TABLE)
        self.tmp.close()
        self.path = Path(self.tmp.name)

    def tearDown(self):
        self.path.unlink(missing_ok=True)

    def test_parses_all_rows(self):
        vocab = load_vocab(self.path)
        self.assertEqual(len(vocab), 4)
        self.assertIn("太阳", vocab)
        self.assertIn("我们", vocab)

    def test_entry_fields(self):
        vocab = load_vocab(self.path)
        e = vocab["太阳"][0]
        self.assertEqual(e.num, "0001")
        self.assertEqual(e.reading, "thai24Ǿiaŋ0")
        self.assertEqual(e.dialect_form, "太阳")

    def test_single_sense_headword_has_one_entry(self):
        vocab = load_vocab(self.path)
        self.assertEqual(len(vocab["太阳"]), 1)

    def test_header_row_not_included(self):
        vocab = load_vocab(self.path)
        self.assertNotIn("词条", vocab)


class TestSegment(unittest.TestCase):
    def setUp(self):
        self.vocab = {
            "太阳": [VocabEntry("0001", "太阳", "", "thai24Ǿiaŋ0", "太阳")],
            "我们": [VocabEntry("0002", "我们", "", "Ǿuan13", "顽=")],
            "你们": [VocabEntry("0003", "你们", "", "niɛn13", "你安=")],
        }

    def test_single_match(self):
        matches = segment("太阳出来了", self.vocab)
        self.assertEqual(matches, [Match(0, 2, tuple(self.vocab["太阳"]))])

    def test_match_in_middle_of_sentence(self):
        text = "我们去看太阳"
        matches = segment(text, self.vocab)
        self.assertEqual(len(matches), 2)
        self.assertEqual((matches[0].start, matches[0].end), (0, 2))
        self.assertEqual(text[matches[0].start : matches[0].end], "我们")
        self.assertEqual((matches[1].start, matches[1].end), (4, 6))
        self.assertEqual(text[matches[1].start : matches[1].end], "太阳")

    def test_no_match(self):
        self.assertEqual(segment("今天天气不错", self.vocab), [])

    def test_longest_match_preferred(self):
        # "你们" (2 chars) must win over any hypothetical single-char "你"
        # entry, proving forward-maximum-matching (not first-match) behavior.
        vocab = dict(self.vocab)
        vocab["你"] = [VocabEntry("9999", "你", "", "ni21", "你")]
        matches = segment("你们好", vocab)
        self.assertEqual(matches[0].entries[0].headword, "你们")

    def test_polysemous_headword_keeps_all_senses(self):
        vocab = dict(self.vocab)
        vocab["叫"] = [
            VocabEntry("0280", "叫", "狗～", "Ǿuaŋ55", "汪="),
            VocabEntry("0285", "叫", "公鸡～", "tɕiau13", "叫"),
            VocabEntry("0920", "叫", "～他一声儿", "xan21", "喊"),
        ]
        matches = segment("叫", vocab)
        self.assertEqual(len(matches[0].entries), 3)


class TestRealFileSmoke(unittest.TestCase):
    """Sanity check against the actual shipped hanshou-ipa-vocab.md, so a
    broken file (bad table formatting, wrong path, etc.) fails the suite
    instead of failing silently at runtime."""

    def test_real_file_loads_all_nonblank_rows(self):
        path = default_vocab_path()
        self.assertTrue(path.exists(), f"expected vocab file at {path}")
        vocab = load_vocab(path)
        total_rows = sum(len(v) for v in vocab.values())
        # 1200 numbered slots, but 0164/0172/0321 are blank in the official
        # source itself (informant didn't provide those 3 words) -- 1197
        # real rows is correct, not a parsing bug. See hanshou-ipa-vocab.md.
        self.assertEqual(total_rows, 1197)
        # 45 headwords are genuinely polysemous (multiple senses/readings),
        # so distinct-headword count is less than the row count -- both
        # numbers are asserted so a regression in either direction fails.
        self.assertEqual(len(vocab), 1142)

    def test_known_word_present(self):
        vocab = load_vocab(default_vocab_path())
        self.assertIn("太阳", vocab)
        self.assertEqual(vocab["太阳"][0].dialect_form, "太阳")

    def test_polysemous_word_keeps_multiple_senses(self):
        vocab = load_vocab(default_vocab_path())
        self.assertIn("叫", vocab)
        self.assertGreaterEqual(len(vocab["叫"]), 3)

    def test_segments_a_real_sentence(self):
        vocab = load_vocab(default_vocab_path())
        matches = segment("我们明天去看太阳", vocab)
        headwords = [e.headword for m in matches for e in m.entries]
        self.assertIn("我们", headwords)
        self.assertIn("太阳", headwords)


if __name__ == "__main__":
    unittest.main()
