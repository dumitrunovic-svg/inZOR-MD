# Zenodo Upload — inZOR-ND Active Space Selection: Cr₂

## Files
```
inZORi_ActiveSpace_Cr2_Zenodo.pdf
```

## Upload type
```
Publication → Preprint
```

## Basic information

**Title:**
```
inZOR-ND Active Space Selection: Bio-Adaptive Discovery of Optimal CASSCF Active Spaces for Cr₂ Without Chemical Priors (STO-3G, 30.26M Candidates)
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
selection problem for the chromium dimer Cr₂ — one of the most challenging
molecules in quantum chemistry. Using a STO-3G basis with CASSCF(8,8),
inZOR-ND searches for the optimal active space from C(36,8) = 30,260,340
possible candidates.

Without any chemical priors, orbital symmetry labels, or occupation-number
thresholds, inZOR-ND evaluates only 1,572 spaces (0.0052% of the search
space) and discovers the optimal active space containing Cr 3d/4s orbitals,
capturing 0.559 Eh of correlation energy. 10 degenerate optima are found.

Key results:
  - Search space: C(36,8) = 30,260,340 — brute-force infeasible (~5 years)
  - Evaluated: 1,572 (0.0052%) — 99.995% savings
  - Optimal: MOs [8,20,21,22,24,27,33,35] — Cr 3d/4s character
  - E(CASSCF) = −2064.595 Eh, Correlation = −0.559 Eh
  - Wall time: 51.7 min on 14-core CPU
  - inZOR-ND engine: unmodified
```

**Publication date:**
```
2026-03-19
```

**Version:**
```
1.0.0
```

## License
```
Creative Commons Attribution 4.0 International (CC BY 4.0)
```

## Keywords
```
active space selection, CASSCF, quantum chemistry, strongly correlated electrons,
chromium dimer, Cr2, multi-reference methods, bio-inspired optimization,
inZOR-ND, combinatorial optimization, PySCF, transition metal chemistry,
STO-3G, orbital degeneracy, evolutionary algorithm
```

## Related identifiers
```
Type: Is supplement to
Identifier: https://dumitrunovic-svg.github.io/inZORi/tests/active_space_cr2/
Resource type: Software

Type: Is related to
Identifier: https://dumitrunovic-svg.github.io/inZORi/tests/active_space_n2/
Resource type: Publication / Preprint
Description: Companion study — N₂ active space selection (6-31G)
```
