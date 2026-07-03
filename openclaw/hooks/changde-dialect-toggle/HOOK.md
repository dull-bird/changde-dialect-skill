---
name: changde-dialect-toggle
description: "关键词开关：说'说常德话'时让 agent 用常德方言回应，说'说普通话'时恢复"
homepage: https://github.com/dull-bird/changde-dialect-skill
metadata:
  {
    "openclaw":
      {
        "emoji": "🗣️",
        "events": ["message:received", "agent:bootstrap"],
        "install": [{ "id": "bundled", "kind": "bundled", "label": "changde-dialect-skill" }],
      },
  }
---

# 常德话关键词开关钩子

配合 [changde-dialect skill](https://github.com/dull-bird/changde-dialect-skill) 使用。

- `message:received`：检测入站消息里的"说常德话/退出方言"等关键词，按 `sessionKey` 记录开关状态到 `state/<sessionKey>.json`。
- `agent:bootstrap`：如果该 session 的方言模式已开启，往 bootstrap 内容里追加常德话使用提醒（改写已存在的 bootstrap 文件内容，不新增文件名，因为 `bootstrapFiles` 的 `name` 只能是固定的几个 basename）。

## 启用

```bash
openclaw hooks enable changde-dialect-toggle
```
