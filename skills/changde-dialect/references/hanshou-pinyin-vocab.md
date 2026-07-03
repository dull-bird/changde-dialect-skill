# 汉寿话（龙阳话）近似拼音词汇表 —— 由 hanshou-ipa-vocab.md 自动转换

> 这份文件是 `hanshou-ipa-vocab.md`（语保工程官方 1200 词 IPA 表）的派生版本，用 `../scripts/ipa_to_pinyin.py` 自动转换生成，**不是独立的第二手数据**——原始 IPA 才是权威来源，这里只是把国际音标和赵元任调值换成更好读的拼音式拼写，方便不熟悉 IPA 的人快速上手。转换脚本配了 50 条单元测试（`scripts/test_ipa_to_pinyin.py`），逐一核对过真实词条。

## 怎么读这份表

- 声母/韵母已经换成拼音字母（q/j/x/zh/z/c/s/b/d/g/y/w 等），照拼音习惯读就行。
- 每个音节后面的数字不是拼音的四声，是这份表**自定义的调类编号**：按这1200词里出现频率从高到低分成 1-7 号（1=13调值，2=21，3=55，4=24，5=33，6=22，7=14），`0`=轻声，跟普通话的四个声调不是一回事，只是借用"字母+数字"这种眼熟的格式。要知道准确调值，回 `hanshou-ipa-vocab.md` 查原始 IPA。
- 例：太阳＝IPA `thai24Ǿiaŋ0` → 近似拼音 `tai4yang0`（"太"调类4，"阳"轻声）。

## 完整词表（1200 条，其中 0164/0172/0321 三条官方原始数据本身为空）

