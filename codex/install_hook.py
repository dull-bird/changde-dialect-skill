#!/usr/bin/env python3
"""Idempotently register the changde-dialect UserPromptSubmit hook in
~/.codex/config.toml without clobbering existing config.

Verified against Codex CLI 0.142.4 via `codex exec`. TOML array-of-tables
(`[[hooks.UserPromptSubmit]]` etc.) can be appended anywhere in the file, but
a duplicate `[features]` table header would break parsing, so that part is
patched in place if it already exists instead of being re-appended.
"""
import os
import re
import sys

CONFIG_PATH = os.path.expanduser("~/.codex/config.toml")
MARKER = "changde-dialect/scripts/dialect_hook.py"
HOOK_COMMAND = "python3 " + os.path.expanduser(
    "~/.codex/skills/changde-dialect/scripts/dialect_hook.py"
)


def ensure_features_hooks_enabled(text: str) -> str:
    match = re.search(r"^\[features\]\s*$", text, re.MULTILINE)
    if not match:
        return text + "\n[features]\nhooks = true\n"

    if re.search(r"^\s*hooks\s*=", text[match.end():], re.MULTILINE):
        # A `hooks` key already exists under [features]; leave it as-is
        # (assume the user or a previous run already enabled it).
        return text

    insert_at = match.end() + 1
    return text[:insert_at] + "hooks = true\n" + text[insert_at:]


def main() -> int:
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    text = ""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, encoding="utf-8") as f:
            text = f.read()

    if MARKER in text:
        print("已经注册过哒，冒得重复添加。")
        return 0

    text = ensure_features_hooks_enabled(text)
    if not text.endswith("\n"):
        text += "\n"
    text += (
        "\n[[hooks.UserPromptSubmit]]\n"
        "[[hooks.UserPromptSubmit.hooks]]\n"
        'type = "command"\n'
        f'command = "{HOOK_COMMAND}"\n'
    )

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"钩子已注册到 {CONFIG_PATH}")
    print(
        "首次运行 codex 时可能需要批准 hook trust；"
        "非交互/自动化场景可加 --dangerously-bypass-hook-trust（谨慎使用）。"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
