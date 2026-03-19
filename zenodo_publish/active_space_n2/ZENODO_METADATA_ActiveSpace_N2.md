# Zenodo Upload — inZORi Active Space Selection: N₂ Dissociation

## ⏳ DE PUBLICAT PE ZENODO
**Fișier PDF:** `inZORi_ActiveSpace_N2_Zenodo.pdf`
**Web report:** https://dumitrunovic-svg.github.io/inZORi/tests/active_space_n2/

---

## Câmpuri de completat pe Zenodo (zenodo.org/uploads/new)

### 1. Files
```
inZORi_ActiveSpace_N2_Zenodo.pdf
```

### 2. Upload type
```
Publication → Preprint
```

### 3. Basic information

**Title:**
```
inZORi Active Space Selection: Bio-Adaptive Discovery of Optimal CASSCF Active Spaces for N₂ Dissociation Without Chemical Priors (6-31G, 3 Geometries)
```

**Authors:**
```
Novic, Dumitru
  Affiliation: Independent Researcher
  Email: dumitru.novic@gmail.com
```

**Description / Abstract:**
```
We apply the inZOR-ND bio-adaptive discovery engine to the active space
selection problem in strongly correlated quantum chemistry. For N₂
dissociation across three geometries (R = 1.1, 1.5, 2.0 Å) using a 6-31G
basis set, inZOR-ND selects the optimal CASSCF(6,6) active space from a
pool of 18 molecular orbitals — a combinatorial search space of
C(18,6) = 18,564 possible choices.

Without any chemical priors, orbital symmetry labels, or natural orbital
occupation thresholds, inZOR-ND explores an 18-dimensional continuous space.
Candidate positions are mapped to orbital selections via top-k ranking.
Fitness aggregates CASSCF energies across all three geometries
simultaneously, correctly weighting strongly correlated (dissociation-limit)
configurations.

inZOR-ND evaluates only 541 active spaces (2.91% of the search space) and
discovers the globally optimal CASSCF(6,6) space, achieving convergence at
all three geometries. A 97.1% reduction in CASSCF evaluations compared to
brute-force search.

A key finding: the bio-adaptive search dynamics naturally reveal 10
degenerate optimal active spaces — symmetry-equivalent configurations under
N₂'s D∞h point group — discovered without any symmetry information provided
to the optimizer.

Key results:
  - Search space: C(18,6) = 18,564 CASSCF(6,6) candidates
  - Evaluated: 541 (2.91%) — 97.1% savings vs brute-force
  - Best active space: MOs [2,4,5,7,11,15] (σ/π/π*/σ* manifold)
  - E(CASSCF) @ R=1.10Å: −109.015944 Eh (conv: True)
  - E(CASSCF) @ R=1.50Å: −108.886195 Eh (conv: True)
  - E(CASSCF) @ R=2.00Å: −108.773492 Eh (conv: True)
  - Correlation energy @ R=2.0Å: −0.464 Eh (strong multi-reference)
  - Degenerate optima: 10 symmetry-equivalent spaces
  - Wall time: 1244s (20.7 min) on 14-core CPU
  - inZOR-ND engine: unmodified
  - Basis: 6-31G | Software: PySCF 2.x, inZOR-ND
```

**Publication date:**
```
2026-03-19
```

**Version:**
```
1.0.0
```

### 4. License
```
Creative Commons Attribution 4.0 International (CC BY 4.0)
```

### 5. Keywords
```
active space selection
CASSCF
quantum chemistry
strongly correlated electrons
N2 dissociation
multi-reference methods
bio-inspired optimization
bio-adaptive optimization
inZOR-ND
combinatorial optimization
PySCF
6-31G basis set
D∞h symmetry
orbital degeneracy
multi-geometry optimization
evolutionary algorithm
derivative-free optimization
```

### 6. Subject / Domain
```
Physics → Chemical Physics
Computer Science → Artificial Intelligence
Chemistry → Quantum Chemistry
```

### 7. Related identifiers
```
Type: Is supplement to
Identifier: https://dumitrunovic-svg.github.io/inZORi/tests/active_space_n2/
Resource type: Software

Type: Is related to
Identifier: 10.5281/zenodo.18716837
Resource type: Publication / Preprint
Description: inZORi-PFΔ Phase 1 (companion paper, same ZOR framework)
```

### 8. Additional notes
```
Web report with figures:
  https://dumitrunovic-svg.github.io/inZORi/tests/active_space_n2/

Hardware: 14-core CPU, Linux
Dependencies: PySCF 2.x, NumPy, Python 3.10+
Seed: 42 (fully deterministic)

Research conducted without institutional affiliation or external funding.
March 2026.
```

---

## Pași pe Zenodo

1. Mergi la: https://zenodo.org/uploads/new
2. Upload: `inZORi_ActiveSpace_N2_Zenodo.pdf`
3. Completează câmpurile de mai sus
4. **Save draft** → verifică preview
5. **Publish** → primești DOI instant
6. Adaugă DOI-ul în:
   - `web/brochure/tests/manifest.json` → câmpul `links.zenodo`
   - `web/brochure/tests/active_space_n2/index.html` → secțiunea Reproducibility

## Linkuri
- Upload: https://zenodo.org/uploads/new
- Web report: https://dumitrunovic-svg.github.io/inZORi/tests/active_space_n2/
- inZORi project: https://dumitrunovic-svg.github.io/inZORi/
