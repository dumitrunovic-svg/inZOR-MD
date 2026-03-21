# Zenodo Upload — inZOR-ND: Comprehensive Validation for Automatic CASSCF Active Space Selection

## Files
```
inZORi_ActiveSpace_Comparative_Zenodo.pdf
```

## Upload type
```
Publication → Preprint
```

## Basic information

**Title:**
```
inZOR-ND: Comprehensive Validation for Automatic CASSCF Active Space Selection — 6 Benchmarks on 5 Molecular Systems
```

**Authors:**
```
Novic, Dumitru
  Affiliation: Independent Researcher
  Email: dumitru.novic@gmail.com
```

**Description / Abstract:**
```
We present a comprehensive validation of the inZOR-ND bio-adaptive discovery
engine for automatic CASSCF and SA-CASSCF active space selection across
6 increasingly challenging benchmarks on 5 molecular systems: Cr₂ (transition
metal, 3 geometries), N₂ (full dissociation PEC, 7 geometries), 1,3-butadiene
(torsion PEC, 7 angles), formaldehyde (SA-CASSCF, 3 excited states), and
benzene (large-scale CAS(8,8), 5.7 billion candidates).

inZOR-ND is compared against corrected implementations of NOON-MP2 (natural
orbital occupation numbers from MP2 density matrix) and AVAS (atomic valence
active space), as well as random search on Cr₂.

Key results across all benchmarks:
  - inZOR-ND matches or outperforms standard heuristics on all 6 benchmarks
  - Largest advantage: benzene CAS(8,8)/6-31G — 29 kcal/mol better than
    both NOON-MP2 and AVAS, exploring only 562 out of 5.7 billion candidates
    (0.00001% coverage)
  - Cr₂ hard (3 geometries): 35 kcal/mol vs random search; 7.9 kcal/mol
    vs NOON-MP2/AVAS
  - N₂ PEC (7 geometries): 76 kcal/mol vs NOON; shared CAS converges at
    all bond lengths from 0.90 to 2.50 Å
  - Butadiene torsion (7 angles): 5.5 kcal/mol vs NOON-MP2; non-contiguous
    orbital selection captures π-conjugation across all torsion angles
  - SA-CASSCF formaldehyde (3 states): matches NOON-MP2; AVAS fails entirely
  - The inZOR-ND engine is used completely unmodified across all benchmarks
  - No chemical knowledge is required — no orbital symmetry labels,
    occupation thresholds, or expert input

The study establishes that inZOR-ND provides a genuine advantage for active
space selection on hard problems (large search spaces, multi-geometry
constraints, transition metals), while matching heuristics on easy problems.
The scientific contribution is methodological: quantitative evidence that
standard heuristics can be significantly suboptimal, and a practical black-box
optimizer for automated CASSCF workflows.
```

**Publication date:**
```
2026-03-21
```

**Version:**
```
2.0.0
```

## License
```
Creative Commons Attribution 4.0 International (CC BY 4.0)
```

## Keywords
```
active space selection, CASSCF, SA-CASSCF, quantum chemistry, strongly correlated electrons,
chromium dimer, nitrogen dimer, benzene, butadiene, formaldehyde, multi-reference methods,
bio-inspired optimization, inZOR-ND, combinatorial optimization, comparative validation,
NOON, AVAS, PySCF, transition metal chemistry, multi-geometry optimization,
potential energy curve, excited states, state-averaged CASSCF, large active space
```

## Related identifiers
```
Type: Is supplement to
Identifier: https://dumitrunovic-svg.github.io/inZORi/tests/active_space_comparative/
Resource type: Software

Type: Is related to
Identifier: https://dumitrunovic-svg.github.io/inZORi/tests/active_space_n2/
Resource type: Publication / Preprint
Description: Earlier study — N₂ active space selection (6-31G, global optimum verified)

Type: Is related to
Identifier: https://dumitrunovic-svg.github.io/inZORi/tests/active_space_cr2/
Resource type: Publication / Preprint
Description: Earlier study — Cr₂ active space selection (STO-3G, single geometry)
```
