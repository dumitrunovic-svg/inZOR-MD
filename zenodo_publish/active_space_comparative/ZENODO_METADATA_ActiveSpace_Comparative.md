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
inZOR-ND: Comprehensive Validation for Automatic CASSCF Active Space Selection — 8 Benchmarks on 6 Molecular Systems
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
8 benchmarks on 6 molecular systems: N₂ PEC with 3 basis sets (6-31G,
cc-pVDZ, cc-pVTZ), Cr₂ (transition metal, 3 geometries), 1,3-butadiene
(torsion PEC, 7 angles), formaldehyde (SA-CASSCF, 3 excited states),
benzene (large-scale CAS(8,8), 5.7 billion candidates), and ethylene
(SA-CASSCF S0/S1, 4 torsion angles, cc-pVDZ).

inZOR-ND is compared against corrected implementations of NOON-MP2 (diagonal
1-RDM method for canonical MO selection) and AVAS (PySCF atomic valence
active space module).

Key results across all benchmarks:
  - inZOR-ND wins all 8 benchmarks (3.7–430 kcal/mol advantage)
  - NOON-MP2 or AVAS fail to converge on 4 out of 8 systems
  - N₂ PEC: consistent advantage across 3 basis sets (5.8–42.8 kcal/mol);
    shared CAS converges at all bond lengths from 0.90 to 2.50 Å
  - Cr₂ (3 geometries): −20 kcal/mol vs corrected NOON-MP2
  - Butadiene torsion (7 angles): −3.7 kcal/mol vs NOON-MP2
  - SA-CASSCF formaldehyde (3 states): corrected NOON and AVAS both fail
  - Benzene CAS(8,8): corrected NOON and AVAS both fail; 562 evals out
    of 5.7 billion (0.00001% coverage)
  - Ethylene SA-CASSCF (S0/S1, 4 angles): −430 kcal/mol vs NOON;
    AVAS not applicable due to truncation limitation
  - The inZOR-ND engine is used completely unmodified across all 8 benchmarks
  - No chemical knowledge is required — no orbital symmetry labels,
    occupation thresholds, or expert input

Hardware: Intel Core Ultra 7 255H (14 cores), 20 GB RAM, PySCF 2.12.1.

The study establishes that inZOR-ND provides a genuine advantage for active
space selection, particularly on hard problems. The scientific contribution
is methodological: quantitative evidence that standard heuristics can be
significantly suboptimal or fail entirely, and a practical black-box
optimizer for automated CASSCF workflows.
```

**Publication date:**
```
2026-03-22
```

**Version:**
```
4.0.0
```

## License
```
Creative Commons Attribution 4.0 International (CC BY 4.0)
```

## Keywords
```
active space selection, CASSCF, SA-CASSCF, quantum chemistry, strongly correlated electrons,
chromium dimer, nitrogen dimer, benzene, butadiene, formaldehyde, ethylene, multi-reference methods,
bio-inspired optimization, inZOR-ND, combinatorial optimization, comparative validation,
NOON, AVAS, PySCF, transition metal chemistry, multi-geometry optimization,
potential energy curve, excited states, state-averaged CASSCF, large active space,
cc-pVDZ, cc-pVTZ, photochemistry, conical intersection, torsion
```

## Related identifiers
```
Type: Is supplement to
Identifier: https://dumitrunovic-svg.github.io/inZOR-ND/tests/active_space_comparative/
Resource type: Software

Type: Is related to
Identifier: https://dumitrunovic-svg.github.io/inZOR-ND/tests/active_space_n2/
Resource type: Publication / Preprint
Description: Earlier study — N₂ active space selection (6-31G, global optimum verified)

Type: Is related to
Identifier: https://dumitrunovic-svg.github.io/inZOR-ND/tests/active_space_cr2/
Resource type: Publication / Preprint
Description: Earlier study — Cr₂ active space selection (STO-3G, single geometry)
```
