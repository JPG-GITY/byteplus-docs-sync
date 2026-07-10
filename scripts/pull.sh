#!/bin/bash
# Keeps the local clone (and thus the ~/.claude/skills symlink) in sync with the
# weekly GitHub Action commits. Fast-forward only; never diverges since this clone
# is read-only for skill consumption.
export PATH="/opt/homebrew/bin:/usr/bin:/bin"
REPO="/Users/bytedance/Documents/byteplus-docs-sync"
LOG="$HOME/Library/Logs/byteplus-docs-sync-pull.log"
echo "== $(date -u +%FT%TZ) pull ==" >> "$LOG"
git -C "$REPO" pull --ff-only >> "$LOG" 2>&1
