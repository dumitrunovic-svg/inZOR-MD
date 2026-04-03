#!/usr/bin/env python3
"""
Zenodo PDFs for QC gaps unified chapter + ethylene 3D technical page.

Uses WeasyPrint (same approach as zenodo_publish/baws_nr_study/generate_zenodo_pdf.py):
  HTML(filename=..., base_url=...) → write_pdf(...)

Figures are expected under web/brochure/tests/qc_gaps_h2_ethylene_unified/figures/.
If missing, the script tries to download them from GitHub Pages (mirrors the live site).

Run from anywhere:
  python3 zenodo_publish/qc_gaps_h2_ethylene_unified/generate_zenodo_pdfs.py
"""
from __future__ import annotations

import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

from weasyprint import CSS, HTML

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
BROCHURE = REPO_ROOT / "web" / "brochure" / "tests" / "qc_gaps_h2_ethylene_unified"

FIGURES_REMOTE_BASE = (
    "https://dumitrunovic-svg.github.io/inZOR-ND/tests/qc_gaps_h2_ethylene_unified/figures/"
)

# All PNGs referenced by index.html or ethylene_3d_zor.html (relative to brochure dir).
FIGURE_NAMES = [
    "ethylene_s0s1_gap.png",
    "vladimir_final_comparison.png",
    "vladimir_answer.png",
    "regional_155239_scatter_torsion_rcc_gap.png",
    "regional_155239_torsion_low_gap_hist.png",
    "regional_155239_local_gap_grid.png",
    "regional_155239_local_gap_z_sweep.png",
]

PDF_EXTRA_CSS = CSS(
    string="""
    @page { size: A4; margin: 14mm 16mm; }
    body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    """
)

OUTPUTS = [
    ("index.html", "inZOR-ND_QC_Gaps_H2_Ethylene_Unified_Zenodo.pdf"),
    ("ethylene_3d_zor.html", "inZOR-ND_Ethylene_3D_Quasidegenerate_Gap_Structure_Zenodo.pdf"),
]


def ensure_figures() -> None:
    fig_dir = BROCHURE / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    for name in FIGURE_NAMES:
        dest = fig_dir / name
        if dest.is_file() and dest.stat().st_size > 512:
            continue
        url = FIGURES_REMOTE_BASE + name
        print(f"Fetching figure: {url}")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "inZOR-ND-zenodo-pdf/1.0"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            dest.write_bytes(data)
            print(f"  → {dest} ({len(data)} bytes)")
        except (urllib.error.URLError, OSError) as e:
            print(f"  WARN: could not fetch {name}: {e}", file=sys.stderr)


def write_pdf(html_name: str, pdf_name: str) -> Path:
    html_path = BROCHURE / html_name
    if not html_path.is_file():
        raise FileNotFoundError(f"Missing HTML: {html_path}")
    out_pdf = HERE / pdf_name
    # Trailing slash so relative URLs resolve like the browser.
    base_url = BROCHURE.as_uri() + "/"
    HTML(filename=str(html_path), base_url=base_url).write_pdf(
        str(out_pdf),
        stylesheets=[PDF_EXTRA_CSS],
    )
    kb = out_pdf.stat().st_size / 1024
    print(f"Wrote {out_pdf} ({kb:.0f} KB)")
    return out_pdf


def main() -> int:
    if not BROCHURE.is_dir():
        print(f"ERROR: brochure dir not found: {BROCHURE}", file=sys.stderr)
        return 1
    ensure_figures()
    for html_fn, pdf_fn in OUTPUTS:
        write_pdf(html_fn, pdf_fn)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
