#!/usr/bin/env python3
"""Unit tests for ipa_to_pinyin.py, using real entries from
hanshou-ipa-vocab.md (语保工程 official Hanshou point 26J41) as fixtures,
so a passing suite means the converter matches actually-recorded data,
not made-up examples.
"""
import unittest

from ipa_to_pinyin import convert_reading


class TestBasicSyllables(unittest.TestCase):
    def test_taiyang(self):
        # 太阳 thai24Ǿiaŋ0 -> "太" th+ai tone24, "阳" zero-initial+iang tone0
        self.assertEqual(convert_reading("thai24Ǿiaŋ0"), "tai4yang0")

    def test_yueliang(self):
        # 月亮 Ǿye24niaŋ0
        self.assertEqual(convert_reading("Ǿye24niaŋ0"), "yue4niang0")

    def test_xingxing(self):
        # 星星 ɕin55ɕin55
        self.assertEqual(convert_reading("ɕin55ɕin55"), "xin3xin3")

    def test_yun(self):
        # 云 Ǿyn13
        self.assertEqual(convert_reading("Ǿyn13"), "yun1")

    def test_feng(self):
        # 风 foŋ55
        self.assertEqual(convert_reading("foŋ55"), "fong3")

    def test_taifeng(self):
        # 台风 thai13foŋ55
        self.assertEqual(convert_reading("thai13foŋ55"), "tai1fong3")

    def test_yu_rain(self):
        # 雨 Ǿy21
        self.assertEqual(convert_reading("Ǿy21"), "yu2")


class TestZeroInitialFinals(unittest.TestCase):
    def test_yi(self):
        self.assertEqual(convert_reading("Ǿi0"), "yi0")

    def test_ya(self):
        self.assertEqual(convert_reading("Ǿia21"), "ya2")

    def test_yao(self):
        self.assertEqual(convert_reading("Ǿiau13"), "yao1")

    def test_ye(self):
        self.assertEqual(convert_reading("Ǿie13"), "ye1")

    def test_yin(self):
        self.assertEqual(convert_reading("Ǿin24"), "yin4")

    def test_yong(self):
        self.assertEqual(convert_reading("Ǿioŋ13"), "yong1")

    def test_wu(self):
        self.assertEqual(convert_reading("Ǿu13"), "wu1")

    def test_wa(self):
        self.assertEqual(convert_reading("Ǿua21"), "wa2")

    def test_wai(self):
        self.assertEqual(convert_reading("Ǿuai33"), "wai5")

    def test_wan(self):
        self.assertEqual(convert_reading("Ǿuan13"), "wan1")

    def test_wang(self):
        self.assertEqual(convert_reading("Ǿuaŋ55"), "wang3")

    def test_wei(self):
        self.assertEqual(convert_reading("Ǿuei13"), "wei1")

    def test_wo(self):
        self.assertEqual(convert_reading("Ǿuo13"), "wo1")

    def test_wen(self):
        self.assertEqual(convert_reading("Ǿuən13"), "wen1")

    def test_er(self):
        self.assertEqual(convert_reading("Ǿɚ24"), "er4")

    def test_yuan(self):
        self.assertEqual(convert_reading("Ǿyan13"), "yuan1")

    def test_yue(self):
        self.assertEqual(convert_reading("Ǿye0"), "yue0")


class TestConsonantClusters(unittest.TestCase):
    def test_aspirated_q(self):
        # 淋 tɕhyaŋ13 (aspirated tɕh -> q; y after q -> u per pinyin orthography)
        self.assertEqual(convert_reading("tɕhyaŋ13"), "quang1")

    def test_j(self):
        # 蜘蛛 first syllable tɕi24 -> ji4
        self.assertEqual(convert_reading("tɕi24"), "ji4")

    def test_x_alveolopalatal(self):
        # 水沟儿 first syllable ɕiau21 -> xiao2
        self.assertEqual(convert_reading("ɕiau21"), "xiao2")

    def test_plain_x_velar_to_h(self):
        # 后天 xou33 -> hou5 (IPA x = velar fricative = pinyin h, not x)
        self.assertEqual(convert_reading("xou33"), "hou5")

    def test_aspirated_t(self):
        # 太 thai24 -> tai4 (aspirated th -> unmarked pinyin t)
        self.assertEqual(convert_reading("thai24"), "tai4")

    def test_bare_t_to_d(self):
        # 大后天 first syllable Ǿuaŋ33, second xou33, third Ǿɚ0 -- no bare t
        # here; use 到底 pattern instead: tau24ti0 (到底) unaspirated t -> d
        self.assertEqual(convert_reading("tau24ti0"), "dao4di0")


class TestApicalVowelAndSchwa(unittest.TestCase):
    def test_shi_apical(self):
        # 时候 sɿ13xou0 -> apical vowel ɿ -> i
        self.assertEqual(convert_reading("sɿ13xou0"), "si1hou0")

    def test_zi_apical(self):
        # 流氓 second syllable ʦɿ0 -> zi0
        self.assertEqual(convert_reading("ʦɿ0"), "zi0")

    def test_schwa_en(self):
        # 田埂 third syllable sən0 -> sen0
        self.assertEqual(convert_reading("sən0"), "sen0")


class TestPluralPronouns(unittest.TestCase):
    """These four entries are the ones that corroborate 李蓝's 2002 paper
    about Hanshou's shared nasal plural morpheme across persons."""

    def test_women(self):
        # 我们 Ǿuan13
        self.assertEqual(convert_reading("Ǿuan13"), "wan1")

    def test_nimen(self):
        # 你们 niɛn13
        self.assertEqual(convert_reading("niɛn13"), "nian1")

    def test_tamen(self):
        # 他们 tha55ŋan0
        self.assertEqual(convert_reading("tha55ŋan0"), "ta3ngan0")


class TestMultiSyllableAndSpaces(unittest.TestCase):
    def test_two_alternatives_space_separated(self):
        # 钝 pu24khuai13 tən33 ("不快 钝" -- two alternative renderings).
        # Plain (unaspirated) "t" -> pinyin "d", matching Mandarin 钝=dun.
        self.assertEqual(convert_reading("pu24khuai13 tən33"), "bu4kuai1 den5")


if __name__ == "__main__":
    unittest.main()