| 编号 | 词条 | 注例 | 近似拼音 | 原始IPA | 说法 |
|---|---|---|---|---|---|
| 0001 | 太阳 | ～下山了 | tai4yang0 | thai24Ǿiaŋ0 | 太阳 |
| 0002 | 月亮 | ～出来了 | yue4niang0 | Ǿye24niaŋ0 | 月亮 |
| 0003 | 星星 |  | xin3xin3 | ɕin55ɕin55 | 星星 |
| 0004 | 云 |  | yun1 | Ǿyn13 | 云 |
| 0005 | 风 |  | fong3 | foŋ55 | 风 |
| 0006 | 台风 |  | tai1fong3 | thai13foŋ55 | 台风 |
| 0007 | 闪电 | 名词 | san2 | san21 | 闪 |
| 0008 | 雷 |  | nei1 | nei13 | 雷 |
| 0009 | 雨 |  | yu2 | Ǿy21 | 雨 |
| 0010 | 下雨 |  | nuo4yu2 | nuo24Ǿy21 | 落雨 |
| 0011 | 淋 | 衣服被雨～湿了 | quang1 | tɕhyaŋ13 | #2 |
| 0012 | 晒 | ～粮食 | sai1 | sai13 | 晒 |
| 0013 | 雪 |  | xie4 | ɕie24 | 雪 |
| 0014 | 冰 |  | bin3 | pin55 | 冰 |
| 0015 | 冰雹 |  | bin3bao0 | pin55pau0 | 冰雹 |
| 0016 | 霜 |  | xuang3 | ɕyaŋ55 | 霜 |
| 0017 | 雾 |  | wu5 | Ǿu33 | 雾 |
| 0018 | 露 |  | nou5xuei2 | nou33ɕyei21 | 露水 |
| 0019 | 虹 | 统称 | ma2yun0 | ma21Ǿyn0 | 马=云 |
| 0020 | 日食 |  | er4si4 | Ǿɚ24sɿ24 | 日食 |
| 0021 | 月食 |  | yue4si4 | Ǿye24sɿ24 | 月食 |
| 0022 | 天气 |  | tian3si0 | thiɛn55sɿ0 | 天势 |
| 0023 | 晴 | 天～ | qin1 | tɕhin13 | 晴 |
| 0024 | 阴 | 天～ | yin3 | Ǿin55 | 阴 |
| 0025 | 旱 | 天～ | gan3 | kan55 | 干 |
| 0026 | 涝 | 天～ | nao1 | nau13 | 涝 |
| 0027 | 天亮 |  | tian3niang0 | thiɛn55niaŋ0 | 天亮 |
| 0028 | 水田 |  | tian1 | thiɛn13 | 田 |
| 0029 | 旱地 | 浇不上水的耕地 | di5 | ti33 | 地 |
| 0030 | 田埂 |  | tian1yan2sen0 | thiɛn13Ǿiɛn21sən0 | 田掩=塍 |
| 0031 | 路 | 野外的 | nou5 | nou33 | 路 |
| 0032 | 山 |  | san3 | san55 | 山 |
| 0033 | 山谷 |  | san3gu4 | san55ku24 | 山谷 |
| 0034 | 江 | 大的河 | jiang3 | tɕiaŋ55 | 江 |
| 0035 | 溪 | 小的河 | qi3 | tɕhi55 | 溪 |
| 0036 | 水沟儿 | 较小的水道 | xiao2gou3er0 | ɕiau21kou55Ǿɚ0 | 小沟儿 |
| 0037 | 湖 |  | hu1 | xu13 | 湖 |
| 0038 | 池塘 |  | tang1 tang1nger0 | thaŋ13 thaŋ13ŋɚ0 | 塘 塘儿 |
| 0039 | 水坑儿 | 地面上有积水的小洼儿 | xuei2ken3 | ɕyei21khən55 | 水坑 |
| 0040 | 洪水 |  | dai5xuei2 | tai33ɕyei21 | 大水 |
| 0041 | 淹 | 被水～了 | wen1 | Ǿuən13 | 文= |
| 0042 | 河岸 |  | ngan5 | ŋan33 | 岸 |
| 0043 | 坝 | 拦河修筑拦水的 | ti1 | thi13 | 堤 |
| 0044 | 地震 |  | di5zen2 | ti33tsən21 | 地震 |
| 0045 | 窟窿 | 小的 | ngan2 | ŋan21 | 眼 |
| 0046 | 缝儿 | 统称 | fong5 | foŋ33 | 缝 |
| 0047 | 石头 | 统称 | ngai1tai0 | ŋai13thai0 | 崖头 |
| 0048 | 土 | 统称 | tou2 | thou21 | 土 |
| 0049 | 泥 | 湿的 | ni1ba0 | ni13pa0 | 泥巴 |
| 0050 | 水泥 | 旧称 | xuei2ni0 | ɕyei21ni0 | 水泥 |
| 0051 | 沙子 |  | sa3 huo1sa3 huang1sa3 | sa55 xuo13sa55 xuaŋ13sa55 | 沙 河沙 黄沙 |
| 0052 | 砖 | 整块的 | juan3 | tɕyan55 | 砖 |
| 0053 | 瓦 | 整块的 | wa2 | Ǿua21 | 瓦 |
| 0054 | 煤 |  | mei1 | mei13 | 煤 |
| 0055 | 煤油 |  | yang1you0 | Ǿiaŋ13Ǿiou0 | 洋油 |
| 0056 | 炭 | 木炭 | tan1 | than13 | 炭 |
| 0057 | 灰 | 烧成的 | huei3 | xuei55 | 灰 |
| 0058 | 灰尘 | 桌面上的 | huei3 | xuei55 | 灰 |
| 0059 | 火 |  | huo2 | xuo21 | 火 |
| 0060 | 烟 | 烧火形成的 | yan3 | Ǿiɛn55 | 烟 |
| 0061 | 失火 |  | qi6huo2 | tɕhi22xuo21 | 起火 |
| 0062 | 水 |  | xuei2 | ɕyei21 | 水 |
| 0063 | 凉水 |  | nen6xuei2 | nən22ɕyei21 | 冷水 |
| 0064 | 热水 | 如洗脸的热水，不是指喝的开水 | yue4xuei2 | Ǿye24ɕyei21 | 热水 |
| 0065 | 开水 | 喝的 | kai3xuei2 | khai55ɕyei21 | 开水 |
| 0066 | 磁铁 |  | xi4tie0 | ɕi24thie0 | 吸铁 |
| 0067 | 时候 | 吃饭的～ | si1hou0 | sɿ13xou0 | 时候 |
| 0068 | 什么时候 |  | mo1si1ji2 | mo13sɿ13tɕi21 | 么时几= |
| 0069 | 现在 |  | er1jin0 | Ǿɚ13tɕin0 | 而今 |
| 0070 | 以前 | 十年～ | yi2qian1 | Ǿi21tɕhiɛn13 | 以前 |
| 0071 | 以后 | 十年～ | yi2hou5 | Ǿi21xou33 | 以后 |
| 0072 | 一辈子 |  | yi4si1 | Ǿi24sɿ13 | 一世 |
| 0073 | 今年 |  | jin3nian0 | tɕin55niɛn0 | 今年 |
| 0074 | 明年 |  | min1nian0 | min13niɛn0 | 明年 |
| 0075 | 后年 |  | hou5nian0 | xou33niɛn0 | 后年 |
| 0076 | 去年 |  | qu4nian0 | tɕhy24niɛn0 | 去年 |
| 0077 | 前年 |  | qian1nian0 | tɕhiɛn13niɛn0 | 前年 |
| 0078 | 往年 | 过去的年份 | wang2nian0 | Ǿuaŋ21niɛn0 | 往年 |
| 0079 | 年初 |  | zen3yue0gan0 | tsən55Ǿye0kan0 | 正月间 |
| 0080 | 年底 |  | na4yue0gan0 | na24Ǿye0kan0 | 腊月间 |
| 0081 | 今天 |  | n3zao0 jin3zao0 | Ǿn55tsau0 tɕin55tsau0 | 嗯=朝 今朝 |
| 0082 | 明天 |  | men1zao0 | mən13tsau0 | 明朝 |
| 0083 | 后天 |  | hou5er0 | xou33Ǿɚ0 | 后日 |
| 0084 | 大后天 |  | wang5hou5er0 | Ǿuaŋ33xou33Ǿɚ0 | 万=后日 |
| 0085 | 昨天 |  | co1er0 | tsho13Ǿɚ0 | 昨日 |
| 0086 | 前天 |  | qian1ner0 | tɕhiɛn13nɚ0 | 前日 |
| 0087 | 大前天 |  | qian1qian0er0 | tɕhiɛn13tɕhiɛn0Ǿɚ0 | 前前日 |
| 0088 | 整天 |  | yi4gen2tian0 | Ǿi24kən21thiɛn0 | 一#3天 |
| 0089 | 每天 |  | tian3tian0 | thiɛn55thiɛn0 | 天天 |
| 0090 | 早晨 |  | zao2sang0 | tsau21saŋ0 | 早上 |
| 0091 | 上午 |  | sang5wu2 | saŋ33Ǿu21 | 上午 |
| 0092 | 中午 |  | zong3wu2 | tsoŋ55Ǿu21 | 中午 |
| 0093 | 下午 |  | xia5wu2 | ɕia33Ǿu21 | 下午 |
| 0094 | 傍晚 |  | sa4he4 | sa24xe24 | 煞黑 |
| 0095 | 白天 |  | be1tian3 be1tian3ni0 | pe13thiɛn55 pe13thiɛn55ni0 | 白天 白天里 |
| 0096 | 夜晚 | 与白天相对，统称 | ya5ni0 | Ǿia33ni0 | 夜里 |
| 0097 | 半夜 |  | ban1ya5 | pan13Ǿia33 | 半夜 |
| 0098 | 正月 | 农历 | zen3yue0 | tsən55Ǿye0 | 正月 |
| 0099 | 大年初一 | 农历 | zen3yue0cou3yi4 | tsən55Ǿye0tshou55Ǿi24 | 正月初一 |
| 0100 | 元宵节 |  | zen3yue0si0wu2 | tsən55Ǿye0sɿ0Ǿu21 | 正月十五 |
| 0101 | 清明 |  | qin3min0 | tɕhin55min0 | 清明 |
| 0102 | 端午 |  | dang3wu2 | taŋ55Ǿu21 | 端午 |
| 0103 | 七月十五 | 农历，节日名 | qi4yue4ban1 | tɕhi24Ǿye24pan13 | 七月半 |
| 0104 | 中秋 |  | ba4yue0si0wu2 | pa24Ǿye0sɿ0Ǿu21 | 八月十五 |
| 0105 | 冬至 |  | dong3zi0 | toŋ55tsɿ0 | 冬至 |
| 0106 | 腊月 | 农历十二月 | na4yue0 | na24Ǿye0 | 腊月 |
| 0107 | 除夕 | 农历 农历 | san3si0 qu1xi0 | san55sɿ0 tɕhy13ɕi0 | 三十 除夕 |
| 0108 | 历书 |  | huang1ni0 | xuaŋ13ni0 | 黄历 |
| 0109 | 阴历 |  | yin3ni0 | Ǿin55ni0 | 阴历 |
| 0110 | 阳历 |  | yang1ni0 | Ǿiaŋ13ni0 | 阳历 |
| 0111 | 星期天 |  | xin3qi0er4 | ɕin55tɕhi0Ǿɚ24 | 星期日 |
| 0112 | 地方 |  | di5fang0 | ti33faŋ0 | 地方 |
| 0113 | 什么地方 |  | huo1ni0 | xuo13ni0 | 何里 |
| 0114 | 家里 |  | wu4ni0 | Ǿu24ni0 | 屋里 |
| 0115 | 城里 |  | xian5ni0 | ɕiɛn33ni0 | 县里 |
| 0116 | 乡下 |  | xiang3ni0 | ɕiaŋ55ni0 | 乡里 |
| 0117 | 上面 | 从～滚下来 | sang5tai0 | saŋ33thai0 | 上头 |
| 0118 | 下面 | 从～爬上去 | ha5tai0 | xa33thai0 | 下头 |
| 0119 | 左边 |  | zo2bian3 | tso21piɛn55 | 左边 |
| 0120 | 右边 |  | you5bian0 | Ǿiou33piɛn0 | 右边 |
| 0121 | 中间 | 排队排在～ | zong3kan2 | tsoŋ55khan21 | 中间 |
| 0122 | 前面 | 排队排在～ | qian1tai0 | tɕhiɛn13thai0 | 前头 |
| 0123 | 后面 | 排队排在～ | hai5tai0 | xai33thai0 | 后头 |
| 0124 | 末尾 | 排队排在～ | din2hai5tai0 | tin21xai33thai0 | 顶后头 |
| 0125 | 对面 |  | dei1men0 | tei13mən0 | 对门 |
| 0126 | 面前 |  | ngan2men0qin0 | ŋan21mən0tɕhin0 | 眼门前 |
| 0127 | 背后 |  | hai5tai0 | xai33thai0 | 后头 |
| 0128 | 里面 | 躲在～ 躲在～ | dong5ni0 ni6tai0 | toŋ33ni0 ni22thai0 | 洞=里 里头 |
| 0129 | 外面 | 衣服晒在～ | wai5tai0 | Ǿuai33thai0 | 外头 |
| 0130 | 旁边 |  | bian3qin0 | piɛn55tɕhin0 | 边前 |
| 0131 | 上 | 碗在桌子～ | gao3tai0 | kau55thai0 | 高头 |
| 0132 | 下 | 凳子在桌子～ | ha5tai0 | xa33thai0 | 下头 |
| 0133 | 边儿 | 桌子的～ | bian3sang0 | piɛn55saŋ0 | 边上 |
| 0134 | 角儿 | 桌子的～ | guo4guer0 | kuo24kuɚ0 | 角角儿 |
| 0135 | 上去 | 他～了 | sang5ke0 | saŋ33khe0 | 上去 |
| 0136 | 下来 | 他～了 | ha5nai0 | xa33nai0 | 下来 |
| 0137 | 进去 | 他～了 | jin1ke0 | tɕin13khe0 | 进去 |
| 0138 | 出来 | 他～了 | qu4nai0 | tɕhy24nai0 | 出来 |
| 0139 | 出去 | 他～了 | qu4ke0 | tɕhy24khe0 | 出去 |
| 0140 | 回来 | 他～了 | wei1nai0 | Ǿuei13nai0 | 回来 |
| 0141 | 起来 | 天冷～了 | qi2nai0 | tɕhi21nai0 | 起来 |
| 0142 | 树 |  | xu5 | ɕy33 | 树 |
| 0143 | 木头 |  | mu4tai0 | mu24thai0 | 木头 |
| 0144 | 松树 | 统称 | cong1xu0 | tshoŋ13ɕy0 | 松树 |
| 0145 | 柏树 | 统称 | be4xu0 | pe24ɕy0 | 柏树 |
| 0146 | 杉树 |  | sa3xu0 | sa55ɕy0 | 杉树 |
| 0147 | 柳树 |  | niou2xu0 | niou21ɕy0 | 柳树 |
| 0148 | 竹子 | 统称 | zou4de0 | tsou24te0 | 竹嘚 |
| 0149 | 笋 |  | sen2de0 | sən21te0 | 笋嘚 |
| 0150 | 叶子 |  | ye4de0 | Ǿie24te0 | 叶嘚 |
| 0151 | 花 |  | hua3 | xua55 | 花 |
| 0152 | 花蕾 | 花骨朵 | hua3bao2ber0 | xua55pau21pɚ0 | 花宝宝儿 |
| 0153 | 梅花 |  | mei1hua0 | mei13xua0 | 梅花 |
| 0154 | 牡丹 |  | mo2dan0 | mo21tan0 | 牡丹 |
| 0155 | 荷花 |  | huo1hua0 | xuo13xua0 | 荷花 |
| 0156 | 草 |  | cao2 | tshau21 | 草 |
| 0157 | 藤 |  | ten1 | thən13 | 藤 |
| 0158 | 刺 | 名词 | ci1 | tshɿ13 | 刺 |
| 0159 | 水果 |  | xuei6guo0 | ɕyei22kuo0 | 水果 |
| 0160 | 苹果 |  | pin1guo0 | phin13kuo0 | 苹果 |
| 0161 | 桃子 |  | tao1de0 | thau13te0 | 桃嘚 |
| 0162 | 梨 |  | ni1de0 | ni13te0 | 梨嘚 |
| 0163 | 李子 |  | me4nier0 | me24niɚ0 | 麦李儿 |
| 0164 |  |  |  |  |  |
| 0165 | 橘子 |  | ju4de0 | tɕy24te0 | 橘嘚 |
| 0166 | 柚子 |  | you4de0 | Ǿiou24te0 | 柚嘚 |
| 0167 | 柿子 |  | si5de0 | sɿ33te0 | 柿嘚 |
| 0168 | 石榴 |  | si5niou0 | sɿ33niou0 | 石榴 |
| 0169 | 枣 |  | zao2er0 hong1zao2 | tsau21Ǿɚ0 xoŋ13tsau21 | 枣儿 红枣 |
| 0170 | 栗子 |  | ban2ni0 | pan21ni0 | 板栗 |
| 0171 | 核桃 |  | he4tao0 | xe24thau0 | 核桃 |
| 0172 |  |  |  |  |  |
| 0173 | 甘蔗 |  | gan3za0 | kan55tsa0 | 甘蔗 |
| 0174 | 木耳 |  | er6zi0 | Ǿɚ22tsɿ0 | 耳子 |
| 0175 | 蘑菇 | 野生的 野生的 | jun5de0 cong1yang0jun5 | tɕyn33te0 tshoŋ13Ǿiaŋ0tɕyn33 | 菌嘚 重阳菌 |
| 0176 | 香菇 |  | jun5de0 | tɕyn33te0 | 菌嘚 |
| 0177 | 稻子 | 指植物 | dao5 | tau33 | 稻 |
| 0178 | 稻谷 | 指籽实（脱粒后是大米） | gu4 | ku24 | 谷 |
| 0179 | 稻草 | 脱粒后的 | dao5cao2 | tau33tshau21 | 稻草 |
| 0180 | 大麦 | 指植物 | me4de0 | me24te0 | 麦嘚 |
| 0181 | 小麦 | 指植物 | xiao2me0 | ɕiau21me0 | 小麦 |
| 0182 | 麦秸 | 脱粒后的 | me4gan2 | me24kan21 | 麦秆 |
| 0183 | 谷子 | 指植物(籽实脱粒后是小米) | xiou4 | ɕiou24 | 粟 |
| 0184 | 高粱 | 指植物 | gao3niang0 | kau55niaŋ0 | 高粱 |
| 0185 | 玉米 | 指成株的植物 | bao3gu0 | pau55ku0 | 苞谷 |
| 0186 | 棉花 | 指植物 | mian1hua0 | miɛn13xua0 | 棉花 |
| 0187 | 油菜 | 油料作物，不是蔬菜 | you1cai0 | Ǿiou13tshai0 | 油菜 |
| 0188 | 芝麻 |  | zi3ma0 | tsɿ55ma0 | 芝麻 |
| 0189 | 向日葵 | 指植物 | xiang4yuer0kuei1 | ɕiaŋ24Ǿyɚ0khuei13 | 向日葵 |
| 0190 | 蚕豆 |  | wan3dou0 | Ǿuan55tou0 | 豌豆 |
| 0191 | 豌豆 |  | me4wuer0 | me24Ǿuɚ0 | 麦碗儿 |
| 0192 | 花生 | 指果实，注意婉称 | hua3sen0 | xua55sən0 | 花生 |
| 0193 | 黄豆 |  | wang1dou0 | Ǿuaŋ13tou0 | 黄豆 |
| 0194 | 绿豆 |  | nou4der0 | nou24tɚ0 | 绿豆儿 |
| 0195 | 豇豆 | 长条形的 | dou5guer0 | tou33kuɚ0 | 豆角儿 |
| 0196 | 大白菜 | 东北～ | dai5be0cai0 | tai33pe0tshai0 | 大白菜 |
| 0197 | 包心菜 | 卷心菜，圆白菜，球形的 | bao3cai0 | pau55tshai0 | 包菜 |
| 0198 | 菠菜 |  | ce2gen3cai0 | tshe21kən55tshai0 | 扯跟菜 |
| 0199 | 芹菜 |  | qin1cai0 | tɕhin13tshai0 | 芹菜 |
| 0200 | 莴笋 |  | wo3sen2 | Ǿuo55sən21 | 莴笋 |
| 0201 | 韭菜 |  | jiou2cai0 | tɕiou21tshai0 | 韭菜 |
| 0202 | 香菜 | 芫荽 | yan1xi5cai0 | Ǿiɛn13ɕi33tshai0 | 芫荽菜 |
| 0203 | 葱 |  | cong3 | tshoŋ55 | 葱 |
| 0204 | 蒜 |  | xuan1 | ɕyan13 | 蒜 |
| 0205 | 姜 |  | jiang3 | tɕiaŋ55 | 姜 |
| 0206 | 洋葱 |  | yang1cong0 | Ǿiaŋ13tshoŋ0 | 洋葱 |
| 0207 | 辣椒 | 统称 | na4jiao0 | na24tɕiau0 | 辣椒 |
| 0208 | 茄子 | 统称 | qia1de0 | tɕhia13te0 | 茄嘚 |
| 0209 | 西红柿 |  | xi3hong0si5 | ɕi55xoŋ0sɿ33 | 西红柿 |
| 0210 | 萝卜 | 统称 | nuo1pu2 | nuo13phu21 | 萝卜 |
| 0211 | 胡萝卜 |  | hu1nuo1pu2 | xu13nuo13phu21 | 胡萝卜 |
| 0212 | 黄瓜 |  | wang1gua0 | Ǿuaŋ13kua0 | 黄瓜 |
| 0213 | 丝瓜 | 无棱的 | si3gua0 | sɿ55kua0 | 丝瓜 |
| 0214 | 南瓜 | 扁圆形或梨形，成熟时赤褐色 | be4gua0 | pe24kua0 | 北瓜 |
| 0215 | 荸荠 |  | ci1mi2 | tshɿ13mi21 | 慈=米 |
| 0216 | 红薯 | 统称 | hong1qu2 | xoŋ13tɕhy21 | 红薯 |
| 0217 | 马铃薯 |  | tou2dou0 | thou21tou0 | 土豆 |
| 0218 | 芋头 |  | yu5tou0 | Ǿy33thou0 | 芋头 |
| 0219 | 山药 | 圆柱形的 | san3yo0 | san55Ǿio0 | 山药 |
| 0220 | 藕 |  | ngai2 | ƞai21 | 藕 |
| 0221 | 老虎 |  | nao2cong1 | nau21tshoŋ13 | 老虫 |
| 0222 | 猴子 |  | hou1de0 | xou13te0 | 猴嘚 |
| 0223 | 蛇 | 统称 | sa1 | sa13 | 蛇 |
| 0224 | 老鼠 | 家里的 家里的 | gao3ke0 nao2qu2de0 | kau55khe0 nau21tɕhy21te0 | 高客 老鼠嘚 |
| 0225 | 蝙蝠 |  | yan1mi2ji0er0 | Ǿiɛn13mi21tɕi0Ǿɚ0 | 檐米鸡儿 |
| 0226 | 鸟儿 | 飞鸟，统称 飞鸟，统称 | diao2er0 niao2er0 | tiau21Ǿɚ0 niau21Ǿɚ0 | 鸟儿 鸟儿 |
| 0227 | 麻雀 |  | ma1qier0 | ma13tɕhiɚ0 | 麻雀儿 |
| 0228 | 喜鹊 |  | nga3qiao2de0 | ŋa55tɕhiau21te0 | 丫巧=嘚 |
| 0229 | 乌鸦 |  | nao2wa0de0 | nau21Ǿua0te0 | 老哇嘚 |
| 0230 | 鸽子 |  | guo4de0 | kuo24te0 | 鸽嘚 |
| 0231 | 翅膀 | 鸟的，统称 | zi1bang2 | tsɿ13paŋ21 | 翅膀 |
| 0232 | 爪子 | 鸟的，统称 | zao2de0 | tsau21te0 | 爪嘚 |
| 0233 | 尾巴 |  | wei2ba0 | Ǿuei21pa0 | 尾巴 |
| 0234 | 窝 | 鸟的 | wo3 | Ǿuo55 | 窝 |
| 0235 | 虫子 | 统称 | cong1 | tshoŋ13 | 虫 |
| 0236 | 蝴蝶 | 统称 | hu1die0 | xu13tie0 | 蝴蝶 |
| 0237 | 蜻蜓 | 统称 | zi3niao2er0 | tsɿ55niau21Ǿɚ0 | 知了儿 |
| 0238 | 蜜蜂 |  | mi4fong3 | mi24foŋ55 | 蜜蜂 |
| 0239 | 蜂蜜 |  | mi4tang0 | mi24thaŋ0 | 蜜糖 |
| 0240 | 知了 | 统称 | yin3mi2cong1nger0 | Ǿin55mi21tshoŋ13ŋɚ0 | 音=米虫儿 |
| 0241 | 蚂蚁 |  | ma6nin2de0 | ma22nin21te0 | 蚂蚁嘚 |
| 0242 | 蚯蚓 |  | cou4nian2de0 | tshou24niɛn21te0 | 臭粘嘚 |
| 0243 | 蚕 |  | can1cong0 | tshan13tshoŋ0 | 蚕虫 |
| 0244 | 蜘蛛 | 会结网的 | ji4ju3 | tɕi24tɕy55 | 吸=蛛 |
| 0245 | 蚊子 | 统称 | wen1de0 | Ǿuən13te0 | 蚊嘚 |
| 0246 | 苍蝇 | 统称 统称 | huang5wen0de0 nou4tou0wen1de0 | xuaŋ33Ǿuən0te0 nou24thou0Ǿuən13te0 | 饭=蚊嘚 绿头蚊嘚 |
| 0247 | 跳蚤 | 咬人的 | tiao4zao2 | thiau24tsau21 | 跳蚤 |
| 0248 | 虱子 |  | se4po0 | se24pho0 | 虱婆 |
| 0249 | 鱼 |  | yu1 | Ǿy13 | 鱼 |
| 0250 | 鲤鱼 |  | ni2yu0 | ni21Ǿy0 | 鲤鱼 |
| 0251 | 鳙鱼 | 胖头鱼 | ma1nao2kuo0 | ma13nau21khuo0 | 麻脑壳 |
| 0252 | 鲫鱼 |  | ji4yu0 | tɕi24Ǿy0 | 鲫鱼 |
| 0253 | 甲鱼 |  | xuei2yu0 jio4yu0 | ɕyei21Ǿy0 tɕio24Ǿy0 | 水鱼 脚鱼 |
| 0254 | 鳞 | 鱼的 | nin1 | nin13 | 鳞 |
| 0255 | 虾 | 统称 | ha5de0 | xa33te0 | 虾嘚 |
| 0256 | 螃蟹 | 统称 | pang1ga0 | phaŋ13ka0 | 螃甲 |
| 0257 | 青蛙 | 统称 | ka1ma2de0 | kha13ma21te0 | 蛤蟆嘚 |
| 0258 | 癞蛤蟆 | 表皮多疙瘩 | nai5de0ka1ma2 | nai33te0kha13ma21 | 癞嘚蛤蟆 |
| 0259 | 马 |  | ma2 | ma21 | 马 |
| 0260 | 驴 |  | jiao1niou0de0 | tɕiau13niou0te0 | 叫驴嘚 |
| 0261 | 骡 |  | nuo1de0 | nuo13te0 | 骡嘚 |
| 0262 | 牛 |  | niou1 | niou13 | 牛 |
| 0263 | 公牛 | 统称 | gu2niou0 | ku21niou0 | 牯牛 |
| 0264 | 母牛 | 统称 | sa3niou0 | sa55niou0 | 㸺牛 |
| 0265 | 放牛 |  | huang1niou0 | xuaŋ13niou0 | 放牛 |
| 0266 | 羊 |  | yang1nger0 | Ǿiaŋ13ŋɚ0 | 羊儿 |
| 0267 | 猪 |  | ju3 | tɕy55 | 猪 |
| 0268 | 种猪 | 配种用的公猪 | jio4ju0 | tɕio24tɕy0 | 脚猪 |
| 0269 | 公猪 | 成年的，已阉的 | huen1ju3er0 | xuən13tɕy55Ǿɚ0 | 豮猪儿 |
| 0270 | 母猪 | 成年的，未阉的 | ju3niang0 | tɕy55niaŋ0 | 猪娘 |
| 0271 | 猪崽 |  | xiao2ju3er0 | ɕiau21tɕy55Ǿɚ0 | 小猪儿 |
| 0272 | 猪圈 |  | ju3nan0 | tɕy55nan0 | 猪栏 |
| 0273 | 养猪 |  | wei1ju3 | Ǿuei13tɕy55 | 喂猪 |
| 0274 | 猫 |  | mao3 | mau55 | 猫 |
| 0275 | 公猫 |  | gong3mao3 | koŋ55mau55 | 公猫 |
| 0276 | 母猫 |  | mu2mao3 | mu21mau55 | 母猫 |
| 0277 | 狗 | 统称 | gai2 | kai21 | 狗 |
| 0278 | 公狗 |  | gong3gai2de0 | koŋ55kai21te0 | 公狗嘚 |
| 0279 | 母狗 |  | gai2niang1de0 mu6gai2de0 | kai21niaŋ13te0 mu22kai21te0 | 狗娘嘚 母狗嘚 |
| 0280 | 叫 | 狗～ | wang3 | Ǿuaŋ55 | 汪= |
| 0281 | 兔子 |  | tou4er0 | thou24Ǿɚ0 | 兔儿 |
| 0282 | 鸡 |  | ji3 | tɕi55 | 鸡 |
| 0283 | 公鸡 | 成年的，未阉的 | ji3gong0de0 | tɕi55koŋ0te0 | 鸡公嘚 |
| 0284 | 母鸡 | 已下过蛋的 | ji3po0 | tɕi55pho0 | 鸡婆 |
| 0285 | 叫 | 公鸡～(即打鸣儿) | jiao1 | tɕiau13 | 叫 |
| 0286 | 下 | 鸡～蛋 | sen1 | sən13 | 生 |
| 0287 | 孵 | ～小鸡 | bao5 | pau33 | 抱 |
| 0288 | 鸭 |  | nga4de0 | ŋa24te0 | 鸭嘚 |
| 0289 | 鹅 |  | wo1 | Ǿuo13 | 鹅 |
| 0290 | 阉 | ～公的猪 | jian3 | tɕiɛn55 | 犍 |
| 0291 | 阉 | ～母的猪 | jian3 | tɕiɛn55 | 犍 |
| 0292 | 阉 | ～鸡 | xian1 | ɕiɛn13 | 鏾 |
| 0293 | 喂 | ～猪 | wei1 | Ǿuei13 | 喂 |
| 0294 | 杀猪 | 统称，注意婉称 | sa4ju3 | sa24tɕy55 | 杀猪 |
| 0295 | 杀 | ～鱼 | po1 | pho13 | 破 |
| 0296 | 村庄 | 一个～ | cen3 | tshən55 | 村 |
| 0297 | 胡同 | 统称：一条～ | nang5ner0 | naŋ33nɚ0 | 浪=浪=儿 |
| 0298 | 街道 |  | gai3 | kai55 | 街 |
| 0299 | 盖房子 |  | xiou3wu4 | ɕiou55Ǿu24 | 修屋 |
| 0300 | 房子 | 整座的，不包括院子 | wu4 | Ǿu24 | 屋 |
| 0301 | 屋子 | 房子里分隔而成的，统称 | huang1 | xuaŋ13 | 房 |
| 0302 | 卧室 |  | huang1 | xuaŋ13 | 房 |
| 0303 | 茅屋 | 茅草等盖的 | mao1wu0de0 | mau13Ǿu0te0 | 茅屋嘚 |
| 0304 | 厨房 |  | zao1jio0ha0 | tsau13tɕio0xa0 | 灶脚下 |
| 0305 | 灶 | 统称 | zao1 | tsau13 | 灶 |
| 0306 | 锅 | 统称 | guo3 | kuo55 | 锅 |
| 0307 | 饭锅 | 煮饭的 | huan5guo3er0 | xuan33kuo55Ǿɚ0 | 饭锅儿 |
| 0308 | 菜锅 | 炒菜的 | cai1guo3er0 | tshai13kuo55Ǿɚ0 | 菜锅儿 |
| 0309 | 厕所 | 旧式的，统称 | mao1huang0 | mau13xuaŋ0 | 茅房 |
| 0310 | 檩 | 左右方向的 左右方向的 | nin6zi0 nin2tiao1 | nin22tsɿ0 nin21thiau13 | 檩子 檩条 |
| 0311 | 柱子 |  | ju5tou0 | tɕy33thou0 | 柱头 |
| 0312 | 大门 |  | juan3men0 | tɕyan55mən0 | 专门 |
| 0313 | 门槛儿 |  | men1kan0 | mən13khan0 | 门槛 |
| 0314 | 窗 | 旧式的 | quang3huer0 | tɕhyaŋ55xuɚ0 | 窗户儿 |
| 0315 | 梯子 | 可移动的 | nou1ti0 | nou13thi0 | 楼梯 |
| 0316 | 扫帚 | 统称 统称 | sao1ba2 sao1ju2 | sau13pa21 sau13tɕy21 | 扫把 扫帚 |
| 0317 | 扫地 |  | sao2di5 | sau21ti33 | 扫地 |
| 0318 | 垃圾 |  | za3de0 | tsa55te0 | 渣嘚 |
| 0319 | 家具 | 统称 | jia3ju0 | tɕia55tɕy0 | 家具 |
| 0320 | 东西 | 我的～ | dong3xi0 | toŋ55ɕi0 | 东西 |
| 0321 |  |  |  |  |  |
| 0322 | 床 | 木制的，睡觉用 | quang1 | tɕhyaŋ13 | 床 |
| 0323 | 枕头 |  | zen2tou0 | tsən21thou0 | 枕头 |
| 0324 | 被子 |  | bei5wo0 | pei33Ǿuo0 | 被窝 |
| 0325 | 棉絮 |  | mian1xi5 | miɛn13ɕi33 | 棉絮 |
| 0326 | 床单 |  | dian5bei5 | tiɛn33pei33 | 垫被 |
| 0327 | 褥子 |  | dian5mian0xi5 | tiɛn33miɛn0ɕi33 | 垫棉絮 |
| 0328 | 席子 |  | dian5de0 | tiɛn33te0 | 簟嘚 |
| 0329 | 蚊帐 |  | zang1de0 | tsaŋ13te0 | 帐嘚 |
| 0330 | 桌子 | 统称 | zuo4er0 | tsuo24Ǿɚ0 | 桌儿 |
| 0331 | 柜子 | 统称 | guei5 | kuei33 | 柜 |
| 0332 | 抽屉 | 桌子的 | ti4er0 | thi24Ǿɚ0 | 屉儿 |
| 0333 | 案子 | 长条形的 | ngan4ban2 | ŋan24pan21 | 案板 |
| 0334 | 椅子 | 统称 | yi2den0 | Ǿi21tən0 | 椅凳 |
| 0335 | 凳子 | 统称 | den4der0 | tən24tɚ0 | 凳凳儿 |
| 0336 | 马桶 | 有盖的 | ma6tong2 | ma22thoŋ21 | 马桶 |
| 0337 | 菜刀 |  | cai1dao0 | tshai13tau0 | 菜刀 |
| 0338 | 瓢 | 舀水的 | gua3piao0 | kua55phiau0 | 瓜瓢 |
| 0339 | 缸 |  | xuei2gang0 | ɕyei21kaŋ0 | 水缸 |
| 0340 | 坛子 | 装酒的～ | tan1ter0 | than13thɚ0 | 坛坛儿 |
| 0341 | 瓶子 | 装酒的～ | pin1pier0 | phin13phiɚ0 | 瓶瓶儿 |
| 0342 | 盖子 | 杯子的～ | gai1ger0 | kai13kɚ0 | 盖盖儿 |
| 0343 | 碗 | 统称 | wan2 | Ǿuan21 | 碗 |
| 0344 | 筷子 |  | kuai1de0 | khuai13te0 | 筷嘚 |
| 0345 | 汤匙 |  | tang3piao0 | thaŋ55phiau0 | 汤瓢 |
| 0346 | 柴火 | 统称 | pi4cai0 | phi24tshai0 | 劈柴 |
| 0347 | 火柴 |  | yang1huo0 | Ǿiaŋ13xuo0 | 洋火 |
| 0348 | 锁 |  | so2 | so21 | 锁 |
| 0349 | 钥匙 |  | yo4si0 | Ǿio24sɿ0 | 钥匙 |
| 0350 | 暖水瓶 |  | yue4xuei2pin0 | Ǿye24ɕyei21phin0 | 热水瓶 |
| 0351 | 脸盆 |  | nian2per0 | niɛn21phɚ0 | 脸盆儿 |
| 0352 | 洗脸水 |  | xi6nian6xuei2 | ɕi22niɛn22ɕyei21 | 洗脸水 |
| 0353 | 毛巾 | 洗脸用 | hu1de0 | xu13te0 | 袱嘚 |
| 0354 | 手绢 |  | sou2hu1de0 | sou21xu13te0 | 手袱嘚 |
| 0355 | 肥皂 | 洗衣服用 | yang1jian2 | Ǿiaŋ13tɕiɛn21 | 洋碱 |
| 0356 | 梳子 | 旧式的，不是篦子 | mu4sou3 | mu24sou55 | 木梳 |
| 0357 | 缝衣针 |  | zen3 | tsən55 | 针 |
| 0358 | 剪子 |  | jian2dao0 | tɕiɛn21tau0 | 剪刀 |
| 0359 | 蜡烛 |  | na4 | na24 | 蜡 |
| 0360 | 手电筒 |  | sou2dian0 | sou21tiɛn0 | 手电 |
| 0361 | 雨伞 | 挡雨的，统称 | san2 | san21 | 伞 |
| 0362 | 自行车 |  | xian1ce3 dan3ce3 | ɕiɛn13tshe55 tan55tshe55 | 线车 单车 |
| 0363 | 衣服 | 统称 | yi3 | Ǿi55 | 衣 |
| 0364 | 穿 | ～衣服 | quan3 | tɕhyan55 | 穿 |
| 0365 | 脱 | ～衣服 | to4 | tho24 | 脱 |
| 0366 | 系 | ～鞋带 | tie4 | thie24 | 缔 |
| 0367 | 衬衫 |  | gua1er0 | kua13Ǿɚ0 | 褂儿 |
| 0368 | 背心 | 带两条杠的，内衣 | bei1xin0 | pei13ɕin0 | 背心 |
| 0369 | 毛衣 |  | sen1de0yi0 | sən13te0Ǿi0 | 绳嘚衣 |
| 0370 | 棉衣 |  | guen2ser0 | kuən21sɚ0 | 滚身儿 |
| 0371 | 袖子 |  | yi3xiou0 | Ǿi55ɕiou0 | 衣袖 |
| 0372 | 口袋 | 衣服上的 | dai5der0 | tai33tɚ0 | 袋袋儿 |
| 0373 | 裤子 |  | xiao2yi0 | ɕiau21Ǿi0 | 小衣 |
| 0374 | 短裤 | 外穿的 | dan2ku0 | tan21khu0 | 短裤 |
| 0375 | 裤腿 |  | ku1jio5 | khu13tɕio33 | 裤脚 |
| 0376 | 帽子 | 统称 | mao5de0 | mau33te0 | 帽嘚 |
| 0377 | 鞋子 |  | hai1 | xai13 | 鞋 |
| 0378 | 袜子 |  | wa4de0 | Ǿua24te0 | 袜嘚 |
| 0379 | 围巾 |  | wei1jin0 | Ǿuei13tɕin0 | 围巾 |
| 0380 | 围裙 |  | wei1yer0 | Ǿuei13Ǿiɚ0 | 围衣儿 |
| 0381 | 尿布 |  | niao5pian0de0 | niau33phiɛn0te0 | 尿片嘚 |
| 0382 | 扣子 |  | kou1mer0 | khou13mɚ0 | 扣帽儿 |
| 0383 | 扣 | ～扣子 | kou1 | khou13 | 扣 |
| 0384 | 戒指 |  | gu3zi0 | ku55tsɿ0 | 箍子 |
| 0385 | 手镯 |  | sou2quan3quer0 | sou21tɕhyan55tɕhyɚ0 | 手圈圈儿 |
| 0386 | 理发 |  | ti1tou1 | thi13thou13 | 剃头 |
| 0387 | 梳头 |  | sou3tou1 | sou55thou13 | 梳头 |
| 0388 | 米饭 |  | huan5 | xuan33 | 饭 |
| 0389 | 稀饭 | 用米熬的，统称 | zou4 | tsou24 | 粥 |
| 0390 | 面粉 | 麦子磨的，统称 | huei3mian0 | xuei55miɛn0 | 灰面 |
| 0391 | 面条 | 统称 | mian5 | miɛn33 | 面 |
| 0392 | 面儿 | 玉米～，辣椒～ | mo4er0 | mo24Ǿɚ0 | 末儿 |
| 0393 | 馒头 | 无馅的，统称 | man4to0 | man24tho0 | 馒坨 |
| 0394 | 包子 |  | bao3zi0 | pau55tsɿ0 | 包子 |
| 0395 | 饺子 |  | jiao2er0 | tɕiau21Ǿɚ0 | 饺儿 |
| 0396 | 馄饨 |  | huen1ten0 | xuən13thən0 | 馄饨 |
| 0397 | 馅儿 |  | xin3de0 | ɕin55te0 | 心嘚 |
| 0398 | 油条 | 长条形的，旧称 | jiao2tiao0 | tɕiau21thiau0 | 绞条 |
| 0399 | 豆浆 |  | dou5jiang3 | tou33tɕiaŋ55 | 豆浆 |
| 0400 | 豆腐脑 |  | dou5hu2nao2er0 | tou33xu21nau21Ǿɚ0 | 豆腐脑儿 |
| 0401 | 元宵 | 食品 | yuan1xiao0 | Ǿyan13ɕiau0 | 元宵 |
| 0402 | 粽子 |  | zong1de0 | tsoŋ13te0 | 粽嘚 |
| 0403 | 年糕 | 用黏性大的米或米粉做的 | nian1gao0 | niɛn13kau0 | 年糕 |
| 0404 | 点心 | 统称 | san2kai2ser0 | san21khai21sɚ0 | 散口食儿 |
| 0405 | 菜 | 吃饭时吃的，统称 | cai1 | tshai13 | 菜 |
| 0406 | 干菜 | 统称 | gan3cai0de0 | kan55tshai0te0 | 干菜嘚 |
| 0407 | 豆腐 |  | gan3zi0 | kan55tsɿ0 | 干子 |
| 0408 | 猪血 | 当菜的 | ju3xue0 | tɕy55ɕye0 | 猪血 |
| 0409 | 猪蹄 | 当菜的 | ju3ti5hua3er0 | tɕy55thi33xua55Ǿɚ0 | 猪蹄花儿 |
| 0410 | 猪舌头 | 当菜的，注意婉称 | kou2tiao0 | khou21thiau0 | 口条 |
| 0411 | 猪肝 | 当菜的，注意婉称 | ju3gan3 | tɕy55kan55 | 猪肝 |
| 0412 | 下水 | 猪牛羊的内脏 | xia5xuei2 | ɕia33ɕyei21 | 下水 |
| 0413 | 鸡蛋 |  | dan2 | tan21 | 蛋 |
| 0414 | 松花蛋 |  | pi1dan2 | phi13tan21 | 皮蛋 |
| 0415 | 猪油 |  | ban2you0 | pan21Ǿiou0 | 板油 |
| 0416 | 香油 |  | ma1you0 | ma13Ǿiou0 | 麻油 |
| 0417 | 酱油 |  | jiang4you0 | tɕiaŋ24Ǿiou0 | 酱油 |
| 0418 | 盐 | 名词 | yan1 | Ǿiɛn13 | 盐 |
| 0419 | 醋 | 注意婉称 | cou4 | tshou24 | 醋 |
| 0420 | 香烟 |  | zi2yan0 | tsɿ21Ǿiɛn0 | 纸烟 |
| 0421 | 旱烟 |  | han4yan0 | xan24Ǿiɛn0 | 旱烟 |
| 0422 | 白酒 |  | be1jiou2 | pe13tɕiou21 | 白酒 |
| 0423 | 黄酒 |  | huang1jiou2 | xuaŋ13tɕiou21 | 黄酒 |
| 0424 | 江米酒 | 酒酿，醪糟 酒酿，醪糟 | tian1jiou2 tian1jiou2de0 | thiɛn13tɕiou21 thiɛn13tɕiou21te0 | 甜酒 甜酒嘚 |
| 0425 | 茶叶 |  | ca1ye0 ca1ye4de0 | tsha13Ǿie0 tsha13Ǿie24te0 | 茶叶 茶叶嘚 |
| 0426 | 沏 | ～茶 | pao1 | phau13 | 泡 |
| 0427 | 冰棍儿 |  | bin3bang0 | pin55paŋ0 | 冰棒 |
| 0428 | 做饭 | 统称 | nong5huan5 | noŋ33xuan33 | 弄饭 |
| 0429 | 炒菜 | 统称，和做饭相对 | nong5cai1 | noŋ33tshai13 | 弄菜 |
| 0430 | 煮 | ～带壳的鸡蛋 | ju2 | tɕy21 | 煮 |
| 0431 | 煎 | ～鸡蛋 | jian3 | tɕiɛn55 | 煎 |
| 0432 | 炸 | ～油条 | za1 | tsa13 | 炸 |
| 0433 | 蒸 | ～鱼 | zen3 | tsən55 | 蒸 |
| 0434 | 揉 | ～面做馒头等 | huo1 | xuo13 | 和 |
| 0435 | 擀 | ～面，～皮儿 | gan2 | kan21 | 擀 |
| 0436 | 吃早饭 |  | qi4zao2huan0 | tɕhi24tsau21xuan0 | 吃早饭 |
| 0437 | 吃午饭 |  | qi4zong3huan0 | tɕhi24tsoŋ55xuan0 | 吃中饭 |
| 0438 | 吃晚饭 |  | qi4ya5huan0 | tɕhi24Ǿia33xuan0 | 吃夜饭 |
| 0439 | 吃 | ～饭 | qi4 | tɕhi24 | 吃 |
| 0440 | 喝 | ～酒 | huo4 | xuo24 | 喝 |
| 0441 | 喝 | ～茶 | huo4 | xuo24 | 喝 |
| 0442 | 抽 | ～烟 | qi4 | tɕhi24 | 吃 |
| 0443 | 盛 | ～饭 | sen1 | sən13 | 盛 |
| 0444 | 夹 | 用筷子～菜 | ga4 | ka24 | 夹 |
| 0445 | 斟 | ～酒 | dao1 | tau13 | 倒 |
| 0446 | 渴 | 口～ | gan3 | kan55 | 干 |
| 0447 | 饿 | 肚子～ | wo5 | Ǿuo33 | 饿 |
| 0448 | 噎 | 吃饭～着了 | gen2 | kən21 | 哽 |
| 0449 | 头 | 人的，统称 | nao2kuo0 | nau21khuo0 | 脑壳 |
| 0450 | 头发 |  | tou1hua0 | thou13xua0 | 头发 |
| 0451 | 辫子 |  | bian5de0 | piɛn33te0 | 辫嘚 |
| 0452 | 旋 |  | xuan5 | ɕyan33 | 旋 |
| 0453 | 额头 |  | nge4gao0 | ŋe24kau0 | 额高 |
| 0454 | 相貌 |  | xiang1 | ɕiaŋ13 | 相 |
| 0455 | 脸 | 洗～ | nian2 | niɛn21 | 脸 |
| 0456 | 眼睛 |  | ngan2jin0 | ŋan21tɕin0 | 眼睛 |
| 0457 | 眼珠 | 统称 | ngan2ju3de0 | ŋan21tɕy55te0 | 眼珠嘚 |
| 0458 | 眼泪 | 哭的时候流出来的 | ngan6yu2 | ŋan22Ǿy21 | 眼雨 |
| 0459 | 眉毛 |  | mei1mao0 | mei13mau0 | 眉毛 |
| 0460 | 耳朵 |  | er2dang0 | Ǿɚ21taŋ0 | 耳朵 |
| 0461 | 鼻子 |  | bi5de0 | pi33te0 | 鼻嘚 |
| 0462 | 鼻涕 | 统称 | bi5tai0 | pi33thai0 | 鼻涕 |
| 0463 | 擤 | ～鼻涕 | xin2 | ɕin21 | 擤 |
| 0464 | 嘴巴 | 人的，统称 | zei2ba0 | tsei21pa0 | 嘴巴 |
| 0465 | 嘴唇 |  | zei2sen0pi1er0 | tsei21sən0phi13Ǿɚ0 | 嘴唇皮儿 |
| 0466 | 口水 | ～流出来 | can1xuei2 | tshan13ɕyei21 | 涎水 |
| 0467 | 舌头 |  | se5de0 | se33te0 | 舌嘚 |
| 0468 | 牙齿 |  | nga1ci0 | ŋa13tshɿ0 | 牙齿 |
| 0469 | 下巴 |  | ha5kuo0 ha5ba0de0 | xa33khuo0 xa33pa0te0 | 下壳 下巴嘚 |
| 0470 | 胡子 | 嘴周围的 | hu1de0 | xu13te0 | 胡嘚 |
| 0471 | 脖子 |  | jiang6hang2 | tɕiaŋ22xaŋ21 | 颈项 |
| 0472 | 喉咙 |  | hou1guan2 | xou13kuan21 | 喉管 |
| 0473 | 肩膀 |  | jian3bao0 | tɕiɛn55pau0 | 肩包 |
| 0474 | 胳膊 |  | ga4ngan2 | ka24ŋan21 | 胳眼= |
| 0475 | 手 | 方言指(打√)：只指手；包括臂：他的～摔断了 | sou2 | sou21 | 手 |
| 0476 | 左手 |  | zo6sou2 | tso22sou21 | 左手 |
| 0477 | 右手 |  | you5sou2 | Ǿiou33sou21 | 右手 |
| 0478 | 拳头 |  | quan1tai0 sou2quei0tai0 | tɕhyan13thai0 sou21tɕhyei0thai0 | 拳头 手捶头 |
| 0479 | 手指 |  | sou2zi4mer0 | sou21tsɿ24mɚ0 | 手指拇儿 |
| 0480 | 大拇指 |  | dai5zi4mer0 | tai33tsɿ24mɚ0 | 大指拇儿 |
| 0481 | 食指 |  | si4zi4mer0 | sɿ24tsɿ24mɚ0 | 食指拇儿 |
| 0482 | 中指 |  | zong3zi4mer0 | tsoŋ55tsɿ24mɚ0 | 中指拇儿 |
| 0483 | 无名指 |  | wu1min1zi2 | Ǿu13min13tsɿ21 | 无名指 |
| 0484 | 小拇指 |  | xiao2zi4mer0 | ɕiau21tsɿ24mɚ0 | 小指拇儿 |
| 0485 | 指甲 |  | zi4ga0 | tsɿ24ka0 | 指甲 |
| 0486 | 腿 |  | tei2 | thei21 | 腿 |
| 0487 | 脚 | 方言指(打√)：只指脚；包括小腿；包括小腿和大腿：他的～压断了 | jio4 | tɕio24 | 脚 |
| 0488 | 膝盖 | 指部位 | xi4tou0guer0 | ɕi24thou0kuɚ0 | 膝头骨儿 |
| 0489 | 背 | 名词 | bei5xin0 | pei33ɕin0 | 背心 |
| 0490 | 肚子 | 腹部 | dou5 | tou33 | 肚 |
| 0491 | 肚脐 |  | dou5ji5nger0 | tou33tɕi33ŋɚ0 | 肚脐儿 |
| 0492 | 乳房 | 女性的 | zi4zi0 | tsɿ24tsɿ0 | 汁汁 |
| 0493 | 屁股 |  | pi1gu0 | phi13ku0 | 屁股 |
| 0494 | 肛门 |  | pi1ngan0 | phi13ŋan0 | 屁眼 |
| 0495 | 阴茎 | 成人的 | ba4er0 | pa24Ǿɚ0 | 把儿 |
| 0496 | 女阴 | 成人的 | ma1pi0 | ma13phi0 | 麻䏘 |
| 0497 | 肏 | 动词 动词 | er4 tong3 | Ǿɚ24 thoŋ55 | 日 通 |
| 0498 | 精液 |  | nan2jiang0 | nan21tɕiaŋ0 | 卵浆 |
| 0499 | 来月经 | 注意婉称 | nai1yi1ma0 | nai13Ǿi13ma0 | 来姨妈 |
| 0500 | 拉屎 |  | wo3ba2ba0 wo3si2 | Ǿuo55pa21pa0 Ǿuo55sɿ21 | 屙粑粑 屙屎 |
| 0501 | 撒尿 |  | wo3niao0 | Ǿuo55niau0 | 屙尿 |
| 0502 | 放屁 |  | da2pi1 | ta21phi13 | 打屁 |
| 0503 | 相当于“他妈的”的口头禅 |  | ma3na3ge0ba3zi0 | ma55na55kə0pa55tsɿ0 | 妈拉=个巴=子 |
| 0504 | 病了 |  | bin5da0 | pin33ta0 | 病哒 |
| 0505 | 着凉 |  | sou5niang1da0 | sou33niaŋ13ta0 | 受凉哒 |
| 0506 | 咳嗽 |  | ka2 | kha21 | #4 |
| 0507 | 发烧 |  | hua4yue4 | xua24Ǿye24 | 发热 |
| 0508 | 发抖 |  | da2zan1 | ta21tsan13 | 打颤 |
| 0509 | 肚子疼 |  | dou5ni0tong1 | tou33ni0thoŋ13 | 肚里痛 |
| 0510 | 拉肚子 |  | wo3xi3 | Ǿuo55ɕi55 | 屙稀 |
| 0511 | 患疟疾 |  | da6bai2de0 | ta22pai21te0 | 打摆嘚 |
| 0512 | 中暑 |  | hua1dou0de0 | xua13tou0te0 | 哗=斗=哒 |
| 0513 | 肿 |  | zong2 | tsoŋ21 | 肿 |
| 0514 | 化脓 |  | guan1nong1 | kuan13noŋ13 | 灌浓 |
| 0515 | 疤 | 好了的 好了的 | ba3 ba3de0 | pa55 pa55te0 | 疤 疤嘚 |
| 0516 | 癣 |  | xian2 | ɕiɛn21 | 癣 |
| 0517 | 痣 | 凸起的 | zi1 | tsɿ13 | 痣 |
| 0518 | 疙瘩 | 蚊子咬后形成的 | tuo1 | thuo13 | 坨 |
| 0519 | 狐臭 |  | fu1sao3qi0 | fu13sau55tɕhi0 | 狐骚气 |
| 0520 | 看病 |  | kan1bin5 | khan13pin33 | 看病 |
| 0521 | 诊脉 |  | ka3me4 | kha55me24 | #5脉 |
| 0522 | 针灸 |  | za4nin1zen3 | tsa24nin13tsən55 | 扎银针 |
| 0523 | 打针 |  | da2zen3 | ta21tsən55 | 打针 |
| 0524 | 打吊针 |  | da2diao1xuei2 | ta21tiau13ɕyei21 | 打吊水 |
| 0525 | 吃药 | 统称 | qi4yo4 | tɕhi24Ǿio24 | 吃药 |
| 0526 | 汤药 |  | zong3yo0 | tsoŋ55Ǿio0 | 中药 |
| 0527 | 病轻了 |  | bin5hao2xi3da0 | pin33xau21ɕi55ta0 | 病好些哒 |
| 0528 | 说媒 |  | zou1mei1 | tsou13mei13 | 做媒 |
| 0529 | 媒人 |  | mei1po1po0 | mei13pho13pho0 | 媒婆婆 |
| 0530 | 相亲 |  | kan1zen1ga0 | khan13zən13ka0 | 看人家 |
| 0531 | 订婚 |  | din5fen3 | tin33fən55 | 订婚 |
| 0532 | 嫁妆 |  | pei1jia1 | phei13tɕia13 | 陪嫁 |
| 0533 | 结婚 | 统称 | wei1xi2si0 | Ǿuei13ɕi21sɿ0 | 为喜事 |
| 0534 | 娶妻子 | 男子～，动宾 | jie4xi4huer0 | tɕie24ɕi24xuɚ0 | 接媳妇儿 |
| 0535 | 出嫁 | 女子～ | qu4jia1 | tɕhy24tɕia13 | 出嫁 |
| 0536 | 拜堂 |  | bai1tang1 | pai13thaŋ13 | 拜堂 |
| 0537 | 新郎 |  | xin3nang1guan3 | ɕin55naŋ13kuan55 | 新郎倌 |
| 0538 | 新娘子 |  | xin3jia2jia0 | ɕin55tɕia21tɕia0 | 新姐姐 |
| 0539 | 孕妇 |  | dou5po0de0 | tou33pho0te0 | 肚婆嘚 |
| 0540 | 怀孕 |  | huai7qi0da0 | xuai14tɕhi0ta0 | 怀起哒 |
| 0541 | 害喜 | 妊娠反应 | da2bie5 | ta21pie33 | 打瘪 |
| 0542 | 分娩 |  | sen3 | sən55 | 生 |
| 0543 | 流产 |  | xiao6can0da0 | ɕiau22tshan0ta0 | 小产哒 |
| 0544 | 双胞胎 |  | xuang3sen0de0 | ɕyaŋ55sən0te0 | 双生嘚 |
| 0545 | 坐月子 |  | zai5yue4ni0 | tsai33Ǿye24ni0 | 在月里 |
| 0546 | 吃奶 |  | hu3zi4zi0 | xu55tsɿ24tsɿ0 | 敷=汁汁 |
| 0547 | 断奶 |  | ge4nai0 | ke24nai0 | 隔奶 |
| 0548 | 满月 |  | man2yue4da0 | man21Ǿye24ta0 | 满月哒 |
| 0549 | 生日 | 统称 | sen3ner0 | sən55nɚ0 | 生日 |
| 0550 | 做寿 |  | zou1sou5 | tsou13sou33 | 做寿 |
| 0551 | 死 | 统称 | si2 | sɿ21 | 死 |
| 0552 | 死 | 婉称，最常用的几种，指老人：他～了 婉称，最常用的几种，指老人：他～了 | nao2 zou2 | nau21 tsou21 | 老 走 |
| 0553 | 自杀 |  | qin1dan2nou5 | tɕhin13tan21nou33 | 寻短路 |
| 0554 | 咽气 |  | diao1qi1 | tiau13tɕhi13 | 掉气 |
| 0555 | 入殓 |  | jin1cai1 | tɕin13tshai13 | 进材 |
| 0556 | 棺材 |  | huang3de0 | xuaŋ55te0 | 枋嘚 |
| 0557 | 出殡 |  | qu4zang1 | tɕhy24tsaŋ13 | 出葬 |
| 0558 | 灵位 |  | nin1pai0de0 | nin13phai0te0 | 灵牌嘚 |
| 0559 | 坟墓 | 单个的，老人的 | huen1san0 | xuən13san0 | 坟山 |
| 0560 | 上坟 |  | dao5huen1san0sang0ke1 | tau33xuən13san0saŋ0khe13 | 到坟山上去 |
| 0561 | 纸钱 |  | qian1zi2 | tɕhiɛn13tsɿ21 | 钱纸 |
| 0562 | 老天爷 |  | tian3nao2ye0 | thiɛn55nau21Ǿie0 | 天老爷 |
| 0563 | 菩萨 | 统称 | pu1sa0 | phu13sa0 | 菩萨 |
| 0564 | 观音 |  | guan3yin0 | kuan55Ǿin0 | 观音 |
| 0565 | 灶神 | 口头的叫法，其中如有方言亲属称谓要释义 | zao1wang0ye0 | tsau13Ǿuaŋ0Ǿie0 | 灶王爷 |
| 0566 | 寺庙 |  | miao5 | miau33 | 庙 |
| 0567 | 祠堂 |  | ci1tang0 | tshɿ13thaŋ0 | 祠堂 |
| 0568 | 和尚 |  | huo1sang0 | xuo13saŋ0 | 和尚 |
| 0569 | 尼姑 |  | ni1gu0 | ni13ku0 | 尼姑 |
| 0570 | 道士 |  | dao5si0 | tau33sɿ0 | 道士 |
| 0571 | 算命 | 统称 | xuan1ba4zi0 | ɕyan13pa24tsɿ0 | 算八字 |
| 0572 | 运气 |  | yun4qi0 | Ǿyn24tɕhi0 | 运气 |
| 0573 | 保佑 |  | bao2you0 | pau21Ǿiou0 | 保佑 |
| 0574 | 人 | 一个～ | zen1 | zən13 | 人 |
| 0575 | 男人 | 成年的，统称 | nan1di0 | nan13ti0 | 男的 |
| 0576 | 女人 | 三四十岁已婚的，统称 | yu2di0 | Ǿy21ti0 | 女的 |
| 0577 | 单身汉 |  | dou1zen0 | tou13zən0 | 独人 |
| 0578 | 老姑娘 |  | nao6yu2 | nau22Ǿy21 | 老女 |
| 0579 | 婴儿 |  | mao1mao0 | mau13mau0 | 毛毛 |
| 0580 | 小孩 | 三四岁的，统称 | xiao2nger0 | ɕiau21ŋɚ0 | 小伢儿 |
| 0581 | 男孩 | 统称：外面有个～在哭 | nang1nger0 | naŋ13ŋɚ0 | 男伢儿 |
| 0582 | 女孩 | 统称：外面有个～在哭 | yu2nger0 | Ǿy21ŋɚ0 | 女伢儿 |
| 0583 | 老人 | 七八十岁的，统称 | nao2zen1ga0 | nau21zən13ka0 | 老人家 |
| 0584 | 亲戚 | 统称 | qin3qi0 | tɕhin55tɕhi0 | 亲戚 |
| 0585 | 朋友 | 统称 | huo4si4di0 | xuo24sɿ24ti0 | 合适的 |
| 0586 | 邻居 | 统称 | nin1sa0 | nin13sa0 | 邻舍 |
| 0587 | 客人 |  | ke4 | khe24 | 客 |
| 0588 | 农民 |  | xiang3ni0di0 | ɕiaŋ55ni0ti0 | 乡里的 |
| 0589 | 商人 |  | zou1sen3yi0di0 | tsou13sən55Ǿi0ti0 | 做生意的 |
| 0590 | 手艺人 | 统称 | zou1sou2yi0di0 | tsou13sou21Ǿi0ti0 | 做手艺的 |
| 0591 | 泥水匠 |  | wa6jiang2 | Ǿua22tɕiaŋ21 | 瓦匠 |
| 0592 | 木匠 |  | mu4jiang2 | mu24tɕiaŋ21 | 木匠 |
| 0593 | 裁缝 |  | cai1fong0 | tshai13foŋ0 | 裁缝 |
| 0594 | 理发师 |  | ti1tou1di0 | thi13thou13ti0 | 剃头的 |
| 0595 | 厨师 |  | nong5huan5di0 | noŋ33xuan33ti0 | 弄饭的 |
| 0596 | 师傅 |  | si3hu0 | sɿ55xu0 | 师傅 |
| 0597 | 徒弟 |  | xio1tou1di0 | ɕio13thou13ti0 | 学徒的 |
| 0598 | 乞丐 | 统称，非贬称(无统称则记成年男的) | gao1hua0de0 | kau13xua0te0 | 告化嘚 |
| 0599 | 妓女 |  | mai2sen3di0 | mai21sən55ti0 | 卖身的 |
| 0600 | 流氓 |  | pi2zi0 | phi21ʦɿ0 | 痞子 |
| 0601 | 贼 |  | ha3tiao0de0 | xa55thiau0te0 | 哈=巧嘚 |
| 0602 | 瞎子 | 统称，非贬称(无统称则记成年男的) | ha4de0 | xa24te0 | 瞎嘚 |
| 0603 | 聋子 | 统称，非贬称(无统称则记成年男的) | nong3de0 | noŋ55te0 | 聋嘚 |
| 0604 | 哑巴 | 统称，非贬称(无统称则记成年男的) | nga2ba0 | ŋa21pa0 | 哑巴 |
| 0605 | 驼子 | 统称，非贬称(无统称则记成年男的) | tuo1de0 | thuo13te0 | 驼嘚 |
| 0606 | 瘸子 | 统称，非贬称(无统称则记成年男的) | bai3de0 | pai55te0 | 足拜嘚 |
| 0607 | 疯子 | 统称，非贬称(无统称则记成年男的) | dian3de0 | tiɛn55te0 | 癫嘚 |
| 0608 | 傻子 | 统称，非贬称(无统称则记成年男的) | sai2tuo0 | sai21thuo0 | 傻坨 |
| 0609 | 笨蛋 | 蠢的人 | qun2tuo0 | tɕhyn21thuo0 | 蠢坨 |
| 0610 | 爷爷 | 呼称，最通用的 | ye1ye0 | Ǿie13Ǿie0 | 爷爷 |
| 0611 | 奶奶 | 呼称，最通用的 | nai3nai0 | nai55nai0 | 奶奶 |
| 0612 | 外祖父 | 叙称 | ga3gong0 | ka55koŋ0 | 家公 |
| 0613 | 外祖母 | 叙称 | ga3ga0 | ka55ka0 | 家家 |
| 0614 | 父母 | 合称 | dai5zen0 | tai33zən0 | 大人 |
| 0615 | 父亲 | 叙称 叙称 | die3die0 ba1ba0 | tie55tie0 pa13pa0 | 爹爹 爸爸 |
| 0616 | 母亲 | 叙称 | m2ma0 | Ǿm21ma0 | 姆妈 |
| 0617 | 爸爸 | 呼称，最通用的 呼称，最通用的 | die3 ba1ba0 | tie55 pa13pa0 | 爹 爸爸 |
| 0618 | 妈妈 | 呼称，最通用的 | m2ma0 | Ǿm21ma0 | 姆妈 |
| 0619 | 继父 | 叙称 | hou5nai0die3 | xou33nai0tie55 | 后来爹 |
| 0620 | 继母 | 叙称 | hou5nai0m2ma0 | xou33nai0Ǿm21ma0 | 后来姆妈 |
| 0621 | 岳父 | 叙称 | zang5zen0nao2 | tsaŋ33zən0nau21 | 丈人佬 |
| 0622 | 岳母 | 叙称 | zang5mu2niang0 | tsaŋ33mu21niaŋ0 | 丈母娘 |
| 0623 | 公公 | 叙称 叙称 | gong3ga0 ga3ya0 | koŋ55ka0 ka55Ǿia0 | 公家 家爷 |
| 0624 | 婆婆 | 叙称 | ga3niang0 | ka55niaŋ0 | 家娘 |
| 0625 | 伯父 | 呼称，统称 | be4be0 | pe24pe0 | 伯伯 |
| 0626 | 伯母 | 呼称，统称 | be4ma0 | pe24ma0 | 伯妈 |
| 0627 | 叔父 | 呼称，统称 | sou4sou0 | sou24sou0 | 叔叔 |
| 0628 | 排行最小的叔父 | 呼称，如“幺叔” | yao3sou0 | Ǿiau55sou0 | 幺叔 |
| 0629 | 叔母 | 呼称，统称 | yao3yao0 | Ǿiau55Ǿiau0 | 幺幺 |
| 0630 | 姑 | 呼称，统称(无统称则记分称：比父大，比父小；已婚，未婚) | yao3yao0 | Ǿiau55Ǿiau0 | 幺幺 |
| 0631 | 姑父 | 呼称，统称 | gu3ya0 | ku55Ǿia0 | 姑爷 |
| 0632 | 舅舅 | 呼称 | jiou5jiou0 | tɕiou33tɕiou0 | 舅舅 |
| 0633 | 舅妈 | 呼称 | jiou5ma0 | tɕiou33ma0 | 舅妈 |
| 0634 | 姨 | 呼称，统称(无统称则记分称：比母大，比母小；已婚，未婚) 呼称，统称(无统称则记分称：比母大，比母小；已婚，未婚) | yi1ma3 yi1yi0 | Ǿi13ma55 Ǿi13Ǿi0 | 姨妈 姨姨 |
| 0635 | 姨父 | 呼称，统称 | yi1ya0 | Ǿi13Ǿia0 | 姨爷 |
| 0636 | 弟兄 | 合称 合称 | di5xiong0 xiong3di0 | ti33ɕioŋ0 ɕioŋ55ti0 | 弟兄 兄弟 |
| 0637 | 姊妹 | 合称，注明是否可包括男性 | zi2mei0 | tsɿ21mei0 | 姊妹 |
| 0638 | 哥哥 | 呼称，统称 | guo3guo0 | kuo55kuo0 | 哥哥 |
| 0639 | 嫂子 | 呼称，统称 | sao2de0 | sau21te0 | 嫂嘚 |
| 0640 | 弟弟 | 叙称 | nao2er0 | nau21Ǿɚ0 | 佬儿 |
| 0641 | 弟媳 | 叙称 | nao2di0xi4hu0 | nau21ti0ɕi24xu0 | 佬弟媳妇 |
| 0642 | 姐姐 | 呼称，统称 | jie2jie0 | tɕie21tɕie0 | 姐姐 |
| 0643 | 姐夫 | 呼称 | jie2hu0 | tɕie21xu0 | 姐夫 |
| 0644 | 妹妹 | 叙称 | mei4mei0 | mei24mei0 | 妹妹 |
| 0645 | 妹夫 | 叙称 | mei5hu0de0 | mei33xu0te0 | 妹夫嘚 |
| 0646 | 堂兄弟 | 叙称，统称 | sou4be0di5xiong0 | sou24pe0ti33ɕioŋ0 | 叔伯弟兄 |
| 0647 | 表兄弟 | 叙称，统称 | nao6biao2 | nau22piau21 | 老表 |
| 0648 | 妯娌 | 弟兄妻子的合称 | cou1ni0 | tshou13ni0 | 妯娌 |
| 0649 | 连襟 | 姊妹丈夫的关系，叙称 | nian1jin0 | niɛn13tɕin0 | 连襟 |
| 0650 | 儿子 | 叙称：我的～ | er1 | Ǿɚ13 | 儿 |
| 0651 | 儿媳妇 | 叙称：我的～ | xi4hu0 | ɕi24xu0 | 媳妇 |
| 0652 | 女儿 | 叙称：我的～ | mei4zi0 | mei24tsɿ0 | 妹子 |
| 0653 | 女婿 | 叙称：我的～ | nang1 | naŋ13 | 郎 |
| 0654 | 孙子 | 儿子之子 | sen3nger0 | sən55ŋɚ0 | 孙儿 |
| 0655 | 重孙子 | 儿子之孙 | cong1sen3ser0 | tshoŋ13sən55sɚ0 | 重孙孙儿 |
| 0656 | 侄子 | 弟兄之子 | zi5er0 | tsɿ33Ǿɚ0 | 侄儿 |
| 0657 | 外甥 | 姐妹之子 | wai5sen0 | Ǿuai33sən0 | 外甥 |
| 0658 | 外孙 | 女儿之子 | wai5sen3 | Ǿuai33sən55 | 外孙 |
| 0659 | 夫妻 | 合称 | niang6kou6zi0 | niaŋ22khou22tsɿ0 | 两口子 |
| 0660 | 丈夫 | 叙称，最通用的，非贬称：她的～ 叙称，最通用的，非贬称：她的～ | nan1di0 nao2jie0 | nan13ti0 nau21tɕie0 | 男的 老姐 |
| 0661 | 妻子 | 叙称，最通用的，非贬称：他的～ | xi4huer0 | ɕi24xuɚ0 | 媳妇儿 |
| 0662 | 名字 |  | min1zi0 | min13tsɿ0 | 名字 |
| 0663 | 绰号 |  | huen5min0 | xuən33min0 | 混名 |
| 0664 | 干活儿 | 统称：在地里～ | zou1si5 | tsou13sɿ33 | 做事 |
| 0665 | 事情 | 一件～ | si5 | sɿ33 | 事 |
| 0666 | 插秧 |  | ca4yang3 | tsha24Ǿiaŋ55 | 插秧 |
| 0667 | 割稻 |  | guo4dao5 | kuo24tau33 | 割稻 |
| 0668 | 种菜 |  | zong2cai1 | tsoŋ21tshai13 | 种菜 |
| 0669 | 犁 | 名词 | ni1pa0de0 | ni13pha0te0 | 犁耙嘚 |
| 0670 | 锄头 |  | wa4cou0 | Ǿua24tshou0 | 挖锄 |
| 0671 | 镰刀 |  | yue4niang0dao0er0 | Ǿye24niaŋ0tau0Ǿɚ0 | 月亮刀儿 |
| 0672 | 把儿 | 刀～ | ba1ber0 | pa13pɚ0 | 把把儿 |
| 0673 | 扁担 |  | bian2tan0 | piɛn21than0 | 扁担 |
| 0674 | 箩筐 |  | nuo1qiang0 | nuo13tɕhiaŋ0 | 箩筐 |
| 0675 | 筛子 | 统称 | sai3de0 | sai55te0 | 筛嘚 |
| 0676 | 簸箕 | 农具，有梁的 | cuo4ji0 | tshuo24tɕi0 | 撮箕 |
| 0677 | 簸箕 | 簸米用 | sai3de0 | sai55te0 | 筛嘚 |
| 0678 | 独轮车 |  | ca3er0 | tsha55Ǿɚ0 | 叉儿 |
| 0679 | 轮子 | 旧式的，如独轮车上的 | guen2zi0 | kuən21tsɿ0 | 滚子 |
| 0680 | 碓 | 整体 | dei1 | tei13 | 碓 |
| 0681 | 臼 |  | dei1wo3de0 | tei13Ǿuo55te0 | 碓窝嘚 |
| 0682 | 磨 | 名词 | mo5de0 | mo33te0 | 磨嘚 |
| 0683 | 年成 |  | sou3cen1 | sou55tshən13 | 收成 |
| 0684 | 走江湖 | 统称 | pao2se4huei0 | phau21se24xuei0 | 跑社会 |
| 0685 | 打工 |  | zou1si5 | tsou13sɿ33 | 做事 |
| 0686 | 斧子 |  | kai3san3zi0 | khai55san55tsɿ0 | 开山子 |
| 0687 | 钳子 |  | ga4jian2 | ka24tɕiɛn21 | 夹剪 |
| 0688 | 螺丝刀 |  | qi2zi0 | tɕhi21tsɿ0 | 起子 |
| 0689 | 锤子 |  | din3quer0 | tin55tɕhyɚ0 | 钉锤儿 |
| 0690 | 钉子 |  | din3de0 | tin55te0 | 钉嘚 |
| 0691 | 绳子 |  | sen1de0 | sən13te0 | 绳嘚 |
| 0692 | 棍子 |  | guen1de0 | kuən13te0 | 棍嘚 |
| 0693 | 做买卖 |  | zou1sen3yi0 | tsou13sən55Ǿi0 | 做生意 |
| 0694 | 商店 |  | dian4dier0 | tiɛn24tiɚ0 | 店店儿 |
| 0695 | 饭馆 |  | can3guan2 | tshan55kuan21 | 餐馆 |
| 0696 | 旅馆 | 旧称 | ni2se0 | ni21se0 | 旅社 |
| 0697 | 贵 |  | guei1 | kuei13 | 贵 |
| 0698 | 便宜 |  | pian1yi0 | phiɛn13Ǿi0 | 便宜 |
| 0699 | 合算 |  | hua1de0nai1 | xua13te0nai13 | 划得来 |
| 0700 | 折扣 |  | ze4kou0 | tse24khou0 | 折扣 |
| 0701 | 亏本 |  | se1ben2 | se13pən21 | 折本 |
| 0702 | 钱 | 统称 | qian1 | tɕhiɛn13 | 钱 |
| 0703 | 零钱 |  | san2qian1 | san21tɕhiɛn13 | 散钱 |
| 0704 | 硬币 |  | kuo4zi0 | khuo24tsɿ0 | 锞子 |
| 0705 | 本钱 |  | ben2qian0 | pən21tɕhiɛn0 | 本钱 |
| 0706 | 工钱 |  | gong3qian0 | koŋ55tɕhiɛn0 | 工钱 |
| 0707 | 路费 |  | pan1cen0 nou5huei0 | phan13tshən0 nou33xuei0 | 盘缠 路费 |
| 0708 | 花 | ～钱 | yong5 | Ǿioŋ33 | 用 |
| 0709 | 赚 | 卖一斤能～一毛钱 | juan5 | tɕyan33 | 赚 |
| 0710 | 挣 | 打工～了一千块钱 | nong5 | noŋ33 | 弄 |
| 0711 | 欠 | ～他十块钱 ～他十块钱 | gai3 ca3 | kai55 tsha55 | 该 差 |
| 0712 | 算盘 |  | xuan1pan0 | ɕyan13phan0 | 算盘 |
| 0713 | 秤 | 统称 | cen1 | tshən13 | 秤 |
| 0714 | 称 | 用秆秤～ | cen3 | tshən55 | 称 |
| 0715 | 赶集 |  | gan6cang2 | kan22tshaŋ21 | 赶场 |
| 0716 | 集市 |  | si4cang2 | sɿ24tshaŋ21 | 市场 |
| 0717 | 庙会 |  | miao5huei5 | miau33xuei33 | 庙会 |
| 0718 | 学校 |  | xio5tang0 | ɕio33thaŋ0 | 学堂 |
| 0719 | 教室 |  | jiao4si0 | tɕiau24sɿ0 | 教室 |
| 0720 | 上学 |  | tou1xu3 | thou13ɕy55 | 读书 |
| 0721 | 放学 |  | huang1xio1 | xuaŋ13ɕio13 | 放学 |
| 0722 | 考试 |  | kao2si0 | khau21sɿ0 | 考试 |
| 0723 | 书包 |  | xu3bao0 | ɕy55pau0 | 书包 |
| 0724 | 本子 |  | ben2de0 ben2ber0 | pən21te0 pən21pɚ0 | 本嘚 本本儿 |
| 0725 | 铅笔 |  | qian3bi0 | tɕhiɛn55pi0 | 铅笔 |
| 0726 | 钢笔 |  | gang3bi0 | kaŋ55pi0 | 钢笔 |
| 0727 | 圆珠笔 |  | yuan1zi0bi0 | Ǿyan13tsɿ0pi0 | 圆子笔 |
| 0728 | 毛笔 |  | mao1bi0 | mau13pi0 | 毛笔 |
| 0729 | 墨 |  | me4 | me24 | 墨 |
| 0730 | 砚台 |  | nian5tai0 | niɛn33thai0 | 砚台 |
| 0731 | 信 | 一封～ | xin1 | ɕin13 | 信 |
| 0732 | 连环画 |  | nga1nger0xu0 | ŋa13ŋɚ0ɕy0 | 伢伢儿书 |
| 0733 | 捉迷藏 |  | duo2qia3mer0 | tuo21tɕhia55mɚ0 | 躲#6迷儿 |
| 0734 | 跳绳 |  | tiao4sen1 | thiau24sən13 | 跳绳 |
| 0735 | 毽子 |  | jian1de0 | tɕiɛn13te0 | 毽嘚 |
| 0736 | 风筝 |  | fong3zong0 | foŋ55tsoŋ0 | 风筝 |
| 0737 | 舞狮 |  | wan1si3de0 | Ǿuan13sɿ55te0 | 玩狮嘚 |
| 0738 | 鞭炮 | 统称 | pao1zang2 | phau13tsaŋ21 | 炮仗 |
| 0739 | 唱歌 |  | cang1guo3 | tshaŋ13kuo55 | 唱歌 |
| 0740 | 演戏 |  | yan2xi1 | Ǿiɛn21ɕi13 | 演戏 |
| 0741 | 锣鼓 | 统称 | nuo1gu2ga3si0 | nuo13ku21ka55sɿ0 | 锣鼓家什 |
| 0742 | 二胡 |  | fu1qin0 | fu13tɕhin0 | 胡琴 |
| 0743 | 笛子 |  | ti4er0 | thi24Ǿɚ0 | 笛儿 |
| 0744 | 划拳 |  | cai3quan1 | tshai55tɕhyan13 | 猜拳 |
| 0745 | 下棋 |  | zai2xiang5qi0 | tsai21ɕiaŋ33tɕhi0 | 走象棋 |
| 0746 | 打扑克 |  | da2pai1 | ta21phai13 | 打牌 |
| 0747 | 打麻将 |  | wan1ma1jiang0 | Ǿuan13ma13tɕiaŋ0 | 玩麻将 |
| 0748 | 变魔术 |  | wan1ba2xi0 | Ǿuan13pa21ɕi0 | 玩把戏 |
| 0749 | 讲故事 |  | gang2gu4si0 | kaŋ21ku24sɿ0 | 讲故事 |
| 0750 | 猜谜语 |  | cai3mei1de0 | tshai55mei13te0 | 猜谜嘚 |
| 0751 | 玩儿 | 游玩：到城里～ | wan1 | Ǿuan13 | 玩 |
| 0752 | 串门儿 |  | dao5bie1guo0wu4ni0ke1 | tau33pie13kuo0Ǿu24ni0khe13 | 到别个屋里去 |
| 0753 | 走亲戚 |  | zai2zen1ga0 | tsai21zən13ka0 | 走人家 |
| 0754 | 看 | ～电视 | kan1 | khan13 | 看 |
| 0755 | 听 | 用耳朵～ | tin3 | thin55 | 听 |
| 0756 | 闻 | 嗅：用鼻子～ | wen1 | Ǿuən13 | 闻 |
| 0757 | 吸 | ～气 | hu3 | xu55 | 敷= |
| 0758 | 睁 | ～眼 | zen3 | tsən55 | 睁 |
| 0759 | 闭 | ～眼 | bei1 | pei13 | 闭 |
| 0760 | 眨 | ～眼 | za4 | tsa24 | 眨 |
| 0761 | 张 | ～嘴 | za3 | tsa55 | 奓 |
| 0762 | 闭 | ～嘴 | bei1 | pei13 | 闭 |
| 0763 | 咬 | 狗～人 | ngao2 | ŋau21 | 咬 |
| 0764 | 嚼 | 把肉～碎 | jiao5 | tɕiau33 | 嚼 |
| 0765 | 咽 | ～下去 | ten3 | thən55 | 吞 |
| 0766 | 舔 | 人用舌头～ | tian2 | thiɛn21 | 舔 |
| 0767 | 含 | ～在嘴里 | han1 | xan13 | 含 |
| 0768 | 亲嘴 |  | qiou3 | tɕhiou55 | 秋= |
| 0769 | 吮吸 | 用嘴唇聚拢吸取液体，如吃奶时 | hu3 | xu55 | 敷= |
| 0770 | 吐 | 上声，把果核儿～掉 | tou2 | thou21 | 吐 |
| 0771 | 吐 | 去声，呕吐：喝酒喝～了 | wa2 | Ǿua21 | 哇 |
| 0772 | 打喷嚏 |  | da2huen1qiou0 | ta21xuən13tɕhiou0 | 打喷=球= |
| 0773 | 拿 | 用手把苹果～过来 | na3 | na55 | 拿 |
| 0774 | 给 | 他～我一个苹果 他～我一个苹果 | ba2 ge2 | pa21 ke21 | 把 给 |
| 0775 | 摸 | ～头 | mo3 | mo55 | 摸 |
| 0776 | 伸 | ～手 | sen3 | sən55 | 伸 |
| 0777 | 挠 | ～痒痒 | kou3 | khou55 | 抠 |
| 0778 | 掐 | 用拇指和食指的指甲～皮肉 | ka4 | kha24 | 掐 |
| 0779 | 拧 | ～螺丝 | jiou3 | tɕiou55 | 㲃 |
| 0780 | 拧 | ～毛巾 | jiou3 | tɕiou55 | 㲃 |
| 0781 | 捻 | 用拇指和食指来回～碎 | co3 | tsho55 | 搓 |
| 0782 | 掰 | 把橘子～开，把馒头～开 | mie4 | mie24 | 搣 |
| 0783 | 剥 | ～花生 | bo4 | po24 | 剥 |
| 0784 | 撕 | 把纸～了 | si3 | sɿ55 | 撕 |
| 0785 | 折 | 把树枝～断 | que2 | tɕhye21 | 抈 |
| 0786 | 拔 | ～萝卜 | ca2 | tsha21 | 扯 |
| 0787 | 摘 | ～花 | ka4 | kha24 | 掐 |
| 0788 | 站 | 站立：～起来 | zan1 | tsan13 | 站 |
| 0789 | 倚 | 斜靠：～在墙上 | kao1 | khau13 | 靠 |
| 0790 | 蹲 | ～下 | juai3 | tɕyai55 | #1 |
| 0791 | 坐 | ～下 | zo5 | tso33 | 坐 |
| 0792 | 跳 | 青蛙～起来 | zao4 | tsau24 | #7 |
| 0793 | 迈 | 跨过高物：从门槛上～过去 | qia1 | tɕhia13 | 㐄 |
| 0794 | 踩 | 脚～在牛粪上 | jiang1 | tɕiaŋ13 | #8 |
| 0795 | 翘 | ～腿 | niao3 | niau55 | 蹘 |
| 0796 | 弯 | ～腰 | gong3 | koŋ55 | 弓 |
| 0797 | 挺 | ～胸 | tin2 | thin21 | 挺 |
| 0798 | 趴 | ～着睡 | pu4 | phu24 | 扑 |
| 0799 | 爬 | 小孩在地上～ | na1 | na13 | #9 |
| 0800 | 走 | 慢慢儿～ | zou2 | tsou21 | 走 |
| 0801 | 跑 | 慢慢儿走，别～ | pao2 | phau21 | 跑 |
| 0802 | 逃 | 逃跑：小偷～走了 | pao2 | phau21 | 跑 |
| 0803 | 追 | 追赶：～小偷 | ka3 | kha55 | #5 |
| 0804 | 抓 | ～小偷 | ka3 | kha55 | #5 |
| 0805 | 抱 | 把小孩～在怀里 | bao5 | pau33 | 抱 |
| 0806 | 背 | ～孩子 | bei3 | pei55 | 背 |
| 0807 | 搀 | ～老人 | hu1 | xu13 | 扶 |
| 0808 | 推 | 几个人一起～汽车 | cong2 | tshoŋ21 | 揰 |
| 0809 | 摔 | 跌：小孩～倒了 跌：小孩～倒了 | ban2 da4 | pan21 ta24 | 绊 #10 |
| 0810 | 撞 | 人～到电线杆上 | bang5 | paŋ33 | 棒= |
| 0811 | 挡 | 你～住我了，我看不见 | nan1 | nan13 | 拦 |
| 0812 | 躲 | 躲藏：他～在床底下 | qia3 | tɕhia55 | #6 |
| 0813 | 藏 | 藏放，收藏：钱～在枕头下面 | sou3 | sou55 | 收 |
| 0814 | 放 | 把碗～在桌子上 | guo4 | kuo24 | 搁 |
| 0815 | 摞 | 把砖～起来 | do5 | to33 | #11 |
| 0816 | 埋 | ～在地下 | mai1 | mai13 | 埋 |
| 0817 | 盖 | 把茶杯～上 | gai1 | kai13 | 盖 |
| 0818 | 压 | 用石头～住 | nga4 | ŋa24 | 压 |
| 0819 | 摁 | 用手指按：～图钉 | cen2 | tshən21 | #12 |
| 0820 | 捅 | 用棍子～鸟窝 | co4 | tsho24 | 戳 |
| 0821 | 插 | 把香～到香炉里 | ca4 | tsha24 | 插 |
| 0822 | 戳 | ～个洞 | co4 | tsho24 | 戳 |
| 0823 | 砍 | ～树 | kan2 | khan21 | 砍 |
| 0824 | 剁 | 把肉～碎做馅儿 把肉～碎做馅儿 | zan2 do1 | tsan21 to13 | 斩 剁 |
| 0825 | 削 | ～苹果 | xio4 | ɕio24 | 削 |
| 0826 | 裂 | 木板～开了 | za3 | tsa55 | 奓 |
| 0827 | 皱 | 皮～起来 | zong4 | tsoŋ24 | 皱 |
| 0828 | 腐烂 | 死鱼～了 | cou1 | tshou13 | 臭 |
| 0829 | 擦 | 用毛巾～手 | kai3 | khai55 | 揩 |
| 0830 | 倒 | 把碗里的剩饭～掉 | kuang3 | khuaŋ55 | #13 |
| 0831 | 扔 | 丢弃：这个东西坏了，～了它 | diou3 | tiou55 | 丢 |
| 0832 | 扔 | 投掷：比一比谁～得远 | yua1 | Ǿya13 | #14 |
| 0833 | 掉 | 掉落，坠落：树上～下一个梨 | diao1 | tiau13 | 掉 |
| 0834 | 滴 | 水～下来 | di4 | ti24 | 滴 |
| 0835 | 丢 | 丢失：钥匙～了 | diao1 | tiau13 | 掉 |
| 0836 | 找 | 寻找：钥匙～到 | qin1 | tɕhin13 | 寻 |
| 0837 | 捡 | ～到十块钱 | jian2 | tɕiɛn21 | 捡 |
| 0838 | 提 | 用手把篮子～起来 | ti1 | thi13 | 提 |
| 0839 | 挑 | ～担 | tiao3 | thiau55 | 挑 |
| 0840 | 扛 | kánɡ，把锄头～在肩上 | bei3 | pei55 | 背 |
| 0841 | 抬 | ～轿 | tai1 | thai13 | 抬 |
| 0842 | 举 | ～旗子 | ju2 | tɕy21 | 举 |
| 0843 | 撑 | ～伞 | da2 | ta21 | 打 |
| 0844 | 撬 | 把门～开 | qiao2 | tɕhiau21 | 撬 |
| 0845 | 挑 | 挑选，选择：你自己～一个 | xuan2 | ɕyan21 | 选 |
| 0846 | 收拾 | ～东西 | qin3si5 | tɕhin55sɿ33 | 清拾 |
| 0847 | 挽 | ～袖子 | juan2 | tɕyan21 | 卷 |
| 0848 | 涮 | 把杯子～一下 | nang2 | naŋ21 | 朗= |
| 0849 | 洗 | ～衣服 | xi2 | ɕi21 | 洗 |
| 0850 | 捞 | ～鱼 | ka3 | kha55 | #5 |
| 0851 | 拴 | ～牛 | tao1 | thau13 | 绹 |
| 0852 | 捆 | ～起来 ～起来 | bang2 kuen2 | paŋ21 khuən21 | 绑 捆 |
| 0853 | 解 | ～绳子 | gai2 | kai21 | 解 |
| 0854 | 挪 | ～桌子 | yi1 | Ǿi13 | 移 |
| 0855 | 端 | ～碗 | dan3 | tan55 | 端 |
| 0856 | 摔 | 碗～碎了 | da4 | ta24 | #10 |
| 0857 | 掺 | ～水 | can3 | tshan55 | 掺 |
| 0858 | 烧 | ～柴 | sao3 | sau55 | 烧 |
| 0859 | 拆 | ～房子 | ce4 | tshe24 | 拆 |
| 0860 | 转 | ～圈儿 ～圈儿 | da2 juan4 | ta21 tɕyan24 | 打 转 |
| 0861 | 捶 | 用拳头～ | nei1 | nei13 | 擂 |
| 0862 | 打 | 统称：他～了我一下 | da2 | ta21 | 打 |
| 0863 | 打架 | 动手：两个人在～ | da2jia1 | ta21tɕia13 | 打架 |
| 0864 | 休息 |  | xie4 | ɕie24 | 歇 |
| 0865 | 打哈欠 |  | ca2huo3xian0 | tsha21xuo55ɕiɛn0 | 扯呵欠 |
| 0866 | 打瞌睡 |  | da6cong2 | ta22tshoŋ21 | 打#15 |
| 0867 | 睡 | 他已经～了 | xie4 | ɕie24 | 歇 |
| 0868 | 打呼噜 |  | da2han0 | ta21xan0 | 打鼾 |
| 0869 | 做梦 |  | zou1mong5 | tsou13moŋ33 | 做梦 |
| 0870 | 起床 |  | qi2nai0 | tɕhi21nai0 | 起来 |
| 0871 | 刷牙 |  | sou1kou2 | sou13khou21 | 漱口 |
| 0872 | 洗澡 |  | xi6zao2 | ɕi22tsau21 | 洗澡 |
| 0873 | 想 | 思索：让我～一下 | xiang2 | ɕiaŋ21 | 想 |
| 0874 | 想 | 想念：我很～他 | xiang2 | ɕiaŋ21 | 想 |
| 0875 | 打算 | 我～开个店 | jun2bei5 | tɕyn21pei33 | 准备 |
| 0876 | 记得 |  | ji1de0 | tɕi13te0 | 记得 |
| 0877 | 忘记 |  | bu4ji1de0 | pu24tɕi13te0 | 不记得 |
| 0878 | 怕 | 害怕：你别～ | he4 | xe24 | 嚇 |
| 0879 | 相信 | 我～你 | xin4 | ɕin24 | 信 |
| 0880 | 发愁 |  | you4 | Ǿiou24 | 忧 |
| 0881 | 小心 | 过马路要～ | kan1dao2xi0 | khan13tau21ɕi0 | 看倒些 |
| 0882 | 喜欢 | ～看电视 | ngai4 | ŋai24 | 爱 |
| 0883 | 讨厌 | ～这个人 | bu4xi2huan0 | pu24ɕi21xuan0 | 不喜欢 |
| 0884 | 舒服 | 凉风吹来很～ | xu3hu0 | ɕy55xu0 | 舒服 |
| 0885 | 难受 | 生理的 | bu4xu3hu0 | pu24ɕy55xu0 | 不舒服 |
| 0886 | 难过 | 心理的 | bu4xu3hu0 | pu24ɕy55xu0 | 不舒服 |
| 0887 | 高兴 |  | kuai4huo0 xi2 | khuai24xuo0 ɕi21 | 快活 喜 |
| 0888 | 生气 |  | qi1 | tɕhi13 | 气 |
| 0889 | 责怪 |  | guai1 | kuai13 | 怪 |
| 0890 | 后悔 |  | huei2 | xuei21 | 悔 |
| 0891 | 忌妒 |  | ngan2yue0 | ŋan21Ǿye0 | 眼热 |
| 0892 | 害羞 |  | pa1cou2 | pha13tshou21 | 怕丑 |
| 0893 | 丢脸 |  | se1zen1 qu4cou2 | se13zən13 tɕhy24tshou21 | 折人 出丑 |
| 0894 | 欺负 |  | qi3 | tɕhi55 | 欺 |
| 0895 | 装 | ～病 | juan3 | tɕyan55 | 装 |
| 0896 | 疼 | ～小孩儿 | xin3tong0 | ɕin55thoŋ0 | 心痛 |
| 0897 | 要 | 我～这个 | yao1 | Ǿiau13 | 要 |
| 0898 | 有 | 我～一个孩子 | you2 | Ǿiou21 | 有 |
| 0899 | 没有 | 他～孩子 | mao5de4 | mau33te24 | 冇得 |
| 0900 | 是 | 我～老师 | si5 | sɿ33 | 是 |
| 0901 | 不是 | 他～老师 | bu4si5 | pu24sɿ33 | 不是 |
| 0902 | 在 | 他～家 | dao5 | tau33 | 到 |
| 0903 | 不在 | 他～家 他～家 | mao5dao5 bu4dao5 | mau33tau33 pu24tau33 | 冇到 不到 |
| 0904 | 知道 | 我～这件事 | xiao2den0 | ɕiau21tən0 | 晓得 |
| 0905 | 不知道 | 我～这件事 | bu4xiao2den0 | pu24ɕiau21tən0 | 不晓得 |
| 0906 | 懂 | 我～英语 | xiao2den0 | ɕiau21tən0 | 晓得 |
| 0907 | 不懂 | 我～英语 | bu4xiao2den0 | pu24ɕiau21tən0 | 不晓得 |
| 0908 | 会 | 我～开车 | xiao2den0 | ɕiau21tən0 | 晓得 |
| 0909 | 不会 | 我～开车 | bu4xiao2den0 | pu24ɕiau21tən0 | 不晓得 |
| 0910 | 认识 | 我～他 | zen5de0 | zən33te0 | 认得 |
| 0911 | 不认识 | 我～他 | bu4zen5de0 | pu24zən33te0 | 不认得 |
| 0912 | 行 | 应答语 | yao1de0 | Ǿiau13te0 | 要得 |
| 0913 | 不行 | 应答语 | yao1bu0de0 | Ǿiau13pu0te0 | 要不得 |
| 0914 | 肯 | ～来 | ken2 | khən21 | 肯 |
| 0915 | 应该 | ～去 | yin4dang0 | Ǿin24taŋ0 | 应当 |
| 0916 | 可以 | ～去 | kuo6yi2 | khuo22Ǿi21 | 可以 |
| 0917 | 说 | ～话 | gang2 | kaŋ21 | 讲 |
| 0918 | 话 | 说～ | hua5 | xua33 | 话 |
| 0919 | 聊天儿 |  | ca2be1hua5 | tsha21pe13xua33 | 扯白话 |
| 0920 | 叫 | ～他一声儿 | han2 | xan21 | 喊 |
| 0921 | 吆喝 | 大声喊 | han2 | xan21 | 喊 |
| 0922 | 哭 | 小孩～ | ku4 | khu24 | 哭 |
| 0923 | 骂 | 当面～人 | jue1 | tɕye13 | 噘 |
| 0924 | 吵架 | 动嘴：两个人在～ | cao2jia1 | tshau21tɕia13 | 吵架 |
| 0925 | 骗 | ～人 ～人 | ce4 huang4 | tshe24 xuaŋ24 | 测= 幌 |
| 0926 | 哄 | ～小孩 ～小孩 | huo3 hong2 | xuo55 xoŋ21 | 呵 哄 |
| 0927 | 撒谎 |  | ca2huang2 | tsha21xuaŋ21 | 扯谎 |
| 0928 | 吹牛 |  | gang2dai5hua5 | kaŋ21tai33xua33 | 讲大话 |
| 0929 | 拍马屁 |  | pe4ma2pi0 | phe24ma21phi0 | 拍马屁 |
| 0930 | 开玩笑 |  | kai3wan1xiao0 | khai55Ǿuan13ɕiau0 | 开玩笑 |
| 0931 | 告诉 | ～他 | gao4sen0 | kau24sən0 | 告诉 |
| 0932 | 谢谢 | 致谢语 | gan2xie0 | kan21ɕie0 | 感谢 |
| 0933 | 对不起 | 致歉语 | bu4hao2yi4si0 | pu24xau21Ǿi24sɿ0 | 不好意思 |
| 0934 | 再见 | 告别语 | sao2pei1 | sau21phei13 | 少陪 |
| 0935 | 大 | 苹果～ | dai5 | tai33 | 大 |
| 0936 | 小 | 苹果～ | xiao2 | ɕiau21 | 小 |
| 0937 | 粗 | 绳子～ | cou3 | tshou55 | 粗 |
| 0938 | 细 | 绳子～ | xi1 | ɕi13 | 细 |
| 0939 | 长 | 线～ | cang1 | tshaŋ13 | 长 |
| 0940 | 短 | 线～ | dan2 | tan21 | 短 |
| 0941 | 长 | 时间～ | jiou2 | tɕiou21 | 久 |
| 0942 | 短 | 时间～ | dan2 | tan21 | 短 |
| 0943 | 宽 | 路～ | kuan3 | khuan55 | 宽 |
| 0944 | 宽敞 | 房子～ | kuan3to0 | khuan55tho0 | 宽拓 |
| 0945 | 窄 | 路～ | ze4 | tse24 | 窄 |
| 0946 | 高 | 飞机飞得～ | gao3 | kau55 | 高 |
| 0947 | 低 | 鸟飞得～ | di3 | ti55 | 低 |
| 0948 | 高 | 他比我～ | gao3 | kau55 | 高 |
| 0949 | 矮 | 他比我～ | ngai2 | ŋai21 | 矮 |
| 0950 | 远 | 路～ | yuan2 | Ǿyan21 | 远 |
| 0951 | 近 | 路～ | jin5 | tɕin33 | 近 |
| 0952 | 深 | 水～ | sen3 | sən55 | 深 |
| 0953 | 浅 | 水～ | qian2 | tɕhiɛn21 | 浅 |
| 0954 | 清 | 水～ | qin3 | tɕhin55 | 清 |
| 0955 | 浑 | 水～ | fen3 | fən55 | 浑 |
| 0956 | 圆 |  | yuan1 | Ǿyan13 | 圆 |
| 0957 | 扁 |  | bian2 | piɛn21 | 扁 |
| 0958 | 方 |  | huang3 | xuaŋ55 | 方 |
| 0959 | 尖 |  | jian3 | tɕiɛn55 | 尖 |
| 0960 | 平 |  | pin1 | phin13 | 平 |
| 0961 | 肥 | ～肉 | huei1 | xuei13 | 肥 |
| 0962 | 瘦 | ～肉 | jin3 | tɕin55 | 精 |
| 0963 | 肥 | 形容猪等动物 | juang1 | tɕyaŋ13 | 壮 |
| 0964 | 胖 | 形容人 形容人 | juang1 pang4 | tɕyaŋ13 phaŋ24 | 壮 胖 |
| 0965 | 瘦 | 形容人、动物 形容人、动物 | nang3 sou1 | naŋ55 sou13 | 朖= 瘦 |
| 0966 | 黑 | 黑板的颜色 | he4 | xe24 | 黑 |
| 0967 | 白 | 雪的颜色 | be1 | pe13 | 白 |
| 0968 | 红 | 国旗的主颜色，统称 | hong1 | xoŋ13 | 红 |
| 0969 | 黄 | 国旗上五星的颜色 | wang1 | Ǿuaŋ13 | 黄 |
| 0970 | 蓝 | 蓝天的颜色 | nan1 | nan13 | 蓝 |
| 0971 | 绿 | 绿叶的颜色 | nou4 | nou24 | 绿 |
| 0972 | 紫 | 紫药水的颜色 | zi2 | tsɿ21 | 紫 |
| 0973 | 灰 | 草木灰的颜色 | huei3 | xuei55 | 灰 |
| 0974 | 多 | 东西～ | do3 | to55 | 多 |
| 0975 | 少 | 东西～ | sao2 | sau21 | 少 |
| 0976 | 重 | 担子～ | zong5 | tsoŋ33 | 重 |
| 0977 | 轻 | 担子～ | qin3 | tɕhin55 | 轻 |
| 0978 | 直 | 线～ | zi5 | tsɿ33 | 直 |
| 0979 | 陡 | 坡～，楼梯～ | dou2 | tou21 | 陡 |
| 0980 | 弯 | 弯曲：这条路是～的 | wan3 | Ǿuan55 | 弯 |
| 0981 | 歪 | 帽子戴～了 帽子戴～了 | qia1 pian3 | tɕhia13 phiɛn55 | 斜 偏 |
| 0982 | 厚 | 木板～ | hou5 | xou33 | 厚 |
| 0983 | 薄 | 木板～ | bo1 | po13 | 薄 |
| 0984 | 稠 | 稀饭～ | gan3 | kan55 | 干 |
| 0985 | 稀 | 稀饭～ | xi3 | ɕi55 | 稀 |
| 0986 | 密 | 菜种得～ | mi4 | mi24 | 密 |
| 0987 | 稀 | 稀疏：菜种得～ | xi3 | ɕi55 | 稀 |
| 0988 | 亮 | 指光线，明亮 | niang5 | niaŋ33 | 亮 |
| 0989 | 黑 | 指光线，完全看不见 | qu3he0 | tɕhy55xe0 | 黜黑 |
| 0990 | 热 | 天气 | yue4 | Ǿye24 | 热 |
| 0991 | 暖和 | 天气 | yue4huo0 | Ǿye24xuo0 | 热和 |
| 0992 | 凉 | 天气 | niang1 | niaŋ13 | 凉 |
| 0993 | 冷 | 天气 | nen2 | nən21 | 冷 |
| 0994 | 热 | 水 | yue4 | Ǿye24 | 热 |
| 0995 | 凉 | 水 | nen2 | nən21 | 冷 |
| 0996 | 干 | 干燥：衣服晒～了 | gan3 | kan55 | 干 |
| 0997 | 湿 | 潮湿：衣服淋～了 | si4 | sɿ24 | 湿 |
| 0998 | 干净 | 衣服～ | so4ni0 | so24ni0 | 索=里= |
| 0999 | 脏 | 肮脏，不干净，统称：衣服～ | nai3tai0 | nai55thai0 | 邋遢 |
| 1000 | 快 | 锋利：刀子～ | kuai1 | khuai13 | 快 |
| 1001 | 钝 | 刀～ 刀～ | bu4kuai1 den5 | pu24khuai13 tən33 | 不快 钝 |
| 1002 | 快 | 坐车比走路～ | kuai1 | khuai13 | 快 |
| 1003 | 慢 | 走路比坐车～ | man5 | man33 | 慢 |
| 1004 | 早 | 来得～ | zao2 | tsau21 | 早 |
| 1005 | 晚 | 来～了 | ci1 | tshɿ13 | 迟 |
| 1006 | 晚 | 天色～ | ya5 | Ǿia33 | 夜 |
| 1007 | 松 | 捆得～ | song3 | soŋ55 | 松 |
| 1008 | 紧 | 捆得～ | jin2 | tɕin21 | 紧 |
| 1009 | 容易 | 这道题～ | yong1yi0 | Ǿioŋ13Ǿi0 | 容易 |
| 1010 | 难 | 这道题～ | nan1 | nan13 | 难 |
| 1011 | 新 | 衣服～ | xin3 | ɕin55 | 新 |
| 1012 | 旧 | 衣服～ | jiou5 | tɕiou33 | 旧 |
| 1013 | 老 | 人～ | nao2 | nau21 | 老 |
| 1014 | 年轻 | 人～ | nian1qin3 | niɛn13tɕhin55 | 年轻 |
| 1015 | 软 | 糖～ | yuan2 | Ǿyan21 | 软 |
| 1016 | 硬 | 骨头～ | ngen5 | ŋən33 | 硬 |
| 1017 | 烂 | 肉煮得～ | nan5 | nan33 | 烂 |
| 1018 | 煳 | 饭烧～了 | hei4 | xei24 | 黑 |
| 1019 | 结实 | 家具～ | za4si0 | tsa24sɿ0 | 扎实 |
| 1020 | 破 | 衣服～ | nan5 | nan33 | 烂 |
| 1021 | 富 | 他家很～ | fu4zou0 | fu24tsou0 | 富足 |
| 1022 | 穷 | 他家很～ | qiong1 | tɕhioŋ13 | 穷 |
| 1023 | 忙 | 最近很～ | mang1 | maŋ13 | 忙 |
| 1024 | 闲 | 最近比较～ | de4kong1 | te24khoŋ13 | 得空 |
| 1025 | 累 | 走路走得很～ | qi4kuei3 | tɕhi24khuei55 | 吃亏 |
| 1026 | 疼 | 摔～了 | tong1 | thoŋ13 | 痛 |
| 1027 | 痒 | 皮肤～ | yang2 | Ǿiaŋ21 | 痒 |
| 1028 | 热闹 | 看戏的地方很～ | yue4nao0 | Ǿye24nau0 | 热闹 |
| 1029 | 熟悉 | 这个地方我很～ | sou1 | sou13 | 熟 |
| 1030 | 陌生 | 这个地方我很～ | bu4sou1 | pu24sou13 | 不熟 |
| 1031 | 味道 | 尝尝～ | wei5dao0 | Ǿuei33tau0 | 味道 |
| 1032 | 气味 | 闻闻～ 闻闻～ | wei5dao0 qi1si5 | Ǿuei33tau0 tɕhi13sɿ33 | 味道 气势 |
| 1033 | 咸 | 菜～ | han1 | xan13 | 咸 |
| 1034 | 淡 | 菜～ | dan5 | tan33 | 淡 |
| 1035 | 酸 |  | xuan3 | ɕyan55 | 酸 |
| 1036 | 甜 |  | tian1 | thiɛn13 | 甜 |
| 1037 | 苦 |  | ku2 | khu21 | 苦 |
| 1038 | 辣 |  | na4 | na24 | 辣 |
| 1039 | 鲜 | 鱼汤～ | xian3 | ɕiɛn55 | 鲜 |
| 1040 | 香 |  | xiang3 | ɕiaŋ55 | 香 |
| 1041 | 臭 |  | cou1 | tshou13 | 臭 |
| 1042 | 馊 | 饭～ | sai3 | sai55 | 馊 |
| 1043 | 腥 | 鱼～ | xin3 | ɕin55 | 腥 |
| 1044 | 好 | 人～ | hao2 | xau21 | 好 |
| 1045 | 坏 | 人～ | huai5 | xuai33 | 坏 |
| 1046 | 差 | 东西质量～ | ca3 | tsha55 | 差 |
| 1047 | 对 | 账算～了 | dei1 | tei13 | 对 |
| 1048 | 错 | 账算～了 | co1 | tsho13 | 错 |
| 1049 | 漂亮 | 形容年轻女性的长相：她很～ | guai3 | kuai55 | 乖 |
| 1050 | 丑 | 形容人的长相：猪八戒很～ | cou2 | tshou21 | 丑 |
| 1051 | 勤快 |  | qiong1kuai0 | tɕhioŋ13khuai0 | 勤快 |
| 1052 | 懒 |  | nan2 | nan21 | 懒 |
| 1053 | 乖 |  | guai3 | kuai55 | 乖 |
| 1054 | 顽皮 |  | tiao1pi1 | thiau13phi13 | 调皮 |
| 1055 | 老实 |  | nao2si0 | nau21sɿ0 | 老实 |
| 1056 | 傻 | 痴呆 | sai2 | sai21 | 傻 |
| 1057 | 笨 | 蠢 | qun2 | tɕhyn21 | 蠢 |
| 1058 | 大方 | 不吝啬 | dai5fang0 | tai33faŋ0 | 大方 |
| 1059 | 小气 | 吝啬 | xiao2qi0 | ɕiau21tɕhi0 | 小气 |
| 1060 | 直爽 | 性格～ | zi1 | tsɿ13 | 直 |
| 1061 | 犟 | 脾气～ | jiang5 | tɕiaŋ33 | 犟 |
| 1062 | 一 | ～二三四五……，下同 | yi4 | Ǿi24 | 一 |
| 1063 | 二 |  | er5 | Ǿɚ33 | 二 |
| 1064 | 三 |  | san3 | san55 | 三 |
| 1065 | 四 |  | si1 | sɿ13 | 四 |
| 1066 | 五 |  | wu2 | Ǿu21 | 五 |
| 1067 | 六 |  | nou4 | nou24 | 六 |
| 1068 | 七 |  | qi4 | tɕhi24 | 七 |
| 1069 | 八 |  | ba4 | pa24 | 八 |
| 1070 | 九 |  | jiou2 | tɕiou21 | 九 |
| 1071 | 十 |  | yi4pao1 | Ǿi24phau13 | 一炮= |
| 1072 | 二十 | 有无合音 | er5si5 | Ǿɚ33sɿ33 | 二十 |
| 1073 | 三十 | 有无合音 | san3si5 | san55sɿ33 | 三十 |
| 1074 | 一百 |  | yi4be4 | Ǿi24pe24 | 一百 |
| 1075 | 一千 |  | yi4qian3 | Ǿi24tɕhiɛn55 | 一千 |
| 1076 | 一万 |  | yi4wan5 | Ǿi24Ǿuan33 | 一万 |
| 1077 | 一百零五 |  | yi4be4nin1wu2 | Ǿi24pe24nin13Ǿu21 | 一百零五 |
| 1078 | 一百五十 |  | yi4be4wu2 | Ǿi24pe24Ǿu21 | 一百五 |
| 1079 | 第一 | ～，第二 | di5yi4 | ti33Ǿi24 | 第一 |
| 1080 | 二两 | 重量 | er5niang2 | Ǿɚ33niaŋ21 | 二两 |
| 1081 | 几个 | 你有～孩子？ | ji2ze4 | tɕi21tse24 | 几只 |
| 1082 | 俩 | 你们～ | niang2guo0 | niaŋ21kuo0 | 两个 |
| 1083 | 仨 | 你们～ | san5guo0 | san33kuo0 | 三个 |
| 1084 | 个把 |  | ze4ba2 | tse24pa21 | 只把 |
| 1085 | 个 | 一～人 | ze4 | tse24 | 只 |
| 1086 | 匹 | 一～马 一～马 | ze4 pi1 | tse24 phi13 | 只 匹 |
| 1087 | 头 | 一～牛 一～牛 | ze4 tou1 | tse24 thou13 | 只 头 |
| 1088 | 头 | 一～猪 一～猪 | ze4 tou1 | ʦe24 thou13 | 只 头 |
| 1089 | 只 | 一～狗 一～狗 | ze4 tiao1 | tse24 thiau13 | 只 条 |
| 1090 | 只 | 一～鸡 | ze4 | tse24 | 只 |
| 1091 | 只 | 一～蚊子 | ze4 | tse24 | 只 |
| 1092 | 条 | 一～鱼 | tiao1 | thiau13 | 条 |
| 1093 | 条 | 一～蛇 | tiao1 | thiau13 | 条 |
| 1094 | 张 | 一～嘴 一～嘴 | ze4 zang3 | tse24 tsaŋ55 | 只 张 |
| 1095 | 张 | 一～桌子 | zang3 | tsaŋ55 | 张 |
| 1096 | 床 | 一～被子 | quang1 | tɕhyaŋ13 | 床 |
| 1097 | 领 | 一～席子 | quang1 | tɕhyaŋ13 | 床 |
| 1098 | 双 | 一～鞋 | xuang3 | ɕyaŋ55 | 双 |
| 1099 | 把 | 一～刀 | ba2 | pa21 | 把 |
| 1100 | 把 | 一～锁 | ba2 | pa21 | 把 |
| 1101 | 根 | 一～绳子 | gen3 | kən55 | 根 |
| 1102 | 支 | 一～毛笔 | zi3 | tsɿ55 | 支 |
| 1103 | 副 | 一～眼镜 | fu4 | fu24 | 副 |
| 1104 | 面 | 一～镜子 | kuai2 | khuai21 | 块 |
| 1105 | 块 | 一～香皂 一～香皂 | to1 kuai2 | tho13 khuai21 | 坨 块 |
| 1106 | 辆 | 一～车 | niang2 | niaŋ21 | 辆 |
| 1107 | 座 | 一～房子 | dong5 | toŋ33 | 栋 |
| 1108 | 座 | 一～桥 | zo5 | tso33 | 座 |
| 1109 | 条 | 一～河 | tiao1 | thiau13 | 条 |
| 1110 | 条 | 一～路 | tiao1 | thiau13 | 条 |
| 1111 | 棵 | 一～树 | kuo2 | khuo21 | 棵 |
| 1112 | 朵 | 一～花 | do2 | to21 | 朵 |
| 1113 | 颗 | 一～珠子 一～珠子 | ze4 ni4 | tse24 ni24 | 只 粒 |
| 1114 | 粒 | 一～米 | ni4 | ni24 | 粒 |
| 1115 | 顿 | 一～饭 | can3 | tshan55 | 餐 |
| 1116 | 剂 | 一～中药 | hu4 | xu24 | 付 |
| 1117 | 股 | 一～香味 | gu2 | ku21 | 股 |
| 1118 | 行 | 一～字 | hang1 | xaŋ13 | 行 |
| 1119 | 块 | 一～钱 | kuai2 | khuai21 | 块 |
| 1120 | 毛 | 角：一～钱 | jio4 | tɕio24 | 角 |
| 1121 | 件 | 一～事情 一～事情 | ze4 jian5 | tse24 tɕiɛn33 | 只 件 |
| 1122 | 点儿 | 一～东西 一～东西 | dian4dier0 di3dier0 | tiɛn24tiɚ0 ti55tiɚ0 | 点点儿 滴滴儿 |
| 1123 | 些 | 一～东西 | xie3 | ɕie55 | 些 |
| 1124 | 下 | 打一～，动量，不是时量 | ha5 | xa33 | 下 |
| 1125 | 会儿 | 坐了一～ 坐了一～ | ha2her0 ha3her0 | xa21xɚ0 xa55xɚ0 | 下下儿 下下儿 |
| 1126 | 顿 | 打一～ | dao1 | tau13 | 道 |
| 1127 | 阵 | 下了一～雨 下了一～雨 | ha2her0 ha3her0 | xa21xɚ0 xa55xɚ0 | 下下儿 下下儿 |
| 1128 | 趟 | 去了一～ 去了一～ | nou5 huei1 | nou33 xuei13 | 路 回 |
| 1129 | 我 | ～姓王 | wo2 | Ǿuo21 | 我 |
| 1130 | 你 | ～也姓王 | ni2 | ni21 | 你 |
| 1131 | 您 | 尊称 | ni2er0 | ni21Ǿɚ0 | 你儿 |
| 1132 | 他 | ～姓张 | ta3 | tha55 | 他 |
| 1133 | 我们 | 不包括听话人：你们别去，～去 | wan1 | Ǿuan13 | 顽= |
| 1134 | 咱们 | 包括听话人：他们不去，～去吧 | wan1 | Ǿuan13 | 顽= |
| 1135 | 你们 | ～去 | nian1 | niɛn13 | 你安= |
| 1136 | 他们 | ～去 | ta3ngan0 | tha55ŋan0 | 他安= |
| 1137 | 大家 | ～一起干 | wan1 | Ǿuan13 | 顽= |
| 1138 | 自己 | 我～做的 | zi5ga2 | tsɿ33ka21 | 自家 |
| 1139 | 别人 | 这是～的 | bie1guo0 | pie13kuo0 | 别个 |
| 1140 | 我爸 | ～今年八十岁 ～今年八十岁 | wan1die3die0 wan1nao2guan0de0 | Ǿuan13tie55tie0 Ǿuan13nau21kuan0te0 | 顽=爹爹 顽=佬倌嘚 |
| 1141 | 你爸 | ～在家吗？ ～在家吗？ | nian1die3die0 nian1nao2guan0de0 | niɛn13tie55tie0 niɛn13nau21kuan0te0 | 你安=爹爹 你安=佬倌嘚 |
| 1142 | 他爸 | ～去世了 ～去世了 | ta3die3die0 ta3nao2guan0de0 | tha55tie55tie0 tha55nau21kuan0te0 | 他爹爹 他老倌嘚 |
| 1143 | 这个 | 我要～，不要那个 | ze1guo0 | tse13kuo0 | 这个 |
| 1144 | 那个 | 我要这个，不要～ | nuo4guo0 | nuo24kuo0 | 那个 |
| 1145 | 哪个 | 你要～杯子？ 你要～杯子？ | huo4ze0 huo4guo0 | xuo24tse0 xuo24kuo0 | 何只 何个 |
| 1146 | 谁 | 你找～？ | huo4guo0 | xuo24kuo0 | 何个 |
| 1147 | 这里 | 在～，不在那里 | da1ni0 | ta13ni0 | 达=里 |
| 1148 | 那里 | 在这里，不在～ | nuo5ni0 | nuo33ni0 | 那里 |
| 1149 | 哪里 | 你到～去？ | huo5ni0 | xuo33ni0 | 何里 |
| 1150 | 这样 | 事情是～的，不是那样的 | dang1nger0 | taŋ13ŋɚ0 | #16儿 |
| 1151 | 那样 | 事情是这样的，不是～的 | gong1nger0 | koŋ13ŋɚ0 | #17儿 |
| 1152 | 怎样 | 什么样：你要～的？ | hong1nger0 | xoŋ13ŋɚ0 | #18儿 |
| 1153 | 这么 | ～贵啊 | dang1nger0 | taŋ13ŋɚ0 | #16儿 |
| 1154 | 怎么 | 这个字～写？ | hong1nger0 | xoŋ13ŋɚ0 | #18儿 |
| 1155 | 什么 | 这个是～字？ | mo2de0 | mo21te0 | 么嘚 |
| 1156 | 什么 | 你找～？ | mo2de0 | mo21te0 | 么嘚 |
| 1157 | 为什么 | 你～不去？ | wei5mo2de0 | Ǿuei33mo21te0 | 为么嘚 |
| 1158 | 干什么 | 你在～？ | gao2mo2de0 | kau21mo21te0 | 搞么嘚 |
| 1159 | 多少 | 这个村有～人？ | hao2do0 | xau21to0 | 好多 |
| 1160 | 很 | 今天～热 | man1 | man13 | 蛮 |
| 1161 | 非常 | 比上条程度深：今天～热 | he3man0 | xe55man0 | 黑=蛮 |
| 1162 | 更 | 今天比昨天～热 | hai1 | xai13 | 还 |
| 1163 | 太 | 这个东西～贵，买不起 | tai4 | thai24 | 太 |
| 1164 | 最 | 弟兄三个中他～高 | zei4 | tsei24 | 最 |
| 1165 | 都 | 大家～来了 | dou3 | tou55 | 都 |
| 1166 | 一共 | ～多少钱？ | yi4qi2 | Ǿi24tɕhi21 | 一起 |
| 1167 | 一起 | 我和你～去 | yi4nou5 | Ǿi24nou33 | 一路 |
| 1168 | 只 | 我～去过一趟 | zi4 | tsɿ24 | 只 |
| 1169 | 刚 | 这双鞋我穿着～好 | gang3gang0 | kaŋ55kaŋ0 | 刚刚 |
| 1170 | 刚 | 我～到 | jiang3zi0 | tɕiaŋ55tsɿ0 | 将只 |
| 1171 | 才 | 你怎么～来啊？ | cai1zi0 | tshai13tsɿ0 | 才只 |
| 1172 | 就 | 我吃了饭～去 | jiou5 | tɕiou33 | 就 |
| 1173 | 经常 | 我～去 | yao1si0ga0 | Ǿiau13sɿ0ka0 | 要时嘎 |
| 1174 | 又 | 他～来了 | you5 | Ǿiou33 | 又 |
| 1175 | 还 | 他～没回家 | hai1 | xai13 | 还 |
| 1176 | 再 | 你明天～来 | zai4 | tsai24 | 再 |
| 1177 | 也 | 我～去；我～是老师 | ya2 | Ǿia21 | 也 |
| 1178 | 反正 | 不用急，～还来得及 | fan2zen0 | fan21tsən0 | 反正 |
| 1179 | 没有 | 昨天我～去 | mao5 | mau33 | 冇 |
| 1180 | 不 | 明天我～去 | bu4 | pu24 | 不 |
| 1181 | 别 | 你～去 | mo4 | mo24 | 莫 |
| 1182 | 甭 | 不用，不必：你～客气 | mo4 | mo24 | 莫 |
| 1183 | 快 | 天～亮了 | kuai1dang0 | khuai13taŋ0 | 快当 |
| 1184 | 差点儿 | ～摔倒了 | ca3dian2dier0 | tsha55tiɛn21tiɚ0 | 差点点儿 |
| 1185 | 宁可 | ～买贵的 | nen1yuan0 | nən13Ǿyan0 | 宁愿 |
| 1186 | 故意 | ～打破的 | ban5ma2zi0 | pan33ma21tsɿ0 | 办=码=子 |
| 1187 | 随便 | ～弄一下 | guan2ta3di0 | kuan21tha55ti0 | 管它的 |
| 1188 | 白 | ～跑一趟 | yuan3wang2 | Ǿyan55Ǿuaŋ21 | 冤枉 |
| 1189 | 肯定 | ～是他干的 ～是他干的 | jue4dei0 ken2din0 | tɕye24tei0 khən21tin0 | 绝对 肯定 |
| 1190 | 可能 | ～是他干的 | you2kuo2nen1 | Ǿiou21khuo21nən13 | 有可能 |
| 1191 | 一边 | ～走，～说 | yi4nou5 | Ǿi24nou33 | 一路 |
| 1192 | 和 | 我～他都姓王 | niang2guo0 | niaŋ21kuo0 | 两个 |
| 1193 | 和 | 我昨天～他去城里了 | niang2guo0 | niaŋ21kuo0 | 两个 |
| 1194 | 对 | 他～我很好 | dei4 | tei24 | 对 |
| 1195 | 往 | ～东走 | wang2 | Ǿuaŋ21 | 往 |
| 1196 | 向 | ～他借一本书 | zao2 | tsau21 | 找 |
| 1197 | 按 | ～他的要求做 | zao1 | ʦau13 | 照 |
| 1198 | 替 | ～他写信 ～他写信 | gen3 bang3 | kən55 paŋ55 | 跟 帮 |
| 1199 | 如果 | ～忙你就别来了 | yao1si0 | Ǿiau13sɿ0 | 要是 |
| 1200 | 不管 | ～怎么劝他都不听 | bu4guan2 | pu24kuan21 | 不管 |
