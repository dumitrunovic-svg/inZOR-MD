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

# GitHub Actions deploys the whole repo; /tests.html loads ./tests/manifest.json at repo root.
for d in qc_gaps_h2_ethylene_unified; do
  if [[ -d "$SRC/tests/$d" ]]; then
    rsync -a "$SRC/tests/$d/" "$ROOT/tests/$d/"
  fi
done
echo "Mirrored unified QC report → $ROOT/tests/ (for Pages root)"
