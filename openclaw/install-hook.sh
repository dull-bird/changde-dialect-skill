#!/usr/bin/env bash
# Install and enable the changde-dialect-toggle OpenClaw hook.
# Verified end-to-end with `openclaw agent --local` on OpenClaw 2026.6.6.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO_DIR/openclaw/hooks/changde-dialect-toggle"
DEST="$HOME/.openclaw/hooks/changde-dialect-toggle"

if ! command -v openclaw >/dev/null 2>&1; then
  echo "冒得找到 openclaw 命令，跳过。"
  exit 1
fi

mkdir -p "$HOME/.openclaw/hooks"
rm -rf "$DEST"
cp -r "$SRC" "$DEST"
echo "✓ 已装到 $DEST"

openclaw hooks enable changde-dialect-toggle
