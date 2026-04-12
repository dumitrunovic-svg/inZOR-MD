# LinkedIn — article / long post (copy-paste, English)

Use as a **LinkedIn Article** or split into 2–3 consecutive posts. Tone: professional, evidence-led, no empty hype.

---

## Headline options (“hook” — pick one)

1. **12 out of 12. No exceptions. A photochemical benchmark where active-space selection beats NOON-MP2 at every geometry.**

2. **Fulvene CAS(10,10): not one lucky mask — a cluster of solutions that outperform the MP2 baseline across the full torsion scan.**

3. **When the heuristic stays strong but stops being the ceiling: multi-geometry SA-CASSCF with inZOR-ND vs NOON-MP2.**

*Suggestion:* use **1** for broad feed impact; **2** for a technical audience.

---

## Subhead (optional, first line under the headline)

Three molecules. 52 geometries. 100% convergence. Main result: fulvene CAS(10,10), cc-pVDZ — mean advantage ~5.2 kcal/mol vs NOON-MP2 across all 12 torsion angles tested.

---

## Body (LinkedIn Article)

In computational quantum chemistry, choosing the active space for CASSCF is still one of the decisions that separates a calculation that converges from one that merely *looks* convergent while misrepresenting the physics.

Many workflows use **NOON-MP2** — natural orbital occupation numbers from MP2 — as the default starting point. It is fast, interpretable, and often solid.

This study asks a question that matters for **photochemistry**: can you find **one shared** active space that remains sensible across an **entire torsion scan** — including regions near conical intersections and strong quasi-degeneracy where single-reference rules break?

We compared **inZOR-ND** (bio-adaptive discrete search) to **NOON-MP2** using the same evaluation protocol (**SA-CASSCF**, two states, **cc-pVDZ**, Procrustes MO alignment), with **no molecule-specific tuning** of the search engine.

The **main result** is unambiguous: for **fulvene CAS(10,10)** at **12** torsion angles, the inZOR-ND selected spaces yield **lower mean SA-CASSCF energy than NOON-MP2 at every geometry** — **12/12**. The mean advantage is on the order of **5.2 kcal/mol**. This is not a single “magic” mask: we report a **cluster of nearly degenerate winning masks** (five equivalent solutions) that deliver the same outcome across the grid.

This does not “invalidate” NOON — it positions it fairly: **NOON-MP2 remains a strong heuristic baseline**, but **in this benchmark set** it is no longer the empirical upper bound for SA-CASSCF energy.

Beyond fulvene, the study includes comparative context for **ethylene**, **1,3-butadiene**, and fulvene at **CAS(6,6)** and **CAS(8,8)** — including a large mean advantage for CAS(8,8) on a diagnostic angle subset. Tables and figures are public.

If you work on non-adiabatic dynamics, torsion scans, or automating CASSCF workflows, the practical message is simple: **treat active-space selection as an optimization problem**, not only as a fixed rulebook.

**Results (HTML):**  
https://dumitrunovic-svg.github.io/inZOR-ND/tests/photochem_multi_geom_active_space/index.html

**PDF (repository path):**  
`zenodo_publish/photochem_multigeom/inZOR-ND_Photochem_MultiGeom_ActiveSpace_Zenodo.pdf`

---

## Short post variants (if you do not use Article mode)

**Post A — hook + link**  
12/12 is not marketing — it is the fulvene CAS(10,10) outcome: inZOR-ND vs NOON-MP2 on the full torsion scan under one SA-CASSCF protocol. NOON stays a strong baseline; here, search systematically finds lower energies. Details and figures → [link].

**Post B — for QC engineers**  
If NOON is still your “good enough default” for active spaces on photochemical PECs: we published a multi-geometry benchmark (ethylene, butadiene, fulvene) where discrete optimization is worth a serious look. Hardest datapoint — fulvene CAS(10,10): 12/12 angles, cluster of solutions. [link]

---

## Hashtags (pick 5–8)

`#QuantumChemistry` `#ComputationalChemistry` `#CASSCF` `#Photochemistry` `#ActiveSpace` `#PySCF` `#Research` `#OpenScience`

---

## Hero image (LinkedIn)

File: `zenodo_publish/photochem_multigeom/linkedin_photochem_hero.png`  
English headline on image. For **link preview** cards LinkedIn often prefers ~1200×627 — crop or resize if needed.
