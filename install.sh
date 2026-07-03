#!/usr/bin/env bash
# Install the changde-dialect Agent Skill into whichever of
# Claude Code / Codex / OpenClaw are present on this machine.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$REPO_DIR/skills/changde-dialect"

install_into() {
  local target_root="$1"
  local label="$2"
  local dest="$target_root/skills/changde-dialect"

  mkdir -p "$target_root/skills"
  rm -rf "$dest"
  cp -r "$SRC" "$dest"
  echo "✓ 已安装到 $label: $dest"
}

installed_any=false

if [ -d "$HOME/.claude" ]; then
  install_into "$HOME/.claude" "Claude Code (~/.claude/skills)"
  installed_any=true
  echo "  可选：运行 claude-code/install-hook.sh 注册自动关键词开关钩子"
fi

if [ -d "$HOME/.codex" ]; then
  install_into "$HOME/.codex" "Codex (~/.codex/skills)"
  installed_any=true
fi

if [ -d "$HOME/.openclaw" ]; then
  install_into "$HOME/.openclaw" "OpenClaw (~/.openclaw/skills，全局，所有 agent 共用)"
  installed_any=true
fi

if [ "$installed_any" = false ]; then
  echo "没有检测到 ~/.claude、~/.codex 或 ~/.openclaw，任何一个都没装，跳过安装。"
  echo "你也可以手动把 skills/changde-dialect 拷贝到对应工具的 skills 目录下。"
  exit 1
fi

echo
echo "装好哒！在对应工具里说「说常德话」试一哈。"
