# arXiv preprint: QC gaps — H₂ diagnostic & ethylene (inZOR-ND), unified

## Path (repository)

```
/opt/projects/zor_task_solver/papers_arxiv/qc_gaps_h2_ethylene_arxiv/
```

Files:

- `main.tex` — manuscript (pdflatex)
- `references.bib` — bibliography
- `title_abstract.txt` — copy-paste helpers for arXiv metadata

## Figures

`main.tex` includes PNGs from the brochure tree (single source of truth):

`web/brochure/tests/qc_gaps_h2_ethylene_unified/figures/`

Required files:

- `ethylene_s0s1_gap.png`
- `vladimir_final_comparison.png`
- `vladimir_answer.png`

If missing, copy from your validation exports into that `figures/` folder.

## Build (local PDF)

**Option A — pdfLaTeX + BibTeX** (TeX Live / MiKTeX):

```bash
cd /opt/projects/zor_task_solver/papers_arxiv/qc_gaps_h2_ethylene_arxiv
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

**Option B — Tectonic** (single command, downloads TeX packages on first run):

```bash
cd /opt/projects/zor_task_solver/papers_arxiv/qc_gaps_h2_ethylene_arxiv
tectonic main.tex
```

Output: **`main.pdf`** (arXiv-style PDF: embedded fonts, standard article class, natbib + `unsrtnat`).

The committed **`main.pdf`** in this folder is the reference build for submission previews.

## arXiv submission (typical)

1. Prefer **pdflatex** compilation on arXiv; upload `main.tex`, `references.bib`, and the **three** figure files (or ensure figures are findable — arXiv may not resolve `../../web/...`; see below).

2. **If arXiv cannot see parent-path figures:** copy the three PNGs into this folder and set in `main.tex`:

   ```latex
   \graphicspath{{./}}
   ```

3. License: choose **arXiv non-exclusive license**; suggested journal-style licence note in manuscript footer.

4. **Primary subject:** Physics → Chemical Physics (`physics.chem-ph`) or `cond-mat.mtrl-sci` if you prefer; cross-list as needed.

5. **Data availability:** cite the GitHub Pages report and JSON `h2_stretch_results.json`; ethylene scene path `zor_scenes/scene_ethylene_quasidegen/` in the source repo.

## Public HTML companion

- Unified: https://dumitrunovic-svg.github.io/inZOR-ND/tests/qc_gaps_h2_ethylene_unified/index.html
- Ethylene 3D: https://dumitrunovic-svg.github.io/inZOR-ND/tests/qc_gaps_h2_ethylene_unified/ethylene_3d_zor.html

## Zenodo PDF mirror (optional)

`zenodo_publish/qc_gaps_h2_ethylene_unified/inZOR-ND_QC_Gaps_H2_Ethylene_Unified_Zenodo.pdf` (WeasyPrint export of the HTML).
