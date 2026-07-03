#!/usr/bin/env python3
"""Idempotently register the changde-dialect UserPromptSubmit hook in
~/.claude/settings.json without clobbering existing hooks/settings."""
import json
import os
import sys

SETTINGS_PATH = os.path.expanduser("~/.claude/settings.json")
HOOK_COMMAND = "python3 " + os.path.expanduser(
    "~/.claude/skills/changde-dialect/scripts/dialect_hook.py"
)
MARKER = "changde-dialect/scripts/dialect_hook.py"


def main() -> int:
    if os.path.exists(SETTINGS_PATH):
        with open(SETTINGS_PATH, encoding="utf-8") as f:
            settings = json.load(f)
    else:
        settings = {}

    hooks = settings.setdefault("hooks", {})
    prompt_hooks = hooks.setdefault("UserPromptSubmit", [])

    for block in prompt_hooks:
        for h in block.get("hooks", []):
            if MARKER in h.get("command", ""):
                print("已经注册过哒，冒得重复添加。")
                return 0

    if prompt_hooks and "matcher" not in prompt_hooks[0]:
        prompt_hooks[0].setdefault("hooks", []).append(
            {"type": "command", "command": HOOK_COMMAND}
        )
    else:
        prompt_hooks.append(
            {"hooks": [{"type": "command", "command": HOOK_COMMAND}]}
        )

    os.makedirs(os.path.dirname(SETTINGS_PATH), exist_ok=True)
    with open(SETTINGS_PATH, "w", encoding="utf-8") as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"钩子已注册到 {SETTINGS_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
