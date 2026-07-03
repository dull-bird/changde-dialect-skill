#!/usr/bin/env python3
"""Idempotently register the changde-dialect UserPromptSubmit hook in
~/.kimi/config.toml without clobbering existing config.

Verified against Kimi Code CLI 1.48.0 via `kimi --print`. Kimi's hook
event names and stdin/stdout JSON contract match Claude Code closely
enough that the same dialect_hook.py works unmodified.

`hooks` in config.toml is a single flat TOML array (not an appendable
array-of-tables like Codex's `[[hooks.X]]`), so this does a bracket-match
on the existing `hooks = [ ... ]` span and rewrites just that array,
appending our entry to whatever was already there instead of assuming
the array starts empty.
"""
import os
import re
import sys

CONFIG_PATH = os.path.expanduser("~/.kimi/config.toml")
MARKER = "changde-dialect/scripts/dialect_hook.py"
HOOK_COMMAND = "python3 " + os.path.expanduser(
    "~/.claude/skills/changde-dialect/scripts/dialect_hook.py"
)
HOOK_ENTRY = (
    '{ event = "UserPromptSubmit", command = "%s" }' % HOOK_COMMAND
)


def find_hooks_span(text: str):
    match = re.search(r"^hooks\s*=\s*\[", text, re.MULTILINE)
    if not match:
        return None
    start = match.end() - 1  # position of the opening '['
    depth = 0
    i = start
    while i < len(text):
        if text[i] == "[":
            depth += 1
        elif text[i] == "]":
            depth -= 1
            if depth == 0:
                return match.start(), i + 1
        i += 1
    return None


def main() -> int:
    if not os.path.exists(CONFIG_PATH):
        print(f"冒得找到 {CONFIG_PATH}，Kimi Code CLI 好像还没跑过一次，先跑一下再装钩子。")
        return 1

    with open(CONFIG_PATH, encoding="utf-8") as f:
        text = f.read()

    if MARKER in text:
        print("已经注册过哒，冒得重复添加。")
        return 0

    span = find_hooks_span(text)
    if span is None:
        # No `hooks = [...]` key at all (unexpected for a config written
        # by a recent kimi-cli, but handle it anyway).
        if not text.endswith("\n"):
            text += "\n"
        text += f"hooks = [\n  {HOOK_ENTRY}\n]\n"
    else:
        start, end = span
        inner = text[start + len("hooks = ["):end - 1].strip()
        if inner:
            new_inner = f"{inner},\n  {HOOK_ENTRY}"
        else:
            new_inner = f"\n  {HOOK_ENTRY}\n"
        text = text[:start] + "hooks = [" + new_inner + "]" + text[end:]

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"钩子已注册到 {CONFIG_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
