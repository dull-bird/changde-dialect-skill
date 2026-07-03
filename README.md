# changde-dialect-skill

用常德话（湖南常德方言）跟 AI 对话的 Agent Skill + 关键词开关钩子，**Claude Code、Codex、OpenClaw 三个工具都验证跑通**。

🌐 网页介绍：https://dull-bird.github.io/changde-dialect-skill/

底子是《常德方言词语汇1000》（水兵1986编，[美篇原文](https://www.meipian.cn/m5r5mum)），994 条日常词条 + 151 条桃源本地歇后语，全部按语义分类整理成机器可查的参考文件。

```
你：说常德话，你好
AI：好啵！俺今朝刚上线，你就来哒。有么得事要搞，你港给俺听斗起？

你：好了，说普通话吧
AI：好的，已经切回普通话了！有什么可以帮你的？
```

## 这是什么

一个标准的 Agent Skills（`SKILL.md` + 参考文件）包，装进对应工具的 skills 目录后，说"说常德话"就会触发；说"说普通话"退出。**三个工具各自都有一个关键词开关钩子**（不是靠模型自己猜），按 session 记录开关状态，说一次触发词就一直保持到你说退出为止——这三个钩子的实现分别用了各工具原生的钩子机制，并且都经过真实调用测试确认生效（不是纸面设计）：

| 工具 | 钩子机制 | 验证方式 |
|---|---|---|
| Claude Code | `~/.claude/settings.json` 的 `UserPromptSubmit` hook（Python） | 手动 pipe 测试开/关/持久化/多会话隔离 |
| Codex | `~/.codex/config.toml` 的 `[[hooks.UserPromptSubmit]]`（同一个 Python 脚本） | `codex exec` 真实跑通，日志里能看到 `hook: UserPromptSubmit` |
| OpenClaw | `~/.openclaw/hooks/` 下的 `HOOK.md` + `handler.ts`（`message:received` + `agent:bootstrap` 两个事件） | `openclaw agent --local` 真实跑通，开/关/持久化全部验证 |

- **词汇分类**：称谓/人称（120）、动植物名称（78）、农具生活用具（46）、身体部位（32）、时间方位（13）、民俗礼仪与丧葬文化（22）、骂人贬损粗语（24+）、桃源本地歇后语（151）、其余日常动词/程度词/俗语（约508）
- **语法核心**：了→哒，讲→港，去→克，看到→看斗，我→俺，很→几得，什么→么得，自己→各人……详见 `skills/changde-dialect/SKILL.md`

## 安装

三种方式，前两种能装上技能 + 确定性开关钩子，第三种只装技能本身。

### ① 让 AI agent 自动装（技能 + 钩子）

把下面这段发给 Claude Code / Codex / OpenClaw：

```text
请帮我安装 changde-dialect 这个常德话 Agent Skill：
1. 克隆 https://github.com/dull-bird/changde-dialect-skill
2. 运行 ./install.sh，把 skills/changde-dialect 装到本机检测到的
   Claude Code / Codex / OpenClaw 的 skills 目录
3. 如果我用 Claude Code，运行 claude-code/install-hook.sh 注册关键词开关钩子
4. 如果我用 Codex，运行 codex/install-hook.sh（首次可能要批准 hook trust；
   非交互场景可以加 --dangerously-bypass-hook-trust，但这是 DANGEROUS 选项，
   装之前跟我确认一下）
5. 如果我用 OpenClaw，运行 openclaw/install-hook.sh
6. 装完后跟我说"说常德话"确认效果，测试完再说"说普通话"退出
```

### ② 手动 clone + install.sh（技能 + 钩子）

```bash
git clone https://github.com/dull-bird/changde-dialect-skill.git
cd changde-dialect-skill
./install.sh                    # 自动探测 ~/.claude、~/.codex、~/.openclaw，装好技能
./claude-code/install-hook.sh   # 可选：注册到 ~/.claude/settings.json
./codex/install-hook.sh         # 可选：注册到 ~/.codex/config.toml
./openclaw/install-hook.sh      # 可选：装到 ~/.openclaw/hooks/ 并 openclaw hooks enable
```

技能安装位置：

| 工具 | 技能安装位置 |
|---|---|
| Claude Code | `~/.claude/skills/changde-dialect` |
| Codex | `~/.codex/skills/changde-dialect` |
| OpenClaw | `~/.openclaw/skills/changde-dialect`（全局，所有 agent 共用） |

所有脚本都是幂等的，重复跑不会重复注册或破坏你已有的配置。

**Codex 用户注意**：hook 有个"hook trust"机制，交互式使用时首次可能需要批准；全自动/非交互场景可以加 `--dangerously-bypass-hook-trust`（官方标注 DANGEROUS，谨慎使用，仅在你信任 hook 来源时开）。

### ③ `npx skills` 一键装（仅技能，不含钩子）

实测 [skills.sh](https://skills.sh) 的通用安装器能正确识别并装好 `skills/changde-dialect`，自动适配 Claude Code / Codex / Cursor / OpenClaw 等 70 余个 agent：

```bash
npx skills add dull-bird/changde-dialect-skill
```

它只拷贝技能文件（复制/软链接到各工具的 skills 目录），**不会**帮你注册 `claude-code/`、`codex/`、`openclaw/` 下的确定性开关钩子——想要钩子还是走①或②。没装钩子时，触发依然可以工作，只是退化成模型自己识别技能描述里的关键词，没有强制的按会话状态锁定。

### 手动安装

不想跑脚本的话，直接把 `skills/changde-dialect/` 拷到对应工具的 skills 目录，钩子部分参考 `claude-code/settings-snippet.json`、`codex/config-snippet.toml`、`openclaw/hooks/changde-dialect-toggle/` 手动合并。

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
├── install.sh                          # 一键装技能到检测到的所有工具
├── skills/changde-dialect/
│   ├── SKILL.md                        # 技能定义：语法、高频词表、使用边界
│   ├── references/glossary.md          # 完整分类词表（994 条 + 151 条歇后语）
│   └── scripts/dialect_hook.py         # Claude Code / Codex 共用的开关钩子脚本
├── claude-code/
│   ├── install-hook.sh / install_hook.py
│   └── settings-snippet.json
├── codex/
│   ├── install-hook.sh / install_hook.py
│   └── config-snippet.toml
└── openclaw/
    ├── install-hook.sh
    └── hooks/changde-dialect-toggle/
        ├── HOOK.md
        └── handler.ts                  # message:received 记状态，agent:bootstrap 注入提醒
```

## 为什么三个工具能共用一份 SKILL.md，钩子却要分开写

Claude Code、Codex、OpenClaw 都支持同一种 Agent Skills 约定（`name` + `description` frontmatter 的 `SKILL.md`，模型根据 `description` 里的触发词自行判断何时调用），所以一份 skill 三边通用。

但三家的**钩子事件模型和运行时不一样**：Claude Code 和 Codex 都有 `UserPromptSubmit` 事件、都用 JSON stdin/stdout 的 command hook，所以能共用同一个 `dialect_hook.py`；OpenClaw 的 hook 是 TypeScript/Node 写的，事件模型也不同（没有直接对应"用户提交消息"的事件，而是 `message:received`——记录状态——配合 `agent:bootstrap`——注入 bootstrap 内容里），所以单独写了一份 `handler.ts`，用的是 OpenClaw 真实的内部类型定义（`AgentBootstrapHookContext.bootstrapFiles`、`MessageReceivedHookContext.content`），照着它自带的 `bootstrap-extra-files` 内置钩子源码抄的模式。

## 致谢与出处

方言词汇内容整理自水兵1986发布于美篇的[《常德方言词语汇1000》](https://www.meipian.cn/m5r5mum)，原作者在文末注明"欢迎修订补充完善"。本仓库据此邀请重新整理、结构化并附上分类和用法说明。如果你是原作者或对内容使用有疑问，欢迎提 issue。

欢迎补充词条、修正释义、纠正分类，或者给三个工具之外的其它 agent 框架补上等价的钩子。

## License

MIT，词表内容附带来源声明，见 [LICENSE](LICENSE)。
