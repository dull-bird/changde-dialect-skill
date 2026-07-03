#!/usr/bin/env bash
# Register the changde-dialect keyword-toggle hook in ~/.kimi/config.toml.
# Safe to re-run; patches existing config instead of overwriting it.
set -euo pipefail
python3 "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/install_hook.py"
