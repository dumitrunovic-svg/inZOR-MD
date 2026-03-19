# Zenodo Upload — inZOR-ND vs Random Search: Comparative Validation

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
inZOR-ND vs Random Search: Comparative Validation for CASSCF Active Space Discovery on Cr₂ with Multiple Geometries
```

**Authors:**
```
Novic, Dumitru
  Affiliation: Independent Researcher
  Email: dumitru.novic@gmail.com
```

**Description / Abstract:**
```
We present a controlled comparative validation of the inZOR-ND bio-adaptive
discovery engine against random search for automatic CASSCF(8,8) active space
selection. Building on two previous studies — N₂ dissociation (6-31G,
C(18,6) = 18,564 candidates) and Cr₂ single-geometry (STO-3G,
C(36,8) = 30.26M candidates) — we design a harder benchmark: Cr₂ with
3 simultaneous geometries (R = 1.68, 2.0, 2.5 Å), requiring the active
space to converge at all bond lengths.

The multi-geometry constraint reduces the convergence rate from ~100%
(single geometry) to only 8.8%, and eliminates solution degeneracy:
from ~77 degenerate optima (single geometry) to exactly 1.

Under these conditions, inZOR-ND finds the unique optimal active space
with fitness 2064.493, while random search stagnates at 2064.437 — a gap
of 0.056 Hartree (35 kcal/mol), far beyond chemical accuracy (1 kcal/mol).

Key results:
  - inZOR-ND best fitness: 2064.493 vs Random: 2064.437
  - Energy gap: 0.056 Eh = 35 kcal/mol (35× chemical accuracy)
  - inZOR-ND convergence rate: 8.8% vs Random: 1.1% (8× higher)
  - Only 1 degenerate optimal solution out of 30.26M candidates
  - 11 progressive fitness improvements (inZOR-ND) vs stagnation (Random)
  - inZOR-ND engine: unmodified
  - Third study in series: N₂ → Cr₂ → Cr₂ comparative
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
inZOR-ND, combinatorial optimization, comparative validation, random search,
PySCF, transition metal chemistry, multi-geometry optimization
```

## Related identifiers
```
Type: Is supplement to
Identifier: https://dumitrunovic-svg.github.io/inZORi/tests/active_space_comparative/
Resource type: Software

Type: Is related to
Identifier: https://dumitrunovic-svg.github.io/inZORi/tests/active_space_n2/
Resource type: Publication / Preprint
Description: Study 1 — N₂ active space selection (6-31G, global optimum verified)

Type: Is related to
Identifier: https://dumitrunovic-svg.github.io/inZORi/tests/active_space_cr2/
Resource type: Publication / Preprint
Description: Study 2 — Cr₂ active space selection (STO-3G, single geometry)
```
