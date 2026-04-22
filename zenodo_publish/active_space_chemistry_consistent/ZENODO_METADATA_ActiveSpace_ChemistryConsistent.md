# Zenodo Upload — inZOR-ND: Chemistry-Consistent Active-Space Selection (CH2O, C2H4, C4H6)

## Files
```
inZORi_ActiveSpace_ChemistryConsistent_Zenodo.pdf
```

## Upload type
```
Publication → Preprint
```

## Basic information

**Title:**
```
inZOR-ND: Chemistry-Consistent Active-Space Selection across CH2O, C2H4 and C4H6 — A Three-Benchmark Validation under SA(2)-CASSCF / cc-pVDZ
```

**Authors:**
```
Novic, Dumitru
  Affiliation: Independent Researcher
  Email: dumitru.novic@gmail.com
```

**Description / Abstract:**
```
We report a chemistry-consistent validation of inZOR-ND active-space selection on three
frontier-driven photochemical systems: formaldehyde (CH2O, CAS(2,2)), ethylene
(C2H4, CAS(4,4)) and 1,3-butadiene (C4H6, CAS(4,4)). All calculations use PySCF,
SA(2)-CASSCF with weights [0.5, 0.5], cc-pVDZ basis, and identical fitness
evaluation across systems. The benchmark covers 11 independent GA seeds and 47
SA-CASSCF runs.

Methodological framing. Traditional active-space ranking often overweights a
single scalar (the optimized SA-CASSCF energy). On these systems, that scalar can
reward chemically poor masks (deep-sigma correlation, far virtuals, masks that omit
the frontier orbitals altogether). We introduce a chemistry-consistent validation
framework that filters such failures before any energy ranking is performed:
chemical gates (frontier-orbital overlap, mask validity, frozen-core sanity),
followed by a hard convergence check (any non-converged SA-CASSCF cycle propagates
as a worst-case sentinel and cannot win the population step), with energy ranking
performed only on candidates that survive both.

Headline results.
  - 11/11 accepted winners are chemistry-valid across the 3 molecules and 11 GA seeds.
  - 5/11 winners that pure-energy ranking would have promoted are exposed as
    anti-chemical (zero or insufficient frontier content) and rejected pre-CASSCF.
    Breakdown: 3 on CH2O (zero frontier MOs), 2 on C2H4 (seed 73 zero HOMO/LUMO
    content; seed 101 only 1 frontier MO).
  - Ethylene seed 73 is redirected from the sigma-only mask [2,4,21,22] to the
    canonical pi/pi* manifold [6,7,8,9] = (HOMO-1, HOMO, LUMO, LUMO+1).
  - On 1,3-butadiene CAS(4,4), the framework outperforms the NOON-MP2 baseline by
    approximately 16 kcal/mol on R_E,raw with a chemically cleaner mask
    [13,14,15,16] than the NOON-MP2 selection [13,14,15,19] (NOON-MP2 picks LUMO+4
    instead of LUMO+1 here — the baseline is itself the chemistry outlier).
  - 47/47 SA-CASSCF runs converged on accepted candidates (100%). Convergence is
    enforced architecturally through Inf-safe arithmetic — a non-converged geometry
    cannot win a sort. 99/99 internal regression tests cover this branch.

Multi-basin observation. The SA-CASSCF orbital-optimization landscape on these
systems is genuinely multi-basin. On butadiene at phi = 86°, two competing CAS(4,4)
solutions are separated by an essentially orthogonal active dimension (89.85°
principal angle from the subspace-overlap diagnostic; singular values
[0.996, 0.982, 0.946, 0.003]) and approximately 18 kcal/mol of energy. Standard
intra-active multistart (M = 30 starts at sigma_max = 3.0) cannot bridge this gap:
the bridging direction sits outside the 4-dimensional active sub-space being
rotated. Combinatorial exploration over candidate masks samples the basin
landscape independently of intra-active orientation and is therefore the
appropriate sampling strategy at this scale.

Five-test acceptance protocol. An active space is reported only when it satisfies:
(1) chemical meaning — frontier-orbital overlap above the per-CAS threshold;
(2) smooth path behaviour — no non-physical jumps in S0 or in the S1-S0 gap;
(3) proper convergence — every geometry of the scan converges, partial scans
disqualified; (4) reproducibility — independent seeds collapse to a small number
of chemistry-valid equivalence classes; (5) competitive energy — R_E,raw is
reported and compared to NOON-MP2 only after 1-4 are met.

Hardware (representative): Intel Core Ultra 7 255H (14 cores), PySCF 2.x.
```

**Publication date:**
```
2026-04-19
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
active space selection, CASSCF, SA-CASSCF, photochemistry, chemistry-consistent
validation, frontier orbitals, HOMO-LUMO, multi-basin landscape, subspace overlap,
combinatorial optimization, formaldehyde, ethylene, butadiene, n-pi* transition,
pi-pi* transition, NOON-MP2, PySCF, cc-pVDZ, multireference methods, convergence
integrity, evolutionary search, inZOR-ND, quantum chemistry
```

## Related identifiers
```
Type: Is supplement to
Identifier: https://dumitrunovic-svg.github.io/inZOR-ND/tests/active_space_chemistry_consistent/
Resource type: Software

Type: Is related to
Identifier: https://dumitrunovic-svg.github.io/inZOR-ND/tests/active_space_comparative/
Resource type: Publication / Preprint
Description: Comprehensive 8-benchmark active-space comparative study (context)

Type: Is related to
Identifier: https://dumitrunovic-svg.github.io/inZOR-ND/tests/photochem_multi_geom_active_space/
Resource type: Publication / Preprint
Description: Photochemical multi-geometry active-space selection (related methodology)
```
