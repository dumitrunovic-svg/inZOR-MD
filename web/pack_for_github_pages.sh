#!/usr/bin/env bash
# Sync brochure/ → inzori-web-deploy/ for GitHub Pages (inZORi / inZOR-ND).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/web/brochure"
DST="$ROOT/web/inzori-web-deploy"
mkdir -p "$DST"

# Home + language pages live at repo root (not in web/brochure/). GitHub Actions publishes ONLY
# web/inzori-web-deploy — without this copy, index.html would never reach Pages after the "web-only" workflow.
for f in index.html de.html fr.html ro.html; do
  if [[ -f "$ROOT/$f" ]]; then
    rsync -a "$ROOT/$f" "$DST/$f"
  fi
done

# No --delete: deploy may contain bundles not yet mirrored in brochure; avoid wiping assets.
rsync -a \
  --exclude '.git/' \
  "$SRC/tests/" "$DST/tests/"
rsync -a "$SRC/tests.html" "$DST/tests.html"
if [[ -f "$SRC/style.css" ]]; then
  rsync -a "$SRC/style.css" "$DST/style.css"
fi
echo "Synced $SRC → $DST (tests/ + tests.html)"

# GitHub Actions deploys only web/inzori-web-deploy; tests.html loads ./tests/manifest.json there.
for d in qc_gaps_h2_ethylene_unified; do
  if [[ -d "$SRC/tests/$d" ]]; then
    rsync -a "$SRC/tests/$d/" "$ROOT/tests/$d/"
  fi
done
echo "Mirrored unified QC report → $ROOT/tests/ (for Pages root)"
