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
inZOR-ND: Photochemical Multi-Geometry Active Space Selection — Shared CAS Stability Across Torsion Scans (Ethylene, Butadiene, Fulvene)
```

**Authors:**
```
Novic, Dumitru
  Affiliation: Independent Researcher
  Email: dumitru.novic@gmail.com
```

**Description / Abstract:**
```
We test whether inZOR-ND (bio-adaptive discrete search engine) can discover a single
shared active space that remains valid across multiple torsion geometries in photochemically
challenging systems — including quasi-degenerate regions near conical intersections —
where canonical orbital selection rules (NOON-MP2) routinely fail.

The study covers three organic photochemical systems with SA-CASSCF(2 states, S0/S1),
all using the cc-pVDZ basis set:
  - Ethylene (C2H4): CAS(4e,4o), 16 torsion + pyramidalization geometries
  - 1,3-Butadiene (C4H6): CAS(4e,4o), 10 dihedral geometries (phi = 0°–180°)
  - Fulvene (C5H4=CH2): three CAS sizes — (6e,6o) / (8e,8o) / (10e,10o) — up to 12 tilt geometries

inZOR-ND is compared against NOON-MP2 (canonical MP2 natural orbital occupation numbers)
using identical SACASFitness evaluation with Procrustes MO alignment at the reference geometry.
The same engine configuration is used across all benchmarks without system-specific tuning.

Key results:
  - inZOR-ND outperforms NOON-MP2 on all 5 benchmark configurations (3 molecules × CAS sizes)
  - Ethylene: +0.04 kcal/mol energy advantage; dramatically better gap regularity
    (σ = 0.79 vs 1.18 eV; gap max = 2.79 vs 5.08 eV)
  - Butadiene: +4.45 kcal/mol advantage with 10/10 convergence
    (largest per-geom: 31.7 mHa at anti conformer phi=180°)
  - Fulvene CAS(6,6): +1.32 kcal/mol, 9/9 convergence
  - Fulvene CAS(8,8): +14.40 kcal/mol mean advantage, 5/5 angles
  - Fulvene CAS(10,10): +3.48 kcal/mol mean, 10/12 per-angle wins (12/12 convergence)
  - 100% convergence on all geometries for all inZOR-ND active spaces

The study demonstrates that standard NOON-MP2 selection is systematically suboptimal
for photochemical torsion scans, particularly at biradical or charge-transfer geometries
where MP2 1-RDM occupations are distorted by multi-reference effects.
inZOR-ND discovers non-canonical orbital mixtures with 0.01–1.68% coverage of the
combinatorial search space.

Hardware: Intel Core Ultra 7 255H (14 cores), 20 GB RAM, PySCF 2.x.
```

**Publication date:**
```
2026-04-11
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
active space selection, CASSCF, SA-CASSCF, photochemistry, conical intersection,
torsion scan, multi-geometry optimization, state-averaged CASSCF, excited states,
ethylene, butadiene, fulvene, quantum chemistry, strongly correlated electrons,
bio-inspired optimization, inZOR-ND, combinatorial optimization, NOON, PySCF,
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
