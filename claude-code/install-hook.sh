#!/usr/bin/env bash
# Register the changde-dialect keyword-toggle hook in ~/.claude/settings.json.
# Safe to re-run; merges instead of overwriting existing hooks.
set -euo pipefail
python3 "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/install_hook.py"
