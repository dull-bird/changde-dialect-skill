#!/usr/bin/env bash
# Install the changde-dialect Agent Skill into whichever of
# Claude Code / Codex / OpenClaw / Kimi Code CLI are present on this machine.
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

if [ -d "$HOME/.kimi" ]; then
  # Kimi Code CLI merges skills from the shared ~/.agents/skills directory
  # (merge_all_available_skills in config.toml) rather than a ~/.kimi/skills
  # dir of its own, so it shares this install with any other tool reading
  # the same universal directory.
  install_into "$HOME/.agents" ".agents (Kimi Code CLI 等读取 ~/.agents/skills 的通用目录)"
  installed_any=true
  echo "  可选：运行 kimi/install-hook.sh 注册自动关键词开关钩子"
fi

if [ "$installed_any" = false ]; then
  echo "没有检测到 ~/.claude、~/.codex、~/.openclaw 或 ~/.kimi，任何一个都没装，跳过安装。"
  echo "你也可以手动把 skills/changde-dialect 拷贝到对应工具的 skills 目录下。"
  exit 1
fi

echo
echo "装好哒！在对应工具里说「说常德话」试一哈。"
