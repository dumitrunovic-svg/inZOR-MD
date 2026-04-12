# Zenodo Upload — inZOR-ND: Photochemical Multi-Geometry Active Space Selection

## Files
```
inZOR-ND_Photochem_MultiGeom_ActiveSpace_Zenodo.pdf
```

## Upload type
```
Publication → Preprint
```

## Basic information

**Title:**
```
inZOR-ND: Photochemical Multi-Geometry Active Space Selection — Fulvene CAS(10,10) 12/12 vs NOON-MP2 (Ethylene, Butadiene, Fulvene)
```

**Authors:**
```
Novic, Dumitru
  Affiliation: Independent Researcher
  Email: dumitru.novic@gmail.com
```

**Description / Abstract:**
```
We benchmark inZOR-ND (bio-adaptive discrete search) against NOON-MP2 (MP2 natural
orbital occupation numbers) for state-averaged SA-CASSCF active space selection on
photochemical torsion scans. All calculations use PySCF, SA(2) S0/S1 with weights
[0.5, 0.5], cc-pVDZ, and identical SACASFitness evaluation with Procrustes MO
alignment to a reference geometry. The engine configuration is shared across systems
without chemical tuning.

Primary result — Fulvene (C5H4=CH2) CAS(10e,10o), 12 torsion angles (tau = 0°–70°):
inZOR-ND identifies active spaces with lower mean SA-CASSCF energy than NOON-MP2 at
every geometry (12/12). Mean advantage approximately −5.22 kcal/mol vs NOON. Five
nearly degenerate winning masks are reported (cluster of solutions), not a single
accidental selection.

Supporting systems:
  - Ethylene (C2H4): CAS(4e,4o), 16 geometries — energies near-degenerate vs NOON;
    markedly improved S1−S0 gap regularity (e.g. gap sigma 0.79 vs 1.18 eV).
  - 1,3-Butadiene (C4H6): CAS(4e,4o), 10 dihedral angles — mean energy advantage for
    inZOR-ND about −4.45 kcal/mol; per-angle comparison is mixed (e.g. NOON lower
    near one conical-intersection region at phi = 78°).
  - Fulvene CAS(6,6): 9 geometries — about −1.32 kcal/mol mean advantage, 9/9 wins.
  - Fulvene CAS(8,8): 5 diagnostic angles — about −14.40 kcal/mol mean advantage, 5/5.

NOON-MP2 remains a strong, interpretable heuristic baseline. In this benchmark set it
is repeatedly outperformed by inZOR-ND on mean energy for each of the five
configurations (ethylene / butadiene / three fulvene CAS sizes), and for fulvene
CAS(10,10) at every sampled geometry. 100% SA-CASSCF convergence was achieved for
both methods on all 52 single-geometry evaluations in the consolidated table.

Hardware (representative): Intel Core Ultra 7 255H (14 cores), PySCF 2.x.
```

**Publication date:**
```
2026-04-12
```

**Version:**
```
1.1.0
```

## License
```
Creative Commons Attribution 4.0 International (CC BY 4.0)
```

## Keywords
```
active space selection, CASSCF, SA-CASSCF, photochemistry, conical intersection,
torsion scan, multi-geometry optimization, state-averaged CASSCF, excited states,
fulvene, ethylene, butadiene, quantum chemistry, strongly correlated electrons,
bio-inspired optimization, inZOR-ND, combinatorial optimization, NOON-MP2, PySCF,
cc-pVDZ, S0/S1 gap, gap regularity, multi-reference methods, potential energy surface
```

## Related identifiers
```
Type: Is supplement to
Identifier: https://dumitrunovic-svg.github.io/inZOR-ND/tests/photochem_multi_geom_active_space/
Resource type: Software

Type: Is related to
Identifier: https://dumitrunovic-svg.github.io/inZOR-ND/tests/active_space_comparative/
Resource type: Publication / Preprint
Description: Comprehensive validation — 8 benchmarks on 6 molecular systems

Type: Is related to
Identifier: https://dumitrunovic-svg.github.io/inZOR-ND/tests/qc_gaps_h2_ethylene_unified/
Resource type: Publication / Preprint
Description: QC gaps — H2 & ethylene unified chapter (gap structure analysis)
```
