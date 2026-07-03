# changde-dialect-skill

用常德话（湖南常德方言）跟 AI 对话的 Agent Skill，同时兼容 **Claude Code**、**Codex**、**OpenClaw**。

底子是《常德方言词语汇1000》（水兵1986编，[美篇原文](https://www.meipian.cn/m5r5mum)），994 条日常词条 + 151 条桃源本地歇后语，全部按语义分类整理成机器可查的参考文件。

```
你：说常德话，帮我看看今天该干哈子
AI：好啵！你搞快些港下你今朝有么得事要搞，俺帮你理一哈。
    莫急，一样一样来，搞归一哒就轻松哒。
```

## 这是什么

一个标准的 [Agent Skills](https://docs.openclaw.ai/tools/creating-skills)（`SKILL.md` + 参考文件）包，装进对应工具的 skills 目录后，说"说常德话"就会触发；说"说普通话"退出。

- **词汇分类**：称谓/人称（120）、动植物名称（78）、农具生活用具（46）、身体部位（32）、时间方位（13）、民俗礼仪与丧葬文化（22）、骂人贬损粗语（24+）、桃源本地歇后语（151）、其余日常动词/程度词/俗语（约508）
- **语法核心**：了→哒，讲→港，去→克，看到→看斗，我→俺，很→几得，什么→么得，自己→各人……详见 `skills/changde-dialect/SKILL.md`
- **Claude Code 专属增强**：一个 UserPromptSubmit 钩子，按会话做确定性的关键词开关 + 状态持久化（Codex / OpenClaw 目前没有等价的通用钩子机制，激活依赖模型自己识别触发词，效果接近，只是没有强制状态锁定）

## 安装

```bash
git clone https://github.com/dull-bird/changde-dialect-skill.git
cd changde-dialect-skill
./install.sh
```

`install.sh` 会自动探测本机装了哪些工具（`~/.claude`、`~/.codex`、`~/.openclaw`），把 `skills/changde-dialect` 拷贝到对应的 skills 目录：

| 工具 | 安装位置 |
|---|---|
| Claude Code | `~/.claude/skills/changde-dialect` |
| Codex | `~/.codex/skills/changde-dialect` |
| OpenClaw | `~/.openclaw/skills/changde-dialect`（全局，所有 agent 共用） |

**Claude Code 用户**：想要"说常德话"后自动锁定方言模式直到你说"说普通话"，额外跑一下：

```bash
./claude-code/install-hook.sh
```

这会把钩子注册进 `~/.claude/settings.json`，脚本是幂等的，不会覆盖你已有的其它 hooks。如果不想装钩子，跳过这一步也没关系——技能本身照样能被模型按描述语义触发。

### 手动安装

不想跑脚本的话，直接把 `skills/changde-dialect/` 整个文件夹拷到对应工具的 skills 目录下即可，例如：

```bash
cp -r skills/changde-dialect ~/.claude/skills/
cp -r skills/changde-dialect ~/.codex/skills/
cp -r skills/changde-dialect ~/.openclaw/skills/
```

## 用法

| 说这句话 | 效果 |
|---|---|
| 说常德话 / 讲常德话 / 切换方言 / 开启方言模式 | 开启方言对话 |
| 退出方言 / 说普通话 / 切回普通话 / 关闭方言模式 | 恢复普通话 |
| "XX方言是什么意思" | 查词条，不用整段切方言 |

代码、命令、报错等技术性输出不会被方言化，只影响自然语言对话部分。骂人/粗语词条只用于轻度打趣或用户主动询问词义，不用来真正冒犯人。

## 目录结构

```
changde-dialect-skill/
├── install.sh                    # 一键装到检测到的所有工具
├── skills/changde-dialect/
│   ├── SKILL.md                  # 技能定义：语法、高频词表、使用边界
│   ├── references/glossary.md    # 完整分类词表（994 条 + 151 条歇后语）
│   ├── scripts/dialect_hook.py   # Claude Code 关键词开关钩子
│   └── state/                    # 钩子按 session 记录开关状态（运行时生成，不提交）
└── claude-code/
    ├── install-hook.sh           # 把钩子注册进 ~/.claude/settings.json
    ├── install_hook.py
    └── settings-snippet.json     # 钩子配置示例，供手动合并参考
```

## 为什么三个工具能共用一份 SKILL.md

Claude Code、Codex、OpenClaw 都支持同一种 Agent Skills 约定（`name` + `description` frontmatter 的 `SKILL.md`，模型根据 `description` 里的触发词自行判断何时调用）。这份 skill 就是按这个共同标准写的，装进任意一个工具的 skills 目录都能被原生识别，不需要为每个工具各写一套。Claude Code 额外有一套通用的 hooks 机制（`UserPromptSubmit` 等事件钩子），所以这里多提供了一个可选的确定性开关钩子；Codex 和 OpenClaw 目前没有对外暴露等价的通用钩子接口，欢迎 PR 补上。

## 致谢与出处

方言词汇内容整理自水兵1986发布于美篇的[《常德方言词语汇1000》](https://www.meipian.cn/m5r5mum)，原作者在文末注明"欢迎修订补充完善"。本仓库据此邀请重新整理、结构化并附上分类和用法说明。如果你是原作者或对内容使用有疑问，欢迎提 issue。

欢迎补充词条、修正释义、纠正分类，或者给 Codex / OpenClaw 补上等价的自动开关钩子。

## License

MIT，词表内容附带来源声明，见 [LICENSE](LICENSE)。
