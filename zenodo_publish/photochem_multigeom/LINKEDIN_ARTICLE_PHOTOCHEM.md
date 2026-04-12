# LinkedIn — article / post (English, copy-paste)

Tone: **evidence-led**, strong but not “marketing”. Use as **Article** or a single **post** + image.

---

## Recommended headline (balanced: force + scientific anchor)

**12/12 geometries in a fulvene CAS(10,10) torsion scan — active-space search vs NOON-MP2**

Alternatives:

- **12/12 geometries. A full torsion-scan benchmark where active-space search outperforms NOON-MP2.**
- **Fulvene CAS(10,10): not one lucky mask — a cluster of solutions that outperform the MP2 baseline across the full scan.**

Avoid leading only with *“12 out of 12. No exceptions.”* — strong, but some readers read it as hype unless the next line anchors the claim.

---

## Subhead (numbers — read this before you post)

- **Primary headline result (cluster-refined 12/12 masks):** mean advantage **~5 kcal/mol** vs NOON-MP2 (reported ~5.2 kcal/mol for the best cluster).
- **Earlier evolutionary mask** on the same page was **~3.5 kcal/mol** mean vs NOON — different stage of the search, same protocol.

**Safe one-liner for LinkedIn:**

> Main fulvene CAS(10,10) result: **~5 kcal/mol** mean advantage vs NOON (**cluster-refined solutions**). Earlier evolutionary masks sit **~3–5 kcal/mol** depending on selection stage — see tables on the site.

**Instead of bare “100% convergence”:**

> **Full SA-CASSCF convergence** for all tested single-geometry evaluations in the consolidated table (**12/12 angles** for fulvene CAS(10,10); **52/52** geometry evaluations across systems for both methods).

---

## Body (LinkedIn Article — polished)

In computational quantum chemistry, choosing the active space for CASSCF is still one of the decisions that separates a calculation that converges from one that merely *looks* convergent.

Many workflows rely on **NOON-MP2** — a **strong, interpretable heuristic baseline**.

This study asks a simple question: can **one shared active space** remain valid across an **entire torsion scan**, including difficult regions with quasi-degeneracy?

**We expected occasional improvements.**  
**We did not expect to see improvements everywhere.**

Using a **consistent SA-CASSCF protocol** (two states, **cc-pVDZ**, Procrustes MO alignment), we compared **inZOR-ND** to **NOON-MP2** across multiple systems — **no molecule-specific tuning** of the search engine.

**Main result — fulvene CAS(10,10), 12 torsion angles:** inZOR-ND yields **lower energy than NOON-MP2 at every point (12/12)**, with a mean advantage of **~5 kcal/mol** for the **cluster-refined** solutions (see page for exact digits and the earlier ~3.5 kcal/mol evolutionary stage).

**Crucially, this is not a single “lucky” solution:** we observe a **cluster of nearly degenerate active spaces**, all **outperforming NOON across the full scan**.

**These results do not contradict NOON — they show that it is not always the upper bound** in this benchmark set.

If you work on photochemical surfaces or automated workflows, the takeaway is simple: **active-space selection behaves like a search problem**, not just a rule-based default.

**Results:**  
https://dumitrunovic-svg.github.io/inZOR-ND/tests/photochem_multi_geom_active_space/index.html

**PDF (repo path):**  
`zenodo_publish/photochem_multigeom/inZOR-ND_Photochem_MultiGeom_ActiveSpace_Zenodo.pdf`

---

## Ready-to-post short version (optimized for feed + credibility)

**Headline:**  
12/12 geometries in a fulvene CAS(10,10) torsion scan — active-space search vs NOON-MP2

**Body:**

In computational quantum chemistry, choosing the active space for CASSCF is still one of the decisions that separates a calculation that converges from one that merely looks convergent.

Many workflows rely on NOON-MP2 — a strong, interpretable heuristic baseline.

This study asks a simple question: can a single active space remain valid across an entire torsion scan, including difficult regions with quasi-degeneracy?

We expected occasional improvements.  
We did not expect to see improvements everywhere.

Using a consistent SA-CASSCF protocol (two states, cc-pVDZ, Procrustes alignment), we compared inZOR-ND to NOON-MP2 across multiple systems.

**Main result:** For fulvene CAS(10,10) across 12 geometries, inZOR-ND yields lower energy at every point (12/12), with a mean advantage of ~5 kcal/mol (cluster-refined solutions; earlier evolutionary masks ~3–5 kcal/mol depending on stage — details on the page).

**Crucially, this is not a single “lucky” mask:** we observe a cluster of nearly degenerate active spaces, all outperforming NOON across the full scan.

These results do not contradict NOON — they show that it is not always the upper bound.

If you work on photochemical surfaces or automated workflows, the takeaway is simple: active space selection behaves like a search problem, not just a rule-based one.

Results:  
https://dumitrunovic-svg.github.io/inZOR-ND/tests/photochem_multi_geom_active_space/index.html

---

## Short post variants

**Post A — hook + link**  
12/12 geometries · fulvene CAS(10,10) · same SA-CASSCF protocol, no molecule tuning. Cluster-refined masks ~5 kcal/mol mean vs NOON; not one lucky solution. Full tables → [link]

**Post B — for QC engineers**  
If NOON is your default on photochemical PECs: we published a multi-geometry benchmark where discrete search merits attention. Hardest line — fulvene 12/12, cluster of equivalent solutions. [link]

---

## Hashtags (pick 5–8)

`#QuantumChemistry` `#ComputationalChemistry` `#CASSCF` `#Photochemistry` `#ActiveSpace` `#PySCF` `#Research` `#OpenScience`

---

## Hero image (LinkedIn)

**File:** `zenodo_publish/photochem_multigeom/linkedin_photochem_hero.png`

**Design intent (v2 — scroll-stopping):**

1. **Instant read:** “12/12 geometries” + “(fulvene CAS(10,10))” so the metric is not ambiguous.
2. **One human line:** Active space search vs NOON-MP2 (large enough to read on mobile).
3. **Differentiator:** “Cluster of solutions — not one lucky mask” (smaller but legible).
4. **Trust bar:** “Same protocol · no molecule-specific tuning” — short, not a wall of jargon.

For link-preview crops (~1200×627), keep text in the **upper two-thirds** of the image.

---

## Alternate graphic — “ACTIVE SPACE” variant

**File:** `zenodo_publish/photochem_multigeom/linkedin_photochem_active_space.png`

Use as a second carousel slide or A/B test in the feed. Copy on image:

- ACTIVE SPACE / with inZOR-ND  
- 12/12 geometries · (fulvene CAS(10,10))  
- outperforms NOON-MP2  
- multiple solutions — same result  
- same protocol
