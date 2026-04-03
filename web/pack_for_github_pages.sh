#!/usr/bin/env bash
# Sync brochure/ → inzori-web-deploy/ for GitHub Pages (inZORi / inZOR-ND).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/web/brochure"
DST="$ROOT/web/inzori-web-deploy"
mkdir -p "$DST"
# No --delete: deploy may contain bundles not yet mirrored in brochure; avoid wiping assets.
rsync -a \
  --exclude '.git/' \
  "$SRC/tests/" "$DST/tests/"
rsync -a "$SRC/tests.html" "$DST/tests.html"
if [[ -f "$SRC/style.css" ]]; then
  rsync -a "$SRC/style.css" "$DST/style.css"
fi
echo "Synced $SRC → $DST (tests/ + tests.html)"
