#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURE="$ROOT_DIR/examples/fixture_vault"
OUT="$ROOT_DIR/examples/sample-output"

python3 "$ROOT_DIR/obsidian_revenue_scout.py" \
  --vault "$FIXTURE" \
  --out "$OUT" \
  --limit 10

printf '\nWrote sample output to %s\n' "$OUT"
