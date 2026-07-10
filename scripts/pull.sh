#!/bin/bash
# Fast-forward the clone this script lives in, so the ~/.claude/skills symlink
# reflects the weekly GitHub Action commits. Location-independent.
export PATH="/opt/homebrew/bin:/usr/bin:/bin"
REPO="$(cd "$(dirname "$0")/.." && pwd)"
LOG="$HOME/Library/Logs/byteplus-docs-sync-pull.log"
echo "== $(date -u +%FT%TZ) pull ($REPO) ==" >> "$LOG"
git -C "$REPO" pull --ff-only >> "$LOG" 2>&1
