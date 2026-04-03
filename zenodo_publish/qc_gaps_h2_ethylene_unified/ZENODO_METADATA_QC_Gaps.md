# Zenodo upload — QC gaps (H₂ + ethylene) & ethylene 3D

Web companions (GitHub Pages):

- Unified chapter: [tests/qc_gaps_h2_ethylene_unified/index.html](https://dumitrunovic-svg.github.io/inZOR-ND/tests/qc_gaps_h2_ethylene_unified/index.html)
- Ethylene 3D technical report: [tests/qc_gaps_h2_ethylene_unified/ethylene_3d_zor.html](https://dumitrunovic-svg.github.io/inZOR-ND/tests/qc_gaps_h2_ethylene_unified/ethylene_3d_zor.html)

## PDF files (this folder)

| File | Source HTML |
|------|-------------|
| `inZOR-ND_QC_Gaps_H2_Ethylene_Unified_Zenodo.pdf` | `web/brochure/tests/qc_gaps_h2_ethylene_unified/index.html` |
| `inZOR-ND_Ethylene_3D_Quasidegenerate_Gap_Structure_Zenodo.pdf` | `web/brochure/tests/qc_gaps_h2_ethylene_unified/ethylene_3d_zor.html` |

## Regenerate

Same stack as other Zenodo HTML→PDF notes in this repo (**WeasyPrint**):

```bash
cd /path/to/inZOR-ND   # repository root
python3 zenodo_publish/qc_gaps_h2_ethylene_unified/generate_zenodo_pdfs.py
```

The script fills `web/brochure/tests/qc_gaps_h2_ethylene_unified/figures/` from the live site when local PNGs are absent, then writes the two PDFs next to this file.

## Requirements

- Python 3 with `weasyprint` installed (`pip install weasyprint`).
- Network access optional: only needed to auto-fetch figures if they are not already on disk.
